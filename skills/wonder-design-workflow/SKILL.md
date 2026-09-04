---
name: wonder-design-workflow
description: Use when creating, importing, editing, reviewing, verifying, saving, or exporting a design in Wonder through its canvas or external session. Exclude generic frontend review, tldraw work, and code-only implementation.
---

# Wonder Design Workflow

Use Wonder to create, change, or verify a canvas design. Keep visual-critique criteria in `$nyan-ui-visual-review`.

## Select the Surface

1. Confirm that Wonder is the requested design surface.
2. Use the repository as the source of truth for code imports and code handoff.
3. Use a running product to prove runtime behavior.
4. Use a hosted product to prove hosted behavior.
5. Use Git or a pull request only to prove repository history or publication.

Do not treat proof from one surface as proof from another surface.

## Prepare the Work

1. Acquire the current Wonder file and page context before a mutation.
2. Select the file and page that match the request.
3. Pin that selected page for every later read, refresh, and mutation.
4. If the pinned context becomes invalid, reconnect and select the same file again.
5. Never retry against whichever unpinned file or page is currently visible.
6. Inspect the current artboards, components, tokens, and reference material.
7. Inspect the relevant repository owners before an import or handoff.
8. Record each requested surface, state, expected proof, and completion status in a task ledger.

Use `complete`, `partial`, or `unavailable` for each ledger entry. Treat a state as incomplete until its requested proof exists.

## Change the Design

1. Reuse the existing artboards, components, and tokens when they fit the request.
2. Preserve existing routes, workflows, page structure, and copy unless the user asks to change them.
3. Edit the existing artboard when the request or user preference requires one final artboard.
4. Duplicate an artboard only when the user requests a variation or original preservation.
5. Do not create a new frame when the user asks to work in the existing frame or collapse the work to one frame.
6. Make changes to one artboard at a time.
7. Reread the artboard structure after a structural failure before another edit.
8. Do not delete artboards, elements, tokens, or files without an explicit request.

## Verify and Save

1. Capture a final screenshot of each requested design state.
2. Check every requested state against the screenshot and other requested evidence.
3. Mark failed or unavailable states in the ledger.
4. Finish each changed artboard after its final check.
5. Save the changed session after every changed artboard is finished.
6. Save valid partial work even when another requested state is unavailable.
7. Mark the task complete only when every requested state has its required proof.
8. Do not finish or save an unchanged design only for inspection.

## Report the Result

1. Report the selected Wonder file and the completed surfaces.
2. Label each claim as observed, inferred, or unavailable.
3. Separate static-design, runtime, hosted, and Git or pull-request evidence.
4. State incomplete or unavailable proof without calling the task complete.
5. Do not write code, create Git history, publish, or change external systems without an explicit request.
