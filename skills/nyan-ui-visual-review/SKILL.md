---
name: nyan-ui-visual-review
description: Reviews existing rendered interfaces for production-grade visual quality. Use when the user asks to visually audit, critique, polish, refine, modernize, or QA an existing website, app, page, dashboard, workflow, or component using screenshots, live routes, responsive states, interaction states, or frontend code. Identifies evidence-backed visual problems, traces systemic root causes, protects product behavior, and produces implementation-ready recommendations or targeted fixes.
---

# UI Visual Review

Review an existing rendered interface as a senior design engineer and visual QA reviewer. Determine what works, identify what prevents the interface from feeling coherent and production-ready, and recommend changes that a designer or developer can implement directly.

Do not create a replacement interface unless the user explicitly requests a redesign. Do not change code when the user asks only for a review.

## Scope

Use this skill when a rendered baseline exists: a screenshot, live route, working build, interaction recording, component preview, or visual-regression image. Supporting frontend code improves root-cause analysis but does not replace rendered evidence.

Do not use this skill for greenfield concepting, backend or API design, or copywriting-first strategy. If no render is available, state the limitation and request one. Never claim to have inspected a state that was unavailable.

## Operating mode

Follow these stages:

1. **Inspect:** Record the evidence, product context, implementation constraints, and current design system.
2. **Diagnose:** Report strengths, problems, causes, and priorities from the evidence.
3. **Implement:** Change code only when the user requests changes.
4. **Verify:** Render the changed routes and states again.
5. Compare the new render with the original evidence.
6. Check for regressions.

For an implementation request, report the diagnosis and make the authorized changes.

If the user requests recommendations first, wait for approval before you change code.

## Select review depth

Choose the smallest depth that can answer the request and state it in the review summary.

- **Quick** — one component or narrow screenshot. Report a contextual read, strengths, up to five findings, meaningful before/after changes, and a verification list.
- **Standard** — one route or workflow. Report up to ten findings. Inspect relevant responsive and non-default states.
- **Production** — multiple routes, workflows, or release readiness. Report up to fifteen findings. Add an evidence matrix, design-rule updates, regression coverage, and the pre-flight assessment.

Do not fill the finding cap. A short review or no findings is a valid result.

## Read the interface before judging it

Identify:

- Identify the interface type and primary task.
- Identify the audience and usage frequency.
- Select an appropriate information density.
- Identify the design language and brand anchors.
- Identify accessibility, platform, regulatory, and trust constraints.
- Identify protected product structure, terms, analytics, and behavior.
- Read the user references and design-system documentation.

Start a substantial review with one sentence about the interface, audience, task, and visual priorities.

Do not impose a new aesthetic.

Respect quiet constraints. A financial product needs precise number and status communication. A healthcare interface needs cautious semantic color. An expert tool may appropriately use high density. Accessibility needs override subtle styling. Route and field names may be tied to documentation, analytics, autofill, or backend contracts.

## Select the change posture

- **Preserve** — retain the visual direction and layout concept. Correct inconsistency, hierarchy, usability, and incomplete states. Default to this posture when uncertain.
- **Modernize** — preserve information architecture and brand anchors while improving tokens, components, hierarchy, responsiveness, and interaction behavior.
- **Overhaul** — use only when the current structure prevents task completion, responsive behavior is fundamentally broken, the design system cannot support the product, or the user explicitly requests a major redesign.

State the posture when it materially affects the recommendations.

## Inspect the implementation context

When code is available, identify:

- Identify the framework, router, and rendering model.
- Identify the styling system and its version.
- Identify the theme and design tokens.
- Identify shared components and their owners.
- Identify icon, asset, chart, and animation sources.
- Identify component-preview tools.
- Identify visual, accessibility, and responsive test tools.
- Check available dependencies before you recommend a new package.

Follow the existing stack. Do not migrate frameworks or styling libraries for visual polish. Verify that every proposed import and dependency exists.

## Protected elements

Never silently change:

- Do not change route structure or primary navigation labels.
- Do not change workflow order, field names, or field order.
- Do not change the brand logo or wordmark.
- Do not change legal, consent, compliance, or permission behavior.
- Do not change analytics event names.
- Do not change metric definitions, calculations, or data meaning.
- Do not change destructive-action meaning or recovery behavior.
- Do not change established keyboard shortcuts.
- Do not change accessibility labels that have functional dependencies.

Flag a protected element if it creates a problem, but state that explicit product or engineering approval is required.

## Evidence workflow

1. Record available and unavailable evidence.
2. Inspect the entry point and reading order.
3. Inspect hierarchy, primary actions, grouping, density, alignment, and visual noise.
4. Compare repeated controls, cards, headings, tables, charts, badges, dialogs, lists, and empty states.
5. Inspect all available interaction and data states.
6. Inspect responsive transitions, not only the smallest and largest screenshots.
7. Check wrapping, reflow, overflow, sticky elements, touch targets, safe areas, and reading order.
8. Check the responsive strategy for tables and charts.
9. Trace each visible problem to its owning component, primitive, token, or utility.
10. Rank the findings.
11. Recommend targeted changes.
12. After an authorized change, render the same routes, viewports, content, and states again.

