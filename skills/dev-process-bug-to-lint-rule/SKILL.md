---
name: dev-process-bug-to-lint-rule
description: >-
  Use when you just fixed or found a bug, a code-review nit, or an AI agent
  repeating a mistake, and want it to never happen again by turning it into an
  automated lint or check rule.
---

# Bug to lint rule

Part of the [Dev Process playbook](../dev-process-playbook/SKILL.md). Principle: every issue found becomes a rule the machine enforces, so the code base polices itself and the AI cannot repeat the mistake.

## When
- You fixed a bug and can name the pattern that caused it.
- A reviewer or agent flagged the same thing twice.
- A rule exists only in a doc or in your head.

## Steps
1. State the bad pattern in one sentence, as something a tool can detect (a banned call, a banned syntax shape, a missing field, a wrong import).
2. Write the smallest rule that catches it: ESLint custom rule, Roslyn analyzer (C#), ruff/flake8 plugin, semgrep pattern, or a plain grep in CI. Prefer semgrep or a grep when a full plugin is overkill.
3. Add a failing fixture (code that must be flagged) and a passing fixture (near-miss that must not be flagged).
4. Make the error message say the fix, not just the violation ("use MarketTime, not DateTime.UtcNow").
5. Run it over the whole repo, fix or explicitly allow-list existing hits, and wire it into CI so the build fails.
6. Log the rule in a `RULES.md` list: rule name, the bug it came from, the date.

## Good first rules
- Ban comments: if code needs explaining, rename it or write a test.
- Ban the wall clock where a domain clock exists.
- Ban allocation in hot paths (see [Context in file paths](../dev-process-context-in-file-paths/SKILL.md)).
- Ban empty catch blocks and swallowed errors.

## Ask the agent
"I just fixed <bug>. Write a lint rule that would have caught it, with one failing and one passing fixture, and wire it into CI."
