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

## Layout

- Check grouping before recommending separators or more decoration.
- Check shared alignment edges and reading order.
- Check that controls remain visually distinct from static content.
- Select breakpoints from content failure, not common device widths.
- Check intermediate widths, not only endpoint screenshots.
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
