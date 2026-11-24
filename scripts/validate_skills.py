#!/usr/bin/env python3
"""Validate repository skills with Python 3.11+ and no third-party modules."""

from __future__ import annotations

import argparse
import json
import os
import re
from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from html import unescape
from pathlib import Path
from urllib.parse import unquote, urlsplit

if __package__:
    from .skill_markdown import parse_markdown
else:
    from skill_markdown import parse_markdown


DESCRIPTION_LIMIT = 1_024
SKILL_LINE_LIMIT = 500
SKILL_BYTE_LIMIT = 15 * 1_024
REFERENCE_BYTE_LIMIT = 25 * 1_024

NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
TRIGGER = re.compile(r"\b(?:use|apply|activate|trigger|select|invoke)\s+(?:when|for|to|if|on)\b", re.I)
REQUIRED_INTERFACE = ("display_name", "short_description", "default_prompt")
RESOURCE_FOLDERS = {"agents", "references", "scripts", "assets"}
YAML_KEY = re.compile(r"([a-z_][a-z0-9_-]*):(?:[ \t]+(.*))?\Z")
YAML_BLOCK = re.compile(r"([>|])([1-9][+-]?|[+-][1-9]?)?(?:\s+#.*)?\Z")
YAML_QUOTED = re.compile(r"'(?:[^']|'')*'" "|" r'"(?:[^"\\]|\\.)*"', re.S)
YAML_NON_STRING = re.compile(
    r"null|~|true|false|yes|no|on|off|[-+]?(?:\.inf|\.nan|0(?:x[0-9a-f_]+|o[0-7_]+|b[01_]+)"
    r"|(?:[0-9][0-9_]*(?:\.[0-9_]*)?|\.[0-9][0-9_]*)(?:e[-+]?[0-9]+)?"
    r"|[0-9][0-9_]*(?::[0-5]?[0-9])+(?:\.[0-9_]*)?)|[0-9]{4}-[0-9]{2}-[0-9]{2}"
    r"|[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}(?:[Tt]|[ \t]+)[0-9]{1,2}:[0-9]{2}:[0-9]{2}"
    r"(?:\.[0-9]*)?(?:[ \t]*(?:Z|[-+][0-9]{1,2}(?::[0-9]{2})?))?",
    re.I,
)


@dataclass(frozen=True)
class Field:
    value: str
    line: int


class MetadataError(ValueError):
    def __init__(self, line: int, message: str) -> None:
        super().__init__(message)
        self.line = line


def without_yaml_comment(value: str) -> str:
    return re.split(r"(?:^|\s+)#", value, maxsplit=1)[0].rstrip()


def scalar(value: str, line: int, *, require_string: bool) -> str:
    """Read the plain and quoted string forms used by the repository."""
    if value.startswith('"'):
        try:
            decoded, end = json.JSONDecoder().raw_decode(value)
        except json.JSONDecodeError:
            raise MetadataError(line, "Use a valid double-quoted string.") from None
    elif value.startswith("'"):
        match = re.match(r"'((?:[^']|'')*)'", value)
        if not match:
            raise MetadataError(line, "Close the single-quoted string.")
        decoded, end = match[1].replace("''", "'"), match.end()
    else:
        decoded = without_yaml_comment(value)
        if (
            decoded.startswith(("[", "]", "{", "}", ",", "&", "*", "!", "@", "`", "|", ">", "%"))
            or re.match(r"^[-?](?:\s|$)", decoded)
            or re.search(r":(?:\s|$)", decoded)
            or (require_string and YAML_NON_STRING.fullmatch(decoded))
        ):
            raise MetadataError(line, "Use a string value. Quote YAML punctuation or reserved values.")
        return decoded
    remainder = value[end:]
    if remainder.strip() and not re.fullmatch(r"\s+#.*", remainder):
        raise MetadataError(line, "Put only a comment after the closing quote.")
    return decoded


def fold_block_lines(lines: list[str]) -> str:
    filled = [(index, value) for index, value in enumerate(lines) if value]
    if not filled:
        return ""
    first, value = filled[0]
    parts = ["\n" * first, value]
    for (previous, before), (current, after) in zip(filled, filled[1:]):
        distance = current - previous
        if before[0].isspace() or after[0].isspace():
            separator = "\n" * distance
        else:
            separator = "\n" * (distance - 1) if distance > 1 else " "
        parts.extend((separator, after))
    return "".join(parts)


