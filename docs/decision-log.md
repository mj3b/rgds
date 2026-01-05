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
- `defer_with_required_evidence` is a governed deferment that explicitly records missing evidence and re-entry criteria
  
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

## Options are mandatory

Every decision log must enumerate **at least two options** in `options_considered` — even when the choice feels obvious.

- “Proceed” vs “Defer” counts as two options.
- The selected outcome **must** map to a `selected_option_id`.

Example (conceptual):

| option_id | option_text | when it’s valid |
|---|---|---|
| A | Proceed now | Evidence is sufficient within declared risk posture |
| B | Defer | Missing evidence, unresolved dependencies, or unacceptable residual risk |

## Evidence completeness classification

Each evidence item must declare a completeness state:

- `complete` — verified, source-linked, and decision-ready
- `partial` — materially informative but missing some expected components
- `placeholder` — a known gap (e.g., “TBD”) recorded for planning but **not** treated as supporting evidence

This classification is captured per evidence item (for example: `evidence.evidence_items[].completeness_state`) and should align with any summary field such as `evidence_completeness`.

## Residual risk is required

Residual risk is what remains true **after** you proceed — even when conditions are applied.

A “GO” decision is not “risk-free.”
RGDS requires residual risk to be stated explicitly so decision owners can defend *what they accepted*.

Record residual risk as:
- a summary statement (e.g., `risk_assessment.residual_risk_statement`)
- and (when helpful) structured items (e.g., `risk_assessment.residual_risk_items[]` with triggers and mitigations)

## Decision deadlines

Regulated decisions expire.

RGDS requires a `decision_deadline` so stakeholders can distinguish:
- a decision that is still valid, from
- a decision that has become stale due to new evidence, scope changes, or timeline shifts.

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

---

## IND-aligned decision fields (v1.3)

The following fields reflect **real IND delivery constraints**—interdependencies, author-at-risk drafting, reviewer triage, and lock points.  
They are often the difference between defensible speed and downstream rework.

These fields are **optional by default**, but may be required by program governance.  
Once required, they are enforced as part of the decision record.

### risk_posture
**Prevents:** silent risk acceptance and “we never said we were being aggressive.”

Captures the phase-appropriate stance (aggressive / balanced / conservative) and the trade-offs the team is consciously making.

### author_at_risk_items[]
**Prevents:** placeholders becoming invisible, uncontrolled risk.

Models drafting-at-risk as a governed choice with explicit verification criteria, owners, and due dates.

### review_plan
**Prevents:** late-breaking edits without clear reviewer accountability.

Captures required vs optional reviewers, triage rules, and the review window used when time compresses.

### scope_change_events[]
**Prevents:** undocumented scope changes that force rework after gates close.

Logs late discoveries (“we also have report X”), approvals, and impact statements.

### dependency_map[]
**Prevents:** underestimating interdependencies across modules or workstreams.

Records only the dependencies that materially affect schedule, rework, or risk.

### data_readiness_status[]
**Prevents:** pretending key datasets are “ready” when they are audited drafts or still in flight.

Provides a lightweight readiness view for rate-limiting items at decision time.

### publishing_plan
**Prevents:** changes that arrive after lock points and create submission chaos.

Captures rolling publish intent and explicit lock dates for content freezes.

### tpp_links[]
**Prevents:** decisions that drift away from the Target Product Profile.

Ensures each gate decision can be traced to the TPP elements it supports.

These fields do not eliminate assumptions.  
They ensure assumptions are **explicit, owned, and surfaced before the gate closes**.

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
