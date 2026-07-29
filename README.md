# Nyan Agent Skills

A collection of focused Codex skills. Each skill is self-contained under `skills/` and can be installed or linked independently.

Released under the [MIT License](LICENSE).

## Skills

| Skill | Purpose |
| :--- | :--- |
| [nyan-ui-visual-review](skills/nyan-ui-visual-review/) | Review existing rendered interfaces, trace visual problems to systemic root causes, and produce or implement evidence-backed improvements. |

## Add a skill

1. Create `skills/<skill-name>/`.
2. Add a valid `SKILL.md` and `agents/openai.yaml`.
3. Keep detailed references and reusable scripts inside the skill folder.
4. Validate the skill.
5. Add one catalog entry above.

See `AGENTS.md` for the library conventions.
