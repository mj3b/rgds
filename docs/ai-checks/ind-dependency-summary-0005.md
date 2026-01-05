# AI Dependency Summary — RGDS-DEC-0005

**Artifact type:** Informational dependency snapshot  
**Decision linkage:** RGDS-DEC-0005 (informational only; not part of the decision record)  
**Reviewed by:** Human stakeholders only  
**Authority:** None (non-decision-support)

---

## Purpose

This artifact provides a **concise, human-reviewable snapshot** of rate-limiting
dependencies that materially affect the IND Readiness Gate.

It exists to:
- surface dependencies that constrain decision timing
- support triage under compressed timelines
- make downstream propagation risk visible at decision time

This artifact does **not** replace the integrated project plan.  
It does **not** assign ownership or approve changes.

---

## Scope and use constraints

- Informational only  
- Must be reviewed by human stakeholders  
- Program and Submission Managers remain owners of the integrated plan  
- Dependencies summarized here must be reconciled with the Decision Log  

AI assistance may be used to draft this summary,
but **humans determine relevance, materiality, and action**.

---

## Rate-limiting dependencies

### 1. Final signed GLP toxicology report
- **Current state:** Audited draft used for drafting  
- **Expected availability:** 2026-02-10  
- **Why it matters:**  
  May require propagation across Module 2.6, Investigator’s Brochure,
  and protocol dosing rationale.

---

### 2. Additional stability timepoints (3-month / 6-month)
- **Current state:** In progress  
- **Expected availability:** 2026-03-01  
- **Why it matters:**  
  Supports shelf-life and storage qualifiers; may require updates
  in Module 3 and all cross-referenced text.

---

### 3. Publishing lock points
- **Lock 1:** 2026-01-18  
  *(Protocol and IB/GIP narrative freeze)*  
- **Lock 2:** 2026-01-19  
  *(eCTD assembly begins; only critical fixes with QA approval)*  

- **Why it matters:**  
  Constrains late changes and requires controlled routing
  for any post-lock updates.

---

## Triage triggers

The following events require immediate attention and potential re-review:

- **Toxicology deltas** affecting NOAEL or dosing margins  
  → Regulatory + Nonclinical + Clinical re-review required

- **Stability changes** affecting shelf-life or storage qualifiers  
  → CMC + Quality sign-off required

- **Post-lock edits** to controlled content  
  → Submission Manager approval  
  → Propagation recorded in the Decision Log

---

## Governance note

This artifact supports **decision awareness**, not decision authority.

If a dependency materially affects:
- evidence completeness,
- residual risk, or
- decision timing,

the impact must be explicitly captured in the **Decision Log**
(e.g., `dependency_map[]`, `data_readiness_status[]`, or decision rationale).

Unreviewed or undisclosed AI-generated summaries
are **not valid governance inputs**.
