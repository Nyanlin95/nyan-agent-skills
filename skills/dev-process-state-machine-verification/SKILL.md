---
name: dev-process-state-machine-verification
description: Model stateful modes, timers, and interleaved events to find counterexamples with TLA+/TLC or bounded state and property checks. Use for a subsystem whose ordering or recovery rules need explicit verification.
---

# State-machine verification

1. Map the subsystem's authoritative state, events, effects, and code owners.
2. Define safety invariants and liveness obligations with explicit environment and fairness assumptions.
3. Choose a state table with property tests or a TLA+ model according to the ordering risk.
4. Run the checker over documented bounds and configurations.
5. Trace each counterexample to the requirement, model, or implementation that is wrong.
6. Add a real-code regression for each confirmed implementation defect.

Model shared events and interactions when separately correct subsystems can fail together. Include relevant interruption, timeout, stale-event, and recovery paths; do not invent states or force every flow into terminal completion. Inspect deadlocks and vacuous properties as well as reported violations.

Keep the model, command, and state-to-code mapping beside the subsystem's existing verification owner. Rerun after relevant changes; do not create a per-system skill automatically. Report assumptions, explored bounds, counterexamples, and implementation checks. Treat checker success as evidence about the model within those limits, not proof of all runtime behavior.

Adapted from the [tibo.dog development thread](https://x.com/poteto/status/2117043478140276847).
