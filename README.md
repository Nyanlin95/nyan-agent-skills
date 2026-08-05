# Nyan Agent Skills

Agent ကို လိုအပ်သည်များ အောက်ပါအတိုင်း မှာကြားနိုင်ပါတယ်

Independent coding-agent skills with natural-language triggers for code review, implementation quality, UI visual review, and bounded OpenCode delegation. Each skill is self-contained under `skills/`.

Released under the [MIT License](LICENSE).

## Use a skill

The coding agent loads an installed skill when a request matches its description. The match uses meaning, not an exact keyword.

1. State the outcome, scope, and limits.
2. Share the relevant files, evidence, or rendered result.
3. Use plain language or select the skill with `$skill-name`.
4. Review the reported evidence before you authorize a change or publication.

### CQT review

Use `cqt-review` for findings, risks, or an architecture review. Use it for requests such as:

```text
review this code
audit this repository
review this pull request beyond correctness
find ownership and dependency problems
assess this migration
review this forked implementation
check failure behavior and state modeling
plan a safe ownership cutover
```

Share the files, diff, pull request, migration plan, or repository scope that the coding agent must review. To select it directly, write:

```text
Use $cqt-review to review this code.
```

### Adversarial review

Use `adversarial-review` to challenge a plan, change, review, or CQT conclusion before you act. Use it for requests such as:

```text
red-team this plan
stress-test this pull request
try to falsify this architecture decision
challenge this CQT review
find the failure case we missed
play devil's advocate before we merge
```

Share the artifact and the decision it supports. To select it directly, write:

```text
Use $adversarial-review to challenge this CQT report before we implement its recommendations.
```

### Implementation quality

Use `implementation-quality` to write or refactor code. Use it for requests such as:

```text
refactor this code
implement this feature
move this behavior to the correct owner
simplify this control flow
replace this old implementation
migrate this module with parity tests
remove accidental complexity
make this failure path explicit
```

State the required behavior, allowed scope, and compatibility limits. To select it directly, write:

```text
Use $implementation-quality to refactor this code.
```

### Local Git Gates

Use `local-git-gates` to add, change, or review repository-local Git checks. Use it for requests such as:

```text
add a pre-push check
set up local Git hooks
route changed paths to focused tests
make this hook failure reproducible locally
review our pre-commit checks
install a repository-local hooks path
```

Share the repository scope, existing test commands, and hook requirements. To select it directly, write:

```text
Use $local-git-gates to add a path-aware pre-push check.
```

### UI visual review

Use `nyan-ui-visual-review` to review an existing rendered interface. Use it for requests such as:

```text
review this UI
audit this screen
critique this dashboard
review the responsive states
find visual consistency problems
review this user flow
polish this existing interface
check this page against the design system
```

Share screenshots, live routes, or frontend code. Include interaction and responsive states when they matter. To select it directly, write:

```text
Use $nyan-ui-visual-review to review this screen.
```

### Handoff to OpenCode

Use `handoff-to-opencode` to hand off a limited, non-sensitive implementation task to OpenCode. Use it for requests such as:

```text
use OpenCode to implement this change
delegate this bounded fix to OpenCode
use a free OpenCode Zen model
let OpenCode add these focused tests
use DeepSeek V4 Flash Free for this task
implement this on a new branch with OpenCode
prepare this bounded OpenCode change for a pull request
```

State each file or folder that OpenCode can edit. Do not include secrets or confidential code. To select it directly, write:

```text
Use $handoff-to-opencode to implement this task only in src/auth/.
```

### Simplified technical writing

Use `simplified-technical-writing` to make technical prose clear, controlled, and concise. Use it for requests such as:

```text
rewrite this README in plain technical English
make these error messages less AI-generated
write this runbook in strict simplified technical English
make this pull-request description clear and direct
```

Share the prose and state whether it is a strict procedure or general technical prose. To select it directly, write:

```text
Use $simplified-technical-writing to rewrite this runbook in strict mode.
```

Use more than one skill when a task needs more than one owner. For a high-risk change, use this order:

1. Use `cqt-review` to identify ownership, lifecycle, and code-quality concerns.
2. Use `adversarial-review` to try to falsify the CQT conclusions and the underlying change claims.
3. Use `implementation-quality` to implement only the accepted, bounded corrections.

## Skills

| Skill | Purpose |
| :--- | :--- |
| [cqt-review](skills/cqt-review/) | Review code and migrations for correctness, quality, taste, ownership, dependencies, state, and failure behavior. |
| [adversarial-review](skills/adversarial-review/) | Try to falsify material claims in plans, changes, and reviews before a decision. |
| [implementation-quality](skills/implementation-quality/) | Keep implementation and ownership migrations simple, readable, correctly owned, and free of accidental complexity. |
| [local-git-gates](skills/local-git-gates/) | Design repository-local Git hooks that route changed paths to existing verification commands. |
| [nyan-ui-visual-review](skills/nyan-ui-visual-review/) | Review rendered interfaces through bounded, evidence-backed domain coverage, systemic findings, targeted improvements, and a clear verdict. |
| [handoff-to-opencode](skills/handoff-to-opencode/) | Hand off limited implementation work to a live OpenCode model within explicit paths, with optional branch and pull-request delivery. |
| [simplified-technical-writing](skills/simplified-technical-writing/) | Rewrite technical prose in strict or STE-flavored Simplified Technical English. |

## Library approach

- Keep implementation skills separate from review skills.
- Give each behavior, rule, and finding one canonical owner.
- Start each skill with one authoritative flow.
- Use detailed checks only to complete the current flow step.
- Keep core workflows in `SKILL.md` and detailed checks in one-level references.
- Adapt external guidance to the owning skill instead of adding overlapping dependencies.
- Verify rendered behavior with rendered evidence.

## Add a skill

1. Create `skills/<skill-name>/`.
2. Add a valid `SKILL.md` and `agents/openai.yaml`.
3. Keep detailed references and reusable scripts inside the skill folder.
4. Validate the skill.
5. Add one catalog entry above.

See `AGENTS.md` for the library conventions.
