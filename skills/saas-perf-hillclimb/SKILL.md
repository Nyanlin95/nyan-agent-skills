---
name: saas-perf-hillclimb
description: Improve the measured performance of a SaaS product one layer at a time with a statistically gated hill-climb loop across database, backend/API, frontend, CDN/edge, infrastructure, and load capacity. Use for sustained latency, Core Web Vitals, query time, throughput, or error-rate improvement against a target, performance baselines, and layer-by-layer optimization passes. Do not use for a one-off slowness fix without a sustained target, read-only performance audits, or capacity purchases; use implementation-quality for ordinary code changes and cqt-review for review-only work.
---

# SaaS Performance Hill Climb

Improve one metric at a time with measured, reversible changes. Climb the stack one layer at a time in the order below. Keep a change only when the measurement proves it and correctness holds. Never claim a win from code inspection.

## Frame the climb

1. Name the user complaint and the layer most likely to own it.
2. Choose one metric and the direction that counts as better.
3. Set a ceiling from the user's target or the default targets below.
4. Choose a fast signal that runs in seconds and tracks the metric.
5. Define a guard: the tests and output checks that must stay identical.
6. Fix the scope: the paths, services, and settings you may change.
7. Split the inputs into a dev set for climbing and a holdout set for the final score.
8. Set a budget in attempts or time.

Ground each choice in a realistic workload: data size, tenant count, history depth, cache state, and concurrency. If no workload reproduces the complaint, fix the reproduction before climbing.

## Default targets

Use these as ceilings when the user gives none.

| Layer | Metric | Default ceiling |
| --- | --- | --- |
| Backend/API | Response time | P50 < 200 ms, P95 < 1 s |
| Database | Query time | P95 < 100 ms |
| Frontend | Core Web Vitals | LCP < 2.5 s, CLS < 0.1 |
| Load | Capacity | 2x expected peak at < 1% errors |

## Build the harness

1. Write one repeatable command that runs the workload and prints the metric, the error count, and a count of the work done.
2. Run the guard and record a green result.
3. Run an A/A baseline: the unchanged system measured at least five times.
4. Record the median and spread as the noise floor.
5. Freeze the harness. Do not edit it during the climb.

If the harness cannot separate an easy case from the complaint case, revise the workload or metric before continuing.

## Profile before guessing

Profile the current layer and rank where time goes. Ground each hypothesis in a named mechanism from the profile. Order candidates cheapest first:

1. Don't do it.
2. Do it once, not again.
3. Do less of it.
4. Do it later.
5. Do it when the user is not looking.
6. Do it concurrently.
7. Do it cheaper.

Read [layers.md](references/layers.md) for per-layer metrics, profiling tools, and candidate lists.

## Run the loop

1. Read the decision log.
2. Pick one hypothesis.
3. Make one change for that hypothesis only.
4. Run the guard.
5. Measure with the frozen harness on the dev set.
6. Accept only when the guard is green, p < 0.1 against the baseline samples, and the median improves by at least 3%.
7. Revert the change in full when any condition fails.
8. Log the attempt as kept or reverted.
9. Commit each accepted change on its own, staging only its files.

Use [decision-log.md](references/decision-log.md) for the log format. Never stack untested changes.

## Stop and move layers

Stop climbing the current layer when one of these holds:

- The metric reaches the ceiling.
- Three candidates in a row are rejected after you pivot category once.
- The budget is spent.

Then move to the next layer: database, backend/API, frontend, CDN/edge, infrastructure, load. Re-run the A/A baseline after moving, because earlier layers change the noise floor. Skip a layer only when its profile shows it holds no meaningful share of the metric, and record why.

Correctness and simplicity outrank the number. Revert a win that changes output. Keep a simplification that holds the number.

## Score the holdout

1. Run the frozen harness on the holdout inputs for the baseline revision.
2. Run it on the final revision.
3. Report a dev gain that does not reproduce on the holdout as overfit, not a win.

## Related skills

- Use [implementation-quality](../implementation-quality/SKILL.md) for the code inside each accepted change.
- Use [frontend-system-principles](../frontend-system-principles/SKILL.md) for frontend state, caching, and loading behavior touched by frontend candidates.
- Use [local-git-gates](../local-git-gates/SKILL.md) when adding a performance budget check to hooks or CI.
- Use [cqt-review](../cqt-review/SKILL.md) for an independent review of the final change set.

## Completion

Report:

- the metric, ceiling, and workload per layer
- the baseline, final value, and percent change on dev and holdout
- the noise floor
- attempts run, kept, and reverted per layer
- each kept change on one line
- the decision log path
- layers skipped and why
- the next idea worth trying

## Sources

Synthesized from Hill Climb by bendrucker (https://www.skillsdirectory.com/skills/bendrucker-hill-climb-claude) for the gated loop, and application-performance-performance-optimization by sickn33 (https://github.com/boisenoise/skills-collections/blob/fd52b51a21f89151424e03609bd1a549c3bd7a96/skills/antigravity-application-performance-performance-optimization/SKILL.md) for the layer coverage and default targets. Loop structure follows the pstack Hillclimb and Perf issue playbooks.