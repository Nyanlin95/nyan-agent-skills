#!/usr/bin/env python3
"""Run and monitor a bounded OpenCode implementation task."""

from __future__ import annotations

import argparse
import json
import os
import queue
import shutil
import subprocess
import sys
import threading
import time
from pathlib import Path
from typing import TextIO


DEFAULT_MODEL = "opencode/deepseek-v4-flash-free"
BOUNDED_AGENT = "bounded-delegate"

EXIT_CONFIGURATION = 2
EXIT_QUOTA = 20
EXIT_RATE_LIMIT = 21
EXIT_AUTHENTICATION = 22
EXIT_IDLE_TIMEOUT = 23
EXIT_TOTAL_TIMEOUT = 24
EXIT_INCOMPLETE = 25
EXIT_FAILED = 26
EXIT_INTERRUPTED = 130


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run and monitor a bounded task through an OpenCode model."
    )
    parser.add_argument("--prompt", required=True, help="Task prompt for OpenCode.")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--cwd", type=Path, default=Path.cwd())
    parser.add_argument(
        "--allow-path",
        action="append",
        required=True,
        dest="allowed_paths",
        help="Relative file or folder that OpenCode can edit. Repeat as needed.",
    )
    parser.add_argument(
        "--allow-command",
        action="append",
        default=[],
        dest="allowed_commands",
        help="OpenCode bash permission pattern. Repeat as needed.",
    )
    parser.add_argument(
        "--file",
        action="append",
        default=[],
        dest="files",
        help="Explicit file to attach. Repeat for multiple files.",
    )
    parser.add_argument(
        "--format",
        choices=("default", "json"),
        default="default",
        dest="output_format",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=300,
        help="Maximum session duration in seconds.",
    )
    parser.add_argument(
        "--idle-timeout",
        type=float,
        default=90,
        help="Maximum seconds without OpenCode output.",
    )
    parser.add_argument(
        "--allow-non-free",
        action="store_true",
        help="Allow a model whose ID does not end in '-free'.",
    )
    return parser.parse_args()


def emit_status(status: str, **fields: object) -> None:
    payload = {"status": status, **fields}
    print(
        f"OPENCODE_STATUS={json.dumps(payload, separators=(',', ':'))}",
        file=sys.stderr,
        flush=True,
    )


def find_opencode() -> str:
    candidates = ("opencode.cmd", "opencode.exe", "opencode")
    for candidate in candidates:
        executable = shutil.which(candidate)
        if executable:
            return executable
    raise RuntimeError("OpenCode CLI is not installed or is not on PATH.")


def build_permissions(
    cwd: Path,
    allowed_paths: list[str],
    allowed_commands: list[str],
) -> tuple[dict[str, object], list[str]]:
    edit_rules: dict[str, str] = {"*": "deny"}
    normalized_paths: list[str] = []

    for supplied_path in allowed_paths:
        relative = Path(supplied_path)
        if relative.is_absolute() or ".." in relative.parts:
            raise RuntimeError(
                f"Allowed paths must stay inside the working directory: {supplied_path}"
            )
        normalized = relative.as_posix().strip("/")
        if not normalized or normalized == ".":
            raise RuntimeError("Do not allow the whole working directory.")

        resolved = (cwd / relative).resolve()
        try:
            resolved.relative_to(cwd)
        except ValueError as error:
            raise RuntimeError(
                f"Allowed path escapes the working directory: {supplied_path}"
            ) from error

        normalized_paths.append(normalized)
        edit_rules[normalized] = "allow"
        if resolved.is_dir() or supplied_path.endswith(("/", "\\")):
            edit_rules[f"{normalized}/*"] = "allow"

    bash_rules: dict[str, str] = {"*": "deny"}
    for pattern in allowed_commands:
        if not pattern.strip():
            raise RuntimeError("Allowed command patterns cannot be empty.")
        bash_rules[pattern] = "allow"

    permissions: dict[str, object] = {
        "edit": edit_rules,
        "bash": bash_rules,
        "task": "deny",
        "external_directory": "deny",
        "webfetch": "deny",
        "websearch": "deny",
        "skill": "deny",
        "question": "deny",
    }
    return permissions, normalized_paths


