# IND-aligned Backlog (derived from requirements gaps)

This backlog converts IND webinar requirements into sprint-ready work items for RGDS.

## P0 — Add IND/Regulatory Interaction decision pattern + example (pre-IND pause / questions / outcomes)
- Requirement(s): IND-PREIND-008
- Files: `examples/rgds-dec-0003-defer-required-evidence.json`, `docs/decision-log.md`, `docs/governance.md`
- Description: Provide a canonical decision that logs a pre-IND interaction trigger (e.g., tox signal), questions, FDA feedback placeholder, and re-entry actions.

## P0 — Link decisions to Target Product Profile (TPP) claims (minimal, non-domain-specific field)
- Requirement(s): IND-TPP-009
- Files: `decision-log/decision-log.schema.json`, `docs/decision-log.md`
- Description: Add optional program_context.tpp_refs[] (strings/objects) and document how to use it; ensures decision rationale ties to label-oriented targets.

## P0 — Add semantic validator enforcing completeness for conditional_go / defer_with_required_evidence
- Requirement(s): IND-PHASE-004, IND-FLEX-007
- Files: `scripts/validate_all_examples.py`, `.github/workflows/validate.yml`
- Description: Fail CI if conditional_go lacks conditions; if defer_with_required_evidence lacks gaps and actions; ensure evidence items include confidence and quality_notes.

## P1 — Add decision_outcome enum: defer_with_required_evidence
- Requirement(s): IND-PHASE-004
- Files: `decision-log/decision-log.schema.json`, `examples/`
- Description: Schema updated + example added; docs updated.

## P1 — Add ‘nomenclature/identifier’ guidance + optional consistency check hooks
- Requirement(s): IND-ALIGN-010
- Files: `docs/decision-log.md`, `evaluation/evidence-quality-rubric.md`
- Description: Document how to keep compound IDs consistent across evidence and decisions; provide recommended controlled vocab for gates.

## P2 — Add timeline/benchmark capture fields in program_context
- Requirement(s): IND-BENCH-011
- Files: `decision-log/decision-log.schema.json`, `docs/decision-log.md`
- Description: Record planned submission date, last-data date, and assumptions to support ‘start with the end in mind’.

