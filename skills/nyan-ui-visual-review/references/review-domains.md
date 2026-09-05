# Review Domains

Use these checks for the relevant interface domains. Keep shared spatial rules
in the skill's spatial reference and non-UI checks in its media reference.

## Accessibility

- Prefer native elements before custom controls.
- Check visible focus and full keyboard operation.
- For dialogs and overlays, check focus entry, containment, and restoration.
- Check accessible names, labels, input types, and error announcements.
- Check that color is not the only state indicator.
- Check dynamic content announcements.
- Check reduced-motion behavior.
- Test browser zoom and text resizing when the interface can reflow.
- Check skip links and in-page anchors against the actual router: a `href="#anchor"` target breaks a hash router by replacing the routed hash, and the target (for example `<main>`) must be focusable, such as with `tabindex="-1"`.
- Check route-change focus lifecycle: move focus once per navigation, and flag effects or observers that refocus on every DOM update.
- For adjustable controls, check the ARIA state values (`aria-valuenow`, `aria-valuemin`, `aria-valuemax`) and require tests that assert state and keyboard behavior, not only `tabindex` or handler presence.

## Layout

- Read the repository domain model before judging a complex screen structure.
- Identify the primary task, entity, user decision, entity state, and supporting relationships.
- Classify a prominent control as navigation, a filter, a lifecycle view, or an action by its user effect.
- Treat navigation as a change of task, context, collection, route, or selected item.
- Treat a filter as a change to the current content set, not to the task or context.
- Treat a lifecycle view as a change to the visible state of the same entity.
- State all roles when one control has more than one effect.
- Check whether tabs, sidebars, search, and filters communicate their actual effect.
- Check whether the selected layout supports the task: list with context, master-detail, collection navigation, focused workspace, or another structure.
- Check whether viewport allocation and persistent context match the user decision and entity relationships.
- Trace a structural mismatch to information architecture, route state, component ownership, or layout implementation before recommending CSS changes.
- Do not create or change domain-model files during a visual review.
- Apply the spatial reference's group, spacing-owner, fit, and alignment checks to the interface's actual content and state.
- Check that controls remain visually distinct from static content.
- Select breakpoints from content failure, not common device widths.
- Check intermediate widths, not only endpoint screenshots.
- Record responsive evidence for the in-scope routes; a desktop-only test or screenshot does not prove responsive behavior.
- Use existing responsive and reduced-motion checks where relevant; do not treat a mocked `matchMedia` test as rendered reflow or motion proof.
- Check safe areas, sticky regions, overflow, and clipped actions.
- Check logical direction properties and RTL behavior.
- Check localization growth and wrapping.
- Check cues for hidden or progressively disclosed content.

## Writing

- Match the established product voice and terminology.
- Use action labels that state the result.
- Keep workflow terms consistent across screens and states.
- Make links describe their destination.
- Put error guidance near the failed action or field.
- State what failed and what the user can do next.
- Give empty states a relevant next action.
- Use placeholders as examples, not as field labels.

## Typography

- Check that the application loads the intended font files, weights, and styles.
- Check semantic type roles instead of raw size changes.
- Check heading order, line height, letter spacing, and readable measure.
- Check wrapping for headings, controls, and translated text.
- Use tabular numbers when values change or align in columns.
- Make truncated content available through expansion or another accessible path.
- Keep mobile text inputs large enough to avoid unwanted viewport zoom.
- Check language, text direction, selection, and bidirectional content.

## Color

- Check semantic color roles before individual color values.
- Measure text and control contrast in each relevant theme.
- Check disabled, selected, warning, error, and success states.
- Check that charts and statuses remain clear without color.
- Check light and dark theme behavior.
- Check gradients and palette steps for visible discontinuities.
- Check whether wide-gamut colors have safe fallbacks.
- Preserve the project color space and token system unless evidence shows a defect.

## Visual polish

- Apply the spatial reference's nested-boundary and optical-alignment checks.
- Separate structural borders from decorative depth.
- Check icon weight, size, alignment, and state behavior.
- Apply the spatial-motion reference's ownership, sequencing, and intermediate-state checks.
- Do not use `transition: all`.
- Check initial render, entry, exit, hover, press, loading, and reduced-motion states.
- Preserve the project motion language unless evidence shows a defect.
