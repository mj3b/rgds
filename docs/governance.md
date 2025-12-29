# RGDS Governance Model
**How decisions are owned, reviewed, approved, and escalated**

---

## Purpose

The RGDS governance model ensures that **decisions remain human-owned, auditable, and defensible** while benefiting from structured evidence and bounded AI assistance.

Governance in RGDS is not an overlay.  
It is embedded directly into the decision record.

---

## IND delivery alignment (v1.3)

In real IND execution, many failures surface late as **governance failures**, not analytical ones:

- interdependencies are underestimated
- vendor inputs arrive late or out of sequence
- teams draft with placeholders (“author-at-risk”) without making risk explicit
- reviewer routing degrades into ad-hoc triage under time pressure
- content lock points are unclear during rolling publishing

RGDS v1.3 treats these as **first-class decision elements**, captured through optional—but governable—fields such as:

- `risk_posture`
- `author_at_risk_items[]`
- `review_plan`
- `scope_change_events[]`
- `dependency_map[]`
- `data_readiness_status[]`
- `publishing_plan`
- `tpp_links[]`

These fields make delivery constraints **visible at decision time**, rather than discovered after a gate closes.

---

## Decision authority clarity (v1.4.0)

RGDS v1.4.0 extends the governance record to make **decision rights auditable**, not assumed.

The following optional fields clarify authority without changing ownership:

- **`authority_scope`** — `recommend` | `decide` | `veto`
- **`escalation_path`** — defines who resolves deadlock when reviewers disagree or timelines compress

These fields do not redistribute power.  
They make authority, limits, and escalation **explicit and reviewable**.

For a cross-role view of ownership and artifacts, see  
`docs/role-decision-artifact-matrix.md`.

---

## Core governance principles

1. **Humans decide; systems assist**  
2. **Authority is explicit, not implied**  
3. **Risk is accepted knowingly—or not at all**  
4. **No decision is final without traceable ownership**  
5. **Stopping is a valid and respected outcome**

---

## Decision roles

### Decision Owner
- Accountable for the decision outcome and rationale
- Ensures the decision question is clearly framed
- Confirms evidence, assumptions, and risks are represented accurately
- Owns follow-through on conditions and required actions

There is exactly **one** Decision Owner per decision.

---

### Reviewers
- Assess evidence quality and completeness
- Surface gaps, assumptions, and risks
- Challenge the decision *before* approval

Reviewers do not approve or reject decisions.

---

### Approvers
- Accept or reject the decision and its residual risk
- May approve, reject, or request changes
- Are explicitly recorded with timestamps

Risk acceptance is never implicit or delegated silently.

---

### Quality
- Confirms governance completeness
- Ensures records are audit-ready
- Verifies required fields and approvals are present

Quality protects the **process**, not the outcome, unless policy requires intervention.

---

## Approval methods

RGDS supports multiple approval paths:

- **Meeting vote** — synchronous executive or gate review
- **Asynchronous sign-off** — documented approvals within a defined window
- **Delegated authority** — pre-approved authority with defined scope and limits

The approval method is always recorded in the Decision Log.

---

## Conditional decisions

Conditional-go decisions are permitted when:

- gaps are bounded and understood
- risks are explicitly documented
- closure actions have named owners and due dates

Conditions are **governance commitments**, not suggestions.

Failure to close conditions requires escalation or re-review.

---

## No-Go and deferral decisions

No-Go and defer decisions are first-class outcomes.

They are used when:
- evidence confidence is low
- integrity or traceability cannot be demonstrated
- residual risk cannot be accepted

Stopping early is treated as **risk reduction**, not failure.

---

## Escalation rules

Escalation is required when:

- conditions are not closed by due dates
- new material risks emerge post-decision
- evidence is invalidated or superseded
- approvals conflict or are withdrawn

Escalation results in:
- decision re-review, or
- a superseding decision record

All escalations are documented.

---

## Record lifecycle

- Draft → In Review → Decided → Superseded
- Superseded decisions are retained for traceability
- Controlled records are immutable except through versioned updates

The Decision Log is the system of record for governance.

---

## What governance does not do

- It does not automate approvals
- It does not replace expert judgment
- It does not eliminate disagreement

It ensures disagreement is **visible, owned, and resolved before the gate closes**.
