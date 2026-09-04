---
name: build-html-prototype
description: Builds disposable HTML prototypes in one removable folder. Use for browser documents, checklists, reports, UI mockups, interaction tests, animation studies, HTML Canvas demos, and Three.js prototypes. Scale from one static `index.html` to a multi-file browser experience. Audit the folder boundary and verify the rendered result. Do not add prototype code to a production application or create a Codex Canvas.
---

# Build HTML Prototype

Build a browser artifact that makes an idea visible, testable, or clear. Treat it as disposable evidence, not production code.

This skill creates files that run in a browser. It does not create a Codex Canvas. Use the `canvas` skill when the user asks for a live Codex Canvas.

## Keep one prototype owner

Use this skill for a standalone browser artifact in one removable folder.

Use a project-native workflow for a temporary route, component, state model, or production-adjacent implementation.

Do not let both workflows own the same prototype.

## Protect containment

Put the complete prototype in one new folder. Use the location that the user requests.

Otherwise, use the repository's prototype convention. If no convention exists, create `<workspace>/prototypes/<short-slug>/`.

Before writing:

1. Record the existing workspace status without changing it.
2. Resolve and state the absolute prototype folder.
3. Confirm that the folder does not exist.
4. If it exists, choose a new name or get explicit authority to update that exact prototype folder.

Do not edit files outside that folder unless the user requests a separate catalog or link.

Do not change the host router, package files, build configuration, source tree, or shared assets.

Keep all authored files inside the prototype folder. Prefer one `index.html` for a small artifact.

Split files only when inline code is difficult to read or an asset needs a separate owner.

Use in-memory state or fixtures. Do not use production services, credentials, analytics, databases, or user data.

Label illustrative data when a user could mistake it for real data.

Treat pasted, imported, URL-derived, and fixture content as untrusted. Render it as text by default.

Do not use `innerHTML`, dynamic code execution, or unsanitized URLs for convenience.

Make each permitted remote origin explicit and narrow.

## Frame the question

State one question that the prototype must answer. Infer it from the request and available context.

Ask only when different interpretations produce materially different artifacts.

Choose one form:

- **Document:** A designed brief, checklist, plan, comparison, report, guide, specification, or narrative explainer.
- **Interface:** A screen, workflow, component, dashboard, form, tool, or interaction model.
- **Visual experiment:** A spatial, canvas, WebGL, shader, physics, particle, or Three.js study.
- **Hybrid:** A document that contains interactive controls, diagrams, simulations, or UI examples.

Read [references/prototype-modes.md](references/prototype-modes.md) for the selected form. Read only the sections that apply.

## Choose the smallest technical level

Use the lowest level that can answer the question:

1. **Static:** Semantic HTML and CSS.
2. **Interactive:** Add small vanilla JavaScript behavior and in-memory state.
3. **Structured:** Use separate local modules or data files when the artifact has several views or substantial behavior.
4. **Visual:** Add Canvas, SVG, WebGL, or Three.js only when spatial or animated behavior is part of the question.

Do not add a framework, bundler, package manager, or build step for familiarity.

Use the host stack only when the user requests production-stack fidelity. Keep its configuration inside the prototype folder.

Use a pinned CDN dependency only when it reduces necessary work and permits network access.

Report its name, exact version, source, and network requirement. Do not use `latest`.

Do not describe a network-dependent artifact as offline or fully self-contained.

Keep an offline prototype local or dependency-free.

## Set the design contract

Before implementation, record:

- The audience and question being tested.
- The primary task or reading path.
- The intended viewport and input mode.
- The content density and information hierarchy.
- The visual direction and available brand anchors.
- The protected terms, data meaning, and behavior.
- The states and interactions required to answer the question.

Use repository or user evidence when it exists.

Otherwise, state the selected direction as a prototype assumption. Do not treat this assumption as a production design rule.

## Build the artifact

1. Inspect relevant product terms, content, screenshots, design tokens, or behavior without copying production machinery into the prototype.
2. Define the essential content, states, and interactions.
3. Build the primary path first.
4. Add only the alternate states needed to answer the question.
5. Make each control work.
6. Remove decorative controls that imply unavailable behavior.
7. Expose important state changes in the interface.
8. Make the layout responsive for the intended viewport.
9. Add keyboard access, visible focus, semantic structure, readable contrast, and reduced-motion behavior.
10. Provide an obvious reset when exploration changes state.
11. Remove scaffolding and dead experiments from the final prototype folder.

Do not present a static mockup as a working system.

Mark simulated uploads, saves, payments, messages, AI output, and network activity as simulated.

## Keep visual ambition purposeful

Match the visual language to the prototype question. Preserve supplied brand or design-system evidence.

If no direction exists, select a coherent direction and state it briefly.

Use motion to explain cause, hierarchy, navigation, or spatial change. Support `prefers-reduced-motion`.

Pause expensive animation when the page is hidden.

For continuous rendering, resize correctly and cap the pixel ratio. Release resources when the artifact no longer needs them.

Render on demand when the scene does not need an animation loop.

Do not add gradients, glass, cards, icons, charts, particles, or 3D merely to make the artifact appear finished.

## Run and verify

Give the prototype one obvious run path:

- Open `index.html` directly when the artifact has no module, fetch, or browser-origin requirement.
- Otherwise give one local-server command that serves only the prototype folder.

When you start a helper server, record its exact process.

Stop only that process after verification. Keep it active only when the user requests this.

Do not kill a process by name, port pattern, or broad command-line match.

Verify the actual rendered artifact, not only its source:

1. Open the documented entry point.
2. Confirm the first render has no blocking console error.
3. Exercise the primary interaction and reset path.
4. Check the intended viewport and one narrower width when layout can reflow.
5. Check keyboard focus and reduced motion when the artifact is interactive or animated.
6. Confirm that referenced local assets resolve.
7. Compare the final workspace status with the recorded baseline.
8. Confirm that every authored change is inside the prototype folder.
9. Report each separately authorized catalog or link change.
10. Confirm that the prototype folder contains every new local dependency.
11. Do not delete the prototype during verification.

For Three.js, Canvas, or WebGL, check initialization failure, resizing, and animation cleanup.

When possible, check a device without high-performance graphics. State unavailable runtime coverage.

## Hand off

Report:

- The question the prototype answers.
- The absolute prototype folder and entry point.
- The form and technical level selected.
- The run command or direct-open instruction.
- The interactions and states implemented.
- The checks that passed and remained unavailable.
- External dependencies and network requirements.
- The containment audit result and any separately authorized external change.
- The deletion boundary: remove the named prototype folder only.

Do not present prototype behavior as a production implementation or architecture decision.

State what the prototype showed and what it did not prove.