Prefer a live route over a single screenshot when it is available. Resize the viewport and exercise real states rather than guessing between breakpoints.

## Evidence requirements

For each priority finding, give at least one available locator:

- Name the screenshot or recording and visible region.
- Give the route and viewport size.
- Give the interaction sequence.
- Name the component or story.
- Give the source file and component.
- Name the browser, platform, or input mode.

Label claims:

- **Observed** — directly visible in inspected render, behavior, or code.
- **Inferred** — likely but not directly confirmed because evidence is incomplete.

Give each inferred finding a High, Medium, or Low confidence level.

Do not present an inference as a confirmed observation.

For implemented changes, capture or describe comparable before and after states using the same viewport, content, and interaction state.

Do not infer a visual defect from source code when the rendered result determines the outcome.

Do not infer a code-level cause from appearance alone. Inspect the owning source or label the cause as Inferred.

## Review priorities

Evaluate only dimensions relevant to the inspected interface:

1. Task fidelity and reading order
2. Visual hierarchy and action hierarchy
3. Component and state consistency
4. Accessibility and keyboard behavior
5. Responsive behavior and content preservation
6. Typography, spacing, alignment, and geometry
7. Color, contrast, surfaces, and depth
8. Content, data formatting, and data visualization
9. Icons, imagery, and asset consistency
10. Motion and perceived responsiveness

For a Standard or Production review, read [references/review-domains.md](references/review-domains.md).

For a Quick review, read only the relevant domain sections in that reference.

For dashboards and reports, verify KPI order, comparison context, metric definitions, axes, legends, units, precision, missing-data treatment, filter clarity, freshness, and color-independent interpretation. Distinguish zero from missing data.

For motion, ask what the motion communicates, how frequently it runs, whether feedback begins immediately, whether it is interruptible, whether it preserves layout stability, and whether reduced motion is supported. Do not add motion solely to make the interface feel active.

## Domain ownership

Assign each finding to one owner:

- **Accessibility:** semantics, focus, keyboard behavior, announcements, zoom, and reduced motion.
- **Layout:** grouping, alignment, reading order, responsive structure, safe areas, RTL, and localization growth.
- **Writing:** labels, actions, errors, empty states, terminology, and recovery guidance.
- **Typography:** fonts, type roles, measure, wrapping, numeric alignment, truncation, and text direction.
- **Color:** semantic roles, contrast, gamut, themes, and color-independent meaning.
- **Visual polish:** surfaces, geometry, icons, motion, optical alignment, and perceived responsiveness.

Report one root cause once. Mention secondary domain effects in the impact statement.

Do not create separate domain reports. Consolidate all findings into one ranked list.

## Strategic omissions

Check these only when applicable:

- No route out, back navigation, or useful not-found state
- No skip link, keyboard entry point, or visible focus
- No loading, empty, partial-data, offline, permission-denied, or error state
- No destructive confirmation, cancellation, or recovery path
- No responsive table or overflow strategy
- No form validation or useful inline error placement
- Missing page title, description, favicon, or sharing metadata on public pages
- Missing privacy, consent, or legal affordances where required

Do not add a feature merely because it appears in this list. Connect every omission to the product and task.

## Consistency locks

Describe project-level rules rather than universal aesthetic rules:

- Color roles and semantic states
- Typography roles
- Spacing relationships
- Shape and radius system
- Control geometry
- Interaction feedback
- Data and date formatting
- Chart conventions
- Responsive behavior
- Focus and loading behavior
- Motion duration and easing

Multiple accents, fonts, shapes, or layout patterns are acceptable when their roles are coherent and intentional.

## Anti-generic audit

Flag a pattern only when it does not fit the product. Common accidental patterns include equal visual weight across all sections, identical card grids, excessive pills, decorative gradients unrelated to brand, glass effects that reduce clarity, every region inside a bordered card, arbitrary status dots, fake screenshots, charts without decision value, identical spacing at every hierarchy level, meaningless icons, unrealistic sample data, generic placeholder copy, indiscriminate `transition: all`, and mobile layouts that merely shrink desktop.

Do not ban a font, icon library, gradient, grid, card, sidebar, radius, palette, or motion style by category. Judge whether its use supports the audience, task, brand, accessibility, and implementation system.

## Root-cause standard

For a meaningful finding, identify:

- Describe the visual symptom.
- Give the evidence and reproduction steps.
- Identify the owning component, primitive, token, or utility.
- List affected instances or frequency.
- Describe the user and system impact.
- Classify the scope as local or systemic.
- Identify the regression surface.
- Recommend a change.
- Give a verification target.

Prefer one systemic fix for a repeated systemic problem. Do not hide a shared defect with local overrides.

