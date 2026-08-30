# Single-Surface Refinement

Use this workflow to give one visible surface unusually deep attention without turning the request into a product-wide redesign.

Form this working semantic hypothesis and remove optional stages that the user's requested artifact state does not require:

```text
Single-Surface Refinement :=
    Research-Synthesize-Verify?
    → Hypothesis-Test-Refine
    → Focused Implementation?
    → Blast-Radius Validation?
```

Stop after diagnosis and recommendations for research-only or review-only requests. Use `Focused Implementation` only when the user requests a change. Use `Blast-Radius Validation` when the surface is shared, responsive, stateful, or crosses an interaction or accessibility boundary.

## Seal the surface

Record four boundaries before implementation:

| Boundary | Record |
| --- | --- |
| Selected surface | The component, layout, composition, animation, section, or repeated surface the user identified. |
| Required owners | The component, shared primitive, token, state rule, or parent layout that directly produces it. |
| Protected world | Neighboring UI, navigation, routes, product meaning, data contracts, and behaviors that must remain unchanged. |
| Completion proof | The rendered comparison, important states, focused gate, and failure or protected-behavior check that can falsify the result. |

Treat a repeated collection and its item as one surface system when their rhythm, selection, scrolling, metadata, or action behavior cannot be judged independently. Include a shared owner outside the visible boundary only when evidence shows that it causes the selected problem.

Choose the change posture explicitly:

- `Preserve`: retain the structure and behavior; refine hierarchy, geometry, styling, feedback, and motion.
- `Modernize`: change presentation patterns while retaining product meaning and task flow.
- `Overhaul`: replace the surface structure or interaction model under explicit authority.

Default to `Preserve` when the user says refine, polish, improve, or focus on this component.

## Triangulate evidence

Use sources according to what they can establish:

1. Use the user's selected target, reference, and feeling-based feedback to establish intent and scope.
2. Use the rendered baseline to establish actual appearance, behavior, timing, and breakpoints.
3. Use repository source, tests, tokens, and design-system rules to establish ownership and protected product behavior.
4. Use current shipped product interfaces and flows to discover established and emerging UI patterns for the same surface and product context.
5. Use recent curated galleries, design-editorial reports, platform releases, and current design-tool showcases to discover visual-direction signals.
6. Use official platform, accessibility, browser, framework, or library guidance to establish interaction and runtime constraints.
7. Use the product's brand and design system to decide which transferable patterns and visual signals belong in this product.

For a meaningful visual refinement, combine evidence from current shipped interfaces with an independent current visual or platform source. For a question involving interaction, motion, accessibility, or platform convention, also use relevant authoritative guidance. Add examples only when they resolve a real design choice. Record what each source confirmed, challenged, or changed. Reject decorative research that has no decision consequence.

Prefer primary technical sources. Check freshness when a platform, framework, library, or browser behavior may have changed. Separate observed evidence from inference and mark unavailable coverage.

## Scan current patterns and visual direction

Run a fresh scan when the user asks for a modern, current, fresh, elevated, best-in-class, or trend-aware result, or when the existing surface appears visually dated. Do not rely on a memorized trend list. Collect or revalidate every source used to support a currentness claim during the active task, and report the scan's as-of date. An undated source can provide an example but cannot establish recency by itself.

Separate the scan into two questions:

| Lane | Question | Prefer |
| --- | --- | --- |
| Shipped UI patterns | How do current real products solve this component, state, flow, or information-density problem? | Direct product inspection, recent product screenshots and flows, current design-system releases, and versioned platform examples. |
| Visual-direction signals | Which compositions, materials, typography treatments, shapes, color systems, depth cues, and motion languages are gaining current design attention? | Recent curated galleries, dated design-editorial reports, current design-tool showcases, conference releases, and newly published case studies. |

For each candidate pattern or signal, record:

- its source, publication or update date when available, observation date, and product context;
- whether it is a shipped pattern, platform convention, editorial trend claim, curated example, or experimental concept;
- the recurring principle seen across independent sources, not merely the surface styling of one example;
- the part that transfers to the selected surface and the part that conflicts with its brand, content, behavior, or technical constraints;
- the evidence that would make Omelet adopt, adapt, or reject it.

Use direct product evidence to establish that a UI pattern is in real use. Use editorial and gallery sources to detect visual movement, not to prove usability or product fit. Treat community concepts as hypothesis generators only. Treat a trend repeated across unrelated current sources as a stronger signal than a named trend appearing in one roundup.

Classify the result before implementation:

- `Established pattern`: a current, repeated solution to a comparable product problem. Adapt its structural principle.
- `Emerging pattern`: a repeated but still context-dependent solution. Prototype or localize it before adoption.
- `Visual signal`: a current aesthetic direction without product-behavior authority. Translate it through the product's own brand and tokens.
- `Novelty`: a one-off effect or concept without corroboration. Reject it unless the user explicitly wants experimentation.

Prefer an ownable visual system over a collage of fashionable effects. Do not copy another product's distinctive identity, combine unrelated trends, or apply a platform material outside the platform and functional layer it was designed to serve. Let current sources widen the option space; let intent, brand, content, runtime evidence, and protected behavior decide the result.

## Inspect only the relevant dimensions

Select the dimensions that can change the outcome:

- Composition and layout: containment, alignment, rhythm, density, anchoring, safe areas, and overflow.
- Visual hierarchy: scale, typography, contrast, color, depth, grouping, and emphasis.
- Interaction: affordance, feedback, focus, selection, direct manipulation, latency, cancellation, and recovery.
- Motion: purpose, continuity, duration, easing or spring response, interruption, reduced motion, and exit behavior.
- Content: empty, short, long, localized, loading, error, disabled, and permission-limited states.
- Input and viewport: keyboard, IME composition, mouse, touch, coarse or fine pointer, mobile, intermediate, and desktop layouts.
- Runtime: layout stability, scroll ownership, expensive effects, console errors, and behavior at content extremes.

Do not turn this list into a mandatory audit. Build the smallest state matrix that can falsify the hypotheses for this surface.

## Run the refinement loop

1. Capture the current surface with stable content, viewport, and state.
2. Describe the intended feeling and observable outcome without prescribing values prematurely.
3. Research the uncertain decisions through the evidence hierarchy.
4. Write bounded hypotheses such as “the metadata feels detached because its alignment follows the card edge instead of the title column.”
5. Trace each confirmed problem to one canonical owner.
6. Fix the owner and remove competing local rules when the migration is complete.
7. Re-render the same baseline and compare geometry, hierarchy, behavior, and timing.
8. Exercise the relevant extremes, alternate inputs, responsive states, interruption, and one protected or failure path.
9. Run the repository-owned focused gate and inspect the rendered surface for console or runtime failures.
10. Close with the before-and-after decision, evidence used, proof achieved, and unavailable coverage.

When several coupled visual or motion parameters would materially benefit from live comparison, route through [dialkit.md](dialkit.md) only if DialKit already exists or the user explicitly authorizes adding it. Promote accepted values into the canonical owner and verify the production rendering.

## Route common scenarios

| Pointed-at surface | Treat as the local system | Typical evidence and proof |
| --- | --- | --- |
| Button, input, card, menu, modal, or composer | Component, direct state owner, relevant primitive, and tokens | Content extremes; hover, focus, press, disabled, loading, error; keyboard or IME where applicable; touch target; responsive render. |
| List, rail, table, or repeated item | Collection rhythm, item hierarchy, selection, metadata, actions, and scroll owner | Empty, short, long, selected, status, overflow, keyboard, touch, intermediate width, and repeated-item consistency. |
| Page layout or composition | Parent grid or stack, regions, spacing scale, containment, and breakpoint owner | Stable before-and-after geometry at mobile, intermediate, and desktop widths; long content; safe areas; overflow and scroll behavior. |
| Animation or transition | Trigger, state transition, property owner, timing model, interruption, and reduced-motion route | Replayable start and end states; rapid reversal; cancellation; reduced motion; no unintended layout shift or input delay. |
| Website section | Section composition, content hierarchy, responsive media, calls to action, and section boundary | Real content, crop and wrap extremes, action focus, mobile and desktop composition, and continuity with adjacent sections without redesigning them. |
| One visual value | Existing token or local declaration that owns it | Use a direct measured correction and focused render; do not invoke the full workflow when uncertainty and coupling are low. |

## Prevent false depth

- Do not broaden the product surface to make the result appear comprehensive.
- Do not change product meaning, route ownership, ordering, persistence, or authorization to solve a presentation problem.
- Do not preserve a competing rule that overrides the selected or non-default state.
- Do not infer input capability from viewport width when the platform exposes input-capability signals.
- Do not animate routine typing, scrolling, or frequently repeated actions without a user-benefiting purpose.
- Do not accept a still screenshot as proof for interaction or motion.
- Do not accept automated checks alone as proof of visible quality.
- Do not invent exact values from taste alone when tokens, measured geometry, platform guidance, or rendered comparison can decide them.
- Do not modify or publish unrelated concurrent changes.
