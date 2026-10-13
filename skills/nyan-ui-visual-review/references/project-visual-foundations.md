# Project visual foundations

Help the project express one coherent design language through reusable roles and relationships. Extend what works before proposing a replacement. Keep the foundation proportional to the project's current surfaces; avoid building a speculative component library or a second theme system.

## Distill the existing language

Inspect the user brief, brand guidance, canonical style owners, and a small representative sample of the actual work. Include distinct contexts that can expose conflicting rules, such as a dense form and a spacious overview, a content slide and a title slide, or body pages and chapter openers. Expand the sample only when an unresolved choice or shared owner warrants it.

Trace each important visible choice back to its source: token, component variant, native text style, master, template, asset, or local override. Use DOM/computed measurements or native bounds alongside renders. Do not treat extracted raw values, names, or frequency counts as a complete design system.

Record a compact inventory:

| Role or relationship | Observed choice and use | Source owner | Interpretation | Proposed disposition |
| --- | --- | --- | --- | --- |
| Body reading | Font, measure, leading in actual prose | Body text style | Repeated reading role | Retain if readable |
| Related-item spacing | Gaps around icon-label pairs | Control primitive | Reused group rule | Name or reuse its semantic role |
| Section separation | Different gaps across contexts | Layout/template | Intentional density or drift | Compare purpose before merging |
| Primary action | Fill, contrast, type, shape, states | Action variant | Decision hierarchy | Preserve meaning across themes |
| One-off inset | Local offset in one instance | Local override | Cause not established | Trace parent and visible bounds first |

Label observations separately from inferred intent. Treat explicit user direction as intended outcome, canonical guidance as declared policy, source as implementation, and renders as visible behavior. Report conflicts; do not automatically promote either the most frequent value or the latest isolated example.

Classify variation before consolidating:

- **Retain:** Keep a coherent choice that supports the intended identity and task.
- **Consolidate:** Map redundant choices serving the same role to the existing owner after checking consumers.
- **Preserve as a variant:** Keep differences justified by density, role, medium, state, or brand expression.
- **Correct:** Trace a defect to its owner before treating it as a foundation rule.
- **Defer:** Name missing evidence or unresolved direction; avoid inventing consensus.

Explain the language in a few concrete relationships: for example, “compact controls, generous section separation, quiet surfaces, strong title contrast.” Tie each statement to examples and measurable rules. Do not replace the project's identity with generic adjectives or a fashionable palette.

## Scaffold the smallest useful foundation

For a new project, derive candidate roles from the brief, content, medium, and first intended compositions. Mark their values provisional until rendered. For an existing project, fill actual gaps and reconcile drift rather than starting from blank defaults.

Select only relevant domains:

| Foundation | Define | Prove in context |
| --- | --- | --- |
| Typography | Reading and display roles, family, weight, size, leading, measure, wrapping | Body text, heading, label, and long content |
| Color | Text, surface, emphasis, action, and status roles with required theme mappings | Hierarchy, contrast, and state distinction |
| Space and layout | Binding grid contract, group gaps, content insets, section rhythm, alignment axes, width and reflow constraints | Measured local component and parent composition |
| Shape and depth | Control and surface shapes, strokes, nested boundary relationships, elevation purpose | Neighboring and nested surfaces |
| Icons and imagery | Family, apparent weight, occupied area, crop and framing roles | Actual use size and varied assets |
| Motion | Purpose, anchor, duration/easing roles, coordinated properties, reduced-motion outcome | One meaningful transition and its failure path |
| Components or templates | Required anatomy, variants, states, slot relationships, content/overflow rules | Two distinct uses plus a stress case |

Separate raw values from semantic roles only where that distinction adds value. Reuse existing token and naming conventions. Permit two roles to share today's value without merging their meaning; avoid creating an alias for every number or every individual component.

Define constraints as well as tokens. A gap token alone does not establish who owns it, when it applies, how a group wraps, or how text grows. Apply the shared spatial method to those relationships without duplicating its full checks here.

Preserve meaningful variation: a display heading need not share body leading, a dense table need not use hero spacing, and a printed page need not use interactive control sizing. Define the variant's purpose and owner instead of normalizing all differences.

## Map the foundation to real owners

Prefer existing project locations over new parallel files. Express the foundation in the medium's native structure:

- For web work, map roles to existing theme tokens, shared controls, and layout primitives.
- For presentations, map roles to text styles, masters, layouts, and chart conventions.
- For books, map roles to paragraph/character styles, page templates, and text-flow rules.
- For graphics, map roles to shared swatches, text styles, symbols, and export presets.
- For motion, map roles to the existing transition or timeline owner and its reusable presets.

Do not generate all these structures for every project. Do not add a package, theme engine, documentation site, asset library, or governance process unless the requested work needs it. Keep an inventory in working notes by default; place durable guidance beside the canonical project owner when documentation or scaffolding is in scope.

Keep the same agent free to author and critique in sequence. Treat this reference as decision guidance, not an instruction to find another person or agent. Apply requested scaffolding through the normal authoring workflow and verify its output before reporting it complete.

## Adopt through a representative slice

Choose a bounded slice that exercises different roles together. For a web project, a button/input pair, a form or card, and their enclosing page can expose the foundation without rebuilding every route. For a deck, use a title slide and a dense evidence slide; for a book, a body spread and a chapter opener.

Map old roles or overrides to proposed owners before changing them. Inspect the shared owner's affected consumers. Keep a narrower opt-in variant when a global change would exceed scope; do not change a shared token globally while claiming to update only the sample.

Remove replaced definitions and overrides within the migrated scope once their consumers are verified. Identify remaining unmigrated uses explicitly. Do not retain duplicate active sources indefinitely or describe a pilot slice as project-wide adoption.

Use these counterexamples to challenge the candidate system:

| Tempting consolidation | Challenge | Appropriate outcome |
| --- | --- | --- |
| Replace every 15–17 px gap with 16 px | Check role, computed rounding, transform, and optical intent | Consolidate only equivalent intentional gaps |
| Use one inset for every container | Check nested groups and density | Keep distinct surface and local-group roles |
| Promote the most common color | Check whether it is legacy or fails the intended role | Retain, correct, or defer based on evidence |
| Apply a demo token across the app | Inspect all consumers touched by the shared owner | Verify affected scope or use a bounded variant |
| Match a book and website numerically | Compare medium, viewing conditions, and task | Share language while allowing native values |

## Challenge the foundation in context

Compare representative renders before and after with stable content, dimensions, and state. Check role consistency across distinct uses, hierarchy within each use, measured spatial relationships, and at least one relevant stress case. Select long text, narrow parent, theme change, validation error, repagination, export substitution, or interrupted motion according to the artifact.

For a new system, compare the first render with the proposed constraints rather than inventing a before state. Keep the result provisional when rendering is unavailable. Do not claim completeness from a token file, swatch board, or one attractive demo alone.
