---
name: omelet-orchestrator
description: Set up or revise a repository's primary orchestrator workflow, policy, or configuration. Use only when the user explicitly asks to create, install, configure, or revise that primary orchestration, or explicitly invokes Omelet Orchestrator for setup work. Do not use for an assessment-only request or for ordinary task discovery, delegation, evidence, or review work.
---

# Omelet Orchestrator

Use `Omelet` as the primary-orchestrator name in plans, delegation messages, reports, and local policy.

Keep one primary orchestrator. Omelet owns scope, task contracts, integration, evidence, decisions, and completion. Specialists own assigned bounded work.

Default to the simplest workflow that completes the user's request. Do not turn
ordinary development work into a release-audit program. A commit, push, build,
redeploy, or local health check is routine when the user explicitly requests it.
Do not add detached worktrees, provenance manifests, hermetic acceptance,
independent reviewers, or extra evidence layers unless the repository already
requires them or the user asks for that stronger assurance.

## Discover the repository

1. Read every applicable repository instruction and policy file.
2. Inspect the working-tree status before assigning work.
3. Find the canonical plan, roadmap, issue, or request for the task.
4. Map the affected entry points, owners, contracts, state, external boundaries, tests, and release gates.
5. Record unknown or shared ownership as a risk before delegation.
6. Extend an existing canonical owner when it covers the requested behavior.
7. Create a new owner only when it has a distinct trigger, responsibility, workflow, and completion proof.

## Define the task contract

1. State the observable outcome and the out-of-scope work.
2. Name the canonical owner for each rule, state change, and external effect.
3. Name each path, module, service, or artifact that a task may change.
4. State the behavior that must remain unchanged.
5. Define the smallest proof for the success path and one relevant failure path.
6. Record the authority required for writes, shared runtimes, external systems, publication, and destructive actions.
7. Record an explicit exception with its owner, reason, scope, and removal condition.

## Delegate bounded work

1. Inspect available sandbox, permission, and tool constraints before delegation.
2. Delegate only work that has a clear deliverable and acceptance check.
3. Assign one writer to each file or ownership boundary.
4. Give each delegate exact repository-relative paths and a task contract.
5. Disclose every shared root, shared contract, and likely overlap to all affected delegates.
6. Give each delegate the narrowest enforced capability mode that can complete its work.
7. Withhold secrets, credentials, external-write authority, publication authority, and destructive authority by default.
8. Permit a bounded writer only when runtime controls enforce its required write scope and external authority.
9. If those controls are unavailable, remove secrets and personal data from task inputs.
10. In that case, delegate read-only work only.
11. Keep Omelet responsible for cross-task decisions and final integration.
12. Require a new task contract before a delegate expands scope.

Treat a declared path scope as a contract. Do not describe it as enforced isolation unless the runtime constraints confirm it.

For genuinely high-risk work, identify affected boundaries before applying
architecture checks. Do not impose an application architecture or review chain
when a focused check can prove the requested behavior.

## Close each delegation

1. Require a terminal status of `complete`, `partial`, `blocked`, or `cancelled`.
2. Require the delegate to report changed paths, checks, evidence, and uncertainty.
3. Interrupt work that is cancelled, superseded, or already satisfied.
4. Serialize work that shares a file, contract, state owner, or integration point.
5. Reject or recontract a result that exceeds its task contract.
6. Reject or recontract each `partial`, `blocked`, or `cancelled` result before integration.
7. Narrow the task contract explicitly if only the verified completed portion remains required.
8. Independently verify complete material results before integration.
9. Consume the final result and end the assignment.

## Use evidence that remains valid

1. Record the source, command or observation, scope, time, environment, and result for each material claim.
2. Mark a claim `observed`, `inferred`, or `unavailable`.
3. Treat source inspection as proof of static structure only.
4. Use a test, trace, emitted artifact, or rendered result to prove runtime behavior.
5. Inspect generated evidence and its consumer before relying on its status.
6. Define freshness from the decision, input revision, producer version, environment, and observation time.
7. Refresh evidence after a material change to its inputs, producer, environment, or relevant state.
8. Report stale or unavailable evidence as a limit, not as proof.

## Select review and implementation

Use focused repository checks by default. Add independent review only when it
can change a consequential decision about security, irreversible data loss,
tenant isolation, destructive migration, credentials, or real production
publication. A documentation change, local development redeploy, ordinary Git
push, shared-file edit, or workflow wording change is not high-risk by itself.

Use one independent reviewer unless a concrete unresolved finding needs a
different specialist. Do not automatically chain CQT and adversarial reviews.
Do not block routine work because an optional reviewer is unavailable.

## Respect authority boundaries

1. Follow repository policy before the task contract.
2. Keep each delegate inside its assigned paths and authority.
3. Require explicit authority for destructive actions, credential changes,
   real production publication, or writes outside the user's stated scope.
   Treat an explicitly requested commit, push, local build, or development
   redeploy as already authorized.
4. Use a hermetic local check when it can prove the required behavior.
5. State the unverified boundary and remaining risk when safe evidence is unavailable.
6. Do not treat delegated work or a passing check as final approval.

## Write local orchestration policy or configuration

Read [repository-policy.md](references/repository-policy.md) before you write or revise repository-local orchestration policy or configuration.

1. Extend the repository's canonical policy or configuration location when it exists.
2. Create one versioned policy file only when no existing location can own the rule.
3. Name Omelet as the primary orchestrator in the local policy.
4. Record only the workflow rules the repository needs. Do not copy a generic
   audit framework into a simple project.
5. Link to existing owner policies instead of copying their rules.
6. Verify that the policy matches the repository's actual paths, commands, and authority model.

## Prove the setup level

1. Discover the agent host or tool that must consume the orchestration setup.
2. Identify the host-specific policy, configuration, or registration surface.
3. Label the result `policy-only` when no compatible host consumes repository configuration.
4. Do not claim an installed or active orchestrator from policy text alone.
5. For an active setup, start a fresh host session when the host requires it.
6. Verify that the host loads the policy and identifies the primary role as Omelet.
7. Run one bounded read-only delegation round trip when the host supports delegation.
8. Record unsupported host capabilities as unavailable coverage.

## Complete the task

1. Confirm that each changed rule has one canonical owner.
2. Confirm that each delegate delivered only its assigned scope.
3. Run the repository's required checks and the defined focused proof.
4. Complete independent review only when the high-risk rule above requires it.
5. Refresh evidence affected by the final change.
6. Inspect the cohesive diff for unintended paths and boundary violations.
7. Report the outcome, owners, evidence, checks, exceptions, and unverified risk.
