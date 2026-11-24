from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.validate_skills import read_frontmatter, read_interface

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "skills"
VALIDATOR = ROOT / "scripts" / "validate_skills.py"
GENERATOR = ROOT / "scripts" / "gen_catalog.py"


class SkillChecks(unittest.TestCase):
    def setUp(self) -> None:
        temp = tempfile.TemporaryDirectory(prefix="nyan-skills-tests-")
        self.addCleanup(temp.cleanup)
        self.repo = Path(temp.name)
        self.skills = self.repo / "skills"
        self.skills.mkdir()

    def copy_skill(self, name: str) -> Path:
        folder = self.skills / name
        shutil.copytree(FIXTURES / name, folder)
        return folder

    def command(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            args, cwd=self.repo, capture_output=True, encoding="utf-8", check=False,
            env={**os.environ, "PYTHONUTF8": "1"},
        )

    def validate(self, *paths: str) -> subprocess.CompletedProcess[str]:
        return self.command(sys.executable, str(VALIDATOR), *paths)

    def seed_catalog(self) -> None:
        (self.repo / "README.md").write_text(
            "Keep this header.\n\n<!-- skills-catalog:start -->\n"
            "<!-- skills-catalog:end -->\n\nKeep this footer.\n",
            encoding="utf-8",
        )
        (self.repo / "scripts").mkdir()
        (self.repo / "scripts" / "catalog_purposes.json").write_text("{}\n", encoding="utf-8")

    def test_scoped_cli_accepts_valid_skill_and_checks_all_by_default(self) -> None:
        self.copy_skill("sample-skill")
        self.copy_skill("broken-skill")
        scoped = self.validate("skills/sample-skill")
        self.assertEqual(scoped.returncode, 0, scoped.stdout + scoped.stderr)
        self.assertIn("Checked 1 skill(s): 0 error(s), 0 warning(s).", scoped.stdout)

        full = self.validate()
        self.assertEqual(full.returncode, 1)
        self.assertIn("SKILL.md:2: error: Set name", full.stdout)
        self.assertIn("SKILL.md:3: warning: Add explicit trigger wording", full.stdout)
        self.assertIn("SKILL.md:8: error: Link target 'references/missing.md' is missing", full.stdout)
        self.assertIn("references/README.md:1: error: Move README", full.stdout)
        self.assertIn("agents/openai.yaml:4: error: Include the invocation $broken-skill", full.stdout)
        self.assertIn("Checked 2 skill(s): 4 error(s), 1 warning(s).", full.stdout)

    def test_required_fields_and_folder_structure(self) -> None:
        folder = self.copy_skill("sample-skill")
        entry = folder / "SKILL.md"
        interface = folder / "agents" / "openai.yaml"
        (folder / "other.txt").touch()
        cases = (
            ("# Missing frontmatter", "SKILL.md:1: error: Start SKILL.md"),
            ("---\nname: sample-skill\ndescription: ''\n---\n", "SKILL.md:3: error: Fill in 'description'"),
            ("---\nname: sample-skill\ndescription: Use when needed.\nmetadata: discard\n---\n",
             "SKILL.md:4: error: Remove 'metadata'"),
            ("---\nname: sample-skill\nname: sample-skill\ndescription: Use when needed.\n---\n",
             "SKILL.md:3: error: Keep a single 'name'"),
            ("---\nname: sample-skill\ndescription:\n  - Use when needed.\n---\n",
             "SKILL.md:3: error: Use a string value."),
            ("---\nname: sample-skill\ndescription:\n  false\n---\n",
             "SKILL.md:3: error: Use a string value."),
            ('---\nname: sample-skill\ndescription: "Use when needed." # note\n  stray text\n---\n',
             "SKILL.md:4: error: Remove the extra text"),
            ("---\nname: sample-skill\ndescription: Use when ready. # note\n  stray text\n---\n",
             "SKILL.md:4: error: Remove the extra text"),
        )
        interface.write_text("interface:\n  display_name: Sample Skill\n", encoding="utf-8")
        for source, message in cases:
            with self.subTest(message=message):
                entry.write_text(source, encoding="utf-8")
                result = self.validate()
                self.assertEqual(result.returncode, 1)
                self.assertIn(message, result.stdout)
                self.assertIn("other.txt:1: error: Keep only SKILL.md", result.stdout)
                self.assertIn("agents/openai.yaml:1: error: Add 'interface.short_description'", result.stdout)
        interface.unlink()
        self.assertIn("agents/openai.yaml:1: error: Add a readable UTF-8", self.validate().stdout)

    def test_rejects_nested_references_and_missing_anchors(self) -> None:
        folder = self.copy_skill("sample-skill")
        nested = folder / "references" / "nested"
        nested.mkdir()
        (nested / "guide.md").touch()
        with (folder / "SKILL.md").open("a", encoding="utf-8") as file:
            file.write(
                "\n[Deep](references/nested/guide.md)\n[Anchor](#not-a-heading)\n"
                "[Missing](references/Missing(one(two)).md)\n"
            )
        result = self.validate()
        self.assertEqual(result.returncode, 1)
        self.assertIn("Link directly to a file under references/", result.stdout)
        self.assertIn("Anchor '#not-a-heading' is missing", result.stdout)
        self.assertIn("Link target 'references/Missing(one(two)).md' is missing", result.stdout)

    def test_rejects_links_with_incorrect_filename_or_directory_case(self) -> None:
        folder = self.copy_skill("sample-skill")
        with (folder / "SKILL.md").open("a", encoding="utf-8") as file:
            file.write("\n[Wrong file](references/a%20guide.md)\n[Wrong directory](References/A%20guide.md)\n")
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("Link target 'references/a%20guide.md' is missing", result.stdout)
        self.assertIn("Link target 'References/A%20guide.md' is missing", result.stdout)

    def test_wraps_plain_descriptions_and_accepts_explicit_block_indentation(self) -> None:
        folder = self.copy_skill("sample-skill")
        source = folder / "SKILL.md"
        for description in (
            "Validate a sample. Use\n  when checking a skill.",
            ">2-\n  Validate a sample. Use\n  when checking a skill.",
            '"Validate a sample. Use\n  when checking a skill." # note\n# A separate comment',
            "2026-11-24 release notes. Use when publishing.",
        ):
            with self.subTest(description=description):
                source.write_text(f"---\nname: sample-skill\ndescription: {description}\n---\n", encoding="utf-8")
                result = self.validate()
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn("0 error(s), 0 warning(s)", result.stdout)

    def test_block_scalars_preserve_chomping_and_stop_at_a_less_indented_comment(self) -> None:
        folder = self.copy_skill("sample-skill")
        source = folder / "SKILL.md"
        valid = "---\nname: |-\n  sample-skill\ndescription: |-\n  Use when checking skills.\n # End\n---\n"
        source.write_text(valid, encoding="utf-8")
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        source.write_text(valid.replace("name: |-", "name: |"), encoding="utf-8")
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("SKILL.md:2: error: Set name", result.stdout)

        source.write_text(valid.replace(" # End\n", "# End\n  stray text\n"), encoding="utf-8")
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("SKILL.md:7: error: Remove the extra text after the block string.", result.stdout)

        source.write_text(valid.replace("description: |-\n", "description: |-\n    \n"), encoding="utf-8")
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("SKILL.md:5: error: Keep leading blank lines within the block string indentation.", result.stdout)

    def test_folded_description_preserves_breaks_around_more_indented_lines(self) -> None:
        source = (
            "---\nname: sample-skill\ndescription: >-\n"
            "  Use when checking skills.\n    One detail\n  Continue.\n  Final line.\n---\n"
        )
        self.assertEqual(
            read_frontmatter(source)["description"].value,
            "Use when checking skills.\n  One detail\nContinue. Final line.",
        )

    def test_yaml_flow_scalars_preserve_paragraphs_and_prompts_can_span_lines(self) -> None:
        folder = self.copy_skill("sample-skill")
        interface = folder / "agents" / "openai.yaml"
        source = interface.read_text(encoding="utf-8")
        source = source.replace(
            '"Use $sample-skill to check this example."',
            "|-\n    Use $sample-skill to check this example.\n    Report the verification results.",
        )
        interface.write_text(source, encoding="utf-8")
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(
            read_interface(source)["default_prompt"].value,
            "Use $sample-skill to check this example.\nReport the verification results.",
        )
        self.seed_catalog()
        catalog = self.command(sys.executable, str(GENERATOR))
        self.assertEqual(catalog.returncode, 0, catalog.stdout + catalog.stderr)

        for description in ("First line\n\n    Second line", "'First line\n\n    Second line'", '"First line\n\n    Second line"'):
            with self.subTest(description=description):
                interface.write_text(source.replace("'Check a sample skill | with examples'", description), encoding="utf-8")
                result = self.validate()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn("openai.yaml:3: error: Keep 'interface.short_description' on one line", result.stdout)

    def test_rejects_non_string_yaml_and_invalid_optional_sections(self) -> None:
        folder = self.copy_skill("sample-skill")
        path = folder / "agents" / "openai.yaml"
        before = path.read_text(encoding="utf-8")
        for value in ("0x10", "1e3", ".inf", "2026-11-24", "2026-11-24 12:34:56Z", "\n    true", "\n    - An example"):
            with self.subTest(value=value):
                path.write_text(before.replace("'Check a sample skill | with examples'", value), encoding="utf-8")
                result = self.validate()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn("openai.yaml:3: error: Use a string value.", result.stdout)
        path.write_text(before + "trailing: [\n", encoding="utf-8")
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("openai.yaml:7: error: Use a valid JSON-style collection", result.stdout)

        path.write_text(before + "extras: [] # note\n  stray text\n", encoding="utf-8")
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("openai.yaml:8: error: Remove the extra text after the collection.", result.stdout)

        path.write_text(before + 'dependencies: {"tools": [], "tools": [{"type": "mcp"}]}\n', encoding="utf-8")
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("openai.yaml:7: error: Keep a single 'tools' entry", result.stdout)

        path.write_text(
            before + "dependencies:\n  tools:\n    - type: mcp\n      value: sample\n"
            'extra: [\n  "sample"\n  ] # An inline collection may span lines.\n',
            encoding="utf-8",
        )
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_link_anchors_use_rendered_heading_text(self) -> None:
        folder = self.copy_skill("sample-skill")
        with (folder / "SKILL.md").open("a", encoding="utf-8") as file:
            file.write(
                "\n## Use _sample_ files\n\n[Jump](#use-sample-files)\n\n"
                "## [Guide][ref]\n\n[ref]: #guide\n\n"
                "## Use [`_sample_`](#guide) files\n\n[Literal](#use-_sample_-files)\n"
            )
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_fences_respect_their_own_containers(self) -> None:
        folder = self.copy_skill("sample-skill")
        with (folder / "SKILL.md").open("a", encoding="utf-8") as file:
            file.write(
                "\n```md\n> [Ignored](inside-code.md)\n```\n\n"
                "[After root code](after-root-code.md)\n\n"
                "- Sample\n\n  ```md\n  [Ignored](inside-list-code.md)\n\n"
                "[After list code](after-list-code.md)\n\n"
                "1.  Sample\n\n    > [list-ref]: missing-quoted-list-ref.md\n    >\n    > [Look][list-ref]\n"
            )
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("Link target 'after-root-code.md' is missing", result.stdout)
        self.assertIn("Link target 'after-list-code.md' is missing", result.stdout)
        self.assertIn("Link target 'missing-quoted-list-ref.md' is missing", result.stdout)
        self.assertIn("3 error(s), 0 warning(s)", result.stdout)

    def test_checks_linked_images_and_links_with_escaped_titles(self) -> None:
        folder = self.copy_skill("sample-skill")
        with (folder / "SKILL.md").open("a", encoding="utf-8") as file:
            file.write('\n[![Screenshot](missing.png)](#sample-skill)\n\n')
            file.write(r'[Guide](missing.md "Read \"this\" first")' + "\n")
            file.write('[Title](#sample-skill "Literal [Example](ignored.md)")\n')
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("Link target 'missing.png' is missing", result.stdout)
        self.assertIn("Link target 'missing.md' is missing", result.stdout)
        self.assertIn("2 error(s), 0 warning(s)", result.stdout)

    def test_code_and_comments_hide_only_their_own_contents(self) -> None:
        folder = self.copy_skill("sample-skill")
        with (folder / "SKILL.md").open("a", encoding="utf-8") as file:
            file.write(
                "\n`<!--`\n\n[Between spans](missing-span.md)\n\n`-->`\n\n"
                "```html\n<!-- example\n```\n\n[After fence](missing-fence.md)\n\n"
                "<!--\n```md\n[Inside comment](ignored-comment.md)\n-->\n\n"
                "Check <!-- [Inside inline comment](ignored-inline.md) --> [After comment](missing-comment.md).\n"
            )
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        for destination in ("missing-span.md", "missing-fence.md", "missing-comment.md"):
            self.assertIn(f"Link target '{destination}' is missing", result.stdout)
        self.assertIn("3 error(s), 0 warning(s)", result.stdout)

    def test_setext_headings_respect_block_boundaries(self) -> None:
        folder = self.copy_skill("sample-skill")
        with (folder / "SKILL.md").open("a", encoding="utf-8") as file:
            file.write(
                "\n> Setup\n---\n\n## Setup\n\n[Wrong anchor](#setup-1)\n\n"
                "Longer\nheading\n=======\n    [Indented example](ignored.md)\n\n"
                "[Real heading](#longer-heading)\n"
            )
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("Anchor '#setup-1' is missing", result.stdout)
        self.assertIn("1 error(s), 0 warning(s)", result.stdout)

    def test_inline_links_and_definitions_respect_paragraph_boundaries(self) -> None:
        folder = self.copy_skill("sample-skill")
        with (folder / "SKILL.md").open("a", encoding="utf-8") as file:
            file.write(
                "\n# Heading `\n[After heading](missing-after-heading.md) `\n\n"
                '[Multiline title](missing-with-title.md "line one\nline two")\n\n'
                "Intro\n[not-a-definition]: ignored-prose.md\n\n"
                "[a real definition]:\n  missing-definition.md\n"
            )
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        for link in ("missing-after-heading.md", "missing-with-title.md", "missing-definition.md"):
            self.assertIn(f"Link target '{link}' is missing", result.stdout)
        self.assertIn("3 error(s), 0 warning(s)", result.stdout)

    def test_footnotes_and_empty_list_items_keep_their_containers(self) -> None:
        folder = self.copy_skill("sample-skill")
        with (folder / "SKILL.md").open("a", encoding="utf-8") as file:
            file.write(
                "\nRead both notes.[^1][^2]\n\n"
                "[^1]: This explains the example.\n\n"
                "[^2]: See the [source](missing-footnote.md).\n\n"
                "    See the [continuation](missing-footnote-continuation.md).\n\n"
                "-\n  ```md\n  [Code](ignored.md)\n\n[After list](missing-after-list.md)\n"
            )
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        for link in ("missing-footnote.md", "missing-footnote-continuation.md", "missing-after-list.md"):
            self.assertIn(f"Link target '{link}' is missing", result.stdout)
        self.assertIn("3 error(s), 0 warning(s)", result.stdout)

    def test_lazy_continuations_and_raw_html_follow_markdown_block_rules(self) -> None:
        folder = self.copy_skill("sample-skill")
        with (folder / "SKILL.md").open("a", encoding="utf-8") as file:
            file.write(
                "\n> Read the [installation\nguide](missing-lazy-link.md).\n\n"
                "Intro\n2. [note]: ignored-prose.md\n\n"
                '<pre class="example">\n[Example](ignored-raw-html.md)\n\n</PRE>\n\n'
                "[After raw HTML](missing-after-html.md)\n"
            )
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("Link target 'missing-lazy-link.md' is missing", result.stdout)
        self.assertIn("Link target 'missing-after-html.md' is missing", result.stdout)
        self.assertIn("2 error(s), 0 warning(s)", result.stdout)

    def test_numbered_list_siblings_open_independent_blocks(self) -> None:
        folder = self.copy_skill("sample-skill")
        (folder / "references" / "numbered.md").write_text(
            "1. First item\n2. ```text\n   [Example](ignored.md)\n   ```\n   [Real](missing-real.md)\n"
            "3. [more]: missing-definition.md\n\n   [Read][more]\n",
            encoding="utf-8",
        )
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("references/numbered.md:5: error: Link target 'missing-real.md' is missing", result.stdout)
        self.assertIn("references/numbered.md:6: error: Link target 'missing-definition.md' is missing", result.stdout)
        self.assertIn("2 error(s), 0 warning(s)", result.stdout)

    def test_raw_html_and_valid_escaped_or_nested_destinations(self) -> None:
        folder = self.copy_skill("sample-skill")
        (folder / "references" / "markup.md").write_text(
            "<details>\n<summary>Summary</summary>\n[Literal](ignored-html.md)\n</details>\n\n"
            "<details>\n<summary>Summary</summary>\n\n[Markdown](missing-inside-details.md)\n\n</details>\n\n"
            + chr(92) + "[Escaped brackets](ignored-escape.md)\n"
            + 2 * chr(92) + "[After a backslash](missing-escaped.md)\n"
            + "[Guide](absent(one(two(three))).md)\n",
            encoding="utf-8",
        )
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        for destination in ("missing-inside-details.md", "missing-escaped.md", "absent(one(two(three))).md"):
            self.assertIn(f"Link target '{destination}' is missing", result.stdout)
        self.assertIn("3 error(s), 0 warning(s)", result.stdout)

    def test_links_handle_punctuation_nested_labels_and_html_anchors(self) -> None:
        folder = self.copy_skill("sample-skill")
        (folder / "references" / "index_file.md").write_text("# Index\n", encoding="utf-8")
        (folder / "references" / "markup.md").write_text(
            r"[Index](index\_file.md)" + "\n\n"
            "[See [guide](missing-nested.md)](ignored-outer.md)\n\n"
            r"[guide\]]: missing-definition.md" + "\n\n" + r"[guide\]]" + "\n\n"
            '<a id="marker">\n[Literal](ignored-html.md)\n</a>\n\n[Anchor](#marker)\n\n'
            'Intro\n<a id="inline">\n[Real](missing-inline.md)\n</a>\n',
            encoding="utf-8",
        )
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        for destination in ("missing-nested.md", "missing-definition.md", "missing-inline.md"):
            self.assertIn(f"Link target '{destination}' is missing", result.stdout)
        self.assertIn("3 error(s), 0 warning(s)", result.stdout)

    def test_nested_reference_links_do_not_validate_unrendered_wrappers(self) -> None:
        folder = self.copy_skill("sample-skill")
        (folder / "references" / "nested-links.md").write_text(
            "# Example\n\n"
            "[See [guide][ref]](ignored-full.md)\n\n"
            "[See [guide]](ignored-shortcut.md)\n\n"
            "[See ![guide][ref]](missing-image-wrapper.md)\n\n"
            "[See [unknown]](missing-undefined-wrapper.md)\n\n"
            "[ref]: #example\n[guide]: #example\n",
            encoding="utf-8",
        )
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        for destination in ("missing-image-wrapper.md", "missing-undefined-wrapper.md"):
            self.assertIn(f"Link target '{destination}' is missing", result.stdout)
        self.assertIn("2 error(s), 0 warning(s)", result.stdout)

    def test_html_anchor_attributes_allow_spacing_and_unquoted_values(self) -> None:
        folder = self.copy_skill("sample-skill")
        (folder / "references" / "anchors.md").write_text(
            '<a id = "spaced"></a>\n\n<a id=unquoted></a>\n\n<a data-id="placeholder"></a>\n\n'
            "[Spaced](#spaced)\n[Unquoted](#unquoted)\n[Missing](#placeholder)\n",
            encoding="utf-8",
        )
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("Anchor '#placeholder' is missing", result.stdout)
        self.assertIn("1 error(s), 0 warning(s)", result.stdout)

    def test_html_anchors_are_extracted_only_from_rendered_elements(self) -> None:
        folder = self.copy_skill("sample-skill")
        (folder / "references" / "anchors.md").write_text(
            chr(92) + '<a id="escaped"></a>\n\n'
            + 2 * chr(92) + '<a id="rendered"></a>\n\n'
            '<pre id="real">Example</pre>\n\n'
            '<textarea id="field"><a id="text"></a></textarea>\n\n'
            '[Escaped](#escaped)\n[Rendered](#rendered)\n[Real](#real)\n[Field](#field)\n[Text](#text)\n'
            '[Title](#title "Example <a id=title>")\n'
            '[Angle](#angle) [Docs](https://example.org/<version> "<a id=angle>")\n'
            '[A [B [C]]](#real "<a id=nested>") [Nested](#nested)\n',
            encoding="utf-8",
        )
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        for anchor in ("#escaped", "#text", "#title", "#angle", "#nested"):
            self.assertIn(f"Anchor '{anchor}' is missing", result.stdout)
        self.assertIn("5 error(s), 0 warning(s)", result.stdout)

    def test_markdown_checks_prose_and_quoted_definitions_outside_indented_code(self) -> None:
        folder = self.copy_skill("sample-skill")
        with (folder / "SKILL.md").open("a", encoding="utf-8") as file:
            file.write(
                "\n## Install ###\n\n[Install](#install)\n\n"
                "    [Code](ignore-code.md)\n\n"
                "1.  Keep the definition in this list.\n\n"
                "    [List link](missing-list.md)\n\n"
                "> [ref]: missing-quote.md\n>\n> [Reference link][ref]\n"
            )
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("Link target 'missing-list.md' is missing", result.stdout)
        self.assertIn("Link target 'missing-quote.md' is missing", result.stdout)
        self.assertIn("2 error(s), 0 warning(s)", result.stdout)

    def test_rejects_an_unrelated_display_name(self) -> None:
        folder = self.copy_skill("sample-skill")
        interface = folder / "agents" / "openai.yaml"
        source = interface.read_text(encoding="utf-8")
        interface.write_text(source.replace("Sample Skill", "Unrelated Skill"), encoding="utf-8")
        result = self.validate()
        self.assertEqual(result.returncode, 1)
        self.assertIn("agents/openai.yaml:2: error: Use a recognizable display name", result.stdout)

    def test_size_diagnostics_leave_exit_status_zero(self) -> None:
        folder = self.copy_skill("sample-skill")
        entry = folder / "SKILL.md"
        entry.write_text(
            "---\nname: sample-skill\ndescription: Use when " + "x" * 1024 + "\n---\n"
            + "Example.\n" * 501, encoding="utf-8",
        )
        (folder / "references" / "large.txt").write_text("x" * (26 * 1024), encoding="utf-8")
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Shorten the description to about 1024 characters", result.stdout)
        self.assertIn("Keep SKILL.md within 500 lines and 15 KiB", result.stdout)
        self.assertIn("large.txt:1: warning: Trim or split", result.stdout)

    def test_catalog_detects_drift_and_preserves_text_outside_markers(self) -> None:
        self.copy_skill("sample-skill")
        self.seed_catalog()
        path = self.repo / "README.md"
        before = path.read_bytes()
        result = self.command(sys.executable, str(GENERATOR), "--check")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("Run python scripts/gen_catalog.py", result.stdout)
        self.assertEqual(path.read_bytes(), before)

        result = self.command(sys.executable, str(GENERATOR))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        generated = path.read_text(encoding="utf-8")
        self.assertTrue(generated.startswith("Keep this header.\n"))
        self.assertTrue(generated.endswith("\nKeep this footer.\n"))
        self.assertIn(r"| [sample-skill](skills/sample-skill/) | Check a sample skill \| with examples. |", generated)
        self.assertEqual(self.command(sys.executable, str(GENERATOR), "--check").returncode, 0)

    def test_hook_checks_index_even_when_working_tree_differs(self) -> None:
        folder = self.copy_skill("sample-skill")
        self.seed_catalog()
        for name in ("check.py", "gen_catalog.py", "skill_markdown.py", "validate_skills.py"):
            shutil.copyfile(ROOT / "scripts" / name, self.repo / "scripts" / name)
        hook = self.repo / ".githooks" / "pre-commit"
        hook.parent.mkdir()
        shutil.copyfile(ROOT / ".githooks" / hook.name, hook)
        hook.chmod(0o755)
        for args in (
            ("git", "init", "-q"),
            (sys.executable, str(GENERATOR)),
            ("git", "add", "README.md", "scripts", "skills"),
        ):
            result = self.command(*args)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        entry = folder / "SKILL.md"
        original = entry.read_text(encoding="utf-8")
        entry.write_text(original.replace("name: sample-skill", "name: wrong-skill"), encoding="utf-8")
        (self.skills / "untracked-skill").mkdir()
        launcher = self.repo / "scripts" / "check.py"
        launcher.write_text("raise SystemExit(1)\n", encoding="utf-8")
        run_hook = ("git", "-c", "core.hooksPath=.githooks", "hook", "run", "pre-commit")
        result = self.command(*run_hook)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        staged = self.command("git", "add", "skills/sample-skill/SKILL.md")
        self.assertEqual(staged.returncode, 0, staged.stderr)
        entry.write_text(original, encoding="utf-8")
        launcher.write_text("raise SystemExit(0)\n", encoding="utf-8")
        result = self.command(*run_hook)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("SKILL.md:2: error: Set name", result.stdout + result.stderr)

        readme = self.repo / "README.md"
        generated = readme.read_text(encoding="utf-8")
        readme.write_text(generated.replace("Check a sample skill", "Stale catalog row"), encoding="utf-8")
        staged = self.command("git", "add", "README.md", "skills/sample-skill/SKILL.md")
        self.assertEqual(staged.returncode, 0, staged.stderr)
        readme.write_text(generated, encoding="utf-8")
        result = self.command(*run_hook)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("Catalog is out of date", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
