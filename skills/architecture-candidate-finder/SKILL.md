---
name: architecture-candidate-finder
description: Find and explain evidence-backed candidates to improve a codebase's design patterns, module boundaries, or architectural decisions. Use when the user asks what structural change is worth exploring, why a structural decision appears to cause recurring errors, or how to compare architecture options. For code or pull-request findings use cqt-review; for implementation use implementation-quality.
---

# Architecture Candidate Finder

Help the user choose which structural design problem is worth exploring. Ground each candidate in code or supplied evidence, explain technical terms in plain language, and compare the likely benefit with the complexity the change would add. Treat patterns as possible solution shapes, never as goals.

Translate everyday descriptions such as “brittle,” “hard to change,” or “this keeps breaking” into hypotheses to check. Do not require the user to know pattern or architecture vocabulary.

## Find and rank candidates

1. Set the requested area and question from the user's prompt. Keep the scan within that scope.
2. Read the relevant code, callers, tests, local architecture notes, and existing decision records. For a proposed design with no code, use its stated needs and mark unstated constraints as unavailable.
3. Gather concrete signals such as recurring errors, repeated changes across modules, duplicated rules, unclear ownership, leaked dependencies, confusing state transitions, or tests blocked by unrelated effects. Treat a reported pain as a lead; verify it where evidence is available.
4. Trace each promising signal from observation to its cause, affected owner, and practical cost. Separate observed structure from inferred runtime or maintenance impact.
5. Compare the current design, a local correction, and the smallest structural change that could remove the cause. Use a named pattern only when it describes that specific change.
6. Rank candidates by demonstrated pain or risk, likely reach, clarity of the responsible owner, benefit to future changes, and the indirection, migration, or operating cost introduced. Use qualitative confidence; do not invent numeric scores.
7. Explain each technical term when it first matters. Connect the term to the actual code and say what becomes easier or harder for a caller or maintainer.
8. Recommend the strongest candidate first. Include up to two other candidates only when they offer materially different benefits. Recommend no structural change when the evidence does not justify one.

Read [references/candidate-lens.md](references/candidate-lens.md) when translating design signals into questions or explaining pattern choices.

## Report

For each candidate, state:

- **Evidence and friction:** Point to the relevant paths or supplied evidence and describe the concrete cost.
- **Candidate direction:** Name the owner or boundary that may change and sketch the smallest useful shift.
- **Why it may fit:** Explain the design idea in plain language and connect it to the observed cause.
- **Trade-off:** State the new indirection, migration cost, failure mode, or operating responsibility it could add.
- **Confidence and unknowns:** Separate observed facts, inferences, and missing evidence that could change the ranking.
- **Next decision:** Say what to inspect or compare next, without treating the recommendation as approval.

Keep the report short enough to compare candidates. Do not force a finding count, pattern name, severity label, or formal architecture diagram.

## Boundaries

- Keep the work read-only. Do not edit code, create an ADR, or record a decision unless separately asked.
- Do not turn a candidate scan into a correctness review of a changed area; use `cqt-review` for that work.
- Do not implement a selected design until the user asks; use `implementation-quality` for the implementation.
- Do not recommend a pattern because of a line count, a switch threshold, a popular architecture style, or a hypothetical future need.
- Treat broad system choices as unresolved when workload, consistency, reliability, operating capacity, data lifecycle, or cost evidence is missing.
