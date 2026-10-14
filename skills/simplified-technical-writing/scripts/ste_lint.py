#!/usr/bin/env python3
"""Check text for the mechanical STE rules: sentence length, semicolons,
contractions, and marketing words. Exit 1 when any issue is found."""

from __future__ import annotations

import argparse
import re
import sys

MARKETING_WORDS = (
    "seamless", "robust", "powerful", "cutting-edge", "effortless",
    "world-class", "next-generation", "revolutionary",
)
CONTRACTION = re.compile(
    r"\b(?:\w+(?:n't|'re|'ve|'ll|'d|'m)|(?:it|that|there|what|let|here|who)'s)\b",
    re.IGNORECASE,
)
SENTENCE_END = re.compile(r"(?<=[.!?])\s+")
CODE = re.compile(r"```.*?```|`[^`]*`", re.DOTALL)


def lint(text: str, max_words: int) -> list[str]:
    issues: list[str] = []
    prose = CODE.sub(" ", text)
    for number, line in enumerate(prose.splitlines(), start=1):
        if ";" in line:
            issues.append(f"line {number}: semicolon")
        for match in CONTRACTION.finditer(line):
            issues.append(f"line {number}: contraction '{match.group(0)}'")
        lowered = line.lower()
        for word in MARKETING_WORDS:
            if re.search(rf"\b{re.escape(word)}\b", lowered):
                issues.append(f"line {number}: marketing word '{word}'")
        for sentence in SENTENCE_END.split(line.strip()):
            count = len(sentence.split())
            if count > max_words:
                issues.append(
                    f"line {number}: {count} words (max {max_words}): {sentence[:60]}"
                )
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", help="File to check; reads stdin when omitted.")
    parser.add_argument("--strict", action="store_true", help="Use the 20-word cap.")
    args = parser.parse_args()
    text = (
        open(args.path, encoding="utf-8").read() if args.path else sys.stdin.read()
    )
    issues = lint(text, 20 if args.strict else 25)
    for issue in issues:
        print(issue)
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
