# Aerial Gravitas — resolved example

This is a normalized readable version of a resolved style response. Parameters:

- Palette: Alpine Terracotta
- Roundness: Basic Roundness
- Elevation: Gentle Lift
- Imagery: Aerial Photography
- Headings: Playfair Display
- Body: Inter
- Captions: Inter
- Data: Geist Mono

## Identity

Full-bleed photography is a structural surface rather than an accent. It alternates
with typographic slabs to create rhythm. Every photographic block uses a tonal
overlay that unifies imagery and content.

## Layout

Use stacked, full-width horizontal slabs with hard transitions. Within each slab,
use an asymmetric split: large primary text at the leading edge, supporting text
and the main action at the trailing edge.

One zone may use an extreme two-column split with index markers on the leading edge
and names on the trailing edge. Use only one floating container overlapping a slab
boundary; it is the only layered-depth moment.

Keep density moderate to sparse. Text slabs use generous margins. Photography
bleeds edge to edge. Separate slabs with surface-color changes, one optional
hairline rule, and whitespace. Do not shadow the structural slabs.

## Token behavior

- Alternate `surface.primary` and `surface.inverse`.
- Reserve `accent.primary` for index markers, small indicators, and actions.
- Use secondary and tertiary accents only once at one transition.
- Use `rounded.sm` for actions and `rounded.none` for structural containers.
- Do not use pills.
- Apply `shadow.md` only to the single floating container.

## Decoration

Use full-bleed aerial or landscape photography as the main decorative layer. Add
low-opacity geometric construction lines over the photographic surface. Permit one
row of small color blocks at a single transition; do not repeat it.

## Hierarchy

Use three scale levels. Primary headings are about five to six times body size,
indexed list items about two to three times body size, and labels/body at baseline.
Each slab has one clear leader.

## Imagery sourcing

Search for aerial, drone, top-down landscape, or bird's-eye imagery. Prefer terrain
patterns, coastlines, urban grids, river deltas, fields, or ocean texture. Require
strong geometry and at least 30% low-detail space for typography. Exclude eye-level
shots, dominant people, text overlays, watermarks, and heavy filters.

## Resolved tokens

```yaml
surface.primary: "#FFFFFF"
surface.inverse: "#1A1A1A"
foreground.primary: "#1A1A1A"
foreground.secondary: "#666666"
foreground.inverse: "#FFFFFF"
border.subtle: "#EEEEEE"
accent.primary: "#5D5DFF"
accent.secondary: "#E07A5F"
accent.tertiary: "#3D5A80"
rounded.none: 0
rounded.sm: 4
shadow.md:
  - { type: shadow, shadowType: outer, color: "#00000008", offset: { x: 0, y: 2 }, blur: 4 }
  - { type: shadow, shadowType: outer, color: "#0000000d", offset: { x: 0, y: 6 }, blur: 16 }
```
