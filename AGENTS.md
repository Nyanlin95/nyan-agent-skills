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

Use [omelet-orchestrator](skills/omelet-orchestrator/SKILL.md) as the canonical workflow owner. Omelet is the primary thread and owns scope, integration, evidence, decisions, shared state, and authorized publication. It may complete focused work directly. Delegate only when a bounded specialist or independent result can improve the outcome.

Follow the skill's task-aware model guidance at delegation time. Prefer Astra for Omelet when available; respect the user's selection and host capabilities. Keep role contracts free of fixed models and reasoning levels. Use host capacity without a repository agent cap.

Ground decisions in current repository evidence and applicable primary sources. Infer the request posture and intended artifact state before acting. Follow the skill's sections on request interpretation, starting a project, and product design; preserve optional design skills and ask only for unresolved consequential decisions.

Plan in semantic orchestration patterns and reconstruct the task semantic from the work actually performed. Use [orchestration-layers.md](skills/omelet-orchestrator/references/orchestration-layers.md) for the catalogs and reconstruction policy. Keep contracts proportionate: outcome, owner, allowed paths, protected behavior, acceptance proof, authority, and shared boundaries. Record material evidence with its source, time, environment, revision, relevant dirty state, and observed, inferred, or unavailable status. Refresh it when those inputs change.

Use `skills-run:` routes as task hypotheses, not mandatory agent pipelines:

| Route | Semantics | Scope |
| --- | --- | --- |
| `skills-run:research <question>` | Research-Synthesize-Verify | Read-only; return findings unless a repository artifact is requested. |
| `skills-run:create <outcome>` | Research-Synthesize-Verify? → Focused Implementation | Search owners first; repository writes only. |
| `skills-run:maintain <outcome>` | Research-Synthesize-Verify? → Focused Implementation | Extend the existing owner; repository writes only. |
| `skills-run:validate <scope>` | Blast-Radius Validation | Check changed owners and affected scripts; no installed-copy writes. |
| `skills-run:sync <scope>` | Blast-Radius Validation → Checkpoint | Copy explicitly authorized skills to installed roots and prove SHA-256 parity. |
| `skills-run:publish <scope>` | Release Qualification | Perform only explicitly authorized Git or GitHub actions. |

Compile a semantic plan into the registered roles only when delegation helps. Use one writer per file and canonical rule. Parallelize independent reads or disjoint writes; serialize shared files, contracts, state, and integration boundaries. Read the required task and owner skills before acting. Follow the skill's "Delegate bounded work" section for elevated execution permissions; a declared path contract is not enforced isolation.

Use [handoff-to-opencode](skills/handoff-to-opencode/SKILL.md) when OpenCode delegation is requested or selected for bounded, non-sensitive work. Keep free-model eligibility, task routing, the wrapper, and recovery in that skill. Do not duplicate its model policy in role files. Retain scope, review, verification, and publication decisions in Omelet.

Close delegates with a terminal status (`complete`, `partial`, `blocked`, or `cancelled`), result, changed paths, checks, and uncertainty. Do not require a fixed report template. Verify complete material results before integration; reject or recontract partial or out-of-scope results. End assignments after consuming their results.

Use focused repository checks by default. Follow the skill's "Select review and implementation" section for consequential independent review. Use one reviewer; add adversarial review only for an unresolved decision-critical claim. Do not require review chains for routine documentation or Git pushes. Keep the skill validator, catalog checks, and cohesive `git diff --check` required above.

Treat plain orchestration as no publication authority. Preserve repository publishing rules: use `main` as the base and push changes on a feature branch, never directly to `main`. Create a ready PR only when authorized; merge only when explicitly authorized. `skills-run:full <task>` authorizes the feature-branch, ready-PR, review, and merge workflow, not deployments or unrelated work. Never bypass hooks or rewrite shared history.

For orchestration policy or role changes, follow the skill's "Prove the setup level" section. Keep the revision `policy-only` until a fresh trusted-project session loads the policy, resolves the registered roles, and completes one bounded read-only delegation round trip. Require this proof before publishing setup changes; do not claim desktop activation from CLI-only proof.

Keep history analysis read-only and privacy-bounded. Discover installed applications and use app-owned indexes before raw sessions. Exclude credential and personal-data stores, sanitize examples, distinguish recurring patterns from isolated incidents, and report unavailable coverage.
