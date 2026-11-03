---
name: dev-process-state-machine-verification
description: >-
  Use when a system has several modes, timers, pauses or events that can
  interleave (a signal watcher, a game story or cutscene flow, a checkout, a
  trading position) and you want to find bugs by modeling it as a state machine
  and checking it with TLA+.
---

# State machine verification (TLA+)

Part of the [Dev Process playbook](../dev-process-playbook/SKILL.md). Principle: model each tricky system as states and events, write the rules that must always hold, and let a model checker try every order of events and hand back a concrete failing sequence.

## What the source did
One verification skill per major system (story, cutscenes, level-up offers, pause and focus). Each red state in her diagrams was a real bug that TLC (the TLA+ checker) found as a counterexample, for example: an 8 second auto-pick cutting off a story line, an auto-pick firing while the player looked away, an auto-pick pointing at a card from an old hand after a reroll, a pause menu opening over the finale. See the diagrams in the playbook's [references](../dev-process-playbook/references/) folder.

## Steps
1. Name the system and draw it as states (boxes) and events (arrows). Add a paused "needs a person" or "held" state and an exit for every outcome.
2. List invariants ("must always be true") and liveness rules ("must eventually happen"). Example: a timer auto-action never fires while the user is away or while a story beat is playing.
3. Write the TLA+ spec: variables for state, one action per event, the invariants. Keep one spec per subsystem and run them side by side with shared events, like her "at the same time" panels.
4. Run TLC. For each counterexample, write the sequence in plain words, decide the correct behavior, fix the spec, then fix the code.
5. Add a regression test from the counterexample sequence in the real code.
6. Save a per-system skill (`verify-<system>`) holding the spec path, how to run TLC, and how to map spec states to code.
7. Re-run the spec whenever that system changes.

## Tools
TLA+ Toolbox or the `tla2tools.jar` command line (TLC), the VS Code TLA+ extension. Needs Java. A lighter option for small flows is a plain state table plus property tests.

## Signal watcher starter model
States: Idle, TradeSeen, Validated, Queued, Sent, Expired, Dropped, Held. Events: new trade, validate ok or fail, queue full, send ok or fail, timeout, connection lost, replay or reload. Invariants: a signal is sent at most once; an expired signal is never sent; every signal ends in Sent, Expired or Dropped with a logged reason.
