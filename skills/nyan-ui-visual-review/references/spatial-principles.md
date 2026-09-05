# Spatial principles

Adapt the supplied *Spatial layout principles for design agents* guide into the following critique method. Treat its numbers as worked examples, not required tokens. Use meaning → group tree → constraints → fit → render → measurement → owner correction as the reasoning order.

## Model meaning before decoration

Identify the reader's task and the primary information or action. Group by relationship before choosing backgrounds or borders. For a player card, use:

```text
Player
├── Identity
│   ├── Artwork
│   └── Text
│       ├── Title
│       └── Artist
└── Playback
    ├── Progress
    └── Controls and time
```

Preserve these relationships when the component wraps. Avoid equal gaps between every leaf: they imply equal relationships. Add a group only for a semantic, layout, or interaction responsibility. Use proximity and alignment without a visible surface when sufficient.

## Name the spatial contract

Distinguish container bounds, content area, visible artwork or glyph bounds, and interactive hit area. Name padding for boundary-to-content space, gap for sibling separation, margin for external spacing, and line height for allocated text height.

Record important containers compactly, not every decorative node:

```yaml
name: identity
purpose: identify the track
parent: player
direction: horizontal
width: fill remaining allocation
height: fit content
padding: 0
gap: identity-gap token
cross-axis: center
main-axis: start
children: [fixed artwork, flexible text]
overflow: wrap text and grow parent
```

Specify hug-content (fit-content), fill, fixed, or bounded behavior on both axes of each relevant child. Use these as design-contract terms, not automatic mappings to similarly named CSS properties. Interpret fill as remaining allocated space after siblings and gaps. For bounded text, require a deliberate overflow treatment and access to essential content. Avoid fixed heights that only fit the shortest copy.

## Audit child sizing before tuning gaps

Inspect children in their actual parent; a correct outer size does not prove correct internal allocation. Start with these contracts and adapt them to the task:

| Child | Width starting point | Height and containment |
| --- | --- | --- |
| Short badge or status | Hug content within available width | Fit content; contain long text through the intended wrap or overflow policy |
| Text field | Fill its allocation with a usable minimum | Follow the control's single- or multiline contract |
| Icon | Fixed visible size | Preserve aspect and define any hit area separately |
| Supporting paragraph | Fill or bounded reading measure | Grow with wrapping |
| Button | Hug content or intentionally full width | Preserve usable target size and the long-label policy |

Compare a short badge with its content, internal inset, and borders; compare a long badge with the parent's available width. Test both cases rather than accepting a wide parent screenshot. Use DOM or native child bounds and rendered appearance to establish whether the contract holds.

Trace repeated sizing defects to the shared component or template. Recommend enforcing the relationship there before adding regression tests or explanatory documentation. Keep intentional full-width controls and fill-sized fields intact when correcting a content-sized sibling.

## Assign spacing roles and owners

Reuse the artifact's existing spacing scale and semantic roles. Distinguish text-pair, related-item, group, and section gaps. Begin with a smaller within-group gap than between-group gap for comparable relationships; account for dividers, backgrounds, and alignment that already establish grouping.

Inspect the nearest common parent, distribution rule, margins, nested padding, line boxes, and asset whitespace before recommending a spacing change. In an additive layout, a 16 px parent gap plus an 8 px child margin and 12 px nested inset can create 36 px between visible content. Check the actual layout model before summing: margin collapse and distributed free space change the result.

Assign sibling separation to the parent where practical and internal inset to the container. Remove redundant inset at its owner instead of nudging several descendants. Do not increase all gaps to solve one crowded boundary. Keep spacing rhythm separate from stroke widths, icon geometry, typography, and flexible dimensions; permit valid fractional values.

## Calculate fit with explicit assumptions

Use one box model, unit, and coordinate system. For an outer border box:

```text
content width = outer width - left/right borders - left/right padding
content height = outer height - top/bottom borders - top/bottom padding
row requirement = sum(child widths) + sum(gaps)
column requirement = sum(child heights) + sum(gaps)
```

