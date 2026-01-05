# RGDS Evaluation Plan  
**How decision quality, AI assistance, and governance effectiveness are assessed**

---

## Purpose

This evaluation plan defines how RGDS is assessed as a **human-governed decision-support system**.

The goal is not to benchmark models in isolation.  
The goal is to determine whether RGDS:

- improves decision readiness and confidence,
- shortens time-to-decision without lowering quality,
- preserves auditability and governance integrity,
- uses AI assistance safely, transparently, and reversibly.

Evaluation focuses on **decision quality and governance execution**, not model novelty.

---

## Scope

This plan applies to:

- phase-gate decisions,
- executive readiness reviews,
- quality or data readiness determinations,
- conditional-go, no-go, and defer decisions.

It covers evaluation of:

- human decision quality,
- evidence quality and completeness,
- AI-assisted task performance (when AI is used),
- governance execution and accountability.

---

## Evaluation Dimensions

### 1. Decision Readiness & Defensibility

**Question:**  
Was the decision defensible at the time it was made?

**Required checks:**
- Evidence completeness is declared per item (`complete` / `partial` / `placeholder`)
- Known gaps, assumptions, and residual risk are explicitly recorded
- Cross-document or downstream impact is declared when applicable

**Measured by:**
- completeness of the decision log,
- clarity of options considered and rationale,
- explicit articulation of risks, gaps, and trade-offs,
- reviewer confidence scoring (see Evidence Quality Rubric).

---

### 2. Time-to-Decision

**Question:**  
Did RGDS reduce cycle time without increasing risk or ambiguity?

**Measured by:**
- elapsed time from evidence availability → decision sign-off,
- comparison to historical baselines for similar phase gates.

**Reported as:**
- absolute time (days),
- percentage change vs baseline.

Time reduction is only considered positive when decision defensibility is preserved.

---

### 3. Evidence Quality

**Question:**  
Was the evidence fit for the decision being made at that stage?

**Measured by:**
- evidence freshness,
- traceability and lineage completeness,
- human-assigned confidence ratings,
- explicit documentation of gaps and mitigations.

Formal scoring criteria are defined in:  
→ [`evaluation/evidence-quality-rubric.md`](./evidence-quality-rubric.md)

---

### 4. AI-Assisted Task Performance (When Used)

**Question:**  
Did AI assistance improve efficiency without undermining trust or accountability?

**Required checks (if AI is used):**
- AI usage is explicitly disclosed in the decision record
- Tool identity, purpose, and human review are recorded
- Human overrides or corrections are documented
- AI output is never treated as evidence by default

**Measured at the task level (not decision level):**
- extraction accuracy,
- comparison fidelity,
- missed-risk rate (false negatives),
- human disposition (`accepted` / `edited` / `rejected`).

AI performance is evaluated only as **decision support**, never as authority.

---

### 5. Governance Execution

**Question:**  
Was governance explicit, timely, and auditable?

**Measured by:**
- presence of a single named decision owner,
- documented reviewers and approvers with timestamps,
- clarity of approval method and authority scope,
- explicit conditions, follow-up actions, and due dates,
- completeness of the audit trail.

Governance failures are treated as **decision failures**, regardless of outcome.

---

## Roles & Responsibilities

- **Decision Owner**  
  Accountable for the decision outcome and rationale.

- **Reviewers**  
  Assess evidence quality, surface gaps and risks, and challenge assumptions.

- **Approvers**  
  Accept or reject the decision and its residual risk.

- **Quality / Governance**  
  Confirms evaluation artifacts are complete, consistent, and audit-ready.

---

## Evaluation Cadence

- **Per decision**  
  Lightweight evaluation captured using the scorecard template.

- **Per phase / program**  
  Aggregated review of trends (cycle time, overrides, deferrals, re-entries).

- **Retrospective**  
  Identification of systemic evidence, governance, or execution gaps.

---

## Success Indicators (Illustrative)

- High proportion of decisions rated defensible by reviewers
- Measurable reduction in time-to-decision vs historical baseline
- Explicit documentation of gaps, assumptions, and residual risk in all decisions
- AI assistance used only within disclosed, bounded, and human-reviewed limits

These indicators guide interpretation; they are not pass/fail gates.

---

## What This Plan Does Not Do

- It does not optimize for model accuracy in isolation
- It does not replace expert judgment or review
- It does not automate approvals or decision outcomes

RGDS is successful when **humans decide faster and with greater confidence**,  
not when models appear more sophisticated.


