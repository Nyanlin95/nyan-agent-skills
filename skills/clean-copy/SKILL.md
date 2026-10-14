---
name: clean-copy
description: Cut interface copy that does not need to exist. Use when writing UI strings, tightening existing copy, or deciding whether a user-facing string should stay. Apply to labels, hints, empty states, toasts, confirmations, button text, and similar microcopy. Do not use to review changed copy, accessibility, localization, or interface states; use ui-copy-review.
---

# Clean Copy

Decide whether the string belongs before you improve its wording. Polishing unnecessary copy only makes it sound better. Remove copy that creates questions instead of answering them.

## Decide whether it belongs

Walk through these checks in order. Stop when a check shows that the string should go.

1. Ask whether the user needs the fact to understand a state, choose an action, or complete a task. If not, remove it. Do not surface a fact the user would not have wondered about if it adds no useful decision information.
2. Compare the string with nearby labels, values, fields, and controls. Remove text that repeats them. Keep units, scale, or format needed to interpret a value.
3. Check whether the string warns against a failure that no longer occurs, defends a design decision, or repeats engineering history. Remove that copy after the behavior works. Keep current limitations and consequences the user needs.
4. Remove the unnecessary clause. If nothing useful remains, remove the hint or explanatory element. Remove an empty `hint` prop instead of shortening it.

Examples:

- `Retry limit` already labels the field. Remove `How many times we retry.`
- Keep `seconds` beside a bare value such as `30`.
- After fixing a cancel bug, show `Cancel upload` without a reassurance paragraph about keeping transferred files.

## Keep what supports a decision or recovery

- Keep a real consequence under a destructive action when the user cannot infer it. For example: `Anything not yet synced is lost.`
- Keep a compatibility or scope fact the user cannot see. For example: `Works with keys issued after March. Rotate older keys first.`
- Explain what a blank state means and how to continue. For example: `No projects yet. Create one and it will appear here.`
- Keep units, scale, or format needed to understand a bare value.
- Preserve accurate limitations, consent, safety, privacy, legal, and security information. Do not remove copy required for an informed action.

## Work on strings in context

- Read each string beside its label, value, field, button, and nearby copy. Judge redundancy in context.
- Cut whole clauses before trimming individual words.
- Report a batch as `file:line` with the current string and either a replacement or `cut`. Name the failed check in a few words.
- Leave copy that passes the checks unchanged.
- If useful copy applies only to a rare state, recommend showing it in that state instead of keeping it on the page at all times.
- Use `ui-copy-review` for accessibility, localization, state, or rendered-behavior questions. Do not claim those checks from source text alone.

## Verify in the rendered state

1. Open the running interface, a preview, or a screenshot that shows each changed string.
2. Check each string in the state where it appears, such as empty, error, loading, or confirmation.
3. Confirm the string fits its container without truncation or an unexpected wrap.
4. Confirm the user can still understand the state and the next action without the removed text.
5. Report each string you could not render as `unverified` with the reason.

Do not claim a cut is safe from source text alone.
