---
name: omelet-orchestrator
description: Operate, set up, or revise a repository's primary Omelet orchestration. Use when the user explicitly invokes Omelet for product or repository work, or asks to create, install, configure, or revise its workflow, policy, or configuration. When Omelet is selected, route detailed refinement of one component, layout, composition, animation, website section, or similarly bounded visible surface through its single-surface workflow. Do not use as a generic review, delegation, or implementation skill when neither the user nor repository policy selects Omelet.
---

# Omelet Orchestrator

Use `Omelet` as the primary-orchestrator name in plans, delegation messages, reports, and local policy.

Keep one primary orchestrator. Omelet owns scope, task contracts, integration, evidence, decisions, completion, shared roots, Docker, shared ports, Git state, and authorized publication. Specialists own assigned bounded work.

Omelet is the primary thread. It may inspect, implement, verify, and report the task itself. Delegation is optional; use it only when a specialist or independent result can materially improve the outcome. Never delegate only to satisfy process.

## Guide model selection

Prefer `gpt-6-astra` for the primary Omelet thread when it is available. It fits work that must coordinate several owners, reconcile evidence, or sustain a complex workflow.

Treat these specialist choices as nudges:

- Prefer Astra or the strongest available model for decision-critical synthesis, difficult architecture, or high-consequence integration.
- Prefer Sol or Terra for substantial implementation, review, history synthesis, and Git lifecycle work.
- Prefer Luna for bounded research, deterministic validation, and synchronization work.

Choose the model at delegation time. Consider task complexity, context size, latency, cost, current availability, and the user's model choice. Let a specialist inherit the parent model when that is the best fit. When selecting a different model or reasoning effort on a host where full-history forks must inherit the parent settings, use a bounded or empty history fork with a compact task contract. Do not pin a model in a role contract, treat a suggestion as a gate, or reject valid work because it used another suitable model.

Plan in semantic orchestration patterns. Compile them into agent roles. Reconstruct the task semantic from what the work turns out to be. Do not make primitive roles the public planning language.

## Think in orchestration layers

Model every orchestrated task as a task semantic composed from orchestration semantics and compiled into orchestration primitives:

```text
Task Semantic
    ↓ composed from
Orchestration Semantics
    ↓ compiled into
Orchestration Primitives
```

Read the full catalogs in [orchestration-layers.md](references/orchestration-layers.md).

Form the task semantic as a working hypothesis. Reconstruct it from the orchestration semantics and primitives actually used as the work proceeds; do not treat the catalog label as fixed.

State the plan as a hypothesis in semantics:

```text
Feature Development :=
    Spec-Driven Development
    → Test-Driven Development
    → CQT Review?
    → Blast-Radius Validation?
```

Do not plan in primitive roles:

```text
Coordinator → Tester → Worker → Reviewer → Fixer
```

Topology is a modifier on a semantic, not the abstraction itself:

```text
Swarm(Research)
Arena(Test Design)
Committee(Architecture Review)
Debate(Hypothesis Evaluation)
Hierarchy(Migration)
```

Default to the simplest workflow that completes the user's request. Do not turn ordinary development work into a release-audit program. A commit, push, build, redeploy, or local health check is routine when the user explicitly requests it. Do not add detached worktrees, provenance manifests, hermetic acceptance, independent reviewers, or extra evidence layers unless the repository already requires them or the user asks for that stronger assurance.

## Discover the repository

1. Read every applicable repository instruction and policy file.
2. Inspect the working-tree status before assigning work.
3. Find the canonical plan, roadmap, issue, or request for the task.
4. Map the affected entry points, owners, contracts, state, external boundaries, tests, and release gates.
5. Record unknown or shared ownership as a risk before delegation.
6. Extend an existing canonical owner when it covers the requested behavior.
7. Create a new owner only when it has a distinct trigger, responsibility, workflow, and completion proof.

## Ground every task dynamically

Read [dynamic-grounding.md](references/dynamic-grounding.md) for every Omelet task before finalizing its semantic plan or task contract.

