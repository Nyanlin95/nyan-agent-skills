---
name: local-git-gates
description: Design, install, review, or improve repository-local Git hooks and verification gates, including their agreement with CI and self-hosted execution. Use for pre-commit/pre-push checks, changed-path or dependency-aware routing, exact-commit qualification, reproducible gate commands, and hook or runner verification. Derive commands and policy from the target repository; keep one gate owner and distinguish working-tree feedback from publication proof.
---

# Local Git Gates

Keep hooks small and one project-owned runner responsible for planning, routing, execution, and results. Reuse the target repository's verification commands from local hooks and CI. Adapt the model to existing capabilities; do not copy another project's commands, branches, credentials, runner labels, or testing policy.

## Establish scope and ownership

1. Read repository instructions, testing/release guides, hook setup, runner source, workflow files, and relevant tests.
2. Inspect the current revision, dirty paths, hook configuration origin/scope, and existing command owners.
3. Identify the requested outcome and distinguish design/review, repository edits, local installation, and remote configuration authority.
4. Map each enforcement point to its revision context, selected checks, prerequisites, and success criteria.
5. Preserve unrelated work and existing hook-manager conventions.

Complete authorized local changes without repeated approval for ordinary routing or verification decisions. Treat an explicit installation request as authority for its required repository-local configuration. Ask before replacing an unknown hooks path, changing global configuration, creating a separate worktree, configuring remote rules or runner services, or expanding beyond the requested scope. Do not infer commit, push, merge, deployment, or credential authority from gate work.

## Separate feedback from qualification

| Mode | Establish | Do not claim |
| --- | --- | --- |
| Pre-commit / explicit paths | Fast feedback for staged scope or selected working-tree files | Validation of a committed tree when commands actually read unstaged content |
| Publication range / pre-push | Complete affected checks for the exact candidate commit and actual publication base | Qualification of another tip or a dirty checkout |
| CI | Completed checks for the workflow's exact checkout and event scope | Local results as a substitute for the required remote result |
| Supplemental lane | Coverage of its explicitly selected feature or fixture scope | Qualification of an arbitrary diff or a live provider |

Choose a publication execution model the repository can support. Prefer a clean existing checkout with exact-HEAD and cleanliness guards when sufficient. Use object-isolated execution only when required and authorized; do not create a worktree implicitly. Reject an unsupported pushed object rather than validate HEAD and label it as that object. Read [Publication qualification](references/publication-qualification.md) for revision, range, and multi-ref rules.

## Keep one canonical plan

1. Assign ref parsing, revision validation, path ownership, dependency closure, command selection, and result semantics to the existing runner.
2. Keep hook entrypoints as delegates that preserve stdin, arguments, and exit status.
3. Expose direct reproduction for the supported staged, explicit-path, range, pre-push, and full modes through the same runner.
4. Provide a read-only plan mode when routing complexity warrants it.
5. Include selected paths, base/head, affected owners, checks, and broadening reasons in the plan.
6. Make CI consume the canonical plan instead of maintaining a second path classifier in workflow conditions.

Treat interface flags as repository choices, not a required spelling. Keep check implementations with their existing owners; do not create a parallel verification framework.

## Route by ownership and dependency

1. Map known paths to complete existing feature checks and their consumers.
2. Include both old and new ownership for renames and retain old ownership for deletions and type changes.
3. Compute the union and transitive affected closure for multiple owners.
4. Retain required static checks and shared foundation checks according to repository policy.
5. Broaden to full qualification for shared configuration, gate policy, security, runtime, storage, migrations, contracts, coupled owners, or uncertain impact where narrower coverage is unproven.
6. Allow hygiene-only handling only for known documentation paths outside executable gate or release policy.
7. Validate selected command wiring and required test inventory before expensive service setup.

Keep complete required journeys where the repository uses feature slices; do not silently narrow them by test-name filters. Fail on required missing, empty, disabled, exclusive, unwired, or skipped coverage according to the repository's test policy. Do not import another project's ban on a test type or its provider/performance requirements. State what each lane actually proves.

