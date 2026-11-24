"""Check the trigger example inventory and its wording against the skill descriptions."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

from scripts.validate_skills import read_frontmatter

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = Path(__file__).with_name("trigger_examples.json")


def contains(text: str, keywords: list[str]) -> bool:
    normalized = " ".join(text.split())
    return all(re.search(rf"(?<!\w){re.escape(keyword)}(?!\w)", normalized, re.I) for keyword in keywords)


def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate key {key!r}")
        result[key] = value
    return result


class SkillTriggerTests(unittest.TestCase):
    def test_trigger_examples_cover_each_skill_and_match_its_description(self) -> None:
        try:
            examples = json.loads(EXAMPLES.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
        except (OSError, ValueError) as error:
            self.fail(f"{EXAMPLES.name}: {error}")

        descriptions = {
            path.parent.name: read_frontmatter(path.read_text(encoding="utf-8"))["description"].value
            for path in sorted((ROOT / "skills").glob("*/SKILL.md"))
        }
        self.assertIsInstance(examples, dict, f"{EXAMPLES.name} must be an object keyed by skill name")
        self.assertSetEqual(set(examples), set(descriptions), f"{EXAMPLES.name} must cover every skill")
        for target, cases in examples.items():
            with self.subTest(skill=target):
                self.assertIsInstance(cases, dict)
                self.assertSetEqual(set(cases), {"should_trigger", "should_not_trigger"})
                seen_prompts: set[str] = set()
                for expectation, example in cases.items():
                    with self.subTest(case=expectation):
                        prompt = self.check_example(target, expectation, example, descriptions)
                        normalized = " ".join(prompt.casefold().split())
                        self.assertNotIn(normalized, seen_prompts, "positive and near-miss prompts must differ")
                        seen_prompts.add(normalized)

    def check_example(self, target: str, expectation: str, example: object, descriptions: dict[str, str]) -> str:
        negative = expectation == "should_not_trigger"
        fields = {"prompt", "keywords", "instead"} if negative else {"prompt", "keywords"}
        self.assertIsInstance(example, dict)
        self.assertSetEqual(set(example), fields)
        prompt = example["prompt"]
        keywords = example["keywords"]
        self.assertTrue(isinstance(prompt, str) and prompt.strip(), "prompt must be non-empty text")
        self.assertTrue(
            isinstance(keywords, list) and keywords
            and all(isinstance(word, str) and word.strip() for word in keywords),
            "keywords must be a non-empty list of non-empty strings",
        )

        expected = target
        if negative:
            expected = example["instead"]
            self.assertIsInstance(expected, str, "instead must be a skill name")
            self.assertIn(expected, descriptions, f"unknown alternate skill {expected!r}")
            self.assertNotEqual(expected, target, "the alternate skill must differ from the target")

        missing = [keyword for keyword in keywords if not contains(prompt, [keyword])]
        self.assertFalse(missing, f"phrases missing from prompt: {missing!r}")
        matches = {name for name, description in descriptions.items() if contains(description, keywords)}
        self.assertSetEqual(matches, {expected}, f"phrases {keywords!r} should match only {expected!r}")
        return prompt
