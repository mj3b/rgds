# RGDS Evaluation Plan
**How decision quality, AI assistance, and governance effectiveness are assessed**

---

## Purpose

This evaluation plan defines how RGDS is assessed as a **human-governed decision-support system**.

The goal is not to benchmark models in isolation.  
The goal is to determine whether RGDS:

- improves decision readiness and confidence
- shortens time-to-decision without lowering quality
- preserves auditability and governance
- uses AI assistance safely and transparently

Evaluation focuses on **decision outcomes and process integrity**, not model novelty.

---

## Scope

This plan applies to:

- phase-gate decisions
- executive readiness reviews
- quality or data readiness determinations
- conditional-go and no-go decisions

It covers:
- human decision quality
- evidence quality
- AI-assisted task performance (when used)
- governance execution

---

## Evaluation dimensions

### 1. Decision readiness & confidence

**Question:** Was the decision defensible at the time it was made?

Measured by:
- completeness of the decision log
- explicit articulation of risks, gaps, and assumptions
- reviewer confidence scoring (see rubric)

---

### 2. Time-to-decision

**Question:** Did RGDS reduce cycle time without increasing risk?

Measured by:
- elapsed time from evidence availability → decision sign-off
- comparison to historical baselines for similar gates

Reported as:
- absolute time (days)
- percentage reduction vs baseline

---

### 3. Evidence quality

**Question:** Was the evidence fit for the decision being made?

Measured by:
- freshness of evidence
- traceability and lineage completeness
- human-assigned confidence ratings
- documented gaps and mitigations

See `evidence-quality-rubric.md`.

---

### 4. AI-assisted task performance (if applicable)

**Question:** Did AI assistance improve efficiency without undermining trust?

Measured at the task level (not the decision level):
- extraction accuracy
- comparison fidelity
- missed-risk rate (false negatives)
- human disposition (accepted / edited / rejected)

AI outputs are never treated as evidence by default.

---

### 5. Governance execution

**Question:** Was governance explicit, timely, and complete?

Measured by:
- presence of named decision owner
- documented approvals with timestamps
- clarity of conditions and follow-up actions
- audit trail completeness

---

## Roles & responsibilities

- **Decision Owner:** Accountable for decision outcome and rationale
- **Reviewers:** Assess evidence quality and surface risks
- **Approvers:** Accept or reject the decision and residual risk
- **Quality:** Confirms evaluation artifacts are complete and auditable

---

## Evaluation cadence

- **Per decision:** Lightweight scoring captured in the scorecard
- **Per phase:** Aggregate review of trends (cycle time, overrides, no-gos)
- **Retrospective:** Identify systematic evidence or governance gaps

---

## Success criteria (illustrative)

- ≥90% of decisions rated “defensible” or higher by reviewers
- measurable reduction in time-to-decision vs baseline
- explicit documentation of gaps and assumptions in 100% of decisions
- AI assistance used only within disclosed and approved bounds

---

## What this plan does not do

- It does not optimize for model accuracy in isolation
- It does not replace expert review
- It does not automate approval decisions

RGDS is successful when **humans decide faster and with greater confidence**, not when models appear more impressive.

