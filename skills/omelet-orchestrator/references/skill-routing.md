# Skill routing

Use this index to select owners, then read only their relevant instructions. Keep the active route in working context as `task part → skill → required proof`; avoid producing a routing report unless it helps the user. Keep scope, authority, coordination, and final acceptance with Omelet.

## Resolve a route

Prefer explicit user selection, applicable repository policy, and the actual deliverable over keyword matches. Use canonical repository skills for edits to this library. Resolve installed and plugin skills through the current session catalog and its access mechanism; names below are discovery hints, not installation paths or promises of availability. Prefer the available provider tools when they cover the task. Follow tool prerequisite skills before the tool call.

Keep unavailable optional craft guidance from blocking authorized work. Report an unavailable explicitly requested or required skill and its consequence. Never install, synchronize, add dependencies, send messages, or publish merely because a route mentions that capability. Do not treat routing as authority for an external write.

## Library owners

Use these sibling-relative links in this repository or when the linked skills are installed together. Resolve by catalog name when the host stores them elsewhere.

| Task part | Canonical skill | Selection boundary |
| --- | --- | --- |
| Runnable foundations, code changes, ownership correction | [implementation-quality](../../implementation-quality/SKILL.md) | Keep ordinary implementation here; avoid loading it for a trivial mechanical edit. |
| Frontend state, navigation, caching, loading and recovery | [frontend-system-principles](../../frontend-system-principles/SKILL.md) | Add for interactive system boundaries rather than every CSS edit. |
| Sustained measured performance improvement | [saas-perf-hillclimb](../../saas-perf-hillclimb/SKILL.md) | Require a target and empirical comparison; keep one-off fixes with implementation. |
| Code, migration, correctness and ownership review | [cqt-review](../../cqt-review/SKILL.md) | Keep the review read-only. |
| Discover and compare structural improvements | [architecture-candidate-finder](../../architecture-candidate-finder/SKILL.md) | Return evidence and options before implementing a redesign. |
| Challenge an uncertain decision-critical claim | [adversarial-review](../../adversarial-review/SKILL.md) | Use bounded counterexamples; avoid adding a routine second review. |
| Shared hooks, CI agreement, recurring defects and budgets | [local-git-gates](../../local-git-gates/SKILL.md) | Keep regression tests in their owning suite and recurring enforcement in the existing gate. |
| Visual foundations, geometry, composition and verdict | [nyan-ui-visual-review](../../nyan-ui-visual-review/SKILL.md) | Require for rendered UI changes; retain its evidence and verdict ownership. |
| Author or remove unnecessary interface text | [clean-copy](../../clean-copy/SKILL.md) | Preserve facts, decisions, recovery and accessible meaning. |
| Review changed copy and related accessibility | [ui-copy-review](../../ui-copy-review/SKILL.md) | Keep findings read-only; avoid treating it as a complete accessibility audit. |
| Disposable browser document or interaction study | [build-html-prototype](../../build-html-prototype/SKILL.md) | Contain the artifact in one removable folder; keep production untouched. |
| Wonder canvas design, review, save or export | [wonder-design-workflow](../../wonder-design-workflow/SKILL.md) | Keep static canvas evidence distinct from runtime or provider acceptance. |
| Source-grounded editorial ideas, drafts and review | [nyan-editorial](../../nyan-editorial/SKILL.md) | Preserve the draft owner, voice and verified facts. |
| Plain technical prose or controlled-language rewrite | [simplified-technical-writing](../../simplified-technical-writing/SKILL.md) | Apply its requested language mode to prose rather than code. |
| Bounded non-sensitive OpenCode implementation | [handoff-to-opencode](../../handoff-to-opencode/SKILL.md) | Leave live model eligibility and wrapper recovery with this skill. |
| Interleaved state, timers and recovery counterexamples | [dev-process-state-machine-verification](../../dev-process-state-machine-verification/SKILL.md) | Bound the subsystem; avoid requiring formal modeling for ordinary work. |
| Exact recorded-input reproduction | [dev-process-deterministic-core-and-replay](../../dev-process-deterministic-core-and-replay/SKILL.md) | Keep effects isolated and compatibility explicit. |
| Simulation-based parameter or difficulty tuning | [dev-process-bot-playtesting-and-tuning](../../dev-process-bot-playtesting-and-tuning/SKILL.md) | Use held-out inputs; keep SaaS optimization with hillclimb. |
| Broad simulated usability testing | [user-testing-playbook](../../user-testing-playbook/SKILL.md) | Let it own the testing workflow; label simulated evidence honestly. |
| Select simulated users and behavioral goals | [user-testing-personas](../../user-testing-personas/SKILL.md) | Route directly for persona-only requests. |
| Build a persona/situation/environment matrix | [user-testing-scenarios](../../user-testing-scenarios/SKILL.md) | Keep scenarios tied to audience goals and risk. |
| Execute one in-character test session | [user-testing-session-runner](../../user-testing-session-runner/SKILL.md) | Capture expectation, observed result and evidence. |
| Seeded careless or random input and replay | [user-testing-chaos-and-random-input](../../user-testing-chaos-and-random-input/SKILL.md) | Isolate mutations from real users and live effects. |
| Synthesize usability logs and retest handoff | [user-testing-findings-report](../../user-testing-findings-report/SKILL.md) | Preserve evidence, tested scope, severity and simulation limits. |

