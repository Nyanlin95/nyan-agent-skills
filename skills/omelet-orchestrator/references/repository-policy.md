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

## Register compact role contracts

Register project-scoped agent roles in the host agent registry when one exists. Keep each role contract compact:

1. Name the role and state its narrow ownership in one or two lines.
2. Name the required skill and read it before acting.
3. State the exact owned paths and the explicit prohibitions.
4. Set the narrowest sandbox or capability mode that completes the role's work.
5. Do not add mandatory delegation, verification, review, evidence, or reporting gates to a role file; the primary policy owns those rules.

## Record the local contract

Write each section in the policy and link its rule content to the owning `SKILL.md` section.

1. **Primary orchestrator:** Name `Omelet` as the role that owns scope, integration, decisions, evidence, completion, shared roots, shared runtimes, and authorized publication.
2. **Discovery:** Name the instruction files, canonical plans, owners, contracts, state boundaries, and gates Omelet must inspect.
3. **Request interpretation:** Infer the work posture and intended artifact state from the user's action, subject, deliverable, quantity, and constraints. Use the defaults in `SKILL.md` "Interpret product requests" without turning them into a required run template.
4. **Semantic plan:** Require a working hypothesis for the task semantic composed from orchestration semantics, optional semantics marked `?`, and topology modifiers. Record the reconstruction policy so the label is re-derived from discovered work. Link the `orchestration-layers.md` catalogs.
5. **Task contract:** Require the outcome, scope, protected behavior, owner, paths, proof, authority limits, and the semantic plan (`Task := Semantic → Semantic → Semantic?`). Defer to `SKILL.md` "Define the task contract".
6. **Product design:** When visible design is in scope, name the design intent, the aspects a reference actually governs, protected product behavior, the local design-system owner, and the rendered proof. Require explicit user approval for broad product changes. Link to `SKILL.md` "Orchestrate product design" and the repository's design skill instead of copying a visual checklist or prescribing a pixel solution.
7. **Delegation:** Require a minimal contract per delegate, disclosed shared roots, repository-relative paths, and checked runtime capability limits. Defer to `SKILL.md` "Compile semantics into roles" and "Delegate bounded work".
8. **Evidence:** Require the source, command or observation, scope, time, environment, result, freshness rule, and an `observed`, `inferred`, or `unavailable` status. Defer to `SKILL.md` "Use evidence that remains valid".
9. **Review:** Use focused checks by default; require independent review only for the high-risk cases. Defer to `SKILL.md` "Select review and implementation".
10. **Authority:** Name the actions that need explicit approval. Defer to `SKILL.md` "Respect authority boundaries" and "Authorize release workflows".
11. **Exceptions:** Require an owner, reason, bounded scope, removal condition, and verification.
12. **Completion:** Require the focused proof, repository gates, final evidence refresh, cohesive-diff check, and remaining-risk report. Defer to `SKILL.md` "Complete the task".

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
10. Confirm that role contracts stay compact and do not add policy gates.
11. Confirm that a plain request authorizes no Git or GitHub writes.
12. Confirm that visual references do not silently authorize product-model changes.
13. Confirm that design specialists receive intent and constraints without a universal visual prescription.
14. Confirm that design delegation remains optional and broad product changes require explicit user approval.
15. Confirm that exploration does not mutate production or present a recommendation as a decision.
16. Confirm that implementation verbs do not expand a broad subject into unbounded product authority.
17. Confirm that the reported artifact state distinguishes exploration, local changes, publication, deployment, and live proof.
18. Confirm that research and planning remain response-only unless the user or a canonical repository owner selects a file destination.
19. Confirm that the consuming host loads Omelet policy for ordinary requests that explicitly invoke Omelet; otherwise keep the setup labeled `policy-only`.

## Prove the setup level

Follow `SKILL.md` "Prove the setup level". Record the policy path, the consuming host, and the setup label (`policy-only` or verified active) in the delegation result.
