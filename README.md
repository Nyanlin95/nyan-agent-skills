# Nyan Agent Skills

Independent Codex skills with natural-language triggers for code review, implementation quality, UI visual review, and bounded OpenCode delegation. Each skill is self-contained under `skills/`.

Released under the [MIT License](LICENSE).

## Trigger a skill

Codex can select an installed skill when your request matches its description. You do not need a special command.

Use a direct request:

| Request example | Skill that Codex can select |
| :--- | :--- |
| `Review this code for ownership, failure behavior, and migration risks.` | `cqt-review` |
| `Review this pull request beyond correctness.` | `cqt-review` |
| `Refactor this code without changing its behavior.` | `implementation-quality` |
| `Implement this feature with clear ownership and simple control flow.` | `implementation-quality` |
| `Review this rendered UI and list the visual problems.` | `nyan-ui-visual-review` |
| `Use OpenCode to implement this change only in src/auth/.` | `opencode-cli` |

Use the skill name when you must select one skill:

```text
Use $cqt-review to review this code.
Use $implementation-quality to refactor this code.
Use $nyan-ui-visual-review to review this screen.
Use $opencode-cli to implement this bounded task.
```

The skill must be installed where Codex can discover it. Codex reads the `description` in `SKILL.md` to decide when to select a skill.

One request can use more than one skill. For example, `Review this code, then refactor the accepted findings` can use `cqt-review` first and `implementation-quality` second.

## Skills

| Skill | Purpose |
| :--- | :--- |
| [cqt-review](skills/cqt-review/) | Review code and migrations for correctness, quality, taste, ownership, dependencies, state, and failure behavior. |
| [implementation-quality](skills/implementation-quality/) | Keep implementation and ownership migrations simple, readable, correctly owned, and free of accidental complexity. |
| [nyan-ui-visual-review](skills/nyan-ui-visual-review/) | Review rendered interfaces through bounded, evidence-backed domain coverage, systemic findings, targeted improvements, and a clear verdict. |
| [opencode-cli](skills/opencode-cli/) | Delegate limited implementation work to a live OpenCode model within explicit paths, with optional branch and pull-request delivery. |

## Library approach

- Keep implementation skills separate from review skills.
- Give each behavior, rule, and finding one canonical owner.
- Keep core workflows in `SKILL.md` and detailed checks in one-level references.
- Adapt external guidance to the owning skill instead of adding overlapping dependencies.
- Verify rendered behavior from rendered evidence.

## Add a skill

1. Create `skills/<skill-name>/`.
2. Add a valid `SKILL.md` and `agents/openai.yaml`.
3. Keep detailed references and reusable scripts inside the skill folder.
4. Validate the skill.
5. Add one catalog entry above.

See `AGENTS.md` for the library conventions.
