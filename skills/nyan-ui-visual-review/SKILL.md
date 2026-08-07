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

## Evidence budget

Start with the smallest rendered baseline that can test the request. Do not load or retain every route, viewport, state, screenshot, or implementation file before the initial read.

- **Quick:** Inspect one target surface and the one state that contains the reported problem.
- **Standard:** Inspect the target route or workflow at its primary viewport, then add only the responsive or non-default states that can change a reported finding.
- **Production:** Name the primary routes and high-risk states before inspection. Establish one baseline per route, then expand only where shared components, product risk, or a finding requires comparison.

Record compact evidence references: route or surface, viewport, state, and observation. Reopen a render when detail is needed instead of retaining large rendered artifacts in working context. Mark uninspected routes and states as unavailable. Expand the evidence budget only when the user broadens the scope or the current evidence indicates a systemic, accessibility, responsive, or release-risk problem.

## Interview the repository first

Before asking the user for information that the repository can provide, inspect the smallest relevant evidence set. Start from the rendered surface, then read the route, owning component, current state names, relevant types, tests, product documentation, and design-system rules that explain it.

Use the render and identified owners to bound repository inspection. Do not search the whole repository or load unrelated implementation detail merely to avoid a question.

Ask the user only when the repository evidence is unavailable, conflicts, or cannot answer a product-direction question. Always ask before a decision that needs product authority, including a broad implementation scope or a protected behavior change. Do not infer that authority from source code, tests, or historical conventions.

## Mandatory flow

Use this sequence for every implementation request. Do not change code before you complete the required pre-change steps.

### Pre-change

1. Set the review depth and evidence budget.
2. Inspect the target render and read the relevant repository evidence.
3. Record the baseline, product context, implementation constraints, and design system.
4. Diagnose the strengths, problems, causes, priorities, and affected states.
5. Select and justify the change posture.
6. Classify the proposed scope as localized or broad.
7. State a broad implementation proposal when the scope is broad.
8. Get explicit authority before you implement a broad scope.
9. Implement only the authorized scope.

### Post-change

1. Render the changed surface again within the evidence budget.
2. Compare the new render with the baseline.
3. Check the named regression surfaces.
4. Run the repository's verification gates for the changed path (typecheck, build, format, and tests) and report their results.
5. Report the verified result and any remaining risk.
6. Ask whether to stop or authorize a separately scoped next iteration.

Do not treat a post-change question as authority to change an unapproved surface. If the user requests recommendations only, stop after the pre-change diagnosis.

## Select review depth

Choose the smallest depth that can answer the request and state it in the review summary.

Set the review depth before you inspect the interface.

- **Quick** — one component or narrow screenshot. Report a contextual read, strengths, up to five findings, meaningful before/after changes, and a verification list.
- **Standard** — one route or workflow. Report up to ten findings. Inspect relevant responsive and non-default states.
- **Production** — multiple routes, workflows, or release readiness. Report up to fifteen findings. Add an evidence matrix, design-rule updates, regression coverage, and the pre-flight assessment.

Do not fill the finding cap. A short review or no findings is a valid result.

## Read the interface before judging it

Record:

- The interface type and primary task.
- The audience and usage frequency.
- The appropriate information density.
- The design language and brand anchors.
- The accessibility, platform, regulatory, and trust constraints.
- The protected product structure, terms, analytics, and behavior.
- The relevant user references and design-system documentation.

Start a substantial review with one sentence about the interface, audience, task, and visual priorities.

Do not impose a new aesthetic.

Respect quiet constraints. A financial product needs precise number and status communication. A healthcare interface needs cautious semantic color. An expert tool may appropriately use high density. Accessibility needs override subtle styling. Route and field names may be tied to documentation, analytics, autofill, or backend contracts.

## Select the change posture

- **Preserve** — retain the visual direction and layout concept. Correct inconsistency, hierarchy, usability, and incomplete states. Default to this posture when uncertain.
- **Modernize** — preserve information architecture and brand anchors while improving tokens, components, hierarchy, responsiveness, and interaction behavior.
- **Overhaul** — use only when the current structure prevents task completion, responsive behavior is fundamentally broken, the design system cannot support the product, or the user explicitly requests a major redesign.

State the posture and the evidence that supports it whenever you recommend or implement a change. When the user asks to modernize, replace, recompose, redesign, or make a substantial visual change, assess Modernize before choosing Preserve. State why Preserve is sufficient or why it would leave a structural problem unresolved.

## Change authorization

Treat a change as broad when it changes a user task, information architecture, domain relationship, control meaning, route, navigation, workflow order, or multiple primary surfaces.

Classify the scope before you implement a change.

Diagnose and recommend a broad change from the available evidence. Before you implement it, state the scope, affected tasks, protected behavior, and verification plan. Then get explicit user approval.

An implementation request is enough for a localized change that preserves the existing task, structure, and control meaning. Do not request confirmation for ordinary review, evidence gathering, or a bounded visual fix.

## Broad implementation proposal

Before requesting authority for a broad implementation, state:

1. The selected posture and the observed problem it addresses.
2. The affected routes, surfaces, and user tasks.
3. The visual-system changes, such as layout, hierarchy, density, shared components, tokens, or responsive behavior.
4. The protected behavior that must not change.
5. Any proposed change to information architecture, navigation meaning, workflow order, or control meaning.
6. The bounded rendered-evidence and regression plan.

Get explicit approval before you edit a broad scope. After the authorized fix, use the post-change render to ask whether the user wants another scoped proposal. Do not roll an unapproved next phase into the completed change.

## Inspect the implementation context

