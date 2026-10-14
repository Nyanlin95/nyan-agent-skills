# Migrations

Step-by-step lifecycles for moving behavior to a new owner and for changing persisted schema or data.

## Migration and fork lifecycle

Use a fork only as a temporary parallel implementation. Do not make the fork a second permanent owner.

Use these steps to move behavior to a new owner:

1. List the current owner, callers, behavior, failures, and old-owner tests.
2. Add a focused parity test before the migration.
3. Compare results, state changes, errors, and side effects in the parity test.
4. Implement the new path without unrelated behavior.
5. Route both paths through one explicit selection point.
6. Add new-owner tests for success, failure, invariants, and state transitions.
7. Run the parity test for all agreed cases.
8. Move callers to the new owner after the parity test passes.
9. Remove the migration-only parity test after the move.
10. List the old code and old-owner tests that can be removed.
11. Report remaining callers, rollback effects, and verification evidence.
12. Remove the old code and obsolete tests when the task scope authorizes removal and compatibility is resolved.
13. Ask for approval only when removal exceeds the requested scope or compatibility remains unresolved.

If both paths cannot use the same input, use contract fixtures or recorded outputs. State the limits of this comparison.

Do not add separate features, policies, or callers to the fork.

If the parity test finds an intentional difference, stop the migration. Ask the user to select the required behavior and owner.

## Schema and data migration lifecycle

Use this lifecycle when a change alters persisted schema, stored data, or compatibility between deployed versions. Do not treat code-path parity as proof that the data migration is safe.

1. Identify the old and new schemas, data owners, compatibility window, and source of truth.
2. Implement an additive schema change that old and new readers and writers can use before the rollout.
3. Implement an idempotent, resumable backfill with explicit checkpoints and retry behavior.
4. Test production-shaped legacy fixtures that include malformed, partial, duplicate, and boundary records.
5. Define data invariants and a reconciliation method such as counts, checksums, or sampled record comparison.
6. Define deployment order and reader/writer authority for mixed-version clients.
7. Define the stop condition and the rollback boundary, or state the forward-recovery path when rollback is unsafe.
8. Verify progress, error, invariant, and reconciliation signals before and during cutover.
9. Remove old reads, writes, schema, and migration code only after compatibility ends and reconciliation succeeds.
