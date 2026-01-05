# Evaluation Artifacts — How to Read This Folder

This folder contains the evaluation artifacts for **RGDS (Regulated Gate Decision Support)**.

Together, these files define **how decision quality and governance effectiveness are assessed**
in a regulated, human-governed decision-support system.

These artifacts are aligned to the **v2.0.0 whitepaper-defined governance baseline**,
including mandatory options analysis, evidence completeness classification,
residual risk capture, named human accountability, and bounded AI disclosure.

The artifacts are intentionally layered.  
They should be read **in sequence**, not as isolated documents.

---

## Recommended Reading Flow

### 1. Evaluation Note — Interpretive Context

**File:**  
[evaluation-note.md](./evaluation-note.md)

**Purpose:**  
Provides interpretive context for RGDS evaluation.

- Explains *why* specific evaluation measures exist  
- Reinforces governance principles (e.g., AI is not evidence by default)  
- Prevents misinterpretation of metrics as model benchmarking  

This document is **non-authoritative** and conceptual.  
It exists to orient readers before reviewing formal evaluation definitions.

---

### 2. Evaluation Plan — Authoritative Evaluation Contract

**File:**  
[evaluation-plan.md](./evaluation-plan.md)

**Purpose:**  
Defines **how RGDS is evaluated** as a human-governed decision-support system.

The evaluation plan specifies:
- evaluation scope
- decision quality dimensions
- governance and AI-use checks
- roles and responsibilities
- evaluation cadence and success criteria

This is the **authoritative evaluation definition**.  
All other evaluation artifacts align to this plan.

---

### 3. Evidence Quality Rubric — Scoring & Judgment Framework

**File:**  
[evidence-quality-rubric.md](./evidence-quality-rubric.md)

**Purpose:**  
Provides structured criteria for assessing whether evidence is **fit for the decision being made**.

The rubric supports:
- consistent reviewer scoring
- explicit confidence assignment
- transparent discussion of gaps and limitations

It operationalizes the “evidence quality” dimension defined in the Evaluation Plan.

---

### 4. Decision Gate Extract — Flattened, Review-Ready View

**File:**  
[decision-gate-extract.md](./decision-gate-extract.md)

**Purpose:**  
Defines a **flattened decision representation** derived from RGDS decision logs.

This extract is designed for:
- phase-gate forums
- executive reviews
- portfolio-level analysis

It preserves traceability to:
- external requirements
- observed gaps
- backlog items
- full decision log JSON

The decision log remains the **source of truth**.

The Decision Gate Extract is a **read-only derivative**
and must never be used to approve, override, or reinterpret a decision.

---

### 5. Decision Gate Extract — Power BI Sample — Operational Example

**File:**  
[decision-gate-extract-powerbi-sample.md](./decision-gate-extract-powerbi-sample.md)

**Purpose:**  
Provides a **concrete example** of how the Decision Gate Extract can be operationalized
in a BI tool (e.g., Power BI).

This sample illustrates:
- a BI-ready schema
- example transformations
- governance-focused dashboard views
- drill-through to auditable decision records

It is illustrative only and does not mandate tooling or implementation.

---

## Supporting Traceability & Scoring Artifacts

The following artifacts support **traceability, defensibility, and repeatability**
across all evaluations.

---

### 6. IND Requirements Gap Log — Why Work Exists

**File:**  
[ind-requirements-gap-log.md](./ind-requirements-gap-log.md)

**Purpose:**  
Documents observed gaps between **external IND expectations**
and common delivery practices.

Each gap:
- is assigned a stable `IND-GAP-XXX` identifier  
- is linked to one or more backlog items  
- provides evidence-backed justification for RGDS design decisions  

This artifact explains **why evaluation and backlog work exists**.

---

### 7. Requirements Traceability Matrix — End-to-End Alignment

**File:**  
[requirements-traceability-matrix.md](./requirements-traceability-matrix.md)

**Purpose:**  
Provides end-to-end traceability across:

External requirement  
→ Observed gap  
→ Backlog item  
→ RGDS artifact  

The RTM enables:
- governance review
- audit readiness
- confirmation that evaluation artifacts map back to real requirements

This is the **primary traceability artifact** for reviewers.

---

### 8. Scorecard Template — Per-Decision Capture

**File:**  
[scorecard-template.csv](./scorecard-template.csv)

**Purpose:**  
Defines a lightweight, repeatable format for capturing
**per-decision evaluation signals**, including:

- reviewer confidence
- evidence completeness
- governance execution indicators
- decision outcome context

The scorecard supports:
- per-decision evaluation
- phase-level aggregation
- retrospective trend analysis

Scorecards support **evaluation only**;
they do not constitute approval, rejection, or risk acceptance.

---

## How These Artifacts Fit Together

Evaluation Note  
→ Evaluation Plan  
→ Evidence Quality Rubric  
→ Decision Gate Extract  
→ Power BI Sample  

Supported by:  
→ IND Requirements Gap Log  
→ Requirements Traceability Matrix  
→ Scorecard Template  

- The **Note** explains intent  
- The **Plan** defines evaluation  
- The **Rubric** enables scoring  
- The **Extract** supports review  
- The **Sample** shows operationalization  
- The **Gap Log & RTM** ensure traceability  
- The **Scorecard** captures execution evidence  

Together, they ensure RGDS evaluation is:
- defensible  
- interpretable  
- auditable  
- explicitly human-governed  

---

## Notes

- Evaluation artifacts are expected to evolve as RGDS matures.
- Changes should preserve traceability and backward compatibility.
- BI tooling and AI assistance must never become decision authorities.

RGDS evaluation exists to support **better human decisions**, not to replace them.

