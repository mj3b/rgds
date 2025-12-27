# Change Control Log

This log records controlled changes to RGDS schemas, validators, and canonical examples.
It is intentionally lightweight: enough to support auditability and explain evolution.

| Date | Change | Rationale | Impacted Files | Approved By |
|---|---|---|---|---|
| 2025-12-27 | Decision Log Schema v1.1 (added `defer_with_required_evidence`) | Support defensible “pause and re-enter” decisions when evidence is insufficient but the program is not terminated. | `decision-log/decision-log.schema.json` | TBD |
| 2025-12-27 | Semantic validation rules for examples | JSON schema validation is necessary but insufficient; enforce decision-type invariants (e.g., conditional decisions must include conditions). | `scripts/validate_all_examples.py` | TBD |
| 2025-12-27 | Canonical IND defer decision example | Provide a concrete, reviewable exemplar for late-breaking evidence and re-entry conditions. | `examples/rgds-dec-0003-defer-required-evidence.json` | TBD |
| 2025-12-27 | Optional Target Product Profile context | Allow decisions to be grounded in development intent without imposing a rigid template. | `decision-log/decision-log.schema.json`, `docs/decision-log.md` | TBD |
| 2025-12-27 | Regulatory interaction decision category + context | Treat regulatory interactions as decision inputs with explicit interpretation risk. | `decision-log/decision-log.schema.json`, `docs/decision-log.md`, `examples/rgds-dec-0004-regulatory-interaction.json` | TBD |
| 2025-12-27 | Decision gate extract definition | Make RGDS BI-native for phase-gate forums and portfolio review. | `evaluation/decision-gate-extract.md` | TBD |
