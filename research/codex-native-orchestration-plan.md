# Codex-native orchestration plan for Wer Ywet Studio

> **Research note — non-authoritative.** This document records an external proposal for Wer Ywet Studio at the dated snapshot below. It does not define rules or configuration for Nyan Agent Skills. Use this repository's `AGENTS.md` and `.codex/config.toml` as its authority. Before applying any Studio guidance, verify it against Studio's current code and repository instructions.

Research date: 2026-08-12

Upstream comparison snapshot: `alvinunreal/oh-my-opencode-slim@282d5f26a4ad2665118a73014fcf02e57869bd38`

## Decision

Codex can implement the useful core of `oh-my-opencode-slim` without installing the OpenCode plugin. For `<target-repository-root>`, use Codex's native subagent workflow with artifact-owned specialists. Keep the primary thread as the only planner, delegation owner, conflict resolver, final verifier, and publication owner. The primary thread guides and reconciles; it does not implement product changes.

Studio's release slices normally cross a migration, Rust repository, service, route, authorization, tests, acceptance, and release evidence. Use one default implementation owner for the full bounded product-code invariant, plus specialists for artifacts that have separate ownership:

- `codebase-explorer`: trace route -> service -> repository -> migration -> tests.
- `roadmap-verifier`: compare local `HEAD` with one canonical release packet and exit condition.
- `default-implementer`: implement the primary thread's bounded product-code contract.
- `test-engineer`: extend the existing test owner with success and highest-risk failure coverage.
- `product-manager`: write bounded product and UX documentation.
- `design-engineer`: implement bounded rendered UI, component, token, motion, and performance work.

Use `security-isolation-reviewer` for independent tenancy, authorization, RunPermit, secret, retry, and deletion scrutiny. Use `dependency-researcher` only for an approved dependency, specification, or ADR question. Do not assign overlapping paths or invariants to concurrent writers.

This architecture provides most of the practical quality and context-isolation benefit while keeping Codex itself responsible for spawning, steering, waiting, interrupting, and synthesizing agent work. Current Codex releases enable subagent workflows by default. Local Codex clients support personal agents in `~/.codex/agents/` and project agents in `.codex/agents/`. Each agent can define its model, reasoning effort, sandbox, MCP servers, and instructions. Name applicable skills in those instructions so runtime skill discovery can load them. Use `[[skills.config]]` only for path-based enablement overrides. [OpenAI: Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)

## Wer Ywet Studio binding

This section records the proposed Studio-specific binding at the research snapshot. Studio's current code and repository instructions override it.

### Repository snapshot

The research snapshot is local `master` at `1bfea474` on 2026-08-12. The worktree is clean and two local commits are ahead of `origin/master` at `f0fa0d35`. Treat local `HEAD` as the inspected source of truth. Preserve both unpublished commits. Do not reset, publish, or describe `origin/master` as current without a fresh check and explicit user authority.

Studio is cloud-only. The product is `apps/platform`: Rust/Axum, MySQL, object storage, RunPermit workers, Clerk authentication, and the React browser UI under `apps/platform/web`. Do not introduce desktop, Tauri, `shared`, or `packages` contracts.

### Authority order

Use this order before planning or delegating:

1. Live Rust and React code, migrations, route registry, tests, and runtime behavior.
2. Root `AGENTS.md`, then `docs/AGENTS.md` for documentation work.
3. `CONTEXT.md` for domain language and fixed boundaries.
4. `docs/architecture/mvp-rust-mysql-horizontal-expansion-plan.md` for release order, packet scope, owner, and exit condition.
5. `docs/architecture/react-cloud-frontend-plan.md` for browser routes, presentation ownership, and rendered behavior.
6. `docs/architecture/final-rust-mysql-multitenant-ai-platform-architecture.md` for target architecture.
7. `apps/platform/README.md` for the current API/runtime summary.
8. `docs/ops/platform-production-acceptance.md` and `apps/platform/evals/release-decision.md` for runtime and release evidence.

The fixed domain chain is Clerk identity -> Account (identity/profile only) -> WorkspaceMembership (role) -> Workspace (tenant) -> Project -> immutable Project Type. Rust owns authorization, workflows, durable state, provider access, and failure behavior. React owns presentation, local UI state, accessibility, and thin same-origin requests.

### Current roadmap binding

The local canonical plan records `v0.37.0` AnyDoc binary import and `v1.2.0` lineage/receipts as released. The next executable slice is `v1.3.0` Workspace libraries and explicit mounts. The current next migration number is `0026`.

One task may implement one release slice only. `v1.4.0` export/deletion follows `v1.3.0`; `v1.5.0` ownership transfer/Account deletion follows `v1.4.0`; `v1.6.0` semantic retrieval remains blocked on a product decision; `v1.7.0` remains ordered after it. Subagents must not bypass these gates or treat implementation ahead of the release train as a release exit.

### Existing Codex owner

Studio already tracks `.codex/hooks.json`, `.codex/hooks/*.cjs`, and `.codex/README.md`. The hooks mark validation after `apply_patch` and run scoped validation on Stop. Add orchestration beside this system; do not replace it or create another validation runner.

Studio's `.gitignore` currently ignores `.codex/*` except the hook files and README. An implementation packet must add narrow allow-list entries for `.codex/config.toml` and `.codex/agents/**`; otherwise new agent definitions remain local and invisible to Git.

### Studio specialist set

Studio calls its primary Codex thread Omelet. Omelet is a workflow identity, not
a configured agent. Run Omelet on `gpt-5.6-sol` with
`model_reasoning_effort = "medium"`. Omelet owns intent, task-graph design,
release-slice selection, delegation, disagreement resolution, final
verification, and publication. Do not use a separate permanent planner agent.
Do not use Omelet as the normal product-code writer.

