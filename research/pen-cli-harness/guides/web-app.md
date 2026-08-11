# Web App guide

Normalized into readable Markdown from the output of:

```text
get_guidelines({category:"guide", name:"Web App"})
```

## Purpose first

Every screen must have one clearly defined primary purpose, answer one dominant
user question, and support one primary action. Competing goals belong on distinct
surfaces.

## Dominant region

Every screen must have one dominant visual region. Visual weight must reflect
importance. Secondary regions must remain subordinate. Avoid equal-weight layouts
and competing focal points.

## Understandability

The interface must explain itself. Labels must be clear, actions recognizable,
and system state visible. Icons must not replace essential text. If the user must
guess what something does, redesign it.

## Progressive disclosure

Reveal complexity gradually. Show essential information first, keep advanced
controls contextual, and open details on demand. Complexity is allowed; confusion
is not.

## Recognition over recall

Surface relevant actions when needed. Keep navigation and control placement
predictable. Do not require users to remember prior states.

## System status

Every data-driven surface must support loading, empty, error, success, and—when
applicable—permission or restriction states. No silent failure or blank ambiguity.

## Action hierarchy

Use one primary action per screen or section. Reduce secondary actions, distinguish
destructive actions, and place rare actions in overflow. Use honest emphasis.

## Structural consistency

Use similar solutions for similar problems. Navigation, layout rhythm, and spacing
must feel system-driven and stable.

## Density

Choose compact, medium, or airy density deliberately. Do not mix density modes
arbitrarily within one screen.

## Spatial logic

Use one dominant axis per screen. Prefer two structural zones before three. Avoid
unnecessary nested scrolling and decorative dividers. Use whitespace for
separation. Structure over ornament.

## Feedback

Every action needs immediate acknowledgment, clear validation, reversible behavior
where possible, and confirmation for destructive operations.

## Responsive hierarchy

- Mobile: one dominant column; secondary panels become sheets or stacked sections.
- Tablet: transitional structural logic.
- Desktop: multiple zones and higher density are allowed.

Hierarchy must survive every breakpoint. Horizontal scrolling is allowed only
when essential.

## Entity integrity

For each user, record, document, or asset, show its name prominently, expose its
status and key metadata, and make its actions obvious.

## Constraint over decoration

An element must support navigation, understanding, decision-making, or action. If
it supports none of these, remove it. Use as little design as possible.

## Scalability

More data must not break the structure. More features must extend existing
patterns instead of collapsing hierarchy.

## Adaptation

Infer the product type from the user's prompt. Then determine the dominant region,
primary action, density, and progressive-disclosure level. Do not assume a
dashboard, table, sidebar, or canvas unless the purpose requires it.
