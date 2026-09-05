# Media and scale checks

Apply the shared spatial method at the scale of the task. Select relevant checks rather than requiring every medium in every review. Pair a local crop with its parent composition when context changes the judgment. Use the task's authoring tools for edits and native inspection; do not convert every artifact to HTML merely to obtain a DOM.

## Choose equivalent evidence

| Medium | Inspect structure and geometry | Inspect the rendered result | Select a likely failure case |
| --- | --- | --- | --- |
| Web UI | DOM, selected computed styles, scroll bounds, accessibility tree | Browser at named viewport, zoom, theme, and state | Long copy, narrow width, error, keyboard focus |
| Vector or design canvas | Scene graph, frames, transforms, text styles, clipping masks | Native canvas and intended export at known scale | Small-size export, substituted font, changed aspect ratio |
| Slides | Master/layout ownership, object and text bounds, slide dimensions | Exported or presented slides at intended viewing scale | Long title, dense chart, overflow after export |
| Books and documents | Paragraph styles, text frames, page boxes, margins, text flow | Exported pages and facing-page spreads | Page break, long caption, gutter or trim conflict |
| Graphics | Artboard, layers, visible bounds, safe area, crop and asset resolution | Final raster/vector export at intended size | Alternate crop, small-size use, low-resolution asset |
| Motion | Scene hierarchy, anchors, keyframes or layout states, clip regions | Playback plus sampled intermediate frames | Reversal for interactive work; edit or crop discontinuity for linear work |

Record whether bounds describe local, page, artboard, or viewport coordinates. Convert points, pixels, millimeters, and export scale explicitly before comparing. Do not assume a screenshot's pixels equal document units. With image-only input, critique visible relationships and label coordinate estimates; leave source ownership inferred and hidden behavior unavailable.

## Icons and marks

- Inspect silhouette, negative space, stroke consistency, corner treatment, and detail survival at actual use size.
- Compare layout bounds, visible ink, and optical center; inspect view-box whitespace before changing the surrounding control's padding.
- Compare related icons as a family, including apparent weight and occupied area rather than only identical numeric dimensions.
- Check the enclosing hit area and focus indicator for interactive icons; omit those UI checks for a static printed mark.
- Review pixel-edge softness at the intended raster scale without forcing all vector paths onto a universal pixel grid.

## Buttons and inputs

- Inspect icon-label grouping, text baseline, internal inset, shape, and alignment among neighboring controls.
- Separate a control's visible shape from its activation area and focus extent.
- Check normal, relevant active/disabled/loading, and long-label cases without moving the primary action unexpectedly.
- Review an input together with its persistent label, helper text, error, and adjacent fields; trace label-to-field and field-to-error gaps to their group owners.
- Preserve readable entered text and reachable recovery actions under text growth and narrow widths.

### Match treatment to meaning

Classify interface elements by their actual role, such as action, input, status, or explanation, before recommending their visual treatment. Keep tips distinguishable from disabled actions and noninteractive statuses distinguishable from click targets. Verify actual semantics and behavior when available; appearance alone cannot establish interactivity.

Choose controls from task necessity rather than displaying every available component variant. Favor a clear primary action and the required way to reverse or recover; allow the same control to provide both where appropriate. Preserve distinct necessary actions. Put a component inventory in an explicit state matrix only when that artifact is requested.

### Align choice controls with their title

For a checkbox with supporting guidance, begin with this group structure:

```text
Choice
├── Heading row
│   ├── Checkbox mark
│   └── Title
└── Supporting explanation
```

Align the mark with the title's first line rather than centering it beside the combined title-and-description stack. Declare whether the explanation belongs to the title column or the entire group. Favor the title column for repeated icon-and-title rows; allow a deliberately standalone composition to align guidance with the group's start edge.

Choose this relationship from the composition's role, not the current visible item count. Filtering a list to one result must preserve its list alignment. Keep a standalone exception at the composition owner and remove or revise it when the intended composition becomes a repeated list.

Preserve native labeling, focus, activation behavior, and descriptive associations when the authoring workflow changes grouping. Inspect the mark, title line, and explanation in the rendered parent, including wrapped guidance, a populated draft, and relevant content-added states such as validation success. A passing outer-card measurement does not verify these relationships.

## Forms, cards, sections, and whole pages

- Group related fields before choosing separators; make label, help, error, and action hierarchy follow the user's task.
- Compare card header, body, media, and footer axes; inspect growth with long text, missing media, and validation content.
- Check repeated components through their shared primitive or template before suggesting individual offsets.
- Review page grid, readable content width, section rhythm, density, primary emphasis, and navigation context together.
- Inspect one level above and below the reported defect; expand scope only when the same owner causes repeated failure.
- Check content-driven reflow, reading order, sticky regions, and reachable actions at relevant intermediate widths.

## Presentations

- Identify each slide's message and the sequence's argument before judging decoration.
- Inspect title, evidence, annotation, and source hierarchy at presentation viewing scale; do not accept editor zoom as proof of legibility.
- Compare recurring title axes, chart regions, footers, and margins through the slide master or layout owner.
- Balance consistent structure with intentional variation in pacing; avoid turning every slide into identical cards.
- Keep chart labels, units, and legends readable without changing data meaning or shrinking essential content to fit.
- Review the exported deck for substituted fonts, altered wrapping, cropped objects, and media behavior.
- Compare slide-to-slide transitions in playback when motion carries the argument; inspect static exports separately when those are deliverables.

## Books and editorial layouts

- Establish page size, binding direction, facing-page behavior, margins, gutter, columns, and the production provider's actual bleed and safe-area requirements.
- Distinguish page trim from bleed and live text area; use supplied production specifications rather than universal margin numbers.
- Inspect spreads for balance and reading continuity while also checking individual pages.
- Review body measure, leading, paragraph spacing, headings, captions, running heads, folios, and footnotes through their style and text-flow owners.
- Check widows, orphans, awkward heading breaks, caption separation, and overset text after repagination.
- Preserve intentional baseline rhythm without forcing display typography and illustrations onto every body-text baseline.
- Recheck later pages after a flow change; one corrected page does not prove the rest of a chapter remains sound.
- Label screen-render proof separately from physical print proof and inaccessible production checks.

## Graphic design

- Establish the message, focal point, viewing distance, output size, and crop variants before comparing compositions.
- Inspect figure-ground separation, negative space, visual weight, type-image relationships, and the intended eye path.
- Preserve purposeful asymmetry and expressive type when they serve the brief; judge geometry by relationships rather than compulsory symmetry.
- Check essential marks and text against each crop's safe area and visible asset bounds.
- Inspect resolution, transparency, font rendering, and clipping in the actual export.
- Obtain production-specific color and output requirements when relevant; do not claim print color accuracy from a screen screenshot.

## Collaborate with the authoring workflow

Supply a compact brief with the audience, purpose, protected content, group tree, key spatial contracts, intended feeling, and normal/failure verification cases. Recommend the smallest change at a named owner. Let the authoring workflow choose the native implementation and return a render for critique.

For example, replace “make the book page more spacious” with “separate the caption from body prose while retaining its association with the figure; adjust the caption style or frame relationship, then review the spread and the next page after reflow.” Keep the proposal provisional until those renders exist.
