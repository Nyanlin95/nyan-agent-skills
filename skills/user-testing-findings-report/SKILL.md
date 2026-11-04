---
name: user-testing-findings-report
description: >-
  Use when turning user-test session logs and chaos runs into a ranked findings
  report: deduplicating, severity by harm to each persona, evidence, a verdict,
  what was not tested, and a hand-off for fixes and re-testing.
---

# User Testing Findings Report

Part of the [User Testing Playbook](../user-testing-playbook/SKILL.md). Inputs: session logs from [Session Runner](../user-testing-session-runner/SKILL.md) and failures from [Chaos and Random Input](../user-testing-chaos-and-random-input/SKILL.md). Use [report-template.md](../user-testing-playbook/references/report-template.md) for the layout.

## Steps
1. **Collect.** List every session with persona, scenario, outcome and effort. Count outcomes: met, partly, not met, gave up.
2. **Extract.** Pull every non-ok step into a candidate finding with its evidence.
3. **Merge.** Combine candidates that share one cause, even when found by different personas. Keep the list of which personas and sessions hit it; that count is a signal.
4. **Rate severity** using the rubric below.
5. **Write each finding** with the format below. One finding, one problem.
6. **Give the verdict** and the list of what was not tested.
7. **Hand off** with clear owners and a re-test list.

## Severity rubric (by harm to that persona's goal)
- **Blocker**: the persona could not reach the goal, lost data or money, or the app crashed or misled them in a way that matters. Includes any accessibility barrier to the main job.
- **Major**: reached the goal only with detours, repeated errors, or high confusion; or trust was damaged.
- **Minor**: noticeable hesitation, rough edges, unclear wording, small layout slips, with no effect on the outcome.
- **Polish**: preferences and delight opportunities.
Raise by one level when three or more personas hit it, or when it is on the main job's path. Lower by one when it needs an unusual action that a real person is unlikely to take. State the reason for every Blocker and Major.

## Finding format
```
F-07 [Major] Short plain title (what the user experiences)
Where: screen and element
Who hit it: personas and sessions (for example Achiever S-01, First-Timer S-04)
What happened: observed, in order
What they expected: and why a real person would
Evidence: screenshot paths, log lines, console or network lines, seed (for chaos)
Steps to repeat: from a stated start state
Confidence: confirmed (repeated) / seen once / intermittent / unclear
Hypothesis (optional, labelled): a guess about the cause, which the builder is free to discard
Suggested direction: the outcome wanted, not a prescription
```
Rules: no finding without evidence; label a cause guess as a hypothesis; write what the user felt in plain words; do not blame the user.

## Verdict
Pick one and give three lines of reasons:
- **Block**: at least one Blocker on a P1 job.
- **Fix before release**: no Blocker but Majors on P1 jobs, or many Majors.
- **Release with known issues**: only Minor and Polish on P1, Majors only on P3.
- **Looks good for the tested scope**: no Blocker or Major; say which scope.
Never say "no issues"; say "no issues found in N sessions covering X; not covered: Y".

## Always include
- **Scope and method**: app and build, date, personas, number of sessions, environments, seeds.
- **Outcome table**: persona by scenario with met, partly, not met, gave up.
- **What worked**: moments of delight and clear flows, so they are kept.
- **What was not tested** and why (needed real accounts, real payments, device types, languages, load, real users).
- **Questions for real users**: things a simulation cannot answer.
- The note that all findings are from simulated users.

## Hand-off and re-test
1. Group findings by owner (design, frontend, backend, content, product) and by suggested order: Blockers, then Majors on P1, then the rest.
2. For each finding that is a bug, suggest the regression check that would have caught it; see [Bug to Lint Rule](../dev-process-bug-to-lint-rule/SKILL.md) and [Budgets That Fail the Build](../dev-process-budgets-that-fail-the-build/SKILL.md) for slowness.
3. After a fix, re-run the failed sessions and the chaos seeds that found it. Mark the finding closed only when the same session passes, never because the symptom is hidden.
4. Keep the matrix and logs so the next round starts from them.

## Presenting
Lead with the verdict and the three most important findings, with screenshots. The full list is a link or a file. In chat keep it to a short summary; for a report the person will return to or share, make it a Page.
