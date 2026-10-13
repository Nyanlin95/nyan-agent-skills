# Durable commands and effects

Apply these checks when commands or background work can outlive their caller. Use existing repository mechanisms; do not add a queue, receipt table, or approval framework to an ordinary local operation without a concrete need.

## Define an operation and its result

1. Bind operation identity to the actor/tenant, operation kind, and exact submitted payload according to the existing contract.
2. Reuse that identity to reconcile an uncertain attempt, not to collapse every future identical user intent.
3. Reject reuse with a changed payload or authority context.
4. Persist the canonical result with the state change where the transaction boundary permits it.
5. Return the existing authoritative result on valid replay without applying the effect again.
6. Recheck current read/access authority before exposing a stored result.

Distinguish accepted, queued, completed, rejected, and unconfirmed outcomes. A timeout, aborted request, or lost acknowledgement cannot establish that an effect did not happen. For an external effect outside the local transaction, use the provider's supported idempotency or reconciliation contract. Leave an unreconcilable outcome explicit and stop automatic replay when it could duplicate the effect. Do not promise exactly-once delivery from a local deduplication key.

## Keep dispatch and execution separate

- Commit product state and durable dispatch intent together when they must succeed together.
- Treat queue messages, wake signals, and realtime notifications as delivery hints; recover from persisted work when a hint is lost.
- Claim work with a bounded lease and an execution identity that fences later writes, renewal, completion, and cleanup.
- Reject stale executors after a replacement claim or generation takes ownership; a timestamp check alone does not fence the final write.
- Release database connections and transactions before waiting for a provider, user approval, or retry delay.
- Bound retries and retain the actionable failure or dead-letter outcome through the existing owner.

Verify a duplicate wake, expired claim, stale completion, restart, and lost response only where those paths apply. Use deterministic synchronization at the contested boundary instead of sleeps as evidence.

## Preserve exact authority across resume

Capture the reviewed run/operation, actor, tool or capability identity, input digest, target, and relevant version or grant when approval is required. Validate that binding at the effect boundary, including delayed resume and retry. Treat model output and plugin/provider metadata as input, never as authority to grant themselves access.

Separate revoking an unstarted operation from reconciling an effect that already started. Reject new unauthorized effects after cancellation or revocation while preserving permitted recovery of a completed or uncertain result. Do not discard receipts merely to display a cancelled status.

For versioned runtime or plugin changes, update the canonical identity owner and its required manifests, digests, migrations, and consumers together. Preserve existing access choices and waiting-run contracts. Keep newly introduced capabilities disabled or ungranted until accepted where the product requires it. Use a recognized-drift repair only within the authorized local scope; reject unknown migrations, ambiguous versions, or unreviewed capability changes instead of rewriting grants to match.

## Prove the effect boundary

Select a success and relevant failure/recovery journey that asserts durable state and effect count, not only an HTTP status or emitted event. Include identity/payload mismatch and cross-actor access when the changed contract affects them. Exercise the real public entrypoint with isolated persistence; substitute only external boundaries allowed by repository policy. Keep synthetic, provider-wire, and hosted evidence distinct.
