# Nyan Agent Skills

This repository is a library of independent Codex skills.

## Library structure

- Store every skill at `skills/<skill-name>/`.
- Name the folder exactly as the `name` in `SKILL.md`.
- Keep reusable instructions in `SKILL.md`.
- Store optional resources only in `agents/`, `references/`, `scripts/`, or `assets/`.
- Do not add a README, changelog, or installation guide inside an individual skill.

## Skill requirements

- Use lowercase letters, digits, and hyphens for skill names.
- Include only `name` and `description` in YAML frontmatter.
- Put all trigger conditions in the frontmatter description.
- Write body instructions in imperative form.
- Write procedures and do-or-do-not lists as direct actions. Keep one action in each numbered step.
- Keep conceptual guidance flexible when the task needs judgment.
- Keep `SKILL.md` concise and use one-level references for detailed material.
- Add `agents/openai.yaml` with a display name, short description, and default prompt.
- Do not add dependencies unless the skill requires them.

## Ownership and refinement

- Give each skill one clear job. Do not mix implementation and review ownership.
- Keep orchestration, evidence rules, output rules, and completion checks in `SKILL.md`.
- Put detailed domain checks in a direct file under `references/`.
- Keep one canonical owner for each rule or finding. Report secondary effects without duplicating the rule.
- Synthesize useful external guidance into the owning skill. Do not add overlapping skills or dependencies without a clear need.
- Preserve repository and product conventions instead of importing universal style rules.
- For review skills, separate observed evidence from inference and state unavailable coverage.
- Use bounded findings. Do not add findings or rejected candidates only to meet a count.

## Validation

Run the skill validator after each material change:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "skills\<skill-name>"
```

Test scripts by running them. Verify rendered behavior against the actual artifact, not source code alone.

## Catalog maintenance

Add each skill to the root `README.md`. Describe its purpose in one sentence and link to its folder. Keep library-wide guidance here instead of copying it into every skill.
