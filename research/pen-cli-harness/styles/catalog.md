# Embedded style catalog

The style catalog is returned by `get_guidelines()` and is part of the system
prompt available to the design agent.

## Archetypes

- Aerial Gravitas
- Anchored Ribbon Grid
- Artisan Editorial
- Blueprint Technical
- Centered Device Cascade
- Centered Serif List
- Cinematic Alternating
- Cinematic Device Column
- Color Block Stack
- Dark Centered Platform
- Editorial Landscape Stack
- Editorial Scientific
- Gradient Prompt Stack
- Illustrated Ribbon Stack
- Illustrated Warm
- Inline Friendly
- Modular Bento Showcase
- Monumental Editorial
- Narrative Illustrated
- Product Data Grid
- Product Demo
- Saturated Code Bridge
- Soft Bento
- Spatial Plus
- Split Inverse Showcase
- Zigzag Bold Split

## Parameter modules

Styles request compatible parameters before returning a full design specification.
The available modules include:

- Color palettes: Alpine Terracotta, Amber Night, Bold Tangerine, Carbon Frost,
  Deep Space Neon, Electric Cobalt, Fern Journal, Forest Sage, Heritage Warmth,
  Lavender Cream, Lavender Mist, Minimal Ink, Onyx Peach, Parchment Gold,
  Prismatic White, Rose Charcoal, Solar Warmth, Spring Meadow, Tangerine Orbit,
  Terminal Green, Twilight Garden, Violet Bloom, Violet Void, Warm Concrete,
  Warm Linen, and Warm Parchment.
- Roundness: Basic Roundness.
- Elevation: Gentle Lift, Sharp Depth, Soft Cloud, and Soft Lift.
- Typography categories: Anton, Funnel Sans, Geist, Geist Mono, IBM Plex Mono,
  Inter, Newsreader, and Playfair Display. A style selects separate heading, body,
  caption, and data faces.
- Decorative imagery: archetype-specific modules such as Aerial Photography,
  Cartographic Grid Overlay, and Landscape Photography.

The returned specification describes identity, layout, density, edge behavior,
separation, token usage, decoration, hierarchy, typography, imagery sourcing,
palette values, roundness values, and exact shadow definitions.
