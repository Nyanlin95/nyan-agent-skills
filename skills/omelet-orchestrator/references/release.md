# Release and pull request workflows

Authority and monitoring rules for publication.

## Authorize release workflows

A plain orchestration request never authorizes commits, pushes, pull requests, merges, or other GitHub writes.

A `full` workflow authorizes validation, commit, and publication through the repository's delivery convention. Follow an explicit user or repository rule to push directly to `main`; do not impose a feature branch or PR. Use a PR workflow when explicitly requested or required by the repository. Verify that the published commit is contained by the intended remote branch and report remaining local changes. Delete branches only when cleanup is authorized and fresh ancestry checks prove they are merged into the remote base branch. A `full` workflow does not build, start, stop, or redeploy services and does not run hermetic acceptance.

A `release` workflow authorizes the commit, direct push to the base branch, and redeploy. Inspect the intended diff, run the repository gates, commit with a plain title, and push without force. Stop on a failed gate, push, build, or health check. The user does not need to provide a commit SHA.

## Monitor authorized pull requests economically

1. Finish scope review, repository gates, commit, push, and ready-PR creation before handing off monitoring. Preserve excluded dirty work; never bypass a clean-snapshot gate.
2. Use Luna xhigh for a bounded read-only watch under "Guide model selection". Give it the repository, PR, exact head SHA, check/review scope, and escalation conditions. Keep fixes, GitHub replies, merge, and cleanup with Omelet.
3. Require one initial snapshot, then back off polling and report only changes. Escalate failed checks, actionable feedback, changed heads, or unavailable access promptly; do not let quiet polling conceal a stalled monitor. Avoid duplicate polling by the primary.
4. Return current-head checks, review threads, review decision, and limitations. Distinguish no submitted review from approval. A successful watch proves this bounded task, not general repair ability or measured cost savings.
5. Before an authorized merge, let Omelet refresh head identity and mergeability. After merge, prove remote-base containment, synchronize the local base, and delete only branches proven merged when cleanup is authorized. Restore preserved local work and report remaining changes.
