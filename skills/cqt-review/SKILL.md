---
name: cqt-review
description: Review a repository for correctness, code quality, code taste, ownership, abstraction, dependency direction, state modeling, failure behavior, and migration lifecycle. Use when auditing an existing codebase, reviewing a feature or pull request beyond correctness, identifying architectural friction, or assessing a parallel implementation. Keep this work read-only. Report bounded, evidence-based findings and recommendations. Do not expand a bounded review into a repository-wide rewrite.
---

# CQT Review

Review Correctness, Quality, and Taste. Respect the repository's architecture, delivery context, and requested scope.

The canonical owner is the module, component, or service that owns a rule or decision.

## Review contract

Inspect and report by default. Do not edit code, data, configuration, infrastructure, or external systems unless the user separately authorizes implementation.

Run only read-only inspection and local, hermetic checks by default. Require authorization for a state-changing or external check. Mark unavailable runtime evidence as unavailable.

Classify every material claim:

- **Observed:** Current source, test, configuration, diff, trace, log, or render proves it.
- **Inferred:** Observed evidence supports it, but an unobserved path needs an assumption.
- **Unavailable:** The required artifact, environment, credential, or runtime path was unavailable.

State the evidence limit. Do not report an inference as an observed defect.

## Review flow

1. Set the scope, delivery context, review authority, and evidence limits.
2. Map the affected owners, state boundaries, external boundaries, and critical flows.
3. Trace each selected flow from input to visible outcome, including failure and recovery.
4. Review correctness, ownership, abstraction, dependencies, state, effects, and tests at the affected seams.
5. Rank evidence-backed findings and name the smallest responsible correction.
6. Report checks, unavailable coverage, remaining risk, and deliberate non-fixes.

For a pull request or feature, inspect the current status and diff, trace the changed behavior and its direct owners, compare it with its contract and tests, and separate new findings from existing debt.

Read [references/review-guide.md](references/review-guide.md) for detailed checks, critical-flow tracing, migration lifecycle, and review outputs. Read [references/language-behavior.md](references/language-behavior.md) when a finding depends on language or runtime semantics. Read [references/framework-behavior.md](references/framework-behavior.md) when framework lifecycle, reactivity, rendering, dependency injection, or server-client boundaries matter.

## Review model

Evaluate three dimensions:

- **Correctness:** Required behavior, trust boundaries, state consistency, failure, recovery, idempotency, and compatibility.
- **Quality:** Clear ownership, direct control flow, explicit state and effects, dependency direction, and testability.
- **Taste:** Concepts, names, abstractions, and local design that make the system understandable and affordable to change.

Tie every taste finding to comprehension, ownership, consistency, misuse risk, or change cost. Do not report a style preference as a defect.

## Severity

- **P0:** A release-blocking correctness, security, data-integrity, or primary-workflow failure.
- **P1:** A material risk in the changed or critical area that needs a bounded correction.
- **P2:** A documented improvement that does not require scope expansion.

Rank by concrete impact and confidence. Do not let a broad existing problem block a bounded change without evidence that it affects the reviewed behavior.

## Finding format

Use this format for each finding:

```text
Title:
Severity: P0 | P1 | P2
Confidence: High | Medium | Low

Location:
Observation:
Evidence:
Evidence status:
Change reach:
Rationale status:
Domain-language status:
Why it matters:
Current owner:
Recommended owner:
Smallest responsible change:
Dependency workaround: none | adapter | mapping layer | compatibility wrapper | local policy | tactical duplication
Ideal later direction:
Verification:
Remaining risk:
```

Omit `Ideal later direction` when it would repeat the recommended change. Keep findings concise, specific, and actionable.

## Completion

Before finishing:

1. Trace the critical behavior from input to result.
2. Confirm one canonical owner for every important rule.
3. Trace success, failure, side effects, and recovery.
4. State each check and unavailable boundary.
5. Give a reliable verification method for each proposed correction.
6. Separate blockers from adjacent debt.
7. Stop before the review becomes an unrelated repository rewrite.

For a migration, check the applicable lifecycle in the review guide. Report recommendations only. A separately authorized implementation task owns the change.
