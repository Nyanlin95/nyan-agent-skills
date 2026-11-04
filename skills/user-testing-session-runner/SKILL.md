---
name: user-testing-session-runner
description: >-
  Use when actually running one simulated user-test session in character against
  an app: acting one step at a time, narrating expectation versus result,
  deciding when the persona gives up, capturing screenshots and logs, and
  keeping the session safe.
---

# User Testing Session Runner

Part of the [User Testing Playbook](../user-testing-playbook/SKILL.md). Input: one scenario from [User Testing Scenarios](../user-testing-scenarios/SKILL.md) and its persona card. Output: a session log using [session-log-template.md](../user-testing-playbook/references/session-log-template.md) plus evidence files.

## Before the session
1. Confirm the safety rules in the playbook. Confirm the environment: build or URL, account, viewport, network, theme, locale.
2. Reset or note the start state. Use a fresh browser profile for First-Timer and Wrong-Audience sessions.
3. Read only the persona card and scenario. For the First-Timer, do not read the app map.
4. Set the session clock: start time and the patience limit.

## The loop (one action at a time)
For every step:
1. **Look.** Take a screenshot (or read the accessible tree) of what is on screen now.
2. **Expect.** Write one line: what the persona expects to happen next and why.
3. **Act.** Do exactly one thing a person would do (click, type, scroll, press a key, wait). Not several at once.
4. **Observe.** Take another screenshot. Write what actually happened, including how long it took if it was slow.
5. **Judge.** Compare expectation and result. Mark the step: ok, hesitation, confusion, error, dead end, broken, slow, or delight.
6. Capture evidence for anything that is not ok: screenshot, visible text, console or network error if you can see one, and the exact steps from the start state.

Keep the log as you go; do not reconstruct it after.

## Decisions that make it a test, not a demo
- **Look where the persona would look.** If the control they need is below the fold or hidden in a menu, they may not find it. Record how long you needed and where you looked first.
- **Hesitation counts.** If a persona would pause to work out what a label means, log it as "hesitation" with the label. Many findings are pauses, not errors.
- **Give up honestly.** When the patience limit passes with no progress, stop and write "gave up at step N because ...". Do not push through using knowledge the persona lacks.
- **Take the wrong turn they would take.** If the obvious button is not the one that works, follow the obvious one first.
- **Retry once, then switch.** Real users retry once, then try something else, then leave.
- **Note emotion in plain words** where it changes behaviour: "annoyed, closing the tab".
- **Don't fix while testing.** Record the problem; keep going from the state a user would be in.
- **Delight is data.** Log what felt good, so fixes do not remove it.

## Stop at the safe boundary
End the session at the last step before anything irreversible: payment, send, publish, delete, invite, real signup with a real email. Record "reached confirm step X; stopped by safety rules" and count that as reaching the goal for scoring, unless a test account was provided for completing it.

## Handling surprises
- App blocks you (captcha, login wall, bot check): record it as a finding on the persona's journey if a real user would hit it, and stop; do not try to get around a block aimed at automation.
- App crashes or goes blank: capture the screen, wait the patience limit, try reload once, record what was lost.
- You hit private or real data: stop, record that it exists, not what it says.
- You cannot tell if something is a bug or intended: log it as "unclear" with the reason; do not guess.

## Session scoring (each persona, each session)
- **Outcome**: goal met / partly / not met / gave up.
- **Effort**: number of steps, number of hesitations, number of errors, time.
- **Feeling**: one word and why.
- **Top three problems** with step numbers.
- **Best moment**.

## Parallel runs
Sessions are independent, so several can run at once if the environment allows separate browser profiles or devices, but not on shared accounts or shared mutable test data. If they share data, run them in turn. Keep one log per session and merge only in the report.

## Done means
The log has a verdict per step, the outcome and score, evidence for every problem, and a list of what the persona did not reach.
