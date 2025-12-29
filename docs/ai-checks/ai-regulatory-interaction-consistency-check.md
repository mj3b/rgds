# AI Regulatory Interaction Consistency Check — RGDS-DEC-0005

**Artifact type:** Informational regulatory interpretation check  
**Decision linkage:** RGDS-DEC-0005  
**Authority:** None (non-decision-support)

---

## Purpose

This artifact provides a **human-reviewable check** that regulatory interactions
(pre-IND meetings, written feedback, advice letters) are being interpreted and applied consistently.

It exists to:
- prevent over- or under-interpretation of regulatory feedback
- surface interpretation risk
- ensure assumptions are explicit before decisions are finalized

This artifact does **not** interpret regulatory intent or provide strategy.

---

## Scope

This check applies when regulatory interactions are used as decision inputs, including:

- pre-IND meeting feedback
- written advice or information requests
- informal agency communications referenced in rationale

AI assistance may be used to extract and compare statements.  
Humans own interpretation.

---

## Checklist

### Source fidelity
- [ ] Regulatory feedback is referenced verbatim or with traceable citations
- [ ] No paraphrasing introduces stronger claims than the source supports
- [ ] Context (question asked vs answer given) is preserved

---

### Interpretation clarity
- [ ] Interpretive assumptions are explicitly stated
- [ ] Distinction between *what FDA said* and *what the team infers* is clear
- [ ] Alternative interpretations have been considered where ambiguity exists

---

### Consistency across artifacts
- [ ] Regulatory interpretation is consistent across IB, protocol, and summaries
- [ ] No single artifact implies endorsement that others do not

---

### Risk acknowledgment
- [ ] Interpretation risk is explicitly acknowledged where applicable
- [ ] Contingency actions are identified if interpretation proves incorrect

---

## Findings (completed by reviewer)

### Observations
- 

### Potential inconsistencies or risks
- 

### Recommended clarifications or actions
- 

---

## Reviewer disposition

- [ ] Regulatory interpretation acceptable for this decision  
- [ ] Interpretation risk acknowledged and governed  
- [ ] Interpretation requires re-review or escalation  

**Reviewer name:**  
**Date:**  

---

## Governance note

Regulatory feedback is an **input**, not a decision.

Interpretation risk must be captured in the Decision Log
(e.g., `decision_category`, `regulatory_context`, or decision rationale).
