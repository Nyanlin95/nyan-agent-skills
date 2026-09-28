# DialKit Interface Tuning

Use DialKit as an optional, local authoring adapter for rendered interface work. Keep Omelet responsible for intent, scope, canonical ownership, authority, promotion, evidence, and completion.

## Ground the installed release

Resolve the repository's installed DialKit version from its manifest and lockfile before using API guidance. Check the matching published package, types, and documentation when implementation details matter; do not assume the GitHub default branch, latest tag, and npm release identify the same artifact.

The reviewed baseline is npm `dialkit@2.0.2`, published on 2026-09-09. It supports React 18+, Solid 1.6+, Svelte 5.8+, Vue 3.3+, and plain JavaScript through separate adapter entry points. Refresh this baseline from first-party sources when the installed version differs or the task depends on a current release claim.

## Decide whether it fits

Use DialKit when all of these conditions hold:

- A running interface can provide a fast visual or interaction feedback loop.
- The design question involves several coupled numeric, color, boolean, select, spring, easing, or timeline values.
- The product behavior and state transitions are already understood.
- Comparing live candidates is more useful than editing one isolated value.
- DialKit is already available in the repository, or the user explicitly authorized adding it.

Do not use DialKit to decide information architecture, content meaning, accessibility requirements, authorization, business rules, durable state, provider behavior, deployment, or destructive actions. Do not treat an action button as an approval gate. Use the repository's owning code and verification for those concerns.

Skip DialKit for a one-value correction, a static design-token change with an obvious owner, a non-rendered task, or a task whose main uncertainty is correctness rather than feel. Continue with ordinary implementation when the dependency is absent.

## Route the scenario

| Scenario | Useful controls | Omelet contract |
| --- | --- | --- |
| Layout and visual hierarchy | Spacing, size, radius, typography, opacity, color, blur, shadow | Tune within the existing component and token boundaries. Check responsive and repeated states before promotion. |
| Component interaction | Hover, press, modal, toast, reveal, and replay parameters | Exercise the real trigger and non-default states. Preserve focus, keyboard, reduced-motion, and dismissal behavior. |
| Motion timing | Spring, easing, delay, stagger, clip values, sequence timing | Keep animation structure in code. Use the timeline for parameter search, then promote the selected timing into the production animation. |
| Effects and generative UI | Particle count, spread, shader values, canvas geometry, loader speed, visual modes | Bound ranges against performance and valid rendering. Verify the real render loop and a representative low-end or reduced-motion state when applicable. |
| Component playground | Props, selects, toggles, saved versions, reset, copied output | Keep the playground separate from product state. Validate copied output against the component contract before using it. |
| Cross-page authoring | Stable panel identity and optional browser persistence | Use only for local continuity. Do not store secrets, approval state, user data, or durable project decisions in browser storage. |
| Production-facing configurator | Inline controls or persisted values | Treat this as a separate product feature, not a tuning shortcut. Require explicit user direction, production ownership, authorization, persistence, accessibility, and security design. |

## Run the tuning lifecycle

