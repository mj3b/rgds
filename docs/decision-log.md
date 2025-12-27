# RGDS Decision Log  
**Why it exists, how it’s used, and what it protects**

---

## Purpose

The RGDS Decision Log is the **spine artifact** of Regulated Gate Decision Support.

Its purpose is not to record outcomes, recommendations, or model outputs.  
Its purpose is to **make phase-gate decisions defensible over time** by explicitly capturing:

- what decision was made
- who owned it
- what evidence was considered
- what risks were accepted
- what conditions or follow-up actions were required
- and how governance was exercised


## Decision outcomes

RGDS supports the following outcomes:

- `go`
- `no_go`
- `conditional_go`
- `defer`
- `defer_with_required_evidence` (explicit missing evidence + re-entry conditions)

In regulated environments, the failure mode is rarely “bad intent” or “bad analysis.”  
It is **implicit assumptions, undocumented trade-offs, and late-discovered misalignment**.  
The Decision Log exists to surface and record those *before* the gate closes.

---

## What the Decision Log is (and is not)

**It is:**
- A human-governed decision record for phase-gated workflows
- An audit-ready artifact that links delivery evidence to governance
- A shared contract between delivery teams, quality, and executives
- A way to preserve *decision context* after the moment has passed

**It is not:**
- An autonomous decision system
- A replacement for expert judgment
- A log of AI outputs or recommendations
- A compliance checkbox or documentation exercise

AI assistance, if used, is explicitly disclosed and bounded.  
AI outputs are **never treated as evidence by default**.

---

## When the Decision Log is created

A Decision Log is created when **a real decision must be defended later**, including:

- Phase-gate readiness decisions
- Executive go / no-go reviews
- Quality or data readiness determinations
- Conditional approvals with follow-up actions
- Decisions that accept residual risk

Drafts may exist, but the log becomes a **controlled record** once a decision is finalized.

---

## How the Decision Log is structured

The schema is intentionally opinionated. Each section exists to prevent a known failure mode.

### 1. Record identity & gate context
**Prevents:** ambiguity about *which* decision was made, when, and under what authority.

Captures:
- stable decision ID
- program / asset context
- gate type and timing
- decision deadline pressure

---

### 2. Decision statement
**Prevents:** retrospective reframing of what was actually decided.

Captures:
- the exact decision question
- options that were considered
- the selected outcome
- a concise rationale written *at the time*

The rationale is short by design.  
It should explain *why this decision made sense then*, not re-argue the analysis.

---

### 3. Evidence packet
**Prevents:** evidence drift and selective memory.

Captures:
- what evidence was actually used
- where it lives
- who owns it
- how fresh it was at decision time
- a human-assigned confidence rating

This makes it explicit when decisions are made with incomplete or uneven evidence.

---

### 4. Known gaps and assumptions
**Prevents:** hidden risk accumulation.

If something is missing, uncertain, or assumed:
- it is named
- its impact is described
- a mitigation or verification plan is recorded

This section is critical.  
Well-run programs do not avoid assumptions — they **surface them early**.

---

### 5. Risk posture
**Prevents:** unowned or accidental risk acceptance.

Captures:
- key risks, their severity and likelihood
- mitigation plans
- a clear residual risk statement
- whether explicit risk acceptance is required

This allows leadership to knowingly accept risk rather than inherit it unknowingly.

---

### 6. Governance and accountability
**Prevents:** unclear ownership and post-hoc blame.

Captures:
- decision owner
- reviewers and approvers
- approval method
- individual approvals with timestamps
- final sign-off

This makes accountability explicit without being punitive.

---

### 7. AI assistance disclosure (optional)
**Prevents:** silent automation risk.

If AI assistance is used:
- the use case is disclosed
- artifacts are referenced
- human disposition (accepted / edited / rejected) is recorded
- controls and constraints are documented

This preserves trust and auditability without banning AI.

---

### 8. Actions, dependencies, and change control
**Prevents:** decisions that stop at the meeting.

Captures:
- follow-up actions with owners and due dates
- dependencies that affect execution
- links to change control or validation artifacts

Conditional decisions only work if follow-through is visible.

---

### 9. Audit trail and lifecycle
**Prevents:** record tampering and ambiguity over time.

Captures:
- versioning
- change history
- superseded decisions
- retention class (draft vs controlled record)

This allows the organization to reconstruct decision history months or years later.

---

## How this supports regulated delivery

The Decision Log is designed to support:

- faster phase-gate decisions without lowering confidence
- clearer executive approvals
- cleaner audits and inspections
- earlier surfacing of misalignment
- reduced rework caused by late-discovered risk

It aligns delivery, governance, and decision confidence without relying on heroics or memory.

---

## Relationship to the rest of RGDS

Within RGDS:
- The Decision Log is the **primary output**
- Evaluation artifacts explain *how* decision quality is measured
- Dashboards and analyses feed evidence into the log
- Governance happens *through* the log, not around it

If RGDS were implemented in a real program, the Decision Log would be the artifact people point to when asked:

> “Why did you decide this — and who agreed?”



---

## Decision category

RGDS distinguishes between:

- **internal** — delivery/governance decisions (default)
- **regulatory_interaction** — decisions primarily about regulatory interactions (e.g., pre-IND strategy, interpreting written feedback)

When `decision_category` is `regulatory_interaction`, the log must include a `regulatory_context` block to capture:
interaction type, questions submitted, feedback received, interpretation risks, and follow-up actions.

This is intentional: regulatory feedback is not treated as “notes” or “truth” — it is treated as a **decision input** with explicit interpretation risk.

---

## Optional Target Product Profile context

`program_context.target_product_profile` is an optional context block used to ground decisions in development intent.
It is **not** a claim about label, and it is **not** validated for completeness.

Use it when it helps a reviewer answer: *“Why was this evidence sufficient for this stage?”*
