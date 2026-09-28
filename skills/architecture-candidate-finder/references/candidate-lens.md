# Candidate Lens

Use these questions to connect a real design cost to a possible improvement. A signal starts an investigation; it does not prove that a pattern is needed.

## Useful terms

| Term | Plain-language meaning |
| --- | --- |
| Owner | The one part of the system responsible for a rule, state, or decision. |
| Boundary | The point where one part hands work or information to another. |
| Coupling | How much one part must know about another part's details. |
| Cohesion | Whether the decisions inside one part belong together and tend to change for the same reason. |
| Abstraction | A small interface that lets a caller ask for an outcome without managing all the mechanics. |
| Invariant | A rule that must remain true, such as a payment being captured at most once. |
| Design pattern | A known shape for solving a recurring design problem; it does not prove the shape fits this case. |
| Architectural decision | A choice about durable boundaries, dependencies, data, runtime, or operations that affects more than one local implementation. |

## Read signals as questions

| Signal | Ask before recommending | Direction worth considering |
| --- | --- | --- |
| One rule appears in several places | Do these places enforce the same policy, or do similar-looking cases change for different reasons? | Give a truly shared rule one clear owner, or keep separate rules separate when they evolve independently. |
| A caller contains repeated branches | Are the choices independent policies, lifecycle states, or a small stable set that is easiest to read inline? | Consider Strategy for independently varying behaviors, or an explicit state model when legal transitions matter. Keep a simple branch when it is clearer. |
| External API, database, or framework details appear across core logic | Which owner should translate that external contract, and is the detail already causing change or test pain? | Consider a narrow adapter or mapping boundary when it contains real leakage. Keep direct calls when the boundary would only forward data. |
| Construction logic repeats | Is the choice of what to build a real policy, or is this only a few similar lines? | Centralize construction only when the decision varies or must stay consistent. A factory or builder adds indirection and upkeep. |
| A workflow's steps, retries, or cleanup are scattered | Is there a meaningful lifecycle whose order and partial failures need one owner? | Consider an explicit workflow owner when it can make ordering and recovery predictable. Do not add a service layer that merely forwards calls. |
| A module or file seems too large | Which concepts change independently, and which callers need separate knowledge? | Split around distinct ownership or change reasons, not line count. A larger cohesive module may be simpler. |
| Similar-looking code is duplicated | Do both copies represent the same concept and change together? | Share one owner only when the concepts truly match. Keeping duplication can be safer than binding concepts that will diverge. |
| A small rule requires booting a large system to test | Which side effect or dependency makes the decision hard to isolate? | Separate a pure decision or introduce a seam at the real boundary. Avoid interfaces that have no second implementation or test need. |
| A change spreads across distant owners | Which decision is leaking, and what dependency direction would let one owner hide it? | Move the decision behind a focused boundary only when that boundary reduces knowledge or change reach. |

Use pattern names as short explanations, not as recipes. For example:

- **Strategy** groups interchangeable behaviors behind one choice point. Consider it when alternatives vary independently; account for the extra indirection and registration path.
- **State model** names the meaningful stages and allowed transitions of a lifecycle. Consider it when invalid transitions or conflicting flags cause real mistakes; account for the new explicit transition rules.
- **Adapter** translates an external contract at a boundary. Consider it when provider or framework details leak into internal rules; account for maintaining the mapping.
- **Factory** owns a real choice about object construction. Consider it when construction policy varies or is repeated; avoid it when a direct constructor already makes intent clear.

## Check broader architecture choices

For choices such as adding services, queues, event sourcing, or stronger module boundaries, inspect the actual requirements and operating constraints before comparing designs. Look for evidence about workload, ownership, latency, consistency, failure recovery, data retention, deployment, support capacity, and cost. Do not infer that a system needs distributed architecture from code size, team ambition, or a generic scaling concern. State which missing constraint would change the recommendation.

Check official documentation for the project's exact library, provider, or runtime version when a comparison depends on its guarantees or limits.

## Test whether a candidate is worth keeping

1. Point to the observed code, test, error, change history, or user-reported friction that motivates it.
2. Explain the causal mechanism, rather than only naming a smell or pattern.
3. Name the canonical owner the change would establish or preserve.
4. Show how a caller, test, or future change becomes simpler, safer, or more local.
5. Compare that gain with added layers, concepts, migration work, runtime behavior, and maintenance.
6. Keep the local fix or current design when it solves the demonstrated problem with less total complexity.
7. Lower confidence when frequency, runtime behavior, workload, or operating constraints are inferred rather than observed.
