# Source thread (lauren / @poteto), posted 2026-11-01

This file quotes a third-party X thread. It is source material for the playbook.

- Author: lauren (@poteto)
- Source URL: https://x.com/poteto/status/2117043478140276847
- Posted: 2026-11-01
- Parent: https://x.com/poteto/status/2117004709198475365 ("Day 28 / tibo's game has landed", https://tibo.dog)
- Evidence: initial commit by cursoragent and poteto on Oct 28, 2026, 9:07 PM PDT.

trivia:

- started working on the game as a side project 4 days ago, landing ~1,150 PRs
- every time i found an issue in the code i asked bot to make a lint rule against it
- used TLA+ heavily to find bugs in the game's various state machines: the story, cutscenes, the game's systems. there are many formal verification skills, one for each major system
- i put context into the filepaths: code that runs every frame or every tick gets a .hot.ts extension, and a lint rule bans allocating in it (no object literals, closures, new, etc.), so the game loop creates almost no garbage and GC doesn't cause stutters
- game engine is mostly custom. three.js draws the 3D scene, but the simulation, post-processing and audio are all ours
- the simulation is fully deterministic, so every run replays exactly from its inputs. when you post a high score, the server replays your whole run to check it isn't cheated
- we generate dynamic og:images for every run based on your final stats, and it's all localized too! the game supports 10 languages
- my favorite feature: the music seamlessly transitions into different music for the various biomes, continuing the previous melody
- no audio files. all the music and sound effects are synthesized live in the browser by a custom Game Boy-style chip (two pulse voices, a wave voice, noise) plus a synthwave layer. the songs are written as text in code
- all the pixel art is code. every sprite is a file drawn with one shared palette and packed into a sprite atlas at build time
- it runs inside an X post, from the 245px card up to full screen. the bar is 60 fps with 500 enemies on a mid-range phone
- the build fails if the first download goes over budget. it's about 124 KB gzipped right now
- bots play the game headless to tune each difficulty against target survival rates
- comments are banned by a lint rule. if code needs explaining, the fix is a better name or a test

## Diagram notes (images in this folder)
Title: "Bugs TLA+ caught in tibo.dog story mode". Red states are rule violations TLC found, each ending in a real counterexample. Numbered bugs with PR numbers:
1 A slow load froze the landing with no line on screen (#943)
2 Tibo got up behind the loading screen while WebGL was lost (#1080)
3 The gear chest gave Tibo a second Peeler, via a Grok Bot level-up before (#1092 / #933)
4 The 8 s auto-pick cut poteto's level-up lesson (#1191)
5 The auto-pick picked while you looked away, and the run played on (#1191)
6 After a reroll, the auto-pick pointed at a card from the old hand (#1191)
7 amusing's entrance ran on behind the loading screen (#1013)
8 After her lines failed to load, the next run froze at her bonk (#988)
9 The pause menu opened over poteto's finale line (#988)
10 Her evil laugh kept shaking the screen under the focus pause (#1094)
11 After Reset run?, her half-typed line stayed on the splash (#929)
(Numbers read from a small screenshot; check against the image if exact wording matters.)
Panels run "at the same time": Story (wake up, grab chest, zombies, boss amusing, alex, poteto's visit, the end), Lines, Pause (playing, held, away from the cards, focus pause, reset splash), Offer (no offer, gear panel, her lesson over the cards, 8 s count then auto-pick).
