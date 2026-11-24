from __future__ import annotations

import unittest

from scripts.skill_markdown import parse_markdown


class MarkdownInlineTests(unittest.TestCase):
    def test_links_and_anchors_use_the_same_inline_boundaries(self) -> None:
        cases = (
            (
                "backticks in a link title",
                '[Docs](missing.md "Use a ` delimiter") and `example`.',
                ("missing.md",),
                set(),
            ),
            (
                "links and HTML in image alt text",
                '![Diagram <a id=phantom> [ignored](ignored.md)](diagram.png) [Jump](#phantom)',
                ("diagram.png", "#phantom"),
                set(),
            ),
            (
                "HTML and inline syntax in a link title",
                '[Jump](#ghost) [Docs](https://example.org/<version> "<a id=ghost> [ignored](ignored.md)")',
                ("#ghost", "https://example.org/<version>"),
                set(),
            ),
            (
                "brackets in a code span inside a link",
                '[A [B [C]] and `]`](example.md) <span id=real></span> [Jump](#real)',
                ("example.md", "#real"),
                {"real"},
            ),
            (
                "Markdown-shaped text in a raw attribute",
                '<span title="[ignored](ignored.md) and `quoted`" id=real>Text</span> [Jump](#real)',
                ("#real",),
                {"real"},
            ),
            (
                "a nested reference link suppresses the unrendered wrapper",
                "[See [guide][ref]](ignored.md)\n\n[ref]: real.md",
                ("real.md",),
                set(),
            ),
        )
        for name, source, destinations, anchors in cases:
            with self.subTest(name=name):
                document = parse_markdown(source)
                self.assertEqual(tuple(target for target, _ in document.links), destinations)
                self.assertEqual(document.anchors, anchors)

    def test_headings_keep_literal_code_and_ignore_link_titles(self) -> None:
        source = '## Use [`_sample_`](#real "An ` example") and _help_\n\n<a id=real></a>\n'
        document = parse_markdown(source)
        self.assertEqual(document.links, (("#real", 1),))
        self.assertEqual(document.anchors, {"real", "use-_sample_-and-help"})

    def test_gfm_tables_bound_inline_state_to_each_rendered_cell(self) -> None:
        source = (
            "| First | Second |\n| :--- | ---: |\n"
            "| ` example | [Visible](visible.md) ` |\n"
            "| [Example | Data](ignored.md) |\n"
            "| [Pipe \\| label](escaped.md) | [Second](second.md) | [Truncated](ignored.md) |\n"
            "[Short row](short.md)\n"
            "> [After the table](quote.md)\n"
        )
        self.assertEqual(parse_markdown(source).links, (
            ("visible.md", 3), ("escaped.md", 5), ("second.md", 5), ("short.md", 6), ("quote.md", 7),
        ))

    def test_gfm_single_column_table_starts_after_preceding_prose(self) -> None:
        source = "[Intro](intro.md)\nOnly column\n| --- |\n| [Shown](shown.md) | [Trimmed](ignored.md) |\n"
        self.assertEqual(parse_markdown(source).links, (("intro.md", 1), ("shown.md", 4)))

    def test_table_delimiter_indentation_and_pipe_free_alignment(self) -> None:
        for delimiter in (":---", ":---:", "---:"):
            with self.subTest(delimiter=delimiter):
                source = f"Column\n{delimiter}\n| [Shown](shown.md) | [Trimmed](ignored.md) |\n"
                self.assertEqual(parse_markdown(source).links, (("shown.md", 3),))

        source = "A | B\n    ---|---\n| A | B | [Still prose](shown.md) |\n"
        self.assertEqual(parse_markdown(source).links, (("shown.md", 3),))

    def test_raw_html_blocks_keep_rendered_anchors_and_ignore_literal_markdown(self) -> None:
        source = (
            '<!-- Marker --> <a id="same-line"></a>\n\n'
            '<!-- Multiline\n\n[Inside comment](ignored.md)\n--> <a id="closing-line"></a>\n\n'
            '<?example\n\n[Processing instruction](ignored.md)\n?>\n\n'
            '<![CDATA[\n\n[CDATA](ignored.md)\n]]>\n\n'
            '[First](#same-line) [Second](#closing-line)\n'
        )
        document = parse_markdown(source)
        self.assertEqual(document.links, (("#same-line", 18), ("#closing-line", 18)))
        self.assertEqual(document.anchors, {"same-line", "closing-line"})

    def test_gfm_raw_text_block_ends_at_any_eligible_closing_tag(self) -> None:
        source = '<pre id="example">\n[HTML text](ignored.md)\n</style>\n[Markdown](checked.md)\n'
        document = parse_markdown(source)
        self.assertEqual(document.links, (("checked.md", 4),))
        self.assertEqual(document.anchors, {"example"})