| Role | Model | Effort | Default | Job | Must return |
| --- | --- | --- | --- | --- | --- |
| `codebase-explorer` | `gpt-5.6-luna` | `low` | Read-only | Trace one behavior through route, service, repository, migration, tests, and UI consumer where applicable. | Exact paths, symbols, canonical owner, call chain, and gaps. |
| `roadmap-verifier` | `gpt-5.6-luna` | `medium` | Read-only | Compare one requested slice against the live implementation, predecessor exit, and canonical packet. | Implemented, missing, conflicting, blocked, and required evidence. |
| `test-engineer` | `gpt-5.6-luna` | `medium` | Workspace write | Extend explicitly assigned existing test files and fixtures. | Changed tests, cases, commands, results, and runtime gaps. |
| `security-isolation-reviewer` | `gpt-5.6-terra` | `high` | Read-only | Challenge Workspace/Project scope, membership authorization, RunPermit, idempotency, retries, deletion, redaction, and secret boundaries. | Severity-ordered evidence-backed findings and untested claims. |
| `cqt-reviewer` | `gpt-5.6-terra` | `high` | Read-only | Review material ownership, state, dependency, failure, and migration changes. | Severity-ordered findings, non-findings, and decision-critical claims. |
| `adversarial-reviewer` | `gpt-5.6-terra` | `high` | Read-only | Falsify decision-critical CQT claims and non-findings. | Counterexamples, untested claims, verdict, and unavailable coverage. |
| `product-manager` | `gpt-5.6-terra` | `high` | Workspace write | Own bounded product and UX docs for goals, journeys, hierarchy, language, roles, states, recovery, and acceptance criteria. | Changed docs, evidence, decisions, and unresolved product questions. |
| `design-engineer` | `gpt-5.6-terra` | `high` | Workspace write | Inspect and implement bounded React, shared-component, token, style, responsive, motion, feedback, and UI-performance work. | Changed UI paths, render evidence, checks, and unavailable coverage. |
| `dependency-researcher` | `gpt-5.6-luna` | `medium` | Read-only | Verify an approved dependency/API/specification against primary sources. | Version-pinned facts, risks, licenses/maintenance evidence, and links. |
| `default-implementer` | `gpt-5.6-terra` | `high` | Workspace write | Implement the primary orchestrator's bounded general product-code contract as the single owner of that invariant. | Changed paths, focused tests, failures, and remaining uncertainty. |
| `git_pr_manager` | `gpt-5.6-terra` | `high` | Workspace write plus authorized GitHub operations | Commit an intentional feature branch, file a ready PR, babysit CI/review, and merge when explicitly authorized and green. | Branch, commit, PR URL, checks, review disposition, merge result, and remote proof. |

Name applicable skills explicitly in each agent's instructions so runtime discovery loads the owning procedures instead of relying on role prose alone:

| Role | Assigned skills |
| --- | --- |
| `codebase-explorer` | `domain-modeling` |
| `roadmap-verifier` | `cqt-review` |
| `default-implementer` | `implementation-quality` |
| `test-engineer` | `implementation-quality`, `local-git-gates` |
| `security-isolation-reviewer` | `adversarial-review` |
| `cqt-reviewer` | `cqt-review` |
| `adversarial-reviewer` | `adversarial-review` |
| `product-manager` | `domain-modeling`, `ui-copy-review`, `simplified-technical-writing` |
| `design-engineer` | `nyan-ui-visual-review`, `emil-design-eng`, `apple-design`, `implementation-quality` |
| `dependency-researcher` | `research` |
| `git_pr_manager` | `file-pr`, `babysit-pr`, `local-git-gates`, `implementation-quality` |

Each specialist must read every named skill before acting. Keep the set minimal: role instructions define identity and scope; skills own reusable procedures. Add a skill only when it directly applies to that role's normal work.

These assignments optimize for token cost: Sol Medium is reserved for orchestration and planning, Luna owns bounded exploration and test work, and Terra High owns implementation, product management, design engineering, and security judgment. Escalate one failed or materially disputed lane to `gpt-5.6-sol` at `high` only when the result can change a security-sensitive, destructive, expensive, or hard-to-reverse decision. Do not rerun every lane on a stronger model.

Keep subagent prompts lean. Give each agent only the exact slice, paths, constraints, output contract, and stop condition it needs. Ask for concise evidence rather than raw logs. The primary thread receives summaries and opens detailed agent output only when a claim needs inspection. Official OpenAI guidance identifies Terra as the balance of intelligence and cost, Luna as the cost-sensitive high-volume option, and recommends validating lower reasoning effort on representative tasks. [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model)

Do not create a generic `designer`, `fixer`, or permanent Council role. Keep `product-manager` and `design-engineer` separate: one owns product/UX documentation and the other owns rendered UI implementation. Use independent read-only reviewers with distinct lenses for a high-cost decision, then synthesize in the primary thread.

### Root-only responsibilities

The primary thread must retain:

- release-slice selection and predecessor confirmation;
- dirty/ahead/divergence checks and preservation of user changes;
- migration numbering and the decision boundary for schema/repository/route integration;
- one complete serial contract for changes that cross membership, policy, run,
  usage, conversion, or deletion invariants;
- Docker acceptance, real-Clerk proof, ports, process ownership, generated evidence, and local infrastructure lifecycle;
- dependency and lockfile changes;
- roadmap, release matrix, acceptance evidence, and release-decision updates;
- final full-diff inspection and authoritative gates;
- publication scope and merge authority. Delegate branch, commit, PR,
  monitoring, and merge mechanics to `git_pr_manager`; keep Docker and Clerk
  lifecycle in the primary thread.