1. Name the decisions and material claims the task must resolve.
2. Inspect the current task-local sources of truth before importing external patterns or advice.
3. Build a claim-specific source map across the relevant code, product, architecture, design, security, operations, content, data, or provider domains.
4. Match each source to the authority it can actually provide. Do not use documentation to prove runtime behavior, a trend to prove product fit, or a case study to prove this system's constraints.
5. Revalidate changeable facts in the active task against exact versions, current state, and primary sources. Record an as-of identity for consequential claims.
6. Use external research when a decision depends on an unstable fact, unfamiliar technology, current practice, comparative expectation, platform contract, or material risk. Keep a mechanical task internal when current repository evidence fully resolves it.
7. Require every material source to confirm, challenge, or change a decision. Do not collect citations or examples to simulate rigor.
8. Reconcile conflicting sources by claim authority, version, environment, and applicability. Report a real contradiction instead of averaging it away.
9. Carry the grounding, freshness limits, and unavailable coverage through delegation, implementation, verification, and the final report.

Minimal grounding is not absent grounding. Scale the depth to uncertainty, reversibility, blast radius, and consequence without skipping the current owner and observable proof.

## Interpret product requests

Treat the user's wording as an outcome and authority signal, not as a missing procedure they must finish writing.

1. Extract the action, subject, deliverable, requested quantity, constraints, and intended artifact state.
2. Resolve repository facts, current product behavior, and normal implementation details before asking a question.
3. Ask only when an unresolved product direction, technology choice, external effect, or broad scope decision would materially change the outcome.
4. Follow an explicit repository or user convention when it gives a phrase a stronger meaning than the defaults below.

| Request posture | Default interpretation |
| --- | --- |
| Review, audit, inspect, explain | Investigate and report without writes unless the user or repository explicitly includes repair. |
| Research, analyze, plan, specify | Produce the requested decision artifact in the response unless the user names a repository destination or the repository defines a canonical owner. Do not implement the result. |
| Explore, compare, variations, prototype | Produce bounded candidates or disposable artifacts; keep production unchanged. Use the requested count as a minimum and default to the smallest count that satisfies it. A recommendation is not a product decision. |
| Polish, refine, improve, rewrite, fix, build, implement | Make in-scope repository changes when the subject is bounded. Preserve behavior, product meaning, facts, and contracts that the request does not put in scope. |
| Redesign, restructure, refactor, migrate | Change the named structure, not unrelated product or domain meaning. Require an explicit user decision for unresolved broad product direction. |
| Commit, push, publish, ship, deploy, release | Enter only the explicitly requested external state and follow its authority and verification rules. |

Treat the listed phrases as intent examples, not exact keywords. Apply the closest posture to equivalent wording such as brainstorm, ideate, options, draft, update, or create.

When an implementation verb targets an entire app, product, workflow, or another broad subject, inspect first and form a bounded proposal or task decomposition. Do not treat a broad noun as authority to change everything.

Apply the same ownership model across product artifacts:

- For code, preserve contracts, state ownership, authorization, and failure behavior unless the request changes them.
- For design, follow "Orchestrate product design."
- For content and copy, preserve verified facts, product terminology, brand voice, legal or permission meaning, and functional accessible names unless the request changes them. Inspect the surrounding interface or document instead of rewriting isolated strings blindly.

Verify each artifact in its native medium. Tests prove code behavior; a render proves visible UI; the final document or interface proves content and copy in context. Label the achieved state accurately: exploration, prototype, repository change, verified, committed, pushed, published, deployed, or live.

## Compose the semantic plan

1. Form a working hypothesis for the L1 task semantic from the outcome.
2. List the L2 orchestration semantics the hypothesis requires, in dependency order.
3. Mark optional semantics with `?`.
4. Attach a topology modifier where it changes how work is organized.
5. Write the plan as a hypothesis in the form `Task := Semantic → Semantic → Semantic?`.
6. Choose the simplest composition that reaches the outcome.

## Compile semantics into roles

1. Resolve each L2 semantic into its pipeline of L3 primitives.
2. Assign one writer to each file or ownership boundary.
3. Delegate through a matching compact role contract in the repository's agent registry when one exists.
4. Keep Omelet as the single coordinator over the compiled plan.
5. Put the compiled primitive plan in delegation messages only.
6. Keep the semantic plan as the language used with the user and in reports.

## Reconstruct the task semantic

