# Model routing

How to choose an eligible free model for the current task.

## Route the free model

Select the model for the current task. Do not keep a fixed default or infer capability from model names or list order.

| Task | Selection priority among eligible models |
| --- | --- |
| Mechanical edits or simple transformations | Prefer lower observed latency when capability is sufficient. |
| Bounded implementation or focused tests | Prefer demonstrated coding and tool-use reliability for comparable work. |
| Debugging or bounded refactoring | Prefer evidence of reasoning quality for dependencies, failure paths, and behavior preservation. |
| Context-heavy work within the allowed scope | Require enough context first, then apply the relevant task priority above. |

Use comparable verified results or current documented capabilities as evidence. Record the source and observation date. Treat provider descriptions as capability claims, not comparative proof. If comparative evidence is unavailable, choose an eligible candidate provisionally and state that limitation. Do not require the user to name a model.

Honor an explicit user model choice when it is eligible. If that choice is unavailable or ineligible, complete the task directly. Apply the routing policy to alternatives only when the user permits substitution. Record the selected model, task fit, eligibility evidence, and concise rationale before dispatch.
