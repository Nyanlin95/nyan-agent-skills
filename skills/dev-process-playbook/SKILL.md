---
name: dev-process-playbook
description: >-
  Use as the starting point when setting up or improving how a software project
  is built with AI agents: turning bugs into lint rules, verifying state
  machines with TLA+, deterministic replay, build budgets, bot playtesting. It
  routes to the linked Dev Process skills and holds the source reference
  material.
---

# Dev Process Playbook (meta skill)

A way of working distilled from lauren's ([@poteto](https://x.com/poteto/status/2117043478140276847)) thread about building tibo.dog, a full game, in 4 days with about 1,150 PRs, using coding agents. The core idea: the AI writes the code, and the project's own automated checks keep it correct. Every lesson becomes a rule, a test or a spec, never a memory.

## The loop
1. Build a small slice with the agent.
2. Something breaks or looks off.
3. Fix it, then ask: what check would have caught this? Add it (lint rule, test, TLA+ invariant, budget).
4. The next agent run starts with that check already in place.

## The linked skills
| When | Skill |
| --- | --- |
| You found a bug or a repeated AI mistake | [Bug to Lint Rule](../dev-process-bug-to-lint-rule/SKILL.md) |
| Some code has special rules (hot loop, pure, generated) | [Context in File Paths](../dev-process-context-in-file-paths/SKILL.md) |
| A system has modes, timers, pauses, interleaving events | [State Machine Verification](../dev-process-state-machine-verification/SKILL.md) |
| You need reproducible runs or verifiable results | [Deterministic Core and Replay](../dev-process-deterministic-core-and-replay/SKILL.md) |
| Speed, size or latency must not regress | [Budgets That Fail the Build](../dev-process-budgets-that-fail-the-build/SKILL.md) |
| You have settings to tune toward a target | [Bot Playtesting and Tuning](../dev-process-bot-playtesting-and-tuning/SKILL.md) |
| You make art, audio, cards or text assets | [Everything as Code](../dev-process-everything-as-code/SKILL.md) |

## Bootstrapping a new project (order matters)
1. Create `RULES.md` and `AGENTS.md` with the rule log and the naming conventions.
2. Add CI with lint, tests and one budget from day one.
3. Keep the core pure and deterministic from the first commit; it is hard to add later.
4. Ship tiny PRs. Each PR is one slice plus the check it needed.
5. Ban comments by lint rule: explain with names and tests.
6. For each risky subsystem, write a state machine and a `verify-<system>` skill.

## Other habits from the thread
- Small side projects get a hard deadline and are shipped in public.
- The custom engine owns simulation, audio and post-processing; a library only draws.
- It runs inside an X post, from a 245px card up to full screen, so the layout is tested at both sizes.
- Localized in 10 languages from the start, including the share images.

## Applying it to a signal watcher (ATAS X)
1. Rule: ban `DateTime.Now` and `DateTime.UtcNow` for trade age; use the platform `MarketTime` (see the ATAS Developer API time docs: https://docs.atas.net/en/chart-indicators/sessions.html).
2. Hot path: mark handlers that run per trade or per order book change, and ban slow work there.
3. State machine: model signal life (seen, validated, queued, sent, expired, dropped, held) and check it.
4. Replay: record the market stream and replay it in tests.
5. Budget: fail the tests if p99 trade-to-signal time goes over the limit.
6. Tune thresholds on replayed days.

## References
Files in the reference folder of this skill (`references/`):
- [source-thread.md](references/source-thread.md): the full thread text.
- [tla-bugs-overview.jpg](references/tla-bugs-overview.jpg), [tla-closeup.jpg](references/tla-closeup.jpg), [story-state-machine.png](references/story-state-machine.png): her state machine diagrams and the bugs the checker found.
- [signal-watcher-state-machine.md](references/signal-watcher-state-machine.md): a starter model for the watcher.
