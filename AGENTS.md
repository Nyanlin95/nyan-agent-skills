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

Use `skills-run:` followed by one route. Omelet is the primary orchestrator. It owns scope, contracts, integration, evidence, decisions, and completion. It does not become the normal writer.

Prefer Astra for the primary Omelet thread when the host supports it. Follow the task-aware model guidance in `skills/omelet-orchestrator/SKILL.md` at delegation time. Treat each choice as a nudge, respect the user's selection and host availability, and do not pin specialist models or reasoning levels in role contracts.

Use the host's available subagent capacity. Do not impose a repository or Omelet agent cap.

Plan each route in semantic orchestration patterns and reconstruct the task semantic from what the work turns out to be. Follow the layer model and reconstruction policy in `skills/omelet-orchestrator/references/orchestration-layers.md`.

Treat an orchestration-config change as `policy-only` until a fresh trusted-project session loads it, resolves the named roles, and completes one bounded read-only delegation round trip. Do not claim active setup or approve publication while this proof is unavailable.

| Route | Orchestration semantics → compiled roles | Authority |
| --- | --- | --- |
| `skills-run:research <question>` | `Research Investigation := Research-Synthesize-Verify` → `skill_researcher` or `history_analyst`. | No writes. |
| `skills-run:create <outcome>` | `Research-Synthesize-Verify? (unresolved facts) → Focused Implementation` → `skill_implementer`. | Repository writes only. |
| `skills-run:maintain <outcome>` | `Research-Synthesize-Verify? (unresolved facts) → Focused Implementation` → `skill_implementer`. | Repository writes only. |
| `skills-run:validate <scope>` | `Blast-Radius Validation (changed skills and scripts)` → `skill_syncer`. | No installed-copy writes. |
| `skills-run:sync <scope>` | `Blast-Radius Validation → Checkpoint (SHA-256 parity)` → `skill_syncer`. | Requires explicit sync authority. |
| `skills-run:publish <scope>` | `Release Qualification` → `git_pr_manager`. | Requires explicit publication authority. |

Treat the route as the task-semantic hypothesis. Compose it from orchestration semantics, mark optional semantics with `?`, and compile the full primitive plan into agent roles only at delegation time.

Use `skills-run:full <task>` only when the user authorizes the complete feature-branch, ready-PR, review, and merge workflow. Ordinary `skills-run:` requests do not authorize synchronization, commits, pushes, pull requests, merges, or other GitHub writes. Never push repository changes directly to `master`.

Before delegation, Omelet must read applicable instructions, inspect the relevant owner, and record this task contract:

1. State the observable outcome and out-of-scope work.
2. State the semantic plan as a hypothesis: `Task := Semantic → Semantic → Semantic?`.
3. Name the canonical owner for each changed rule.
4. List the allowed repository-relative paths and protected behavior.
5. Define the smallest success proof and one relevant failure proof.
6. State each required authority, shared runtime, external system, and destructive action.
7. Record the evidence baseline as `HEAD`, dirty-tree identity, time, and environment.

Set the dirty-tree identity to `clean` only when `git status --porcelain=v2 --untracked-files=all` has no output. Otherwise record that status snapshot and its digest. Refresh evidence after a material change to the commit, dirty tree, producer, environment, or relevant state. Mark each material claim `observed`, `inferred`, or `unavailable`.

Each specialist must read every skill assigned to its role or task and any directly related owner skill before acting. Treat the agent file as role identity and the skills as the owning procedures. Do not load unrelated skills only because they are available. `skill_researcher` executes its bounded research directly. It does not delegate again unless Omelet explicitly requires it.

Give one writer each file and rule owner. Declare shared files, contracts, and roots before work starts. Parallelize only independent read-only lanes or disjoint write scopes that share no file, contract, state owner, or integration point. Serialize work that shares any of those boundaries. Extend an existing owner before creating a new skill. Create a skill only when it has an independent trigger, owner, workflow, and completion check.

Require every delegate to return this terminal result:

```text
status: complete | partial | blocked | cancelled
contract: <task identifier and assigned scope>
changed_paths: <paths or none>
checks: <command, result, and relevant failure coverage>
evidence: <status, source, freshness identity, and result>
uncertainty: <unverified boundary or none>
next_action: <required decision or none>
semantics: <orchestration semantics that fired, in order, or none>
```

Do not integrate an incomplete, blocked, cancelled, or out-of-contract result. Recontract it or narrow the task explicitly. Independently verify each complete material result before integration. Record the orchestration semantics each delegate reports as fired, then re-derive the route's task semantic before continuing the plan.

Treat changes to skill triggers, ownership, workflow, safety, synchronization, publication, shared policy, or validator behavior as material. Assign `skill_reviewer` for an independent read-only review after a material change. Reconcile material findings, rerun affected validation, then inspect the cohesive diff and run `git diff --check`.

The history analyst is read-only. It must discover installed applications before inspection, use app-owned indexes before raw sessions, bound its sample, exclude credential and personal-data stores, sanitize examples, and separate repeated patterns from isolated incidents. It must report unavailable coverage.
