# Grid contract and audit

Declare a binding spatial contract for the selected composition. Reuse the project's existing owners and native units. Keep the declaration in working notes unless durable project guidance is in scope. Mark unresolved intent as proposed; do not invent a rule from a screenshot and then report the existing design as violating it.

## Declare the contract

Use only applicable fields; mark other fields not applicable with a reason. Treat these examples as candidate values, not universal defaults.

| Field | Declare | Example |
| --- | --- | --- |
| Unit and origin | Native unit, base increment, coordinate origin | CSS px, 4 px spacing increment, content-box start |
| Spacing scale | Permitted gaps and insets with role mappings | 4, 8, 12, 16, 24, 32, 48, 64 |
| Columns and axes | Tracks, spans, local alignment axes | 12 desktop columns; card contents share an inset axis |
| Gutters and margins | Fixed or responsive rules | 24 px gutters and 32 px margins at desktop |
| Content width | Maximum, minimum, and fluid allocation | Max 1200 px; fill available width below it |
| Baseline rhythm | Applicable line-height roles and increments | Body leading in 4 px steps; display style separate |
| Radius relationships | Shape roles and nested-boundary rules | Concentric inner radius = max(0, outer radius - inset) |
| Reflow | Exact breakpoints or container rules and changed relationships | Four columns below the declared breakpoint; wrap local groups |
| Exceptions | Element, value/rule, reason, owner, proof | Optical icon offset verified at use size |

Define numeric breakpoints in the project's actual units; preserve existing relative or container-based rules. For a single control, declare its local axes, gap, inset, and sizing rules without creating unrelated page foundations. For print or graphics, use the native page, artboard, or export coordinates.

## Apply the contract

- Snap authored fixed offsets, dimensions, gaps, insets, and line heights to their declared scales where applicable.
- Align block edges to their declared column, gutter, or local content axes; do not force every descendant onto page columns.
- Assign gaps to the parent and insets to the container; use native auto-layout or equivalent layout constraints instead of empty spacer layers.
- Keep sibling gaps equal when they express the same relationship; separate groups more strongly than related items where proximity carries the hierarchy.
- Keep text containers on their declared axes and rhythm; apply verified optical adjustments inside them when practical.
- Preserve content growth, usable targets, wrapping, and responsive allocation when enforcing the grid.
- Treat fluid track widths, centered origins, intrinsic text sizes, strokes, glyph paths, and animation interpolation according to their own declared rules. Do not round them to a spacing unit merely because they produce fractional coordinates.
- Apply concentric radius arithmetic only to boundaries intended to follow the same curve; preserve independent control shapes.

## Audit each rendered pass

1. Identify the revision, viewport or page size, scale, state or timeline sample, and nodes covered by the audit.
2. Read actual geometry and relevant styles through DOM, native design bounds, or export coordinates.
3. Normalize units, origins, transforms, box boundaries, and scroll offsets before comparing values.
4. Check fixed authored values exactly against their declared scale.
5. Compare rendered bounds against expected axes and allocation rules using a stated tolerance; begin with 0.5 CSS px for browser subpixel rounding and justify changes for another medium or scale.
6. List every violation within the declared audit scope with node, property, observed value, expected value or rule, difference, tolerance, and sampled state.
7. Trace each violation to its canonical token, component, layout, template, or asset owner.
8. Correct the owner through the authorized authoring workflow or record an intentional exception with a reason and rendered proof.
9. Repeat the measurements affected by the correction and one relevant stress case.
10. Report checked-node count, violating-node count, and verified-exception count alongside the violation and exception lists.

Count distinct nodes with remaining unexcepted violations as violating nodes; list multiple violations on one node separately. Count verified element/rule exceptions separately. Keep unverified proposed exceptions open. State excluded nodes, unmeasured states, and unavailable native geometry instead of claiming exhaustive coverage.

Use screenshots for perceptual verification alongside geometry. Label image-space estimates when native inspection is unavailable and keep the required native audit unavailable. Do not approve a composition from an overlay, token file, or arithmetic alone.

Check a normal state and a relevant stress state, such as long content or a narrow parent. A 15 px authored gap against a declared 4 px scale is a violation; a 247.5 px fluid column that satisfies its allocation rule is not. A recorded optical offset still needs visible proof. Do not relabel accidental drift as expressive intent to clear a finding.
