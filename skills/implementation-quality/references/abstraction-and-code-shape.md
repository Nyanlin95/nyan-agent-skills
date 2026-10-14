# Abstraction and code shape

Detailed rules for when to create an abstraction, where each decision lives, and how code should read.

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
