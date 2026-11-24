from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("ste_lint.py")


class SteLintTests(unittest.TestCase):
    def lint(self, text: str, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            (sys.executable, str(SCRIPT), *arguments),
            input=text, capture_output=True, encoding="utf-8", check=False,
        )

    def test_ignores_code_in_clean_prose(self) -> None:
        result = self.lint("Run `tool --robust; check`.\n```\nIt's ignored;\n```\n")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(result.stdout, "")

    def test_reports_prose_issues_and_fails(self) -> None:
        result = self.lint("It's seamless; use it.\n")
        self.assertEqual(result.returncode, 1)
        self.assertIn("line 1: semicolon", result.stdout)
        self.assertIn("line 1: contraction 'It's'", result.stdout)
        self.assertIn("line 1: marketing word 'seamless'", result.stdout)

    def test_strict_mode_uses_the_twenty_word_cap(self) -> None:
        sentence = " ".join(["word"] * 21) + ".\n"
        self.assertEqual(self.lint(sentence).returncode, 0)
        strict = self.lint(sentence, "--strict")
        self.assertEqual(strict.returncode, 1)
        self.assertIn("line 1: 21 words (max 20)", strict.stdout)


if __name__ == "__main__":
    unittest.main()
