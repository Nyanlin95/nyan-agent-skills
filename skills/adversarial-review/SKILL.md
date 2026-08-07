---
name: adversarial-review
description: Falsify important claims in an implementation plan, architecture decision, code change, pull request, repository assessment, or another review before people act on it. Use for a red-team or devil's-advocate review, to stress-test a CQT review from an independent perspective, or when a design appears ready but its failure paths, evidence, assumptions, or stated non-findings need hostile scrutiny. Report only evidence-backed counterexamples, untested claims, and decision-relevant risks.
---

# Adversarial Review

Attack the artifact's conclusions. Do not produce a second conventional code-quality review.

Treat the supplied artifact as a set of falsifiable claims. The artifact can be a plan, ADR, implementation, diff, pull request, repository assessment, test result, or a prior review such as a CQT report. Inspect the source needed to test those claims. Do not treat an earlier review, a passing check, or a confident assertion as proof.

## Review Contract

State the artifact under review and the decision it is meant to support. State the evidence available and material limits before making conclusions.

Keep this ownership boundary:

- `cqt-review` assesses correctness, quality, taste, ownership, abstraction, dependency direction, state, failure behavior, and migration lifecycle.
- This skill tries to disprove the important claims and omissions in that assessment or in the underlying artifact.
- Use both skills in sequence when a decision needs both a constructive assessment and an independent challenge.
- Do not repeat CQT findings unless the adversarial evidence changes their severity, confidence, owner, or required action.
- Do not turn skepticism into a finding quota. A clean result is valid only when the attacks had enough evidence to run.

## Review flow

Use this flow in order. Use the attack lists only to complete the selected attack.

1. Extract the decision, scope, explicit claims, stated non-findings, assumptions, and required evidence.
2. Convert each decision-relevant claim into a testable proposition with a concrete consequence if false.
3. Build the smallest system or change map needed to challenge the proposition.
4. Run hostile attacks that fit the artifact type and critical path.
5. Seek disconfirming evidence before accepting a claim.
6. Classify each result as `refuted`, `observed risk`, `withstood`, or `untested`.
7. Report only counterexamples, material evidence gaps, and risks that can change the decision.

Do not invent facts to make the review adversarial. Mark a claim `untested` when the repository, runtime, credentials, or evidence needed to challenge it is unavailable.

Perform read-only analysis by default. Run fault injection, malformed-input tests, retries, cancellations, migrations, or interruptions only in a hermetic test environment or with explicit authorization for the exact non-production target. Do not interrupt shared services, alter user data, send provider traffic, or expose credentials merely to create adversarial evidence. Mark the claim `untested` when safe evidence is unavailable.

## Claim Ledger

For every important claim, record:

| Field | Record |
|---|---|
| Claim | The exact assertion or a faithful short paraphrase. |
| Origin | `artifact claim`, `review conclusion`, `stated non-finding`, or `reviewer hypothesis`, with a source anchor. |
| Decision | What would be approved, rejected, built, merged, or deferred because of it. |
| Falsifier | The smallest observation that would prove the claim false or incomplete. |
| Evidence | File, symbol, diff hunk, trace, test, command, or plan section. |
| Status | `refuted`, `observed risk`, `withstood`, or `untested`. |

Treat absence claims as claims. Examples include “there is no duplicate owner,” “the migration is safe,” “tests cover the failure path,” and “no P1 issues remain.”

Use a reviewer hypothesis only to direct investigation. Do not describe it as a refuted artifact claim unless the artifact or review made that claim. Report direct evidence for a hypothesis as an `observed risk`: evidence-backed, decision-relevant, and not an assertion that the artifact made a false claim.

## Hostile Attacks

Choose attacks that can change the decision. Follow a critical input to its observable result rather than inspecting isolated files.

### Authority and state

- Find a second writer, cached copy, fallback, or UI-side policy that contradicts the claimed source of truth.
- Simulate retry, duplicate delivery, cancellation, stale read, concurrent action, partial write, restart, and rollback boundaries in an authorized test environment.
- Check whether a migration leaves callers, data, tests, or feature work on two active owners.

### Failure and recovery

- For each selected critical external call, persistence step, or handoff, simulate interruption at the point where state changes in an authorized test environment.
- Test whether failure status is observable, bounded, recoverable, and safe to retry.
- Challenge claims based only on happy-path checks, mocks that cannot fail realistically, or unit tests that omit side effects.

### Boundaries and trust

- Trace untrusted input, paths, provider output, credentials, permissions, and serialized state across boundaries.
- Look for an implicit authority grant, lossy mapping, unvalidated return, cross-tenant or cross-project reach, secret exposure, or canon write before a required gate.
- Challenge architecture claims with the actual entry point, registration, routing, schema, and generated-contract evidence.

