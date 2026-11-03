# Publication qualification

Bind publication evidence to the candidate commit and actual publication base. Keep explicit-path and staged feedback available without mislabeling them as publication proof.

## Guard the execution context

1. Resolve immutable full commit IDs with Git before selecting checks.
2. Require the candidate to match checkout HEAD for a clean-checkout model.
3. Reject tracked, staged, and untracked dirt before qualification.
4. Remove inherited Git context overrides from repository-targeted child processes so hook variables cannot redirect them to another repository or index.
5. Check range whitespace against Git objects rather than only the working diff.
6. Revalidate HEAD and cleanliness after all selected checks finish.

Preserve existing staged-feedback semantics intentionally: selecting staged paths does not make a working-tree formatter or build read staged content. Label that limit or use a repository-supported index execution model when required.

Describe clean-checkout guards accurately. They check the checkout before and after execution; they do not provide object isolation or prevent an adversarial transient edit. Do not promise stronger isolation without implementing and proving it. Do not stash, clean, switch branches, or discard user work to satisfy qualification.

## Resolve pre-push scope

1. Parse every local-ref/local-object/remote-ref/remote-object tuple strictly.
2. Enforce the target repository's destination policy before any deletion shortcut.
3. Handle deletions explicitly without treating a zero local object as a runnable commit.
4. Use the supplied remote tip as the base for an existing remote ref when that object is available.
5. Derive a meaningful verified merge-base against repository-declared anchors for a genuinely new branch.
6. Select full coverage at the qualification checkpoint when relevant history is missing or divergent instead of borrowing an unrelated anchor or returning an empty plan. A repository's feedback-only pre-push stays unqualified and must not execute the release checkpoint implicitly.
7. Fail on malformed identities and Git execution errors instead of treating them as no changes.
8. Group supported updates by candidate object and retain each base/range in the result.

Reject empty pre-push input. Distinguish an unavailable valid base from an invalid object identifier. An empty-tree diff can enumerate a candidate's files when history is unavailable, but cannot justify bounded qualification: record the missing history and require full coverage at the release checkpoint. A new-branch anchor equal to the candidate does not establish a meaningful changed scope by itself. Let the repository's stage contract determine whether pre-push executes qualification or feedback; never label feedback as qualification or move the full checkpoint back into every push by default.

For several candidate objects, use proven object-specific execution or reject objects the current execution model cannot validate. Do not union paths and run once against HEAD while claiming all pushed objects passed. Deduplicate shared work only when the revision and environment inputs are equivalent.

## Qualify a tree-identical promotion without repeating checks

Treat a merge commit's identity change separately from a change to tested inputs. Do not require a complete rerun solely because a qualified candidate acquires a new SHA through promotion.

Use the repository runner's explicit promotion-receipt path when it supports one. Verify the merge parents, identical candidate trees, equivalent publication bases, current canonical coverage and the complete successful source receipt. Retain source evidence and its digest; identify inherited results separately from checks executed on the merge. Run revision-sensitive planning, diff hygiene, clean-checkout and final identity checks against the actual merge. Recheck remote identity before publication or deployment.

Reject reuse when inputs, required coverage, policy, relevant environment or evidence differ or cannot be established. Run the required fresh qualification in that case. Never relabel a source receipt manually, silently reuse results in ordinary pre-push, or invent a second validator outside the canonical runner. A gate-policy change needs its own bootstrap qualification before this path can be relied on.

## Assign checks to release stages

Keep development feedback, integration qualification, production promotion and deployment readiness distinct. Let the repository define which branch or PR owns the complete release checkpoint and which earlier stages provide feedback only. Feedback receipts must remain unqualified. Use complete affected coverage when qualifying a feature and full coverage for shared inputs or the repository's production checkpoint. Preserve successful source checks across equivalent merges through the canonical receipt contract instead of executing the same plan at both branch identities.

When a repository deploys automatically after its promotion PR merges, require the full checkpoint before merge and verify its evidence again before deployment. Bind the evidence to the same-repository merged PR, actual base/head and merge parents, successful workflow run attempt, workflow revision and complete ordinary source receipt. Verify tree equivalence and current production identity through the canonical runner; retain fresh configuration, recovery and health checks. Missing or failed proof blocks deployment even when remote merge protection is unavailable. Do not replace unavailable protection with fabricated success, or describe local hooks as remote enforcement.

For a manual deployment action, require current production identity, complete qualification, configuration and recovery prerequisites before side effects. Keep a user-selected full production recheck explicit and default it as the repository specifies; do not make merging a branch trigger deployment implicitly. A selected recheck must execute its complete canonical plan and fail closed. Bind it to the actual production range so unrelated diagnostic controls are not selected merely because they exist in the repository.

## Keep the result reproducible

Include base/head identities, selected paths and owners, dependency closure, selected commands, broadening reasons, and execution model in the plan. Record the actual command results against that plan. Reject pending, missing, failed, or timed-out required checks. Provide the exact supported rerun command without embedding credentials.

Verify through isolated repositories that dirty/mismatched contexts fail, valid contexts succeed, and the same operation succeeds after the triggering fault is repaired. Cover non-HEAD pushes and multiple refs without mutating the user's checkout.
