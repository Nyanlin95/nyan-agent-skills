# Spatial motion

Review motion as a meaningful change of spatial relationships. Use the existing motion system and authoring workflow. Judge valid start and end layouts before evaluating interpolation; animation cannot repair an invalid destination.

## Define meaning, identity, and ownership

Record only fields relevant to the transition:

```yaml
trigger: expand row
identity: same row before and after
owner: list layout
start: collapsed
end: expanded
anchor: row top edge
changes: [row height, following sibling positions]
preserves: [row width, content start, sibling order, inter-row gap]
interruption: retarget from current visible state
reduced-motion: reach final geometry immediately
```

For linear animation, replace interaction triggers with timeline cues and define continuity across shots or scenes. Do not require keyboard behavior or user reversal for a noninteractive film. Check those paths for interactive controls and interactive presentations.

Choose motion from what changed, object identity, parent axes, actual placement, anchor, and free space. Avoid arbitrary quadrant-based entrances. Use no motion when it delays access without explaining a relationship.

| Change | Starting treatment | Preserve or inspect |
| --- | --- | --- |
| Row expands | Grow away from heading and move siblings together | Heading anchor and gaps |
| Edge panel opens | Reveal from its declared edge | Overlay versus in-flow behavior |
| Popover opens | Small reveal from actual attachment edge | Collision-adjusted placement and focus |
| Item changes grid cell | Move corresponding identity between measured bounds | Reading order and internal state |
| List item enters or leaves | Open or close its slot coherently | Remaining identities and control access |
| Card becomes detail | Shared geometry only with clear correspondence | Object anchor and readable content |
| Tab or value updates | Immediate update or restrained crossfade | Stable region and text baseline |
| Sequence advances | Use established semantic direction | Reverse meaning and reading direction |
| Centered dialog opens | Immediate appearance or restrained fade | Centering and usable focus |
| Responsive grid reflows | Direct reflow by default | Content size and semantic order |

## Coordinate dependent geometry

Assign each animated property one owner. Let children move with the parent unless their local meaning requires separate motion, such as a disclosure icon rotating during expansion. Inspect composed transforms before accepting doubled travel or drifting children.

Express a rectangle's anchor as fractions `(ax, ay)`:

```text
anchor x = x + ax * width
anchor y = y + ay * height
new x = fixed anchor x - ax * new width
new y = fixed anchor y - ay * new height
```

Use `(0, 0)` for top-left, `(0.5, 0.5)` for center, or `(1, 1)` for bottom-right in that coordinate system. Treat these equations as relationships, not a requirement for absolute positioning.

Check an expanding-row example with an 8 px sibling gap:

```text
B: y = 72, height grows from 64 to 128
C: y moves from 144 to 208
p: shared eased progress from 0 to 1
B height(p) = 64 + 64*p
C y(p) = 144 + 64*p
gap(p) = C y(p) - (72 + B height(p)) = 8
```

Flag unrelated timing when it makes that required gap compress or expand. Permit intentional overlap only when the design brief calls for it. Do not snap intermediate positions to a spacing grid; fractional travel is valid.

Compare start and destination bounds in the same coordinate space, accounting for scroll and ancestor transforms. Recommend preserving identity and retargeting from current visible geometry instead of remounting content to replay entrances.

## Preserve content during change

- Keep live text and icons at readable proportions; avoid stretching the whole surface to resize it.
- Inspect text wrapping separately from the outer box; width changes can produce discrete line breaks.
- Select immediate reflow, a stable text measure when it fits, or a justified crossfade rather than assuming smooth boxes imply smooth text.
- Keep temporary visual copies out of focus and accessibility exposure, and avoid copying application state into them.
- Check that final clipping exposes required content and focus treatment.
- Remove temporary transforms and copies after settling; do not queue obsolete transitions during continuous resizing.

## Evaluate timing and sequencing

Derive travel from actual geometry, not a decorative large slide. Choose timing through rendered evaluation of travel, scale, frequency, and access latency. Reuse existing duration roles when sufficient.

If distance-based timing is warranted, bound it with `duration = clamp(min, base + k * distance, max)` and declare milliseconds, pixels, and milliseconds-per-pixel respectively. Do not derive duration from grid coordinates alone.

Use coordinated easing for dependent geometry. Inspect spring overshoot near neighboring content and clip edges. Use linear motion when it represents constant movement; do not imply real loading progress without data.

Use stagger only to explain a meaningful sequence. Follow semantic reading order after responsive wrapping. For `n > 1`, bound the step by `min(preferred step, start-delay budget / (n - 1))`; use zero for `n <= 1`. Include the last item's duration when evaluating total time. Avoid delaying essential controls or adding stagger to every grid.

## Verify between endpoints

Use timeline scrubbing, frame stepping, deterministic animation controls, or captured playback where available. Inspect an intermediate state as well as the settled endpoints; do not use a fixed sleep as proof of completion.

For interactive motion, exercise the relevant reversal, rapid repeat, resize, scroll, content update, focus, exit, and reduced-motion paths. Check that an old completion callback cannot restore a superseded state. Review exit interaction and valid focus restoration separately from a lingering visual exit.

For linear motion, inspect object continuity, readable dwell time, text distortion, clipping, scene cuts, and the final export's timing and framing. Verify at delivery frame rate and aspect ratio when available; label preview-only evidence.

Record assertions such as stable anchor, preserved gap, unstretched text, continuous reversal, truthful popover origin, reachable controls, equivalent reduced-motion outcome, and no leftover presentation layers. Mark any unsampled transition behavior unavailable rather than inferring it from screenshots.
