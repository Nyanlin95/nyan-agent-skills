# Nyan Agent Skills

Agent ကို လိုအပ်သည်များ အောက်ပါအတိုင်း မှာကြားနိုင်ပါတယ်

Independent coding-agent skills with natural-language triggers for code review, implementation quality, UI visual review, and bounded OpenCode delegation. Each skill is self-contained under `skills/`.

Released under the [MIT License](LICENSE).

## How to trigger a skill

The coding agent loads an installed skill when a request matches its description. The match uses meaning, not an exact keyword.

### CQT review

Use `cqt-review` when you want findings, risks, or an architecture review. These requests match its trigger description:

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

### Implementation quality

Use `implementation-quality` when you want a coding agent to write or refactor code. These requests match its trigger description:

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

Use `local-git-gates` when you want to add, change, or review repository-local Git checks. These requests match its trigger description:

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

Use `nyan-ui-visual-review` when you want a review of an existing rendered interface. These requests match its trigger description:

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

### OpenCode CLI

Use `opencode-cli` when you want OpenCode to implement a limited, non-sensitive task. These requests match its trigger description:

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
Use $opencode-cli to implement this task only in src/auth/.
```

One request can use more than one skill. For example, a coding agent can review code first and then refactor accepted findings.

## Skills

| Skill | Purpose |
| :--- | :--- |
| [cqt-review](skills/cqt-review/) | Review code and migrations for correctness, quality, taste, ownership, dependencies, state, and failure behavior. |
| [implementation-quality](skills/implementation-quality/) | Keep implementation and ownership migrations simple, readable, correctly owned, and free of accidental complexity. |
| [local-git-gates](skills/local-git-gates/) | Design repository-local Git hooks that route changed paths to existing verification commands. |
| [nyan-ui-visual-review](skills/nyan-ui-visual-review/) | Review rendered interfaces through bounded, evidence-backed domain coverage, systemic findings, targeted improvements, and a clear verdict. |
| [opencode-cli](skills/opencode-cli/) | Delegate limited implementation work to a live OpenCode model within explicit paths, with optional branch and pull-request delivery. |

## Library approach

- Keep implementation skills separate from review skills.
- Give each behavior, rule, and finding one canonical owner.
- Keep core workflows in `SKILL.md` and detailed checks in one-level references.
- Adapt external guidance to the owning skill instead of adding overlapping dependencies.
- Verify rendered behavior from rendered evidence.

## Add a skill

1. Create `skills/<skill-name>/`.
2. Add a valid `SKILL.md` and `agents/openai.yaml`.
3. Keep detailed references and reusable scripts inside the skill folder.
4. Validate the skill.
5. Add one catalog entry above.

See `AGENTS.md` for the library conventions.
