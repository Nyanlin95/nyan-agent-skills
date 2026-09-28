# Omelet orchestration

Use the repository's [AGENTS.md](../AGENTS.md#skill-library-orchestration) for local authority and routes, and [omelet-orchestrator](../skills/omelet-orchestrator/SKILL.md) for the workflow. Keep operating rules in those owners.

Omelet can complete focused tasks directly or select a bounded specialist when that improves the result. Use the model and effort assignments in Omelet's "Guide model selection" and keep the registered role defaults aligned. Use focused checks and proportionate evidence. Request independent review for consequential decisions instead of making every edit pass through a review chain.

The host registry is [config.toml](config.toml). Its role files use `danger-full-access` and describe ownership, relevant skills, and prohibitions. Read-only work below describes the assignment, not a sandbox restriction. Follow the skill's "Delegate bounded work" section for execution permissions. The roles do not create additional workflow gates:

| Role | Owned work |
| --- | --- |
| `skill_researcher` | One bounded skill question, read-only. |
| `history_analyst` | Bounded, sanitized analysis of installed coding-agent history, read-only. |
| `skill_implementer` | Assigned canonical skill paths and catalog entries. |
| `skill_reviewer` | Independent findings for the assigned change, read-only. |
| `skill_syncer` | Validation and explicitly authorized installed-copy synchronization. |
| `git_pr_manager` | Explicitly authorized Git and PR actions under Omelet's contract. |

For OpenCode work, use [handoff-to-opencode](../skills/handoff-to-opencode/SKILL.md). That skill owns live free-model selection by task, eligibility, bounded execution, and recovery. Omelet keeps responsibility for the acceptance decision and Git delivery.

Treat changed orchestration configuration as `policy-only` until a fresh trusted-project session loads it, resolves the registered roles, and returns one bounded read-only delegation result. Record the host and tested revision; CLI proof does not establish activation in an already-running desktop task.

Commit and push directly to `main` when publication is authorized. Create a feature branch or PR only when explicitly requested. Follow AGENTS.md for the full-workflow route and authorized cleanup of merged branches.
