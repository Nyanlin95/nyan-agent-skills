# Project start

Detailed guidance for starting a project. The owner rule stays in SKILL.md.

## Make starting a project easy

Turn a rough idea into the first useful outcome. Infer the intended user, problem, central task, and success condition from the conversation and existing material. Keep this brief in working context or the project's existing owner; do not require a questionnaire, PRD, architecture deck, or complete specification before starting.

Resolve questions by consequence rather than by whether a detail is missing:

| Uncertainty | Helpful response |
| --- | --- |
| Reversible implementation detail with no meaningful user consequence | Choose a suitable default from the project or task and proceed. Avoid asking about filenames, component names, initial Git branch names, ordinary tooling commands, or exact initial spacing. |
| Choice that changes who the product serves, its main workflow, data visibility, durable behavior, cost, or a hard-to-reverse constraint | Check existing evidence first; ask a concise decision question if it remains unresolved. Explain the user-visible tradeoff and recommend a direction. |
| Optional preference that can be improved after a first render | Make a reasonable provisional choice or ask asynchronously while continuing independent work. |
| External write, publication, purchase, destructive action, or sensitive-data use | Follow existing authority. Do not treat a convenient default or silence as approval. |

Ask the smallest useful question when its answer will change the next substantial work. Translate technical choices into consequences; ask whether people need shared access across devices before asking them to choose a database. Offer a small set of meaningful alternatives when helpful, without repeating answered questions. Keep required decisions pending and continue only work that does not depend on the answer. Do not hide a consequential assumption inside a default.

Resolve routine technical defaults from the user's existing instruction, then repository conventions and observed configuration, then the tool's normal default. For Git, inspect the existing branch and remote default when relevant; preserve them instead of asking the user to name a default branch. For a new repository, use the configured initial branch or Git's default without an intake question. This does not authorize renaming an established branch, changing a remote default, or publishing. Ask only if a real unresolved consequence remains, not merely because `main` and `master` are both possible names.

Favor an early, coherent working slice over a wide set of disconnected screens. Choose it from the user's goal, then complete the agreed first version rather than stopping after the first successful slice. For a new application, consider `implementation-quality` for runnable foundations, `frontend-system-principles` for interactive journeys, and `nyan-ui-visual-review` for visual foundations and critique. Select only useful guidance; no fixed skill chain, technology stack, or delegation is required.

Make routine setup invisible where practical, while keeping consequential assumptions and actual limitations clear. Bring the user a running result or native artifact early enough to react to real work. Ask for feedback at meaningful product or design decisions rather than after every file or edit. Continue ordinary authorized implementation and verification without another permission round.

Keep the starting point easy to evolve through clear owners, native project conventions, and honest integration boundaries. Avoid speculative platforms and silent demo shortcuts. Distinguish illustrative data, temporary storage, simulated providers, and unverified deployment from working capabilities. Track only material shortcuts beside their owner, with their consequence and the condition that requires replacement.

Report what the user can now do, how to open or run it, the consequential defaults chosen, what was verified, and what still limits use. Describe a preview, a local working project, and a deployed service accurately. Treat observed use as feedback on both the project and this workflow; refine only the skill owner responsible for a repeated problem.
