# Decision Gate Extract (Power BI–Ready)

This document defines a **flattened decision view** derived from RGDS decision logs.
It is designed for **phase-gate forums**, portfolio review, and BI dashboards.

This extract is **not** a source of truth. The source of truth remains the validated decision log JSON.

## Canonical extract fields

| Field | Type | Purpose |
|---|---:|---|
| decision_id | string | Stable join key |
| program_id | string | Portfolio rollups |
| gate | string | Phase-gate anchor (e.g., IND-enabling, CMC readiness) |
| decision_category | enum | `internal` or `regulatory_interaction` |
| decision_outcome | enum | `go`, `conditional_go`, `no_go`, `defer`, `defer_with_required_evidence` |
| decision_status | enum | `draft`, `in_review`, `approved`, `superseded` |
| evidence_coverage_score | number | Executive signal of evidence posture (0–100) |
| missing_evidence_count | number | Red-flag count of declared gaps |
| residual_risk_level | enum | `low`, `medium`, `high` |
| approver_roles | string[] | Accountability surface (roles, not names) |
| decision_date | date-time | Time-to-decision tracking |
| reentry_due_date | date | For deferred decisions, when re-entry is expected |

## Suggested transformations

From decision log JSON:
- `program_id` ← `program_context.program_id`
- `decision_outcome` ← `decision_outcome.outcome`
- `missing_evidence_count` ← `len(evidence_gaps)`
- `approver_roles` ← unique roles in `governance.approvals[]`
- `reentry_due_date` ← earliest due date in `actions[]` linked to re-entry conditions

## Notes for BI

- Keep the JSON decision log **as a drill-through link** for auditability.
- Do not compute “confidence” in BI; capture confidence explicitly in the decision log.
