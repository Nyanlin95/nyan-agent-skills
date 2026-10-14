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

Use [omelet-orchestrator](skills/omelet-orchestrator/SKILL.md) as the canonical workflow owner. Follow that skill for model selection, grounding, request interpretation, semantic planning, task contracts, delegation, evidence, review selection, and setup proof. Do not restate its rules here; this section records only repository-specific policy.

Use `skills-run:` routes as task hypotheses, not mandatory agent pipelines:

| Route | Semantics | Scope |
| --- | --- | --- |
| `skills-run:research <question>` | Research-Synthesize-Verify | Read-only; return findings unless a repository artifact is requested. |
| `skills-run:create <outcome>` | Research-Synthesize-Verify? → Focused Implementation | Search owners first; repository writes only. |
| `skills-run:maintain <outcome>` | Research-Synthesize-Verify? → Focused Implementation | Extend the existing owner; repository writes only. |
| `skills-run:validate <scope>` | Blast-Radius Validation | Check changed owners and affected scripts; no installed-copy writes. |
| `skills-run:sync <scope>` | Blast-Radius Validation → Checkpoint | Copy explicitly authorized skills to installed roots and prove SHA-256 parity. |
| `skills-run:publish <scope>` | Release Qualification | Perform only explicitly authorized Git or GitHub actions. |

Use [handoff-to-opencode](skills/handoff-to-opencode/SKILL.md) when OpenCode delegation is requested or selected for bounded, non-sensitive work. Keep free-model eligibility, task routing, the wrapper, and recovery in that skill. Do not duplicate its model policy in role files. Retain scope, review, verification, and publication decisions in Omelet.

Keep the skill validator, catalog checks, and cohesive `git diff --check` required above.

Treat plain orchestration as no publication authority. For authorized commits and pushes, use `main` and push directly to `origin/main`. Do not create a feature branch or PR unless the user explicitly requests one. `skills-run:full <task>` authorizes validation, commit, and direct push to `main`, not deployments or unrelated work. Delete branches only when cleanup is authorized and fresh ancestry checks prove they are merged into `origin/main`. Never bypass hooks or rewrite shared history.

Keep orchestration policy or role changes `policy-only` until the skill's "Prove the setup level" proof passes in a fresh trusted-project session; do not claim desktop activation from CLI-only proof.

Keep history analysis read-only and privacy-bounded. Discover installed applications and use app-owned indexes before raw sessions. Exclude credential and personal-data stores, sanitize examples, distinguish recurring patterns from isolated incidents, and report unavailable coverage.

For evidence-led look-backs:

- Record the time window, sources checked, eligible and sampled session counts, application and project mix, interaction types, and unavailable coverage.
- Link each proposed change to a sanitized source-session reference and short evidence summary. Mark skill activation as known or unknown, separate observed behavior from inferred cause, and keep raw transcript text out of durable instructions.
- Keep positive evidence distinct from negative signals. Classify negatives as harmful guidance, non-compliance, irrelevant guidance, or orchestration/tooling failure, then route each change to its canonical owner. Treat failed or nonzero tool metadata as an event, not proof that the task failed; attribute it to a skill only when returned evidence shows causation, and mark the cause unknown when outputs or context are unavailable.
- For routine guidance changes, require the same finding in at least two distinct sessions. Require at least two distinct projects before promoting a cross-project rule. A single verified, decision-critical safety or correctness defect can justify a narrow exception; record its direct evidence and reason.
- Exclude retrospective and analysis runs from their own evidence pool. Do not let generated proposals count as validation.
- Keep history analysis read-only. Show each proposed edit with sanitized evidence and a cohesive diff, and apply it only when the user has authorized the change.
