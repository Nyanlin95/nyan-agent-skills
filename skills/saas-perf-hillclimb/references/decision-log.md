# Decision log

Keep one `decision.tsv` per climb outside the repository tree or in a gitignored path. Read it before every attempt.

Columns:

| Column | Content |
| --- | --- |
| id | Attempt number |
| layer | database, backend, frontend, edge, infra, or load |
| hypothesis | The mechanism the change targets |
| change | What changed |
| before | Baseline median |
| after | Candidate median |
| delta_pct | Percent change in the median |
| p_value | Significance against the baseline samples |
| guard | pass or fail |
| verdict | kept or reverted |
| note | Why, and what to try next |

Record the A/A baseline as attempt 0 for each layer with its median and spread.