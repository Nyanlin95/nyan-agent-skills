---
name: user-testing-scenarios
description: >-
  Use when turning an app plus a set of personas into concrete user-test
  scenarios and a test matrix (persona by situation by environment), including
  start state, goal, stop condition, success per persona and which cases to run
  first.
---

# User Testing Scenarios

Part of the [User Testing Playbook](../user-testing-playbook/SKILL.md). Personas come from [User Testing Personas](../user-testing-personas/SKILL.md). A scenario is a persona in a situation with a stop condition.

## Scenario template
```
ID: S-01
Persona:
App area / flow:
Start state: (logged out / new account / existing data / mid-flow / offline / stale session)
Environment: (device, viewport, browser, network, locale, theme, input method)
What they want (their words):
What they do first (their likely first move, not the intended one):
Success (from their point of view):
Failure signals (what would make them give up or distrust):
Stop condition: (goal met / patience limit / blocked / reached the confirm step)
Safety: (test data used, what must not be submitted)
Expectation type: (achieve / entertain / explore / compare / recover / random / interrupted / control / included / speed / help / share)
```

## Situations to draw from (pick those that fit the app)
- First visit with no account, and the first 60 seconds after sign-up.
- The main job done start to finish, once on the happy path and once with a wrong turn.
- A mistake: wrong input, wrong item, wrong click, then recovering.
- An empty state, a full state (hundreds of items), and a slow or failing server response.
- Leaving mid-flow and returning: refresh, Back, closing the tab, session expiry.
- Interruption: network drop, device rotation, another tab changing the same data.
- Rarely used but important paths: settings, billing, export, delete account, invite a teammate, error and help pages.
- A shared link opened by a stranger; a link that is stale or has been deleted.
- Permissions: a user who may only view, or who is not invited.
- Content that is long, short, empty, non-Latin, or has emoji.
- Time: a first-time user now versus a returning user later; dates across time zones.
- Entertainment: a session with no goal that should still feel good and have a next thing to do.

## Test matrix
Rows are scenarios; columns are persona, environment, expectation, priority.
1. List the top 3 jobs from intake. Each job gets at least one Achiever scenario and one First-Timer scenario.
2. Add each persona's best-fit situation from the list above.
3. Add environments for risk, not for completeness: one small phone viewport, one desktop, one slow or offline case, one keyboard-only run. Do not multiply every scenario by every environment.
4. Priority: P1 = money, data loss, sign-up or the main job; P2 = common secondary flows; P3 = rare paths. Run P1 first. A first round is about 8 to 15 sessions.
5. Note on the matrix what is deliberately not covered, so the report can say so.

## Writing good scenarios
- Write the want as the persona would say it, not as the feature name. "Find something to give my sister" is a scenario; "use search" is not.
- Never name the buttons in the scenario. The tester finds them or fails to.
- Give each scenario a stop condition and a patience limit; open-ended sessions drift.
- Include the first wrong move a real person would plausibly make; that is where most findings are.
- Keep scenarios independent so a failed one does not block the others; give each its own start state.
- For apps with an assistant or chat, include scenarios where the user is vague, changes their mind, asks for something the product cannot do, and asks for something risky.