1. **Frame:** State the rendered question, protected behavior, canonical owner, target states, and acceptance evidence.
2. **Inspect:** Check the repository manifests, lockfiles, framework, existing DialKit integration, package conventions, and production guards.
3. **Route:** Use the existing compatible dependency, continue without DialKit when it is absent, or enter a dependency-add path only when the user explicitly authorized that change.
4. **Select:** Use one framework-consistent adapter and style entry so roots and controls share the same registration state.
5. **Add:** In the explicitly authorized path, add DialKit and its adapter-specific peer dependencies through the repository's package workflow.
6. **Confirm:** Inspect the resulting manifest, lockfile, peer dependencies, framework adapter, style loading, client-only boundary when required, and build-mode changes before instrumentation.
7. **Instrument:** Add the smallest control surface with bounded ranges grouped by the visual concept they affect.
8. **Exercise:** Tune against the actual interaction, content extremes, responsive sizes, and relevant accessibility state with replay or reset for deterministic comparison.
9. **Compare:** Use saved versions for candidate comparison while treating Version 1, saved versions, copied output, and persisted values as authoring state rather than approval.
10. **Capture:** Record the reviewed values and timeline instructions with the source revision they were tuned against.
11. **Promote:** Move accepted values into the canonical component, token, prop default, or production animation. Do not make DialKit's store or browser persistence the source of truth.
12. **Verify:** Run the repository's rendered or runtime proof after promotion. A DialKit preview is authoring evidence, not final acceptance evidence.
13. **Classify:** Remove temporary controls and sampled bindings, or document that the checked-in surface is intentionally retained for development or a playground.
14. **Prove:** Confirm the approved production boundary by inspecting the authoring UI and sampled bindings in the built application.

## Preserve the production boundary

Framework roots are hidden in production by default unless `productionEnabled` is true. The plain-JavaScript root has the opposite default and remains enabled unless `productionEnabled` is false. Set and verify the intended boundary explicitly instead of relying on an adapter default or the repository's environment wrapper.

Root visibility controls the editor UI, not the code that consumes live values. Persistence defaults to false. With persistence enabled, values, saved versions, and the active version can enter browser storage; panel open state stays in memory. Use a stable ID only for authoring continuity, and never persist secrets, user data, authorization, approval, or durable project decisions.

The timeline dock is independent of the parameter root and has the same framework-versus-vanilla production defaults. For timeline authoring, bind sampled values only during tuning. After choosing the motion, copy the timings and values into the application's animation system, replace the sampled binding, and remove the timeline hook and dock unless the repository intentionally retains an authoring surface. Removing or hiding only the dock leaves the sampled values in control.

DialKit's deterministic preview supports scrubbing, but it is not guaranteed to match the production animation engine frame for frame. Verify the promoted animation in the real runtime.

## Evidence behind the scenarios

Use current, version-matched first-party documentation for API details before implementation; the library can change after this reference was written.

- The [published npm package](https://www.npmjs.com/package/dialkit) identifies the released version and adapter dependencies.
- The [official repository](https://github.com/joshpuckett/dialkit) documents controls, controllers, saved versions, opt-in persistence, adapter-specific production visibility, and the timeline copy-and-replace lifecycle.
- The repository's [API reference](https://github.com/joshpuckett/dialkit/blob/main/docs/reference.md) and [timeline guide](https://github.com/joshpuckett/dialkit/blob/main/docs/timeline.md) provide current implementation details; reconcile them with the installed package version before use.
- The [official DialKit website](https://www.dialkit.dev/) provides visual scenarios for live interface tuning; use the versioned package and repository docs for API contracts.
- Solana Foundation's [share-card development panel](https://github.com/solana-foundation/tokens/blob/main/apps/web/src/components/share-card-dev-panel.tsx) groups typography, layout, and chart controls behind an explicit development guard.
- Matrix's [loader playground](https://github.com/zzzzshawn/matrix/blob/main/app/playground/playground-client.tsx) combines selects, sliders, toggles, shortcuts, live preview, and generated component snippets.
- Fresh Giammi's [confetti showcase](https://github.com/freshgiammi/portfolio/blob/master/src/routes/_main/craft/confetti/index.tsx) tunes runtime effect shape and range while the real interaction remains the trigger.
- DomainKit's [workshop](https://github.com/AryaLabsHQ/domainkit/blob/main/packages/react/examples/vite/src/workshop.tsx) uses controller-driven controls and actions inside a dedicated component workshop.
- The Interactive SVG Icons [curve-heading component](https://github.com/Indra-photon/Interactive-SVG-Icons/blob/master/components/craftui/blocks/curve-heading/default.tsx) records a completed tune-and-freeze lifecycle by retaining canonical values without the live panel.
