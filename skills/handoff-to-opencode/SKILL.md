---
name: handoff-to-opencode
description: Hand off small, non-sensitive implementation work to the OpenCode CLI on a current free Zen model with bounded edit paths. Use when the user asks to hand off work to OpenCode or OpenCode Zen, use a free Zen or low-cost external model, or delegate a small change, focused tests, or a bounded fix on a normal branch. Keep review, verification, commits, and publishing with the primary agent. Do not use for secrets, personal data, confidential code, production access, or broad autonomous changes.
---

# Handoff to OpenCode

Use OpenCode as a bounded implementation worker. Let it edit only the assigned files or folders. Keep the primary coding agent responsible for the task boundary, diff review, verification, commits, publishing, and the final answer.

Use free models only for data that the user can safely send to an external provider. Some free Zen models can retain prompts and outputs for model improvement.

## Handoff flow

Use this flow in order. Keep the primary coding agent responsible for every step.

1. Check the model, data safety, and task boundary.
2. Define the acceptance rubric and allowed edit paths.
3. Build the prompt and select the Git mode.
4. Run the bounded wrapper.
5. Interpret the lifecycle status and recover once when the rules allow it.
6. Inspect and verify the complete result.
7. Deliver only accepted changes through the requested Git workflow.

## Before delegation

