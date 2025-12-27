# Evidence Quality Rubric
**How evidence confidence is assigned in RGDS**

---

## Why this rubric exists

In regulated decisions, disagreement usually arises from **unstated differences in evidence confidence**.

This rubric standardizes how evidence quality is assessed so decisions are:
- comparable over time
- explainable during audit
- less dependent on individual judgment variance

Confidence ratings are **assigned by humans**, not models.

---

## Confidence levels

### High confidence

Evidence is:
- complete for the decision being made
- traceable to authoritative sources
- current at time of decision
- validated or reviewed where appropriate

Typical indicators:
- controlled datasets with verified lineage
- reviewed reports or dashboards with clear definitions
- QC or validation artifacts attached

---

### Medium confidence

Evidence is:
- largely complete but has bounded gaps
- traceable, but with minor unresolved issues
- sufficient for the decision with conditions or mitigations

Typical indicators:
- known missing fields with documented impact
- assumptions explicitly stated and tracked
- conditional-go decisions

---

### Low confidence

Evidence is:
- incomplete, unstable, or not fully traceable
- missing critical validation or reconciliation
- insufficient to support a defensible decision

Typical indicators:
- failed integrity checks
- unclear lineage
- unresolved discrepancies between sources

Low-confidence evidence should generally lead to:
- no-go decisions, or
- explicit deferral pending remediation

---

## How the rubric is used

- Each evidence item in the Decision Log receives a confidence rating
- Ratings are justified in `quality_notes`
- Disagreements are resolved through review, not averaging
- Confidence ratings inform—but do not determine—the decision outcome

---

## What this rubric does not do

- It does not quantify scientific truth
- It does not replace expert review
- It does not override governance decisions

Its purpose is **clarity, not control**.

