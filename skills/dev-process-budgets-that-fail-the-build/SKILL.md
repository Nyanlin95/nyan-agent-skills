---
name: dev-process-budgets-that-fail-the-build
description: >-
  Use when performance, size or latency matters and you want a hard limit
  checked automatically (bundle size, frame rate, handler time, memory) so
  regressions fail CI.
---

# Budgets that fail the build

Part of the [Dev Process playbook](../dev-process-playbook/SKILL.md). Principle: a number you do not enforce will drift. Put the limit in CI.

## What the source did
The build fails if the first download goes over budget (about 124 KB gzipped). The bar for speed is 60 fps with 500 enemies on a mid-range phone.

## Steps
1. Pick one or two numbers that matter and a reference device or setup.
2. Write a script that measures them and exits non-zero over the limit.
3. Run it in CI on every PR and print the current value next to the limit.
4. Set the limit slightly above today's value, then tighten as you improve.
5. When a PR must go over, the owner raises the limit on purpose, in the diff.

## Examples
- Web or game: gzipped first-load size, frame time with a fixed scene.
- Signal watcher: p99 time from trade arrival (`MarketTime`) to signal sent, handler time per trade, and queue depth. Fail the test run when a replayed day exceeds the budget.
