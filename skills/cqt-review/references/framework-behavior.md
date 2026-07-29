# Framework behavior

Use this reference when framework behavior affects correctness, ownership, state, failure, rendering, or migration findings.

Confirm the framework version and enabled features. Separate framework behavior from the underlying language and runtime.

Use the repository's pinned documentation first. Use the official links in this file when the repository does not answer the question.

## Angular

- Components and services have lifecycle and dependency-injection scopes.
- A service is not always application-global. Its provider location controls instance ownership.
- Change detection depends on the configured strategy and runtime setup.
- `OnPush` does not make nested mutable state reactive.
- Signals track reads in synchronous reactive contexts. Reads after an async boundary are not tracked.
- RxJS observables can be cold or hot. Subscription ownership controls cleanup and duplicate work.
- `AsyncPipe` manages its subscription. Manual subscriptions need explicit cleanup.
- Route guards and client checks do not replace server authorization.
- Forms can have synchronous and asynchronous validation with different completion behavior.
- Zone-based and zoneless applications can schedule updates differently.

Review provider scope, subscription cleanup, change-detection assumptions, signal ownership, form timing, and authorization boundaries.

## Vue

- Vue 3 uses proxies for reactive objects. Raw and proxied identity can differ.
- Destructuring a reactive object can disconnect a value from later reactive updates.
- Refs use `.value` in JavaScript and can unwrap in templates.
- Computed values cache tracked derivations. Watchers own effects and cleanup.
- DOM updates are batched. Use the framework update boundary before reading rendered state.
- Component keys control instance reuse and local state preservation.
- Props flow down. Direct prop mutation breaks ownership even when JavaScript permits it.
- Provide and inject can hide shared mutable state and lifecycle ownership.
- Composables can create global or per-call state depending on declaration location.
- Server rendering requires hydration-compatible output and browser-safe module initialization.

Review proxy identity, lost reactivity, watcher cleanup, component keys, state ownership, and hydration behavior.

## React

- Render must remain free of external side effects.
- State is a snapshot for one render. Closures can retain an older snapshot.
- State updates can batch and do not mutate the current render value.
- Effects run after commit and can require cleanup before rerun or unmount.
- Development Strict Mode can repeat selected lifecycle work to expose unsafe effects.
- Keys define component identity and state preservation.
- Context can create broad render and dependency ownership.
- Concurrent rendering can start work that never commits.
- External stores need stable subscriptions and immutable or cached snapshots.
- Server and client components have different data, effect, and serialization boundaries.

Review effect ownership, stale closures, keys, derived state, context scope, external stores, and server-client boundaries.

## Svelte

- Svelte compiles component reactivity instead of using a general runtime virtual DOM.
- Runes are compiler keywords in Svelte 5. Legacy and runes mode use different reactive rules.
- Reactive work can rerun when tracked inputs change and still needs cleanup.
- Stores and module-level state can outlive one component instance.
- Keyed blocks control instance replacement and local state reset.
- DOM-dependent code must not run during server rendering.
- Bindings can create two-way mutation that obscures ownership.
- Transitions and actions have mount and teardown lifecycles.

Review the configured Svelte version, reactive ownership, store lifetime, bindings, teardown, and server-rendering safety.

## Next.js and Nuxt

- Server and client execution can run the same source under different runtime constraints.
- Rendering, caching, revalidation, and request ownership depend on the selected route mode.
- Static generation can move data reads from request time to build time.
- Hydration requires compatible server and client output.
- Server-only data must not cross a serialized client boundary.
- Middleware and route guards do not replace authoritative backend authorization.
- Framework fetch or data helpers can add caching that ordinary platform calls do not.
- Environment variables can have server-only or client-exposed behavior.

Review route mode, cache ownership, hydration, serialization, authorization, environment exposure, and deployment runtime.

## Official documentation

Use these sources when the repository does not pin a version or document the behavior:

- Angular: [signals](https://angular.dev/guide/signals), [dependency injection](https://angular.dev/guide/di), and [change detection](https://angular.dev/api/core/ChangeDetectionStrategy)
- Vue: [reactivity](https://vuejs.org/guide/extras/reactivity-in-depth.html) and [watchers](https://vuejs.org/guide/essentials/watchers.html)
- React: [rules](https://react.dev/reference/rules), [effects](https://react.dev/reference/react/useEffect), and [external stores](https://react.dev/reference/react/useSyncExternalStore)
- Svelte: [runes](https://svelte.dev/docs/svelte/what-are-runes) and [legacy reactivity](https://svelte.dev/docs/svelte/legacy-reactive-assignments)
- [Next.js documentation](https://nextjs.org/docs)
- [Nuxt rendering](https://nuxt.com/docs/guide/concepts/rendering)

## Add a framework profile

Record:

1. Lifecycle and cleanup.
2. State and reactivity.
3. Dependency and instance scope.
4. Rendering and identity.
5. Concurrency and scheduling.
6. Server-client boundaries.
7. Error and retry behavior.
8. Version-dependent behavior.

Record stable framework semantics only. Confirm disputed or version-specific behavior in primary documentation before reporting a finding.
