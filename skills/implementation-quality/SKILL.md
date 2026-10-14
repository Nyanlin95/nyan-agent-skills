---
name: implementation-quality
description: Start runnable projects or implement and refactor repository code with simple design, clear ownership, and explicit failure behavior. Use for a blank repository, first working product journey, code changes, ownership or component boundaries, and parity-tested migrations or temporary forks, including skill-library files. Do not use for read-only reviews, planning-only work, or trivial mechanical edits; use cqt-review for evidence-based review and recommendations.
---

# Implementation Quality

Implement the requested behavior with a complete design that makes intent, ownership, invariants, and failure paths clear. Preserve the repository's established architecture.

The canonical owner is the one module, component, or service that owns a rule or decision.

A good abstraction lets a caller express what it wants without taking ownership of the mechanics beneath it. It should align with a real responsibility boundary and remain understandable enough that a reader can predict what is underneath, where failures come from, and where to look when behavior changes.

## Implementation flow

Use this flow for changes to an existing implementation. For a blank or incomplete project, use the starting-project guidance below; do not search indefinitely for owners that do not yet exist. Use later sections only where relevant.

1. Define the observable behavior, owner, safety boundary, and proof.
2. When the change crosses a function boundary, sketch the types, signatures, and module structure first, as in pstack's `architect` skill.
3. Trace the current owner, direct callers, state, effects, and failure path.
4. Choose the smallest complete ownership correction.
5. Change one independently checkable unit at a time.
6. Run the focused proof after each unit.
7. Run authorized runtime verification when the behavior crosses a runtime boundary.
8. Report the accepted behavior, checks, and remaining risk.

## Start a runnable project

Establish the smallest complete foundation for the requested first version. Carry the user, central task, core entities, ownership rules, persistence expectations, and observable success into implementation. Resolve consequential missing product decisions with the user; choose routine reversible details from existing conventions or suitable defaults. Keep onboarding and decision timing with the coordinating workflow.

Read [starting-projects.md](references/starting-projects.md) for runnable setup, a complete first journey, project-specific service boundaries, and bounded shortcuts. Adapt it to the actual medium and stack rather than applying a universal starter architecture.

Prefer one working path with real declared behavior over disconnected placeholder screens. Verify setup from the documented commands, the main journey, one relevant failure or recovery path, and actual persistence when claimed. Exercise visible work in the running artifact. Complete the agreed first version beyond the initial slice when more remains in scope.

Before calling the project ready, confirm that its required configuration and commands are discoverable, its authored data is isolated from live user data during testing, and its verified scope matches the claimed capabilities. Report how to run or open it, what works, the checks performed, and any simulated, deferred, or externally unverified boundary. Do not equate a scaffold, mock integration, or passing build with a working product.

## Refactor scope

Set refactor scope from the behavior's ownership boundary, not from a file count or a preference for a local diff.

A complete ownership correction can include the current owner, the destination owner, direct callers, public or generated contracts, state or persistence boundaries, and the tests and documentation that describe the moved behavior. Change every direct participant that is necessary to leave one canonical owner.

Do not retain a duplicate owner, compatibility facade, stale test, or partial routing path merely to keep the refactor smaller. Use a temporary bridge only when compatibility requires it. State its owner and removal condition.

Limit unrelated expansion. Do not add speculative abstractions, features, dependency upgrades, or repository-wide conventions that are not necessary to complete the ownership correction.

## Execution discipline

For a non-trivial change:

1. State the observable behavior that must hold.
2. Build the smallest rerunnable proof for that behavior.
3. Change one unit that can be checked independently.
4. Run the relevant check before changing the next unit.
5. Exercise the real artifact or complete data flow when the behavior crosses a runtime boundary.

Keep a script, focused test, fixture, trace query, or documented command when it makes future verification cheaper. Do not treat a one-time manual assertion or a delegate report as the only proof of a durable behavior.

Prefer removal before addition. Delete dead paths, redundant guards, obsolete tests, and temporary migration code when their removal is required to leave one canonical owner. Do not preserve accidental complexity merely because it is already present.

Fix the owner, lifecycle, state transition, or routing rule that causes a defect. Reproduce the failure, trace it to that cause, and inspect sibling paths for the same fault. Do not add a wording-specific suppression, fallback, or UI exception that only hides the defect.

## Active verification safety

