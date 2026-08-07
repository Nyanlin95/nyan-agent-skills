---
name: cqt-review
description: Review a repository for code quality, code taste, ownership, abstraction, dependency direction, state modeling, failure behavior, and migration lifecycle. Use when auditing an existing codebase, reviewing a feature or pull request beyond correctness, identifying architectural friction, assessing a forked or parallel implementation, or planning beta-safe quality improvements and ownership cutovers. Prefer bounded, evidence-based findings and do not expand a beta review into a repository-wide rewrite.
---

# CQT Review

Review code for **Correctness, Quality, and Taste** while respecting the repository's current architecture, delivery stage, and change budget.

Review code for reliable behavior, visible intent, clear ownership, predictable abstractions, and affordable change.

The canonical owner is the one module, component, or service that owns a rule or decision.

## Language behavior

Read [references/language-behavior.md](references/language-behavior.md) when a finding depends on language or runtime semantics.

Read [references/framework-behavior.md](references/framework-behavior.md) when framework lifecycle, reactivity, rendering, dependency injection, or server-client boundaries affect a finding.

Confirm the language version, runtime, compiler settings, and framework behavior before reporting the finding. Do not turn a language preference into a correctness claim.

## Evidence discipline

Classify each material claim as one of these:

- **Observed:** a current source, test, configuration, diff, trace, log, or rendered result proves the claim.
- **Inferred:** the claim follows from observed evidence but needs an assumption about an unobserved path.
- **Unavailable:** the required artifact, environment, credential, or runtime path was not available.

State the evidence type and its limit. Do not present an inference as an observed defect. Reduce confidence or omit a finding when the evidence cannot support it.

For a pull request or feature review:

1. Read the repository status and relevant diff.
2. Identify the behavior that the diff changes.
3. Trace the changed path and its direct canonical owners.
4. Compare the new behavior with the established contract and direct tests.
5. Separate a change-introduced finding from pre-existing debt.

Do not attribute an existing defect to the reviewed change without evidence.

Use static checks and architecture contracts to prove static properties. Use a test, trace, or rendered user journey to prove runtime behavior. Do not claim a workflow succeeds from static evidence alone.

## Generated evidence

When a release or approval claim depends on a generated artifact:

1. Trace the producer that writes the artifact.
2. Inspect the emitted artifact, not only the producer source.
3. Check that the consumer validates the fields that carry the claim.
4. Distinguish a current runtime result from a stored artifact that may be stale or manually changed.
5. Record the artifact version, provenance, timestamp convention, and freshness rule when they affect the decision.

Do not treat a passing status field as proof of the workflow unless the producer, consumer, and observable artifact agree on the claimed behavior.

## Review authority and active checks

Review artifacts and report findings by default. Do not edit code, data, configuration, infrastructure, or external systems unless the user separately authorizes implementation.

Run only read-only inspection and local, hermetic verification by default. Before an active check can mutate data, call a provider, send a message, charge a payment method, or interrupt a process, require explicit authorization for the exact non-production target. Otherwise, record the runtime evidence as unavailable.

When a user authorizes a fix, hand the accepted finding to `implementation-quality`. Keep CQT responsible for the finding, its evidence, the recommended owner, and the required verification.

## Review flow

Use this flow in order. Use the detailed review sections only to complete the current step.

1. Set the scope, delivery stage, review authority, and evidence limits.
2. Map the relevant system owners, state boundaries, external boundaries, and critical flows.
3. Trace each selected flow from input to outcome, including failure and recovery.
4. Review ownership, abstraction, dependencies, state, effects, and tests at the affected seams.
5. Rank evidence-backed findings and name the smallest responsible correction.
6. Report checks, unavailable coverage, remaining risk, and deliberate non-fixes.

## Change reach and rationale

For a changed behavior, state the safety claim, then trace its direct callers, consumers, state or persistence boundary, external boundary, and failure or recovery path. Follow only the paths that can affect that claim. Run code when static inspection cannot prove the claim.

Do not infer design intent from code shape alone. When rationale affects a finding, inspect available decision records, issue or pull-request discussion, tests, documentation, and commit history separately. Label the rationale as observed, inferred, or unavailable. State competing plausible explanations when the evidence cannot select one.

## Core model

