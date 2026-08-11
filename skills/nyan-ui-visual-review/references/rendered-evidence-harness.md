# Rendered evidence harness

Use this reference when a visual review uses a live HTML, React, Tailwind, or CSS
interface and screenshots can consume too much working context.

## Contents

- Transfer model
- Evidence loop
- Compact evidence packet
- Screenshot budget
- Geometry probe
- Geometry interpretation
- State lifecycle

## Transfer model

Adapt scene-graph design-agent practices to code without copying `.pen` mechanics.

| Design-canvas capability | Code-native equivalent |
| :--- | :--- |
| Document state | Route, viewport, interaction state, DOM or accessibility snapshot |
| Node bounds | `getBoundingClientRect()` and scroll geometry |
| Node styles | A selected set of computed CSS properties |
| Component instances | React components, variants, and shared primitives |
| Design variables | CSS custom properties, theme tokens, and Tailwind configuration |
| Targeted node screenshot | Selector-level or region-level screenshot |
| Canvas mutation | Focused source edit through the owning component or token |
| Canvas warnings | Console, accessibility, overflow, type, lint, and test failures |

Keep task guides, hierarchy checks, density selection, anti-generic checks,
section-level verification, and direct repair. Replace design-file operations with
repository ownership and browser evidence.

## Evidence loop

1. Open the smallest rendered surface that contains the reported condition.
2. Capture one baseline at a named route, viewport, and interaction state.
3. Inspect the baseline before reading broad implementation detail.
4. Convert visual observations into a compact evidence packet.
5. Read only the owners needed to explain those observations.
6. Use geometry for measurable claims.
7. Use a targeted screenshot for perceptual claims.
8. Implement the authorized fix through the canonical owner.
9. Repeat the same geometry probe and screenshot target.
10. Compare the same content, viewport, and state.
11. Retain paths and conclusions instead of repeatedly loading image data.

Do not capture every route or state in advance. Expand only when a finding, shared
owner, responsive transition, or release risk requires another state.

## Compact evidence packet

Record one packet per inspected state. Store it in working notes or an isolated
visual-evidence directory when the task needs persistence. Do not commit generated
evidence unless the repository owns that convention.

```json
{
  "surface": "Profile settings form",
  "route": "/settings/profile",
  "viewport": { "width": 1440, "height": 900 },
  "state": "default",
  "render": "visual-evidence/profile-before.png",
  "observations": [
    {
      "claim": "The primary action does not dominate the form actions.",
      "locator": "form footer",
      "kind": "perceptual"
    }
  ],
  "geometry": {
    "main": { "x": 280, "width": 1096 },
    "form": { "x": 444, "width": 560 },
    "save": { "x": 876, "width": 128 }
  },
  "owners": ["ProfileForm", "Button", "--action-primary"],
  "unavailable": []
}
```

Keep observations short. Record the visible region or selector that supports each
claim. Separate perceptual observations from measurable geometry.

## Screenshot budget

- Use one full-surface screenshot to establish the baseline when composition or
  hierarchy is in scope.
- Use selector-level crops for components, dialogs, tables, and local states.
- Reuse the saved path or artifact identifier after the initial inspection.
- Reopen the image only when a detail cannot be answered by the evidence packet.
- Capture another screenshot after a coherent section or fix, not after every edit.
- Keep before and after screenshots comparable in viewport, content, state, crop,
  browser zoom, and platform.
- Use screenshots for hierarchy, balance, typography, color, depth, density, and
  optical alignment.
- Use DOM and computed evidence for dimensions, spacing, overflow, clipping,
  alignment deltas, sticky behavior, and responsive thresholds.

Do not encode an image as prose exhaustively. Retain only observations that affect
the diagnosis, proposed change, or verification.

## Geometry probe

Run a focused browser evaluation against named selectors. Change the selector map
for the inspected surface. Do not dump the complete DOM or every computed style.

```js
(() => {
  const targets = {
    main: "main",
    form: "[data-review='profile-form']",
    save: "[data-review='save-action']",
  };

  return Object.fromEntries(
    Object.entries(targets).map(([name, selector]) => {
      const element = document.querySelector(selector);
      if (!element) return [name, { selector, missing: true }];

      const rect = element.getBoundingClientRect();
      const style = getComputedStyle(element);

      return [name, {
        selector,
        rect: {
          x: rect.x,
          y: rect.y,
          width: rect.width,
          height: rect.height,
          right: rect.right,
          bottom: rect.bottom,
        },
        contentOverflow: {
          horizontal: element.scrollWidth > element.clientWidth,
          vertical: element.scrollHeight > element.clientHeight,
        },
        viewportOverflow: {
          left: rect.left < 0,
          right: rect.right > window.innerWidth,
          top: rect.top < 0,
          bottom: rect.bottom > window.innerHeight,
        },
        style: {
          display: style.display,
          position: style.position,
          gap: style.gap,
          padding: style.padding,
          fontFamily: style.fontFamily,
          fontSize: style.fontSize,
          lineHeight: style.lineHeight,
          color: style.color,
          backgroundColor: style.backgroundColor,
          borderRadius: style.borderRadius,
          boxShadow: style.boxShadow,
          overflow: style.overflow,
        },
      }];
    }),
  );
})()
```

Use stable semantic selectors that already exist. Add temporary review attributes
only when the requested implementation scope permits that code change. Do not
weaken semantics or production behavior to make inspection easier.

## Geometry interpretation

Calculate relationships instead of judging isolated values:

- Compare shared left, right, center, and baseline axes.
- Compare the gap within a group with the gap between groups.
- Compare repeated component dimensions and internal regions.
- Compare content size with client size to detect clipping and overflow.
- Compare the same geometry across relevant breakpoints and states.
- Compare computed styles with the intended token or component owner.

Treat geometry as evidence of layout behavior, not visual quality by itself. A
measured difference is a defect only when it weakens hierarchy, grouping,
readability, consistency, responsive behavior, or the intended task.

## State lifecycle

Keep a small ledger with these states:

```text
baseline captured -> observations recorded -> owners traced -> fix authorized
-> geometry verified -> targeted render verified -> regression state checked
```

At a context boundary, retain:

- route or surface;
- viewport and interaction state;
- screenshot path or artifact identifier;
- concise observed and inferred findings;
- relevant geometry;
- canonical implementation owners;
- completed and unavailable verification.

Do not retain duplicate screenshots, raw image payloads, full DOM dumps, or all
computed properties as working memory.
