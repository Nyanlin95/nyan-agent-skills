# Frontend system contracts

Adapt the relevant contracts to the target repository. The initial guidance came from Agent Bot's frontend principles; draft acknowledgement and replay refinements also draw on Agent Stead and Agent Bot source inspected on 2026-10-13. Keep product-specific visual contracts, architecture, migration order, and verification results in their local owners. Treat this reference as intended behavior, not implementation proof.

## Give each kind of state one owner

Separate authoritative product state from temporary presentation state.
Do not distribute copies of the same server record across unrelated components.

| State | Appropriate owner | Lifecycle |
| --- | --- | --- |
| Durable product records | Authorized server and persistence layer | Server revision, transaction, or event history |
| Cached server reads | One query/cache layer | Identity, freshness, invalidation, eviction |
| Navigation | Router and URL where meaningful | Direct entry, back, forward, reload |
| Unsaved form values | Form owner | Edit, validate, submit, conflict, discard |
| Temporary interaction | Nearest relevant component | Open, focus, hover, selection |
| Stream or event projection | One ordered event consumer | Snapshot, cursor, replay, reconciliation |
| Authentication scope | Auth boundary | Sign-in, expiry, revocation, sign-out |

Derive values when possible. Do not store both a selected identifier and a copied
selected record without a clear synchronization rule. A cache is a read model,
not permission to accept a write or report a durable outcome.

Keep dependency direction explicit:

```text
Product route and workflow
    -> shared UI components -> semantic tokens and interaction primitives
    -> domain reads and mutations -> authorized API -> durable product owner
    -> event projection -> ordered event source
```

Shared visual components should not know provider credentials, route-specific
fetch paths, or product persistence rules. Domain data modules should not import
cards, dialogs, or other presentation components.

## Design the dependency path before optimizing requests

List what the first useful view actually needs. Start independent reads together.
Keep necessary dependencies, such as authorization before private data access.
Separate optional work from the minimum response needed to continue the task.

An aggregate endpoint is useful when its data shares authorization, freshness,
and failure semantics. Split it when unrelated dependencies delay or fail the
whole response. More endpoints are not automatically better.

Return enough metadata for the initial view without per-row follow-up requests.
Examples include labels, image URLs, status summaries, and pagination cursors.
Use bounded responses and pagination where content can grow without limit.

Treat provider discovery, large reports, and secondary panels as independent
resources when the primary screen can function without them. A slow optional
service should not erase unrelated content.

## Make navigation preserve context

Keep shared shells mounted across related routes. Place loading and error
boundaries around the smallest independently useful region.
Preserve scroll, selection, and drafts according to the product contract.
Reset them deliberately when the entity or authentication scope changes.

