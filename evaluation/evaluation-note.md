# RGDS Evaluation Note

This note provides **context and interpretive guidance** for RGDS evaluation artifacts.  
It does **not** define acceptance criteria, pass/fail rules, or scoring thresholds.

The authoritative evaluation definition lives in:
- **Evaluation Plan**  
  → [evaluation/evaluation-plan.md](./evaluation-plan.md)

---

## Purpose

RGDS evaluation artifacts assess whether a
**human-governed decision-support system**
operates in a way that is:

- defensible under regulatory scrutiny,
- transparent to reviewers,
- supportive (not substitutive) of human judgment.

This note explains the **intent and framing** behind the evaluation measures used elsewhere in the repository.

---

## What RGDS Evaluation Is (and Is Not)

**RGDS evaluation is:**
- focused on decision quality and governance execution
- concerned with whether decisions are *defensible*, not merely fast
- designed to surface gaps, risks, and misuse early

**RGDS evaluation is not:**
- model benchmarking
- algorithm performance scoring in isolation
- automated approval or rejection logic

---

## Evaluation Measures (Conceptual)

RGDS evaluation focuses on **decision quality and governance behavior**, not AI capability alone.

Common evaluation dimensions include:

- **Task-level accuracy**  
  Fidelity of extraction, comparison, and structuring tasks used in support of decisions

- **Missed-risk rate**  
  Frequency of gaps, risks, or dependencies that were not surfaced prior to decision close

- **Human override rate**  
  Proportion of AI-assisted outputs that are edited, corrected, or rejected by humans

- **Time-to-decision delta**  
  Change in decision latency when structured support or AI assistance is used

- **Decision confidence delta**  
  Structured reviewer confidence before vs. after decision artifact preparation

These measures are **signals**, not outcomes.

Formal definitions, scoring methods, and evaluation cadence are specified in the
[Evaluation Plan](./evaluation-plan.md).

---

## Governing Principle

AI-assisted outputs are **not treated as evidence by default**.

They are:
- drafting aids,
- analytical supports,
- comparison accelerators,

unless explicitly reviewed, validated, approved, and logged by a human decision owner.

This principle applies across **all RGDS evaluation artifacts**.

---

## Relationship to Other Evaluation Artifacts

This note should be read alongside:

- **Evaluation Plan**  
  → [evaluation/evaluation-plan.md](./evaluation-plan.md)

- **Evidence Quality Rubric**  
  → [evaluation/evidence-quality-rubric.md](./evidence-quality-rubric.md)

- **Decision Gate Extract**  
  → [evaluation/decision-gate-extract.md](./decision-gate-extract.md)

- **Decision Gate Extract — Power BI Sample**  
  → [evaluation/decision-gate-extract-powerbi-sample.md](./decision-gate-extract-powerbi-sample.md)

- **Requirements Traceability Matrix**  
  → [evaluation/requirements-traceability-matrix.md](./requirements-traceability-matrix.md)

This note exists to support **consistent interpretation** of those artifacts,
not to override or redefine them.

---

## Final Note

RGDS evaluation exists to answer a single question:

> *Are decisions being made in a way that can be explained, defended, and trusted later?*

Metrics support that goal.  
They do not replace human judgment.