## Installed and plugin capabilities

Discover the matching currently available skill for each row. Read its actual trigger and requirements before use. Preserve repository and product conventions over a craft skill's preferred visual style.

| Work | Skills to discover | Routing decision |
| --- | --- | --- |
| Existing web stack and current platform guidance | `modern-web-guidance`, relevant framework/provider skill | Observe mandatory research prerequisites when applicable; verify exact versions before changing contracts. |
| Interface craft and motion | `emil-design-eng`, `apple-design`, `design-taste-frontend`, `animate`, `animate-expo`, `animation-vocabulary` | Select the medium and needed craft; avoid loading multiple aesthetic systems by default. |
| Find or review motion | `find-animation-opportunities`, `improve-animations`, `review-animations` | Match discovery, advisory refinement or read-only review to the requested outcome. |
| Faux product illustration or cursor demo | `stageshow` | Pair its authoring craft with Nyan visual review; treat authored demos as illustrations, never runtime acceptance. |
| Figma design or implementation | `figma-use`, `figma:figma-use`, `figma:figma-design-to-code`, relevant Figma workflow | Load the tool's mandated prerequisite; use the actual file and selected-node context. |
| Wonder or tldraw authoring | `wonder:wonder-design`, `tldraw-offline` | Pair the Wonder provider adapter with the library workflow; select tldraw only for its actual canvas. |
| Images and desktop inspection | `imagegen`, `computer-use:computer-use`, `screenshot` | Match generation, app operation or explicit screenshot capture; prefer purpose-built tools when sufficient. |
| Interactive explanation or disposable experiment | `visualize`, `canvas`, `prototype` | Select the artifact requested; distinguish Codex Canvas from a contained HTML prototype. |
| Documents, PDFs, spreadsheets and presentations | `documents:documents`, `pdf:pdf`, `spreadsheets:Spreadsheets`, `presentations:Presentations` | Load the medium owner and inspect the actual artifact; use available workspace runtimes. |
| Connected Workspace files and reusable pages | `google-drive:google-drive`, relevant Docs/Sheets/Slides skill, `pages:write-page`, `pages:maintain-space` | Use connected-source owners; preserve native document state and explicit write authority. |
| WordPress content and plugin work | `app-6a2b62fd753c8191bcff02ac79b54c6b:edit-wordpress-block-content`, relevant WordPress tools | Use block-content guidance for serialized blocks; use project implementation and checks for PHP plugin code. |
| APIs, webhook delivery and local simulation | Relevant `postman:*` skill | Match discovery, contract, testing, webhook capture or simulation; distinguish local replay from fresh delivery. |
| Authentication and database work | Relevant `clerk*`, `supabase:supabase`, relevant `planetscale-*` skill | Route by the actual provider and operation; keep inspection read-only and require existing authority for mutations. |
| Deployment, AI SDKs and durable workers | Relevant `vercel:*` skill or the project's actual provider workflow | Follow the current provider and repository release owner; never infer deployment authority from implementation. |
| Security investigation | `security-best-practices`, `security-threat-model`, `security-ownership-map`, `review-security` | Match the requested security question; avoid adding a generic audit to every feature. |
| Skills, rules, hooks and agent configuration | `skill-creator`, `create-rule`, `create-hook`, `create-subagent`, `local-git-gates` | Extend the actual owner; keep policy edits distinct from activated host behavior. |
| PR creation, monitoring or repair | `file-pr`, `babysit-pr`, `autopilot` | Select only for the requested Git operation; preserve exact-head checks and publication authority. |
| Automation, goals and chat management | `automate`, `goal`, `loop`, relevant Codex app tools | Honor invocation boundaries; do not turn an ordinary task into a goal, recurring job or new chat. |

## Compose by outcome

Adapt these examples instead of prescribing pipelines:

- Build or repair an app journey: use implementation guidance, add frontend guidance for state boundaries, and require visual review when the UI changes.
- Refine a Wonder screen: use the library Wonder workflow plus the provider adapter; add motion or illustration craft only when the requested artifact needs it.
- Investigate a watcher or webhook: start with read-only provider evidence; add webhook testing or replay for the unresolved delivery boundary; implement only within the authorized scope.
- Improve CI or application performance: use hillclimb for a sustained measured target and local Git gates when enforcement changes; retain the project's qualification owner.
- Test a product from user perspectives: route broad work through the testing playbook, or select the specific testing owner for a bounded request; send bug fixes to implementation and retest the original failure.

Keep simulated usability, visual approval, deterministic checks, provider delivery, release qualification and production readiness as separate claims. Report only the claims supported by the evidence actually collected.
