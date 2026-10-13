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
6. Select full qualification when relevant history is missing or divergent instead of borrowing an unrelated anchor or returning an empty plan.
7. Fail on malformed identities and Git execution errors instead of treating them as no changes.
8. Group supported updates by candidate object and retain each base/range in the result.

Reject empty pre-push input. Distinguish an unavailable valid base from an invalid object identifier. An empty-tree diff can enumerate a candidate's files when history is unavailable, but cannot justify bounded coverage: record the missing history and select full qualification. A new-branch anchor equal to the candidate does not establish a meaningful changed scope by itself.

For several candidate objects, use proven object-specific execution or reject objects the current execution model cannot validate. Do not union paths and run once against HEAD while claiming all pushed objects passed. Deduplicate shared work only when the revision and environment inputs are equivalent.

## Keep the result reproducible

Include base/head identities, selected paths and owners, dependency closure, selected commands, broadening reasons, and execution model in the plan. Record the actual command results against that plan. Reject pending, missing, failed, or timed-out required checks. Provide the exact supported rerun command without embedding credentials.

Verify through isolated repositories that dirty/mismatched contexts fail, valid contexts succeed, and the same operation succeeds after the triggering fault is repaired. Cover non-HEAD pushes and multiple refs without mutating the user's checkout.
