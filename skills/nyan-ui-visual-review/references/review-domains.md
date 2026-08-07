# Review Domains

Use these checks only when the domain is relevant to the inspected interface.

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
- Check grouping before recommending separators or more decoration.
- Compare spacing inside a group with spacing between groups and sections.
- Compare repeated component gaps, container padding, and alignment edges.
- Check spacing with long, missing, loading, validation, and translated content.
- Check intermediate widths, zoom, and text resizing for spacing drift after reflow.
- Trace repeated spacing drift to a token, primitive, or component.
- Distinguish a local optical correction from a shared spacing rule.
- Check shared alignment edges and reading order.
- Check that controls remain visually distinct from static content.
- Select breakpoints from content failure, not common device widths.
- Check intermediate widths, not only endpoint screenshots.
- Record desktop and mobile evidence for every primary route; a desktop-only test or screenshot does not prove responsive behavior.
- Require `matchMedia`-driven tests for mobile layouts and reduced-motion behavior when the interface reflows or animates.
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

- Check nested radii and surface geometry for consistent relationships.
- Use optical alignment when geometric alignment looks wrong.
- Separate structural borders from decorative depth.
- Check icon weight, size, alignment, and state behavior.
- Check that interactive transitions can respond to interruption.
- Inspect motion slowly when timing or sequencing looks wrong.
- Avoid routine staggered motion and decorative movement without task value.
- Do not use `transition: all`.
- Check initial render, entry, exit, hover, press, loading, and reduced-motion states.
- Preserve the project motion language unless evidence shows a defect.
