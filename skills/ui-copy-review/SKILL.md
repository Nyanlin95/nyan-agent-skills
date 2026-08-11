---
name: ui-copy-review
description: Reviews UI copy and related accessibility. Use for microcopy, labels, instructions, errors, empty states, accessible names, status messages, and localized copy. Also use for a pull request, diff, staged change, or working-tree change that changes user-facing text. Resolves the change scope, compares old and new copy, inspects affected states, and classifies findings. This skill is read-only and is not a complete accessibility audit.
---

# UI Copy Review

Review the language that helps users understand state, make decisions, complete actions, and recover from problems.

Treat writing as interface behavior, not decoration.

Keep this review read-only. Recommend exact replacement copy only when the evidence supports it.

Do not edit files unless the user authorizes implementation.

## Keep the boundary clear

Own UI writing where language affects meaning or operation.

Review visible text, accessible names, descriptions, instructions, validation, errors, status messages, confirmations, recovery text, and text alternatives.

Do not claim a complete accessibility audit.

Route unrelated keyboard, focus, contrast, semantics, motion, zoom, or layout failures to an accessibility or visual review.

Report a correctness, security, legal, or product-policy concern once. Assign it to its owner.

Do not use this skill for documentation, release notes, code comments, or long-form technical prose.

## Resolve the review target

Interpret everything after an optional `quick` or `full` mode as the target.

- **Quick:** Review the changed copy and its directly affected state. Report at most five findings.
- **Full:** Inspect relevant sibling states, consumers, localization resources, and available accessibility evidence. Report at most ten findings.

Use `quick` for a supplied string, screenshot, component, or narrow file set.

Use `full` for a branch, pull request, route, or workflow. Do not fill the finding cap.

Accept an explicit pull request, branch, commit range, staged changes, working-tree changes, named files, screenshot, route, or supplied copy inventory.

When the target is Git work and the user gives no range:

1. Resolve the remote default branch from `refs/remotes/origin/HEAD` when available.
2. Compare `HEAD` with its merge-base against the resolved remote default branch.
3. Include commits ahead of that merge-base and report uncommitted changes separately.
4. Use uncommitted changes alone when `HEAD` is not ahead and the working tree is dirty.
5. Use `HEAD~1..HEAD` only as a stated fallback.

If the remote default branch is unavailable, report the limit.

Use the dirty working tree or `HEAD~1..HEAD` as the stated fallback. Do not guess a branch name.

For a pull request, inspect its title, body, commits, base ref, and head ref. Inspect the linked issue when available.

Do not check out the pull request. Fetch a ref only when needed and report the `.git` write.

If required evidence is unavailable, state the limit. Do not silently review the current checkout instead.

For working-tree targets, distinguish staged, unstaged, and untracked files.

Do not claim to have reviewed an untracked file unless you opened it.

Do not check out, switch, reset, stash, or otherwise rewrite the user's working tree.

Exclude generated output, vendored code, binaries, snapshots, and lockfiles. Report each exclusion.

## Expand changes into interface states

Treat a changed string or file as evidence, not the whole review surface.

1. Read both the added and removed sides of each relevant diff.
2. Read the stated change intent from the request, pull request, issue, or commit message when available.
3. Identify the component, route, message catalogue, schema, or service that owns the copy.
4. Expand to direct rendered consumers.
5. Inspect sibling states that can change the reviewed language.
6. Inspect localization resources when the project maintains them.
7. Limit expansion to five representative consumers unless product risk requires more.
8. Name consumers and states that remain uninspected.

Use rendered evidence when it is easy to get or the user requests it.

Require rendered or accessibility-tree evidence for placement, reading order, truncation, accessible names, descriptions, and announcements.

Treat source attributes and string presence as leads, not runtime proof.

## Review the copy

Read [references/review-criteria.md](references/review-criteria.md) before judging findings.

Test whether each relevant message:

1. Appears at the moment the user needs it.
2. Names the object, action, or state precisely.
3. Uses the product's established terminology.
4. Helps the user predict the result of an action.
5. Explains a problem without blame.
6. Gives a specific next action when recovery is possible.
7. Distinguishes destructive, irreversible, or externally visible effects.
8. Remains understandable without relying on position, shape, color, or icon alone.
9. Gives assistive technology an equivalent name, description, state, and update.
10. Remains useful when translated, wrapped, truncated, or read out of visual context.

Preserve the user's voice and the product's terms.

Do not replace specific language with generic friendly language.

Do not remove information needed for confidence, consent, or recovery.

## Classify findings

Give every finding one change status when comparison evidence exists:

- **Introduced:** The reviewed change created the problem.
- **Regression:** The change removed or weakened language that previously worked.
- **Pre-existing:** The problem is visible in an affected surface but was not caused by the reviewed change.
- **Unclassified:** No reliable base evidence exists. Use this status when you cannot establish the source history.

Give every finding one severity:

- **Critical:** Language can cause an irreversible, unsafe, unauthorized, or materially wrong action.
- **Major:** Language blocks task completion, hides essential state, or prevents recovery or accessible operation.
- **Moderate:** Language creates meaningful ambiguity, hesitation, inconsistency, or avoidable error.
- **Minor:** Language has a small clarity or consistency defect with limited task impact.

Label evidence as **Observed** or **Inferred**. Give each inferred finding a High, Medium, or Low confidence level.

Do not report a regression when the change provides an equivalent replacement.

Use introduced findings and regressions to decide if the change can proceed. Report pre-existing findings separately.

Do not block the change for a pre-existing finding unless the change depends on that defect.

Explain the dependency when it occurs. Do not reclassify an unclassified finding without base evidence.

## Write actionable findings

For each finding, state:

- Status, severity, and evidence confidence.
- Location and affected interface state.
- Current or removed copy.
- User consequence.
- Writing or accessibility rule that fails.
- Owning component or resource when known.
- Recommended replacement or structural correction.
- Verification method.

Check surrounding language, product terms, behavior, and character limits before you recommend exact copy.

Use a copy pattern when the final text depends on runtime data.

Consolidate repeated symptoms under one owner. Do not manufacture findings to fill a quota.

## Report

Lead with what the changed copy does well. Then report:

1. **Scope:** Target, base and head refs when applicable, files, exclusions, expanded consumers, and unavailable evidence.
2. **Summary:** User task, copy intent, strongest quality, highest-risk weakness, and first action.
3. **Priority findings:** Order by severity and task impact.
4. **Copy changes:** Use a `Current | Recommended | Why` table for meaningful replacements.
5. **Accessibility judgment:** State what copy-related accessibility was checked and what requires a broader audit.
6. **Verification:** List completed and unavailable rendered, assistive-technology, localization, and state checks.
7. **Verdict:** End with `Block`, `Needs changes`, `Evidence incomplete`, `Approve with follow-ups`, or `Approve`.

Use `Block` when a Critical introduced finding or regression remains.

Use `Needs changes` when another required introduced finding or regression remains.

For a baseline review, apply these verdicts to required unclassified findings. Do not attribute these findings to a change.

Use `Evidence incomplete` when required writing or accessibility evidence is unavailable.

Use `Approve with follow-ups` when only bounded or pre-existing improvements remain.

Use `Approve` only when no actionable finding remains. Verify all material coverage before you use this verdict.
