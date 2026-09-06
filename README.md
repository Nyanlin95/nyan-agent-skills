# Nyan Agent Skills

Nyan Agent Skills is a library of independent skills for coding agents. Each
skill has one clear job and lives under `skills/`.

The library covers project starts, implementation, frontend behavior, visual
foundations, code and design review, Git gates, prototypes, technical writing,
bounded OpenCode handoffs, and a scoped Wonder design workflow.

The project uses the [MIT License](LICENSE).

## Use a skill

Give the agent the outcome, scope, limits, and relevant evidence. The agent can
select a matching skill from the request. You can also select one directly.

```text
Use $nyan-ui-visual-review to review this dashboard at desktop and mobile widths.
```

For a useful result:

1. State the required outcome.
2. Name the files, routes, or systems in scope.
3. State the behavior that must not change.
4. Provide the relevant code, diff, plan, logs, or rendered evidence.
5. Review the evidence before you authorize a broad change or publication.

## Skills

| Skill | Purpose |
| :--- | :--- |
| [cqt-review](skills/cqt-review/) | Review code and migrations for quality, ownership, dependencies, state, and failure behavior. |
| [adversarial-review](skills/adversarial-review/) | Test material claims in plans, changes, and reviews before a decision. |
| [implementation-quality](skills/implementation-quality/) | Start runnable projects and implement or refactor code with clear ownership, complete journeys, and explicit failures. |
| [frontend-system-principles](skills/frontend-system-principles/) | Build coherent frontend journeys with clear state ownership, consistent caching, navigation continuity, and supported recovery. |
| [omelet-orchestrator](skills/omelet-orchestrator/) | Turn requests into working outcomes with consequential questions, routine defaults, grounded scope, and flexible design and implementation guidance. |
| [local-git-gates](skills/local-git-gates/) | Add or review repository-local Git checks that reuse existing verification commands. |
| [nyan-ui-visual-review](skills/nyan-ui-visual-review/) | Distill or scaffold coherent visual foundations and critique icons through pages, presentations, books, graphics, and motion using spatial principles and rendered geometry. |
| [ui-copy-review](skills/ui-copy-review/) | Review changed interface copy for clarity, recovery, consistency, and copy-related accessibility. |
| [build-html-prototype](skills/build-html-prototype/) | Build document, interface, or visual HTML prototypes inside one disposable folder. |
| [handoff-to-opencode](skills/handoff-to-opencode/) | Route limited, non-sensitive implementation work to a current free OpenCode model based on task needs within explicit paths. |
| [simplified-technical-writing](skills/simplified-technical-writing/) | Rewrite technical prose in strict or STE-flavored Simplified Technical English. |
| [wonder-design-workflow](skills/wonder-design-workflow/) | Create, change, verify, and save scoped Wonder designs with clear proof boundaries. |

## Common requests

### Start a project

```text
Use $omelet-orchestrator to build a personal reading tracker. Local-only is fine.
Make routine choices for me and ask when a decision materially changes the product.
Deliver a working first version with a clear visual system and verify saving,
reopening, and recovering from a failed save.
```

Start with the outcome; a complete specification is unnecessary. Omelet can use
implementation, frontend, and visual guidance as needed without a fixed sequence.
For shared or externally connected products, settle consequential access, data,
and service choices before implementing the dependent behavior.

Routine setup follows existing project and tool defaults, including the initial
Git branch name. The agent asks about user consequences, not every technical preference.

### Review code or architecture

```text
Use $cqt-review to review this migration for ownership and failure behavior.
```

### Challenge a decision

```text
Use $adversarial-review to test this implementation plan before we approve it.
```

### Implement a focused change

```text
Use $implementation-quality to move this behavior to the correct owner.
```

### Orchestrate skill work

```text
Use $omelet-orchestrator to coordinate this repository change.
```

Omelet can complete focused work directly or delegate a bounded task when useful. It prefers Astra when the host supports it and selects specialist models for the task. Use focused checks and add independent review for consequential decisions. See [repository orchestration](.codex/README.md) for roles, routes, and activation proof.

### Add a local Git gate

```text
Use $local-git-gates to add a path-aware pre-push check.
```

### Review a rendered interface

```text
Use $nyan-ui-visual-review to review this existing workflow and its responsive states.
```

Provide a screenshot, live route, component preview, recording, or visual-regression
image. Include non-default states when they can change the result.

### Review changed UI copy

```text
Use $ui-copy-review to review the interface copy changed on this branch.
```

The review compares added and removed language, follows it to affected interface
states, and checks accessible names, instructions, errors, status, and recovery.

### Build a contained HTML prototype

```text
Use $build-html-prototype to turn this workflow idea into an interactive browser prototype.
```

The skill can produce document-style artifacts, UI experiments, or richer
Canvas and Three.js studies. It keeps the complete output in one removable folder.

### Hand off bounded work

```text
Use $handoff-to-opencode to select a current free model and implement this task only in src/feature/.
```

Select from the live free-model list using task needs, tool reliability, context limits, and available performance evidence. Keep selection provisional when comparative evidence is unavailable. Do not include credentials, confidential code, or paths outside the approved scope. Omelet retains acceptance and Git delivery decisions.

### Rewrite technical prose

```text
Use $simplified-technical-writing to rewrite this runbook in strict mode.
```

### Work in Wonder

```text
Use $wonder-design-workflow to update this Wonder design and verify each requested state.
```

## Combine skills

Combine skills only when their distinct jobs help the task. Use `implementation-quality` for implementation and `cqt-review` when independent review can change a consequential decision. Add `adversarial-review` only for an unresolved decision-critical claim; do not make these skills a mandatory chain.

Do not let a review skill silently become the implementation owner.

## Repository rules

- Keep each skill independent.
- Keep one canonical owner for each rule.
- Put the core workflow in `SKILL.md`.
- Put detailed checks in direct files under `references/`.
- Put deterministic helpers under `scripts/`.
- Keep optional interface metadata in `agents/openai.yaml`.
- Verify rendered behavior with rendered evidence.
- Preserve repository and product conventions.
- Do not commit generated research unless the repository explicitly includes it.

Git stores text files with LF line endings. `.gitattributes` normalizes text during
staging. `.editorconfig` configures compatible editors to save LF before staging.

## Add or update a skill

The repository folder `skills/<skill-name>/` is the canonical source for each library skill. Global skill roots are installation or synchronization destinations only; do not treat an installed copy as the source to edit.

1. Read `AGENTS.md`.
2. Create or edit `skills/<skill-name>/`.
3. Keep the folder name equal to the frontmatter `name`.
4. Add or update `agents/openai.yaml`.
5. Put detailed material in `references/`, `scripts/`, or `assets/`.
6. Keep every `SKILL.md` reference direct and one level deep.
7. Update the skill catalog in this README.
8. Validate after the last material edit.
9. Run `git diff --check`.

Run the validator from the repository root:

```powershell
$env:PYTHONUTF8 = '1'
py -3.14 "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "skills\<skill-name>"
```

Before finishing, confirm that `agents/openai.yaml` matches the final skill, that this catalog has one current entry, and that the validation command ran after the final material edit.
