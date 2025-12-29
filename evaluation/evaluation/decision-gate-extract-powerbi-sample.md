# Decision Gate Extract — Sample Power BI Schema & Dataflow

This document provides a **concrete example** of how the RGDS Decision Gate Extract
can be operationalized in a BI tool such as Power BI.

It is illustrative, not prescriptive.
The RGDS decision log JSON remains the authoritative source of truth.

---

## Sample Use Case

**Audience**
- Executive phase-gate forums
- Portfolio governance reviewers
- Program leadership

**Primary Questions**
- Which programs are blocked or conditionally approved?
- Where is evidence incomplete?
- Which decisions require re-entry and when?
- What residual risk exists at each gate?

---

## Sample Power BI Data Model (Logical)

### Core Table: `DecisionGateExtract`

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| decision_id | Text | Stable join key |
| program_id | Text | Program / asset identifier |
| gate | Text | Phase gate (e.g., IND-enabling) |
| decision_category | Text | internal / regulatory_interaction |
| decision_outcome | Text | go / conditional_go / no_go / defer / defer_with_required_evidence |
| decision_status | Text | draft / in_review / approved / superseded |
| evidence_coverage_score | Decimal | 0–100 executive signal |
| missing_evidence_count | Whole Number | Count of evidence gaps |
| residual_risk_level | Text | low / medium / high |
| decision_date | DateTime | Approval or decision date |
| reentry_due_date | Date | Expected re-entry date (if applicable) |
| gap_ids | Text | Comma-separated IND-GAP identifiers |
| backlog_ids | Text | Comma-separated backlog identifiers |
| decision_record_link | Text (URL) | Drill-through to decision JSON |

This table is **read-only** in BI.

---

## Sample Power BI Dataflow (Source → Transform → Load)

### Source
- RGDS decision log JSON files
- Location:
  - GitHub repository
  - or document store / data lake

### Transform (Power Query / M-style logic)

**Field derivations (source → extract)**

- `program_context.program_id` → `program_id`
- `decision_context.gate` → `gate`
- `decision_context.category` → `decision_category`
- `decision_outcome.outcome` → `decision_outcome`
- `governance.status` → `decision_status`
- `len(evidence_gaps)` → `missing_evidence_count`
- `risk_summary.residual_risk_level` → `residual_risk_level`
- `governance.approvals[].role` → `approver_roles`
- earliest re-entry action due date → `reentry_due_date`
- referenced `IND-GAP-XXX` → `gap_ids`
- referenced `P*-BL-XXX` → `backlog_ids`
- decision JSON URL → `decision_record_link`

**Explicit exclusions**
- Do NOT compute confidence scores in BI
- Do NOT infer evidence quality
- Do NOT override decision outcomes

---

## Sample Power BI Relationships

Optional supporting tables:

### `Program`
| Column | Purpose |
|------|---------|
| program_id | Join key |
| program_name | Display |
| therapeutic_area | Slice/filter |

### `Gate`
| Column | Purpose |
|------|---------|
| gate | Join key |
| gate_order | Timeline sequencing |

Relationships:
- `DecisionGateExtract.program_id` → `Program.program_id`
- `DecisionGateExtract.gate` → `Gate.gate`

---

## Sample Dashboard Views

### 1. Phase-Gate Overview
- Count of decisions by gate
- Decision outcome distribution
- Conditional / deferred decision spotlight

### 2. Evidence Posture
- Average evidence coverage score by gate
- Programs with missing evidence > 0
- High residual risk decisions

### 3. Re-entry Tracking
- Upcoming re-entry due dates
- Overdue deferred decisions
- Decision outcome by re-entry status

### 4. Drill-Through
- Click decision → open `decision_record_link`
- Reviewer inspects full RGDS decision log JSON

---

## Governance Guardrails

- BI dashboards are **decision-support only**
- Decision authority remains with humans
- RGDS decision log is the audit record
- BI must never mutate decision data

---

## Relationship to RGDS Artifacts (Clickable)

This sample Power BI schema and dataflow is grounded in the following RGDS artifacts:

- **Decision Gate Extract (definition)**  
  [evaluation/decision-gate-extract.md](./decision-gate-extract.md)

- **IND Requirements Gap Log**  
  [evaluation/ind-requirements-gap-log.md](./ind-requirements-gap-log.md)

- **IND-aligned Backlog**  
  [backlog/ind-aligned-backlog.md](../backlog/ind-aligned-backlog.md)

- **Requirements Traceability Matrix (RTM)**  
  [evaluation/requirements-traceability-matrix.md](./requirements-traceability-matrix.md)

- **Decision Log Schema (source of truth)**  
  [decision-log/decision-log.schema.json](../decision-log/decision-log.schema.json)

- **Canonical Decision Examples**  
  [examples/](../examples/)

Reviewers are encouraged to:
1. Start with the **Decision Gate Extract definition**  
2. Inspect a **canonical decision example**  
3. Trace gaps → backlog → requirements using the RTM  
4. Return to this sample to understand how decisions surface in BI

---

## Notes

This sample demonstrates feasibility and intent.
It does not mandate Power BI, specific tooling, or implementation details.

The goal is **decision clarity at scale**, without compromising governance.
