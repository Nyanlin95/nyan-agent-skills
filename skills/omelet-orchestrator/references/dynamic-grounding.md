# Dynamic Grounding

Ground every Omelet task in the evidence that is authoritative for its actual decisions. Keep the source set dynamic: discover it from the current task, exact repository state, active versions, environment, and external conditions instead of reusing a fixed bibliography or memorized best-practice list.

## Frame the grounding contract

Before finalizing the semantic plan, record:

- the decisions and material claims that must survive evidence;
- the current internal owners and observable state;
- the source classes that can answer each unresolved question;
- the required freshness identity and unavailable coverage;
- the threshold for adopting, adapting, rejecting, deferring, or reopening a decision.

Keep this inline for ordinary tasks. Create a separate research artifact only when the user or repository requests one.

## Scale the depth

| Depth | Use when | Required grounding |
| --- | --- | --- |
| Minimal | The task is mechanical, local, reversible, and fully resolved by current repository evidence. | Inspect the exact owner and caller or consumer, then run the smallest falsifying proof. External research is unnecessary. |
| Standard | The task includes judgment, an unfamiliar boundary, a shared owner, product behavior, or a changeable platform fact. | Triangulate current internal evidence with the relevant current primary external source and one independent empirical or comparative perspective when it can change the decision. |
| Deep | The decision is architectural, security-sensitive, difficult to reverse, high-blast-radius, market-defining, operationally consequential, or disputed. | Test alternatives against current system constraints, multiple applicable primary sources, empirical evidence, failure behavior, and explicit trade-offs. Add independent review when repository policy requires it. |

Increase or reduce the depth as evidence changes the uncertainty or blast radius. Do not force a fixed source count. Minimal grounding still requires current source inspection and proof.

## Route sources by domain

| Domain | Start with current task-local truth | Add dynamic sources when relevant | Do not infer |
| --- | --- | --- | --- |
| Code and debugging | Exact code, call sites, types, tests, lockfiles, generated artifacts, runtime reproduction, logs, and measured behavior. | Version-matched official documentation, specifications, source, changelogs, compatibility data, maintained examples, and issue history for the observed version. | A name or stale document does not prove behavior; a passing unit test does not prove an external or stateful boundary. |
| Product and workflow | User intent, canonical product plan, implemented behavior, analytics, research, support evidence, domain rules, and current constraints. | Current comparable products, market expectations, platform policies, customer evidence, and recent domain research. | Competitor behavior does not establish product fit or authorize copying its workflow. |
| Architecture and data | Current topology, ownership, schemas, migrations, data flows, dependency direction, deployment model, SLOs, cost, capacity, incidents, and ADRs. | Exact-version vendor contracts, current standards, maintained reference architectures, benchmarks with comparable workloads, recent postmortems, and applicable case studies. | A generic architecture pattern or vendor diagram does not prove suitability for this workload. |
| Design and interaction | User intent, rendered product, design system, brand, content, component owner, real states, and input behavior. | Current shipped UI patterns, visual-direction signals, platform releases, accessibility guidance, and relevant implementation constraints. | A trend, gallery, or concept does not prove usability, accessibility, product meaning, or brand fit. |
| Security and privacy | Current assets, trust boundaries, dependency inventory, permissions, data classification, threat model, controls, and attack surface. | Current vendor advisories, maintained vulnerability catalogs, exploit evidence, standards, platform security guidance, and regulatory obligations for the affected scope. | A severity label alone does not prove exploitability or remediation priority in this environment. |
| Operations and release | Current configuration, infrastructure state, deployment workflow, runbooks, metrics, traces, logs, incidents, quotas, and health. | Provider status, exact-version operational documentation, service limits, release notes, deprecations, and current regional behavior. | Configured, built, published, deployed, healthy, and live are not interchangeable states. |
| Content, policy, and legal | Verified product facts, canonical terminology, permissions, locale, brand voice, current policy owner, and the final artifact in context. | Current official regulations, platform policies, standards, primary records, and authoritative style or domain guidance. | Secondary summaries do not establish a current legal or policy requirement. |
| Data, AI, and providers | Current datasets, schemas, evaluation cases, model or provider configuration, prompts, limits, observed outputs, cost, latency, and failure behavior. | Exact model and API documentation, current pricing and limits, provider changelogs, safety policies, benchmarks with disclosed methods, and task-representative evaluations. | A benchmark, model name, provider claim, or remembered limit does not prove current task performance. |

Use only the rows that match the task. Add a domain-specific source class when the decision requires it rather than forcing the task into this table.

## Assign authority claim by claim

Do not create one universal source ranking. Use the source that owns the claim:

- Treat current code, routes, schemas, migrations, and machine-owned artifacts as the source of truth for implemented static structure.
- Treat a reproduction, trace, emitted artifact, render, integration check, or live observation as the source of truth for observed behavior in its recorded environment.
- Treat the user and canonical product owner as the authority for intended outcome and approved direction.
- Treat exact-version official documentation, specifications, and vendor contracts as authority for supported external behavior.
- Treat current analytics, research, incidents, and task-representative evaluations as empirical evidence, with their sampling and environment limits.
- Treat comparative products, case studies, galleries, trend reports, and community discussions as contextual evidence or hypothesis generators unless they expose direct primary evidence.

When prose and code disagree, distinguish intended, documented, implemented, tested, and observed behavior. Do not silently choose the most convenient source.

## Prove freshness and applicability

For each consequential changeable claim, record the relevant identity:

- task as-of time and observation time;
- repository revision and dirty-tree identity;
- dependency, API, model, platform, schema, policy, or document version;
- environment, region, configuration, feature flag, and data scope when they affect the result;
- source publication, update, retrieval, or live-observation time;
- the event that invalidates the evidence.

Collect or revalidate sources used to claim current, latest, supported, secure, compatible, recommended, available, priced, or live during the active task. An undated source can provide context but cannot establish currentness by itself. Refresh the grounding after a material change to the decision, source owner, repository state, dependency version, environment, or external condition.

## Resolve contradictions

1. State the exact claim on which the sources disagree.
2. Check version, environment, scope, date, and whether each source is normative, implemented, empirical, comparative, or editorial.
3. Test the disagreement in the current system when safe and proportionate.
4. Follow the source that owns the claim and applies to the current context.
5. Report an unresolved contradiction as a decision risk or unavailable boundary instead of averaging sources together.

Use external best practice to challenge local decisions, not to erase known local constraints. Use local convention to preserve product coherence, not to excuse a stale, unsafe, or disproven rule.

## Carry grounding through the work

Give each delegate the decision questions, current internal owner, allowed source classes, freshness identity, and protected behavior it needs. Require the delegate to separate observed, inferred, and unavailable claims and to return sources that changed or confirmed its decisions.

Before integration:

1. Confirm that material decisions still match the latest applicable grounding.
2. Recheck any source invalidated by implementation or environment changes.
3. Verify the result in the native medium and current boundary.
4. Report what was adopted, adapted, rejected, deferred, or unavailable and why.
5. State the as-of boundary for claims likely to drift.
