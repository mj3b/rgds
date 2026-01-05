# Decision Gate Extract (Power BI–Ready)

This document defines a **flattened decision view** derived from RGDS decision logs.
It is designed for **phase-gate forums**, portfolio review, and BI dashboards (e.g., Power BI).

This extract is **not a source of truth**.  
The authoritative record remains the validated RGDS decision log JSON.

---

## Purpose and Scope

The Decision Gate Extract exists to:

- enable cross-program and portfolio-level visibility
- support executive and governance review forums
- surface evidence posture and residual risk at decision time
- preserve drill-through access to auditable decision records

This extract intentionally trades schema richness for **reviewability and comparability**.
It must never reinterpret, score, or override decisions.

---

## Traceability Context

Decision-gate fields are derived from RGDS decisions that are traceable across:

External IND expectation  
→ Observed gap ([IND-GAP-XXX](./ind-requirements-gap-log.md))  
→ Backlog item ([P0/P1/P2-BL-XXX](../backlog/ind-aligned-backlog.md))  
→ RGDS decision record (JSON)

Traceability is preserved through stable identifiers and drill-through links.

---

## Logical Extract Schema (Read-Only)

### Core Table: `DecisionGateExtract`

| Column Name | Type | Description |
|------------|------|-------------|
| decision_id | Text | Stable decision identifier |
| program_id | Text | Program / asset identifier |
| gate | Text | Phase gate (e.g., IND-enabling) |
| decision_category | Text | internal / regulatory_interaction |
| decision_outcome | Text | go / conditional_go / no_go / defer / defer_with_required_evidence |
| decision_lifecycle_state | Text | draft / in_review / decided / superseded |
| evidence_items_incomplete | Whole Number | Count of evidence items marked `partial` or `placeholder` |
| residual_risk_summary | Text | Human-authored residual risk statement |
| decision_date | DateTime | Decision approval timestamp |
| reentry_due_date | Date | Expected re-entry date (if applicable) |
| gap_ids | Text | Comma-separated IND-GAP identifiers |
| backlog_ids | Text | Comma-separated backlog identifiers |
| decision_record_link | URL | Drill-through to decision log JSON |

All fields are derived.
No column confers approval authority.

---

## Derivation Rules (Conceptual)

Typical mappings from RGDS decision logs:

- `program_context.program_id` → `program_id`
- `decision_context.gate` → `gate`
- `decision_category` → `decision_category`
- `decision_outcome.outcome` → `decision_outcome`
- `governance.lifecycle_state` → `decision_lifecycle_state`
- count of `evidence.evidence_items[].completeness_state != complete`
  → `evidence_items_incomplete`
- `risk_assessment.residual_risk_statement` → `residual_risk_summary`
- `governance.decision_timestamp` → `decision_date`
- earliest re-entry action due date → `reentry_due_date`
- referenced `IND-GAP-XXX` → `gap_ids`
- referenced backlog identifiers → `backlog_ids`
- canonical JSON URL → `decision_record_link`

Explicit exclusions:
- no scoring or confidence computation
- no inference of evidence sufficiency
- no mutation of decision outcomes

---

## Intended Dashboard Views

### Phase-Gate Overview
- Decisions by gate
- Outcome distribution
- Conditional and deferred decisions

### Evidence Posture
- Decisions with incomplete evidence items
- Distribution of completeness states

### Residual Risk Visibility
- Human-authored residual risk summaries by gate
- Decisions proceeding with explicit residual risk

### Re-entry Tracking
- Upcoming re-entry dates
- Overdue deferred decisions

### Drill-Through
- Open `decision_record_link` to inspect the full RGDS decision log

---

## Governance Guardrails

- BI outputs are **decision-support only**
- Humans remain the sole decision authorities
- RGDS decision logs remain the audit record
- Dashboards must never approve, reject, or reinterpret decisions

---

## Relationship to RGDS Artifacts

This extract is grounded in:

- Decision Gate Extract definition  
  → `evaluation/decision-gate-extract.md`
- IND Requirements Gap Log  
  → `evaluation/ind-requirements-gap-log.md`
- IND-aligned backlog  
  → `backlog/ind-aligned-backlog.md`
- Requirements Traceability Matrix  
  → `evaluation/requirements-traceability-matrix.md`
- Decision Log schema (source of truth)  
  → `decision-log/decision-log.schema.json`
- Canonical decision examples  
  → `examples/`

---

## Notes

This extract demonstrates how RGDS decisions can be surfaced at scale
without compromising governance, accountability, or auditability.

