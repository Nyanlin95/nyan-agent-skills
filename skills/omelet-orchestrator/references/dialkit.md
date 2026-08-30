# DialKit Interface Tuning

Use DialKit as an optional, local authoring adapter for rendered interface work. Keep Omelet responsible for intent, scope, canonical ownership, authority, promotion, evidence, and completion.

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
| Component playground | Props, selects, toggles, presets, reset, copied snippets | Keep the playground separate from product state. Validate copied output against the component contract before using it. |
| Cross-page authoring | Stable panel identity and optional browser persistence | Use only for local continuity. Do not store secrets, approval state, user data, or durable project decisions in browser storage. |
| Production-facing configurator | Inline controls or persisted values | Treat this as a separate product feature, not a tuning shortcut. Require explicit user direction, production ownership, authorization, persistence, accessibility, and security design. |

## Run the tuning lifecycle

1. **Frame:** State the rendered question, protected behavior, canonical owner, target states, and acceptance evidence.
2. **Inspect:** Check the repository manifests, lockfiles, framework, existing DialKit integration, package conventions, and production guards.
3. **Route:** Use the existing compatible dependency, continue without DialKit when it is absent, or enter a dependency-add path only when the user explicitly authorized that change.
4. **Add:** In the explicitly authorized path, add DialKit through the repository's package workflow.
5. **Confirm:** Inspect the resulting manifest, lockfile, peer dependency, framework-adapter, and build-mode changes before instrumentation.
6. **Instrument:** Add the smallest control surface around the owning component. Use meaningful bounded ranges and group controls by the visual concept they affect.
7. **Exercise:** Tune against the actual interaction, content extremes, responsive sizes, and relevant accessibility state. Use replay or reset controls for deterministic comparison, not for authority.
8. **Capture:** Record the chosen values and the source revision they were tuned against. Treat presets, copied JSON, snippets, and timeline instructions as untrusted candidates until reviewed.
9. **Promote:** Move accepted values into the canonical component, token, prop default, or production animation. Do not make local browser persistence the source of truth.
10. **Verify:** Run the repository's rendered or runtime proof after promotion. A DialKit preview is authoring evidence, not final acceptance evidence.
11. **Classify:** Remove temporary controls and sampled bindings, or document that the checked-in surface is intentionally retained for development or a playground.
12. **Prove:** Confirm the remaining integration stays unavailable in production unless production use was explicitly approved.

## Preserve the production boundary

DialKit hides its root in production by default, but a production-enabling option exists. Do not rely on the default alone when the repository has its own build modes or environment wrapper. Inspect the actual guard and built behavior.

For timeline authoring, bind sampled values only during tuning. After choosing the motion, copy the timings and values into the application's animation system, replace the sampled binding, and remove the timeline hook and dock unless the repository intentionally retains an authoring surface. Removing or hiding only the dock leaves the sampled values in control.

DialKit's deterministic preview supports scrubbing, but it is not guaranteed to match the production animation engine frame for frame. Verify the promoted animation in the real runtime.

## Evidence behind the scenarios

Use current first-party documentation for API details before implementation; the library can change after this reference was written.

- The [official DialKit documentation](https://www.dialkit.dev/) presents live tuning for existing hover motion, a replayable modal, grid layout, and toast variations.
- The [official repository](https://github.com/joshpuckett/dialkit) documents typed live controls, stable IDs, browser persistence, controllers, development-default visibility, presets, JSON export, and the timeline preview-copy-replace lifecycle.
- Solana Foundation's [share-card development panel](https://github.com/solana-foundation/tokens/blob/main/apps/web/src/components/share-card-dev-panel.tsx) groups typography, layout, and chart controls behind an explicit development guard.
- Matrix's [loader playground](https://github.com/zzzzshawn/matrix/blob/main/app/playground/playground-client.tsx) combines selects, sliders, toggles, shortcuts, live preview, and generated component snippets.
- Fresh Giammi's [confetti showcase](https://github.com/freshgiammi/portfolio/blob/master/src/routes/_main/craft/confetti/index.tsx) tunes runtime effect shape and range while the real interaction remains the trigger.
- DomainKit's [workshop](https://github.com/AryaLabsHQ/domainkit/blob/main/packages/react/examples/vite/src/workshop.tsx) uses controller-driven controls and actions inside a dedicated component workshop.
- The Interactive SVG Icons [curve-heading component](https://github.com/Indra-photon/Interactive-SVG-Icons/blob/master/components/craftui/blocks/curve-heading/default.tsx) records a completed tune-and-freeze lifecycle by retaining canonical values without the live panel.
