# Starting projects

Build toward the user's first useful outcome with the least structure that supports it honestly. Treat the following as decision guidance, not a fixed file tree or required technology stack.

## Establish what is missing

Inspect the target directory, applicable instructions, runtime availability, existing manifests, lockfiles, configuration, commands, and any supplied template. Preserve partial or dirty work. Distinguish an empty project from a project whose entry point is merely unfamiliar.

Extract the smallest domain model needed for the first journey: core entities, identity, ownership, relationships, valid state changes, and the user's observable result. Use the user's terminology. Avoid a general modeling exercise when a few named rules make the implementation clear.

Check unsettled assumptions before committing them to storage or routing. Distinguish a personal tool from shared collaboration, a draft from a published record, and a local session from durable cross-device data. Ask about their user consequences when unresolved; do not silently choose a product model to simplify implementation.

## Choose a runnable base

Reuse a sound existing scaffold when available. Otherwise select the smallest suitable setup supported by the requirements and available environment. Follow explicit user choices. Verify current official guidance for version-sensitive setup or provider contracts instead of using remembered installation commands.

Use framework conventions and a supported dependency baseline. Add packages for concrete needs, not hypothetical future features. Avoid inventing a generic repository/service layer, plugin system, queue, event bus, theme engine, or provider registry for an unproven requirement.

Establish only the commands the project needs, such as development, focused checks, and build. Use the native package or build tool as their owner. Provide non-secret configuration examples and concise startup instructions in the existing project entrypoint or root README. Keep secrets out of source, output, and client bundles.

If the project has no gate, assemble a small native check command from applicable existing tool capabilities; do not create a separate verification framework. Match checks to the artifact: a static page may need no compiler or unit-test suite, while a persisted workflow needs data and failure proof.

## Build a complete first journey

Connect the actual user action to its result across the boundaries the product requires. For a simple tracker, that might be create a record → see it in the list → reopen it → edit it → recover from an unsuccessful save. Use the requested workflow, not this example, to choose the slice.

Implement the required source of truth before displaying a successful outcome. Include input validation, visible pending/error states, and useful recovery. Keep user input available after a failed submission where appropriate. Prevent duplicate effects when retry or repeated activation can create them.

Verify return paths: refresh, reopen, restart, direct entry, back navigation, or cancellation as relevant. Do not claim persistence from a screen that still displays an in-memory object. Match the proof to the storage promise: a browser reload and a process restart answer different questions.

Let representative UI carry the project's visual roles and real content constraints. Reuse local primitives or templates as repetition appears. Use fake data for exploration only with clear labeling; do not disguise hard-coded totals, inert buttons, fake sign-in, or simulated payments as implemented behavior.

Keep prototype and product purposes distinct. Use disposable mocks when the user wants an exploration; build real declared behavior when they asked for a working application. If an external integration is blocked, isolate the mock at its boundary and retain that limitation in the delivered scope.

## Decide service boundaries from the task

| Boundary | Resolve when it affects the first version | Smallest useful proof |
| --- | --- | --- |
| Persistence | Data lifetime, source of truth, schema, and recovery expectations | Create and read back through the real path after the relevant reload or restart |
| Identity and access | Who can see or change each record, including unauthenticated access | Allowed access and a denied cross-user or unauthorized operation when applicable |
| External service | Real versus simulated behavior, configuration, errors, and repeat effects | Isolated contract checks plus authorized live proof where required |
| Delivery | Local-only, preview, or deployed target and its runtime requirements | Run/build locally; claim deployment only after authorized target verification |
| Diagnostics | How an operator can identify the first journey's failure without leaking data | Trigger a relevant failure and inspect a useful sanitized signal |

Apply only needed boundaries. A static portfolio does not need accounts or a database. A shared private workspace cannot substitute a cosmetic login screen for enforced access. Keep server authority distinct from client visibility. Use platform-specific guidance where the selected technology requires it.

Keep setup errors explicit and actionable. Name a missing configuration key without printing its value. Avoid logging credentials, private content, or full provider payloads. Begin with useful native errors or logs before adding an observability platform.

## Keep the starting point easy to change

Separate product rules from provider-specific shapes at real external boundaries. Keep configuration with its owner and avoid hard-coded machine assumptions. Prefer direct code with a clear replacement point to speculative portability layers.

Accept a shortcut only when its consequence is understood and it still satisfies the declared first version. Record material temporary choices beside the relevant owner with their limitation, affected scope, and replacement condition. For example, a local store may suit an explicitly single-device tool but not a promised shared workspace.

Do not classify missing authorization, secret exposure, silent data loss, or false success as acceptable starter debt. Resolve them before claiming the affected feature works. Remove replaced scaffolding, duplicate sources, unused generated features, and demo-only paths inside the completed scope.

Use a small owner note when a decision will matter later; do not maintain a parallel planning system for every default. Keep the initial project understandable enough that someone can locate the main journey, change a rule, run it, and diagnose failure.