Run local, isolated verification by default. Within an authorized build or fix, create and mutate task-owned synthetic fixtures, isolated test stores, and processes you started as needed for verification without another permission request. Verify exact ownership and target paths; keep live application data, credentials, user profiles, and unrelated processes outside that scope.

Use existing explicit authority before exercising a shared runtime, external mutation, message, payment, or destructive operation; request missing authority for the concrete target only when necessary. Do not reuse production credentials or data merely to complete a test. When a boundary cannot be verified safely within authority, continue independent local proof and report that boundary as unverified.

## Before editing

1. Find the current owner of the behavior and its callers.
2. Record the caller intent, input, result, failure behavior, and verification method.
3. Assign each decision to its owning layer.
4. Extend the existing owner only when it is the canonical owner.
5. Establish the destination owner when the current owner crosses a real boundary.

For product behavior:

1. Name the user problem.
2. Name the critical workflow.
3. Identify the canonical state that the change creates or changes.
4. Define the failure that the user can observe.
5. Define the runtime evidence that proves the workflow.

Do not use an architecture improvement as the only reason for a product change. Test the smallest realistic user journey.

## Boundary contract changes

Treat an API, event, IPC, serialization, tool, or provider change as one contract across its boundaries.

1. Identify each producer of the contract.
2. Identify each parser and validator of the contract.
3. Identify each mapping layer and canonical internal model.
4. Identify each consumer and generated artifact.
5. Identify the success, invalid-input, and unavailable-dependency results.
6. Update the direct tests, fixtures, and runtime evidence for the changed contract.
7. Verify the full path at the smallest reliable seam.

Keep external or transport shapes at their boundary. Do not spread them through domain code. Do not add a wording-specific suppression, fallback, or UI exception that only hides a broken owner, lifecycle, state transition, or routing rule.

## Durable commands and background effects

Read [durable-effects.md](references/durable-effects.md) when a change spans persisted commands, external effects, approvals, jobs, or recovery after interruption. Define the operation identity, authoritative result, commit boundary, and uncertain-outcome path before implementing retries. Preserve the approved operation across resume; do not let a new configuration or capability version silently widen its authority.

Keep the model proportional. Reuse existing receipts, transactions, outboxes, worker claims, and version owners instead of adding a parallel execution system. Verify the lost-response and stale-executor boundaries through the repository's existing isolated journeys when they affect the change.

## Verification strength

Match the proof to the risk of the changed behavior.

- Use static checks to prove type, formatting, dependency, or generated-artifact constraints.
- Use focused tests to prove policies, state transitions, mapping, and expected failures.
- Use an integration test, trace, or rendered user journey when behavior crosses a process, persistence, provider, or UI boundary.

Do not report runtime success from static checks alone. State any unverified boundary and its remaining risk.

## Abstraction and code shape

Create an abstraction only for a stable concept, an ownership or external boundary, an invariant, or hidden mechanics that do not hide behavior or failures. Keep duplication while cases may diverge. Read [abstraction-and-code-shape.md](references/abstraction-and-code-shape.md) for the abstraction model, decision rules, ownership layers, code shape, and predictable internals.

## Migrations

Use a fork only as a temporary parallel implementation, prove parity before moving callers, and treat persisted schema or data changes as their own lifecycle. Read [migrations.md](references/migrations.md) and complete each lifecycle step in order. For a multi-unit migration, keep a decision trail in the format of pstack's `show-me-your-work` skill: one TSV row per step with what, why, evidence, and result.

## Before finishing

1. Confirm that the top-level path shows the requested intent.
2. Confirm that the code uses the canonical owner.
3. Inline each new abstraction that owns no meaningful concept, policy, invariant, or boundary.
4. Remove unused configuration, modes, extension points, and generic behavior.
5. Trace success, side effects, and failure through the changed path.
6. Run the smallest reliable test for the changed behavior and failure path.
7. Run the repository's complete verification gate for the changed path (typecheck, build, format, and tests). Tests passing alone do not complete a change when a required gate fails.
8. Update a versioned plan or roadmap only when its canonical status markers track the delivered scope.
9. Run the rerunnable proof and record any unverified boundary.
10. For a migration, confirm that you completed each lifecycle step in order.

Report the requested intent, chosen owner, any new or rejected abstraction, checks run, and remaining risk concisely.
