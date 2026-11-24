# Main branch protection proposal

This document proposes GitHub settings. The repository's delivery policy lives
in [AGENTS.md](../AGENTS.md#skill-library-orchestration). Confirm that the
`validate` workflow has reported a successful GitHub run before requiring it.

## Baseline settings

Under **Settings → Rules → Rulesets → New branch ruleset**, create the following
two rulesets with **Enforcement status: Active** and **Target branches: Include
by pattern → `main`** (API condition `refs/heads/main`). Keep all unlisted rules
off. Separate rulesets let a CI exception preserve branch integrity.

| Ruleset | Enabled rules | Bypass list |
| --- | --- | --- |
| Main integrity | **Restrict deletions** and **Block force pushes** | Empty |
| Main validation | **Require status checks to pass** with check `validate`, expected source **GitHub Actions**, and **Require branches to be up to date before merging** enabled | Empty by default |

Select the check reported by the job named `validate` in the
**Skill library checks** workflow. Strict checks make a PR requalify against
current `main` when concurrent changes land. This can require a branch update and
another short CI run.

## Optional PR requirement

Add a third active ruleset, **Main pull requests**, with the same target. Enable
**Require a pull request before merging**, set **Required approvals** to **0**,
and keep the other PR options off. Use an empty bypass list if every update must
come through a PR. To allow an owner exception, add the owner-only actor with
**Always allow**. GitHub offers bypasses by role, team, or app. For a
personal repository, use **Repository admin** only if the owner is its sole
administrator. For an organization, use a team containing only the owner.

## Direct pushes

The workflow runs on pushes to `main` and PRs targeting it. An ordinary new
commit pushed straight to `main` has no prior `validate` result, so the baseline
usually blocks it. A post-push check cannot satisfy the pre-push rule.

If the owner wants to keep direct pushes, add the same owner-only actor with
**Always allow** to **Main validation** and, if enabled, **Main pull requests**.
This also allows that actor to bypass validation on a PR. Main integrity still
blocks force pushes and deletion. A **For pull requests only** bypass requires
opening a PR and cannot permit a direct push. Direct pushes by the owner receive
CI feedback after the branch update.

The owner can choose strict pre-merge validation for every actor. To enforce
the repository policy while retaining its explicit direct-push exception,
use the owner bypass on Main validation and Main pull requests and leave
Main integrity without bypasses.

Sources: [Creating rulesets for a repository](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository)
and [Available rules for rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets).