Evaluate three separate dimensions.

### Correctness

Determine whether the code produces the required behavior safely.

Check:

- primary success paths;
- expected failure paths;
- input validation and trust boundaries;
- authentication and authorization;
- state consistency;
- destructive or financial operations;
- concurrency, retries, and idempotency;
- migrations and compatibility;
- tests around important observable seams.

Correctness findings may block release.

### Quality

Determine whether the implementation is understandable and maintainable.

Check:

- canonical ownership;
- control-flow clarity;
- dependency direction;
- abstraction boundaries;
- explicit state and error representation;
- side-effect visibility;
- locality of change;
- testability;
- accidental complexity.

Quality is about whether engineers can safely understand and change the code.

### Taste

Determine whether the code's shape fits the problem and repository.

Check:

- whether top-level code expresses product or domain intent;
- whether concepts are modeled at the right abstraction level;
- whether similar decisions are represented consistently;
- whether abstractions hide mechanics without hiding meaning;
- whether names communicate role, policy, or constraint;
- whether the implementation uses ordinary, direct mechanisms;
- whether ceremony, generality, or indirection exceeds present needs.

Taste is not personal style preference. Tie every taste finding to comprehension, ownership, consistency, misuse risk, or change cost.

## Review stance

Use these principles throughout the review:

1. **Express intent.** Higher-level code should state what the system is trying to accomplish rather than narrating low-level mechanics.
2. **Follow ownership boundaries.** Put each policy, invariant, lifecycle, and integration decision in its canonical owner.
3. **Make the underlying behavior understandable.** An abstraction may hide details, but callers should predict its effects, costs, failures, and purpose.
4. **Prefer coherent local design.** Do not demand a repository-wide architecture migration to improve one critical seam.
5. **Preserve useful repository conventions.** Do not replace an established pattern merely because another pattern is fashionable.
6. **Distinguish blockers from adjacent debt.** Broad existing problems are not automatically blockers for a bounded beta change.

## Product and runtime evidence

Connect each architecture finding to a critical user journey.

1. Name the user problem.
2. Name the workflow that owns the behavior.
3. Identify the canonical state that the behavior creates or changes.
4. Define the failure that the user can observe.
5. Identify the runtime evidence that proves the behavior.

For a multi-phase workflow, find evidence for:

- input identity and revision;
- selected context and configuration;
- intermediate requests or artifacts;
- external dependency and version choices;
- diagnostics and policy decisions;
- state mutations and commit boundaries;
- the final observable outcome.

Prioritize provenance, idempotency, recovery, and canonical-state correctness at trust boundaries.

Recommend new test infrastructure only when it protects a durable product invariant or closes an evidence gap.

## Domain language

Use the existing domain model as review evidence. Read the relevant `CONTEXT-MAP.md` and `CONTEXT.md` when they exist. Compare the terms in code, tests, APIs, and user-visible behavior with the glossary.

Flag a domain-language issue when an ambiguous, overloaded, conflicting, or missing term causes an incorrect owner, invalid state, contradictory policy, unsafe boundary, or misleading workflow. Report a term variation only when it affects behavior, ownership, state, or a boundary.

When the review cannot identify a canonical owner because the model itself is unresolved, state:

1. The ambiguous term or relationship.
2. The competing meanings found in the code or glossary.
3. The concrete scenario that requires a decision.
4. The affected workflow, policy, or ownership boundary.

Do not create or edit a glossary or ADR during a CQT review. Report the unresolved question for a separate domain-modeling decision. Resume the review against the resolved model.

## Review preparation

Before evaluating individual files:

1. Identify the repository's delivery stage: prototype, beta, production, or mature platform.
2. Identify the requested review scope: repository, subsystem, feature, pull request, or critical flow.
3. Locate the entry points.
4. Locate the core modules and domains.
5. Locate the state stores and databases.
6. Locate the external integrations and authentication boundaries.
7. Locate the background jobs and queues.
8. Locate the shared UI layers and design system.
9. Locate the test layers and deployment units.
10. Infer the architecture from repeated code, not only folder names or documentation.
11. Identify the critical user flows before you review files alphabetically.
12. Locate the versioned plan or roadmap that tracks the requested scope and compare its status markers with the delivered state; a stale status marker is evidence of an undocumented or incomplete change.

