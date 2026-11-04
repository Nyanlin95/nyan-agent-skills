---
name: user-testing-playbook
description: >-
  Use when you need to test any app, site or prototype the way different kinds
  of users would actually use it (goal-driven, bored, curious, impatient, random
  clicking, first-time, keyboard-only, mobile, and more), find where it breaks
  or disappoints, and report it with evidence. It routes to the linked User
  Testing skills (personas, scenarios, session runner, chaos and random input,
  findings report).
---

# User Testing Playbook (meta skill)

Simulate real people using an app, find where it fails them, and prove it with evidence. It works for any product (web app, site, mobile web, desktop app, chat product, game, dashboard, checkout, onboarding) because nothing here is tied to one app: you learn the app first, then adapt the personas and scenarios to it.

**One idea: a user is a goal plus a state of mind, not a script.** The same screen is a different test for someone who must finish a task in 60 seconds, someone killing time, and someone mashing every button. Test the product against what each person expects, not against what the builder intended.

## What this is and is not
- It finds usability problems, confusion, dead ends, broken flows, crashes, slowness, trust and accessibility gaps, and missing feedback.
- It does not prove people want the product or will pay for it. Simulated users are not real users: label every finding "simulated", and say which questions need real people (see the Limits section).
- It never replaces automated tests. When a finding is a bug, turn it into a regression check. Use [Local Git Gates](../local-git-gates/SKILL.md) when enforcing recurring defects in hooks or CI.

## The linked skills
| Step | Skill |
| --- | --- |
| Decide who is testing and what they want | [User Testing Personas](../user-testing-personas/SKILL.md) |
| Turn the app and the personas into concrete scenarios and a test matrix | [User Testing Scenarios](../user-testing-scenarios/SKILL.md) |
| Run one session in character, log it, capture evidence | [User Testing Session Runner](../user-testing-session-runner/SKILL.md) |
| Random clicking, rapid input, odd input, interruptions, seeded and replayable | [User Testing Chaos and Random Input](../user-testing-chaos-and-random-input/SKILL.md) |
| Turn logs into severity-ranked findings, a verdict and a hand-off | [User Testing Findings Report](../user-testing-findings-report/SKILL.md) |

## The workflow
1. **Intake (5 minutes, never skip).** Get: the app URL or build, who it is for, the top 3 jobs it must do, what is out of bounds, test accounts and test data, what is safe to click. Read [intake-checklist.md](references/intake-checklist.md). If the app is live with real data or money, stop and agree safe rules first (see Safety).
2. **Map the app.** Explore as yourself first, with no persona: list screens, entry points, the main flows, forms, destructive actions, and the places state changes. Note anything surprising.
3. **Pick personas.** Choose 4 to 6 from the persona library that fit this app, always including one goal-driven user, one impatient or distracted user, one random clicker, and one first-timer. Add personas the app's audience needs (for example a store owner, a child, a buyer comparing prices).
4. **Write scenarios.** One scenario per persona per important situation, each with a start state, a want, a stop condition and what success looks like to that persona. Build the matrix (persona x scenario x environment) and choose the smallest set that covers the risk. Read [expectation-matrix.md](references/expectation-matrix.md).
5. **Run sessions.** One session per row. Stay in character, act one step at a time, narrate what you expected and what happened, capture a screenshot at each decision and at each problem.
6. **Run a chaos pass.** At least one seeded random-input run per main flow.
7. **Report.** Merge duplicates, rank by severity and by how many personas hit it, give a verdict, list what was not tested.
8. **Hand off and re-test.** Send fixes to whoever builds. After a fix, re-run only the failed sessions and the chaos seed that found it.

## Expectations to cover (fill in more as the app needs)
Every session carries at least one of these. Name it in the scenario.
- **Achieve a goal**: finish a task fast and correctly (buy, book, set up, find, publish).
- **Entertain themselves**: browse for fun, kill time, follow curiosity, expect delight and no friction.
- **Explore and learn**: poke around to understand what this is; expect clear labels and safe undo.
- **Compare and decide**: weigh options, price and trust before committing; expect honest information.
- **Recover**: made a mistake or lost state; expect a clear way back.
- **Random or careless input**: tap everything, double-click, paste junk, go back mid-flow.
- **Be interrupted**: switch apps, lose network, come back later.
- **Stay in control**: privacy, consent, no surprise charges, no dark patterns.
- **Be included**: keyboard only, screen reader, zoom, reduced motion, colour contrast, small screens.
- **Feel it is fast**: first response under about one second, visible progress for anything slower.
- **Get help**: find support, understand errors, contact someone.
- **Share and return**: send a link or result, then come back later and find things as left.

## Failure modes to avoid (the testers' own)
- **Script following**: the tester does the happy path the builder imagined. Fix: each persona decides what to do from its want, not from the feature list.
- **Mind reading**: the tester knows the app too well and never gets lost. Fix: first-timer sessions start from the intake summary only, with no map notes.
- **Politeness**: every problem is rated minor. Fix: severity follows the harm to that persona's goal, with the rubric in the findings report skill.
- **Invented evidence**: describing what "probably" happens. Fix: every finding has a screenshot, a log line or exact steps. If it was not observed, it is a hypothesis and is labelled one.
- **Cleared by hiding**: closing the finding by hiding the symptom. Fix: re-test the original session.

## Safety (the rules for every session)
- Use test accounts, test data and a staging or local build whenever one exists.
- Never place a real order, send a real message or email, post publicly, delete real data, or change real settings. Stop at the last confirmation step and record it.
- Never enter real personal data, real payment details or real credentials into an app under test unless the owner supplied a test account for that purpose.
- Adversarial and abusive-input personas run only on apps the user owns, on test data.
- Respect rate limits and robots rules; do not load-test someone else's site.
- If a session hits something private, record that it exists, not its contents.

## Limits (say these in the report)
- Simulated users miss human things: real motor errors, real emotion, real context, real language habits.
- A model may know common patterns and behave more competently than a novice; the first-timer rule above reduces this but does not remove it.
- Use real users for decisions about pricing, positioning, brand, desirability, or when the cost of being wrong is high.

## Applying it in a particular environment
Which tools drive the app, capture screenshots and run in parallel depends on the agent. Read [environment-adapter.md](references/environment-adapter.md) for what to look for, and [agent-app-adapter.md](references/agent-app-adapter.md) when running on an agent app with a computer-use subagent.

## References
Files in this skill's `references/` folder:
- [intake-checklist.md](references/intake-checklist.md)
- [expectation-matrix.md](references/expectation-matrix.md)
- [heuristics-checklist.md](references/heuristics-checklist.md)
- [session-log-template.md](references/session-log-template.md)
- [report-template.md](references/report-template.md)
- [environment-adapter.md](references/environment-adapter.md)
- [agent-app-adapter.md](references/agent-app-adapter.md)
