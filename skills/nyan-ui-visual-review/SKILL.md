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

1. **Inspect** — establish available evidence, product context, implementation constraints, and the current design system.
2. **Diagnose** — report evidence-backed strengths, problems, root causes, and priorities before changing code.
3. **Implement** — change code only when requested. Work inside the existing stack and keep the changes focused.
4. **Verify** — re-render affected routes and states, compare them with the original evidence, and check for regressions.

For implementation requests, diagnosis does not require a separate approval unless the user asks to review recommendations before changes. Report the diagnosis, then make the authorized changes.

## Select review depth

Choose the smallest depth that can answer the request and state it in the review summary.

- **Quick** — one component or narrow screenshot. Report a contextual read, strengths, up to five findings, meaningful before/after changes, and a verification list.
- **Standard** — one route or workflow. Use the full review structure and inspect relevant responsive and non-default states.
- **Production** — multiple routes, workflows, or release readiness. Add an evidence matrix, design-rule updates, regression coverage, and the pre-flight assessment.

## Read the interface before judging it

Infer these from available evidence:

- Interface type and primary task
- Intended audience and usage frequency
- Appropriate information density
- Existing design language and brand anchors
- Accessibility, platform, regulatory, and trust constraints
- Product structure, terminology, analytics, and established behavior
- User-provided references and design-system documentation

Begin a substantial review with one sentence that describes the interface, audience, task, and relevant visual priorities. Do not impose a new aesthetic.

Respect quiet constraints. A financial product needs precise number and status communication. A healthcare interface needs cautious semantic color. An expert tool may appropriately use high density. Accessibility needs override subtle styling. Route and field names may be tied to documentation, analytics, autofill, or backend contracts.

## Select the change posture

- **Preserve** — retain the visual direction and layout concept. Correct inconsistency, hierarchy, usability, and incomplete states. Default to this posture when uncertain.
- **Modernize** — preserve information architecture and brand anchors while improving tokens, components, hierarchy, responsiveness, and interaction behavior.
- **Overhaul** — use only when the current structure prevents task completion, responsive behavior is fundamentally broken, the design system cannot support the product, or the user explicitly requests a major redesign.

State the posture when it materially affects the recommendations.

## Inspect the implementation context

When code is available, identify:

- Framework, router, and rendering model
- Styling system and its version
- Theme configuration and design tokens
- Shared components and their ownership
- Icon, asset, chart, and animation sources
- Storybook or other component-preview tooling
- Visual-regression, accessibility, and responsive test infrastructure
- Available dependencies before recommending a new package

Follow the existing stack. Do not migrate frameworks or styling libraries for visual polish. Verify that every proposed import and dependency exists.

## Protected elements

Never silently change:

- Route structure or primary navigation labels
- Established workflow order, field names, or field order
- Brand logo or wordmark
- Legal, consent, compliance, or permission behavior
- Analytics event names
- Metric definitions, chart calculations, or data meaning
- Destructive-action meaning or recovery behavior
- Established keyboard shortcuts
- Accessibility labels with functional dependencies

Flag a protected element if it creates a problem, but state that explicit product or engineering approval is required.

## Evidence workflow

1. Record available and unavailable evidence.
2. Inspect the default state: entry point, reading order, hierarchy, primary action, grouping, density, alignment, and visual noise.
3. Compare repeated patterns: controls, cards, headings, tables, charts, badges, navigation, dialogs, lists, and empty states.
4. Inspect available non-default states: hover, focus, pressed, selected, expanded, loading, empty, no-results, partial data, error, offline, disabled, success, permission denied, and destructive confirmation.
5. Inspect responsive transitions, not only endpoint screenshots. Check wrapping, reflow, overflow, table and chart strategy, sticky elements, touch targets, safe areas, and reading order.
6. Trace visible symptoms to the owning component, primitive, token, or formatting utility.
7. Rank findings and recommend targeted changes.
8. When implementation is authorized, re-render and verify the same routes, viewport sizes, content, and states.

Prefer a live route over a single screenshot when it is available. Resize the viewport and exercise real states rather than guessing between breakpoints.

## Evidence requirements

For each priority finding, provide at least one locator when available:

