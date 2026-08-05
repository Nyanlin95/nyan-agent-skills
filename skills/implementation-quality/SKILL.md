---
name: implementation-quality
description: Implement or refactor application code with simple design, clear ownership, readable control flow, and explicit failure behavior. Use when a coding agent must write code, move behavior to a new owner, choose an abstraction or component boundary, or replace old code through a parity-tested migration or temporary fork. Do not use for reviews or trivial mechanical edits.
---

# Implementation Quality

Implement the requested behavior with a complete design that makes intent, ownership, invariants, and failure paths clear. Preserve the repository's established architecture.

The canonical owner is the one module, component, or service that owns a rule or decision.

A good abstraction lets a caller express what it wants without taking ownership of the mechanics beneath it. It should align with a real responsibility boundary and remain understandable enough that a reader can predict what is underneath, where failures come from, and where to look when behavior changes.

## Implementation flow

Use this flow in order. Use later sections only when they apply to the current step.

1. Define the observable behavior, owner, safety boundary, and proof.
2. Trace the current owner, direct callers, state, effects, and failure path.
3. Choose the smallest complete ownership correction.
4. Change one independently checkable unit at a time.
5. Run the focused proof after each unit.
6. Run authorized runtime verification when the behavior crosses a runtime boundary.
7. Report the accepted behavior, checks, and remaining risk.

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

Run local, hermetic verification by default. Before a check can mutate data, call a provider, send a message, charge a payment method, or interrupt a process, require explicit authorization for the exact non-production target.

Treat authorization to implement a change as separate from authorization to exercise a shared or external runtime. When safe runtime verification is unavailable, state the unverified boundary and its remaining risk.

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

## Verification strength

Match the proof to the risk of the changed behavior.

- Use static checks to prove type, formatting, dependency, or generated-artifact constraints.
- Use focused tests to prove policies, state transitions, mapping, and expected failures.
- Use an integration test, trace, or rendered user journey when behavior crosses a process, persistence, provider, or UI boundary.

Do not report runtime success from static checks alone. State any unverified boundary and its remaining risk.

## Abstraction model

Treat abstractions as boundaries between levels of intent, not merely as extracted code.

A useful abstraction should do all three:

- **Express intent:** its name and interface describe what the caller is trying to accomplish, not the mechanics used to accomplish it.
- **Follow ownership:** it owns one coherent set of decisions that change for the same reason and delegates decisions owned by lower layers.
- **Remain predictable:** callers do not need every implementation detail, but they should be able to infer the major steps, side effects, costs, and failure modes.

Think in layers:

```text
Product or domain intent
    ↓
Application workflow
    ↓
Policies and domain operations
    ↓
Infrastructure and integration boundaries
    ↓
Framework and platform mechanics
```

Each layer should translate higher-level intent into lower-level responsibilities. Do not force the source tree, call tree, component tree, runtime tree, or rendered tree to be identical; they represent different kinds of structure.

## Abstraction decision

Create an abstraction only when at least one is true:

- Use it to name a stable domain concept.
- Use it to translate high-level intent into lower-level work.
- Use it to establish or protect an ownership boundary.
- Use it to isolate an external boundary, lifecycle, resource, or dependency.
- Use it when current cases change for the same reason.
- Use it to state an invariant or prevent an invalid state.
- Use it to hide difficult mechanics without hiding behavior or failures.

Do not create an abstraction only because:

- the code is long;
- a helper might have a future caller;
- two code blocks look similar;
- another layer makes a diagram look cleaner.

Keep duplication while the cases may diverge. Remove or inline an abstraction that:

- only gives syntax a new name;
- crosses unrelated ownership boundaries;
- needs unused options, callbacks, modes, or generic context objects;
- hides order, side effects, cost, or failure behavior;
- serves one caller and owns no meaningful concept or boundary.

## Ownership boundaries

Place each decision in the layer that is responsible for it.

For example, in a component system:

```text
Feature component      owns workflow and product intent
Domain component       owns business-specific presentation and policy
Design-system component owns reusable interaction, accessibility, and states
Primitive              owns low-level layout or rendering mechanics
Token                   owns named visual values and constraints
```

The same principle applies outside UI:

```text
Application service    owns orchestration
Domain model or policy owns business rules and invariants
Repository             owns persistence semantics
Integration adapter    owns provider-specific translation
Platform utility       owns runtime or framework mechanics
```

A higher layer may coordinate lower layers, but it should not absorb their policies. A lower layer should not learn about caller-specific workflows merely to become more reusable.

## Code shape

- Make the top-level path show the domain workflow.
- Keep orchestration linear.
- Use interfaces that state caller intent.
- Do not expose modes or internal data shapes without a current need.
- Extract a helper only for a named action, policy, or boundary.
- Do not extract a helper to meet a line limit.
- Keep related reads, validation, changes, and result handling together.
- Give each abstraction one reason to change.
- Name each value after its role and constraint.
- Use explicit result and error states.
- Show branches, side effects, retries, transactions, and external calls in the owning layer.
- Do not use compact expressions or generic wrappers that hide order, cost, or errors.
- Use the formatter to wrap code.
- Write a comment only for an invariant, trade-off, ownership rule, or external constraint.
- Do not use comments to narrate code or preserve obsolete history.

## Predictable internals

An abstraction may hide implementation details, but it must not make behavior mysterious.

From its name, contract, and location, a reader should be able to answer:

- What intent does this represent?
- Which decisions does it own?
- Which lower-level mechanisms is it likely to delegate to?
- What side effects or external boundaries can it cross?
- How can it fail?
- What kind of requirement change should modify it?

If those answers are unclear, improve the name, contract, ownership, or placement before adding more documentation or indirection.

## Migration and fork lifecycle

Use a fork only as a temporary parallel implementation. Do not make the fork a second permanent owner.

Use these steps to move behavior to a new owner:

1. List the current owner, callers, behavior, failures, and old-owner tests.
2. Add a focused parity test before the migration.
3. Compare results, state changes, errors, and side effects in the parity test.
4. Implement the new path without unrelated behavior.
5. Route both paths through one explicit selection point.
6. Add new-owner tests for success, failure, invariants, and state transitions.
7. Run the parity test for all agreed cases.
8. Move callers to the new owner after the parity test passes.
9. Remove the migration-only parity test after the move.
10. List the old code and old-owner tests that can be removed.
11. Report remaining callers, rollback effects, and verification evidence.
12. Ask the user to approve or reject the removal.
13. Remove the old code and obsolete tests only after user approval.

If both paths cannot use the same input, use contract fixtures or recorded outputs. State the limits of this comparison.

Do not add separate features, policies, or callers to the fork.

If the parity test finds an intentional difference, stop the migration. Ask the user to select the required behavior and owner.

## Schema and data migration lifecycle

Use this lifecycle when a change alters persisted schema, stored data, or compatibility between deployed versions. Do not treat code-path parity as proof that the data migration is safe.

1. Identify the old and new schemas, data owners, compatibility window, and source of truth.
2. Implement an additive schema change that old and new readers and writers can use before the rollout.
3. Implement an idempotent, resumable backfill with explicit checkpoints and retry behavior.
4. Test production-shaped legacy fixtures that include malformed, partial, duplicate, and boundary records.
5. Define data invariants and a reconciliation method such as counts, checksums, or sampled record comparison.
6. Define deployment order and reader/writer authority for mixed-version clients.
7. Define the stop condition and the rollback boundary, or state the forward-recovery path when rollback is unsafe.
8. Verify progress, error, invariant, and reconciliation signals before and during cutover.
9. Remove old reads, writes, schema, and migration code only after compatibility ends and reconciliation succeeds.

## Before finishing

1. Confirm that the top-level path shows the requested intent.
2. Confirm that the code uses the canonical owner.
3. Inline each new abstraction that owns no meaningful concept, policy, invariant, or boundary.
4. Remove unused configuration, modes, extension points, and generic behavior.
5. Trace success, side effects, and failure through the changed path.
6. Run the smallest reliable test for the changed behavior and failure path.
7. Run the rerunnable proof and record any unverified boundary.
8. For a migration, confirm that you completed each lifecycle step in order.

Report the requested intent, chosen owner, any new or rejected abstraction, checks run, and remaining risk concisely.