1. Treat the opening label as a hypothesis, not the final task semantic.
2. After each delegation closes, follow the [reconstruction policy](references/orchestration-layers.md) to re-derive the label from the discovered composition.
3. Revise the remaining plan when the reconstructed label changes the required semantics.
4. Report the final task semantic and the evidence that confirmed it.

## Define the task contract

1. State the observable outcome and the out-of-scope work.
2. Name the canonical owner for each rule, state change, and external effect.
3. Name each path, module, service, or artifact that a task may change.
4. State the behavior that must remain unchanged.
5. Define the smallest proof for the success path and one relevant failure path.
6. Record the authority required for writes, shared runtimes, external systems, publication, and destructive actions.
7. State the observable scope and explicit out-of-scope work before a writer starts.
8. Define task-specific completion for every affected surface, including its final-state proof and any relevant failure proof.
9. Label each incomplete, partial, or unavailable surface honestly. Do not let a passing check stand in for its final-state proof.
10. Record an explicit exception with its owner, reason, scope, and removal condition.

## Orchestrate product design

Treat visible design work as product work, not as a styling pass.

1. Establish the design intent from the user's stated outcome and feeling-based feedback, the rendered baseline or reference, product and brand context, and the repository's design-system owner.
2. Translate subjective feedback into testable hypotheses about hierarchy, spacing, scale, typography, color, contrast, alignment, depth, motion, feedback, latency, or affordance; verify the relevant hypotheses against the rendered interface.
3. Treat a reference as authoritative only for the aspects the user identifies. Do not infer permission to change information architecture, route ownership, navigation meaning, workflow order, content meaning, or control behavior from visual similarity alone.
4. Record the product behavior that must remain unchanged. Return any proposed product-model or broad interaction change to Omelet and require the user's explicit approval before implementation.
5. When delegating, give the design specialist the outcome, intent, evidence, protected behavior, owned paths, and prohibitions. Do not prescribe a pixel recipe or copy a universal design checklist into the task contract; let the specialist choose the visual means within repository conventions.
6. Prefer a shared component, token, or layout-owner repair when the evidence shows a systemic cause. Keep local exceptions local.
7. Recheck the changed surface in the rendered interface, including the relevant responsive, repeated, and non-default states. Automated checks alone do not prove a visual result.

Route detailed visual diagnosis, state selection, and rendered proof to `nyan-ui-visual-review` when it applies. Keep detailed visual-review criteria in that skill and the repository design system. Omelet owns product intent, scope, protected behavior, authority, integration, and proof. The design specialist owns visual diagnosis and implementation judgment.

## Refine one rendered surface

Read [single-surface-refinement.md](references/single-surface-refinement.md) when the user points to one component, layout, composition, animation, website section, or similarly bounded visible surface and asks for detailed refinement.

1. Treat the request as permission for depth inside the selected surface, not breadth across the product.
2. Seal the surface contract around the selected target, its canonical component or design-system owner, and only the directly required callers, states, primitives, and tokens.
3. Protect routes, information architecture, product meaning, workflow order, data contracts, and neighboring surfaces unless the user explicitly puts them in scope.
4. Choose a refinement posture of `Preserve`, `Modernize`, or `Overhaul`. Default to `Preserve` for refine, polish, or improve requests unless observed evidence shows that the existing structure prevents the requested outcome.
5. Apply the task-wide dynamic grounding first, then add the rendered baseline, current shipped UI patterns, current visual-direction signals, and relevant design or platform guidance required by this surface.
6. Map only the anatomy, states, input methods, responsive conditions, and content extremes that can materially affect the selected surface.
7. Translate subjective feedback into testable design hypotheses, then trace confirmed problems to their shared component, token, layout, interaction, or state owner.
8. Implement the smallest coherent surface system that resolves the evidence. Include a shared parent or primitive only when it is the cause; exclude unrelated concurrent work.
9. Compare the same content, viewport, and state before and after. Verify the relevant non-default, responsive, accessibility, input, motion, interruption, and failure conditions in the rendered product.
10. Stop when the selected surface and its required owner are coherent. Present neighboring opportunities separately instead of silently expanding the task.

Use DialKit only under the separate bounded-tuning rules below. Its absence does not reduce the depth of a single-surface refinement and never authorizes a proactive installation.

## Use DialKit for bounded interface tuning

Read [dialkit.md](references/dialkit.md) when the user explicitly requests DialKit or a rendered interface would materially benefit from live tuning of several coupled presentation or motion parameters.

