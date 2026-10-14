# Session status and recovery

Meaning of each `OPENCODE_STATUS` value and the recovery rule for each. The wrapper emits the matching `recovery` action and a distinct exit code.

## Interpret session status

Use `OPENCODE_STATUS` as the lifecycle record.

- **completed:** The process exited successfully and emitted a terminal `step_finish` event with `stop` or `end_turn`.
- **incomplete:** The process exited successfully without a normal terminal event. Review partial output before a smaller retry.
- **quota_limited:** The failed run reported exhausted credits, quota, billing limits, or payment requirements.
- **rate_limited:** The failed run reported HTTP 429, too many requests, or a provider rate limit.
- **authentication_failed:** The failed run reported an invalid key, unauthorized access, or HTTP 401.
- **configuration_error:** The wrapper rejected the working directory, allowed path, command pattern, timeout, or local OpenCode setup before delegation started.
- **model_not_approved:** The selected model is not free and the user did not approve paid-model use.
- **model_unavailable:** The selected model is absent from the current provider model list.
- **idle_timeout:** OpenCode produced no output for the configured idle period. Treat this as suspected stuck behavior.
- **total_timeout:** The session exceeded its total time budget.
- **failed:** The process failed without a more specific classification.
- **interrupted:** The primary coding agent or the user interrupted the wrapper.

Do not classify a session as completed only because the process exited with code zero. Require the terminal event.

Do not classify silence as quota exhaustion. Require failure evidence from OpenCode or the provider.

## Recover from non-completion

Allow at most one retry across all failure types for the delegated task. Inspect the partial output and working-tree diff before that retry. Preserve the allowed paths, commands, and data boundary. Stop delegation after another non-completion, even if the failure type changes.

Before a model change, refresh discovery and reapply eligibility and task routing. Use another free candidate only within existing authority and an acceptable data policy. Record the failed model, failure evidence, replacement, and reason. Complete the task directly when no eligible replacement remains. Do not broaden permissions or silently select a paid model.

For `idle_timeout` or `total_timeout`:

1. Inspect the last event and partial output.
2. Do not use partial claims without verification.
3. Inspect the working-tree diff before any retry.
4. Reduce the scope or input before the retry.
5. Start a new session.
6. Stop delegation if the retry does not complete.
7. Continue the task directly or report the blocked delegation.

For `quota_limited` or `rate_limited`:

1. Do not use a tight retry loop.
2. Record the provider message and selected model.
3. Apply the shared model-change rules for the remaining retry.
4. Complete the task directly if no retry remains.

For `authentication_failed`:

1. Stop delegation.
2. Report that OpenCode Zen authentication needs attention.
3. Do not request or expose the API key in the task transcript.
4. Continue the task directly when possible.

For `configuration_error`, `model_not_approved`, or `model_unavailable`:

1. Report the wrapper reason without exposing sensitive paths or configuration.
2. Correct the bounded input or select another approved live free model.
3. Start a new session only after the correction.
4. Continue the task directly when no safe delegated session is available.

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
