---
name: dev-process-context-in-file-paths
description: >-
  Use when some code has special rules (runs every frame or tick, touches money,
  must be pure, is generated) and you want the file name or folder to tell
  humans, AI agents and lint rules which rules apply.
---

# Context in file paths

Part of the [Dev Process playbook](../dev-process-playbook/SKILL.md). Principle: encode behavior class in the path, so a lint rule can target it and an agent sees it at a glance.

## Example from the source
Code that runs every frame or tick gets a `.hot.ts` extension. A lint rule bans allocating inside `*.hot.ts` (no object literals, closures, `new`, etc.), so the loop creates almost no garbage and the garbage collector does not cause stutters.

## Steps
1. List the special classes of code in the project. Typical: `.hot` (latency or allocation sensitive), `.pure` (no I/O, no clock), `.gen` (generated, do not edit), `.unsafe` (needs review), `.edge` (talks to the outside world).
2. Pick one suffix or folder per class and document it in `RULES.md`.
3. Add one lint rule per class, scoped by glob to that suffix.
4. Tell the agent in the project instructions: "Files ending in .hot.* must not allocate; files ending in .pure.* must not import I/O or time."
5. Move existing code into the right class one file at a time; every move is a small PR.

## For C# or ATAS
Use a naming suffix or a folder such as `Hot/` for code in trade or order book handlers, and a Roslyn analyzer or CI grep that bans allocation, logging, disk or network calls there.
