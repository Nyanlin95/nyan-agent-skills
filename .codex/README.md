# Omelet orchestration

Use the repository's [AGENTS.md](../AGENTS.md#skill-library-orchestration) for local authority and routes, and [omelet-orchestrator](../skills/omelet-orchestrator/SKILL.md) for the workflow. Keep operating rules in those owners.

Omelet can complete focused tasks directly or select a bounded specialist when that improves the result. Select models for the task and current host; do not pin models in role contracts. Use focused checks and proportionate evidence. Request independent review for consequential decisions instead of making every edit pass through a review chain.

The host registry is [config.toml](config.toml). Its role files describe ownership, relevant skills, and prohibitions. They do not create additional workflow gates:

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

Use `main` as the base branch and push changes on a feature branch. Publication requires explicit authority; PR creation and merge are separate actions. See AGENTS.md for the full-workflow route.