Maintain a stable component tree between cold, cached, and refreshed states.
Do not change component identity merely because a module or request has resolved.
In React, component type, position, and keys determine state preservation.
[React state identity](https://react.dev/learn/preserving-and-resetting-state)

Support direct links and browser history. A fast internal click path is incomplete
if reload, back, forward, or expired authentication behaves differently.
Keep route transitions and focus announcements understandable to screen readers.

Choose server and client rendering by responsibility. Server rendering can provide
authorized initial content. Client state supports ongoing interaction and live data.
Avoid fetching the same initial resource twice across that boundary.

## Treat caching as a consistency contract

Define each read once. Navigation, prefetch, refresh, and the rendered consumer
must use the same identity, parameters, and response interpretation.

Every cached resource needs:

- An identity that includes account or tenant scope and all result-changing parameters.
- A freshness duration based on how quickly its meaning changes.
- A retention limit separate from freshness, with bounded memory use.
- Pending-request deduplication and a rule for cancellation.
- Mutation and event invalidation rules.
- Explicit behavior for stale data, unavailable data, and authorization failure.
- A reset rule for authentication and permission changes.

Do not put secrets into cache keys, URLs, diagnostics, or browser persistence.
Use an opaque revision to distinguish credential-dependent results.
Authorize every server request even if the browser has a cached result.

A stale result can remain useful during refresh. Mark its age when it affects
the user's decision. Do not present stale permissions, prices, or resource
availability as a fresh guarantee. The server validates consequential writes.

After a successful mutation, reconcile the returned authoritative result and
invalidate affected lists or aggregates. Do not refetch the whole application.
Reject late results from a prior account, entity, or query generation.

Default to memory caching for sensitive authenticated data. Persistent offline
storage requires an explicit product need, isolation model, retention policy,
and deletion behavior. A service worker is not a prerequisite for a good frontend.

## Prefetch only work likely to help

Prefetch moves read work earlier. It does not remove that work or make stale data
correct. Its value depends on the chance of use, latency saved, and resource cost.

| Trigger | Suitable work | Constraint |
| --- | --- | --- |
| Visible navigation | Small route resources | Use the router's existing scheduling first. |
| Pointer intent or keyboard focus | Likely destination data and code | Deduplicate with the eventual consumer. |
| Explicit selection | The selected dependent resource | Cancel or ignore obsolete selections. |
| Idle time | Small, highly likely next work | Do not compete with input, streaming, or critical reads. |

Keep code, application data, and assets distinct. A router can warm a JavaScript
chunk without warming data fetched by a mount effect. Next.js automatic route
prefetch runs in production and varies by route and cache configuration.
Read the installed framework documentation before changing that configuration.
[Next.js prefetching](https://nextjs.org/docs/app/guides/prefetching)

Set a concurrency and payload budget. Respect reduced-data preferences where
available. Do not depend on hover for touch users. Navigation must work normally
when no prefetch occurred or a prefetch failed.

Prefetch must not submit forms, mark content read, create records, run inference,
send messages, or execute approvals. A read-only endpoint can still be expensive.
Rate-limit costly discovery and stop speculative work from exhausting capacity.

Measure useful prefetch hits, unused work, duplicate reads, and click-to-content
time. Reduce speculation when it wastes bandwidth or delays active work.

## Define the full state contract

| State | Expected behavior |
| --- | --- |
| Cold load | Show a stable shell and an honest placeholder for unknown content. |
| Cached load | Render usable cached content immediately when policy permits. |
| Refresh | Retain usable content and show local progress. |
| Empty | Explain the absence and offer an existing next action where appropriate. |
| Pending mutation | Prevent accidental duplicates and keep the task context. |
| Success | Reflect confirmed state and keep feedback proportional to the action. |
| Failure | Preserve valid input and show the failure beside its task. |
| Conflict | Explain that state changed and provide reload or reconciliation. |
| Offline or interrupted | Distinguish disconnected reads from uncertain writes. |
| Unauthorized | Remove private content and cached access immediately. |

Use skeletons only when real content is unknown. Reserve realistic geometry.
Do not replace useful content with a full-screen spinner during background work.
Avoid artificial loading delays added to make an animation visible.

Optimistic updates fit reversible, predictable actions with reconciliation.
Keep irreversible, financial, permission-sensitive, and external effects pending
until the authoritative owner confirms them. An aborted browser request does not
prove that the server cancelled a write.

## Reconcile drafts and uncertain submissions

Keep editable draft identity separate from submitted operation identity. Capture the submitted value and revision before dispatch; acknowledge or clear only that revision. Retain typing, erasure, attachments, or validation changes made while the request was pending. Do not let a delayed success replace the user's newer draft.

Scope draft and pending-operation state by account/tenant and target. Retain durable browser recovery only when the product explicitly supports it, with bounded retention and account-switch cleanup. Do not introduce persistent private state solely as a polish optimization.

For an uncertain write, preserve the exact operation needed to query or replay the same submission through its existing server contract. Reconcile it independently of the current editable form: newer invalid input must not prevent learning whether the previous submission succeeded. After confirmed completion, treat a deliberate identical submission as a new intent. Do not silently retry an external effect whose owner cannot reconcile it safely.

Distinguish local edit generation, server revision, and command receipt. Use the server revision for conflict detection and the edit generation to reject stale UI acknowledgements. Require an explicit conflict choice before overwriting another device's changed draft where the product contract demands it. Do not infer that an empty remote draft is unchanged; it may be the revision consumed by a successful send.

Verify lost acknowledgement followed by newer typing and erasure, reload with pending recovery when supported, cross-device conflict, and account/target change when those paths are affected. Assert the retained draft and durable effect count after recovery.

## Reconcile realtime delivery with durable history

Give one consumer ownership of snapshot, cursor, pushed events, replay, and terminal state. Treat display deltas and wake signals as provisional delivery; advance the durable cursor only according to the authoritative ordered source. Deduplicate repeats and catch up gaps rather than trusting delivery order.

Fence consumer callbacks by run/entity/session generation. Abort and dispose obsolete subscriptions and ignore their late results. Start a replacement replay without allowing the old session to overwrite it. Preserve committed results when cancellation or a transport failure interrupts display.

Use existing reconnect catch-up or bounded polling when realtime is unavailable. State whether the implementation provides durable cursor replay or only read invalidation; neither a socket connection nor periodic refresh proves ordered recovery. Verify duplicate/out-of-order delivery, a missed wake, disconnect/reconnect, and session replacement where the changed owner handles them.

## Build the visual system from foundations through workflows

Use atomic design as a dependency and review method, not a requirement to create
folders named atoms, molecules, and organisms.

| Layer | Owns | Must survive |
| --- | --- | --- |
| Foundations | Semantic color, typography, spacing, size, radius, elevation, motion | Themes, contrast, zoom, platform differences |
| Primitives | Button, field, icon, select, feedback, focus mechanics | Input methods and full state contract |
| Compositions | Form row, card, toolbar, dialog body, resource row | Long text, nested surfaces, overflow |
| Workflows | Edit, save, recover, navigate, approve | Dependency changes, errors, interruptions |
| Screens and shells | Task hierarchy and navigation | Responsive layout, direct entry, return visits |

Review upward to find composition failures. Review downward to find the shared
owner. A recurring defect belongs in the narrowest owner that explains it.
Recheck the shared control alone and inside its real parents after a correction.

### Spacing expresses relationships

Keep strongly related elements closer than separate groups. Use semantic spacing
roles for inline content, field groups, card sections, and page sections.
Do not enlarge every gap because one screen feels cramped.

Assign each gap to one owner. A parent gap plus child margins can double spacing.
Nested wrappers should provide an actual layout, semantic, or behavior function.
Remove wrappers that only accumulate padding or obscure alignment.

Let content determine repeated row height. Fixed heights require a defined
truncation policy. Scroll containers must not compress children below readable size.
Align single-line icon feedback centrally. Define multiline alignment explicitly.

### Tokens express purpose

Use semantic roles such as page surface, card surface, field surface, muted text,
quiet icon, and destructive feedback. Raw palette values belong in the token owner.
Differentiate adjacent surfaces in actual compositions, including nested cards.
Do not add borders as a universal substitute for a missing surface hierarchy.

Keep focus treatment visible and singular. The product specifies its thickness,
offset, contrast, and states. Focus indication and resting boundaries have different jobs.

### Components carry the default design

Prefer a small set of clear variants over arbitrary style overrides. Separate
appearance from semantics: links navigate, buttons perform actions, and selection
controls expose selection. Icon-only buttons still need accessible names.

Reuse approved icon libraries through one adapter. Avoid mixing replacement icons,
handmade SVGs, and library icons for the same meaning. Brand assets remain distinct.
Use tooltips for information that helps the task, not automatic repetition of labels.

## Reuse established interaction mechanics

Prefer native controls when they satisfy the product. For complex custom controls,
evaluate maintained primitives for focus, keyboard, portals, dismissal, and positioning.
Keep product tokens and composition in the application's own wrappers.

A library does not prove accessibility or prevent application CSS defects.
Test its integration with disabled states, long content, zoom, and nested surfaces.
Choose a searchable combobox when users must find an entry in a large collection.
Base UI explicitly recommends Combobox for this case.
[Base UI Select](https://base-ui.com/react/components/select)

Evaluate dependency cost, supported framework versions, maintenance, and migration
scope. Do not add two libraries for the same interaction responsibility.
Remove the replaced implementation after all consumers migrate.

## Budget rendering, assets, and background work

Measure route bundles before splitting them. Defer expensive optional panels at
meaningful boundaries. Avoid tiny chunks that create new sequential requests.
Warm a deferred panel when intent makes it likely to open.

Reserve image and chart dimensions. Request appropriate image sizes. Use stable,
content-versioned asset URLs and match font preload URLs with actual font requests.
Limit font families, weights, and third-party scripts to real needs.

Keep expensive parsing, formatting, and hidden rendering off the active input path.
Chunk background tasks or move suitable computation to a worker when measurements
show main-thread pressure. Virtualize long collections only when needed, preserving
focus, search, accessibility, and scroll anchoring.

Avoid rendering a whole transcript again for each incoming token. Bound history
loading and reconcile updates through one event projection. Profile before adding
memoization or another state store.

Honor reduced motion. Use motion to explain changes and preserve continuity.
Do not animate layout merely to hide latency or block the next action.

## Measure the actual journey

Define a frequent user action, its readiness/completion signal, and the metric boundary before optimizing it. Measure the same action with controlled content, build, cache state, and external substitute or provider lane. Keep wire bytes, decoded bytes, request counts, main-thread work, database activity, and elapsed time distinct; do not sum overlapping spans or call a local sample a production percentile.

Drive the real browser or API journey rather than invoking collector internals or manufacturing busy work. Require the named scenario and its necessary measurement fields to be present before evaluating a budget. Missing data is unavailable evidence, not zero cost. Keep diagnostics bounded and free of prompts, credentials, or raw private content.

Remove unnecessary work at its owner before adding prefetch, caches, or memoization. Preserve authorization, effect ordering, durability, and useful feedback. Update a baseline or budget only for an explained workload or contract change with matched before/after evidence; do not loosen it merely because a regression fails.
