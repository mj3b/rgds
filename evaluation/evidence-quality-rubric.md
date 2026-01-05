# Evidence Quality Rubric  
**How evidence confidence is assigned in RGDS**

---

## Why this rubric exists

In regulated decisions, disagreement most often arises from **unstated differences in evidence confidence**, not from disagreement about outcomes.

This rubric standardizes how evidence quality is assessed so decisions are:

- comparable over time,
- explainable under audit or inspection,
- less dependent on individual judgment variance.

Confidence ratings are **assigned by humans**, not models.

---

## Confidence levels

### High confidence

Evidence is:

- complete for the decision being made,
- traceable to authoritative sources,
- current at the time of decision,
- validated or formally reviewed where appropriate.

**Typical indicators:**
- controlled datasets with verified lineage,
- reviewed reports with stable definitions,
- QC or validation artifacts attached or referenced.

---

### Medium confidence

Evidence is:

- materially informative but has bounded gaps,
- traceable with minor unresolved issues,
- sufficient to support a decision **with conditions or mitigations**.

**Typical indicators:**
- known missing elements with documented impact,
- assumptions explicitly stated and governed,
- conditional-go decisions supported by follow-up actions.

---

### Low confidence

Evidence is:

- incomplete, unstable, or not fully traceable,
- missing critical validation or reconciliation,
- insufficient to support a defensible decision.

**Typical indicators:**
- failed integrity or consistency checks,
- unclear or disputed lineage,
- unresolved discrepancies across sources.

Low-confidence evidence should generally result in:

- no-go decisions, or  
- explicit deferral pending remediation.

---

## How the rubric is used

- Each evidence item in the Decision Log receives a confidence rating.
- Ratings are justified using reviewer notes (e.g., `quality_notes`).
- Disagreements are resolved through review and escalation, not averaging.
- Confidence ratings **inform** decisions but do not determine outcomes.

---

## What this rubric does not do

- It does not quantify scientific truth.
- It does not replace expert judgment.
- It does not override governance or approval authority.

Its purpose is **clarity and consistency**, not control.

