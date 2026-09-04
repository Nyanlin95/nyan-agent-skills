---
name: nyan-ui-visual-review
description: Review an existing rendered interface for visual quality, usability, responsive behavior, accessibility, component consistency, hierarchy, and interaction states. Use when asked to review, audit, QA, polish, refine, or improve an existing website, application screen, component, dashboard, or visual system. Inspect the rendered result first. Keep recommendations evidence-based, bounded, and tied to the owning system. Do not use for greenfield design, code-only review, or a change that lacks rendered evidence.
---

# Nyan UI Visual Review

Review the rendered result before diagnosing or proposing a change. Translate feedback such as heavy, flat, cramped, noisy, or dead into hypotheses about hierarchy, spacing, scale, typography, contrast, alignment, depth, motion, feedback, latency, or affordance.

## Scope and authority

1. Name the target surface, user task, review depth, and protected behavior.
2. Inspect the repository, route, data state, component owners, tokens, and available checks before judging the surface.
3. Review and recommend by default. Implement only when the user authorizes the named scope.
4. Require explicit authority before a broad change to product structure, navigation, workflow order, data meaning, or protected behavior.
5. Keep an authorized change inside the selected surface and its canonical owner. Report adjacent opportunities separately.

## Evidence contract

1. Capture a baseline with stable content, viewport, route, and interaction state.
2. Record a compact evidence packet with the render path, visible observations, geometry when relevant, owners, and unavailable coverage.
3. Mark each claim **Observed** or **Inferred**. State the confidence and limit for every inference.
4. Use screenshots for perceptual claims. Use DOM geometry and selected computed styles for measurable claims.
5. Re-render the same state after an authorized change. Check the relevant responsive, non-default, input, accessibility, and failure states.

Read [references/rendered-evidence-harness.md](references/rendered-evidence-harness.md) for the compact evidence loop. Read the relevant sections of [references/review-domains.md](references/review-domains.md) for detailed domain checks.

## Review flow

1. Establish the task, audience, protected behavior, and evidence budget.
2. Inspect the rendered baseline and the smallest state matrix that can falsify the hypotheses.
3. Trace each confirmed symptom to one canonical component, primitive, token, layout, or state owner.
4. Rank bounded findings by user impact and confidence.
5. Propose the smallest systemic correction when a shared rule causes repeated drift.
6. Implement only the authorized correction.
7. Compare the same rendered state before and after.
8. Report completed and unavailable proof with a verdict.

## Findings and verdict

For each meaningful finding, report the symptom, evidence and reproduction, owner, affected scope, user impact, recommendation, regression surface, and verification target.

Use these severities:

- **Critical:** Blocks a primary task, hides essential information, corrupts data interpretation, causes a severe responsive failure, or creates a serious accessibility problem.
- **Major:** Materially harms comprehension, navigation, interaction, or system consistency.
- **Moderate:** Creates a noticeable usability or visual-quality problem.
- **Minor:** Creates a limited refinement issue with cumulative value.

End every Standard or Production review with one verdict:

- **Block:** A Critical finding remains.
- **Needs changes:** A required finding remains.
- **Approve with follow-ups:** Only optional polish remains.
- **Approve:** No actionable finding remains in verified coverage.

State unavailable coverage rather than implying it passed. Do not require a follow-up question after the verdict.

## Completion

1. State what works, what is wrong, and why the important issues matter.
2. State the protected behavior and the first recommended action.
3. Classify each material issue as local or systemic.
4. List the rendered and repository checks that passed or remained unavailable.
5. Give the verdict that matches the evidence.