Handle paths as opaque data with NUL-delimited Git output and argument arrays. Avoid line-split filename parsing, shell interpolation, and `eval`. Test spaced, dash-leading, metacharacter, renamed, deleted, and unclassified paths.

## Agree with CI and self-hosted execution

1. Inspect workflow triggers, checkout depth, event SHA/base, wrapper, job names, runner labels, permissions, timeouts, concurrency, and evidence uploads.
2. Require the CI wrapper to match the expected immutable revision to checkout HEAD before selecting checks.
3. Propagate planning and execution failures through a stable required status.
4. Skip expensive setup only after the canonical plan proves it unnecessary and all remaining required checks execute successfully.
5. Separate release qualification from supplemental feature workflows and deterministic substitutes from live lanes.
6. Preserve existing required-status names and trigger behavior unless changing them is in scope.
7. Verify remote protection separately before describing publication as protected.

Read [CI and self-hosted execution](references/ci-self-hosted.md) for persistent-runner state, cache ownership, credential boundaries, evidence, and availability. Treat a queued, offline, cancelled, or missing run as incomplete remote proof; do not change runner infrastructure or purchase capacity merely to make a status green.

## Execute and retain truthful results

1. Resolve prerequisites in the target environment before starting selected checks.
2. Bound commands and jobs with timeouts appropriate to their existing policy.
3. Serialize checks that share a checkout, database, build output, port, or mutable artifact root.
4. Isolate independent lanes only through supported test fixtures and unique resources.
5. Record the candidate revision, plan, selected-check status, exit code, and useful failure logs.
6. Require every selected check to complete successfully before reporting qualification.
7. Report the failed check, earliest failing boundary, and exact reproduction command.
8. Revalidate the qualified revision context after execution.

Use a checkout lock and fresh run-specific evidence directories when concurrent gates or persistent runners can mix results. Keep planning read-only. Do not count stale artifacts, pending checks, timeout, cancellation, or a previous successful run as this attempt's proof. Keep evidence proportional; do not add a reporting service for a small hook.

Never bypass checks with `--no-verify`, `continue-on-error`, success fallbacks, or suppressed failures. Do not weaken coverage or increase budgets merely to obtain a passing result.

## Install without surprises

1. Inspect the effective hooks path and its configuration origin before writing.
2. Verify the installer is operating on the intended repository root.
3. Verify all delegated hook and runner files exist.
4. Apply authorized repository-local configuration while preserving unknown existing setups.
5. Report the installed path, configuration scope, enforcement points, and rerun commands.

Do not install dependencies globally or modify developer credentials. Preserve worktree-specific configuration intentionally when it already exists; do not invent a new checkout model as part of installation.

## Verify the changed boundary

1. Run focused existing gate/installer/wrapper tests through actual CLI or hook entrypoints where available.
2. Exercise a successful selection and a relevant failure/recovery path.
3. Check malformed/empty ref input, deletion, new branch, missing base, divergent history, and multiple refs when pre-push parsing changes.
4. Check dirty tracked/staged/untracked state, mismatched tips, inherited Git context, and post-check mutation when qualification changes.
5. Check plan/CI agreement, missing required coverage, status propagation, timeouts, and current-attempt evidence when those owners change.
6. Exercise cold/warm cache, invalid ownership/link rejection, and recovery when persistent cache behavior changes.
7. Run the selected target-repository gate through the final changed entrypoint.
8. Run `git diff --check` on the cohesive change.

Use isolated test repositories and disposable service/data locations. Follow the target's testing conventions; do not require tests that import private helper internals or install hooks into the user's active checkout merely to test an installer. Verify generated tracked inputs' encoding and line endings where relevant.

## Completion

Report changed owners, enforcement/configuration scope, routed checks, execution model, commands/results, and remaining CI or runtime proof. Distinguish implemented policy, installed hooks, local execution, remote exact-SHA success, and verified remote protection. State unavailable coverage explicitly. Keep publication and installed-copy synchronization separate from editing this skill.