When code is available, identify:

- The framework, router, and rendering model.
- The styling system and its version.
- The theme and design tokens.
- The shared components and their owners.
- The icon, asset, chart, and animation sources.
- The component-preview tools.
- The visual, accessibility, and responsive test tools.
- The available dependencies before you recommend a new package.

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

## Inspect the evidence

Use this checklist in pre-change steps 2 through 4. Inspect only the evidence that fits the selected budget and scope.

Use non-mutating interactions and isolated test data by default. Do not submit forms, send messages, alter records, trigger payments, or perform destructive actions merely to inspect a state. Require explicit authorization for the exact non-production target before a state-changing interaction. Mark the state as unavailable when safe inspection evidence is not available.

1. Record available and unavailable evidence.
2. Inspect the entry point and reading order.
3. Inspect hierarchy, primary actions, grouping, spacing rhythm, density, alignment, and visual noise.
4. Compare repeated controls, cards, headings, tables, charts, badges, dialogs, lists, and empty states.
5. Inspect the interaction and data states that can affect a finding.
6. Inspect responsive transitions, not only the smallest and largest screenshots.
7. Check wrapping, reflow, overflow, sticky elements, touch targets, safe areas, and reading order.
8. Check the responsive strategy for tables and charts.
9. Trace each visible problem to its owning component, primitive, token, or utility.
10. Rank the findings.
11. Recommend targeted changes.
12. Use the post-change flow after an authorized change.

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

## Spacing and density audit

Review spacing as a relationship between elements. Do not judge a gap as an isolated number.

1. Identify the spacing tokens, component gaps, and container padding that affect the inspected surface.
2. Compare the same relationship across repeated instances and related states.
3. Compare the spacing inside a group with the spacing between groups and sections.
4. Check whether the spacing supports hierarchy, grouping, reading order, and intended information density.
5. Inspect long content, missing content, loading states, validation states, and translated text when they can change the rhythm.
6. Inspect intermediate widths, zoom, and text resizing when reflow can change the spacing.
7. Distinguish a token or layout defect from a local optical correction.
8. Trace repeated drift to the owning token, primitive, or component.

Do not require one fixed spacing scale. Do not report a different gap as a defect unless it weakens hierarchy, consistency, readability, touch use, or responsive behavior.

For a spacing finding, state the compared elements, viewport and state, expected relationship, actual relationship, owner, affected instances, and verification target.

## Intent-aware layout structure

Review layout as an expression of the user task and product model. Do not judge it as a generic page template.

### Establish model evidence

1. Look for `CONTEXT-MAP.md` and then the relevant `CONTEXT.md` files.
2. Read product documentation, route definitions, types, state names, and tests when no usable domain model exists.
3. Identify the primary task, primary entity, user decision, entity state, and supporting relationships for the inspected surface.
4. Record the source of each model claim and state which model evidence was unavailable.
5. Report a conflict between the screen and repository model as Inferred until a product owner confirms it.

Use the repository model as evidence. Do not create or change a glossary, context file, or architecture decision record during a visual review.

### Test structural fit

1. Classify each prominent control by its user effect.
2. Treat navigation as a control that changes the user's task, context, collection, route, or selected item.
3. Treat a filter as a control that narrows or arranges the current content set without changing its task or context.
4. Treat a lifecycle view as a control that changes which state of the same entity the user sees.
5. Treat an action as a control that creates, changes, sends, or removes something.
6. State every role when one control has more than one effect.
7. Identify whether the surface needs a list with supporting context, a master-detail view, collection navigation, a focused workspace, or another structure.
8. Check whether the layout gives the primary task, entity, and decision enough visual priority and working space.
9. Check whether persistent context, selected detail, navigation depth, and controls match the relationships the user must understand.
10. Check whether tabs, sidebars, search, and filters communicate their actual effect.
11. Check whether empty, loading, error, and permission states preserve the same task and model cues.
12. Trace a structural mismatch to information architecture, route state, component ownership, or layout implementation before you recommend CSS changes.

Do not require a named layout pattern. Do not treat a tab as a filter only because it changes the visible list. Do not recommend a sidebar, tabs, or master-detail layout without evidence that it supports the task and model.

For an intent-aware layout finding, state the task, entity, relevant relationship or state, control classification, visible mismatch, owner, affected surface, and verification target.

## Domain ownership

Assign each finding to one owner:

- **Accessibility:** semantics, focus, keyboard behavior, announcements, zoom, and reduced motion.
- **Layout:** task structure, grouping, spacing rhythm, alignment, reading order, responsive structure, safe areas, RTL, and localization growth.
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
- Spacing rules across hierarchy, components, and responsive states
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
11. **Verdict:** End with Block, Needs changes, Approve with follow-ups, or Approve.
12. **Next-scope question:** After implementation and post-change verification, ask whether to stop or authorize a separately scoped next iteration.

Do not pad the report with empty sections or dimensions without meaningful findings.

For Coverage, use one result for each domain:

- **Clear:** The inspected evidence has no actionable finding.
- **Findings:** Report the finding count.
- **Not inspected:** State why the evidence was unavailable.

For Considered but rejected, include up to three candidates in Quick reviews. Include up to five in Standard or Production reviews.

Do not invent rejected candidates to meet a count.

For Verdict:

- Use **Block** when a Critical finding remains.
- Use **Needs changes** when a required Major, Moderate, or Minor finding remains.
- Use **Approve with follow-ups** when required fixes are complete and only optional polish remains. List the optional work and its reason for deferral.
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
9. End with Block, Needs changes, Approve with follow-ups, or Approve.