def list_models(executable: str, provider: str) -> set[str]:
    try:
        result = subprocess.run(
            [executable, "models", provider],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
        )
    except subprocess.TimeoutExpired as error:
        raise RuntimeError("OpenCode model discovery timed out.") from error
    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(f"OpenCode model discovery failed: {message}")
    return {line.strip() for line in result.stdout.splitlines() if line.strip()}


def stream_reader(
    stream_name: str,
    stream: TextIO,
    events: queue.Queue[tuple[str, str | None]],
) -> None:
    try:
        for line in iter(stream.readline, ""):
            events.put((stream_name, line))
    finally:
        events.put((stream_name, None))
        stream.close()


def stop_process(process: subprocess.Popen[str]) -> None:
    if process.poll() is not None:
        return
    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=5)


def classify_failure(text: str) -> tuple[str, int]:
    normalized = text.lower()
    quota_markers = (
        "quota",
        "insufficient credit",
        "credit balance",
        "usage limit",
        "billing limit",
        "payment required",
        "status 402",
        "http 402",
    )
    rate_markers = (
        "rate limit",
        "too many requests",
        "status 429",
        "http 429",
    )
    auth_markers = (
        "unauthorized",
        "invalid api key",
        "authentication failed",
        "status 401",
        "http 401",
    )
    if any(marker in normalized for marker in quota_markers):
        return "quota_limited", EXIT_QUOTA
    if any(marker in normalized for marker in rate_markers):
        return "rate_limited", EXIT_RATE_LIMIT
    if any(marker in normalized for marker in auth_markers):
        return "authentication_failed", EXIT_AUTHENTICATION
    return "failed", EXIT_FAILED


def render_event(raw_line: str, output_format: str) -> dict[str, object] | None:
    stripped = raw_line.strip()
    try:
        event = json.loads(stripped)
    except json.JSONDecodeError:
        print(raw_line, end="", file=sys.stderr, flush=True)
        return None

    if not isinstance(event, dict):
        print(raw_line, end="", file=sys.stderr, flush=True)
        return None

    if output_format == "json":
        print(stripped, flush=True)
    elif event.get("type") == "text":
        part = event.get("part")
        if isinstance(part, dict):
            text = part.get("text")
            if isinstance(text, str):
                print(text, flush=True)
    return event


def run_monitored(
    command: list[str],
    environment: dict[str, str],
    output_format: str,
    timeout: float,
    idle_timeout: float,
    model: str,
) -> int:
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        bufsize=1,
        env=environment,
    )
    assert process.stdout is not None
    assert process.stderr is not None

    events: queue.Queue[tuple[str, str | None]] = queue.Queue()
    threads = [
        threading.Thread(
            target=stream_reader,
            args=("stdout", process.stdout, events),
            daemon=True,
        ),
        threading.Thread(
            target=stream_reader,
            args=("stderr", process.stderr, events),
            daemon=True,
        ),
    ]
    for thread in threads:
        thread.start()

    started = time.monotonic()
    last_activity = started
    closed_streams = 0
    evidence: list[str] = []
    session_id: str | None = None
    terminal_reason: str | None = None
    tokens: object = None
    cost: object = None
    forced_status: str | None = None
    forced_exit: int | None = None

    try:
        while closed_streams < 2 or process.poll() is None:
            now = time.monotonic()
            if now - started >= timeout:
                forced_status = "total_timeout"
                forced_exit = EXIT_TOTAL_TIMEOUT
                stop_process(process)
                break
            if now - last_activity >= idle_timeout:
                forced_status = "idle_timeout"
                forced_exit = EXIT_IDLE_TIMEOUT
                stop_process(process)
                break

            try:
                stream_name, line = events.get(timeout=0.25)
            except queue.Empty:
                continue

            if line is None:
                closed_streams += 1
                continue

            last_activity = time.monotonic()
            evidence.append(line)
            if sum(len(item) for item in evidence) > 65536:
                evidence = evidence[-100:]

            if stream_name == "stderr":
                print(line, end="", file=sys.stderr, flush=True)
                continue

            event = render_event(line, output_format)
            if not event:
                continue
            event_session = event.get("sessionID")
            if isinstance(event_session, str):
                session_id = event_session
            if event.get("type") == "step_finish":
                part = event.get("part")
                if isinstance(part, dict):
                    reason = part.get("reason")
                    if isinstance(reason, str):
                        terminal_reason = reason
                    tokens = part.get("tokens")
                    cost = part.get("cost")
    except KeyboardInterrupt:
        stop_process(process)
        emit_status(
            "interrupted",
            model=model,
            session_id=session_id,
            terminal_reason=terminal_reason,
        )
        return EXIT_INTERRUPTED
    finally:
        if process.poll() is None:
            stop_process(process)

    return_code = process.wait()
    elapsed = round(time.monotonic() - started, 3)
    common = {
        "model": model,
        "session_id": session_id,
        "terminal_reason": terminal_reason,
        "process_exit": return_code,
        "elapsed_seconds": elapsed,
    }

    if forced_status is not None and forced_exit is not None:
        emit_status(forced_status, **common)
        return forced_exit

    normal_reasons = {"stop", "end_turn", "completed"}
    if return_code == 0 and terminal_reason in normal_reasons:
        emit_status("completed", tokens=tokens, cost=cost, **common)
        return 0

    if return_code == 0:
        emit_status("incomplete", tokens=tokens, cost=cost, **common)
        return EXIT_INCOMPLETE

    failure_status, failure_exit = classify_failure("".join(evidence))
    emit_status(failure_status, **common)
    return failure_exit


