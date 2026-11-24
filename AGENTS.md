# Nyan Agent Skills

This repository is a library of independent Codex skills.

## Commands

Run from the repository root with Python 3.11 or newer.

```sh
python scripts/validate_skills.py
python scripts/validate_skills.py skills/omelet-orchestrator
python scripts/gen_catalog.py
python scripts/gen_catalog.py --check
python scripts/check.py --tests-only
python scripts/check.py
git diff --check
```

Opt in to the versioned pre-commit hook with `git config core.hooksPath .githooks`.
It checks skill metadata, links, and the catalog from the staged snapshot.
CI runs the full check for pushes and pull requests to `main`.

## Library structure

- Store every skill at `skills/<skill-name>/`.
- Name the folder exactly as the `name` in `SKILL.md`.
- Keep reusable instructions in `SKILL.md`.
- Store optional resources only in `agents/`, `references/`, `scripts/`, or `assets/`.
- Do not add a README, changelog, or installation guide inside an individual skill.

## Skill requirements

- Use lowercase letters, digits, and hyphens for skill names.
- Include only `name` and `description` as strings in YAML frontmatter. Use plain strings, single quotes, JSON-style double quotes, or indented YAML block strings. Quote values that YAML reads as numbers, booleans, dates, or null.
- Put all trigger conditions in the frontmatter description.
- Write body instructions in imperative form.
- Write procedures and do-or-do-not lists as direct actions. Keep one action in each numbered step.
- Keep conceptual guidance flexible when the task needs judgment.
- Keep `SKILL.md` concise and use one-level references for detailed material.
- Require nonempty `interface.display_name`, `interface.short_description`, and `interface.default_prompt` in `agents/openai.yaml`. Reflect the skill name in the title, summarize its purpose in a one-line short description for the catalog, and include `$<skill-name>` in the prompt.
- Use unquoted keys and indented block mappings in `agents/openai.yaml`. Write optional collections as indented mappings or lists, or use JSON syntax for an inline collection.
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

Run the in-repo skill validator after each material change. It warns about missing trigger wording, descriptions over 1,024 characters, `SKILL.md` over 500 lines or 15 KiB, and a reference over 25 KiB. Use the system `quick_validate.py` as an optional extra.

Before finishing a skill edit, review the skill prompt and purpose for semantic alignment. Run `python scripts/check.py` after the final edit to check metadata, references, catalog drift, tests, and whitespace.

Test scripts by running them. Verify rendered behavior against the actual artifact.

## Catalog maintenance

Regenerate the README catalog when a skill is added or its catalog text changes. The generator uses `interface.short_description` by default and preserves existing longer purposes in [catalog_purposes.json](scripts/catalog_purposes.json). Alphabetical order gives each skill a predictable position.

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

Give each concurrent writer a short-lived branch or a separate worktree. Publish through authorized PRs targeting `main` and require a passing `validate` check before merging. Push directly to `origin/main` only when the owner explicitly requests it. See the [branch protection proposal](docs/branch-protection-proposal.md) for server-side enforcement options.

Treat plain orchestration as no publication authority. `skills-run:full <task>` authorizes validation, a commit, and opening a PR. Require separate authority for merging, deployment, and branch cleanup. Delete branches only when fresh ancestry checks prove they are merged into `origin/main`. Never bypass hooks or rewrite shared history.

Keep orchestration policy or role changes `policy-only` until the skill's "Prove the setup level" proof passes in a fresh trusted-project session; do not claim desktop activation from CLI-only proof.

Keep history analysis read-only and privacy-bounded. Discover installed applications and use app-owned indexes before raw sessions. Exclude credential and personal-data stores, sanitize examples, distinguish recurring patterns from isolated incidents, and report unavailable coverage.

For evidence-led look-backs:

- Record the time window, sources checked, eligible and sampled session counts, application and project mix, interaction types, and unavailable coverage.
- Link each proposed change to a sanitized source-session reference and short evidence summary. Mark skill activation as known or unknown, separate observed behavior from inferred cause, and keep raw transcript text out of durable instructions.
- Keep positive evidence distinct from negative signals. Classify negatives as harmful guidance, non-compliance, irrelevant guidance, or orchestration/tooling failure, then route each change to its canonical owner. Treat failed or nonzero tool metadata as an event, not proof that the task failed; attribute it to a skill only when returned evidence shows causation, and mark the cause unknown when outputs or context are unavailable.
- For routine guidance changes, require the same finding in at least two distinct sessions. Require at least two distinct projects before promoting a cross-project rule. A single verified, decision-critical safety or correctness defect can justify a narrow exception; record its direct evidence and reason.
- Exclude retrospective and analysis runs from their own evidence pool. Do not let generated proposals count as validation.
- Keep history analysis read-only. Show each proposed edit with sanitized evidence and a cohesive diff, and apply it only when the user has authorized the change.
