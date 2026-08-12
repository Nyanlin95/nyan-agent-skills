# Skill-library orchestration

Use `skills-run:` followed by the outcome you want.

Examples:

```text
skills-run: research repeated delegation failures and improve the owning skill
skills-run: create a skill for a workflow that has no current owner
skills-run: validate and sync the changed repository-owned skills
```

The primary agent uses Sol at medium reasoning to plan, route work, resolve conflicts, and verify completion. It delegates bounded work to these specialists:

- `history_analyst`: read-only agent-history evidence; uses `research`.
- `skill_researcher`: read-only repository and primary-source research; uses `research`.
- `skill_implementer`: default Terra/high writer; uses `skill-creator`, `implementation-quality`, and `simplified-technical-writing`.
- `skill_reviewer`: independent review; uses `cqt-review` and `adversarial-review`.
- `skill_syncer`: validation and requested installed-copy synchronization; uses `local-git-gates`.
- `git_pr_manager`: Terra/high Git and GitHub owner; uses `file-pr`, `babysit-pr`, `local-git-gates`, and `implementation-quality`.

The primary agent remains the integrator and publication decision owner. The Git manager executes authorized branch, commit, ready-PR, babysitting, and merge operations. Use `skills-run:full <task>` to authorize that complete PR workflow. Ordinary `skills-run:` requests do not authorize commits, pushes, pull requests, merges, or other GitHub writes. Direct pushes to `master` are not part of this orchestration.
