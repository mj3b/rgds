# RGDS Governance Model
**How decisions are owned, reviewed, approved, and escalated**

---

## Purpose

The RGDS governance model ensures that **decisions remain human-owned, auditable, and defensible** while benefiting from structured evidence and bounded AI assistance.

Governance in RGDS is not an overlay.  
It is embedded directly into the decision record.

---

## IND delivery alignment (v1.3)

In real IND execution, many failures are **governance failures** that surface late:

- interdependencies are underestimated
- vendor inputs arrive late or out of sequence
- teams draft with placeholders (“author-at-risk”) without making the risk explicit
- reviewer routing becomes triage under time pressure
- content lock points are unclear during rolling publishing

RGDS v1.3 treats these as *first-class decision elements* through optional fields such as:
`risk_posture`, `author_at_risk_items[]`, `review_plan`, `scope_change_events[]`, `dependency_map[]`, `data_readiness_status[]`, `publishing_plan`, and `tpp_links[]`.

For a cross-role view of who owns what, see `docs/role-decision-artifact-matrix.md`.

---

## Core principles

1. **Humans decide; systems assist**
2. **Authority is explicit, not implied**
3. **Risk is accepted knowingly or not at all**
4. **No decision is final without traceable ownership**
5. **Stopping is a valid and respected outcome**

---

## Decision roles

### Decision Owner
- Accountable for the decision outcome and rationale
- Ensures the decision question is clearly framed
- Confirms evidence and risks are represented accurately
- Owns follow-through on conditions or actions

There is exactly **one** Decision Owner per decision.

---

### Reviewers
- Assess evidence quality and completeness
- Surface gaps, assumptions, and risks
- Do not approve or reject decisions

Reviewers challenge the decision *before* it reaches approvers.

---

### Approvers
- Accept or reject the decision and its residual risk
- May approve, reject, or request changes
- Are explicitly recorded with timestamps

Approvers do not delegate risk acceptance implicitly.

---

### Quality
- Confirms governance completeness
- Ensures evidence and approvals are audit-ready
- Does not override decision authority unless required by policy

Quality protects the process, not the outcome.

---

## Approval methods

RGDS supports multiple approval paths:

- **Meeting vote** — synchronous executive or gate review
- **Asynchronous sign-off** — documented approvals within a defined window
- **Delegated authority** — pre-approved authority with scope and limits

The approval method is always recorded in the Decision Log.

---

## Conditional decisions

Conditional-go decisions are permitted when:

- gaps are bounded and understood
- risks are explicitly documented
- closure actions have named owners and due dates

Conditions are not suggestions.  
They are **governance commitments**.

Failure to close conditions requires escalation or re-review.

---

## No-Go and Deferral decisions

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
- superseding decision record

All escalations are documented.

---

## Record lifecycle

- Draft → In review → Decided → Superseded
- Superseded decisions are retained for traceability
- Controlled records are immutable except through versioned updates

The Decision Log is the system of record for governance.

---

## What governance does not do

- It does not automate approvals
- It does not replace expert judgment
- It does not eliminate disagreement

It ensures disagreement is **visible, owned, and resolved before the gate closes**.

