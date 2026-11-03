# Enforce recurring constraints

## Turn a defect into a check

1. Identify a demonstrated bug pattern or recurring violation that can be detected reliably.
2. Choose the smallest existing test, linter extension, analyzer, or structural check that catches the cause.
3. Add a violating fixture and a valid near-miss fixture.
4. Make the diagnostic explain the corrective action.
5. Inspect existing matches before fixing in-scope violations or documenting justified exceptions.
6. Integrate the check through the canonical runner and CI.

Prefer a behavioral regression test when syntax cannot reliably distinguish the defect. Use text matching only when syntax, comments, and strings cannot create misleading matches. Preserve local style conventions; do not turn every review preference into a lint rule or introduce a separate rule registry by default.

## Scope rules through paths

Reuse existing directories or suffixes when a path reliably identifies code with special constraints, such as generated sources or a measured hot loop. Introduce a new convention only when it enables a needed check and has a clear owner. Verify matching and nonmatching paths, imports, and build discovery after any rename.

Treat path labels as enforcement scope, not proof of purity or performance. Check prohibited effects or measured costs with suitable tooling; avoid blanket allocation bans without evidence about the actual runtime and workload.

## Enforce a performance budget

1. Choose a user-relevant metric and a justified limit from the requirement and baseline.
2. Fix the workload, environment, units, and measurement boundary.
3. Measure repeated runs when noise can affect the result.
4. Report the measured value, limit, and workload from one reproducible command.
5. Fail on a breached limit or unavailable required measurement.
6. Exercise both passing and over-budget cases through the canonical gate.

Use deterministic checks for size and a controlled benchmark with an explicit noise policy for timing. Distinguish domain event time from local elapsed processing time; do not subtract unrelated clocks to claim end-to-end latency. Require an explained workload or requirement change with matched evidence before revising a limit.

Adapted from the [tibo.dog development thread](https://x.com/poteto/status/2117043478140276847); treat its project choices as examples rather than universal policy.
