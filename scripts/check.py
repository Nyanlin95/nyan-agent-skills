#!/usr/bin/env python3
"""Run the repository checks locally, in CI, or against the Git index."""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from collections.abc import Sequence
from pathlib import Path

# Git runs the hook from the worktree root when the launcher comes from the index.
ROOT = Path(__file__).resolve().parents[1] if "__file__" in globals() else Path.cwd()
METADATA_COMMANDS = (
    (sys.executable, "scripts/validate_skills.py"),
    (sys.executable, "scripts/gen_catalog.py", "--check"),
)


def run(command: Sequence[str], cwd: Path = ROOT) -> int:
    print(f"+ {' '.join(command)}", flush=True)
    return subprocess.run(command, cwd=cwd, check=False).returncode


def metadata_checks(root: Path) -> bool:
    return all([run(command, root) == 0 for command in METADATA_COMMANDS])


def test_checks() -> bool:
    suites = [ROOT / "tests"]
    suites.extend(sorted({
        test.parent for test in (ROOT / "skills").glob("*/scripts/test_*.py")
    }))
    results = [
        run((sys.executable, "-m", "unittest", "discover", "-s", suite.relative_to(ROOT).as_posix()))
        for suite in suites
    ]
    return all(result == 0 for result in results)


def staged_checks() -> bool:
    # Export the index without changing it. A full snapshot includes removed
    # skills and link targets, while excluding unstaged edits and untracked files.
    with tempfile.TemporaryDirectory(prefix="nyan-skills-index-") as directory:
        snapshot = Path(directory)
        command = ("git", "checkout-index", "--all", f"--prefix={snapshot.as_posix()}/")
        return run(command) == 0 and metadata_checks(snapshot)


def whitespace_checks(base: str | None) -> bool:
    if base is None:
        unstaged = run(("git", "diff", "--check"))
        staged = run(("git", "diff", "--cached", "--check"))
        return unstaged == staged == 0
    if base and set(base) == {"0"}:
        # A push that creates main has no previous commit.
        result = subprocess.run(
            ("git", "hash-object", "-t", "tree", "-w", "--stdin"),
            cwd=ROOT, input="", text=True, stdout=subprocess.PIPE, check=True,
        )
        base = result.stdout.strip()
    return run(("git", "diff", "--check", base, "HEAD", "--")) == 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--tests-only", action="store_true", help="Discover repository and skill script tests.")
    modes.add_argument("--staged", action="store_true", help="Check skill metadata and the catalog in the Git index.")
    modes.add_argument("--base", help="Check whitespace between this CI event base and HEAD.")
    args = parser.parse_args(argv)
    if args.staged:
        return int(not staged_checks())
    if args.tests_only:
        return int(not test_checks())
    metadata_ok = metadata_checks(ROOT)
    tests_ok = test_checks()
    whitespace_ok = whitespace_checks(args.base)
    return int(not (metadata_ok and tests_ok and whitespace_ok))


if __name__ == "__main__":
    raise SystemExit(main())
