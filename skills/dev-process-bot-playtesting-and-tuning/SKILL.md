---
name: dev-process-bot-playtesting-and-tuning
description: Tune difficulty, thresholds, or other parameters with headless bots or recorded-input replays against target outcomes. Use for simulation-based tuning; use saas-perf-hillclimb for sustained SaaS performance optimization.
---

# Bot playtesting and tuning

1. Define target outcomes, parameter bounds, and correctness guardrails.
2. Build a headless runner using the production logic with isolated effects.
3. Choose representative bots or recordings and reproducible seeds.
4. Separate tuning inputs from held-out evaluation inputs before adjusting parameters.
5. Measure outcome rates and uncertainty across enough trials to support the decision.
6. Evaluate the selected settings once on the holdout set.

Compare candidates on matched workloads and seeds. Include relevant weak and strong strategies or adverse conditions; do not equate bot success with human experience or replay performance with live results. Stop at the agreed trial or time budget and report missed targets rather than tuning indefinitely. Treat repeated holdout-driven adjustment as further tuning that requires fresh evaluation inputs.

Retain the selected configuration and reproducible evaluation command. Use deterministic assertions for exact rules and justified tolerances for noisy outcomes. Report baseline and selected outcomes, trial counts, uncertainty, holdout results, and untested conditions. Keep publication subject to the user's authority.

Adapted from the [tibo.dog development thread](https://x.com/poteto/status/2117043478140276847).
