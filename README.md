# Nyan Agent Skills

Independent Codex skills for implementation quality, CQT code review, and evidence-based UI visual review. Each skill is self-contained under `skills/` and can be installed or linked independently.

Released under the [MIT License](LICENSE).

## Skills

| Skill | Purpose |
| :--- | :--- |
| [cqt-review](skills/cqt-review/) | Review code and migrations for correctness, quality, taste, ownership, dependencies, state, and failure behavior. |
| [implementation-quality](skills/implementation-quality/) | Keep implementation and ownership migrations simple, readable, correctly owned, and free of accidental complexity. |
| [nyan-ui-visual-review](skills/nyan-ui-visual-review/) | Review rendered interfaces through bounded, evidence-backed domain coverage, systemic findings, targeted improvements, and a clear verdict. |
| [opencode-cli](skills/opencode-cli/) | Delegate limited implementation work to a live OpenCode model within explicit file or folder paths. |

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
