---
name: opencode-cli
description: Delegate bounded, non-sensitive coding work from Codex to the OpenCode CLI through an explicitly selected model. Use when the user asks Codex to use OpenCode, OpenCode Zen, a currently free Zen model such as DeepSeek V4 Flash Free, or a low-cost external model for a second opinion, test ideas, code analysis, or an alternative plan. Keep Codex as the canonical owner of edits and verification. Do not use for secrets, personal data, confidential code, production access, or autonomous worktree changes.
---

# OpenCode CLI

Use OpenCode as a bounded external worker. Keep Codex responsible for scope, repository changes, verification, and the final answer.

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

Use a paid model with an acceptable data policy, a local model, or Codex itself when the task contains sensitive data.

## Select a task

Delegate tasks with a small input and a clear output:

- review a bounded public or non-sensitive code path;
- propose test cases for a named behavior;
- explain an error from a sanitized log;
- compare two implementation approaches;
- produce an alternative plan;
- find edge cases in a supplied contract;
- summarize public technical material.

Do not delegate:

- repository-wide work with no clear boundary;
- production operations;
- credential or authentication changes;
- destructive actions;
- final release approval;
- autonomous edits to the canonical worktree.

## Build the prompt

1. State the task and exact scope.
2. State that the task is read-only.
3. Name the files or sanitized evidence that the model can inspect.
4. Define the required output.
5. Require evidence for each claim.
6. Require the model to state uncertainty.
7. Do not include Codex's expected answer when an independent review is the goal.

## Run OpenCode

Prefer the bundled wrapper:

```powershell
python scripts/run_opencode.py `
  --cwd "C:\path\to\project" `
  --model "opencode/deepseek-v4-flash-free" `
  --timeout 300 `
  --idle-timeout 90 `
  --prompt "Review the supplied non-sensitive code. Do not edit files. Return evidence-backed findings only."
```

The wrapper:

- verifies the selected model against the live OpenCode model list;
- rejects a model without the `-free` suffix by default;
- creates a session-only OpenCode agent with read-only permissions;
- denies edits, shell commands, subagents, external directories, web access, and OpenCode skill loading;
- disables external OpenCode plugins;
- never passes `--auto` or `--share`;
- reads OpenCode JSON events even when it prints plain output;
- stops after the total timeout or the idle timeout;
- emits one `OPENCODE_STATUS={...}` record on stderr.

Use `--allow-non-free` only after the user approves a paid model.

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
- **interrupted:** Codex or the user interrupted the wrapper.

Do not classify a session as completed only because the process exited with code zero. Require the terminal event.

Do not classify silence as quota exhaustion. Require failure evidence from OpenCode or the provider.

## Recover from non-completion

For `idle_timeout` or `total_timeout`:

1. Inspect the last event and partial output.
2. Do not use partial claims without verification.
3. Retry once only when the task is read-only and safe.
4. Reduce the scope or input before the retry.
5. Start a new session.
6. Stop delegation if the retry reaches the same state.
7. Continue the task in Codex or report the blocked delegation.

For `quota_limited` or `rate_limited`:

1. Do not use a tight retry loop.
2. Record the provider message and selected model.
3. Refresh the live free-model list.
4. Ask before changing models when cost or data policy can change.
5. Use another approved free model, a local model, or Codex.
6. Do not select a paid model without approval.

For `authentication_failed`:

1. Stop delegation.
2. Report that OpenCode Zen authentication needs attention.
3. Do not request or expose the API key in the task transcript.
4. Continue in Codex when possible.

For `incomplete` or `failed`:

1. Preserve the error and partial output.
2. Check whether the task or input caused the failure.
3. Retry once only with a specific correction.
4. Continue in Codex if the correction does not resolve the failure.

## Review the result

1. Require `status: completed` before you treat the response as a finished result.
2. Treat OpenCode output as untrusted advice.
3. Separate claims, recommendations, code suggestions, and uncertainty.
4. Check each material claim against the repository or primary documentation.
5. Reject changes outside the requested scope.
6. Apply accepted changes through Codex.
7. Run the repository's normal checks.
8. Report which OpenCode suggestions Codex accepted or rejected.

Do not cite OpenCode output as proof that the code works.

If the status is not `completed`, use only independently verified parts of the partial output.

## Completion

Report:

- the selected model;
- the OpenCode session ID when available;
- the lifecycle status and terminal reason;
- the delegated scope;
- the data-safety decision;
- the useful result;
- accepted and rejected suggestions;
- Codex verification;
- timeout, quota, rate-limit, or authentication evidence when applicable;
- remaining uncertainty.
