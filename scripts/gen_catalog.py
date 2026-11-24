#!/usr/bin/env python3
"""Generate the README catalog from skill metadata and existing purpose text."""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from pathlib import Path

from validate_skills import Diagnostic, MetadataError, read_interface, skill_directories

START = "<!-- skills-catalog:start -->"
END = "<!-- skills-catalog:end -->"
OVERRIDES = Path("scripts/catalog_purposes.json")


def catalog() -> str:
    overrides: dict[str, str] = json.loads(OVERRIDES.read_text(encoding="utf-8"))
    if not isinstance(overrides, dict) or any(
        not isinstance(value, str) or not value.strip() or "\n" in value
        for value in overrides.values()
    ):
        raise ValueError(f"{OVERRIDES.as_posix()}:1: Use a JSON object of skill names and one-line purposes.")

    rows = ["| Skill | Purpose |", "| :--- | :--- |"]
    for folder in skill_directories(Path("skills")):
        metadata = folder / "agents" / "openai.yaml"
        try:
            fields = read_interface(metadata.read_text(encoding="utf-8"))
        except MetadataError as error:
            raise ValueError(str(Diagnostic(metadata, error.line, str(error)))) from None
        name = folder.name
        purpose = overrides.pop(name, fields["short_description"].value).strip()
        if purpose[-1] not in ".!?":
            purpose += "."
        escaped = purpose.replace("|", r"\|")
        rows.append(f"| [{name}](skills/{name}/) | {escaped} |")
    if overrides:
        stale = ", ".join(sorted(overrides))
        raise ValueError(f"{OVERRIDES.as_posix()}:1: Remove catalog purposes for missing skills: {stale}.")
    return "\n".join(rows)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Report drift without rewriting README.md.")
    args = parser.parse_args(argv)
    readme = Path("README.md")
    try:
        original = readme.read_bytes().decode("utf-8")
        lines = original.splitlines(keepends=True)
        starts = [index for index, line in enumerate(lines) if line.rstrip("\r\n") == START]
        ends = [index for index, line in enumerate(lines) if line.rstrip("\r\n") == END]
        if len(starts) != 1 or len(ends) != 1 or starts[0] >= ends[0]:
            raise ValueError("README.md:1: Keep one ordered pair of skills-catalog markers.")
        start, end = starts[0], ends[0]
        newline = "\r\n" if lines[start].endswith("\r\n") else "\n"
        table = catalog().replace("\n", newline)
        generated = "".join(lines[:start + 1]) + table + newline + "".join(lines[end:])
        if generated == original:
            print("README.md catalog is current.")
            return 0
        if args.check:
            print(f"README.md:{start + 1}: Catalog is out of date. Run python scripts/gen_catalog.py and stage README.md with the skill changes.")
            return 1
        readme.write_bytes(generated.encode("utf-8"))
        print("Updated the README.md catalog.")
    except (OSError, ValueError) as error:
        print(error)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
