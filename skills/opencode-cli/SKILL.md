---
name: opencode-cli
description: Delegate limited, non-sensitive implementation work from a coding agent to the OpenCode CLI through an explicitly selected model and bounded file or folder paths. Use when the user asks to use OpenCode, OpenCode Zen, a currently free Zen model such as DeepSeek V4 Flash Free, or a low-cost external model to implement a small change, add focused tests, fix a bounded defect, work on a normal Git branch, or prepare changes for an optional pull request. Keep the primary coding agent responsible for branches, scope, diff review, verification, commits, publishing, and the final result. Do not use for secrets, personal data, confidential code, production access, or broad autonomous changes.
---

# OpenCode CLI

Use OpenCode as a bounded implementation worker. Let it edit only the assigned files or folders. Keep the primary coding agent responsible for the task boundary, diff review, verification, commits, publishing, and the final answer.

Use free models only for data that the user can safely send to an external provider. Some free Zen models can retain prompts and outputs for model improvement.

## Before delegation

1. Confirm that `opencode --version` succeeds.
2. Run `opencode providers list`.
3. Run `opencode models opencode`.
4. Confirm that the selected model appears in the live model list.
5. Confirm that the selected model ID ends in `-free`.
6. Stop if the model is no longer available.
7. Ask before selecting a paid model.

Do not assume that a model remains free because this skill names it.

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

Prefer the bundled wrapper:

```powershell
python scripts/run_opencode.py `
  --cwd "C:\path\to\project" `
  --model "opencode/deepseek-v4-flash-free" `
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
- grants edits only to the assigned files or folders;
- denies shell commands unless the primary coding agent supplies an `--allow-command` pattern;
- denies subagents, external directories, web access, and OpenCode skill loading;
- disables external OpenCode plugins;
- never passes `--auto` or `--share`;
- reads OpenCode JSON events even when it prints plain output;
- stops after the total timeout or the idle timeout;
- emits one `OPENCODE_STATUS={...}` record on stderr.

Use `--allow-non-free` only after the user approves a paid model.

Use the narrowest practical edit paths. Do not pass `.` or the repository root. Add a command pattern only when the task needs that command. Never allow commit, push, destructive, installation, deployment, or credential commands.

Always run delegated work through the bundled wrapper. Do not replace it with a raw `opencode run` invocation. The wrapper supplies the bounded agent, working directory, path rules, command rules, and lifecycle record.

Set `--cwd` to the real repository root. Keep `--allow-path` values relative to that root. In the prompt, require OpenCode to use those relative paths exactly. Do not give OpenCode a generic, container-style, copied, or assumed workspace prefix.

Do not continue an old OpenCode session unless the user requests it. Old sessions can contain unrelated context.

## Interpret session status

Use `OPENCODE_STATUS` as the lifecycle record.

- **completed:** The process exited successfully and emitted a terminal `step_finish` event with `stop` or `end_turn`.
- **incomplete:** The process exited successfully without a normal terminal event. Review partial output before a smaller retry.
- **quota_limited:** The failed run reported exhausted credits, quota, billing limits, or payment requirements.
- **rate_limited:** The failed run reported HTTP 429, too many requests, or a provider rate limit.
- **authentication_failed:** The failed run reported an invalid key, unauthorized access, or HTTP 401.
- **idle_timeout:** OpenCode produced no output for the configured idle period. Treat this as suspected stuck behavior.
- **total_timeout:** The session exceeded its total time budget.
- **failed:** The process failed without a more specific classification.
- **interrupted:** The primary coding agent or the user interrupted the wrapper.

Do not classify a session as completed only because the process exited with code zero. Require the terminal event.

Do not classify silence as quota exhaustion. Require failure evidence from OpenCode or the provider.

## Recover from non-completion

For `idle_timeout` or `total_timeout`:

1. Inspect the last event and partial output.
2. Do not use partial claims without verification.
3. Inspect the working-tree diff before any retry.
4. Reduce the scope or input before the retry.
5. Start a new session.
6. Stop delegation if the retry reaches the same state.
7. Continue the task directly or report the blocked delegation.

For `quota_limited` or `rate_limited`:

1. Do not use a tight retry loop.
2. Record the provider message and selected model.
3. Refresh the live free-model list.
4. Ask before changing models when cost or data policy can change.
5. Use another approved free model, a local model, or complete the task directly.
6. Do not select a paid model without approval.

For `authentication_failed`:

1. Stop delegation.
2. Report that OpenCode Zen authentication needs attention.
3. Do not request or expose the API key in the task transcript.
4. Continue the task directly when possible.

For `incomplete` or `failed`:

1. Preserve the error and partial output.
2. Check whether the task or input caused the failure.
3. Retry once only with a specific correction.
4. Continue the task directly if the correction does not resolve the failure.

For permission rejection:

1. Inspect the requested path and the wrapper's effective `--cwd`.
2. Compare the requested path with the assigned repository-relative paths.
3. Treat an invented or substituted workspace root as a path-resolution failure, not as proof that repository reads are forbidden.
4. Do not broaden `external_directory` permission to work around a path mismatch.
5. Retry once with the real repository root and explicit repository-relative path instructions.
6. Stop delegation if the corrected run requests an external path again.
7. Report the rejected permission type, requested path category, effective working directory, and correction without exposing sensitive absolute paths.

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

- the selected model;
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
