# Changelog

All notable changes to this repository are documented here.

## v1.3.0 — IND delivery alignment (webinar-grounded)

**Focus:** incorporate real IND execution constraints (interdependencies, author-at-risk, reviewer triage, lock points, and explicit risk posture) into RGDS as auditable decision fields — without introducing autonomy.

### Added
- `docs/role-decision-artifact-matrix.md` — A cross-role blueprint mapping PM, Regulatory, CMC, Medical Writing PM, Submission Ops, Quality, and the Principal AI Business Analyst to the recurring decisions they own and the RGDS fields that capture them.
- New optional decision-log fields aligned to IND execution: risk posture, author-at-risk items, review plan / triage, scope change events, dependency map, data readiness status, publishing/lock plan, and TPP links.
 

### Changed
- Updated `decision-log.schema.*` and `decision-log.template.yaml` to support the added IND-aligned fields.
- Updated `docs/governance.md` and `docs/decision-log.md` to reflect webinar-grounded delivery reality (kickoff-as-governance, interdependencies, reviewer triage, lock points).
- Updated `README.md` to point to the new matrix and examples.

### Notes
- v1.3.0 keeps RGDS explicitly non-agentic: AI may assist with bounded, reviewable tasks, but never decides or approves.