If scope is broad, first produce a system map. Do not immediately generate a long list of local style observations.

## Critical-flow tracing

For each important flow, trace:

```text
Input
→ parsing and validation
→ authorization
→ application workflow
→ domain decision
→ state mutation
→ external side effects
→ response or visible outcome
→ failure recovery
```

Record:

- Identify the current owner of each decision.
- Find duplicated or conflicting rules.
- Identify irreversible effects.
- Identify partial-failure points.
- Check retry behavior.
- Find where external data becomes internal state.
- Identify the smallest test seam that proves behavior.

Prioritize end-to-end understanding of a few critical flows over shallow inspection of every file.

## Intent and workflow review

The top-level path should read as a recognizable workflow.

Prefer code shaped like:

```ts
async function enrollStudent(command: EnrollStudentCommand) {
  const course = await courses.requireAvailable(command.courseId);
  const student = await students.requireEligible(command.studentId);

  const enrollment = course.enroll(student);

  await enrollments.save(enrollment);
  await notifications.sendEnrollmentConfirmation(enrollment);

  return enrollment;
}
```

Be suspicious when the main path is dominated by:

- generic names such as `process`, `execute`, `handle`, or `manage`;
- framework mechanics;
- deeply nested branching;
- callback plumbing;
- boolean modes;
- unrelated side effects;
- data-shape conversion noise;
- jumps through multiple trivial wrappers.

Ask:

> Can a reader describe the operation by reading the top-level function or component alone?

Do not require every detail to be hidden. Important ordering, branches, and side effects should remain visible.

## Ownership review

For every important decision, ask:

> Which concept, layer, or boundary genuinely owns this rule?

Typical ownership examples:

```text
Button accessibility and interaction states → design-system Button
Feature composition                         → feature or page
Payment eligibility                         → payment or account domain
Transaction boundary                        → application workflow or repository boundary
HTTP serialization                          → transport layer
Provider response mapping                   → integration adapter
Authentication token refresh                → authentication infrastructure
```

Flag:

- the same business rule implemented in several layers;
- feature behavior embedded in design-system primitives;
- domain policy embedded in controllers or views;
- provider-specific response shapes leaking into application code;
- database models treated as the public domain interface;
- convenience modules that become parallel owners;
- modules that depend on one another in both directions.

Defensive checks may exist in more than one layer, but the policy must still have one canonical owner.

## Abstraction review

Treat an abstraction as a boundary that allows one layer to express intent without owning the mechanics below it.

A good abstraction should do at least one of the following:

- represent a stable domain or UX concept;
- express a useful named action or policy;
- establish a real ownership boundary;
- isolate an external dependency, lifecycle, resource, or platform mechanism;
- protect an invariant;
- make invalid use or invalid state harder;
- unify cases that currently change for the same reason;
- provide a stable contract over unstable mechanics.

Do not create or preserve an abstraction merely because:

- code is long;
- two snippets look alike;
- a helper may be reused someday;
- a file exceeds a preferred line count;
- a framework call can be renamed;
- an interface feels architecturally proper;
- a generic component can support more modes.

### Predictable internals

A caller should not need implementation details, but should be able to anticipate:

- what kind of work happens;
- whether I/O or network calls occur;
- which state may change;
- what failure categories are possible;
- whether retries are safe;
- which lower-level layers probably implement the behavior.

Prefer:

```ts
paymentGateway.authorize(payment)
```

over:

```ts
engine.process(context, options)
```

Prefer:

```tsx
<PaymentMethodSelector />
```

over:

```tsx
<Experience mode="conversion" context={data} />
```

The first examples name the action. The second examples hide the action.

### Decomposition is not automatically abstraction

A deep component or module tree may only rename structure.

Flag components or helpers such as:

```text
Page
└── PageContent
    └── ContentWrapper
        └── InnerContainer
```

unless each level owns a real layout contract, interaction pattern, policy, or reason to change.

Ask of every new abstraction:

1. State the intent in its name.
2. Identify the decision or mechanism that it owns.
3. Identify the details that callers no longer need.
4. Confirm that callers can predict its behavior.
5. Identify the current change that can modify it.
6. Inline it if it owns no meaningful concept or boundary.

