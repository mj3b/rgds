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

---

## Decision outcomes

RGDS supports the following outcomes:

- `go`
- `no_go`
- `conditional_go`
- `defer`
- `defer_with_required_evidence` — a governed defer pattern that explicitly records missing evidence and re-entry criteria

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
- A system that optimizes for speed at the expense of accountability

AI assistance, if used, is explicitly disclosed and bounded.  
AI outputs are **never treated as evidence by default**.

---

## Decision Log as a Governance Artifact

In RGDS, the Decision Log is not “documentation after the fact.”  
It is the **mechanism** that prevents ambiguity from becoming unowned risk.

If a required field is missing, that is a **governance failure**, not a formatting issue.

---

## Options are mandatory

Every decision log must enumerate **at least two options** in `options_considered` — even when the choice feels obvious.

- “Proceed” vs “Defer” counts as two options.
- The selected outcome **must** map to a `selected_option_id`.

**Conceptual example:**

| option_id | option_text | when it’s valid |
|---|---|---|
| A | Proceed now | Evidence is sufficient within declared risk posture |
| B | Defer | Missing evidence, unresolved dependencies, or unacceptable residual risk |

---

## Evidence completeness classification

Each evidence item must declare a completeness state:

- `complete` — verified, source-linked, and decision-ready  
- `partial` — materially informative but missing some expected components  
- `placeholder` — a known gap (e.g., “TBD”) recorded for planning but **not** treated as supporting evidence  

This classification is captured **per evidence item**  
(e.g., `evidence.evidence_items[].completeness_state`).

Any summary or roll-up completeness field is **derived** and is not authoritative.

---

## Residual risk is required

Residual risk is what remains true **after** you proceed — even when conditions are applied.

A “GO” decision is not “risk-free.”  
RGDS requires residual risk to be stated explicitly so decision owners can defend *what they accepted*.

Record residual risk as:
- a summary statement (e.g., `risk_assessment.residual_risk_statement`)
- and, when useful, structured items (e.g., `risk_assessment.residual_risk_items[]`)

A decision record missing residual risk is **governance-incomplete** under v2.0.0.

---

## Decision deadlines

Regulated decisions expire.

RGDS requires a `decision_deadline` so stakeholders can distinguish:
- a decision that is still valid, from
- a decision that has become stale due to new evidence, scope changes, or timeline shifts

---

## When the Decision Log is created

A Decision Log is created when **a real decision must be defended later**, including:

- phase-gate readiness decisions
- executive go / no-go reviews
- quality or data readiness determinations
- conditional approvals with follow-up actions
- decisions that explicitly accept residual risk

Drafts may exist, but the log becomes a **controlled record** once a decision is finalized.

Once controlled, changes require explicit change tracking and may trigger re-review.

---

## How the Decision Log is structured

The schema is intentionally opinionated.  
Each section exists to prevent a known failure mode.

---

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

The rationale should explain *why this decision made sense then* — not re-argue the analysis.

---

### 3. Evidence packet  
**Prevents:** evidence drift and selective memory.

Captures:
- what evidence was actually used
- where it lives
- who owns it
- how fresh it was at decision time
- a human-assigned confidence rating
- per-item completeness classification

This makes it explicit when decisions are made with incomplete or uneven evidence.

---

### 4. Known gaps and assumptions  
**Prevents:** hidden risk accumulation.

If something is missing, uncertain, or assumed:
- it is named
- its impact is described
- a mitigation or verification plan is recorded

---

## IND-aligned decision fields (v1.3 → extended in v2.0)

The following fields reflect **real IND delivery constraints**—interdependencies, author-at-risk drafting, reviewer triage, and lock points.

They were introduced in v1.3 and extended in later versions.

These fields are optional by default but may be required by program governance.

### risk_posture  
**Prevents:** silent risk acceptance.

Captures the phase-appropriate stance  
(`risk_minimizing` / `risk_neutral` / `risk_accepting`)  
and the conscious trade-offs being made.

### author_at_risk_items[]  
Models drafting-at-risk as a governed choice with verification criteria and owners.

### review_plan  
Makes compressed review governance explicit.

### scope_change_events[]  
Logs late discoveries and scope volatility.

### dependency_map[]  
Surfaces interdependencies that materially affect risk or schedule.

### data_readiness_status[]  
Provides a lightweight readiness view for rate-limiting items.

### publishing_plan  
Captures rolling publish intent and lock points.

### tpp_links[]  
Ensures decisions trace back to Target Product Profile intent.

---

### 5. Risk assessment  
**Prevents:** unowned or accidental risk acceptance.

Captures:
- key risks
- mitigations
- residual risk
- whether explicit risk acceptance occurred

---

### 6. Governance and accountability  
**Prevents:** unclear ownership and post-hoc blame.

Captures:
- decision owner
- reviewers and approvers
- approval method
- individual approvals with timestamps

---

### 7. AI assistance disclosure  
**Mandatory when AI is used**

**Prevents:** silent automation risk.

If AI assistance is used:
- the use case is disclosed
- tools and purposes are named
- human review is recorded
- overrides are documented
- AI risk assessment is captured

Disclosure is informational only.  
Authority and risk ownership remain human.

---

### 8. Actions, dependencies, and follow-up  
**Prevents:** decisions that stop at the meeting.

Captures:
- follow-up actions
- owners and due dates
- dependencies affecting execution

---

### 9. Audit trail and lifecycle  
**Prevents:** record tampering and ambiguity over time.

Captures:
- versioning
- change history
- superseded decisions
- retention class (draft vs controlled)

Controlled records are immutable except through documented change control.

---

## Decision category

RGDS distinguishes between:

- **internal** — delivery/governance decisions (default)
- **regulatory_interaction** — decisions about regulatory engagement or interpretation

When `decision_category = regulatory_interaction`, the log must include a
`regulatory_context` block capturing interpretation risks and follow-up actions.

---

## Optional Target Product Profile context

`program_context.target_product_profile` is optional.

It grounds decisions in development intent but does not assert label claims or completeness.

---

## How this supports regulated delivery

The Decision Log enables:

- faster decisions without reduced confidence
- clearer executive approvals
- cleaner audits
- earlier surfacing of misalignment
- reduced rework caused by late-discovered risk

When asked *“Why did you decide this — and who agreed?”*  
the Decision Log is the answer.
