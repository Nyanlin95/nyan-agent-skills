# Environment adapter (what to look for in any agent setup)

The skills assume the agent can do these things. Check what you have, and say what is missing in the report.

| Need | Ways to get it |
| --- | --- |
| Drive the app like a person (click, type, scroll, keys, resize, back) | A browser the agent can control, a device or emulator, a UI automation tool, or a computer-use subagent |
| See the screen | Screenshots on every step; an accessibility tree or DOM read as a second view |
| Read errors | Browser console and network panel, app logs, server logs for a local build |
| Control the start state | Fresh browser profile, seeded test data, a reset script |
| Network and device conditions | Browser devtools throttling and offline mode, viewport size, zoom, reduced-motion setting |
| Repeat a run | Seeded random generator; a saved action list |
| Run in parallel | Separate browser profiles or devices, separate test accounts |
| Keep evidence | A folder of screenshots named by session and step; the session log file |

If a capability is missing (for example no console access), say so in the report and lower confidence on findings that needed it.
If the app is on the user's own computer, a local run uses that computer's browser and files; a hosted app can be tested from anywhere. Prefer local or staging builds for anything destructive.
