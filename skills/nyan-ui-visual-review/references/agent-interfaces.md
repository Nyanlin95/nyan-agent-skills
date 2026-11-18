# Agent Interfaces

Use these checks when guiding or reviewing an AI application surface: turn status, tool steps, diffs, composers, decisions, context usage, and background notices. The patterns are adapted from Solid Glass. Translate them into the project's existing components and visual language; do not require React, shadcn/ui, or Solid Glass packages.

Keep presentation findings here. Report missing events, persisted answers, or submission behavior to the implementation owner rather than prescribing state design.

## Composition

- Keep the answer and message input prominent in the conversation.
- Put current activity beside the work it describes.
- Fold execution detail beneath a concise status or step summary.
- Place decisions where the user can understand their consequences.
- Keep completed work available as a stable record.
- Drive each visible state from real events and data; do not show activity the application cannot observe.
- Reserve continuous motion in the conversation for ongoing work; keep entry, exit, and disclosure transitions in the project's motion language.

## Excluded material treatment

- Do not introduce Solid Glass's cast or inset shadows, luminous rims, specular highlights, glows, glints, reflective gradients, or simulated lighting.
- Do not import its full stylesheet as a shortcut; it includes the excluded treatment.
- Avoid translucent surfaces that make text compete with content behind them.
- Keep ordinary separators, accessible focus indicators, and the project's existing elevation tokens for menus, popovers, and dialogs.
- Search changed and imported styles for `box-shadow`, `shadow-` utilities, `inset` shadows, `drop-shadow`, `backdrop-filter`, `mix-blend-mode`, gradient overlays, and glint or shimmer keyframes.
- Keep a match only when it is a separator, a focus indicator, or a pre-existing project elevation token used for its established purpose.
- Report an introduced excluded effect as **Major** when it affects readability or state meaning, and as **Moderate** otherwise.

## State coverage

- Exercise running, waiting-for-input, stopped-by-user, queued-message, completed, and failed states.
- Check long tool output, long diffs, and narrow viewports.
- Check that streamed output does not pull the scroll position away from a user who has scrolled up to read.

## Activity and turn status

- Show the current activity in words, such as searching, running, writing, or compacting, only when supported by actual events.
- Start elapsed time at the user's submission so the initial wait remains visible.
- Show measured output counts only when available and useful.
- Use tabular numbers for ticking time and counts so the status line does not shift.
- Announce activity changes and the final outcome to assistive technology; do not place ticking time or counts in a live region.
- Make the status summary expandable when it contains tool steps; keep it plain text when there is nothing to open.
- Stop activity motion when work ends and retain a textual outcome.
- When events distinguish kinds of work, give each its own motion, such as thinking, searching, running, writing, or compacting, and transition between them instead of jumping.
- Render the activity glyph in flat color that follows the surrounding text; omit upstream's glow and text glints.
- Hold a static pose plus text under reduced motion.

## Tool steps and diffs

- Group related calls behind a concise summary.
- Label each step by its action and object, such as "Read search.py", rather than exposing raw invocation syntax as the primary label.
- Distinguish running, done, and error outcomes per step.
- Reveal command details, output, errors, or a patch on expansion.
- Keep file identity and hunk context available when displaying changes across files.
- Preserve `diff --git` separators and complete hunk ranges when passing unified patches to a compatible diff component.
- Keep additions and removals understandable through signs or labels as well as color.

## Composer

- Keep attachments or context tags near the draft they affect.
- Place model or message settings beneath the input, separate from draft content.
- Give the textarea itself an accessible name, rather than naming only its wrapper.
- Make send, stop, and queue behavior explicit in the control's current label and action, and show a stopped turn and a queued message as distinct, labeled states.
- Preserve the application's established submission policy during an active turn; do not adopt upstream's queue behavior unless the product supports it.
- Keep a settings trigger's open state perceptible without lighting effects.

## Decisions

- Show a concrete question with choices that communicate their consequences.
- Offer answer actions only while the decision is pending.
- Keep an answered or obsolete question as a readable record without active answer controls.
- Show the selected answer in the retained record.

## Context and background work

- Use a compact context indicator only when usage and capacity are known.
- Reveal numeric usage and its breakdown on demand when the application has that data.
- Choose warning thresholds from the product's actual limits; treat upstream's 70% and 90% thresholds as examples, not universal policy.
- Present background task completion as a compact outcome and task title near the relevant conversation.
- Keep background notices separate from the active turn's status so one task ending does not imply all work has ended.

## Optional explanation disclosure

- Keep product-provided explanations or summaries collapsed when they would crowd the answer.
- Render only explanation content deliberately exposed by the product's API; do not fabricate or request private model reasoning to fill an upstream `Reasoning` component.

## Source and adaptation boundary

Ground these patterns in [deeplethe/solid-glass](https://github.com/deeplethe/solid-glass/tree/6e8903e494a15491ceda38fafea5056c95a74d44), inspected on 2026-11-18. Treat the following as source documentation rather than a dependency or a claim about future releases:

- [Introduction](https://github.com/deeplethe/solid-glass/blob/6e8903e494a15491ceda38fafea5056c95a74d44/content/docs/introduction.mdx) and [Material](https://github.com/deeplethe/solid-glass/blob/6e8903e494a15491ceda38fafea5056c95a74d44/content/docs/material.mdx): retain readability, restrained state signaling, and meaningful motion; omit the material rendering recipe.
- [Component usage documentation](https://github.com/deeplethe/solid-glass/tree/6e8903e494a15491ceda38fafea5056c95a74d44/content/solid): consult `turn-status`, `status-glyph`, `tool-steps`, `diff-view`, `composer`, `ask-card`, `context-ring`, `task-notice`, and `reasoning` for the respective patterns above.

Treat accessible state labels, live-region scope, scroll anchoring, retained answer history, product-specific thresholds, and the explanation-content boundary as adaptations in this reference rather than guarantees made by upstream. Recheck installed source and current documentation before relying on a library-specific API or importing an upstream component; inspect its styles for excluded effects.