Do not keep an abstraction that only renames structure.

## Design-system and component-tree review

Interpret a component tree as an abstraction tree only when each level translates higher-level intent into lower-level responsibility.

Typical layers:

```text
Feature intent
    CheckoutFlow

Domain intent
    PaymentMethodSelector
    OrderSummary
    PayButton

UX pattern
    ConfirmationDialog
    FormField
    LoadingAction

UI component
    Dialog
    Select
    Button

Primitive
    Stack
    Text
    Icon

Token
    spacing
    typography
    color

Platform
    HTML
    CSS
    browser accessibility APIs
```

Review whether:

- feature components express product workflows;
- domain components own domain presentation and rules;
- UX patterns own reusable interaction structures;
- design-system components own accessibility, visual states, and interaction behavior;
- primitives own low-level layout or rendering contracts;
- tokens abstract semantic design decisions rather than merely rename arbitrary values.

Do not require the conceptual component tree, source tree, and DOM tree to be identical.

Flag:

- design-system components that know business entities;
- domain components that manually reproduce design-system behavior;
- universal components with many behavioral flags;
- generic wrappers that obscure the rendered interaction;
- component extraction performed only to reduce JSX length.

## Dependency review

Dependencies should generally point toward stable policy:

```text
UI or transport
      ↓
Application workflow
      ↓
Domain policy
      ↓
Interfaces for external capabilities

Infrastructure implements the external interfaces.
```

Use this as a diagnostic model, not a mandatory repository-wide architecture.

Look for:

- domain code importing HTTP, ORM, or UI framework types;
- external SDK objects flowing through several layers;
- feature modules importing one another cyclically;
- shared utility modules becoming hidden dependency hubs;
- abstractions that require many unrelated dependencies;
- dependency injection that adds ceremony without substitution value;
- new dependencies introduced for small behavior already supported by the platform.

For beta work, fix dependency direction only where the current coupling threatens correctness, blocks the requested change, or would spread further.

## State review

Prefer state representations that make valid transitions clear and contradictory states difficult.

Be suspicious of:

- several booleans representing one lifecycle;
- loosely typed status strings;
- nullable fields whose valid combinations are undocumented;
- state mutations spread across UI, services, and persistence;
- hidden transitions inside generic setters;
- optimistic updates without rollback behavior;
- caches with unclear source-of-truth rules.

Prefer explicit state models around risky workflows:

```ts
type JobState =
  | { kind: "queued" }
  | { kind: "running"; startedAt: Date }
  | { kind: "succeeded"; result: Result }
  | { kind: "failed"; error: JobError };
```

Do not demand a state-model rewrite for every simple object. Focus on areas where invalid combinations can produce real beta failures.

## Failure and side-effect review

Keep success, failure, and important effects traceable.

Check:

- which operations can fail;
- what has already changed at each failure point;
- whether partial completion is possible;
- whether retries duplicate effects;
- where errors are translated;
- what the user sees;
- what is logged or measured;
- whether transactions cover the intended boundary;
- whether cleanup and compensation are reliable.

Flag innocent-looking abstractions that silently:

- write several records;
- publish events;
- send messages;
- charge payment methods;
- swallow errors;
- retry work;
- mutate global state.

Important effects may be encapsulated, but the API and workflow should communicate that they exist.

## Simplicity and code-shape review

Prefer:

- linear orchestration;
- explicit branches;
- named domain actions and policies;
- ordinary language and platform features;
- small stable interfaces;
- direct transformations;
- visible effect ordering;
- repository-native patterns;
- local duplication when cases may diverge.

Be suspicious of:

- custom mini-frameworks;
- universal managers or processors;
- metadata-driven pipelines;
- dynamic registries;
- reflection;
- configuration replacing ordinary control flow;
- complicated generic types;
- callback-heavy reuse;
- interfaces with one trivial implementation and no meaningful boundary;
- abstractions that require flags to serve unrelated callers.

Do not score code by line count, abstraction count, class count, or file count.

## Test review

Tests should prove observable behavior at the smallest reliable seam.

Check whether tests cover:

- the changed success path;
- important failure behavior;
- canonical domain policies;
- trust and authorization boundaries;
- state transitions;
- retry or idempotency behavior;
- integration mapping at external boundaries.