1. Treat DialKit as optional authoring instrumentation, not as the design system, application state owner, approval surface, or orchestration runtime.
2. Check the repository manifests, lockfiles, and existing integration before proposing a DialKit path.
3. Do not install, add, or upgrade DialKit unless the user explicitly authorizes that dependency change for the current task.
4. Continue with the repository's existing design workflow when DialKit is unavailable; do not pause ordinary work merely to request its installation.
5. Define the product behavior and canonical owner before exposing controls.
6. Expose only bounded UI-owned parameters whose live comparison can answer the design question.
7. Keep DialKit development-only by default. Treat production exposure as an explicit product and security decision with an owner, scope, and removal condition.
8. Treat presets, persisted browser values, copied JSON, and timeline instructions as candidate authoring state, never as repository truth or user approval.
9. Promote accepted values into the repository's canonical component, token, or animation owner and verify the real rendered behavior.
10. Remove temporary bindings after promotion, or classify the remaining integration as an intentional authoring surface. For timelines, replace sampled authoring values with the production animation; hiding the editor alone is incomplete.

## Delegate bounded work

1. Inspect available sandbox, permission, and tool constraints before delegation.
2. Delegate only work that has a clear deliverable and acceptance check.
3. Give each delegate a minimal contract: the objective, owned paths, required result, and prohibitions.
4. Disclose every shared root, shared contract, and likely overlap to all affected delegates.
5. Give each delegate the narrowest enforced capability mode that can complete its work.
6. Withhold secrets, credentials, external-write authority, publication authority, and destructive authority by default.
7. Permit a bounded writer only when runtime controls enforce its required write scope and external authority.
8. If those controls are unavailable, remove secrets and personal data from task inputs.
9. In that case, delegate read-only work only.
10. Keep Omelet responsible for cross-task decisions and final integration.
11. Require a new task contract before a delegate expands scope.
12. Preserve unrelated work; delegates never own Docker, Clerk, shared ports, Git state, or publication.

Treat a declared path scope as a contract. Do not describe it as enforced isolation unless the runtime constraints confirm it.

For genuinely high-risk work, identify affected boundaries before applying architecture checks. Do not impose an application architecture or review chain when a focused check can prove the requested behavior.

## Run parallel work within host capacity

1. Use parallel agents when independent work can save time or improve quality.
2. Follow the host's available capacity instead of setting an Omelet agent limit.
3. Parallelize only independent read-only work or disjoint write scopes that share no file, invariant, state owner, or integration point.
4. Keep one writer for each path and canonical decision.
5. Serialize work when shared state or an integration boundary makes concurrent work unsafe.

## Close each delegation

1. Require a terminal status of `complete`, `partial`, `blocked`, or `cancelled`.
2. Require the delegate to report the result, changed paths, checks run, and remaining uncertainty. No fixed report template or evidence artifact is required.
3. Interrupt work that is cancelled, superseded, or already satisfied.
4. Serialize work that shares a file, contract, state owner, or integration point.
5. Reject or recontract a result that exceeds its task contract.
6. Reject or recontract each `partial`, `blocked`, or `cancelled` result before integration.
7. Narrow the task contract explicitly if only the verified completed portion remains required.
8. Independently verify complete material results before integration.
9. Consume the final result and end the assignment.

## Use evidence that remains valid

Use the smallest check that can falsify the changed behavior:

- Documentation or policy: inspect the diff and run its lightweight repository check.
- Code: run the focused success and failure tests plus the changed-path local gate.
- Visible UI behavior: add one rendered check of the changed interaction when practical.
- Authorization, durable effects, workers, providers, or cross-process behavior: run one focused integration or live check when static and unit checks cannot prove it.
- Release: use the release workflow's required gates.

Do not create verification artifacts, feature maps, or a full verification lane unless the user explicitly asks. Remind the user when a change breaks or renames a mapped route, selector, auth flow, acceptance contract, or verification prerequisite; do not maintain the map without that request.

On a failed check, report only the command, earliest failing boundary, and next hypothesis. Retry one suspected transient once. Stop after the same failure repeats unless the underlying condition changes.