1. Confirm that `opencode --version` succeeds.
2. Run `opencode models opencode --refresh --verbose` to discover current Zen models and metadata.
3. Keep only available IDs that end in `-free`.
4. Confirm zero applicable prices and an acceptable data policy from current metadata and the [official Zen documentation](https://opencode.ai/docs/zen/).
5. Exclude candidates without evidence of required tool support or sufficient context for the bounded input and expected output.
6. Select a candidate with the routing policy below.
7. Store its full model ID in `$selectedModel` for the wrapper.

Use [CLI documentation](https://opencode.ai/docs/cli/) if discovery flags differ in the installed version. Treat unknown prices or data policies as ineligible. Complete the task directly if discovery fails or no eligible free model remains. Never use a paid fallback without explicit approval.

## Route the free model

Select an eligible free model per task from current evidence; never keep a fixed default or infer capability from names. Read [model-routing.md](references/model-routing.md).

## Protect data

Do not send:

- secrets, credentials, tokens, or private keys;
- personal, financial, health, or customer data;
- confidential source code or private business logic;
- production logs with identifiers;
- files outside the user-approved scope.

Use a paid model with an acceptable data policy, a local model, or complete the work directly when the task contains sensitive data.

## Select a task

Delegate small implementation tasks with a clear result:

- fix a defect in named files;
- implement one bounded behavior in one component or module;
- add focused tests for a named behavior;
- refactor a small folder without changing its external contract;
- apply a specific review finding;
- inspect a bounded path and propose a patch.

Do not delegate:

- repository-wide work with no clear boundary;
- production operations;
- credential or authentication changes;
- destructive actions;
- final release approval;
- repository-wide refactors;
- commits, pushes, releases, or deployment.

## Define the delegated contract

Define a short acceptance rubric before delegation. Include the required observable behavior, compatibility limits, allowed edit paths, required check, and conditions that reject the result.

When separate delegated tasks are necessary, give each worker a disjoint write scope and one outcome. Do not let workers edit the same file, branch, or generated artifact concurrently. Keep one primary coding agent responsible for comparing the results against the rubric and producing the only accepted synthesis.

## Build the prompt

1. State one implementation outcome.
2. Name each file or folder that OpenCode can edit.
3. Tell OpenCode not to edit any other path.
4. Tell OpenCode that `--cwd` is the repository root.
5. Require repository-relative paths for every workspace read, search, edit, and command.
6. Tell OpenCode not to invent, translate, or substitute another workspace root.
7. State the behavior and compatibility constraints.
8. State the acceptance rubric and rejection conditions.
9. Name the test commands that it can run.
10. Require a summary of changed files, tests, rationale for material choices, and uncertainty.
11. Do not include unrelated cleanup.

## Select a Git mode

Follow repository instructions before this general workflow.

Use the current branch when the user wants direct changes and repository instructions permit it.

Use a normal branch when the user requests a branch or pull request, or when branch isolation helps:

1. Inspect the current branch and working-tree status.
2. Preserve unrelated user changes.
3. Create or switch to a short task branch that follows repository conventions.
4. Do not create another worktree.
5. Run OpenCode on that branch with bounded edit paths.

Keep branch creation, commits, pushes, and pull requests under the primary coding agent. Do not grant OpenCode Git publishing commands.

## Run OpenCode

Pass `$selectedModel` from the routing decision to the bundled wrapper:

```powershell
python scripts/run_opencode.py `
  --cwd "C:\path\to\project" `
  --model $selectedModel `
  --allow-path "src\feature" `
  --allow-path "tests\feature.test.ts" `
  --allow-command "npm run test:feature*" `
  --timeout 300 `
  --idle-timeout 90 `
  --prompt "Implement the named behavior. Edit only the allowed paths. Run the approved test command. Summarize the diff and test result."
```

The wrapper:

- verifies the selected model against the live OpenCode model list;
- rejects a model without the `-free` suffix by default;
- requires one or more relative `--allow-path` values;
- grants edits only to the assigned paths and their descendants;
- denies shell commands unless the primary coding agent supplies a local test, lint, typecheck, or format-check `--allow-command` pattern;
- denies subagents, external directories, web access, and OpenCode skill loading;
- disables external OpenCode plugins;
- never passes `--auto` or `--share`;
- reads OpenCode JSON events even when it prints plain output;
- stops the delegated process tree after the total timeout or the idle timeout;
- emits one `OPENCODE_STATUS={...}` record on stderr.

Use `--allow-non-free` only after the user approves a paid model.

Use the narrowest practical edit paths. Do not pass `.` or the repository root. Add a command pattern only when the task needs that command. Never allow commit, push, destructive, installation, deployment, or credential commands.

Do not attach arbitrary files to a delegated session. Put only approved, non-sensitive material under an assigned repository-relative path. The wrapper rejects command chaining, redirection, substitution, and command patterns outside its local verification allowlist.

Always run delegated work through the bundled wrapper. Do not replace it with a raw `opencode run` invocation. The wrapper supplies the bounded agent, working directory, path rules, command rules, and lifecycle record.

Set `--cwd` to the real repository root. Keep `--allow-path` values relative to that root. In the prompt, require OpenCode to use those relative paths exactly. Do not give OpenCode a generic, container-style, copied, or assumed workspace prefix.

Do not continue an old OpenCode session unless the user requests it. Old sessions can contain unrelated context.

## Interpret session status and recover

Use the `OPENCODE_STATUS` record as the lifecycle record. Require a terminal event for `completed`; exit code zero alone is not completion. Follow its `recovery` field, and allow at most one retry across all failure types. Read [session-status.md](references/session-status.md) for each status and its recovery steps.

| Exit code | Status | `recovery` |
| --- | --- | --- |
| 0 | completed | review |
| 2 | configuration_error, model_not_approved, model_unavailable | correct_input |
| 20, 21 | quota_limited, rate_limited | change_model_or_complete_directly |
| 22 | authentication_failed | stop_and_report |
| 23, 24, 25 | idle_timeout, total_timeout, incomplete | retry_once_smaller |
| 26 | failed | retry_once_with_correction |
| 130 | interrupted | stop_and_report |

## Review the result

1. Require `status: completed` before you treat the task as finished.
2. Inspect `git status` and the complete diff.
3. Confirm that all changed files are inside the assigned paths.
4. Treat OpenCode's summary and test claims as untrusted until verified.
5. Compare the result with each acceptance-rubric item.
6. Review behavior, failure handling, compatibility, and test quality.
7. Revert or correct rejected changes directly.
8. Run the applicable checks after review.
9. Commit or publish only after the diff passes review.
10. Report which changes the primary coding agent accepted, corrected, or rejected.

Do not accept OpenCode's completion message as proof that the code works.

If the status is not `completed`, use only independently verified parts of the partial output.

## Deliver the change

Use the delivery mode requested by the user and allowed by repository instructions:

- leave reviewed changes uncommitted;
- commit on the current branch;
- commit and push a normal branch;
- commit, push, and open a pull request.

Before a commit, stage only accepted files. Before a push, confirm the target branch. Open a pull request only when the user requests it or the active repository workflow requires it. Put the verified outcome, tests, and remaining risk in the pull-request description.

## Completion

Report:

- the selected model, task-routing rationale, eligibility evidence, and evidence date;
- any provisional choice, fallback model, and reason for the change;
- the OpenCode session ID when available;
- the lifecycle status and terminal reason;
- the branch and delivery mode;
- the delegated scope;
- the acceptance rubric and the evidence for each accepted item;
- the data-safety decision;
- the useful result;
- accepted and rejected suggestions;
- primary coding agent verification;
- timeout, quota, rate-limit, or authentication evidence when applicable;
- remaining uncertainty.