Run the repository's verification gates for the changed path, not only the unit tests. A change is incomplete when typecheck, build, format, or a scoped local gate fails, even if the tests pass. State which gates ran and which are unavailable.

Prefer tests that describe behavior and outcomes.

Be cautious when tests:

- assert many internal method calls;
- duplicate implementation structure;
- require broad fixture setup for a narrow policy;
- mock every dependency in the repository;
- pass only because ordering is accidentally fixed;
- omit the failure mode most likely to damage users.

Do not require a broad test-suite rewrite for a bounded beta improvement.

## Severity model

Classify findings by release impact.

### P0 — Must fix before beta

Examples:

- data loss or corruption;
- authorization or security flaws;
- unsafe financial or destructive operations;
- primary-flow crashes;
- unrecoverable inconsistent state;
- broken or unsafe migrations;
- exposed credentials;
- unsafe retry or duplicated execution;
- absent validation at a trust boundary.

### P1 — Fix in the changed or critical area

Examples:

- duplicated policy producing contradictory behavior;
- unclear ownership that blocks safe changes;
- hidden major side effects;
- untraceable failure behavior;
- coupling that directly obstructs the current work;
- invalid state combinations likely to occur;
- no reliable test for a critical changed seam;
- substantial duplicated business logic.

### P2 — Record without expanding scope

Examples:

- naming inconsistencies;
- awkward but stable old modules;
- superficial duplication;
- formatting preferences;
- possible future abstractions;
- theoretical scalability;
- dependency upgrades unrelated to the current behavior;
- repository-wide restructuring;
- minor component inconsistencies.

P2 findings do not block beta delivery unless several combine into a concrete P1 risk.

## Beta change policy

When reviewing beta code, apply this rule to the recommended correction:

> Recommend a complete ownership correction that preserves current behavior, gives the changed behavior a clear owner, and creates no new irreversible coupling.

Smallest does not mean careless. Coherent means:

- the workflow can be understood;
- the relevant policy has one canonical owner;
- important dependencies are contained;
- failure behavior is known;
- verification exists;
- temporary debt is narrow and removable.

Complete does not mean few files. Include the destination owner, direct callers, contracts, state boundaries, generated artifacts, and tests that must change to leave one canonical owner. Do not preserve a duplicate owner or partial route merely to make the diff smaller.

## Recommended change budget

Do not turn a review finding into an unlimited migration.

Unless the user sets another budget, use these defaults for a single fix:

- Modify every direct participant required to complete the ownership correction.
- Do not rename or move unrelated repository areas.
- Do not upgrade dependencies unless the behavior requires an upgrade.
- Add only the abstractions required by the corrected ownership boundary.
- Preserve public APIs when practical.
- Do not add a framework, registry, or general extension system.
- Stop when an issue is unrelated to the requested behavior.

File counts are guidance, not correctness constraints. Prefer a small number of coherent files, but do not distort ownership to satisfy a numeric limit.

## Dependency and legacy workarounds

Do not reject a beta task because the ideal architecture requires too many dependency changes.

When a dependency is broad, old, or difficult to replace, prefer containment.

### Code-owner and fork lifecycle

Treat a fork as a temporary parallel implementation. Flag a fork that becomes a second owner.

Review or plan the migration in this order:

1. Identify the old owner, callers, behavior, failures, and old-owner tests.
2. Require a focused parity test before the migration.
3. Require the parity test to compare behavior, state changes, errors, and side effects.
4. Require one explicit routing point for both paths.
5. Reject unrelated behavior in the new path.
6. Require new-owner tests for success, failure, invariants, and state transitions.
7. Require the parity test to pass before callers move to the new owner.
8. Require removal of the migration-only parity test after the move.
9. List the old code and old-owner tests that can be removed.
10. Report remaining callers, rollback effects, and verification evidence.
11. Forward the removal decision to the user.
12. Require explicit user approval before removal.

If both paths cannot use the same input, accept contract fixtures or recorded outputs. State the limits of this comparison.

Flag any fork that gets separate features, policies, or callers.

### Schema and data migration lifecycle

Use this lifecycle when a change alters persisted schema, stored data, or compatibility between deployed versions. Do not treat code-path parity as proof that the data migration is safe.

