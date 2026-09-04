# Omelet orchestration

Omelet is the repository's primary orchestrator. The repository prefers Astra for this role when the host supports it. A user or task can select another available model. Omelet defines the task contract, assigns bounded work, reconciles results, and owns final verification. It does not take the normal implementation assignment.

Specialist roles do not pin a model or reasoning level. Select their models at delegation time with the guidance in [omelet-orchestrator](../skills/omelet-orchestrator/). Treat each model choice as a nudge based on the work, not as a gate. Omelet does not set a subagent cap. It uses the host's available capacity while preserving file and state ownership.

This checked-in revision is `policy-only` until a fresh trusted-project session loads the changed configuration, resolves every named role, and completes one bounded read-only delegation round trip. Do not describe the revised setup as active or approve publication without that evidence.

Use one `skills-run:` route per request:

| Request | Route | Default role | Write authority |
| --- | --- | --- | --- |
| Answer a bounded evidence question | `skills-run:research <question>` | `skill_researcher` or `history_analyst` | None |
| Add a skill with no existing owner | `skills-run:create <outcome>` | `skill_implementer` after owner search | Repository only |
| Improve an existing skill | `skills-run:maintain <outcome>` | `skill_implementer` after owner search | Repository only |
| Check repository skill changes | `skills-run:validate <scope>` | `skill_syncer` | None outside the repository |
| Copy approved skills to installed roots | `skills-run:sync <scope>` | `skill_syncer` | Explicit sync authority |
| Commit, file a PR, watch review, or merge | `skills-run:publish <scope>` | `git_pr_manager` | Explicit publication authority |

Use `skills-run:full <task>` only when the user authorizes the complete feature-branch, ready-PR, review, and merge flow. It does not authorize unrelated changes. Direct pushes to `master` are prohibited.

## Runbook

1. Read the applicable `AGENTS.md`, skill owner, and relevant canonical evidence.
2. Capture `git rev-parse HEAD` and `git status --porcelain=v2 --untracked-files=all`.
3. Record `dirty_tree: clean` only for empty status output. Otherwise record the status snapshot and its digest.
4. Define the outcome, out-of-scope work, owners, allowed paths, protected behavior, proofs, authority, and shared boundaries.
5. Search existing skills before a create or maintain route. Extend the existing owner unless a new skill has an independent trigger, owner, workflow, and validator.
6. Assign one writer for each file and rule owner. Serialize shared paths and contracts.
7. Run research directly in `skill_researcher`. Do not nest delegation unless Omelet requires it.
8. Require independent `skill_reviewer` review for material trigger, ownership, workflow, safety, validator, synchronization, publication, or shared-policy changes.
9. Re-run affected validation after reconciliation. Inspect the cohesive diff and run `git diff --check`.

Evidence must state `observed`, `inferred`, or `unavailable`. Include the source, result, time, environment, `HEAD`, and dirty-tree identity. Refresh evidence after a material input, producer, environment, state, commit, or dirty-tree change.

## Delegate result

Every delegate returns this result before Omelet integrates its work:

```text
status: complete | partial | blocked | cancelled
contract: <task identifier and assigned scope>
changed_paths: <paths or none>
checks: <command, result, and relevant failure coverage>
evidence: <status, source, freshness identity, and result>
uncertainty: <unverified boundary or none>
next_action: <required decision or none>
```

Omelet rejects or recontracts out-of-scope, partial, blocked, and cancelled work. It independently verifies each complete material result before integration.
