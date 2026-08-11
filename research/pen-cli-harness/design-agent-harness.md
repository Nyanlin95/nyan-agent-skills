# pen.dev design-agent harness

This is the design-facing harness used by `@pen.dev/cli` 0.3.2. It is separate
from the public package `SKILL.md`.

## Runtime assembly

The compiled CLI contains a system-prompt builder equivalent to:

```text
system prompt =
  full .pen TypeScript schema
  + general canvas and execute instructions
  + current guide/style catalog returned by get_guidelines()
```

Before the first model turn, the CLI also appends:

```text
user prompt =
  requested design task
  + attachment context
  + current get_app_state result
```

The bootstrap app state includes the live document, selection, top-level nodes,
reusable components, browser state, schema instructions, and canvas rules. The
prompt explicitly tells the agent that this state was fetched immediately before
the turn and does not need to be fetched again unless later evidence makes it
stale.

For Claude, the Pen instructions are appended to the Claude Code preset system
prompt. Codex, Gemini, Cursor, and Pen-hosted models use their corresponding
runtime adapters, but receive the same Pen system prompt and MCP tool surface.

## Design intelligence

The quality does not come from one hidden taste sentence. It comes from a layered
system:

1. A strict structural contract for the `.pen` scene graph.
2. Canvas rules that discourage common AI design artifacts.
3. Task guides for web apps, landing pages, mobile apps, slides, dashboards,
   tables, design systems, Tailwind, and code export.
4. Twenty-six parameterized style archetypes.
5. Palette, type, roundness, elevation, and imagery modules selected as style
   parameters.
6. Iterative work through small `execute` calls.
7. Screenshot and geometry checks after each completed section.
8. Direct repair of the existing design instead of deletion and regeneration.

Important taste rules in the core canvas prompt include:

- Do not create repetitive styles and grids.
- Add unique layout elements when they improve the design.
- Do not wrap every element in a card or box.
- Avoid excessive gradients, shadows, and rounded corners.
- Use containers only for real structure or function.
- Keep one clean scene hierarchy and use reusable components for repetition.
- Verify clipping, contrast, alignment, spacing, and schema-to-visual agreement.
- Use generated SVG or imagery for freeform artwork instead of crude hand-built
  path illustrations.

## Tool surface

The model-facing design tools are:

- `execute`: read and mutate the `.pen` document with Insert, Copy, Update,
  Replace, Move, Delete, Generate, SetVariables, GetVariables, Get,
  FindEmptySpace, and Print.
- `get_app_state`: live document, browser, schema, canvas, script, and shader
  context.
- `get_guidelines`: task guides and parameterized styles.
- `get_screenshot`: targeted visual verification.
- `export_nodes`: PNG, JPEG, WEBP, or PDF export.
- `export_html`: HTML plus Tailwind or CSS export.
- `browser`: load, inspect, screenshot, or import a live web page.
- `spawn_agents`: optional parallel designer-agent delegation.

`spawn_agents` is present in the compiled model tool registry but omitted from
the ordinary interactive help. The CLI enables it only for runs configured for
multiple designer agents. The root agent is instructed to create one fewer child
than the total requested designer count and to keep one partition for itself.

## Execution behavior that improves results

- Every inserted node must have a human-readable name.
- Root frames stay marked as placeholders until their section is complete.
- Failed `execute` snippets are patched through an edit ID instead of retried as
  unrelated new operations.
- Warnings must be fixed in the next operation.
- Layout is verified section by section, not only at the end.
- `Get` visitors expose computed bounds and clipping problems.
- Screenshots are reserved for visual judgments; geometry reads handle sizing.
- Generated imagery is asynchronous, so the agent continues other work and
  checks the placeholder state instead of repeatedly regenerating.

## Where it lives

The prompt assembly is compiled into:

```text
C:\Users\nyanl\AppData\Roaming\npm\node_modules\@pen.dev\cli\dist\index.mjs
```

The relevant compiled functions were identifiable as:

- `Nx`: builds the system prompt from schema, canvas rules, and guideline list.
- `Px`: builds the user turn and app-state bootstrap context.
- `Fx`: adds multi-designer partition instructions.

Those names are minified build identifiers and can change between releases.
