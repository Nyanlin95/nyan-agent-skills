---
name: user-testing-chaos-and-random-input
description: >-
  Use when simulating users who click randomly, mash buttons, double-submit,
  paste junk, resize, go back mid-flow, or lose network, to find crashes, lost
  data and broken states; runs are seeded so a failure can be replayed.
---

# User Testing Chaos and Random Input

Part of the [User Testing Playbook](../user-testing-playbook/SKILL.md). For the Random Clicker, the Rule-Breaker and the Distracted Multitasker personas ([User Testing Personas](../user-testing-personas/SKILL.md)). It follows the same idea as [Bot Playtesting and Tuning](../dev-process-bot-playtesting-and-tuning/SKILL.md) and [Deterministic Core and Replay](../dev-process-deterministic-core-and-replay/SKILL.md): many cheap runs, seeded, replayable.

**One idea: random input is only useful if you can say what "broken" means and replay the run that broke it.**

## 1. Decide what broken means (the oracle) before you start
Write these checks first; a run fails if any is true:
- The page shows a blank screen, an error page, a stack trace or "undefined" / "NaN" / "[object Object]".
- The console shows an uncaught error, or the network shows 5xx responses or failed requests that the UI did not explain.
- The UI shows a spinner for longer than the app's own timeout, or a button stays disabled forever.
- Data is lost, duplicated or wrong after the actions (an item added twice, a draft gone, a total that does not add up).
- The app leaves its own origin, opens an unexpected new tab, or downloads something.
- Focus is lost into nowhere, or the keyboard is trapped.
- Layout breaks badly: content cut off, overlapping, horizontal scroll on a phone viewport.
- State disagrees between two views (a count in the header versus the list).
Record the checks in the session log so a reader knows what was being watched.

## 2. Set the seed and the rules
- Choose a numeric seed, write it down, and use it for every random choice (which element, which action, which input text). A run with the same seed and the same start state should repeat.
- Choose the run length (for example 100 actions) and the time limit.
- Choose the action mix. A good default: 55% click or tap a visible interactive element, 10% type into a field, 8% press a key (Tab, Enter, Escape, arrows, Space), 7% scroll, 6% Back or Forward or reload, 5% double-click or rapid repeat, 4% resize or rotate the viewport, 3% blur and refocus the window, 2% toggle network offline and online.
- Restrict to the app under test: do not follow external links, and block the destructive actions named in the intake (delete, pay, send, sign out of the test account).

## 3. Input pool (for typing into fields)
Empty; one space; a very long string (5,000 characters); text with accents, emoji, right-to-left text, combining characters; quotes, angle brackets and `<script>` text as plain text; a negative number, zero, a huge number, a decimal with a comma; a past and a far-future date; a URL; a line break; pasted rich text. Use only on apps the user owns, with test data.

## 4. Situations to force (not only random clicks)
- Double-click or press Enter twice on every submit; click Submit while it is loading.
- Back and Forward in the middle of a multi-step flow; reload on every step; open the same page in two tabs and change both.
- Go offline mid-save, then online; slow the network.
- Resize from desktop to phone width while a modal is open; rotate.
- Browser zoom 200% and 400%; reduced motion on.
- Open a deep link while signed out; open a link to an item that was deleted.
- Open the app after the session expired.
- Keyboard-only: Tab through the whole page, check the order and that nothing is skipped or trapped.

## 5. Run
1. Start from a known state (fresh profile, same test data).
2. Run the action loop. After every action, check the oracle in section 1; also take a screenshot at every 10th action, and at once when a check fires.
3. When a check fires, stop and write: seed, action number, the last 10 actions, the screenshot, the console and network lines you can see.
4. Replay with the same seed to confirm. If it repeats, shrink: remove actions from the start and middle while the failure stays, until you have the shortest sequence. If it does not repeat, say so and keep the seed.
5. Continue with a new seed. Run at least 3 seeds per main flow in the first round.

## 6. Write it up
Each failure gets: seed, minimal steps, expected versus actual, screenshot, which oracle check, and how many of the seeds hit it. Flaky failures are still findings, labelled "intermittent, seed N". Hand them to [User Testing Findings Report](../user-testing-findings-report/SKILL.md).

## What not to do
- Do not click delete, pay or send buttons in an app you do not own.
- Do not hammer a site with requests; it is a user simulation, not a load test. Use pauses of at least 0.5 seconds between actions on hosted sites.
- Do not count noise: failed requests to third-party trackers or ad hosts are not findings unless the UI breaks.
- Do not call a run clean just because nothing crashed: also check data correctness and focus.