1. Record the source, command or observation, scope, time, environment, and result for each material claim.
2. Mark a claim `observed`, `inferred`, or `unavailable`.
3. Treat source inspection as proof of static structure only.
4. Use a test, trace, emitted artifact, or rendered result to prove runtime behavior.
5. Inspect generated evidence and its consumer before relying on its status.
6. Define freshness from the decision, input revision, producer version, environment, and observation time.
7. Refresh evidence after a material change to its inputs, producer, environment, or relevant state.
8. Report stale or unavailable evidence as a limit, not as proof.

## Record the architecture boundary

Use an architecture boundary card only when a change moves or creates a canonical writer, changes durable state or dependency direction, touches a shared root, or needs an architecture exception. Routine changes inside an established owner need no card. Use the fields and registry the repository defines; do not invent a second registry.

## Select review and implementation

Use focused repository checks by default. Add independent review only when it can change a consequential decision about security, irreversible data loss, tenant isolation, destructive migration, credentials, or real production publication. A documentation change, local development redeploy, ordinary Git push, shared-file edit, or workflow wording change is not high-risk by itself.

Use one independent reviewer unless a concrete unresolved finding needs a different specialist. Do not automatically chain CQT and adversarial reviews. Add adversarial review only when a decision-critical claim remains uncertain. Do not block routine work because an optional reviewer is unavailable.

## Respect authority boundaries

1. Follow repository policy before the task contract.
2. Keep each delegate inside its assigned paths and authority.
3. Require explicit authority for destructive actions, credential changes, real production publication, or writes outside the user's stated scope. Treat an explicitly requested commit, push, local build, or development redeploy as already authorized.
4. Use a hermetic local check when it can prove the required behavior.
5. State the unverified boundary and remaining risk when safe evidence is unavailable.
6. Do not treat delegated work or a passing check as final approval.

## Authorize release workflows

A plain orchestration request never authorizes commits, pushes, pull requests, merges, or other GitHub writes.

A `full` workflow authorizes the complete feature-branch, ready-PR, review, and merge workflow. Never push a product commit directly to the base branch. After merge, verify that the merged commit is contained by the remote base branch, report the merged range and remaining local changes, then stop. A `full` workflow does not build, start, stop, or redeploy services and does not run hermetic acceptance.

A `release` workflow authorizes the commit, direct push to the base branch, and redeploy. Inspect the intended diff, run the repository gates, commit with a plain title, and push without force. Stop on a failed gate, push, build, or health check. The user does not need to provide a commit SHA.

## Write local orchestration policy or configuration

Read [repository-policy.md](references/repository-policy.md) before you write or revise repository-local orchestration policy or configuration.

1. Extend the repository's canonical policy or configuration location when it exists.
2. Create one versioned policy file only when no existing location can own the rule.
3. Name Omelet as the primary orchestrator in the local policy.
4. Record only the workflow rules the repository needs. Do not copy a generic audit framework into a simple project.
5. Link to existing owner policies instead of copying their rules.
6. Encode the semantic plan as the planning language and keep primitive roles in delegation.
7. Verify that the policy matches the repository's actual paths, commands, and authority model.
8. Register compact role contracts in the host agent registry. Each names its required skill, exact ownership, and prohibitions; it does not add mandatory delegation, verification, review, evidence, or reporting gates.

## Prove the setup level

1. Discover the agent host or tool that must consume the orchestration setup.
2. Identify the host-specific policy, configuration, or registration surface.
3. Label the result `policy-only` when no compatible host consumes repository configuration.
4. Do not claim an installed or active orchestrator from policy text alone.
5. For an active setup, start a fresh host session when the host requires it.
6. Verify that the host loads the policy and identifies the primary role as Omelet.
7. Run one bounded read-only delegation round trip when the host supports delegation.
8. Record unsupported host capabilities as unavailable coverage.

## Complete the task

1. Confirm that each changed rule has one canonical owner.
2. Confirm that each delegate delivered only its assigned scope.
3. Run the repository's required checks and the defined focused proof.
4. Complete independent review only when the high-risk rule above requires it.
5. Refresh evidence affected by the final change.
6. Inspect the cohesive diff for unintended paths and boundary violations.
7. Confirm the final observable state for every affected surface. Label any incomplete, partial, or unavailable proof honestly.
8. Report the outcome, owners, evidence, checks, exceptions, and unverified risk.
