# UI copy and accessible-language criteria

Use only the sections relevant to the changed interface states. Prefer product evidence over universal tone rules.

## Controls and navigation

- Name the action or destination, not the control's appearance or location.
- Use the same term for the same object and different terms for different effects.
- Distinguish navigation, selection, filtering, submission, saving, publishing, and destructive actions.
- Make visible labels and accessible names equivalent in meaning.
- Give icon-only controls an accessible name that describes their effect.
- Avoid repeating the control type in its name when the platform already announces it.
- Avoid ambiguous labels such as `Continue`, `Manage`, `Submit`, `Yes`, or `OK` when a more specific action matters.

## Forms and validation

- Put persistent instructions before the user needs them.
- Use labels to name requested data.
- Do not use placeholders as the only label.
- State required format or constraints before submission when users can act on them.
- Identify the field, problem, and correction in validation messages.
- Preserve entered data after a correctable failure.
- Check whether instructions and errors have programmatic control associations.
- Require DOM or accessibility-tree evidence before you confirm an association.
- Do not rely on color, position, or an icon alone to communicate validity.

## Errors and recovery

- State what failed in terms the user recognizes.
- State whether the user's work was saved, sent, charged, published, or otherwise applied.
- Give the next safe action when recovery is available.
- Distinguish retryable, permission, offline, validation, conflict, and permanent failures.
- Do not blame the user or expose internal implementation details.
- Do not promise success, timing, or data safety that the system cannot confirm.
- Keep support identifiers copyable and secondary to recovery guidance.

Prefer this structure when each part is known:

`[What happened]. [Effect on the user's work]. [What to do next].`

## Empty, loading, and status states

- Distinguish an empty collection from no search results, filtered-out results, missing permission, loading, and failed loading.
- State what belongs in the empty region and how to create or find it when that action is available.
- Use loading language only when it adds information beyond an existing progress indicator.
- Check announcements for important asynchronous state changes. Make sure these announcements do not move focus without a reason.
- Require runtime accessibility evidence before you confirm this behavior.
- Avoid success messages that repeat visible state without confirming a consequential result.
- Keep live-region messages concise and prevent repeated announcements during frequent updates.

## Confirmation and destructive actions

- Name the affected object and consequence.
- State whether the action is reversible and how recovery works.
- Use a specific action label such as `Delete project`, not `Confirm`.
- Do not use alarming language for routine reversible actions.
- Do not hide destructive consequences in secondary text when the button label can state them.
- Distinguish removing access, deleting data, archiving, disconnecting, and signing out.

## Accessible names and descriptions

- Check that each relevant interactive element has a stable and meaningful accessible name.
- Require computed accessibility evidence before you confirm the name.
- Keep the visible label inside the accessible name when speech-input users need to name the control.
- Use descriptions for extra instructions, not to repair an unclear name.
- Include state only when the platform or semantic role does not already expose it.
- Give repeated controls enough context to distinguish their targets.
- Give an image meaningful alternative text only when it conveys information.
- Use empty alternative text for a decorative image.
- Avoid duplicating nearby visible text in alternative text.

## Tone and comprehension

- Lead with information needed for the next decision.
- Prefer concrete verbs and familiar nouns.
- Use short sentences, but retain information required for consent, trust, or recovery.
- Avoid jokes, idioms, blame, false urgency, and emotional language in failure or high-risk states.
- Match the product's established voice without sacrificing clarity.
- Address the user directly only when it makes responsibility or the next action clearer.
- Avoid internal names, implementation terms, and unexplained abbreviations.

## Localization and resilient copy

- Avoid concatenated fragments and grammar that depends on variable order.
- Use full messages with named interpolation variables.
- Support plural, gender, number, date, time, and currency rules through the project's localization system.
- Allow text growth without losing meaning or hiding the action.
- Avoid embedding meaningful text in images.
- Check that translators receive enough context to distinguish nouns, verbs, and interface states.
- Treat a missing catalogue entry or fallback to developer text as a finding when localization is supported.

## Evidence and restraint

- Confirm behavior and terminology from the interface, code, product model, tests, or documentation.
- Mark placement, truncation, reading order, and announcement claims unverified when no render or accessibility-tree evidence exists.
- Preserve legally reviewed, consent, privacy, security, and regulated language unless the authorized owner approves a change.
- Report a suspected legal or policy problem to its owner.
- Do not rewrite it as ordinary microcopy.
- Do not enforce a personal style preference when both versions are clear, consistent, accessible, and appropriate.