- Screenshot or recording name and visible region
- Route and viewport size
- Interaction sequence
- Component or story name
- Source file and component
- Browser, platform, or input mode

Label claims:

- **Observed** — directly visible in inspected render, behavior, or code.
- **Inferred** — likely but not directly confirmed because evidence is incomplete.

Give inferred findings High, Medium, or Low confidence. Never present an inference as confirmed.

For implemented changes, capture or describe comparable before and after states using the same viewport, content, and interaction state.

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

For dashboards and reports, verify KPI order, comparison context, metric definitions, axes, legends, units, precision, missing-data treatment, filter clarity, freshness, and color-independent interpretation. Distinguish zero from missing data.

For motion, ask what the motion communicates, how frequently it runs, whether feedback begins immediately, whether it is interruptible, whether it preserves layout stability, and whether reduced motion is supported. Do not add motion solely to make the interface feel active.

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

- Visual symptom
- Evidence and reproduction condition
- Owning component, primitive, token, or utility
- Affected instances or frequency
- User and system impact
- Local or systemic scope
- Regression surface
- Recommended change
- Verification target

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

- **Required fixes** — usability, accessibility, correctness, or strong consistency
- **System improvements** — shared primitives, tokens, utilities, or rules that solve repeated issues
- **Optional polish** — lower-impact refinement that should not delay important fixes

Avoid unrelated rewrites and unnecessary dependencies. Test after each coherent change.

## Before, after, and why

Use a **Before | After | Why** table for meaningful implementation deltas. Do not create a row for every observation.

| Before | After | Why |
| :--- | :--- | :--- |
| Summary cards use inconsistent internal geometry | Use one shared summary-card contract for label, value, comparison, and footer regions | Restores scan alignment and prevents repeated drift |

## Output

Adapt the output to the selected review depth. A Standard or Production review should include:

1. **Review read** — interface, audience, task, and visual priorities
2. **Review summary** — readiness, strongest quality, highest-impact weakness, first action, review depth, and change posture
3. **Strengths** — specific and evidence-supported
4. **Priority findings** — location, evidence, severity, confidence, symptom, root cause, impact, scope, recommendation, and verification
5. **Before / After / Why**
6. **Relevant detailed review**
7. **Implementation recommendations** — required fixes, system improvements, optional polish
8. **Design rules update** — confirmed rules, recommended rules, and local exceptions
9. **Validation checklist**
10. **Next iteration prompt** — include only when implementation is expected

Do not pad the report with empty sections or dimensions without meaningful findings.

## Design rules across iterations

Maintain:

- **Confirmed rules** — patterns consistently supported by evidence
- **Recommended rules** — patterns that should become standard
- **Local exceptions** — deliberate deviations with a documented reason

Never promote one local exception into a global rule.

## Pre-flight check

Before declaring a Production review complete, mark each item **Pass**, **Fail**, or **Not inspected**:

- Claims are backed by inspected evidence and labeled Observed or Inferred.
- The selected review depth and change posture were respected.
- Protected product behavior was not silently changed.
- Hierarchy, consistency, responsive behavior, non-default states, and accessibility were inspected or explicitly marked unavailable.
- Required fixes, system improvements, and optional polish are separated.
- Each meaningful recommendation includes a verification method.
- Implemented changes were re-rendered and checked for repeated-instance and state regressions.

Any Fail must appear in priority findings or limitations. Do not claim production readiness when a load-bearing area is Not inspected.

## Behavioral rules

Start with specific strengths. Review the rendered result before proposing broad change. Explain every meaningful recommendation through task completion, reading order, semantic grouping, comparison speed, interaction clarity, accessibility, maintainability, or perceived responsiveness. Preserve product intent and the existing technology stack. Distinguish deliberate design from implementation drift. Treat responsive and non-default states as part of the primary interface. Prefer systemic fixes for systemic problems. Do not invent unavailable evidence. Do not impose a theme, trend, framework, or personal aesthetic. Re-review the rendered result after implementation.

The final review must make clear what works, what is wrong, why it matters, whether the issue is local or systemic, what must remain unchanged, what should happen first, how to verify the change, and whether the inspected result is ready to ship.
