"""Parse the Markdown constructs used by the repository's link checker."""

from __future__ import annotations

import re
from bisect import bisect_right
from collections.abc import Iterator
from dataclasses import dataclass
from html import unescape
from html.parser import HTMLParser
from string import punctuation
from typing import Literal


def leading_spaces(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


# Destination and reference-definition grammar shared by the block and inline parsers.
LABEL_TEXT = r"(?:\\[!-~]|[^\[\]\\])"
MARKDOWN_ESCAPE = re.compile(r"\\([" + re.escape(punctuation) + r"])")
BARE_TEXT = r"(?:\\[!-~]|[^\x00-\x20\x7f()\\])"


def balanced_text(atom: str, opening: str, closing: str) -> str:
    # Keep CommonMark's balanced delimiters without unbounded recursion.
    before, after = re.escape(opening), re.escape(closing)
    contents = atom
    for _ in range(32):
        contents = rf"(?:{atom}|{before}{contents}*{after})"
    return contents + "*"


ANGLE_TEXT = r"(?:\\[!-~]|[^<>\r\n\\])*"
DESTINATION = rf"(?:<(?P<angle>{ANGLE_TEXT})>|(?P<bare>(?!<){balanced_text(BARE_TEXT, '(', ')')}))"
TITLE = r"""(?:\s+(?:"(?:\\[^\n]|[^"\\])*"|'(?:\\[^\n]|[^'\\])*'|\((?:\\[^\n]|[^()\\])*\)))?"""
LINK_TARGET = re.compile(r"\(\s*" + DESTINATION + TITLE + r"\s*\)")
LINK_DEFINITION = re.compile(
    rf"(?m)^ {{0,3}}\[(?!\^)(?P<reference>{LABEL_TEXT}+)\]:[ \t]*(?:\n[ \t]*)?"
    + DESTINATION + TITLE + r"[ \t]*(?=\n|$)"
)
REFERENCE_LABEL = re.compile(rf"{LABEL_TEXT}+")
REFERENCE_SUFFIX = re.compile(rf"\[(?P<reference>{LABEL_TEXT}*)\]")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
QUOTE = re.compile(r"^ {0,3}> ?")
LIST_ITEM = re.compile(r"^(?P<marker> {0,3}(?:[-+*]|(?P<number>[0-9]{1,9})[.)]))(?:(?P<gap> +)(?=\S)| *$)")
FOOTNOTE = re.compile(r"^ {0,3}\[\^[^\]\n]+\]:[ \t]*(.*)$")
ATX_HEADING = re.compile(r"^ {0,3}#{1,6}(?:[ \t]+(.*)|$)")
SETEXT_UNDERLINE = re.compile(r"^ {0,3}(?:=+|-+)[ \t]*$")
THEMATIC_BREAK = re.compile(r"^ {0,3}(?:(?:\* *){3,}|(?:- *){3,}|(?:_ *){3,})$")
TABLE_PIPE = re.compile(r"\\*\|")
TABLE_DELIMITER = re.compile(r":?-+:?")
BACKTICKS = re.compile(r"`+")
INLINE_START = re.compile(r"[\\`<!\[\]]")
RAW_HTML = re.compile(r"^ {0,3}<(pre|script|style|textarea)(?=[ \t>]|$)", re.I)
RAW_HTML_END = re.compile(r"</(?:pre|script|style|textarea)>", re.I)
HTML_BLANK_END = re.compile(r"^[ \t]*$")
BLOCK_HTML = re.compile(
    r"^ {0,3}</?(?:address|article|aside|base|basefont|blockquote|body|caption|center|col|colgroup|"
    r"dd|details|dialog|dir|div|dl|dt|fieldset|figcaption|figure|footer|form|frame|frameset|h[1-6]|head|"
    r"header|hr|html|iframe|legend|li|link|main|menu|menuitem|nav|noframes|ol|optgroup|option|p|param|"
    r"search|section|source|summary|table|tbody|td|tfoot|th|thead|title|tr|track|ul)(?=[ \t>]|/?>|$)",
    re.I,
)
HTML_TAG = r"""(?:</[A-Za-z][A-Za-z0-9-]*\s*>
    |<[A-Za-z][A-Za-z0-9-]*(?:\s+[A-Za-z_:][A-Za-z0-9_.:-]*
    (?:\s*=\s*(?:'[^']*'|"[^"]*"|[^\s"'=<>`]+))?)*\s*/?>)"""
STANDALONE_HTML = re.compile(r"^[ ]{0,3}" + HTML_TAG + r"[ \t]*$", re.X)
INLINE_HTML = re.compile(HTML_TAG + r"|<!--.*?-->|<\?.*?\?>|<!\[CDATA\[.*?\]\]>|<![A-Z][A-Z0-9]*\s+[^>]*>", re.X | re.S)
AUTOLINK = re.compile(r"<([A-Za-z][A-Za-z0-9+.-]{1,31}:[^<>\x00-\x20]*)>")
EMAIL_LINK = re.compile(r"<([A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*)>")
UNDERSCORE_EMPHASIS = re.compile(r"(?<![\w\\])(_{1,3})(?=\S)(.+?)(?<=\S)(?<!\\)\1(?!\w)")


@dataclass(frozen=True)
class Container:
    width: int | None
    list_marker: str | None = None


def continue_containers(line: str, containers: list[Container]) -> tuple[str, int]:
    """Strip the prefixes for existing blockquotes, list items, or footnotes."""
    for depth, container in enumerate(containers):
        width = container.width
        if width is None:
            quote = QUOTE.match(line)
            if not quote:
                return line, depth
            line = line[quote.end():]
        elif line.startswith(" " * width) or not line.strip():
            line = line[width:]
        else:
            return line, depth
    return line, len(containers)


def list_item(line: str, in_paragraph: bool) -> Container | None:
    if THEMATIC_BREAK.fullmatch(line):
        return None
    item = LIST_ITEM.match(line)
    if not item:
        return None
    gap = item["gap"] or ""
    if in_paragraph and (not gap or (item["number"] and int(item["number"]) != 1)):
        return None
    width = item.end() if 1 <= len(gap) <= 4 else item.end("marker") + 1
    return Container(width, item["marker"][-1])


def html_block_end(line: str, *, in_paragraph: bool) -> re.Pattern[str] | None:
    content = line.lstrip(" ")
    if len(line) - len(content) > 3:
        return None
    if content.startswith("<!--"):
        return re.compile(r"-->")
    if content.startswith("<?"):
        return re.compile(r"\?>")
    if content.startswith("<![CDATA["):
        return re.compile(r"\]\]>")
    if re.match(r"<![A-Z]", content, re.I):
        return re.compile(r">")
    if RAW_HTML.match(line):
        return RAW_HTML_END
    if BLOCK_HTML.match(line) or (not in_paragraph and STANDALONE_HTML.fullmatch(line)):
        return HTML_BLANK_END
    return None


def opening_fence(line: str) -> str | None:
    match = FENCE.match(line)
    if match and (match[1].startswith("~") or "`" not in match[2]):
        return match[1]
    return None


def lazy_paragraph_line(line: str, ending: Container) -> bool:
    item = list_item(line, in_paragraph=False)
    sibling = item is not None and item.list_marker == ending.list_marker
    return bool(line.strip()) and not (
        sibling or QUOTE.match(line) or FOOTNOTE.fullmatch(line) or list_item(line, in_paragraph=True)
        or ATX_HEADING.fullmatch(line) or SETEXT_UNDERLINE.fullmatch(line) or THEMATIC_BREAK.fullmatch(line)
        or opening_fence(line) or html_block_end(line, in_paragraph=True) is not None
    )


def open_containers(line: str, containers: list[Container], in_paragraph: bool) -> str:
    while True:
        quote = QUOTE.match(line)
        if quote:
            containers.append(Container(None))
            line = line[quote.end():]
            in_paragraph = False
            continue
        footnote = FOOTNOTE.fullmatch(line)
        if footnote:
            containers.append(Container(leading_spaces(line) + 4))
            return footnote[1]
        item = list_item(line, in_paragraph)
        if item is None or item.width is None:
            return line
        containers.append(item)
        line = line[item.width:]
        in_paragraph = False


def table_cells(line: str) -> list[str]:
    line = line.strip()
    cells: list[str] = []
    parts: list[str] = []
    start = 0
    first = last = -1
    for pipe in TABLE_PIPE.finditer(line):
        delimiter = pipe.end() - 1
        if (delimiter - pipe.start()) % 2:
            # GFM removes the pipe escape even in a code span inside a cell.
            parts.extend((line[start:delimiter - 1], "|"))
        else:
            parts.append(line[start:delimiter])
            cells.append("".join(parts).strip())
            parts.clear()
            if first == -1:
                first = delimiter
            last = delimiter
        start = pipe.end()
    parts.append(line[start:])
    cells.append("".join(parts).strip())
    if first == 0:
        cells.pop(0)
    if last == len(line) - 1 and last >= 0:
        cells.pop()
    return cells


def table_header(header: str, delimiter: str) -> list[str]:
    indent = leading_spaces(delimiter)
    if indent >= 4 or not delimiter[indent:].startswith(("-", ":", "|")):
        return []
    headings, alignments = table_cells(header), table_cells(delimiter)
    if len(headings) == len(alignments) and all(TABLE_DELIMITER.fullmatch(cell) for cell in alignments):
        return headings
    return []


@dataclass(frozen=True)
class MarkdownBlock:
    source: str
    line: int
    heading: bool = False
    definitions_allowed: bool = True
    raw_html: bool = False


def markdown_blocks(source: str) -> list[MarkdownBlock]:
    if source.startswith("---\n"):
        frontmatter_end = source.find("\n---\n", 3)
        if frontmatter_end >= 0 and re.search(r"(?m)^[a-z_][a-z0-9_-]*:(?:\s|$)", source[4:frontmatter_end]):
            prefix = source[:frontmatter_end + 5]
            source = "\n" * prefix.count("\n") + source[len(prefix):]
    blocks: list[MarkdownBlock] = []
    fence = ""
    html_end = None
    containers: list[Container] = []
    paragraph: list[str] = []
    paragraph_line = 1
    indented_code = False
    table_width = 0

    def finish_paragraph(*, heading: bool = False) -> None:
        if paragraph:
            blocks.append(MarkdownBlock("\n".join(paragraph), paragraph_line, heading))
            paragraph.clear()

    for number, line in enumerate(source.splitlines(), 1):
        content, depth = continue_containers(line.expandtabs(4), containers)
        if depth < len(containers) and paragraph and lazy_paragraph_line(content, containers[depth]):
            paragraph.append(content)
            continue
        if depth < len(containers):
            del containers[depth:]
            fence = ""
            finish_paragraph()
            html_end = None
            indented_code = False
            table_width = 0
        if fence:
            match = FENCE.match(content)
            if match and match[1].startswith(fence) and not match[2].strip():
                fence = ""
            continue
        if html_end is not None:
            if html_end is HTML_BLANK_END and html_end.fullmatch(content):
                html_end = None
            else:
                blocks.append(MarkdownBlock(content, number, definitions_allowed=False, raw_html=True))
                if html_end.search(content):
                    html_end = None
                continue
        content = open_containers(content, containers, bool(paragraph))
        if len(containers) > depth:
            finish_paragraph()
            indented_code = False
            table_width = 0
        if not content.strip():
            finish_paragraph()
            table_width = 0
            continue
        if leading_spaces(content) >= 4 and (indented_code or not paragraph):
            indented_code = True
            table_width = 0
            continue
        indented_code = False
        delimiter = opening_fence(content)
        if delimiter:
            fence = delimiter
            finish_paragraph()
            table_width = 0
            continue
        end = html_block_end(content, in_paragraph=bool(paragraph))
        if end is not None:
            html_end = None if end.search(content) else end
            finish_paragraph()
            table_width = 0
            blocks.append(MarkdownBlock(content, number, definitions_allowed=False, raw_html=True))
            continue
        heading = ATX_HEADING.fullmatch(content)
        if heading:
            finish_paragraph()
            table_width = 0
            title = re.sub(r"(?:^|[ \t]+)#+[ \t]*$", "", heading[1] or "")
            blocks.append(MarkdownBlock(title, number, heading=True, definitions_allowed=False))
        elif paragraph and SETEXT_UNDERLINE.fullmatch(content):
            finish_paragraph(heading=True)
        elif THEMATIC_BREAK.fullmatch(content):
            finish_paragraph()
            table_width = 0
        elif table_width:
            cells = table_cells(content)
            blocks.extend(MarkdownBlock(cell, number, definitions_allowed=False) for cell in cells[:table_width])
        elif paragraph and (cells := table_header(paragraph[-1], content)):
            paragraph.pop()
            finish_paragraph()
            blocks.extend(MarkdownBlock(cell, number - 1, definitions_allowed=False) for cell in cells)
            table_width = len(cells)
        else:
            if not paragraph:
                paragraph_line = number
            paragraph.append(content)
    finish_paragraph()
    return blocks


def definitions_at_start(source: str) -> Iterator[re.Match[str]]:
    position = 0
    while match := LINK_DEFINITION.match(source, position):
        if match["bare"] == "":
            break
        yield match
        position = match.end() + 1


def reference_key(label: str) -> str:
    return " ".join(MARKDOWN_ESCAPE.sub(r"\1", label).casefold().split())


def destination(match: re.Match[str]) -> str:
    value = match["angle"] if match["angle"] is not None else match["bare"]
    return MARKDOWN_ESCAPE.sub(r"\1", value)


@dataclass(frozen=True)
class Inline:
    kind: Literal["text", "literal", "html", "link", "image"]
    offset: int
    text: str = ""
    target: str | None = None
    children: tuple[Inline, ...] = ()


@dataclass
class Bracket:
    index: int
    offset: int
    label: int
    image: bool
    active: bool = True


def read_link(source: str, closing: int, opener: Bracket, references: set[str]) -> tuple[int, str | None] | None:
    if match := LINK_TARGET.match(source, closing + 1):
        return match.end(), destination(match)
    suffix = REFERENCE_SUFFIX.match(source, closing + 1)
    label = suffix["reference"] if suffix else ""
    if not label:
        label = source[opener.label:closing]
        if not REFERENCE_LABEL.fullmatch(label):
            return None
    if reference_key(label) in references:
        # The definition's destination is checked at its own source line.
        return (suffix.end() if suffix else closing + 1), None
    return None


def parse_inline(source: str, references: set[str]) -> list[Inline]:
    """Consume each construct before considering its contents as other syntax."""
    tokens: list[Inline] = []
    brackets: list[Bracket] = []
    runs: dict[int, list[int]] = {}
    for run in BACKTICKS.finditer(source):
        runs.setdefault(len(run[0]), []).append(run.start())

    position = 0
    while position < len(source):
        special = INLINE_START.search(source, position)
        start = special.start() if special else len(source)
        if start > position:
            tokens.append(Inline("text", position, source[position:start]))
        if special is None:
            break
        mark = special[0]
        position = start + 1

        if mark == "\\" and position < len(source) and source[position] in punctuation:
            tokens.append(Inline("literal", start, source[position]))
            position += 1
            continue

        if mark == "`":
            run = BACKTICKS.match(source, start)
            assert run is not None
            width = len(run[0])
            candidates = runs.get(width, [])
            following = bisect_right(candidates, start)
            position = run.end()
            if following < len(candidates):
                end = candidates[following]
                text = source[position:end].replace("\n", " ")
                if text.startswith(" ") and text.endswith(" ") and text.strip(" "):
                    text = text[1:-1]
                tokens.append(Inline("literal", start, text))
                position = end + width
            else:
                tokens.append(Inline("text", start, run[0]))
            continue

        if mark == "<":
            url, email = AUTOLINK.match(source, start), EMAIL_LINK.match(source, start)
            autolink = url or email
            if autolink:
                text = autolink[1]
                address = text if url else "mailto:" + text
                tokens.append(Inline("link", start, target=address, children=(Inline("literal", start, text),)))
                position = autolink.end()
                for opener in brackets:
                    if not opener.image:
                        opener.active = False
                continue
            if tag := INLINE_HTML.match(source, start):
                tokens.append(Inline("html", start, tag[0]))
                position = tag.end()
                continue

        if mark == "[" or source.startswith("![", start):
            image = mark == "!"
            position += int(image)
            brackets.append(Bracket(len(tokens), start, position, image))
            tokens.append(Inline("text", start, source[start:position]))
            continue

        if mark == "]" and brackets:
            opener = brackets.pop()
            if opener.active and (link := read_link(source, start, opener, references)) is not None:
                position, target = link
                content = tuple(tokens[opener.index + 1:])
                tokens[opener.index:] = [Inline("image" if opener.image else "link", opener.offset, target=target, children=content)]
                if not opener.image:
                    for earlier in brackets:
                        if not earlier.image:
                            earlier.active = False
                continue

        tokens.append(Inline("text", start, mark))
    return tokens


def walk_inline(tokens: list[Inline] | tuple[Inline, ...]) -> Iterator[Inline]:
    pending = list(reversed(tokens))
    while pending:
        token = pending.pop()
        yield token
        # Image children are alternate text. Links and HTML in them do not render as elements.
        if token.kind == "link":
            pending.extend(reversed(token.children))


def heading_text(tokens: list[Inline]) -> str:
    literals: list[str] = []
    parts: list[str] = []
    pending = list(reversed(tokens))
    while pending:
        token = pending.pop()
        if token.kind in {"link", "image"}:
            pending.extend(reversed(token.children))
        elif token.kind == "literal":
            parts.append(f"\0{len(literals)}\0")
            literals.append(token.text)
        elif token.kind == "text":
            parts.append(token.text)
    text = unescape(UNDERSCORE_EMPHASIS.sub(r"\2", "".join(parts)))
    return re.sub(r"\x00([0-9]+)\x00", lambda match: literals[int(match[1])], text)


class HtmlAnchors(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.names: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if value and (name == "id" or (tag == "a" and name == "name")):
                self.names.add(value)
        if tag == "textarea":
            self.set_cdata_mode(tag)


@dataclass(frozen=True)
class MarkdownDocument:
    links: tuple[tuple[str, int], ...]
    anchors: frozenset[str]


def parse_markdown(source: str) -> MarkdownDocument:
    source = source.replace("\0", "\ufffd")
    blocks = markdown_blocks(source)
    definitions = [tuple(definitions_at_start(block.source)) if block.definitions_allowed else () for block in blocks]
    references = {reference_key(match["reference"]) for group in definitions for match in group}
    links: list[tuple[str, int]] = []
    headings: list[str] = []
    html = HtmlAnchors()

    for block, group in zip(blocks, definitions):
        if block.raw_html:
            html.feed(block.source + "\n")
            continue
        for match in group:
            links.append((destination(match), block.line + block.source.count("\n", 0, match.start())))
        start = group[-1].end() + 1 if group else 0
        tokens = parse_inline(block.source[start:], references)
        for token in walk_inline(tokens):
            if token.target is not None:
                line = block.line + block.source.count("\n", 0, start + token.offset)
                links.append((token.target, line))
            if token.kind == "html":
                html.feed(token.text)
        if block.heading and tokens:
            headings.append(heading_text(tokens))

    html.close()
    anchors = html.names
    counts: dict[str, int] = {}
    for heading in headings:
        visible = " ".join(line.strip() for line in heading.splitlines())
        slug = re.sub(r"[^\w\- ]", "", visible.lower().strip()).replace(" ", "-")
        count = counts.get(slug, 0)
        anchor = f"{slug}-{count}" if count else slug
        while anchor in anchors:
            count += 1
            anchor = f"{slug}-{count}"
        anchors.add(anchor)
        counts[slug] = count + 1
    return MarkdownDocument(tuple(links), frozenset(anchors))
