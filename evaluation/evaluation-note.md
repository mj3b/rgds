# RGDS Evaluation Note

This note provides **context and interpretive guidance** for RGDS evaluation artifacts.
It does **not** define acceptance criteria or scoring thresholds.

The authoritative evaluation definition lives in:
- **Evaluation Plan**:  
  [evaluation/evaluation-plan.md](./evaluation-plan.md)

---

## Purpose

RGDS evaluation artifacts assess whether a
**human-governed decision-support system**
operates in a way that is:

- defensible under regulatory scrutiny,
- transparent to reviewers,
- supportive (not substitutive) of human judgment.

This note explains the **intent** behind the evaluation measures used elsewhere in the repository.

---

## Evaluation Measures (Conceptual)

RGDS evaluation focuses on **decision quality and governance**, not model performance alone.

Common evaluation dimensions include:

- **Task-level accuracy**  
  Fidelity of extraction, comparison, and structuring tasks

- **Missed-risk rate**  
  Frequency of false negatives in surfaced risks or gaps

- **Human override rate**  
  Proportion of AI-assisted outputs that are edited or rejected by humans

- **Time-to-decision delta**  
  Change in decision latency with AI assistance

- **Decision confidence delta**  
  Structured reviewer scoring before vs. after AI-assisted drafting

Formal definitions, scoring methods, and thresholds are specified in the
[Evaluation Plan](./evaluation-plan.md).

---

## Governing Principle

AI-assisted outputs are **not treated as evidence by default**.

They are:
- drafting aids,
- analytical supports,
- comparison accelerators,

unless explicitly validated, approved, and logged by a human decision-maker.

This principle applies across all RGDS evaluation artifacts.

---

## Relationship to Other Evaluation Artifacts

This note should be read alongside:

- **Evaluation Plan**  
  [evaluation/evaluation-plan.md](./evaluation-plan.md)

- **Evidence Quality Rubric**  
  [evaluation/evidence-quality-rubric.md](./evidence-quality-rubric.md)

- **Decision Gate Extract**  
  [evaluation/decision-gate-extract.md](./decision-gate-extract.md)

- **Decision Gate Extract — Power BI Sample**  
  [evaluation/decision-gate-extract-powerbi-sample.md](./decision-gate-extract-powerbi-sample.md)

- **Requirements Traceability Matrix**  
  [evaluation/requirements-traceability-matrix.md](./requirements-traceability-matrix.md)

This note exists to support **consistent interpretation** of those artifacts.
