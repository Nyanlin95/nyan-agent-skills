# Prototype modes

Read the section for the selected prototype form. Combine sections only for a hybrid artifact.

## Document

Build a designed reading experience rather than a raw Markdown export.

- Establish a clear title, purpose, audience, and reading order.
- Use headings, summaries, callouts, tables, timelines, diagrams, or checklists only when they improve comprehension.
- Keep prose widths readable and long sections navigable.
- Make checklists operable with labels, visible state, reset, and optional progress when progress helps.
- Preserve printing when the artifact may be shared or reviewed on paper.
- Avoid application chrome when the artifact's main task is reading.
- Do not turn every paragraph into a card.
- Verify heading order, readable measure, and text resizing.
- When print matters, verify print behavior.
- Distinguish the summary, evidence, and action.

Useful document prototypes include decision briefs, plans, audits, release evidence, comparison sheets, interactive specifications, and guided checklists.

## Interface

Build enough behavior to test the task, hierarchy, and state model.

- Identify the primary task and keep its action visually clear.
- Include only the navigation needed to understand the prototype.
- Use realistic content and varied lengths instead of repeated placeholders.
- Implement the relevant default, hover, focus, active, disabled, loading, empty, error, success, and narrow-width states.
- Keep one source of in-memory state.
- Make reversible actions reversible and provide reset.
- Preserve clear labels and recovery copy.
- Avoid fake controls, dead menus, and links that unexpectedly leave the prototype.
- Classify prominent controls by effect: navigation, filtering, state selection, or action.
- Check that the layout gives the primary task and current state enough visual priority.
- Verify wrapping, overflow, touch targets, and reading order.
- Check the intermediate widths that cause content to reflow.

When you compare directions, put each variant in the same prototype folder. Provide an explicit switcher.

Keep shared content constant. This makes the comparison test the design instead of the sample data.

## Visual experiment

Use a visual engine only when the prototype tests space, time, depth, material, motion, or direct manipulation.

- Start with the smallest scene that demonstrates the effect.
- Separate scene setup, state, rendering, and disposal when the code needs multiple files.
- Pin library and addon versions to the same release.
- Provide visible loading and failure states for external assets.
- Use local placeholder geometry before adding heavy models or textures.
- Cap renderer pixel ratio to a justified value.
- Resize the renderer and camera from the actual container.
- Use delta time for time-based motion.
- Stop or throttle animation when hidden or offscreen.
- Dispose geometries, materials, textures, controls, listeners, and animation handles created by the prototype.
- Provide reduced-motion or a static alternative when motion is not essential to comprehension.
- Provide conventional HTML controls and explanation around a canvas when users must understand or operate it.

Do not require Three.js for effects that CSS, SVG, or Canvas can express more simply.

## Hybrid

Keep the document as the semantic backbone and embed interaction only where it improves understanding.

- Explain the model before asking the user to manipulate it.
- Keep controls adjacent to the diagram, simulation, or example they affect.
- Reflect the current state in text as well as visually.
- Provide a deterministic reset and useful initial state.
- Ensure the narrative remains understandable when animation is reduced or scripting fails.
- Avoid letting the interactive section overwhelm the document's reading order.

## Completion test

Before handoff, answer:

1. What question does this prototype answer?
2. Can the user reach the answer through the implemented path?
3. Is every implied control functional or clearly marked as simulated?
4. Does the artifact work at its intended viewport?
5. Are keyboard use, focus, contrast, and reduced motion adequate for the prototype?
6. Are external dependencies pinned and disclosed?
7. Is every created file inside one named folder?
8. Can the user remove the complete artifact by deleting that folder?
9. Does the final workspace-status comparison prove the containment claim?
10. Were all helper processes started for verification identified and stopped safely?
