from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

from scripts.validate_skills import read_frontmatter

ROOT = Path(__file__).resolve().parents[1]


def contains(text: str, keywords: list[str]) -> bool:
    normalized = " ".join(text.split())
    return all(re.search(rf"(?<!\w){re.escape(keyword)}(?!\w)", normalized, re.I) for keyword in keywords)


class SkillTriggerTests(unittest.TestCase):
    def test_examples_match_only_the_intended_trigger_phrases(self) -> None:
        examples = json.loads(Path(__file__).with_name("trigger_examples.json").read_text(encoding="utf-8"))
        descriptions = {
            path.parent.name: read_frontmatter(path.read_text(encoding="utf-8"))["description"].value
            for path in (ROOT / "skills").glob("*/SKILL.md")
        }
        self.assertGreaterEqual(len(examples), 6)
        for target, cases in examples.items():
            self.assertIn(target, descriptions)
            for expectation in ("should_trigger", "should_not_trigger"):
                example = cases[expectation]
                with self.subTest(skill=target, expectation=expectation, prompt=example["prompt"]):
                    keywords = example["keywords"]
                    self.assertTrue(keywords)
                    self.assertTrue(contains(example["prompt"], keywords))
                    matches = {name for name, description in descriptions.items() if contains(description, keywords)}
                    if expectation == "should_trigger":
                        self.assertEqual(matches, {target})
                    else:
                        self.assertNotEqual(target, example["instead"])
                        self.assertEqual(matches, {example["instead"]})
