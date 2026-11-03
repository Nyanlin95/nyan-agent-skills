---
name: dev-process-everything-as-code
description: >-
  Use when building assets (art, audio, images, translations, share cards) and
  you want them generated from reviewable text files that an AI agent can write,
  diff and test.
---

# Everything as code

Part of the [Dev Process playbook](../dev-process-playbook/SKILL.md). Principle: if an asset can be a text file, make it one. Agents can write it, PRs can diff it and builds can pack it.

## What the source did
- No audio files. Music and sound effects are synthesized live in the browser by a custom Game Boy-style chip (two pulse voices, a wave voice, noise) plus a synthwave layer. Songs are written as text in code. Music transitions between biomes by continuing the previous melody.
- All pixel art is code: each sprite is a file drawn with one shared palette, packed into a sprite atlas at build time.
- Dynamic og:images for every run based on final stats; 10 languages.
- Custom engine for simulation, post-processing and audio; three.js only draws the 3D scene.

## Steps
1. Pick a small text format for the asset (a note list, a pixel grid with palette letters, a JSON layout).
2. Share one palette or one style table so everything stays consistent.
3. Write the build step that packs or renders it.
4. Add a test that the format parses and the output is in budget.
5. Let the agent create new assets by writing files in that format.

## Music angle for you
Songs as text means a pattern or note list plus instrument definitions. A small synth that plays it in the browser is a good side project and ties into your music work.
