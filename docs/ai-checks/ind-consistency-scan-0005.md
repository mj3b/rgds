# AI Consistency Check — RGDS-DEC-0005

**Artifact type:** Informational consistency check  
**Decision linkage:** RGDS-DEC-0005 (informational only; not part of the decision record)  
**Reviewed by:** Human reviewers only  
**Authority:** None (non-decision-support)

---

## Purpose

This artifact provides a **human-reviewable checklist** of potential inconsistencies
across IND submission artifacts.

It exists to:
- surface cross-document mismatches early
- support reviewer triage under time pressure
- reduce silent propagation errors

This artifact **does not recommend decisions**, assign risk posture,
or override human judgment.

---

## Scope

This check focuses on consistency across:

- Module 2.6 (Nonclinical summaries)  
- Investigator’s Brochure (IB)  
- Protocol (Module 5)

References to Module 3 are limited to how CMC information is *described*,
not evaluated or approved.

---

## Use constraints

- Informational only  
- Must be reviewed by required human reviewers  
- Findings do not constitute evidence  
- Disposition must be recorded by a human  

AI assistance may be used to populate this checklist,
but **humans determine relevance, materiality, and action**.

---

## Checklist

### Dosing and safety margins
- [ ] NOAEL values and units consistent across Module 2.6, IB, and protocol
- [ ] Human equivalent dose (HED) calculations reference consistent assumptions
- [ ] Starting dose and escalation rules align across protocol text and synopsis tables
- [ ] Safety factor language is consistent (no conflicting qualifiers or implied certainty)

---

### Stability / shelf-life qualifiers
- [ ] Shelf-life statements are consistently qualified given available timepoints  
  *(e.g., “supported through 1-month data”)*
- [ ] Storage conditions and handling instructions match across IB and protocol
- [ ] Rolling-update language does not imply finalized timepoints prematurely

---

### Terminology and nomenclature
- [ ] Test article name, code, salt form, and formulation naming are consistent
- [ ] Units and concentration formatting are consistent (mg/kg, mg/mL, etc.)
- [ ] Study identifiers (tox study IDs, batch IDs) match across references

---

### Cross-document population consistency
- [ ] Intended clinical population description is consistent across IB and protocol
- [ ] Inclusion/exclusion rationale aligns with nonclinical safety narrative
- [ ] Disease severity assumptions do not conflict across sections

---

### Implicit claims vs available support
- [ ] Language implying safety or tolerability is appropriately qualified
- [ ] No claims exceed what is supported by available nonclinical data
- [ ] Forward-looking statements are clearly framed as planned or investigational

---

## Findings (completed by reviewer)

### Observations
- 

### Potential inconsistencies identified
- 

### Recommended follow-up actions (if any)
- 

---

## Reviewer disposition

- [ ] No material inconsistencies identified  
- [ ] Minor inconsistencies noted (no decision impact)  
- [ ] Material inconsistencies require correction before gate close  

**Reviewer name:**  
**Date:**  

---

## Governance note

This artifact supports **decision quality**, not decision authority.

If material inconsistencies are identified, they must be:
- resolved prior to decision finalization, or
- explicitly accepted and recorded in the Decision Log
  (e.g., rationale, risk assessment, or conditions).

Unreviewed or undisclosed AI-generated outputs
are **not valid governance inputs**.