1. Identify the old and new schemas, data owners, compatibility window, and source of truth.
2. Require an additive schema change that old and new readers and writers can use before the rollout.
3. Require an idempotent, resumable backfill with explicit checkpoints and retry behavior.
4. Require production-shaped legacy fixtures that include malformed, partial, duplicate, and boundary records.
5. Define data invariants and a reconciliation method such as counts, checksums, or sampled record comparison.
6. Define deployment order and reader/writer authority for mixed-version clients.
7. Define the stop condition and the rollback boundary, or state the forward-recovery path when rollback is unsafe.
8. Require progress, error, invariant, and reconciliation signals before and during cutover.
9. Remove old reads, writes, schema, and migration code only after compatibility ends and reconciliation succeeds.

### Adapter

Hide an external or legacy API behind the narrowest meaningful capability.

```ts
interface PaymentAuthorizer {
  authorize(
    request: AuthorizationRequest,
  ): Promise<AuthorizationResult>;
}
```

Map provider-specific requests and responses inside the adapter.

### Anti-corruption mapping

Translate external schemas into internal models at the boundary.

```ts
const account = mapProviderAccount(providerResponse);
```

Do not let SDK or transport types spread through application and domain code.

### Compatibility wrapper

Wrap an awkward existing API instead of migrating every caller during unrelated work.

```ts
export async function saveEnrollment(
  enrollment: Enrollment,
): Promise<void> {
  await legacyEnrollmentRepository.upsert(toLegacyRecord(enrollment));
}
```

### Local canonical policy

When duplicated behavior must change now, establish one canonical policy for the active flow. Do not migrate every historical caller unless correctness requires it.

Document which legacy paths remain.

### Facade over dependency clusters

When a feature needs several low-level dependencies, introduce a feature-owned facade only when it represents a coherent capability. Do not create a generic service locator.

### Tactical duplication

Allow small duplication when extracting a common abstraction would couple cases that may diverge. Record the shared knowledge only when duplication risks inconsistent policy.

## Tactical debt rules

A beta workaround is acceptable only when it has:

1. **Narrow location** — it does not leak through many callers.
2. **Concrete reason** — the constraint is stated precisely.
3. **Removal condition** — the event that makes the workaround unnecessary is known.
4. **Protection** — a test or assertion preserves the intended behavior.
5. **No false abstraction** — the workaround is not disguised as a permanent generic framework.

Example:

```ts
// The beta API may return duplicate course IDs.
// Deduplicate at this boundary until enrollment API v2 guarantees uniqueness.
// Remove after all enrollment traffic uses v2.
const uniqueCourseIds = [...new Set(response.courseIds)];
```

## Agent non-refusal protocol

Do not stop merely because the repository contains broader architectural problems.

Distinguish:

- **true blocker** — prevents a safe implementation;
- **direct dependency** — must be handled for the requested behavior;
- **adjacent debt** — relevant context but not part of the fix;
- **unrelated debt** — report only when materially risky.

When the ideal solution exceeds beta scope:

1. Recommend the safest local version.
2. Isolate unstable dependencies behind a narrow boundary.
3. Verify the changed behavior and failure path.
4. Record the remaining risk.
5. State the condition that permits a larger migration.

Escalate rather than implement only when:

- the behavior cannot be implemented safely;
- a schema change risks irreversible data loss;
- security or authorization requirements are materially unknown;
- required credentials or external systems are unavailable;
- materially different product interpretations remain unresolved;
- existing tests or contracts prove the request conflicts with current requirements.

Do not cite “too many dependencies,” “large architecture,” or “would take too long” as sufficient reasons to refuse a bounded beta change.

## Detailed review passes

Use these passes to complete steps 2 through 4 of the review flow. Do not restart the review flow for each pass.

For a broad review, use these passes.

### Pass 1: System map

Map:

- List the entry points.
- List the core domains.
- List the major dependencies.
- List the state stores.
- List the external systems.
- List the critical flows.
- List the test layers.
- Identify the likely ownership boundaries.

Do not propose sweeping fixes yet.

### Pass 2: Critical-flow correctness

Trace three to five critical flows. Identify P0 and P1 risks first.

### Pass 3: Ownership and abstraction

Find incorrect owners, duplicated policies, opaque abstractions, and boundary crossings.

