# Review modes

## Chat mode (default)

Present the review in the same chat the author invoked `/vision` in. Do not
open a webpage unless they ask for the web board.

- Send the full draft as one ordinary chat message first (markdown, `#`/`##`
  headings, one sentence per line), so it stays visible above the questions.
- Then ask the hypotheticals with the host's native ask-user tool, batching to
  that tool's limits. Every hypothetical uses the options Accept, Resist, and
  Depends, plus a free-text reason (a notes field, the tool's built-in Other,
  or a typed answer). Map those options to In vision / Off mission /
  Conditional. Each question's prompt carries the id, title, the concrete
  proposal, the tested principle (quoted from the draft), and a one-line
  steelman for each side.
- Known host limits (prefer the live tool schema if it differs):
  - **Claude Code / T3 Claude:** `AskUserQuestion` - at most 4 questions per
    call, 2-4 options each. "Other" is added by the tool for free text; do not
    add an Other option yourself. Batch 8-12 hypotheticals into two or three
    calls (for example 4+4+rest). T3 shows these as question cards in the same
    thread.
  - **Codex / T3 Codex:** Use `request_user_input` in Plan mode (up to 3
    questions per call), or `request_user_input_async` when available in Default
    mode. Follow the live tool limits. Use the client-provided free-text option.
    Wait for the author's reply before advancing. Use the same-chat plain-text
    fallback if neither tool is available.
  - **Grok Bot:** question cards with one step per hypothetical, at most 8
    steps per card, so 8-12 hypotheticals take two cards. Each step's prompt
    carries the id, title, the concrete proposal, the tested principle (quoted
    from the draft) and a one-line steelman for each side. Options: "Yes,
    accept it", "No, resist it", "Depends"; allow a typed answer for the
    reasoning. Keep options real verdicts; the card's own Skip covers
    skipping. If the host running the skill cannot show cards itself (for
    example a coding agent on another machine), it returns the draft and the
    hypotheticals as plain text to the chat assistant, which shows the cards
    and passes the verdicts back verbatim.
  - **Other hosts:** use whatever ask-user or pending-input tool the host
    exposes, batched to its documented limit, with the same Accept / Resist /
    Depends options and a free-text reason.
- If the host has no ask-user tool, or the tool cannot be used in this mode,
  fall back in the same chat: after the draft message, send a numbered
  plain-text list of the remaining hypotheticals. Each item includes the id,
  title, proposal, quoted principle, and both-sides steelman, and asks the
  author to reply once in the form `1 Accept, because ...`, `2 Resist,
  because ...`, or `3 Depends, because ...`. Wait for that reply. Do not open
  the web board.
- On each batch: fold the author's reasoning into the draft so the vision
  document stays self-sufficient for an accept/resist test. Write it in
  whatever form reads best; do not copy the hypothetical, the card id, or the
  transcript. Never write an answers file into the target repo. Then send the
  revised draft and a changelog line per verdict ("H-7 Resist -> authority
  section now opens with ..."). If more hypotheticals remain, ask the next
  batch in the same way. After the last batch, ask in the same chat whether
  to approve the draft, continue with more hypotheticals, or stop.
- A skipped, dismissed, or unanswered item is no verdict, not approval. Do
  not approve on the author's behalf. Do not treat silence as approval.

## Web board mode (opt-in, lavish-axi from the shipped template)

- Copy [review-template.html](../assets/review-template.html) and
  [review.css](../assets/review.css) into the tool's scratch area. Fill only the
  project name, run note, draft Markdown, and cards slots using the escaping
  and serialization instructions in the template. Use `id`, `title`, `body`,
  `tests`, and `why` for each card.
- Change nothing else: the template already carries the house structure -
  full draft on the left, one card at a time on the right, the steelman in
  full view, one queued verdict per card - so no boilerplate is rewritten and
  no run is restyled.
- Launch with `npx -y lavish-axi <board.html>`, report the URL, then wait on
  `npx -y lavish-axi poll <board.html>`; answers arrive as queued verdicts.
- On each batch: fold the author's reasoning into the draft so the vision
  document stays self-sufficient for an accept/resist test. Write it in whatever form
  reads best; do not copy the hypothetical, the card id, or the board
  transcript. Board HTML and poll logs may remain in the tool's scratch
  area; never write an answers file into the target repo. Update the board
  in place (new draft text, remaining cards), and reply through
  `poll --agent-reply` with a changelog line per verdict ("H-7 no ->
  authority section now opens with ...").
- Continue until the author approves or ends the session. Do not approve on
  their behalf; do not treat silence as approval.
