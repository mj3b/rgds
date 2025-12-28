# Decision Gate Extract (Power BI–Ready)

This document defines a **flattened decision view** derived from RGDS decision logs.
It is designed for **phase-gate forums**, portfolio review, and BI dashboards (e.g., Power BI).

This extract is **not a source of truth**.
The authoritative record remains the validated RGDS decision log JSON.

---

## Purpose and Scope

The Decision Gate Extract exists to:

- enable cross-program and portfolio-level visibility,
- support executive and governance review forums,
- surface evidence posture and risk signals at decision time,
- preserve drill-through access to auditable decision records.

This extract intentionally trades schema richness for **reviewability and comparability**.

---

## Traceability Context

Decision-gate fields are derived from RGDS decisions that are traceable to:

IND Requirement  
→ Observed Gap ([IND-GAP-XXX](./ind-requirements-gap-log.md))  
→ Backlog Item ([P0/P1/P2-BL-XXX](../backlog/ind-aligned-backlog.md))  
→ RGDS Decision Artifact (JSON)

Traceability is preserved through stable identifiers and drill-through links.

---

## Canonical Extract Fields

| Field | Type | Purpose |
|------|------|---------|
| decision_id | string | Stable join key across artifacts |
| program_id | string | Portfolio and program rollups |
| gate | string | Phase-gate anchor (e.g., IND-enabling, CMC readiness) |
| decision_category | enum | `internal` or `regulatory_interaction` |
| decision_outcome | enum | `go`, `conditional_go`, `no_go`, `defer`, `defer_with_required_evidence` |
| decision_status | enum | `draft`, `in_review`, `approved`, `superseded` |
| evidence_coverage_score | number | Executive-level signal of evidence posture (0–100) |
| missing_evidence_count | number | Count of declared evidence gaps |
| residual_risk_level | enum | `low`, `medium`, `high` |
| approver_roles | string[] | Accountability surface (roles, not names) |
| decision_date | date-time | Time-to-decision tracking |
| reentry_due_date | date | For deferred decisions, expected re-entry timing |
| gap_ids | string[] | Referenced IND-GAP identifiers |
| backlog_ids | string[] | Referenced backlog item identifiers |
| decision_record_link | string (URL) | Drill-through link to decision log JSON |

---

## Suggested Transformations

From RGDS decision log JSON:

- `program_id` ← `program_context.program_id`
- `gate` ← `decision_context.gate`
- `decision_category` ← `decision_context.category`
- `decision_outcome` ← `decision_outcome.outcome`
- `decision_status` ← `governance.status`
- `missing_evidence_count` ← `len(evidence_gaps)`
- `evidence_coverage_score` ← derived from evaluation summary (not computed in BI)
- `residual_risk_level` ← `risk_summary.residual_risk_level`
- `approver_roles` ← unique roles in `governance.approvals[]`
- `reentry_due_date` ← earliest due date in `actions[]` linked to re-entry conditions
- `gap_ids` ← referenced `IND-GAP-XXX` identifiers
- `backlog_ids` ← referenced `P*-BL-XXX` identifiers
- `decision_record_link` ← URL to decision log JSON in repo or system of record

---

## Power BI Usage Notes

- Treat this extract as a **read-only semantic layer**.
- Use `decision_id` as the primary join key.
- Preserve `decision_record_link` for audit drill-through.
- Do **not** infer or compute confidence, evidence quality, or risk in BI.
  These must be explicitly captured in the decision log.
- Filters commonly used in governance forums:
  - gate
  - decision_outcome
  - residual_risk_level
  - missing_evidence_count
  - reentry_due_date

---

## Relationship to Other Artifacts

- Gap Log: [evaluation/ind-requirements-gap-log.md](./ind-requirements-gap-log.md)
- Backlog: [backlog/ind-aligned-backlog.md](../backlog/ind-aligned-backlog.md)
- Requirements Traceability Matrix:  
  [evaluation/requirements-traceability-matrix.md](./requirements-traceability-matrix.md)
- Decision Schema:  
  [decision-log/decision-log.schema.json](../decision-log/decision-log.schema.json)

---

## Notes

- This extract may evolve as governance needs change, but field additions should remain backward-compatible.
- Any new fields must remain derivable from the decision log JSON.
- BI tooling must not become a decision authority.

The Decision Gate Extract exists to **support decisions, not replace them**.
