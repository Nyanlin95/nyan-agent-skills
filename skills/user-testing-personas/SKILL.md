---
name: user-testing-personas
description: >-
  Use when choosing or writing the simulated users for a user test: a library of
  personas (goal-driven, bored, curious, impatient, random clicker, first-timer,
  keyboard-only, mobile, skeptical, adversarial and more) and how to adapt them
  to a specific app and audience.
---

# User Testing Personas

Part of the [User Testing Playbook](../user-testing-playbook/SKILL.md). A persona is a **want, a state of mind, and a behaviour rule**. It is never a demographic description alone.

## Persona card (write one per persona)
```
Name / label:
Who they are (one line, plain):
What they want right now (one sentence, in their words):
Why it matters to them / what happens if it fails:
State of mind: patience (seconds before giving up), tech skill (low/med/high), attention (focused / distracted)
Behaviour rules: how they decide where to click, what they read, what they ignore
Expectation they judge by: (from the playbook list)
Stops when: (goal met, gave up, bored, blocked, got what they came for)
Never does: (what they would never do, so the tester stays in character)
```
Rules: one want per persona; give a patience number so "gave up" is a decision, not a feeling; give a "never does" so the tester cannot drift into a power user.

## Persona library (pick and adapt; add your own)
1. **The Achiever (goal-driven).** Has a task and a deadline. Reads headings and buttons only, takes the shortest visible path, hates extra steps. Patience about 30 seconds per step. Judges: did I finish, how fast, was anything wrong.
2. **The Entertainer (bored, killing time).** No goal. Follows whatever looks interesting, scrolls, taps animations, watches for delight. Leaves when it feels like work. Judges: is it fun, is it smooth, is there something to do next.
3. **The Explorer (curious).** Wants to understand what this is. Opens every menu, reads tooltips, tries settings, goes back often. Judges: is it clear, can I undo, am I safe.
4. **The Random Clicker.** Clicks and taps everywhere with no plan, double-clicks, clicks during loading, presses Back, Escape, Enter and Tab randomly. Run this one with the chaos skill ([Chaos and Random Input](../user-testing-chaos-and-random-input/SKILL.md)). Judges: does anything break or lose data.
5. **The First-Timer (novice).** Has only the one-line pitch. Does not know the app's vocabulary, reads literally, misses small links, gets lost, and does not know what an icon means. Judges: could I figure it out alone.
6. **The Skimmer (impatient).** Gives up after about 8 seconds of confusion or 3 seconds of waiting. Skips text, closes pop-ups, ignores tutorials. Judges: first impression and speed.
7. **The Distracted Multitasker.** Starts, switches tabs, comes back minutes later, loses connection, rotates the phone, gets a call. Judges: does it keep my place, does it recover.
8. **The Power User (keyboard first).** Expects shortcuts, tab order, bulk actions, search, undo. Judges: efficiency and consistency.
9. **The Skeptic (trust and privacy).** Reads permissions, pricing, terms, cookie banners. Refuses anything that feels pushy. Judges: honesty, no surprise charges, easy opt-out.
10. **The Comparer (evaluator or buyer).** Weighs this against alternatives, checks price, reviews, shipping, refund, proof. Judges: information completeness and confidence.
11. **The Accessibility User.** Keyboard only, then screen reader semantics, 200% and 400% zoom, reduced motion, high contrast. Judges: can I do the main job without a mouse or sight.
12. **The One-Thumb Mobile User.** Small screen, slow network, thumb reach, on the move. Judges: targets, readability, load time, forms.
13. **The Returning User with stale state.** Comes back after weeks, old session, old data, changed settings. Judges: does it welcome me back correctly.
14. **The Wrong-Audience Visitor.** Arrived by mistake or from an ad with a different expectation. Judges: do I understand in 5 seconds whether this is for me.
15. **The Non-Native or Different-Locale User.** Other language, date and number formats, long words, right-to-left text. Judges: is anything cut off or confusing.
16. **The Rule-Breaker (adversarial, owner-approved only).** Pastes very long text, special characters, emoji, script tags, negative numbers, empty fields, repeated submits, stale links, someone else's id. Judges: does it fail safely. Only on an app the user owns, on test data.
17. **The Helper-Seeker.** Gets stuck on purpose to see what help exists: error messages, support, docs, chat.
18. **The Sharer.** Shares or exports something and opens it as a stranger. Judges: does the shared view work without sign-in or leaking private data.

Add domain personas when the audience needs them, such as a store owner, a teacher, a parent, a trader, a child, an admin, a team member who was invited. Take them from the app's real users when you can.

## How to adapt personas to an app
1. From the intake, list the real audiences and their top jobs. Make at least one persona per audience.
2. For each library persona, rewrite the "want" in this app's terms (for a shop: "buy a gift under 30 before tonight"; for a chat tool: "get an answer from the assistant without learning commands").
3. Choose the mix by risk: money or data loss means more Achiever, Skeptic and Rule-Breaker; entertainment or content means more Entertainer and Skimmer; onboarding means First-Timer and Wrong-Audience; internal tools mean Power User and Helper-Seeker.
4. Cap at about six per round. More personas with shallow sessions find less than fewer personas with real sessions.

## Staying in character
- Decide each action from the persona card and what is visible on screen, not from knowledge of the code or the builder's intent.
- If the persona would not notice a thing, do not use it. If the persona would be stuck, be stuck: wait the patience time, try what they would try, then record "gave up" with the reason.
- For the First-Timer, do not use the map notes from intake.
- When a persona ends (goal met, gave up, bored), say which and why.
