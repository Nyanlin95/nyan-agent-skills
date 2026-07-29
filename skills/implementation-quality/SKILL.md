---
name: implementation-quality
description: Implement or refactor application code with simple design, clear ownership, readable control flow, and explicit failure behavior. Use when Codex must write code, move behavior to a new owner, choose an abstraction or component boundary, or replace old code through a parity-tested migration or temporary fork. Do not use for reviews or trivial mechanical edits.
---

# Implementation Quality

Implement the requested behavior with the smallest design that makes intent, ownership, invariants, and failure paths clear. Preserve the repository's established architecture.

A good abstraction lets a caller express what it wants without taking ownership of the mechanics beneath it. It should align with a real responsibility boundary and remain understandable enough that a reader can predict what is underneath, where failures come from, and where to look when behavior changes.

## Before editing

1. Find the current owner of the behavior and its callers.
2. Record the caller intent, input, result, failure behavior, and verification method.
3. Assign each decision to its owning layer.
4. Extend the existing owner unless the change establishes a real new boundary.

For product behavior:

1. Name the user problem.
2. Name the critical workflow.
3. Identify the canonical state that the change creates or changes.
4. Define the failure that the user can observe.
5. Define the runtime evidence that proves the workflow.

Do not use an architecture improvement as the only reason for a product change. Test the smallest realistic user journey.

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

## Before finishing

1. Confirm that the top-level path shows the requested intent.
2. Confirm that the code uses the canonical owner.
3. Inline each new abstraction that owns no meaningful concept, policy, invariant, or boundary.
4. Remove unused configuration, modes, extension points, and generic behavior.
5. Trace success, side effects, and failure through the changed path.
6. Run the smallest reliable test for the changed behavior and failure path.
7. For a migration, confirm that you completed each lifecycle step in order.

Report the requested intent, chosen owner, any new or rejected abstraction, checks run, and remaining risk concisely.
