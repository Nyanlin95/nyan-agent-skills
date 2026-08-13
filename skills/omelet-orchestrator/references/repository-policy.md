# Repository Orchestration Policy

Use this reference to write a repository-local orchestration policy or configuration. Keep the policy short. Extend an existing canonical file if it owns agent work, delivery rules, or automation configuration.

## Select the location

1. Read the repository instructions, contribution guide, automation files, and existing agent configuration.
2. Extend the existing canonical location when it covers orchestration.
3. Create one versioned policy file when no current file owns the rule.
4. Record the policy path in the task contract and delegation messages.
5. Do not create a second policy file for the same rule.

Use machine-readable configuration only when an existing tool reads it. Keep human workflow rules in the versioned policy. Do not invent a schema or a platform-specific filename for a repository that has no consumer.

## Record the local contract

Write these sections in the policy:

1. **Primary orchestrator:** Name `Omelet` as the role that owns scope, integration, decisions, evidence, and completion.
2. **Discovery:** Name the instruction files, canonical plans, owners, contracts, state boundaries, and gates that Omelet must inspect.
3. **Task contract:** Require an outcome, scope, protected behavior, owner, paths, proof, and authority limits before work starts.
4. **Delegation:** Require bounded deliverables, one writer per file, disclosed shared roots, repository-relative paths, a return format, and the checked runtime capability limits.
5. **Evidence:** Require the source, command or observation, scope, time, environment, result, freshness rule, and an `observed`, `inferred`, or `unavailable` status.
6. **Review:** Use focused checks by default. Require independent review only
   for security, irreversible data loss, tenant isolation, destructive
   migration, credentials, or real production publication.
7. **Authority:** Name the actions that need explicit approval, including external writes, shared runtimes, credentials, publication, and destructive work.
8. **Exceptions:** Require an owner, reason, bounded scope, removal condition, and verification for each exception.
9. **Completion:** Require the focused proof, repository gates, final evidence refresh, cohesive-diff check, and remaining-risk report.

## Constrain delegation

1. Inspect the available sandbox, permission, and tool limits before each delegation.
2. Select the narrowest enforced capability mode that can complete the assigned work.
3. Do not give secrets, credentials, external-write authority, publication authority, or destructive authority by default.
4. Permit a bounded writer only when runtime controls enforce its required write scope and external authority.
5. If those controls are unavailable, remove secrets and personal data from task inputs.
6. In that case, delegate read-only work only.
7. Record declared path scope as a contract.
8. Record each shared root before delegates change it.
9. Record the removal condition for each exception.

## Close each delegation

1. Require a terminal status of `complete`, `partial`, `blocked`, or `cancelled`.
2. Require changed paths, checks, evidence, and uncertainty in the result.
3. Stop cancelled, superseded, or satisfied assignments.
4. Serialize delegates that share a file, contract, state owner, or integration point.
5. Reject or recontract work that exceeds the task contract.
6. Reject or recontract each `partial`, `blocked`, or `cancelled` result before integration.
7. Narrow the task contract explicitly if only the verified completed portion remains required.
8. Independently verify complete material results before integration.
9. End the assignment after Omelet consumes the result.

## Select review

1. Use focused repository checks for routine work.
2. Use one independent reviewer when a decision could cause a security breach,
   irreversible data loss, tenant-isolation failure, destructive migration,
   credential exposure, or real production publication.
3. Add a second specialist only for a concrete unresolved finding.
4. Do not classify documentation, local redeploys, ordinary Git pushes,
   shared-file edits, or workflow wording as high-risk by category alone.
5. Do not block routine work because an optional reviewer is unavailable.

## Check affected boundaries

1. For genuinely high-risk work, identify each affected code or system boundary before applying architecture checks.
2. Use the specialist most relevant to the concrete risk.
3. Record important risks as `observed`, `inferred`, or `unavailable`.
4. Use implementation-quality for accepted ownership corrections when needed.
5. Keep new components isolated until an observed integration point requires a connection.
6. Do not add a shared utility, fallback route, or compatibility path without a named owner and removal condition.
7. Do not require a dependency direction or adapter pattern when the task has no material affected boundary.

## Check the policy

1. Compare each policy claim with the repository's current layout, commands, and authority model.
2. Confirm that Omelet can identify one writer for every shared path.
3. Confirm that the evidence rules distinguish static proof from runtime proof.
4. Confirm that the policy does not turn routine work into a review chain.
5. Confirm that any required high-risk reviewer is independent and read-only.
6. Confirm that optional review cannot block routine work.
7. Confirm that the declared scope and enforced runtime capability limits are distinct.
8. Confirm that no rule grants authority beyond repository policy or the user request.

## Prove the setup level

1. Identify the agent host that must consume the setup.
2. Identify its policy, configuration, or registration surface.
3. Label the result `policy-only` when no compatible host consumes repository configuration.
4. Do not claim an active setup from policy text alone.
5. Verify host loading and the Omelet identity for an active setup.
6. Run one bounded read-only delegation round trip when the host supports delegation.
7. Record unsupported host capabilities as unavailable coverage.
