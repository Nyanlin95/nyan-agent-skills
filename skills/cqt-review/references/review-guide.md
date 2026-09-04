# Detailed CQT Review Guide

Use these checks only when they can affect the selected behavior or finding. Do not turn them into a required repository-wide audit.

## Prepare the review

1. Identify the requested scope: repository, subsystem, feature, pull request, or critical flow.
2. Identify the entry points, core domains, stores, integrations, background jobs, shared UI, tests, and deployment units that affect it.
3. Infer architecture from repeated code as well as documentation.
4. Read the relevant `CONTEXT-MAP.md` and `CONTEXT.md` files when they exist.
5. Record delivery-context assumptions as observed, inferred, or unavailable.

For a broad review, map a small number of critical flows before reading files alphabetically.

## Trace critical flows

Trace the selected flow through:

```text
Input → parsing and validation → authorization → application workflow
→ domain decision → state mutation → external side effects
→ response or visible outcome → failure recovery
```

For each seam, identify the current decision owner, duplicate rules, irreversible effects, partial failures, retry behavior, external-to-internal mappings, and smallest test seam.

Use a trace, test, or rendered journey for runtime claims. Static inspection proves static structure only.

## Review the seams

### Correctness

Check the primary path, expected failures, trust boundaries, authorization, state consistency, destructive or financial operations, concurrency, retries, idempotency, compatibility, and important tests.

For a generated artifact that supports a release or approval claim, trace its producer, inspect the emitted artifact, inspect the consumer validation, and record freshness when it affects the claim.

### Ownership and abstraction

Check that one owner holds each policy, invariant, lifecycle, and integration decision. Flag duplicate business rules, feature behavior in shared primitives, domain policy in transport or views, provider shapes in application code, and mutual dependencies.

An abstraction should express intent, own a concept or boundary, and let callers predict important effects, costs, and failures. Do not keep a helper that only renames structure or hides ordering and side effects.

### Dependencies, state, and failure

Check dependency direction toward stable policy, external SDK leakage, cycles, hidden utility hubs, and ceremony without substitution value.

Check for contradictory boolean or nullable state, hidden transitions, unclear source of truth, optimistic updates without recovery, partial completion, swallowed errors, unsafe retries, transactions that miss their boundary, and unreliable cleanup.

### Domain language and code shape

Use domain language as evidence when terms affect behavior, ownership, state, or a boundary. When the model is unresolved, state the competing terms, the scenario that needs a decision, and the affected owner. Do not create a glossary or ADR during this review.

Prefer top-level paths that show the product operation. Flag generic names, deeply nested control flow, hidden effects, generic mode objects, and trivial wrapper chains only when they weaken comprehension or change safety.

## Review migrations and temporary paths

For an ownership migration, inspect the old owner, callers, behavior, failures, selection point, parity evidence, new-owner tests, remaining callers, and removal condition. Recommend removal when the reviewed scope and compatibility evidence support it. State unresolved compatibility as a risk.

For a schema or data migration, inspect schema ownership, compatibility window, backfill idempotency and checkpoints, legacy fixtures, invariants, reconciliation, deployment order, mixed-version authority, stop or recovery conditions, and cutover evidence.

For a temporary adapter, mapping layer, compatibility wrapper, local policy, facade, or duplication, require one owner, a bounded use, a removal condition, and verification. Do not treat a temporary path as a second permanent owner.

## Report the result

For a repository review, report the scope and assumptions, system and critical-flow maps, P0 and P1 findings, ownership and abstraction findings, dependency hotspots, unresolved domain questions, recommended order, deliberate non-fixes, checks, and evidence limits.

For a feature or pull-request review, report changed behavior, correctness and failure findings, the canonical owner, abstraction and dependency findings, unresolved domain questions, the smallest responsible corrections, required checks, and remaining risk.

Do not produce a long list of low-impact observations. Do not invent findings or rejected alternatives.