Never give secrets to a subagent. Real-Clerk proof needs local secret-bearing configuration and must stay in the primary thread. Do not run concurrent agents against machine-global Docker or Clerk state.

### Studio orchestration sequence

```text
primary: preflight and select exactly one release slice
    |
    +-- codebase-explorer -------- live owner and call-path evidence
    +-- roadmap-verifier --------- packet and predecessor parity
    `-- test-engineer ------------ existing test owner and gate map
              (parallel, read-only)
    |
primary: reconcile conflicts and define one implementation contract
    |
    +-- default-implementer ------- general product-code invariant
    +-- product-manager ---------- bounded product/UX docs
    +-- design-engineer ---------- bounded rendered UI work
    `-- test-engineer ------------ bounded test files and fixtures
              (write contracts must not overlap)
    |
    `-- security-isolation-reviewer (independent review when risk applies)
              (parallel, read-only)
    |
primary: integrate -> focused test -> scoped gate -> affected full gate
         -> stateful runtime proof -> docs/evidence update -> diff check
```

### Preflight contract

Before any delegated work:

1. Read root `AGENTS.md` and every applicable nested instruction file.
2. Run `git status --porcelain=v2 --branch`; record dirty paths, upstream, and ahead/behind state.
3. Read the canonical roadmap status and the exact implementation packet.
4. Confirm the preceding release exit condition from current evidence.
5. Inspect live code, migrations, routes, current tests, and recent local commits.
6. Name the canonical owner and one existing test file to extend.
7. Read `.codex/hooks.json` and preserve the scoped-validation lifecycle.
8. Split only independent read lanes. Keep shared writes serial.

### Gate mapping

Use repository-owned commands only:

| Changed surface | Required route |
| --- | --- |
| Any scoped change | `npm run gate:local -- --paths <changed paths>` and `git -c core.whitespace=cr-at-eol diff --check` |
| Local-gate owner | `npm run test:local-git-gate` |
| Rust/API/migration | `npm run test:platform` |
| API contract | `npm run test:platform-contract-smoke` |
| Stateful platform boundary | `npm run prove:platform-acceptance` or `npm run test:platform-cloud` |
| React | `npm run test:web` and `npm run typecheck:web` |
| Web production artifact | `npm run build:web`, then `npm run verify:web-performance` with a safe publishable test key |
| Release-eval owner | `npm run test:platform-release-eval` |
| Clerk launch contract | `npm run test:platform-clerk-launch` |
| Real Clerk boundary | `npm run prove:platform-clerk-launch` in the primary thread only |

The Stop hook is a safety net, not the completion proof. The primary thread must capture the exact commands, results, runtime boundary, and unverified surfaces.

### Acceptance-port collision rule

The existing Clerk-launch stack normally owns host HTTPS port `8443`. If the pre-push code gates pass but Docker acceptance cannot bind `8443`, do not classify that result as an application or test failure until the primary thread identifies the exact port owner.

When the verified owner is the existing Clerk-launch stack, keep that stack intact and retry the same real pre-push or acceptance workflow with the repository-supported override:

```powershell
$env:PLATFORM_ACCEPTANCE_HTTPS_PORT = '8444'
git push
```

For a direct acceptance rerun, set the same environment variable before the repository-owned acceptance command. Record both facts in the evidence: `8443` was occupied by the verified Clerk-launch stack, and the unchanged acceptance test passed or failed on `8444`. Do not suppress a different bind error, select an arbitrary port without checking it, stop an unverified process, or describe an environment collision as a passing test.

### Clean-commit Docker redeployment rule

After an authorized commit and before final deployment or release proof:

1. Confirm the intended commit is checked out and the worktree is clean.
2. Rebuild the Docker image from that committed object. Do not reuse an image built from a dirty worktree as release evidence.
3. Redeploy the affected Docker service or stack with the rebuilt image through the repository-owned compose or deployment command.
4. Wait for deterministic container health rather than a fixed sleep.
5. Run the applicable HTTPS acceptance or Clerk-launch proof against the redeployed image.
6. Record the commit ID, image identity when available, compose/service target, port override, health result, and proof result.
7. If the commit changes after the image build, rebuild and redeploy again before claiming release evidence.

Commit, feature-branch push, ready PR creation, babysitting, and merge remain under primary-thread publication authority but execute through `git_pr_manager`. Image rebuild, redeployment, and runtime proof remain primary-thread actions. A successful pre-commit or pre-push code gate does not prove that the deployed container runs the merged commit.

### Short orchestration triggers

Use `studio-run:` as the concise Studio orchestration prefix.

```text
studio-run: <task>
```

This selects the Studio authority order, artifact-owned specialist routing, non-overlapping write contracts, and repository-owned gates. It does not authorize a commit, push, deployment, or other external write unless the task says so explicitly.

Use `studio-run:full` as the explicit full publication trigger:

```text
studio-run:full <task>
```

`studio-run:full` authorizes this ordered workflow for the requested task:

1. Inspect the complete cohesive worktree and current branch/upstream state.
2. Run applicable focused, scoped, full, and runtime gates.
3. Reconcile evidence-backed review findings and fix blocking failures.
4. Create a short feature branch from the intended `master` state and commit the complete intended change with a plain, specific title.
5. Push the feature branch through the real pre-push hook. If Docker acceptance encounters the verified `8443` collision, retry the unchanged push with `PLATFORM_ACCEPTANCE_HTTPS_PORT=8444`.
6. File a real, ready-for-review PR against `master`; never create a draft for this workflow.
7. Babysit every required CI check and human or bot review item on the latest commit. Fix or explicitly resolve valid in-scope findings and stop on material scope expansion.
8. Merge through the repository's accepted normal method only when the worktree is clean, commits are pushed, required checks are green, feedback is resolved, and the PR is mergeable. Never use force-push, admin merge, or branch-protection bypass.
9. Verify the PR is merged and `origin/master` contains the result.
10. Check out or fast-forward the clean merged `master`, rebuild the Docker image from that exact merged object, redeploy the affected service or stack, and wait for deterministic health.
11. Run the applicable HTTPS acceptance or Clerk-launch proof against that image. Use verified port `8444` when the existing Clerk-launch stack owns `8443`.
12. Confirm clean status and report the branch, commit, PR, checks, review disposition, merge, image/deployment, health, acceptance, and remote evidence.

Stop without publishing if review, a required gate, clean-commit image build, redeployment, runtime proof, or remote verification fails. Do not interpret `studio-run:full` as authority to discard unrelated work, reveal secrets, reset history, bypass hooks, or perform a materially different product change.

### No-subagent threshold

Use one agent for a docs-only correction, a one-file mechanical edit, a tightly ordered single-owner fix, a task dominated by one Docker/Clerk operation, or any task where coordination costs exceed independent evidence value. Do not delegate to imitate a team structure.

## What the upstream system actually provides

The upstream project is more than a set of prompts. Its current source describes seven principal agents: Orchestrator, Explorer, Oracle, Council, Librarian, Designer, and Fixer. It also adds background scheduling, a shared job board, completion hooks, a wake scheduler, reusable child-session aliases, model presets, multi-model Council dispatch, per-agent skills and MCP policy, and multiplexer panes. [Upstream README](https://github.com/alvinunreal/oh-my-opencode-slim/blob/282d5f26a4ad2665118a73014fcf02e57869bd38/README.md) [Upstream codemap](https://github.com/alvinunreal/oh-my-opencode-slim/blob/282d5f26a4ad2665118a73014fcf02e57869bd38/codemap.md)

Its central workflow is:

```text
orchestrator plans
  -> dispatches independent specialist lanes
  -> continues non-conflicting work
  -> receives terminal results
  -> reconciles evidence and disagreement
  -> verifies the integrated outcome
