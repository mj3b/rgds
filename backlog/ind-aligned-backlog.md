# IND-aligned Backlog (derived from documented IND requirement gaps)

This backlog converts IND webinar requirement gaps into sprint-ready RGDS work items.
It is a planning and traceability artifact, not a normative specification.

See: `evaluation/ind-requirements-gap-log.md` for source gap traceability.

---

## P0-BL-001 — Add IND / Regulatory Interaction decision pattern + example  
*(pre-IND pause, questions, outcomes)*

- Status: Planned
- Requirement(s): IND-PREIND-008
- Files:
  - `examples/rgds-dec-0003-defer-required-evidence.json`
  - `docs/decision-log.md`
  - `docs/governance.md`
- Description:  
  Provide a canonical decision example that logs a pre-IND interaction trigger (e.g., emerging tox signal), captures questions posed to regulators, records feedback placeholders, and defines explicit re-entry actions.

---

## P0-BL-002 — Link decisions to Target Product Profile (TPP) claims  
*(minimal, non-domain-specific field)*

- Status: Planned
- Requirement(s): IND-TPP-009
- Files:
  - `decision-log/decision-log.schema.json`
  - `docs/decision-log.md`
- Description:  
  Add an optional `program_context.tpp_refs[]` field and document usage so decision rationale can be traced to label-oriented program targets without embedding domain logic.

---

## P0-BL-003 — Add semantic validator enforcing completeness for gated decisions

- Status: Planned
- Requirement(s): IND-PHASE-004, IND-FLEX-007
- Files:
  - `scripts/validate_all_examples.py`
  - `.github/workflows/validate.yml`
- Description:  
  Enforce semantic completeness in CI:
  - `conditional_go` must include explicit conditions
  - `defer_with_required_evidence` must include gaps and required actions
  - Evidence items must include confidence and quality notes

---

## P1-BL-004 — Add decision_outcome enum: `defer_with_required_evidence`

- Status: Planned
- Requirement(s): IND-PHASE-004
- Files:
  - `decision-log/decision-log.schema.json`
  - `examples/`
- Description:  
  Extend the schema with a `defer_with_required_evidence` outcome, add a canonical example, and update supporting documentation.

---

## P1-BL-005 — Add nomenclature / identifier guidance + optional consistency checks

- Status: Planned
- Requirement(s): IND-ALIGN-010
- Files:
  - `docs/decision-log.md`
  - `evaluation/evidence-quality-rubric.md`
- Description:  
  Document guidance for maintaining consistent compound, study, and artifact identifiers across decisions and evidence. Provide recommended controlled vocabulary for gates and optional consistency check hooks.

---

## P2-BL-006 — Add timeline and benchmark capture fields in `program_context`

- Status: Planned
- Requirement(s): IND-BENCH-011
- Files:
  - `decision-log/decision-log.schema.json`
  - `docs/decision-log.md`
- Description:  
  Add fields to record planned submission date, last-data-cut date, and key assumptions to support timeline-aware decision-making.
