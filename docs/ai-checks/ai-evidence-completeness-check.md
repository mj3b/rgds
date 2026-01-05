# AI Evidence Completeness Check — RGDS-DEC-0005

**Artifact type:** Informational evidence completeness review  
**Decision linkage:** RGDS-DEC-0005 (informational only; not part of the decision record)
**Authority:** None (non-decision-support)

---

## Purpose

Terminology note: Evidence states identified here must map to the schema-enforced
`completeness_state` values (`complete`, `partial`, `placeholder`) when reflected in the Decision Log.

This artifact provides a **human-reviewable check** of evidence completeness at decision time.

It exists to:
- distinguish final, draft, and placeholder evidence
- surface uneven confidence across evidence types
- prevent implicit assumptions about readiness

This artifact does **not** judge sufficiency or approve risk.

---

## Scope

This check applies to evidence referenced in support of a phase-gate decision, including:

- nonclinical study reports
- clinical protocols or summaries
- CMC references used for narrative claims
- regulatory correspondence used as decision input

AI assistance may be used to identify evidence states.  
Humans determine materiality and acceptance.

---

## Checklist

### Evidence state clarity
- [ ] Each referenced artifact is clearly identified as **final**, **audited draft**, or **placeholder**
- [ ] Placeholder evidence has explicit expected availability dates
- [ ] No placeholder is implicitly treated as final

---

### Evidence freshness
- [ ] Evidence recency is appropriate for the decision being made
- [ ] Any outdated evidence is explicitly acknowledged
- [ ] Superseded evidence is not relied upon without justification

---

### Coverage balance
- [ ] No single evidence stream (e.g., nonclinical) carries disproportionate decision weight without acknowledgment
- [ ] Gaps across disciplines are explicitly named

---

### Evidence confidence signaling
- [ ] Human-assigned confidence levels are documented where required
- [ ] Confidence reflects evidence quality, not outcome preference

---

## Findings (completed by reviewer)

### Observations
- 

### Identified gaps or ambiguities
- 

### Recommended follow-up (if any)
- 

---

## Reviewer disposition

- [ ] Evidence completeness acceptable for this decision stage  
- [ ] Gaps acknowledged and governed  
- [ ] Gaps require decision deferral or condition  

**Reviewer name:**  
**Date:**  

---

## Governance note

Evidence completeness does not require perfection.  
It requires **explicit acknowledgment of what is known, unknown, and assumed**.

Any material gaps must be reflected in the Decision Log
(e.g., `evidence_completeness`, `author_at_risk_items[]`, or decision rationale).

In RGDS v2.0.0, any findings from this check must be reflected explicitly
at the evidence-item level in the Decision Log
(e.g., `evidence.evidence_items[].completeness_state`).
This artifact itself never satisfies schema requirements.
