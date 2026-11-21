# CI retries, checkpoints and run-once ownership

Use this reference when a gate plan resumes, retries, or reuses partial work across CI attempts, or when a workflow routes jobs to specific self-hosted runners. Derive labels, job names, and runner pools from the target repository's workflows and runner configuration.

## Ownership of checkpoints

1. A checkpoint belongs to the runner and attempt that produced it, not to the workflow run as a whole.
2. Decide checkpoint ownership on each execution attempt by querying the CI provider's job records for the earliest prior assigned job of the same check. Use paginated API reads.
3. Do not infer ownership from the scheduling label. Re-run of failed jobs can keep the original label after the work moved to another runner.
4. Restore a checkpoint only when the current runner is the owner and the checkpoint matches the candidate revision, canonical plan, and namespace.
5. Invalid ownership, evidence, or context fails closed. Do not replay it.

## Retry admission

| Situation | Required behavior |
| --- | --- |
| Original runner assigned and checkpoint valid | Restore the checkpoint, then plan. Record the assignment. |
| Original runner assigned, no checkpoint namespace or earlier attempt | Start fresh. |
| Retry assigned to a different eligible runner | Set an explicit fresh-retry flag. Run the entire canonical affected plan without inheritance. Record both runner identities. |
| Retry with no assigned prior job | Start fresh. |
| Required runner unavailable | Keep the pinned job queued or incomplete. Do not fall back silently to a shared pool when the check requires that machine's state. |

Routing must not sleep, poll, or fail because a reservation exists. Treat a routing decision as advisory: the provider may still assign work differently. Document that a confirmed spare can go offline after routing, and that a pinned job can then wait until the provider's timeout.

## Run-once and feedback boundaries

- Developer hooks produce feedback. CI produces the remote proof. CI must never accept a receipt produced on a developer machine. A promotion receipt counts as remote proof only when CI produced it for its source commit and the digest verifies.
- Repeat cheap static checks in CI, because local hooks can be bypassed.
- Batch related work into one run where the repository's policy asks for it. Stop parallel lanes on the first failure for feature feedback. Collect every result for the full qualification run.
- A run that the repository's stage contract marks feedback-only, or that skips live or expensive proof, writes an unqualified receipt: an explicit `feedback_only` flag and `qualified: false`. Whether a feature-branch run is feedback-only depends on that repository's policy; some keep live intents on feature CI. Reject any skip-live flag for release, promotion, or deployment modes.

## Timeouts

- Size timeouts in nested order: each job timeout must exceed the sum of its step timeouts, with margin for setup and teardown.
- A timed-out check fails qualification. The runner stops the owned process tree, not only the parent process.
- Do not raise a timeout merely to make a run pass. Record the duration and the lane that consumed it.

## Protected branches and remote boundary

- Local pre-push hooks may reject direct updates to protected branches. Treat that as a guard, not as remote protection.
- Remote protection needs separate verification of the platform's rulesets or required checks. If the plan does not permit branch protection, say so; do not claim it.

## Renames, deletions, and manifests

- A renamed or deleted test or owner file selects both its old and new ownership.
- A manifest or runner that still requires a deleted file must fail planning. Do not skip the requirement silently.

## Evidence for retries

- Each attempt writes its own run-specific evidence directory keyed by the run and attempt identity.
- Upload only this attempt's evidence. Mandatory evidence that is missing fails the attempt.
- A retry's green result never repairs an earlier failed attempt's record. Report both attempts.

## Verify before claiming

- Test each rule with a fixture: original-runner restore, reassignment to a different runner, no prior job, invalid checkpoint, and timeout.
- Test the feedback-only flag: a run that skips live proof must write `qualified: false`.
- Confirm the provider's job-assignment behavior on a real run before describing it as enforced. Repository files establish configured behavior only.
