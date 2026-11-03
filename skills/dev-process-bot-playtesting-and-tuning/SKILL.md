---
name: dev-process-bot-playtesting-and-tuning
description: >-
  Use when a system has tunable difficulty or parameters (game balance, alert
  thresholds, strategy settings) and you want automated bots or replays to tune
  them toward target outcomes.
---

# Bot playtesting and tuning

Part of the [Dev Process playbook](../dev-process-playbook/SKILL.md). Principle: let automated players run the thing headless thousands of times and tune settings to hit a target number, instead of tuning by feel.

## What the source did
Bots play the game headless to tune each difficulty against target survival rates.

## Steps
1. Write down the target outcome per setting (for example: easy 80% survive, hard 20%).
2. Build a headless runner that needs no UI and runs fast on the deterministic core (see [Deterministic core and replay](../dev-process-deterministic-core-and-replay/SKILL.md)).
3. Write a simple bot (random plus a few heuristics) and, if useful, a skilled bot.
4. Run many seeded games per setting; report the outcome rate and its spread.
5. Adjust parameters until each setting meets its target. Commit the result and the target as a test.
6. Re-run on every balance change.

## For a signal watcher
The bot is a replay of recorded market days. The targets are things like signals per day, false-signal rate and signal delay. Tune thresholds on some days and check them on other days.
