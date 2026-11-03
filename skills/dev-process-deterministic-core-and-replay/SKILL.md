---
name: dev-process-deterministic-core-and-replay
description: >-
  Use when you want bugs reproducible, results verifiable or cheating
  detectable: make the core logic deterministic so a run replays exactly from
  its recorded inputs.
---

# Deterministic core and replay

Part of the [Dev Process playbook](../dev-process-playbook/SKILL.md). Principle: same inputs give the same run, always. Then any bug can be replayed and any claimed result can be checked.

## What the source did
The game simulation is fully deterministic. When a player posts a high score, the server replays the whole run from its inputs to check it is not cheated.

## Steps
1. Separate the pure core (state in, event in, state out) from the edges (clock, random, network, UI).
2. Inject time and randomness. Never read the wall clock or a global random inside the core; pass in a time value and a seeded random generator.
3. Record every input with its timestamp: events, seed, config version.
4. Write a replay tool: feed the recording through the core and compare outputs.
5. Make replay a test: keep recordings of past bugs as fixtures that must pass forever.
6. Verify claims server-side by replaying them (scores, signals, fills).

## For a signal watcher
Record the raw trade and order book stream (with `trade.Time` and the platform market time, not the PC clock). Replay it through the watcher in tests to reproduce a late, dropped or duplicated signal exactly, and to compare changes to the rules before using them live.
