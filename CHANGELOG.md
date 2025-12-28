# Changelog

All notable changes to this repository are documented here.

## v1.3.1 — Canonical IND conditional-go example

### Added
- `examples/rgds-dec-0005-ind-conditional-go-author-at-risk.json` — Canonical IND-style **conditional_go** demonstrating:
  - author-at-risk items
  - reviewer triage rules
  - publishing lock points
  - dependency + data readiness tracking
- `docs/ai-checks/ind-consistency-scan-0005.md` — Example AI-assisted consistency checklist (informational only).
- `docs/ai-checks/ind-dependency-summary-0005.md` — Example AI-assisted dependency/lock-point summary (informational only).

### Notes
- No autonomy added. AI artifacts remain support-only and require named human reviewers with recorded dispositions.

## v1.3.0 — IND delivery alignment (webinar-grounded)

**Focus:** incorporate real IND execution constraints (interdependencies, author-at-risk drafting, reviewer triage, and publishing lock points) into RGDS as auditable decision fields — without introducing autonomy.

### Added
- `docs/role-decision-artifact-matrix.md` — Cross-role blueprint (PM, Medical Writing, CMC, Regulatory, Ops/Publishing, Quality, Principal AI BA) mapping decisions to RGDS capture fields.
- Optional decision-log fields aligned to IND execution:
  - `risk_posture`
  - `author_at_risk_items[]`
  - `review_plan`
  - `scope_change_events[]`
  - `dependency_map[]`
  - `data_readiness_status[]`
  - `publishing_plan`
  - `tpp_links[]`

### Changed
- Updated `decision-log/decision-log.schema.json` and `decision-log/decision-log.template.yaml` to support the IND-aligned fields.
- Updated `docs/governance.md` and `docs/decision-log.md` to reference IND-realities (kickoff-as-governance, interdependencies, reviewer triage, lock points).
- Updated `README.md` to point to the new matrix and examples.

### Notes
- RGDS remains explicitly non-agentic: AI may assist with bounded, reviewable tasks, but never decides or approves.