Include margins, free-space distribution, wrapping, and minimum sizes when present. Resolve a failed fit through growth, reflow, bounded shrinkage, or an intentional overflow policy; do not accept clipping as a fix.

Use this worked example to check the reasoning, not as a component prescription:

- Take a 352 × 200 px borderless player with 24 px padding.
- Calculate a 304 × 152 px content area.
- Fit two 64 px groups with a 24 px gap: `64 + 24 + 64 = 152`.
- Allocate the identity row: `304 - 64 px artwork - 16 px gap = 224 px text`.
- Fit title and artist line boxes: `24 + 4 + 20 = 48 px`.
- Center that stack beside the artwork: `(64 - 48) / 2 = 8 px`.

Recalculate when the title wraps: two 24 px title lines produce a 72 px stack with the artist and gap, exceeding the assumed 64 px row. Recommend growth and recheck the card, or apply the task's explicit truncation policy. Do not retain the original fit claim.

Derive a row's minimum width from fixed children, flexible minimums, gaps, borders, and insets. Review just above and below that threshold. Preserve semantic order and usable content when the arrangement changes; avoid uniformly shrinking the desktop composition.

## Name alignment and optical exceptions

Specify a start edge, end edge, center, or baseline rather than saying only “align.” Express useful assertions such as `header.start = body.start`, `label.baseline = value.baseline`, or `footer.end = body.end`. Use logical edges for reading direction.

Inspect loaded fonts, available measure, line height, weight, fallback, wrapping, and glyph shapes. Do not equate font size with line-box height or visible ink. Compare text baselines using suitable text evidence; a rectangle's bottom is not a baseline.

Verify geometric alignment before judging apparent balance. Inspect asset whitespace, SVG view boxes, stroke extent, and asymmetric forms when equally sized boxes look unequal. Permit a small optical adjustment with a named asset or style owner and a perceptual reason. Do not use optical adjustment to hide a broken parent constraint.

For concentric rounded boundaries with uniform inset, consider `inner radius = max(0, outer radius - inset)`. Apply it only to boundaries intended to follow the same curve. Preserve independent control shapes. Inspect shadows, border thickness, clipping, and focus treatment separately.

## Build truthful inspection layers

Request inspection views only when they help explain or falsify the design:

| View | Derive from the same artifact |
| --- | --- |
| Original | Finished content and current state |
| Grid | Declared origin, unit, and measured axes |
| Spacing | Actual padding bands, sibling gaps, and group bounds |
| Structure | Group hierarchy while preserving constraints and wrapping |
| Typography | Actual text styles and line boxes |

Keep overlays outside layout flow and interaction. Use a legend with labels as well as colors. Derive every claimed measurement from the inspected state; mark hand-drawn approximations illustrative. Avoid separately authored copies that drift from the original.

## Diagnose and specify proof

| Symptom | Inspect first | Recommend at the owner |
| --- | --- | --- |
| Flat or equally spaced | Semantic group tree and competing emphasis | Restore hierarchy through group roles |
| Heavy | Redundant surfaces, borders, type weight, and density | Remove unnecessary boundaries or emphasis |
| Cramped | Exact boundary, text growth, and hit area | Correct its allocation or overflow rule |
| Content drifts inward | Accumulated nested insets | Remove redundant parent/child padding |
| Text looks off-center | Line boxes and visible glyph bounds | Correct alignment before optical adjustment |
| Cards have uneven edges | Shared insets, borders, and asset whitespace | Establish a shared content axis |
| One child needs repeated offsets | Common parent constraints | Repair that arrangement |

State expected relationships before measuring. Record expected value or rule, observed value, units, tolerance, sampled state, and pass/fail/unavailable status. Choose tolerance from the medium's rounding and output scale; never use it to excuse a visible or functional defect. Pair arithmetic with perceptual inspection: a mathematically valid composition can still have poor hierarchy or balance.
