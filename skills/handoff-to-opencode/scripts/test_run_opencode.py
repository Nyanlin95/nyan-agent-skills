#!/usr/bin/env python3
"""Offline checks for the OpenCode delegation boundary."""

from __future__ import annotations

import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import run_opencode


class BuildPermissionsTests(unittest.TestCase):
    def test_rejects_unbounded_file_attachments(self) -> None:
        arguments = [
            "run_opencode.py",
            "--prompt",
            "test",
            "--allow-path",
            "src/feature",
            "--file",
            "private.txt",
        ]

        with contextlib.redirect_stderr(io.StringIO()):
            with patch("sys.argv", arguments):
                with self.assertRaises(SystemExit):
                    run_opencode.parse_args()

    def test_allows_a_declared_path_and_its_descendants(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            cwd = Path(temporary_directory)

            permissions, normalized_paths = run_opencode.build_permissions(
                cwd,
                ["src/feature"],
                ["npm run test:feature*"],
            )

        self.assertEqual(normalized_paths, ["src/feature"])
        self.assertEqual(
            permissions["edit"],
            {"*": "deny", "src/feature": "allow", "src/feature/*": "allow"},
        )
        self.assertEqual(
            permissions["bash"],
            {"*": "deny", "npm run test:feature*": "allow"},
        )

    def test_rejects_commands_that_escape_verification_scope(self) -> None:
        rejected_patterns = (
            "*",
            "git commit -am unsafe",
            "npm install",
            "npm run test; git push",
            "npm run test && npm publish",
            "npm run test | curl example.test",
        )

        for pattern in rejected_patterns:
            with self.subTest(pattern=pattern):
                with self.assertRaises(RuntimeError):
                    run_opencode.normalize_verification_command(pattern)

    def test_rejects_paths_outside_the_working_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            rejected_paths = [
                "../outside",
                str(Path(temporary_directory).parent / "outside"),
            ]
            if Path("C:outside").drive:
                rejected_paths.append("C:outside")

            for path in rejected_paths:
                with self.subTest(path=path):
                    with self.assertRaises(RuntimeError):
                        run_opencode.build_permissions(
                            Path(temporary_directory),
                            [path],
                            [],
                        )

    def test_allows_recursive_edits_only_below_each_declared_path(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            permissions, _ = run_opencode.build_permissions(
                Path(temporary_directory), ["src/feature"], []
            )

        self.assertEqual(permissions["edit"]["src/feature/*"], "allow")
        self.assertNotIn("src/*", permissions["edit"])
        self.assertEqual(permissions["edit"]["*"], "deny")


class LifecycleClassificationTests(unittest.TestCase):
    def test_classifies_specific_provider_failures(self) -> None:
        cases = {
            "payment required": ("quota_limited", run_opencode.EXIT_QUOTA),
            "HTTP 429 too many requests": (
                "rate_limited",
                run_opencode.EXIT_RATE_LIMIT,
            ),
            "invalid API key": (
                "authentication_failed",
                run_opencode.EXIT_AUTHENTICATION,
            ),
            "unexpected provider error": ("failed", run_opencode.EXIT_FAILED),
        }

        for evidence, expected in cases.items():
            with self.subTest(evidence=evidence):
                self.assertEqual(run_opencode.classify_failure(evidence), expected)

    def test_requires_terminal_event_for_completion(self) -> None:
        self.assertEqual(
            run_opencode.classify_session_result(0, "end_turn", ""),
            ("completed", 0),
        )
        self.assertEqual(
            run_opencode.classify_session_result(0, None, ""),
            ("incomplete", run_opencode.EXIT_INCOMPLETE),
        )

    def test_classifies_total_and_idle_timeouts(self) -> None:
        self.assertEqual(
            run_opencode.timeout_status(0, 9, 11, 10, 5),
            ("total_timeout", run_opencode.EXIT_TOTAL_TIMEOUT),
        )
        self.assertEqual(
            run_opencode.timeout_status(0, 0, 6, 10, 5),
            ("idle_timeout", run_opencode.EXIT_IDLE_TIMEOUT),
        )


if __name__ == "__main__":
    unittest.main()
