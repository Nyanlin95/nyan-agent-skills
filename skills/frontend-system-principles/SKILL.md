---
name: frontend-system-principles
description: Build or refactor interactive web application journeys whose correctness depends on frontend state ownership, navigation continuity, cache consistency, loading and recovery states, shared UI foundations, or measured delivery performance. Use for frontend system implementation across these boundaries. Do not use for read-only audits, isolated copy edits, or purely visual critique.
---

# Frontend System Principles

Make complete journeys understandable, responsive, and recoverable. Establish correct behavior in code first, challenge it with tests, and document ownership and tradeoffs last. Treat these principles as an intended standard, never proof that an application already meets it.

## Establish the journey

1. Read the target repository's frontend entry point, visual contract, architecture, and verification commands.
2. Identify the requested journey, its current implementation, and the routes and consumers that share its owners.
3. State the protected product behavior, including navigation meaning, workflow order, authorization, and data contracts.
4. Capture the relevant baseline in the running application or existing tests; label unavailable evidence.
5. Read the affected domains in [system-contracts.md](references/system-contracts.md) before choosing the implementation.

Keep the existing framework, brand, component library, and product conventions unless the requested outcome requires a change. Apply only the domains the journey needs. Do not turn a bounded repair into a frontend rewrite or a new offline engine.

## Implement through the owner

1. Assign each durable record, cached read, navigation value, draft, interaction state, event projection, and authentication scope to one owner.
2. Trace the dependency path to the first useful view, separating necessary authorization from independent reads and optional work.
3. Define the affected cold, cached, refresh, empty, pending, success, failure, conflict, interrupted, and unauthorized behavior before changing it.
4. Fix recurring defects in the narrowest shared component, token, layout, data, or lifecycle owner that explains them.
5. Migrate one complete journey and its direct consumers to the corrected owner.
6. Remove the replaced path after the migration is verified, subject to actual deployment compatibility requirements.

Keep authoritative writes on the server and temporary presentation state near its interaction. Preserve useful content, drafts, focus, and scroll according to the product contract. Reset private state at authentication boundaries. Keep speculative reads free of product side effects.

Use existing interaction primitives and verification tools. Add dependencies, persistent caching, virtualization, workers, or memoization only for a concrete requirement or measured constraint. Check installed versions and current official documentation before relying on framework-specific caching, prefetch, rendering, library behavior, or numerical performance thresholds.

## Prove the changed contract

1. Run the repository's checks for the affected paths.
2. Exercise one complete successful journey and its material failure or interruption paths.
3. Check affected direct entry, cold and warm navigation, browser history, refresh, and authentication transitions.
4. Verify visible changes with matched content, viewport, and state in the rendered application, including relevant long-content, narrow-parent, keyboard, zoom, and reduced-motion conditions.
5. Measure performance changes with a stated build, environment, dataset, cache state, device, network, sample count, and metric definition.
6. Confirm that the migrated consumers use one owner and that no obsolete path or unexplained exception remains.

Use state or integration tests for identity, invalidation, out-of-order results, conflicts, and event reconciliation. Use browser evidence for focus, geometry, scrolling, and real interaction. Use performance traces for critical-path claims. Do not substitute CSS-class assertions for layout proof or local timings for production percentiles.

## Report completion

Report the changed journey and owner, the user-visible effect, checks performed, and material unverified boundaries. Separate observed behavior from inference. Record any necessary exception's reason, owner, scope, and removal condition beside the repository's actual owner.
