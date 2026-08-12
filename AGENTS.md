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
$env:PYTHONUTF8 = '1'
py -3.14 "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "skills\<skill-name>"
```

Use `skills/<skill-name>/` as the canonical source. Treat global skill roots only as explicit installation or synchronization destinations. Do not edit an installed copy as the source of a repository skill.

Before finishing a skill edit:

1. Confirm `agents/openai.yaml` matches the skill's name, purpose, and default prompt.
2. Confirm the root `README.md` has one current catalog entry for the skill.
3. Confirm every detailed reference linked from `SKILL.md` is direct and one level deep.
4. Run the validator after the last material edit.
5. Run `git diff --check` on the cohesive change.

Test scripts by running them. Verify rendered behavior against the actual artifact, not source code alone.

## Catalog maintenance

Add each skill to the root `README.md`. Describe its purpose in one sentence and link to its folder. Keep library-wide guidance here instead of copying it into every skill.

## Skill-library orchestration

Use `skills-run:` as the short trigger for repository research, skill creation, skill improvement, validation, or synchronization.

- Keep the primary orchestrator on `gpt-5.6-sol` with medium reasoning. It plans, delegates bounded work, resolves conflicts, integrates changes, and owns final verification.
- Use `skill_implementer` as the default writer. It uses `gpt-5.6-terra` with high reasoning and owns assigned skill files plus their root catalog entries.
- Use `skill_researcher` for bounded repository or primary-source research.
- Use `history_analyst` to inspect installed coding-agent logs and memories for recurring failures and strong examples.
- Use `skill_reviewer` for independent review after material changes.
- Use `skill_syncer` only when the task explicitly includes installed-copy synchronization.
- Use `git_pr_manager` for feature-branch commits, ready PR creation, CI and review babysitting, and explicitly authorized merge.

Each specialist must read every skill assigned to its role or task and any directly related owner skill before acting. Treat the agent file as role identity and the skills as the owning procedures. Do not load unrelated skills only because they are available.

Keep one writer for each file. Parallelize read-only research and review, but do not let two agents edit the same skill or root catalog at the same time. The orchestrator must reconcile findings before assigning implementation.

Treat this repository as the canonical skill source. Extend an existing owner before creating a new skill. Create a skill only when it has an independent trigger, owner, workflow, and completion check.

The history analyst is read-only. It must discover installed applications before inspection, use app-owned indexes before raw sessions, bound its sample, exclude credential and personal-data stores, sanitize examples, and separate repeated patterns from isolated incidents. It must report unavailable coverage.

For a normal skill change, use this sequence:

1. Inspect the current owner, related skills, applicable evidence, and current Git state.
2. Research only the unresolved questions.
3. Assign one bounded implementation owner.
4. Run the skill validator and any changed scripts.
5. Run an independent skill review for material trigger, ownership, workflow, or safety changes.
6. Reconcile findings and rerun affected validation.
7. Synchronize exact repository-owned files only when the user requested sync.
8. Compare SHA-256 parity for synchronized files and exclude generated caches.
9. Inspect the cohesive diff and run `git diff --check`.

For publication, the orchestrator defines the intentional diff and delegates Git and GitHub state to `git_pr_manager`. Never push repository changes directly to `master`. `skills-run:full <task>` explicitly authorizes a feature-branch commit, ready non-draft PR, babysitting, and merge after every required check and review item is clear. Ordinary `skills-run:` does not authorize Git or GitHub writes.
