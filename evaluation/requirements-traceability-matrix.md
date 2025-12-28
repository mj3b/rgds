# Requirements Traceability Matrix (RTM)

This matrix provides end-to-end traceability from external IND requirements to:
- observed delivery gaps,
- planned RGDS backlog work, and
- concrete implementation artifacts.

It supports governance review, audit readiness, and decision defensibility.
This RTM documents alignment and intent; it does not prescribe implementation.

---

## Traceability Model

Each requirement follows the traceability chain below:

IND Requirement  
→ Observed Gap (IND-GAP-XXX)  
→ Backlog Item (P0/P1/P2-BL-XXX)  
→ RGDS Artifact(s)

---

## Requirements Traceability Table

| Requirement ID | Requirement Description | Gap ID(s) | Backlog Item ID(s) | RGDS Artifact(s) | Status | Notes |
|----------------|--------------------------|-----------|--------------------|------------------|--------|-------|
| IND-PREIND-008 | Pre-IND interactions, pauses, and regulatory questions must be traceable and reviewable | IND-GAP-001 | P0-BL-001 | examples/rgds-dec-0003-defer-required-evidence.json<br>docs/decision-log.md<br>docs/governance.md | Planned | Addresses undocumented pre-IND decision pauses |
| IND-TPP-009 | Program decisions should be traceable to Target Product Profile (TPP) claims | IND-GAP-002 | P0-BL-002 | decision-log/decision-log.schema.json<br>docs/decision-log.md | Planned | Enables label-oriented rationale linkage |
| IND-PHASE-004 | Conditional decisions must explicitly document unmet evidence and follow-up actions | IND-GAP-003, IND-GAP-005 | P0-BL-003, P1-BL-004 | decision-log/decision-log.schema.json<br>examples/<br>scripts/validate_all_examples.py | Planned | Separates deferral from approval semantics |
| IND-FLEX-007 | Deferred decisions must retain ownership and accountability | IND-GAP-004 | P0-BL-003 | scripts/validate_all_examples.py<br>.github/workflows/validate.yml | Planned | Prevents accountability loss over time |
| IND-ALIGN-010 | Identifiers must remain consistent across evidence and decisions | IND-GAP-006 | P1-BL-005 | docs/decision-log.md<br>evaluation/evidence-quality-rubric.md | Planned | Reduces manual reconciliation during review |
| IND-BENCH-011 | Submission timelines and benchmarks must be explicit at decision time | IND-GAP-007 | P2-BL-006 | decision-log/decision-log.schema.json<br>docs/decision-log.md | Planned | Supports timing-aware decision evaluation |

---

## Artifact References

- Gap Log: evaluation/ind-requirements-gap-log.md  
- Backlog: backlog/ind-aligned-backlog.md  
- Decision Schema: decision-log/decision-log.schema.json  
- Evaluation Plan: evaluation/evaluation-plan.md  

---

## Notes on Usage

- A single requirement may map to multiple gaps and backlog items.
- Backlog IDs are the authoritative execution linkage.
- Status reflects planning intent, not implementation completion.
- This matrix should be updated as backlog items move from Planned to Implemented.

This RTM is expected to evolve alongside the RGDS schema and evaluation artifacts.
