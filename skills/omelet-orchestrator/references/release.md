# Release and pull request workflows

Authority and monitoring rules for publication.

## Authorize release workflows

A plain orchestration request never authorizes commits, pushes, pull requests, merges, or other GitHub writes.

A `full` workflow authorizes validation, commit, and publication through the repository's delivery convention. Follow an explicit user or repository rule to push directly to `main`; do not impose a feature branch or PR. Use a PR workflow when explicitly requested or required by the repository. Verify that the published commit is contained by the intended remote branch and report remaining local changes. Delete branches only when cleanup is authorized and fresh ancestry checks prove they are merged into the remote base branch. A `full` workflow does not build, start, stop, or redeploy services and does not run hermetic acceptance.

A `release` workflow authorizes publication through the repository's delivery contract and deployment only when the user authorizes that deployment step. Respect required temporary branches and pull requests; do not interpret the word release as permission to push directly to a permanent branch. Inspect the intended diff, run the required gates and stop on a failed gate, publication, build or health check. Resolve the candidate identity from the repository rather than asking the user to supply a commit SHA.

## Separate development, promotion and deployment

Follow the repository's branch model. When it uses a permanent development branch and a permanent production branch, start each change in a temporary branch from the development line, integrate through its PR path and preserve both permanent branches. Delete a temporary branch only when cleanup is authorized and fresh remote ancestry proves it merged. Do not open another integration PR solely to synchronize equivalent contents.

Assign each check to its decision: focused development feedback, complete release-candidate qualification, merge-equivalence verification or deployment readiness. Run the complete required qualification at the release checkpoint, then reuse it through the canonical runner when merge equivalence is proved. Do not repeat the full suite after every merge or rebuild the same artifact solely for branch bookkeeping. Retain separate builds when production configuration changes their inputs.

When the repository chooses automatic deployment after its qualified promotion PR merges, preserve that trigger. Require complete qualification before merge, then verify the merged PR, actual source/base identities, workflow run attempt and revision, retained evidence and equivalent contents before deployment. Keep fresh operational readiness and recovery checks. Do not add a manual button or a second full main run as a default safeguard. If remote branch protection is unavailable, state that limit and enforce qualification at deployment without fabricating a passing merge check.

Honor a manual deployment boundary independently of merge authority. A merge does not authorize deployment when the repository requires a manual release action. Keep required candidate identity, qualification, configuration, recovery and readiness checks on every deployment. Offer an explicit full recheck when requested by the repository, default it off when the user chooses that behavior, and block deployment if a selected recheck fails or is incomplete. Never turn that optional recheck into an unannounced routine gate.

## Monitor authorized pull requests economically

Before scheduling qualification after a merge, inspect the repository runner's promotion contract. When the merged tree and relevant qualification inputs match the qualified candidate, use its explicit provenance-checked promotion path instead of repeating all checks solely for a new commit SHA. Preserve every required check and run fresh merge-identity, publication-range and clean-checkout checks. Follow [local-git-gates](../../local-git-gates/SKILL.md) for the qualification boundary; do not manually relabel receipts or bypass repository policy. Fall back to fresh qualification when equivalence or complete evidence cannot be proved.

1. Finish scope review, repository gates, commit, push, and ready-PR creation before handing off monitoring. Preserve excluded dirty work; never bypass a clean-snapshot gate.
2. Use Luna xhigh for a bounded read-only watch under "Guide model selection". Give it the repository, PR, exact head SHA, check/review scope, and escalation conditions. Keep fixes, GitHub replies, merge, and cleanup with Omelet.
3. Require one initial snapshot, then back off polling and report only changes. Escalate failed checks, actionable feedback, changed heads, or unavailable access promptly; do not let quiet polling conceal a stalled monitor. Avoid duplicate polling by the primary.
4. Return current-head checks, review threads, review decision, and limitations. Distinguish no submitted review from approval. A successful watch proves this bounded task, not general repair ability or measured cost savings.
5. Before an authorized merge, let Omelet refresh head identity and mergeability. After merge, prove remote-base containment, synchronize the local base, and delete only branches proven merged when cleanup is authorized. Restore preserved local work and report remaining changes.
