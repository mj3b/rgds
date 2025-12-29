# Role–Decision–Artifact Matrix (IND-aligned)

This document defines **who owns which decisions** during IND execution and **where those decisions are recorded** within RGDS.

Its purpose is to prevent ambiguity about ownership, authority, and accountability when decisions span multiple functions under compressed timelines.

---

## Roles explicitly supported by RGDS

RGDS is designed to support coordinated decision-making across the following roles:

- Program / Project Management  
- Regulatory Strategy  
- CMC / Module 3 Subject-Matter Experts  
- Medical Writing Leadership and Medical Writing Project Management  
- Regulatory Operations and Submission Management  
- Quality and Compliance  
- Principal AI Business Analyst  
  *(phase-gate facilitation, decision-support reporting, AI governance)*

RGDS does **not** replace these roles.  
It provides a shared decision record that makes cross-functional ownership explicit.

---

## Decision surfaces that routinely span roles

The following decision surfaces consistently cut across functional boundaries in IND delivery and are common sources of downstream rework when left implicit:

1. **Kickoff as governance**  
   Establishes scope truth, RACI clarity, interdependencies, timeline assumptions, and decision authority—not just project logistics.

2. **Author-at-risk decisions**  
   Controlled use of placeholders with explicit verification criteria, owners, and due dates.

3. **Late-breaking change triage**  
   Determines who must review changes, what must propagate across documents, and how content locks are enforced under time pressure.

4. **Risk posture alignment**  
   Makes the program’s stance (aggressive / balanced / conservative) explicit, including acceptance criteria and contingency planning.

5. **Target Product Profile (TPP) linkage**  
   Ensures each gate decision can be traced to the development intent it supports.

These are decision points—not execution details—and require explicit ownership.

---

## RGDS fields that capture IND delivery reality (v1.3)

The following RGDS fields exist specifically to record these cross-functional decision surfaces:

- `risk_posture`  
- `author_at_risk_items[]`  
- `review_plan` *(including reviewer triage rules)*  
- `scope_change_events[]`  
- `dependency_map[]`  
- `data_readiness_status[]`  
- `publishing_plan` *(rolling publish intent and lock points)*  
- `tpp_links[]`

These fields are **optional by default**, but may be required by program governance.  
Once required, they are enforced as part of the controlled decision record.

---

## Relationship to other RGDS documentation

- **`docs/decision-log.md`** defines how these fields are used within a defensible decision record.  
- **`docs/governance.md`** defines how enforcement, escalation, and approval authority are applied.

This matrix exists to ensure that ownership is explicit **before** decisions are made—not reconstructed afterward.