### Change and migration

- Compare stated scope with every direct caller, contract, persistence format, generated artifact, and test seam.
- Search for obsolete routes, duplicate feature flags, compatibility shims without removal conditions, and new behavior in an old path.
- Simulate version skew, missing old data, interrupted rollout, downgrade, and partially upgraded clients where applicable.

### Verification and observability

- Distinguish a test that executes code from one that proves the stated behavior at an observable seam.
- Challenge generated evidence that can be accepted solely from a status flag: test whether its producer, version, provenance, timestamps, and freshness constraints are actually validated by the decision gate.
- Exercise malformed, empty, oversized, delayed, duplicated, and boundary-value inputs only in an authorized test environment.
- Challenge evidence that does not run the changed path, does not assert the required invariant, or cannot reveal production failure.
- Challenge a completion claim that rests on passing tests when the repository's typecheck, build, format, or scoped local gate fails for the changed path.
- Challenge an accessibility claim backed only by `tabindex` or handler presence when ARIA state values, focus lifecycle, skip-link routing, or reduced-motion behavior are untested.
- Verify diagnostics, metrics, traces, user-visible status, and recovery instructions when the decision depends on operability.

### CQT report challenge

When reviewing CQT output, independently test its top findings, recommended canonical owners, severity rankings, and deliberate non-findings.

- Verify that each cited path proves the observation rather than merely being nearby code.
- Try to find a critical flow, direct caller, state transition, or external boundary omitted from the CQT scope.
- Challenge a proposed owner that lacks authority, lifecycle control, or an enforceable contract.
- Challenge a low-risk or non-finding conclusion with an executable counterexample, not a preference.
- Distinguish an evidence gap in CQT from proof that its conclusion is false.

## Finding Standard

Create a finding only when it identifies a credible decision-changing counterexample or evidence gap. Include:

```text
ID: ADV-001
Status: Refuted | Observed risk | Untested
Severity: P0 | P1 | P2
Claim challenged: <claim and source anchor>
Claim origin: Artifact claim | Review conclusion | Stated non-finding | Reviewer hypothesis
Attack: <hostile scenario or falsification test>
Evidence status: Observed | Inferred | Unavailable
Evidence: <direct source, command result, trace, or unavailable coverage>
Consequence: <what decision becomes unsafe or unsupported>
Required action: <smallest check, clarification, or correction>
```

Use `P0` for a credible safety, security, data-loss, or release-blocking counterexample. Use `P1` when the decision is unsafe without correction or evidence. Use `P2` for a bounded concern that should change follow-up work but not the present decision.

Keep evidence status explicit:

- `observed`: Directly reproduced or shown by a source artifact.
- `inferred`: Strongly suggested by evidence but not reproduced; state what would verify it.
- `unavailable`: Needed evidence could not be inspected; do not state the claim is false.

## Output

Return a concise Markdown report:

```markdown
# Adversarial Review: <artifact>

Decision challenged: <decision>
Verdict: Blocked | Unsafe without changes | Evidence incomplete | Withstood the tested attacks

## Scope And Evidence

<artifact, source, commands, and material coverage limits>

## Claim Results

| ID | Claim and origin | Status | Attack | Evidence status | Evidence | Decision effect |
|----|------------------|--------|--------|-----------------|----------|-----------------|

## Findings

<only ADV findings that require action>

## Claims That Withstood Attack

<brief list, with attack and evidence>

## Untested Claims

<claim, missing evidence, and smallest next check>

## Decision

<what may proceed, what must change, and the exact evidence needed to unblock>
```

Do not reveal private chain-of-thought. Do not claim a verdict from unexecuted checks. Do not recommend a broad rewrite when a narrow check or correction resolves the risk.

Select the verdict in this order:

1. Use `Blocked` when an observed or strongly inferred P0 counterexample or observed risk makes the decision unsafe.
2. Use `Unsafe without changes` when a P1 counterexample or observed risk requires a correction before the decision.
3. Use `Evidence incomplete` when any material claim is untested or has unavailable evidence, even if no counterexample was found.
4. Use `Withstood the tested attacks` only when every material claim received a proportionate attack and none is refuted, an observed risk, or materially untested.

## Completion Check

Before finishing:

1. Confirm that every high-impact conclusion was challenged by a plausible falsifier.
2. Confirm that every finding has direct evidence or an explicit unavailable-coverage limit.
3. Confirm that the review distinguishes refuted claims, observed risks, and untested claims.
4. Confirm that the decision names the smallest evidence or correction required to proceed.
5. Confirm that all active attacks ran only in an authorized test environment.
