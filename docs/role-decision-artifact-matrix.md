# Role–Decision–Artifact Matrix (IND-aligned)

This document summarizes **who owns which decisions** during IND execution and **which RGDS fields** capture those decisions.

## Roles RGDS explicitly supports

- Program / Project Management
- Regulatory Strategy
- CMC / Module 3 SMEs
- Medical Writing Leadership and Medical Writing Project Management
- Regulatory Operations and Submission Management
- Quality and Compliance
- Principal AI Business Analyst (phase gates, decision support reporting, AI governance)

## Decision surfaces that routinely span roles

1. **Kickoff-as-governance**: scope truth, RACI, interdependencies, and timeline assumptions.
2. **Author-at-risk**: placeholders with explicit verification criteria, owners, and due dates.
3. **Late-breaking change triage**: who must review, what must propagate across documents, and when content locks.
4. **Risk posture alignment**: explicit stance, acceptance criteria, and contingency planning.
5. **TPP linkage**: each gate decision ties back to the Target Product Profile.

## RGDS fields that capture IND delivery reality (v1.3)

- `risk_posture`
- `author_at_risk_items[]`
- `review_plan` (including triage rules)
- `scope_change_events[]`
- `dependency_map[]`
- `data_readiness_status[]`
- `publishing_plan` (rolling publish + lock points)
- `tpp_links[]`

For detailed governance workflow and usage guidance, see `docs/governance.md` and `docs/decision-log.md`.