def main() -> int:
    args = parse_args()
    if args.timeout <= 0 or args.idle_timeout <= 0:
        emit_status("configuration_error", reason="Timeouts must be positive.")
        return EXIT_CONFIGURATION

    cwd = args.cwd.expanduser().resolve()
    if not cwd.is_dir():
        emit_status(
            "configuration_error",
            reason=f"Working directory does not exist: {cwd}",
        )
        return EXIT_CONFIGURATION

    try:
        permissions, normalized_paths = build_permissions(
            cwd,
            args.allowed_paths,
            args.allowed_commands,
        )
    except RuntimeError as error:
        emit_status("configuration_error", reason=str(error))
        return EXIT_CONFIGURATION

    if "/" not in args.model:
        emit_status(
            "configuration_error",
            reason="Model must use the provider/model format.",
        )
        return EXIT_CONFIGURATION

    if not args.allow_non_free and not args.model.endswith("-free"):
        emit_status(
            "model_not_approved",
            model=args.model,
            reason="The model ID does not end in '-free'.",
        )
        return EXIT_CONFIGURATION

    try:
        executable = find_opencode()
        provider = args.model.split("/", 1)[0]
        models = list_models(executable, provider)
    except RuntimeError as error:
        emit_status("configuration_error", reason=str(error))
        return EXIT_CONFIGURATION

    if args.model not in models:
        free_models = sorted(model for model in models if model.endswith("-free"))
        emit_status(
            "model_unavailable",
            model=args.model,
            available_free_models=free_models,
        )
        return EXIT_CONFIGURATION

    command = [
        executable,
        "--pure",
        "run",
        "--model",
        args.model,
        "--format",
        "json",
        "--dir",
        str(cwd),
        "--agent",
        BOUNDED_AGENT,
    ]
    for file_path in args.files:
        command.extend(["--file", file_path])
    command.append(args.prompt)

    print(
        "Warning: free-model prompts and outputs can be retained for model improvement.",
        file=sys.stderr,
    )
    environment = os.environ.copy()
    environment["OPENCODE_CONFIG_CONTENT"] = json.dumps(
        {
            "agent": {
                BOUNDED_AGENT: {
                    "description": "Bounded implementation worker delegated by a coding agent.",
                    "mode": "primary",
                    "permission": permissions,
                }
            }
        }
    )
    print(
        f"Editable paths: {', '.join(normalized_paths)}",
        file=sys.stderr,
    )
    try:
        return run_monitored(
            command=command,
            environment=environment,
            output_format=args.output_format,
            timeout=args.timeout,
            idle_timeout=args.idle_timeout,
            model=args.model,
        )
    except OSError as error:
        emit_status("failed", model=args.model, reason=str(error))
        return EXIT_FAILED


if __name__ == "__main__":
    raise SystemExit(main())
