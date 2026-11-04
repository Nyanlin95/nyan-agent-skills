# Running on an agent app with a computer-use subagent

- Browser and desktop work goes to a computer-use subagent (one at a time per desktop; load that environment's desktop skill first). Give it one narrow session at a time: the persona card, scenario, patience limit, safety rules, and what to report (the session log, screenshot paths). It cannot ask questions, so make the brief self-contained.
- Sessions on the agent app's own browser run from the agent app's network, not the user's; for an app on the user's own computer (localhost, internal tool) the user's computer needs to be online and the agent app open, then use Playwright or the app's own tests on that computer.
- Screenshots: take them at each decision and on each problem; store them under `user-testing/<date>-<app>/<session>/` and attach the key ones to the report.
- Chaos runs for web apps on the user's own computer are best scripted (Playwright, seeded random, console and network listeners) and run through a machine shell; browser subagent runs suit manual personas.
- Never place orders, send messages, or sign in with real credentials unless the user supplied a test account for that purpose. Credentials come from the secret store, never typed into a chat.
- Large rounds go to a background worker per workstream; keep to one browser subagent at a time.
- The report: short summary in chat; for a report the person will return to or share, build it as a page the person can reopen (use the agent app's document or canvas skill when it has one) and keep the chat to one or two lines and the link.
- Send nothing to anyone else from a test; keep any message as a draft instead of sending it.
