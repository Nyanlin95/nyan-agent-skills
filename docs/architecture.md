# Architecture and ownership

| Area | What it owns |
| --- | --- |
| [AGENTS.md](../AGENTS.md), [CLAUDE.md](../CLAUDE.md), and [README.md](../README.md) | Repository contributor rules, their Claude entry point, and the public guide and generated skill catalog, respectively. |
| [skills/](../skills/) | Canonical source for each skill's trigger, workflow, interface metadata, and bundled resources. [Omelet](../skills/omelet-orchestrator/SKILL.md) owns cross-skill routing and coordination. |
| [scripts/](../scripts/) | [validate_skills.py](../scripts/validate_skills.py) checks skill layout, metadata, and links. [gen_catalog.py](../scripts/gen_catalog.py) generates or checks the README catalog from interface metadata and [purpose overrides](../scripts/catalog_purposes.json). [check.py](../scripts/check.py) runs those checks, discovers tests, and checks Git whitespace. |
| [tests/](../tests/) | Repository tool tests, fixtures, and [trigger examples](../tests/trigger_examples.json). The examples check coverage and phrase alignment with skill descriptions. Live model routing requires a behavioral trial. Tests for bundled skill helpers live alongside those helpers. |
| [.githooks/](../.githooks/) and [CI](../.github/workflows/validate.yml) | The opt-in pre-commit hook invokes `check.py --staged` for metadata and catalog checks against the Git index. CI runs the full check on pushes and pull requests to `main`. |
| [.codex/](../.codex/README.md) | The project-scoped Codex agent registry and role definitions. |
| [docs/](.) and [research/](../research/) | Repository documentation and source material, including the [archived Wer Ywet Studio plan](../research/codex-native-orchestration-plan.md). |

Each `skills/<name>/` directory has a `SKILL.md` for trigger wording and
instructions and an `agents/openai.yaml` for display metadata and the default
prompt. Keep detailed guidance in directly linked `references/` files and
optional bundled helpers and assets in `scripts/` and `assets/`. A meta skill
such as the [User Testing Playbook](../skills/user-testing-playbook/SKILL.md)
owns the overall workflow and links to independently selectable sibling skills
that own specific tasks.

Installed copies live in the consuming host's skill roots, such as
`~/.agents/skills/` or a host-configured `$CODEX_HOME/skills/`. Edit the
repository source. The [skill syncer](../.codex/README.md) owns explicitly
authorized copies to existing roots and verifies source/destination parity.
