# Product design orchestration

Detailed guidance for orchestrating visible design work.

## Orchestrate product design

Treat visible design work as product work, not as a styling pass.

Start from the intended experience, including feeling-based feedback, existing work, and product or brand context. Encourage the agent to explain likely causes in concrete design terms and test the important ones. Let the task determine whether it needs a quick local correction, exploration, deeper critique, or basic visual foundations.

Favor distilling useful existing choices into coherent roles before introducing a new visual language. For a new project, encourage a small provisional foundation tested through representative compositions. Preserve intentional variation and the medium's conventions; avoid turning coherence into uniformity or a local refinement into a project-wide migration.

Use the required visual review below and select other guidance by task:

| Work that needs help | Useful guidance |
| --- | --- |
| Visual foundations, spatial relationships, composition, or rendered critique across media | Use `nyan-ui-visual-review` for UI changes; use it for other visual media when relevant. |
| Implementing interactive web journeys, shared UI foundations, state ownership, navigation, caching, loading, recovery, or measured performance | Consider `frontend-system-principles` for the affected implementation boundaries. |
| A design change whose appearance and frontend behavior are coupled | Consider the relevant parts of both, keeping visual judgments and implementation contracts with their respective owners. |

Require visual review for UI changes as specified below. Keep other skill choices task-dependent; do not require both skills or a fixed sequence. Keep detailed criteria in their owning skills. Let one agent design, implement, and verify when that fits; delegate only when a bounded independent contribution helps. Continue with available project conventions when an optional skill is absent, and disclose any material gap.

When delegating, share the outcome, intended feeling, evidence, protected behavior, and owned scope. Leave the specialist room to choose visual means, methods, and suitable tools. Omelet owns intent, scope, authority, integration, and completion; the authoring agent owns implementation, with visual critique informing its decisions.

Preserve product meaning and behavior outside the requested scope. A visual reference does not authorize changing navigation, information architecture, workflow order, or data meaning. Seek a user decision only for a material expansion not already authorized. Prefer fixing a shared owner when it explains the defect, and keep justified local exceptions local.

Verify visible claims in the native rendered artifact, using measurements for geometry and interaction checks for behavior as relevant. Treat unrendered foundations as provisional and a verified sample as evidence only for its tested scope. Do not infer visual success from automated checks alone.

When the request extends an accepted visual direction across a product, name the accepted baseline, bounded adoption scope, shared owners, affected compositions, and responsive or scale proof when applicable. Promote accepted roles into the existing token, component, and layout owners; correct confirmed drift only within the authorized scope and verify affected consumers. Review enclosing compositions as well as isolated components, including relevant intermediate viewport or scale states and content or state stress. A component gallery, token check, or representative sample does not establish system-wide consistency. Keep incomplete adoption explicit.