### Pass 4: State and failure

Check transitions, retries, idempotency, transactions, partial failure, and recovery.

### Pass 5: Taste and consistency

Check names, code shape, component layers, repeated patterns, API consistency, and test readability.

Do not lead with low-impact style findings while critical-flow behavior remains unclear.

## Finding format

Every finding must be specific and actionable.

```text
Title:
Severity: P0 | P1 | P2
Confidence: High | Medium | Low

Location:
The canonical file, component, module, or seam.

Observation:
What the code currently does.

Evidence:
Relevant symbols, call paths, tests, or runtime behavior.

Evidence status:
Observed, inferred, or unavailable coverage. State any material limit.

Change reach:
The direct consumers and runtime boundaries checked, or the unverified boundary.

Rationale status:
Observed, inferred, unavailable, or not material to this finding.

Domain-language status:
Resolved, or the unresolved term, scenario, and affected ownership boundary.

Why it matters:
The concrete correctness, ownership, comprehension, misuse, or change-cost impact.

Current owner:
Where the decision currently lives.

Recommended owner:
Where the decision should canonically live.

Smallest responsible change:
The beta-sized correction.

Dependency workaround:
Adapter, mapping layer, compatibility wrapper, local policy, tactical duplication,
or none.

Ideal later direction:
Include only when meaningfully different from the beta correction.

Verification:
The test, command, trace, or behavior that proves the correction.

Remaining risk:
What is deliberately not solved.
```

Avoid vague findings such as:

> The architecture should be more modular.

Prefer:

> Enrollment eligibility is implemented in both the API controller and React page. A course-limit change can create contradictory behavior. Move the canonical policy into the existing enrollment service, retain the UI check only for immediate presentation feedback, and add a service-level policy test.

## Review rubric

Score important areas from 1 to 5 only after gathering evidence.

| Area | Review question |
|---|---|
| Correctness | Do critical flows produce safe and expected outcomes? |
| Intent | Does top-level code communicate the product operation? |
| Ownership | Are decisions located in their canonical owner? |
| Abstraction | Do abstractions represent meaningful concepts or boundaries? |
| Predictability | Can callers anticipate effects, costs, and failure modes? |
| Dependencies | Do dependencies point toward stable policy and remain contained? |
| State | Are valid states and transitions represented clearly? |
| Failure | Are partial failure, retry, and recovery understandable? |
| Locality | Can a feature change without touching unrelated modules? |
| Consistency | Are similar product decisions modeled similarly? |
| Verification | Do tests exercise observable seams and important failures? |

Do not average the scores into a false precision metric. Highlight the lowest-scoring areas in critical flows.

## Output requirements

For a repository review, report:

1. State the scope and delivery-stage assumptions.
2. Show the system map and critical-flow map.
3. Report the highest-risk P0 and P1 findings.
4. Report ownership and abstraction findings.
5. Report dependency hotspots and safe containment options.
6. Separate code-taste findings from correctness findings.
7. List unresolved domain-language questions.
8. Give the recommended fix order.
9. List deliberate non-fixes.
10. List completed checks and evidence limits.

For a pull-request or feature review, report:

1. Describe the changed behavior.
2. Report correctness and failure findings.
3. Identify the canonical owner.
4. Report abstraction and dependency findings.
5. List unresolved domain-language questions.
6. Recommend the smallest responsible changes.
7. List the required tests and checks.
8. State the remaining risk.

Keep findings concise, evidence-based, and ranked. Do not produce a long inventory of minor observations merely to appear comprehensive.

## Completion test

Before finishing:

1. Trace the critical behavior from input to result.
2. Confirm one canonical owner for each important rule.
3. Confirm that each abstraction states intent and has predictable behavior.
4. Confirm that the design contains dependency costs and external boundaries.
5. Trace success, failure, and side effects.
6. Check that the state model matches the risk.
7. Keep each recommendation inside the change budget.
8. Separate blockers from adjacent debt.
9. Give a reliable verification method for each proposed change.
10. Stop before the review becomes an unrelated repository rewrite.
11. For a migration, check each migration lifecycle step in order.

A successful CQT review improves the code until the critical behavior has a clear owner, an understandable path, predictable boundaries, contained dependencies, and reliable verification—then stops.
