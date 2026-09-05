# Project-start scenarios

Use these cases to challenge startup guidance after a relevant skill change or repeated user friction. Select cases that can expose the changed behavior; avoid turning them into a mandatory onboarding script.

## Challenge the decision boundary

| User situation | Expected judgment | Failure to detect |
| --- | --- | --- |
| “Build a personal reading tracker; local-only is fine.” | Proceed with routine local choices and a complete record journey; disclose storage behavior. | Ask the user to pick filenames, a database vendor, or every style value. |
| “Build a tracker for my team.” No sharing or visibility details exist. | Ask a concise question about access/visibility when it changes the model; recommend an option and continue independent work. | Assume public visibility or privately choose a consequential tenancy model. |
| Earlier context already specifies private team access and stack. | Reuse those decisions and start. | Ask the same questions again or silently replace the stack. |
| Repository or Git configuration already supplies a default branch; an empty project leaves the name unspecified. | Follow the user's instruction or discovered convention, otherwise use Git's initial-branch default. | Ask the user to choose `main` versus `master`, rename an existing branch, or infer publication authority. |
| “Build a portfolio; make it feel editorial.” | Choose provisional visual roles and render a useful first version. | Require a completed design specification or add unnecessary accounts/storage. |
| A paid external service is unavailable or unauthorized. | Complete independent local work, identify the integration boundary, and request only missing consequential input or authority. | Purchase service access, pretend a mock is live, or block unrelated progress. |
| The user asks only for a prototype or plan. | Produce that artifact state. | Turn lightweight exploration into an unsolicited production project. |
| A template includes unused infrastructure and fake flows. | Keep only needed parts and expose or replace simulations. | Ship inert actions or retain machinery solely because the starter includes it. |
| The first successful slice is done but agreed features remain. | Continue the agreed first version. | Report the scaffold or pilot as completion. |

Use short first-turn or decision exercises to check elicitation and default selection. Treat them as evidence of response behavior only, not a successful implementation.

## Exercise a real starting point when practical

Use an explicitly scoped scratch project or an authorized real project to test the full loop. Keep synthetic data isolated and obey the user's stack and artifact constraints. Do not create or publish an unrelated sample app merely to decorate a skill change.

Choose a modest journey with a real outcome and one meaningful failure, such as creating and reopening an item with persistence, then recovering from an unsuccessful save. Compare actual behavior with what the agent promised. Inspect the rendered result when visual output is part of the task.

Check whether startup commands work, the central task succeeds, the failure is recoverable, the visual foundation stays coherent across representative uses, and the result is easy to locate and run. Observe whether questions improved a consequential decision or merely interrupted reversible work. Inspect any starter shortcut for a clear boundary and honest limitation.

Judge quality and completeness alongside convenience; fewer questions alone is not success. Treat a correct required question as useful progress. Distinguish instruction inspection, simulated decision exercises, local project execution, and deployment proof.

Map observed friction to its owner: decision timing and scope to Omelet; runnable setup and implementation boundaries to implementation-quality; frontend continuity to frontend-system-principles; visual coherence to nyan-ui-visual-review. Refine the responsible owner instead of adding a catch-all startup skill.