## Severity

- **Critical** — blocks a primary task, hides essential information, corrupts data interpretation, causes severe responsive failure, or creates a serious accessibility problem.
- **Major** — significantly harms comprehension, navigation, interaction, or system consistency.
- **Moderate** — creates a noticeable usability or visual-quality problem that should be fixed before production polish is complete.
- **Minor** — creates a small refinement issue with limited individual impact but meaningful cumulative value.

## Implementation priority

When implementing, use this risk-adjusted order unless evidence requires another order:

1. Task blockers and misleading data
2. Accessibility and keyboard failures
3. Responsive overflow and content loss
4. Missing interaction, loading, empty, and error states
5. Systemic component, token, or formatting inconsistencies
6. Hierarchy, typography, spacing, and alignment
7. Copy and asset problems
8. Motion and decorative polish

Separate recommendations into:

- **Required fixes:** Fix usability, accessibility, correctness, and strong consistency problems.
- **System improvements:** Fix repeated problems in shared primitives, tokens, utilities, or rules.
- **Optional polish:** Make low-impact refinements after the required work.

Do not make unrelated rewrites. Do not add an unnecessary dependency.

Test after each coherent change.

## Before, after, and why

Use a **Before | After | Why** table for meaningful implementation deltas. Do not create a row for every observation.

| Before | After | Why |
| :--- | :--- | :--- |
| Summary cards use inconsistent internal geometry | Use one shared summary-card contract for label, value, comparison, and footer regions | Restores scan alignment and prevents repeated drift |

## Output

Adapt the output to the selected review depth. A Standard or Production review should include:

1. **Review read:** Describe the interface, audience, task, and visual priorities.
2. **Review summary:** State readiness, strongest quality, highest-impact weakness, first action, depth, and posture.
3. **Coverage:** Report the evidence and result for each review domain.
4. **Strengths:** Report specific strengths from the evidence.
5. **Priority findings:** Give domain, location, evidence, severity, confidence, cause, impact, scope, recommendation, and verification.
6. **Before / After / Why**
7. **Considered but rejected:** List valid candidates that you rejected and explain why.
8. **Implementation recommendations:** Separate required fixes, system improvements, and optional polish.
9. **Design rules update:** Separate confirmed rules, recommended rules, and local exceptions.
10. **Verification:** List completed and unavailable checks.
11. **Verdict:** End with Block, Needs changes, or Approve.
12. **Next iteration prompt:** Include this only when implementation is expected.

Do not pad the report with empty sections or dimensions without meaningful findings.

For Coverage, use one result for each domain:

- **Clear:** The inspected evidence has no actionable finding.
- **Findings:** Report the finding count.
- **Not inspected:** State why the evidence was unavailable.

For Considered but rejected, include up to three candidates in Quick reviews. Include up to five in Standard or Production reviews.

Do not invent rejected candidates to meet a count.

For Verdict:

- Use **Block** when a Critical finding remains.
- Use **Needs changes** when only Major, Moderate, or Minor findings remain.
- Use **Approve** only when no actionable findings remain and the claimed coverage was verified.

## Design rules across iterations

Maintain:

- **Confirmed rules** — patterns consistently supported by evidence
- **Recommended rules** — patterns that should become standard
- **Local exceptions** — deliberate deviations with a documented reason

Never promote one local exception into a global rule.

## Pre-flight check

Before you complete a Production review, mark each item **Pass**, **Fail**, or **Not inspected**:

- Support each claim with inspected evidence.
- Label each claim as Observed or Inferred.
- Follow the selected review depth and change posture.
- Confirm that protected product behavior did not change without approval.
- Inspect hierarchy, consistency, responsive behavior, non-default states, and accessibility.
- Mark unavailable evidence as Not inspected.
- Separate required fixes, system improvements, and optional polish.
- Give each meaningful recommendation a verification method.
- Consolidate duplicate symptoms under one owning domain and root cause.
- Include considered but rejected candidates.
- Render implemented changes again.
- Check repeated instances and states for regressions.
- Use a verdict that matches the remaining findings and verified coverage.

Report each Fail in the priority findings or limitations.

Do not claim production readiness when an essential area is Not inspected.

## Behavioral rules

- Start with specific strengths.
- Review the rendered result before you propose broad changes.
- Connect each recommendation to a user, product, accessibility, or maintenance effect.
- Preserve product intent and the existing technology stack.
- Separate deliberate design from implementation drift.
- Treat responsive and non-default states as primary interface states.
- Use systemic fixes for systemic problems.
- Do not invent evidence.
- Do not impose a theme, trend, framework, or personal aesthetic.
- Review the rendered result again after implementation.

In the final review:

1. State what works.
2. State what is wrong.
3. Explain why each important problem matters.
4. Classify each problem as local or systemic.
5. State what must not change.
6. Give the first action.
7. Give the verification method.
8. State whether the inspected result is ready to ship.
9. End with Block, Needs changes, or Approve.
