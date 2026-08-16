# Repository Orchestration Policy

Use this reference to write a repository-local orchestration policy or configuration. Keep the policy short. Extend an existing canonical file if it owns agent work, delivery rules, or automation configuration.

Plan policy rules in semantic orchestration patterns. Read [orchestration-layers.md](orchestration-layers.md) for the catalogs. Keep `SKILL.md` as the canonical owner of each operating rule; record rules in the policy as brief requirements and link to the owning section instead of copying step text.

## Select the location

1. Read the repository instructions, contribution guide, automation files, and existing agent configuration.
2. Extend the existing canonical location when it covers orchestration.
3. Create one versioned policy file when no current file owns the rule.
4. Record the policy path in the task contract and delegation messages.
5. Do not create a second policy file for the same rule.

Use machine-readable configuration only when an existing tool reads it. Keep human workflow rules in the versioned policy. Do not invent a schema or a platform-specific filename for a repository that has no consumer.

## Record the local contract

Write each section in the policy and link its rule content to the owning `SKILL.md` section.

1. **Primary orchestrator:** Name `Omelet` as the role that owns scope, integration, decisions, evidence, and completion.
2. **Discovery:** Name the instruction files, canonical plans, owners, contracts, state boundaries, and gates Omelet must inspect.
3. **Semantic plan:** Require a working hypothesis for the task semantic composed from orchestration semantics, optional semantics marked `?`, and topology modifiers. Record the reconstruction policy so the label is re-derived from discovered work. Link the `orchestration-layers.md` catalogs.
4. **Task contract:** Require the outcome, scope, protected behavior, owner, paths, proof, authority limits, and the semantic plan (`Task := Semantic → Semantic → Semantic?`). Defer to `SKILL.md` "Define the task contract".
5. **Delegation:** Require bounded deliverables, one writer per file, disclosed shared roots, repository-relative paths, a return format, and checked runtime capability limits. Defer to `SKILL.md` "Compile semantics into roles" and "Delegate bounded work".
6. **Evidence:** Require the source, command or observation, scope, time, environment, result, freshness rule, and an `observed`, `inferred`, or `unavailable` status. Defer to `SKILL.md` "Use evidence that remains valid".
7. **Review:** Use focused checks by default; require independent review only for the high-risk cases. Defer to `SKILL.md` "Select review and implementation".
8. **Authority:** Name the actions that need explicit approval. Defer to `SKILL.md` "Respect authority boundaries".
9. **Exceptions:** Require an owner, reason, bounded scope, removal condition, and verification.
10. **Completion:** Require the focused proof, repository gates, final evidence refresh, cohesive-diff check, and remaining-risk report. Defer to `SKILL.md` "Complete the task".

## Check the policy

1. Compare each policy claim with the repository's current layout, commands, and authority model.
2. Confirm that Omelet can identify one writer for every shared path.
3. Confirm that the evidence rules distinguish static proof from runtime proof.
4. Confirm that the policy does not turn routine work into a review chain.
5. Confirm that any required high-risk reviewer is independent and read-only.
6. Confirm that optional review cannot block routine work.
7. Confirm that the declared scope and enforced runtime capability limits are distinct.
8. Confirm that no rule grants authority beyond repository policy or the user request.
9. Confirm that the policy reconstructs the task semantic from discovered work instead of prescribing a fixed label.

## Prove the setup level

Follow `SKILL.md` "Prove the setup level". Record the policy path, the consuming host, and the setup label (`policy-only` or verified active) in the delegation result.
