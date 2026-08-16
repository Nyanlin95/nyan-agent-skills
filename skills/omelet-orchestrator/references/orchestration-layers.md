# Orchestration Layers

Use this catalog to compose and compile orchestration plans. Keep the layer boundaries: task semantic → orchestration semantics → orchestration primitives. Do not plan directly in primitive roles.

The hierarchy is compositional and bottom-up authoritative: primitives compose into orchestration semantics, and orchestration semantics compose into the task semantic. The task semantic is a reconstructed label, not a prescribed category.

## L1 — Task Semantics (reconstructed)

Treat these labels as a recognition library, not a classification input. Form the task semantic as a working hypothesis, then re-derive it from the orchestration semantics and primitives actually used. You may prune or remove this catalog; the reconstruction policy below is what makes the label work.

| Task Semantic | Meaning | Reconstruction signature |
| --- | --- | --- |
| Feature Development | Add a new behavior to a product | Spec-Driven Development → Test-Driven Development → CQT Review? → Blast-Radius Validation? |
| Bug Resolution | Fix an observed defect | Debug-and-Repair → Test-Driven Development → Blast-Radius Validation? |
| Large Refactor | Restructure code without changing behavior | Blast-Radius Analysis → Refactoring Orchestration → Test-Driven Development → CQT Review |
| Migration | Move code, data, or infrastructure to a new owner | Migration Orchestration → Test-Driven Development → Blast-Radius Validation |
| Incident Resolution | Restore a live system and record the cause | Debug-and-Repair → Test-Driven Development → Blast-Radius Validation |
| Research Investigation | Answer a question with evidence | Research-Synthesize-Verify |
| Release Preparation | Qualify a change for delivery | Release Qualification → Blast-Radius Validation? |

## Reconstruction policy

Rebuild the task semantic from what the orchestrator discovers. Do not treat the opening request or the initial label as final.

1. Record each orchestration semantic actually invoked, in the order it fired.
2. Record which optional semantics became necessary and which planned semantics never fired.
3. Record the topology that emerged for each semantic.
4. Record which gates and checkpoints produced evidence.
5. When a composition is non-standard, record the primitives that form each semantic.
6. Re-label the task from the discovered composition using the L1 signatures as recognition patterns.
7. Keep the discovered composition as the task's description when no signature matches.
8. Do not force a label onto a composition that matches none.
9. Refresh the label whenever a later delegation changes the discovered composition.
10. Report the final label with the evidence that confirmed it.

## L2 — Orchestration Semantics

Select the orchestration semantics that compose the working hypothesis. These are the reusable patterns; compose each from L3 primitives below.

| Orchestration Semantic | Use when | Compiled pipeline |
| --- | --- | --- |
| Focused Implementation | The change is small and contained | Implementation Worker with a bounded contract |
| Spec-Driven Development | Behavior must match a written contract | Spec Writer → Implementation Worker → Acceptance Judge |
| Test-Driven Development | Correctness must be proven incrementally | Test Designer → Implementation / Fix Worker → Test Runner → Acceptance Judge → Repair Loop |
| Debug-and-Repair | A defect has an unknown cause | Reproduction → Isolation → Fix Worker → Test Runner |
| Refactoring Orchestration | Structure must change without behavior change | Blast-Radius Analysis → Stepwise Refactor → Test Runner |
| Migration Orchestration | State or traffic moves to a new owner | Dual-Run → Cutover → Rollback Gate |
| Research-Synthesize-Verify | A question needs evidence | Researcher → Synthesizer → Verifier |
| Hypothesis-Test-Refine | A hypothesis must survive testing | Hypothesizer → Tester → Refiner → Debate |
| CQT Review | Quality and ownership need assessment | Critic → Report → Judge |
| Blast-Radius Validation | Affected boundaries must stay intact | Boundary Map → Focused Check → Gate |
| Adversarial Review | Material claims need falsification | Critic → Counterexample → Judge |
| Security-Sensitive Change | Credentials, isolation, or data loss dominate | Threat Map → Fix Worker → Security Gate |
| Release Qualification | A change must pass release gates | Release Gates → Sign-off → Gate |

The compiled pipeline is a sketch, not a rigid template. Adjust the primitives to the concrete task and repository constraints. Blast-Radius Analysis is the boundary-mapping phase of Blast-Radius Validation.

## L3 — Orchestration Primitives

Compile semantics into these primitives for delegation. Pipeline role names in the L2 table are concrete labels for these primitives; give each primitive the label the task needs. Do not let primitives become the public planning language.

| Primitive | Responsibility |
| --- | --- |
| Coordinator | Owns the plan, integration, evidence, decisions, and completion |
| Planner | Turns an outcome into a semantic plan |
| Router | Dispatches bounded work to specialists |
| Specialist | Applies domain expertise to a bounded task |
| Implementation Worker | Writes code to an accepted contract |
| Fix Worker | Repairs a specific defect |
| Tester | Runs and reports checks |
| Critic | Raises issues against the plan or result |
| Judge | Accepts or rejects an outcome |
| Synthesizer | Merges evidence and results into a report |
| Gate | Blocks or allows the next step |
| Checkpoint | Records state and evidence for a later decision |
| Ledger | Records contracts, evidence, and results |

## Topology modifiers

Attach a topology to a semantic only where it changes how the work is organized.

| Topology | Example use |
| --- | --- |
| Swarm(Research) | Parallel specialists on independent branches |
| Arena(Test Design) | Competing candidates tested against a shared harness |
| Committee(Architecture Review) | Concurrent critics with one decision |
| Debate(Hypothesis Evaluation) | Opposing judges resolve a claim |
| Hierarchy(Migration) | Serialized levels with gates |

## Example compilations

```text
Test-Driven Development
        ↓ compile

Test Designer(s)
        ↓
Implementation / Fix Worker(s)
        ↓
Test Runner
        ↓
Acceptance Judge
        ↺
Repair Loop
```

```text
Bug Resolution :=
    Debug-and-Repair
    → Test-Driven Development
    → Blast-Radius Validation?
```

```text
Large Refactor :=
    Blast-Radius Analysis
    → Refactoring Orchestration
    → Test-Driven Development
    → CQT Review
```
