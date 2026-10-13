# Effect and recovery attacks

Use these falsifiers only for decision-relevant claims. Inspect source first; execute faults only in an isolated authorized environment. Record unavailable runtime proof as untested rather than inventing a reproduced failure.

| Claim under test | Counterexample to attempt | Observable falsifier |
| --- | --- | --- |
| Retry cannot duplicate the operation | Commit the effect, lose its response, then reconcile with the same identity | More than one durable effect or a fresh identity substituted silently |
| Idempotency preserves authority | Reuse the identity with another actor, target, or payload | Changed effect or disclosure of a result to an unauthorized actor |
| Worker completion is fenced | Expire/reassign a claim before the old executor completes or cleans up | Stale executor changes state or removes the replacement's work |
| Dispatch survives interruption | Commit product state and interrupt notification/queue delivery | Durable intent disappears or cannot be recovered |
| Approval authorizes the exact effect | Alter arguments, target, tool/version, or capability digest before resume | Changed operation executes under the old approval |
| Revocation prevents new effects | Revoke after approval but before effect start | Unstarted operation still executes |
| Cancellation reconciles truthfully | Cancel after the external effect starts but before its receipt returns | Completed effect is hidden, replayed, or falsely reported as never applied |
| Updating capabilities preserves existing choices | Resume an old run after adding or changing a contribution | Old run gains new authority or existing grants are silently rewritten |
| Delayed acknowledgement preserves newer work | Type or erase after submit, then release the old response | New draft is cleared or replaced |
| Recovery is independent of current validation | Make the current form invalid after an uncertain successful submission | Its original receipt cannot be reconciled or the operation is repeated |
| Replay is complete and scoped | Deliver duplicates, a gap, and late callbacks after session replacement | Missing durable events, duplicates, or data from the previous scope |
| Performance passed for the real journey | Remove a required scenario or measurement field while preserving a success flag | Gate accepts missing evidence, zero substitutes, or a collector-only result |

Define the synchronization point that exposes the claim: transaction commit, effect start, claim reassignment, approval resume, UI acknowledgement, or cursor catch-up. Use fixture controls or observable events instead of timing guesses. Assert durable state, effect count, current authority, retained draft, or emitted measurement as appropriate.

Challenge the precise guarantee. A clean-checkout guard does not promise hostile-edit isolation; a lease does not imply provider-side cancellation; an idempotency key does not prove exactly-once delivery; a snapshot does not prove current authority. Do not report a defect because a system lacks a stronger guarantee it never claimed or required.
