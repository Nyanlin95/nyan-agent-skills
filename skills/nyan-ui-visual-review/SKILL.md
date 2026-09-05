---
name: nyan-ui-visual-review
description: Guide and critique visual design during creation or refinement using spatial principles, rendered evidence, and geometry. Use to scaffold a project's basic visual system, distill existing design choices into coherent foundations, or review and polish icons, controls, forms, cards, applications, web pages, presentations, books, graphics, and motion. Pair with the authoring workflow to define visual roles and evaluate hierarchy, typography, fit, optical balance, and transitions. Use DOM or native measurements; label unrendered proposals provisional. Do not use for code-only correctness review or as the artifact implementation workflow.
---

# Nyan UI Visual Review

Guide design decisions and review their visible consequences. Translate feedback such as heavy, flat, cramped, noisy, or dead into hypotheses about hierarchy, spacing, scale, typography, contrast, alignment, depth, motion, feedback, latency, or affordance. Explain the relevant term in plain language and connect the recommendation to the intended feeling.

Keep one job: visual-system guidance and critique. Collaborate with the task's authoring workflow through a design brief, foundations, constraints, findings, and verification targets. Leave artifact construction and edits with that workflow; do not create a second implementation owner or require another agent. Let the same agent apply this guidance while authoring; do not stop authorized scaffolding at a recommendation or require a separate handoff.

## Scope and authority

1. Name the target artifact, audience, task, scale, medium, and protected behavior or content.
2. Inspect the relevant source, design system, component or template owners, and available native inspection tools.
3. Review and recommend by default; pass in-scope corrections to the authoring workflow when the user has requested creation or refinement.
4. Require explicit authority before a broad change to product structure, navigation, workflow order, data meaning, or protected behavior.
5. Keep recommendations inside the selected surface and its canonical owner. Report adjacent opportunities separately.

## Collaborate during creation and refinement

1. Select a posture: establish visual foundations, guide a new composition, critique a draft, or diagnose an existing artifact.
2. Inspect the rendered baseline when one exists.
3. For a new composition, propose its semantic group tree, spatial contracts, and falsifiable assertions before asking the authoring workflow for a first render.
4. Mark pre-render advice as a provisional design hypothesis, never an observed defect or a visual approval.
5. Review from the target's internal details to its parent context; inspect an icon at use size and in its control, or a page both alone and in its sequence.
6. Feed each confirmed issue back to the owning component, layout, style, template, asset, or transition.
7. Reassess the resulting render before closing a finding.

Preserve the chosen visual language. Treat grids, spacing ratios, symmetry, and type palettes as design aids, not universal laws. Support intentional asymmetry, expressive typography, and optical exceptions when they serve the brief and survive verification.

## Establish a coherent project system

1. Identify the project's existing visual contract, tokens, styles, primitives, templates, assets, and representative rendered uses.
2. Distill observed choices into semantic roles and distinguish intended variation, accidental drift, and unresolved intent.
3. Propose the smallest foundation that serves the current project, preserving its recognizable character and useful exceptions.
4. Map each proposed rule to an existing canonical owner or the smallest missing owner required by the requested scaffold.
5. Ask the authoring workflow to apply the foundation to representative compositions within the authorized scope.
6. Verify coherence across distinct uses and one relevant stress case before recommending wider adoption.

Deliver a compact foundation map with each role, rule/value, intended effect, canonical owner, verified uses, and exceptions. Explain retained, consolidated, corrected, and deferred choices. State the bounded adoption slice and whether the result is proposed foundations, an implemented pilot, or adoption across the explicitly verified scope. Report verification evidence, unresolved conflicts, and remaining migration work.

Keep visual foundations here; leave application state, navigation, caching, and runtime architecture to their implementation owners. Do not turn an isolated polish request into a project-wide system migration.

## Evidence contract

1. Capture a baseline with stable content, artifact revision, viewport or page dimensions, output scale, and interaction state or timeline time.
2. Record a compact evidence packet with the render path, visible observations, geometry when relevant, owners, and unavailable coverage.
3. Mark each claim **Observed** or **Inferred**. State the confidence and limit for every inference.
4. Pair perceptual inspection with measurements: use DOM geometry and selected computed styles for web interfaces, native object or text bounds for design files, and export coordinates or timeline samples for other media.
5. Declare units, coordinate origin, transforms, and tolerance before comparing geometry.
6. Re-render the same state after an authorized change through the authoring workflow.
7. Check the normal case and one relevant failure case, such as text growth, a narrow viewport, print trim, export reflow, or interrupted motion.
8. Verify relevant leaf elements inside their rendered parent, including both-axis sizing, semantic treatment, and content-added states; do not close a component finding from outer-container geometry alone.

Treat source styles as declared intent, measurements as proof of the sampled geometry, and renders as perceptual evidence. Do not infer DOM, fonts, hidden states, or interaction behavior from a screenshot. Use image-space measurements only at their known scale; label estimates and unavailable native evidence.

Read only the relevant references:

- [Project visual foundations](references/project-visual-foundations.md): distill an existing design language or scaffold a minimal new system and validate its representative uses.
- [Spatial principles](references/spatial-principles.md): grouping, container contracts, fit calculations, typography, optical alignment, and inspection layers at any scale.
- [Rendered evidence harness](references/rendered-evidence-harness.md): compact browser evidence, DOM probes, coordinate interpretation, and comparable captures.
- [Media and scale checks](references/media-and-scale.md): icons through pages, presentations, books, graphics, and native export checks.
- [Spatial motion](references/spatial-motion.md): anchors, coordinated geometry, timing, interruption, and intermediate-frame review.
- [Review domains](references/review-domains.md): interface-specific usability, accessibility, writing, color, and product structure.

## Review flow

1. Establish the task, audience, protected behavior, and evidence budget.
2. Inspect the rendered baseline and the smallest state matrix that can falsify the hypotheses.
3. Trace each confirmed symptom to one canonical component, primitive, token, layout, or state owner.
4. Rank bounded findings by user impact and confidence.
5. Propose the smallest systemic correction when a shared rule causes repeated drift.
6. Hand the correction and its verification target to the authoring workflow within the user's authorized scope.
7. Compare the same rendered state before and after.
8. Report completed and unavailable proof with a verdict.

## Findings and verdict

For each meaningful finding, report the symptom, evidence and reproduction, owner, affected scope, user impact, recommendation, regression surface, and verification target.

Use these severities:

- **Critical:** Blocks a primary task, hides essential information, corrupts data interpretation, causes a severe responsive failure, or creates a serious accessibility problem.
- **Major:** Materially harms comprehension, navigation, interaction, or system consistency.
- **Moderate:** Creates a noticeable usability or visual-quality problem.
- **Minor:** Creates a limited refinement issue with cumulative value.

End each completed rendered review with one verdict:

- **Block:** A Critical finding remains.
- **Needs changes:** A required finding remains.
- **Approve with follow-ups:** Only optional polish remains.
- **Approve:** No actionable finding remains in verified coverage.

State unavailable coverage rather than implying it passed. Do not require a follow-up question after the verdict.

For creation guidance without a render, end with **Provisional design guidance** and the next render or measurement needed. Do not use an approval verdict until the relevant artifact has been inspected. Scale the report to the task; keep a button review short without weakening its evidence.

## Completion

1. State what works, what is wrong, and why the important issues matter.
2. State the protected behavior and the first recommended action.
3. Classify each material issue as local or systemic.
4. List the rendered and repository checks that passed or remained unavailable.
5. Give the verdict that matches the evidence.