```

The source explicitly limits parallel writes to non-conflicting scopes and prefers read-heavy scouting as a first delegation target. Its Council is intentionally expensive and reserved for decisions where independent perspectives reduce material uncertainty. [Background orchestration](https://github.com/alvinunreal/oh-my-opencode-slim/blob/282d5f26a4ad2665118a73014fcf02e57869bd38/docs/background-orchestration.md) [Orchestrator prompt source](https://github.com/alvinunreal/oh-my-opencode-slim/blob/282d5f26a4ad2665118a73014fcf02e57869bd38/src/agents/orchestrator.ts)

These are the valuable design principles to retain. The OpenCode-specific lifecycle machinery is not required to obtain them in Codex.

## Capability comparison

| Capability | Codex-native status | Recommended treatment |
| --- | --- | --- |
| Root agent plans and synthesizes | Native | Keep the primary thread as the only integration owner. |
| Parallel specialist agents | Native | Delegate only independent, bounded lanes. |
| Follow-up, wait, interrupt, close | Native | Let Codex own thread lifecycle. Use `/agent` in CLI to inspect threads. |
| Built-in general worker and explorer roles | Native | Prefer custom roles only when stricter behavior is useful. |
| Per-agent model and reasoning effort | Native | Use fast models for bounded read work and stronger judgment for review. |
| Per-agent instructions | Native | Put one role in each `.codex/agents/*.toml`. |
| Per-agent sandbox | Native with parent runtime override caveat | Make read roles `read-only`; choose the parent permission mode before delegation. |
| Per-agent MCP and skill configuration | Native | Grant only the tools needed by the role. Omitted settings inherit from the parent. |
| Project routing policy | Native through `AGENTS.md` or skills | State when to delegate, when to wait, and required output. |
| UI visibility into active child threads | Native in supported clients | Use the app/IDE panel or CLI `/agent`. |
| Automatic proactive delegation | Conditional | Current local Codex delegates after a direct request or applicable `AGENTS.md` or skill instruction. Put the policy there. |
| Background job board and wake scheduler | No equivalent project configuration documented | Do not recreate initially. Codex already waits and consolidates requested results within a workflow. |
| Persistent reusable-session aliases | No equivalent custom-agent feature documented | Prefer fresh bounded tasks. Continue an existing agent only inside the active workflow when useful. |
| Cross-provider Council with configured councillors | Partial | Spawn independent read-only reviewers and synthesize in the parent. Codex custom agents use Codex-supported session configuration; there is no documented Council preset abstraction. |
| Runtime `/preset` team switching | Partial | Use Codex config profiles selected with `--profile` for session-level variants. Do not promise hot team switching. |
| Tmux/Zellij/Herdr/cmux panes | No native equivalent needed | Use the client thread UI. Treat multiplexer support as an optional external convenience. |
| Todo auto-continuation after idle | No equivalent project configuration documented | Require explicit completion gates in `AGENTS.md`; do not inject synthetic turns. |
| Custom installation CLI | Not needed for one repository | Commit `.codex/` and `AGENTS.md`. Consider a reusable skill or plugin only after the pattern proves stable. |

The Codex guidance supports this mapping directly: parallel agents are best for read-heavy exploration, tests, triage, and summaries; parallel write-heavy workflows need more care because they increase conflicts and coordination cost. Subagents also consume more tokens than a comparable single-agent run. [OpenAI: Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)

## Generic Codex reference architecture

The examples in this section document the native Codex mechanism. They are not the Studio implementation contract. Use the Studio role names, root-only boundaries, gate mapping, and rollout packet above when configuring Wer Ywet Studio.

```text
user request
    |
    v
primary Codex thread
  owns intent, plan, task graph, integration, final verification
    |
    +-- explorer (read-only) ------ code paths, owners, tests, risks
    |
    +-- researcher (read-only) --- current primary-source facts, when needed
    |
    +-- designer (read-only) ----- rendered UI evidence, when needed
    |
    +-- worker (write) ----------- one bounded, non-overlapping change
    |
    `-- reviewer (read-only) ----- independent diff and evidence challenge
             |
             v
primary thread reconciles -> runs authoritative gates -> reports outcome
```

### Ownership rules

1. Keep planning, task boundaries, user decisions, integration, and the final answer in the primary thread.
2. Give each delegated task one output contract and one clear stop condition.
3. Prefer parallel delegation for independent reads.
4. Use one write owner for a file set at a time.
5. Start implementation only after the relevant ownership and failure paths are known.
6. Treat a subagent summary as evidence to inspect, not proof that the integrated result works.
7. Run repository-owned gates in the primary thread after all changes are integrated.
8. Escalate to multiple reviewers only when disagreement can change a costly or risky decision.

## Generic custom-agent templates

Do not copy this complete generic set into Studio. Studio uses the installed artifact-owned roles in the authoritative binding above; the later generic `worker`, `researcher`, and `designer` examples are reference material only.

```text
<repository>/
├─ AGENTS.md
└─ .codex/
   ├─ config.toml
   └─ agents/
      ├─ explorer.toml
      ├─ worker.toml
      ├─ reviewer.toml
      ├─ researcher.toml      # phase 2
      └─ designer.toml        # phase 2
```

Project-scoped Codex configuration loads only for trusted projects. User-level configuration remains in `~/.codex/config.toml`. [OpenAI: Configuration Reference](https://learn.chatgpt.com/docs/config-file/config-reference)

### `.codex/config.toml`

```toml
[agents]
enabled = true
max_concurrent_threads_per_session = 4
default_subagent_model = "gpt-5.6-terra"
default_subagent_reasoning_effort = "medium"
interrupt_message = true
```

Why four: it permits up to four specialists beside the primary thread without encouraging an unbounded fan-out. Increase the limit only after measurements show that queued independent work is a real bottleneck. Codex excludes the primary thread from this setting. `agents.max_threads` remains a legacy alias, but new configuration should use `agents.max_concurrent_threads_per_session`. [OpenAI: Subagent global settings](https://learn.chatgpt.com/docs/agent-configuration/subagents#global-settings)

### `.codex/agents/explorer.toml`

```toml
name = "explorer"
description = "Read-only codebase explorer. Use to locate canonical owners, execution paths, call sites, tests, and relevant recent changes before implementation."
model = "gpt-5.6-luna"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"

developer_instructions = """
Stay in exploration mode.
Trace behavior from entry point to canonical owner.
Inspect call sites, contracts, tests, and relevant local changes.
Distinguish observed evidence from inference.
Return concise file and symbol references, risks, and unanswered questions.
Do not edit files or propose a broad redesign.
"""
```

### `.codex/agents/worker.toml`

```toml
name = "worker"
description = "Implementation agent for one bounded change after the owner, contract, and failure behavior are understood."
model = "gpt-5.6-terra"
model_reasoning_effort = "medium"

developer_instructions = """
Implement only the assigned bounded change.
Preserve unrelated user work.
Use the existing canonical owner and repository abstractions.
Make failures explicit.
Run the smallest relevant success-path and failure-path checks.
Return changed files, exact checks, failures, and remaining uncertainty.
Do not commit, push, or expand scope.
"""
```

Do not put `sandbox_mode = "workspace-write"` here unless the team wants that default in every client. A child inherits the parent turn's live sandbox and approval choice, and live runtime overrides are reapplied when Codex spawns it. Choose the parent permission mode before delegation. [OpenAI: Approvals and sandbox controls](https://learn.chatgpt.com/docs/agent-configuration/subagents#approvals-and-sandbox-controls)

### `.codex/agents/reviewer.toml`

```toml
name = "reviewer"
description = "Independent read-only reviewer for correctness, security, ownership, regressions, failure paths, and missing proof."
model = "gpt-5.6-sol"
model_reasoning_effort = "high"
sandbox_mode = "read-only"

developer_instructions = """
Try to falsify the implementation's important claims.
Inspect the complete relevant diff and its call paths.
Prioritize correctness, security, state transitions, regressions, and missing tests.
Report only evidence-backed findings, ordered by severity, with file references.
State which claimed surfaces were not tested.
Do not edit files.
"""
```

### `.codex/agents/researcher.toml` (phase 2)

```toml
name = "researcher"
description = "Read-only primary-source researcher for current APIs, frameworks, specifications, and version-specific behavior."
model = "gpt-5.6-luna"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"

developer_instructions = """
Use official documentation, source code, specifications, and first-party APIs.
Verify version-specific claims.
Separate sourced facts from inference.
Return concise findings with direct links.
Do not edit application code.
"""

[mcp_servers.openaiDeveloperDocs]
url = "https://developers.openai.com/mcp"
```

The official custom-agent example uses this MCP endpoint for an OpenAI documentation specialist. Other research domains need their own trusted primary-source tools or web access. [OpenAI: custom-agent example](https://learn.chatgpt.com/docs/agent-configuration/subagents#example-1-pr-review)

### `.codex/agents/designer.toml` (phase 2)

```toml
name = "designer"
description = "Read-only rendered-interface specialist for hierarchy, spacing, typography, color, motion, feedback, and shared component causes."
model = "gpt-5.6-terra"
model_reasoning_effort = "high"
sandbox_mode = "read-only"

developer_instructions = """
Inspect the rendered interface when tools and a runnable route are available.
Translate feeling-based feedback into testable design hypotheses.
Check hierarchy, spacing, scale, typography, contrast, alignment, depth, motion, latency, feedback, and affordance.
Trace shared design-system or component causes before suggesting local patches.
Return evidence, likely owner, exact recommendation, and unavailable coverage.
Do not edit files.
"""
```

All standalone custom-agent files must define `name`, `description`, and `developer_instructions`. Other normal Codex session keys can override model, reasoning, sandbox, MCP, and skill settings. Omitted settings inherit through Codex's documented resolution rules. [OpenAI: Custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents)

## Generic `AGENTS.md` routing pattern

Adapt this pattern to the Studio binding. Do not replace Studio's cloud law, task-routing table, test economy, or verification table.

Add a bounded section to the repository's existing `AGENTS.md`; do not replace repository-specific engineering rules.

```md
## Agent orchestration

Use the primary thread as the only owner of intent, planning, integration,
authoritative verification, and the final response.

Delegate only when the task has independent, bounded work that can run in
parallel or when a specialist's isolated context materially improves quality.

- Use `explorer` before changing unfamiliar or cross-cutting code.
- Use `researcher` for current external APIs or specifications. Require primary
  sources and direct links.
- Use `designer` for rendered UI evidence or feeling-based design feedback.
- Use `worker` for one explicit implementation scope after ownership is known.
- Use `reviewer` after material or risky changes, before declaring completion.

For each delegated task, provide the objective, allowed scope, constraints,
required evidence, output format, and stop condition.

Run independent read-only tasks in parallel. Do not assign overlapping write
scopes. Wait for every result that the next decision depends on. Reconcile
conflicts explicitly. Inspect the integrated diff and run repository-owned
gates in the primary thread.

Use one agent for small, sequential, or tightly coupled work. Do not delegate
only to imitate a team structure.
```

Codex reads `AGENTS.md` before work, combines global and project instructions from repository root toward the current directory, and lets closer files override earlier guidance. The default combined instruction limit is 32 KiB. Keep the routing section short and place detailed specialist procedure in the agent file or an existing skill. [OpenAI: AGENTS.md discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

## Delegation contracts

### Explorer request

```text
Have explorer map the account deletion flow. Return:
1. entry points and canonical owner;
2. persistence, authorization, and external side effects;
3. existing tests and uncovered failure paths;
4. exact file and symbol references.
Do not edit files. Wait for the result before planning the change.
```

### Parallel read request

```text
Run explorer and researcher in parallel.
Explorer: map the current retry implementation and tests.
Researcher: verify the provider's current retry and idempotency contract from
primary sources.
Wait for both, reconcile conflicts, then propose the smallest change.
```

### Bounded worker request

```text
Have worker implement only the agreed retry-owner change in these files: ...
Preserve public contracts and unrelated edits. Run the named focused tests.
Return the diff scope, exact results, and any unverified boundary.
```

### Review request

```text
Have reviewer independently inspect the complete diff against main. Try to
falsify correctness, authorization, recovery, and test-coverage claims. Return
only evidence-backed findings by severity. Do not edit files.
```

### Council request

Codex does not need a permanent Council agent for the first release. Use a prompt-driven pattern:

```text
This is a high-cost architecture decision. Spawn three read-only reviewers with
independent lenses: operational failure, domain ownership, and migration risk.
Do not let them see each other's conclusions. Wait for all three. In the
primary thread, compare agreements and disagreements, cite evidence, and make
one recommendation with a confidence statement and explicit unknowns.
```

This preserves the upstream Council's useful property—independent judgments followed by synthesis—without claiming cross-provider diversity or building a new runtime. Use it only when the answer can change a high-cost, security-sensitive, or hard-to-reverse decision.

## Execution state model

Use a small task graph in the primary thread:

| State | Meaning | Exit gate |
| --- | --- | --- |
| `scoped` | Intent, boundaries, and required proof are explicit. | Independent lanes identified. |
| `exploring` | Read-only agents gather code, docs, runtime, or design evidence. | Required evidence returned or an explicit coverage gap recorded. |
| `decided` | Primary thread selects the owner and approach. | Implementation contract is bounded. |
| `implementing` | One worker owns each non-overlapping write scope. | Changes and focused checks complete. |
| `reviewing` | Reviewer challenges the integrated change and proof. | Findings resolved, accepted, or reported. |
| `verifying` | Primary thread runs authoritative repository and runtime gates. | Exact pass/fail evidence captured. |
| `complete` | Requested outcome is achieved with remaining uncertainty stated. | Final response. |

Do not equate “subagent finished” with “work integrated.” The primary thread owns every state transition.

## Generic staged rollout

Use this as evaluation background. The Studio-specific first implementation packet below is the executable rollout order for this repository.

### Stage 0: Baseline

Before adding configuration, collect five representative tasks:

- unfamiliar code exploration;
- bounded defect fix;
- cross-layer feature change;
- material code review;
- current-documentation lookup.

Record wall-clock time, total agent count, changed-file conflicts, gate results, review findings, and whether the final answer needed correction. This is the comparison baseline.

Exit gate: tasks and scoring rubric are committed or otherwise stable before agent prompts are tuned.

### Stage 1: Minimal three-role pilot

Add `.codex/config.toml`, `explorer.toml`, `worker.toml`, `reviewer.toml`, and the routing section. Keep concurrency at four. Run the five tasks with direct delegation instructions.

Exit gates:

- all agent files load and can be selected;
- explorer and reviewer remain read-only;
- worker stays inside assigned files on at least four of five tasks;
- no overlapping writes occur;
- the primary thread reports exact repository gate results;
- token and elapsed-time increases are justified by fewer missed issues or faster parallel reads.

### Stage 2: Conditional specialists

Add `researcher` only if at least two pilot tasks require external version-specific facts. Add `designer` only if rendered UI work is common and the necessary browser/render tools are available.

Exit gates:

- researcher cites primary sources and labels inference;
- designer provides rendered evidence or explicitly states why it is unavailable;
- neither role edits application code;
- adding the role reduces primary-thread context noise or improves detected issues.

### Stage 3: Workflow skills

If the same multi-step orchestration recurs, encode that workflow in one narrow skill. Keep role identity in agent files and task procedure in the skill. Skills use progressive disclosure: Codex initially receives names and descriptions, then reads full instructions only when a skill is selected. [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills)

Exit gate: at least three real tasks demonstrate the same procedure and output contract. Do not create a skill to wrap one prompt.

### Stage 4: Optional profiles and Council

Add configuration profiles only when teams need stable cost/quality modes. Select them with `codex --profile <name>`; treat them as session configuration, not a clone of upstream `/preset`. Add the prompt-driven Council only after a documented decision class benefits from independent reviews.

Exit gate: measured demand, a documented fallback, and a cost ceiling exist.

### Stage 5: Productized distribution

Only after the repository-local pattern is stable, decide whether to distribute it as a reusable Codex plugin or skill package. A Codex plugin is appropriate when other users need to install a coordinated bundle of skills and tool connections. It is not required for local custom agents. [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills)

## Generic validation and evaluation gates

For Studio, combine these orchestration smoke checks with the repository-owned gate mapping in the authoritative binding above.

### Configuration smoke test

1. Start a new trusted-project Codex session.
2. Ask Codex to list the available custom agents and their descriptions.
3. Ask it to spawn `explorer` for a read-only repository map.
4. In CLI, use `/agent` to inspect the child thread.
5. Confirm that the result returns to the primary thread.
6. Ask Codex to interrupt a disposable read task and confirm the interruption is visible.

### Permission test

Give `explorer` a task that requests a temporary file write. The expected result is refusal or failure under `read-only`. Repeat with the parent permission mode changed and verify that documented live parent overrides behave as expected. Never test this against live data.

### Routing test matrix

| Scenario | Expected route | Failure signal |
| --- | --- | --- |
| One-file mechanical edit | Primary or one worker | Explorer/reviewer ceremony without risk benefit. |
| Unfamiliar cross-layer bug | Explorer, then worker | Worker edits before owner and path are known. |
| Current API behavior | Researcher | Unsourced or secondary-source claims. |
| Visual regression | Designer plus explorer as needed | Source-only design claim with no render evidence. |
| High-risk completed change | Reviewer | Reviewer edits code or reports style-only noise. |
| Three independent audits | Parallel read-only agents | Sequential execution without dependency. |
| Two edits to the same file set | One writer, sequential | Concurrent conflicting patches. |

### Quality rubric

Score each representative task from 0 to 2:

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Scope control | Material drift | Minor drift | Exact bounded scope |
| Evidence | Unsupported | Partial references | Direct code/runtime/source evidence |
| Ownership | Parallel or copied owner | Owner implied | Canonical owner explicit |
| Failure paths | Missing | Mentioned | Tested or bounded gap stated |
| Integration | Child output trusted | Partial primary check | Full relevant diff and gates checked |
| Efficiency | More cost, no value | Mixed | Faster or materially higher quality |

Adopt the pilot only if it improves the aggregate score without increasing unresolved merge conflicts or hiding verification failures.

### Completion gate

Do not call the setup complete until:

- Codex loads every intended agent in a new session;
- one parallel read workflow returns and is reconciled;
- one worker change is constrained to its assigned scope;
- one independent review produces either evidence-backed findings or a clear no-findings result;
- the primary thread runs the repository-owned gate;
- remaining untested surfaces and token/cost impact are reported.

## Risks and mitigations

| Risk | Effect | Mitigation |
| --- | --- | --- |
| Agent proliferation | Routing becomes ceremony and prompts consume attention. | Start with three roles; require repeated demand before adding one. |
| Token amplification | Each child performs its own model and tool work. | Delegate only independent or specialist-worthy work; cap concurrency at four. |
| Parallel write conflicts | Lost time, inconsistent changes, user work overwritten. | One write owner per file set; parallelize reads first. |
| False confidence from consensus | Several agents can repeat the same assumption. | Give reviewers independent lenses; require code/runtime/source evidence; surface disagreement. |
| Permission mismatch | A custom read-only default can be affected by live parent overrides. | Select parent permission mode deliberately and run permission smoke tests. |
| Stale model names or capabilities | Checked-in config stops matching the available catalog. | Review model settings on Codex upgrades; keep role behavior independent of one model name. |
| Tool inheritance too broad | A specialist can access irrelevant or sensitive tools. | Define per-agent MCP/skill settings where needed; use read-only roles. |
| Primary-thread abdication | Child summaries become unverified final claims. | Make integration and authoritative gates explicit primary-thread duties. |
| Instruction conflict | Global, root, nested, skill, and agent rules compete. | Keep one owner for each rule; use nested overrides only for true local differences. |
| Recreating plugin machinery | Maintenance cost exceeds benefit. | Do not build job boards, wake hooks, session aliases, or pane managers without measured need. |

## Non-goals

- Do not port `oh-my-opencode-slim` or install it into Codex.
- Do not reproduce its mythology, names, or full agent count merely for parity.
- Do not build an OpenCode compatibility layer.
- Do not promise multi-provider Council behavior through Codex custom-agent configuration.
- Do not run every task through multiple agents.
- Do not allow overlapping agents to edit the same files.
- Do not replace repository tests, CI, review, or runtime proof with agent agreement.
- Do not add a background scheduler, synthetic continuation turns, reusable-session database, or terminal multiplexer in the initial system.
- Do not package a reusable plugin before the project-local workflow has measured value.

## Recommended first implementation packet

If Studio adopts this packet, use these verification steps when its configuration changes:

1. Recheck `git status --porcelain=v2 --branch`; preserve the current local commits and any newer user work.
2. Keep narrow `.gitignore` exceptions for `.codex/config.toml` and `.codex/agents/**`. Preserve the existing hook exceptions.
3. Keep `.codex/config.toml` on Sol Medium for the primary thread, multi-agent enabled, at most four child threads, Luna as the default subagent model, and Low as the default subagent effort. Do not alter the existing hook lifecycle.
4. Keep these installed roles and permissions:
   - read-only: `codebase-explorer`, `roadmap-verifier`, `security-isolation-reviewer`, and `dependency-researcher`;
   - workspace-write: `default-implementer` (Terra High), `product-manager` (Terra High), `design-engineer` (Terra High), and `test-engineer` (Luna Medium).
5. Keep the concise Studio orchestration section in root `AGENTS.md`. Point to canonical owners and existing gates instead of copying them into agent prompts.
6. Keep `.codex/README.md` synchronized with discovery, permissions, trigger semantics, and the Stop-hook relationship.
7. Start a new trusted-project Codex session and prove all roles load and return to the primary thread.
8. Pilot planning with `codebase-explorer`, `roadmap-verifier`, and `test-engineer` in evidence-only mode; then let the primary thread reconcile one bounded implementation contract.
9. Assign product code to `default-implementer`. Assign separate non-overlapping product docs, UI, and test artifacts to their named specialists only when those artifacts are in scope.
10. Treat disagreement with live code as a blocker to changing the target, not permission to guess.
11. Run `npm run gate:local -- --paths .codex/config.toml .codex/agents AGENTS.md .codex/README.md`, `npm run test:local-git-gate`, and `git -c core.whitespace=cr-at-eol diff --check` for a configuration change.
12. Record time, token use, routing mistakes, write-scope conflicts, false findings, context reduction, and whether specialist work improved the integrated result.

The smallest useful Studio outcome is not “seven agents installed.” It is a reliable loop in which the primary thread selects one canonical release packet, specialists remove read-heavy evidence from the main context, one owner changes each invariant, independent review challenges tenant and failure boundaries, and the existing hooks plus runtime gates remain authoritative.

## Studio source files inspected

These repository-owned sources support the Studio binding. Recheck them at implementation time because the local branch can move after this research snapshot.

- `<target-repository-root>/AGENTS.md` — cloud law, hard boundaries, task routing, test economy, and mandatory gates.
- `<target-repository-root>/docs/AGENTS.md` — documentation authority and cloud ownership.
- `<target-repository-root>/CONTEXT.md` — Account, WorkspaceMembership, Workspace, Project, and Project Type language.
- `<target-repository-root>/docs/architecture/mvp-rust-mysql-horizontal-expansion-plan.md` — live release status, one-slice execution contract, migration order, canonical owners, and exit gates.
- `<target-repository-root>/docs/architecture/react-cloud-frontend-plan.md` — browser ownership, routes, rendered states, and web verification.
- `<target-repository-root>/apps/platform/README.md` — current API and runtime boundary.
- `<target-repository-root>/package.json` — repository-owned command definitions.
- `<target-repository-root>/scripts/local-git-gate.cjs` — changed-path routing and authoritative local checks.
- `<target-repository-root>/.codex/hooks.json` and `<target-repository-root>/.codex/hooks/*.cjs` — existing Codex validation lifecycle.
- `<target-repository-root>/.gitignore` — current `.codex` tracking boundary.

## Primary sources

- [OpenAI, Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) — availability, triggering, orchestration controls, permissions, custom-agent locations/schema, settings, and examples.
- [OpenAI, Configuration Reference](https://learn.chatgpt.com/docs/config-file/config-reference) — project and user config scope, `[agents]` fields, config profiles, sandbox, and MCP keys.
- [OpenAI, Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) — instruction discovery, precedence, and size limit.
- [OpenAI, Build skills](https://learn.chatgpt.com/docs/build-skills) — reusable workflow packaging and progressive disclosure.
- [oh-my-opencode-slim README at researched commit](https://github.com/alvinunreal/oh-my-opencode-slim/blob/282d5f26a4ad2665118a73014fcf02e57869bd38/README.md) — advertised agents, workflows, presets, and optional features.
- [oh-my-opencode-slim background orchestration at researched commit](https://github.com/alvinunreal/oh-my-opencode-slim/blob/282d5f26a4ad2665118a73014fcf02e57869bd38/docs/background-orchestration.md) — scheduler, job-board, wake, reconciliation, and write-scope rules.
- [oh-my-opencode-slim configuration at researched commit](https://github.com/alvinunreal/oh-my-opencode-slim/blob/282d5f26a4ad2665118a73014fcf02e57869bd38/docs/configuration.md) — layered configuration, agents, presets, MCP, and permissions.
- [oh-my-opencode-slim Council at researched commit](https://github.com/alvinunreal/oh-my-opencode-slim/blob/282d5f26a4ad2665118a73014fcf02e57869bd38/docs/council.md) — configured parallel councillors and synthesis behavior.
- [oh-my-opencode-slim orchestrator source at researched commit](https://github.com/alvinunreal/oh-my-opencode-slim/blob/282d5f26a4ad2665118a73014fcf02e57869bd38/src/agents/orchestrator.ts) — routing thresholds, specialist lanes, parallel-write rule, completion, and session reuse.
- [oh-my-opencode-slim codemap at researched commit](https://github.com/alvinunreal/oh-my-opencode-slim/blob/282d5f26a4ad2665118a73014fcf02e57869bd38/codemap.md) — source-level ownership of job board, hooks, presets, task sessions, and multiplexers.
