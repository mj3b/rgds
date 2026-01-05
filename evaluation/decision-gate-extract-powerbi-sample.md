# Decision Gate Extract — Sample Power BI Schema & Dataflow

This document provides a concrete example of how the
[RGDS Decision Gate Extract](./decision-gate-extract.md)
can be operationalized in a BI tool such as Power BI.

It is **illustrative, not prescriptive**.  
The RGDS decision log JSON remains the **authoritative source of truth**.

---

## Sample Use Case

**Audience**
- Executive phase-gate forums
- Portfolio governance reviewers
- Program leadership

**Primary Questions**
- Which programs are blocked, deferred, or conditionally approved?
- Where is evidence incomplete or explicitly acknowledged as partial?
- Which decisions require re-entry and when?
- What residual risk has been knowingly accepted at each gate?

---

## Sample Power BI Data Model (Logical)

### Core Table: `DecisionGateExtract`

This table is a **read-only, flattened view** derived from RGDS decision logs.

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| decision_id | Text | Stable join key |
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
| decision_record_link | Text (URL) | Drill-through to decision JSON |

No column in this table confers authority or approval.

---

## Sample Power BI Dataflow (Source → Transform → Load)

### Source
- RGDS decision log JSON files  
  (see [decision-log/decision-log.schema.json](../decision-log/decision-log.schema.json))
- Location:
  - GitHub repository
  - or document store / data lake

### Transform (Power Query / M-style logic)

**Field derivations (source → extract)**

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
- referenced `IND-GAP-XXX` identifiers → `gap_ids`
- referenced backlog identifiers → `backlog_ids`
- decision JSON URL → `decision_record_link`

**Explicit exclusions**
- Do NOT compute scores, confidence bands, or sufficiency judgments in BI
- Do NOT infer evidence quality beyond declared completeness states
- Do NOT override or reinterpret decision outcomes

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
- Conditional and deferred decisions spotlight

### 2. Evidence Posture
- Decisions with incomplete evidence items
- Distribution of completeness states
- Explicitly accepted residual risk summaries

### 3. Re-entry Tracking
- Upcoming re-entry due dates
- Overdue deferred decisions
- Decision outcomes by re-entry status

### 4. Drill-Through
- Click decision → open `decision_record_link`
- Reviewer inspects full RGDS decision log JSON

---

## Governance Guardrails

- BI dashboards are **decision-support only**
- Decision authority remains with humans
- RGDS decision logs are the audit record
- BI must never mutate, approve, or reinterpret decision data

---

## Relationship to RGDS Artifacts

This sample Power BI schema and dataflow is grounded in:

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

---

## Notes

This sample demonstrates feasibility and intent.  
It does not mandate Power BI, specific tooling, or implementation details.

The goal is **decision clarity at scale**, without compromising governance.