def block_scalar(style: str, lines: list[str], line: int, indent: int, hint: str) -> str:
    first = next((index for index, part in enumerate(lines) if part.strip()), len(lines))
    digit = hint.strip("+-")
    width = indent + int(digit) if digit else max(indent + 1, leading_spaces(lines[first]) if first < len(lines) else 0)
    if not digit and first < len(lines):
        for index, part in enumerate(lines[:first]):
            if leading_spaces(part) > width:
                raise MetadataError(line + index + 1, "Keep leading blank lines within the block string indentation.")
    content: list[str] = []
    for index, part in enumerate(lines):
        if part.strip() and leading_spaces(part) < width:
            if yaml_content(part):
                raise MetadataError(line + index + 1, "Align the indented lines of the block string.")
            stray = first_yaml_line(lines[index + 1:], line + index + 2)
            if stray:
                raise MetadataError(stray[1], "Remove the extra text after the block string.")
            break
        content.append(part[width:])
    raw = "".join(part + "\n" for part in content)
    value = raw.rstrip("\n")
    trailing = raw[len(value):]
    if style == ">":
        value = fold_block_lines(value.split("\n"))
    if "+" in hint:
        return value + trailing
    if "-" not in hint and value:
        return value + trailing[:1]
    return value


def yaml_content(line: str) -> bool:
    return bool(line.strip()) and not line.lstrip().startswith("#")


