# CI and self-hosted execution

Treat self-hosted execution as the canonical gate running on a persistent machine with explicit state ownership. Keep CI policy in the repository's existing runner and wrapper. Do not install a runner, change its service/account, start an offline runner, alter secrets, or configure remote protection without the required authorization.

## Preserve local and remote agreement

- Validate the event's immutable revision against checkout HEAD before planning.
- Resolve the real event base with enough fetched history; select full qualification for valid but unavailable history or manual events without a meaningful base.
- Reject malformed revision input and planning failures.
- Keep a stable required status present for every event it is intended to gate; do not use path filters that leave that status absent.
- Execute a proven hygiene-only plan before skipping language runtimes, dependencies, browsers, or services. A failed or malformed plan must never activate the skip.
- Preserve required job identity and workflow provenance deliberately when combining or reusing workflows; matching a job name alone does not prove compatibility with remote rules.
- Keep fixed-feature supplemental checks distinct from qualification of the event's actual diff.

Use repository-appropriate minimum permissions, pinned actions where that is the convention, nonpersistent checkout credentials, and bounded job/step timeouts. Separate concurrency policy by resource and purpose; do not cancel a required release attempt merely to reuse a generic pull-request setting.

Keep untrusted pull-request code outside privileged persistent runners and credential-bearing execution unless the repository has an explicitly approved isolation design. Inspect workflow triggers and trust boundaries before adding self-hosted coverage. Repository files establish configured behavior; live runner state and remote rules require separate inspection.

## Own persistent state

- Namespace dependency caches by repository, runtime/toolchain, and dependency lock identity.
- Reuse a cache for downloads, while still installing from the lockfile; never treat a warm cache as qualification evidence.
- Validate absolute owned roots and ownership markers before pruning cache generations.
- Reject unexpected entries, symlinks, junctions, and reparse points that could redirect cleanup outside the owned root.
- Preserve developer caches, profiles, credentials, and unrelated runner repositories.
- Use run-specific logs, reports, screenshots, temporary credentials, and disposable service/data locations.
- Serialize execution that shares mutable resources; state the limits of a checkout lock across clones, direct test commands, or descendants after a crash.

Reuse existing cache and fixture owners. Add cache rotation, locks, or run directories only where persistent state or concurrency creates a concrete need. Do not copy a machine path, runtime version, database name, or another project's cache namespace into the target.

## Separate credential and provider lanes

Use deterministic external substitutes for bulk checks only where repository policy allows them. Label the resulting proof synthetic. Keep required live-wire/provider checks separate and explicit about configuration, cost, timeout, and failure. Missing required live configuration leaves that lane incomplete; do not silently replace it with a fixture.

Inspect environment precedence. Prefer CI-scoped configuration over a runner user's personal profile where supported; ensure model/provider or endpoint overrides remain coherent. Document any intentional fallback without reading or printing secrets. Do not copy personal credentials into CI to repair availability.

## Retain current-attempt evidence

Record a fresh run identity, checkout revision, canonical plan, selected checks, status, durations, exit codes, and useful lane logs. Publish summaries atomically when concurrent readers need them. Require all selected checks to finish successfully; a current-run pointer or earlier successful artifact alone proves nothing.

Upload only this attempt's evidence after success or failure as configured. Distinguish optional diagnostic artifacts from mandatory qualification evidence and make missing mandatory evidence fail. Avoid uploading environment files, secret stores, profiles, or unrelated historical artifacts.

## Report the actual remote boundary

After an authorized push or dispatch, identify the intended workflow run by exact candidate SHA and wait for its terminal conclusion. Report missing, queued, cancelled, timed-out, offline-runner, and billing/usage-blocked runs as incomplete remote qualification. Do not infer a product regression from runner unavailability.

Require the successful intended workflow for the exact candidate before an authorized promotion when repository policy demands it. Verify required-check rules and bypass restrictions separately; hooks and workflow files do not enforce remote protection. Preserve existing publication authority boundaries.