def leading_spaces(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


@dataclass(frozen=True)
class YamlEntry:
    value: str
    line: int
    indent: int
    following: list[str]


def yaml_nodes(lines: list[str], start: int, indent: int) -> Iterator[YamlEntry]:
    index = 0
    while index < len(lines):
        raw = lines[index]
        line = index + start
        index += 1
        if not yaml_content(raw):
            continue
        if leading_spaces(raw) != indent:
            raise MetadataError(line, "Align this YAML item with the other items at this level.")
        first = index
        while index < len(lines) and (not yaml_content(lines[index]) or leading_spaces(lines[index]) > indent):
            index += 1
        yield YamlEntry(raw[indent:].rstrip(), line, indent, lines[first:index])


def yaml_mapping(lines: list[str], start: int, indent: int) -> dict[str, YamlEntry]:
    result: dict[str, YamlEntry] = {}
    for node in yaml_nodes(lines, start, indent):
        match = YAML_KEY.fullmatch(node.value)
        if not match:
            raise MetadataError(node.line, "Use a key: value entry at this level.")
        key = match[1]
        if key in result:
            raise MetadataError(node.line, f"Keep a single '{key}' entry.")
        result[key] = YamlEntry((match[2] or "").strip(), node.line, indent, node.following)
    return result


def check_value_tail(source: str, end: int, start: int, kind: str) -> None:
    line_tail, _, following = source[end:].partition("\n")
    line = start + source.count("\n", 0, end)
    if line_tail.strip() and not re.fullmatch(r"\s+#.*", line_tail) and not (end == 0 and line_tail.startswith("#")):
        raise MetadataError(line, f"Keep one {kind} and an optional comment.")
    stray = first_yaml_line(following.splitlines(), line + 1)
    if stray:
        raise MetadataError(stray[1], f"Remove the extra text after the {kind}.")


def yaml_scalar(entry: YamlEntry, *, require_string: bool = True) -> str:
    style = YAML_BLOCK.fullmatch(entry.value)
    if style:
        return block_scalar(style[1], entry.following, entry.line, entry.indent, style[2] or "")
    lines = [entry.value, *(line.strip() for line in entry.following)]
    first_index = next((index for index, line in enumerate(lines) if yaml_content(line)), len(lines))
    rest = lines[first_index:]
    start = entry.line + first_index
    if rest and rest[0].startswith(("'", '"')):
        source = "\n".join(rest)
        quoted = YAML_QUOTED.match(source)
        if quoted is None:
            raise MetadataError(start, "Close the quoted string.")
        check_value_tail(source, quoted.end(), start, "quoted string")
        combined = fold_block_lines(quoted[0].split("\n"))
        if combined.startswith('"'):
            combined = combined.replace("\n", r"\n")
    else:
        parts: list[str] = []
        for index, line in enumerate(rest):
            part = without_yaml_comment(line)
            parts.append(part)
            if part != line:
                check_value_tail("\n".join(rest[index:]), len(part), start + index, "plain value")
                break
        combined = fold_block_lines(parts).strip()
    return scalar(combined, entry.line, require_string=require_string)


def first_yaml_line(lines: list[str], start: int) -> tuple[str, int] | None:
    return next(((line, number) for number, line in enumerate(lines, start) if yaml_content(line)), None)


def optional_yaml(entry: YamlEntry) -> None:
    """Check optional block mappings and sequences without imposing their schema."""
    first = first_yaml_line(entry.following, entry.line + 1)
    if not without_yaml_comment(entry.value) and first:
        first_line, number = first
        indent = leading_spaces(first_line)
        following = entry.following[number - entry.line - 1:]
        if re.match(r"-($|\s)", first_line[indent:]):
            for node in yaml_nodes(following, number, indent):
                item = re.fullmatch(r"-(?: +(.+))?", node.value)
                if not item:
                    raise MetadataError(node.line, "Start every item in this sequence with '-'.")
                value = item[1] or ""
                if YAML_KEY.fullmatch(value):
                    child_indent = indent + item.start(1)
                    child_lines = [" " * child_indent + value, *node.following]
                    for child in yaml_mapping(child_lines, node.line, child_indent).values():
                        optional_yaml(child)
                else:
                    optional_yaml(YamlEntry(value, node.line, indent, node.following))
        else:
            for child in yaml_mapping(following, number, indent).values():
                optional_yaml(child)
    elif entry.value.startswith(("[", "{")):
        flow = "\n".join([entry.value, *entry.following])

        def unique_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
            mapping: dict[str, object] = {}
            for key, value in pairs:
                if key in mapping:
                    raise MetadataError(entry.line, f"Keep a single '{key}' entry in this inline mapping.")
                mapping[key] = value
            return mapping

        try:
            _, end = json.JSONDecoder(object_pairs_hook=unique_keys).raw_decode(flow)
        except json.JSONDecodeError:
            raise MetadataError(entry.line, "Use a valid JSON-style collection or an indented YAML mapping or list.") from None
        check_value_tail(flow, end, entry.line, "collection")
    else:
        yaml_scalar(entry, require_string=False)


def required_field(key: str, entry: YamlEntry) -> Field:
    value = yaml_scalar(entry)
    if not value.strip():
        raise MetadataError(entry.line, f"Fill in '{key}' with a non-empty string.")
    return Field(value, entry.line)


def read_frontmatter(source: str) -> dict[str, Field]:
    lines = source.splitlines()
    if not lines or lines[0] != "---":
        raise MetadataError(1, "Start SKILL.md with a --- frontmatter delimiter.")
    try:
        end = lines.index("---", 1)
    except ValueError:
        raise MetadataError(1, "Close the frontmatter with --- on its own line.") from None
    entries = yaml_mapping(lines[1:end], 2, 0)
    for key, entry in entries.items():
        if key not in {"name", "description"}:
            raise MetadataError(entry.line, f"Remove '{key}'. Frontmatter allows only name and description.")
    for key in ("name", "description"):
        if key not in entries:
            raise MetadataError(1, f"Add '{key}' to the frontmatter.")
    return {key: required_field(key, entry) for key, entry in entries.items()}


def read_interface(source: str) -> dict[str, Field]:
    lines = source.splitlines()
    start = 1
    first = first_yaml_line(lines, start)
    if first and first[0] == "---":
        start = first[1] + 1
    end = next((index for index in range(start - 1, len(lines)) if lines[index] == "..."), len(lines))
    extra = first_yaml_line(lines[end + 1:], end + 2)
    if extra:
        raise MetadataError(extra[1], "Keep one YAML document in agents/openai.yaml.")
    entries = yaml_mapping(lines[start - 1:end], start, 0)
    interface = entries.pop("interface", None)
    if interface is None:
        raise MetadataError(1, "Add a top-level 'interface:' mapping.")
    if without_yaml_comment(interface.value):
        raise MetadataError(interface.line, "Put the interface fields on indented lines.")
    first = first_yaml_line(interface.following, interface.line + 1)
    indent = leading_spaces(first[0]) if first else 2
    fields = yaml_mapping(interface.following, interface.line + 1, indent)
    metadata: dict[str, Field] = {}
    for key in REQUIRED_INTERFACE:
        if key not in fields:
            raise MetadataError(interface.line, f"Add 'interface.{key}'.")
        metadata[key] = required_field(key, fields.pop(key))
        if key == "short_description" and len(metadata[key].value.strip().splitlines()) > 1:
            raise MetadataError(metadata[key].line, "Keep 'interface.short_description' on one line for the catalog.")
    for entry in [*entries.values(), *fields.values()]:
        optional_yaml(entry)
    return metadata


@dataclass(frozen=True)
class Diagnostic:
    path: Path
    line: int
    message: str
    warning: bool = False

    def __str__(self) -> str:
        level = "warning" if self.warning else "error"
        return f"{self.path.as_posix()}:{self.line}: {level}: {self.message}"


def exact_path(root: Path, parts: tuple[str, ...]) -> bool:
    folder = root
    for part in parts:
        if not any(child.name == part for child in folder.iterdir()):
            return False
        folder /= part
    return True


def lint_links(path: Path, source: str, repo: Path, references: Path | None) -> Iterator[Diagnostic]:
    document = parse_markdown(source)
    anchors = {path.resolve(): document.anchors}
    for destination, line in document.links:
        try:
            url = urlsplit(unescape(destination))
        except ValueError:
            yield Diagnostic(path, line, f"Fix the malformed link '{destination}'.")
            continue
        if url.scheme or url.netloc or not destination:
            continue
        relative = unquote(url.path)
        base = repo if relative.startswith("/") else path.parent
        try:
            spelled = Path(os.path.abspath(base / relative.lstrip("/") if relative else path))
            target = spelled.resolve()
        except (OSError, RuntimeError, ValueError):
            yield Diagnostic(path, line, f"Use a valid repository path instead of '{destination}'.")
            continue
        if "\\" in relative or not spelled.is_relative_to(repo) or not target.is_relative_to(repo):
            yield Diagnostic(path, line, f"Link to a repository path with forward slashes instead of '{destination}'.")
            continue
        if references and target.is_relative_to(references):
            if target.parent != references or target.is_dir():
                yield Diagnostic(path, line, f"Link directly to a file under references/ instead of '{destination}'.")
                continue
        try:
            exists = target.exists() and exact_path(repo, spelled.relative_to(repo).parts)
        except OSError:
            exists = False
        if not exists:
            yield Diagnostic(path, line, f"Link target '{destination}' is missing. Update the link or add its target.")
        elif url.fragment and target.suffix.lower() == ".md" and target.is_file():
            try:
                if target not in anchors:
                    anchors[target] = parse_markdown(target.read_text(encoding="utf-8")).anchors
                if unquote(url.fragment) not in anchors[target]:
                    yield Diagnostic(path, line, f"Anchor '{destination}' is missing. Use an existing heading or anchor.")
            except (OSError, UnicodeError):
                yield Diagnostic(path, line, f"Save the Markdown link target '{destination}' as readable UTF-8.")


def skill_directories(root: Path) -> list[Path]:
    return sorted(folder for folder in root.iterdir() if folder.is_dir())


def validate_skill(folder: Path, repo: Path) -> Iterator[Diagnostic]:
    if not folder.is_dir() or not folder.resolve().is_relative_to(repo):
        yield Diagnostic(folder, 1, "Select a skill directory inside this repository.")
        return
    if not NAME.fullmatch(folder.name):
        yield Diagnostic(folder, 1, "Use lowercase letters, digits, and single hyphens in the skill folder name.")
    for entry in sorted(folder.iterdir()):
        if entry.name == "SKILL.md" and entry.is_file():
            continue
        if entry.name in RESOURCE_FOLDERS and entry.is_dir():
            continue
        yield Diagnostic(entry, 1, "Keep only SKILL.md and the agents/, references/, scripts/, and assets/ folders here.")
    for entry in sorted(folder.rglob("*")):
        if entry.is_file() and entry.stem.lower() in {"readme", "changelog"}:
            yield Diagnostic(entry, 1, "Move README or CHANGELOG content to the library documentation.")

    entrypoint = folder / "SKILL.md"
    references = folder / "references"
    reference_files = sorted(path for path in references.glob("*") if path.is_file())
    for reference in reference_files:
        if reference.stat().st_size > REFERENCE_BYTE_LIMIT:
            yield Diagnostic(reference, 1, f"Trim or split this reference to about {REFERENCE_BYTE_LIMIT // 1024} KiB.", True)
    markdown_references = [path for path in reference_files if path.suffix.lower() == ".md"]
    for path in [entrypoint, *markdown_references]:
        try:
            data = path.read_bytes()
            source = data.decode("utf-8").replace("\r\n", "\n")
        except (OSError, UnicodeError):
            yield Diagnostic(path, 1, "Add this file or save it as readable UTF-8.")
            continue
        if path == entrypoint:
            try:
                metadata = read_frontmatter(source)
                name, description = metadata["name"], metadata["description"]
                if name.value != folder.name or not NAME.fullmatch(name.value):
                    yield Diagnostic(path, name.line, f"Set name to the lowercase hyphenated folder name '{folder.name}'.")
                if len(description.value) > DESCRIPTION_LIMIT:
                    yield Diagnostic(path, description.line, f"Shorten the description to about {DESCRIPTION_LIMIT} characters.", True)
                if not TRIGGER.search(description.value):
                    yield Diagnostic(path, description.line, "Add explicit trigger wording such as 'Use when ...'.", True)
            except MetadataError as error:
                yield Diagnostic(path, error.line, str(error))
            if len(data) > SKILL_BYTE_LIMIT or len(source.splitlines()) > SKILL_LINE_LIMIT:
                yield Diagnostic(path, 1, f"Keep SKILL.md within {SKILL_LINE_LIMIT} lines and {SKILL_BYTE_LIMIT // 1024} KiB by moving details to references/.", True)
        yield from lint_links(path, source, repo, references.resolve() if path == entrypoint else None)

    interface_file = folder / "agents" / "openai.yaml"
    try:
        if not exact_path(folder, ("agents", "openai.yaml")):
            raise FileNotFoundError
        interface = read_interface(interface_file.read_text(encoding="utf-8"))
    except (OSError, UnicodeError):
        yield Diagnostic(interface_file, 1, "Add a readable UTF-8 agents/openai.yaml with an interface mapping.")
        return
    except MetadataError as error:
        yield Diagnostic(interface_file, error.line, str(error))
        return
    title = interface["display_name"]
    name_words = set(folder.name.split("-"))
    title_words = re.findall(r"\w+", title.value.lower())
    # A display title can expand a compact slug word, such as "Hill Climb".
    title_variants = set(title_words) | {first + second for first, second in zip(title_words, title_words[1:])}
    if len(name_words & title_variants) < min(2, len(name_words)):
        yield Diagnostic(interface_file, title.line, f"Use a recognizable display name for '{folder.name}'.")
    prompt = interface["default_prompt"]
    if folder.name not in re.findall(r"\$([\w-]+)", prompt.value):
        yield Diagnostic(interface_file, prompt.line, f"Include the invocation ${folder.name} in default_prompt.")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skills", metavar="skills/<name>", nargs="*", type=Path)
    args = parser.parse_args(argv)
    try:
        folders = args.skills or skill_directories(Path("skills"))
    except OSError:
        folders = []
    if not folders:
        print(Diagnostic(Path("skills"), 1, "Run from the repository root with at least one skill under skills/."))
        return 1
    repo = Path.cwd().resolve()
    diagnostics: list[Diagnostic] = []
    for folder in folders:
        if folder.resolve().parent != repo / "skills":
            diagnostics.append(Diagnostic(folder, 1, "Select a direct child of this repository's skills/ directory."))
            continue
        diagnostics.extend(validate_skill(folder, repo))
    for diagnostic in diagnostics:
        print(diagnostic)
    warnings = sum(diagnostic.warning for diagnostic in diagnostics)
    errors = len(diagnostics) - warnings
    print(f"Checked {len(folders)} skill(s): {errors} error(s), {warnings} warning(s).")
    return int(errors > 0)


if __name__ == "__main__":
    raise SystemExit(main())
