# RGDS Canonical Decision Records

Six decision records cover three schema outcomes: `conditional_go`, `no_go`, and `defer_with_required_evidence`. The current set has no `go` or plain `defer` example. CI runs the batch validator on pushes to `main`, pull requests targeting `main`, and manual workflow runs.

---

## Decision Record Map

```
                        RGDS DECISION OUTCOMES
                               │
         ┌─────────────────────┼─────────────────────┐
         │                     │                     │
         ▼                     ▼                     ▼
   ┌───────────┐        ┌───────────┐         ┌───────────┐
   │  DEC-0001 │        │  DEC-0002 │         │  DEC-0003 │
   │           │        │           │         │           │
   │Conditional│        │  No-Go    │         │Defer with │
   │    Go     │        │           │         │required   │
   │           │        │Risk thresh│         │evidence   │
   │Conditions │        │exceeded.  │         │           │
   │owned.     │        │Re-entry   │         │Gaps and   │
   │Deadlines  │        │logic set. │         │actions    │
   │named.     │        │           │         │recorded.  │
   └───────────┘        └───────────┘         └───────────┘

         ┌─────────────────────┬─────────────────────┐
         │                     │                     │
         ▼                     ▼                     ▼
   ┌───────────┐        ┌───────────┐         ┌───────────┐
   │  DEC-0004 │        │  DEC-0005 │         │  DEC-0006 │
   │           │        │           │         │           │
   │Conditional│        │Conditional│         │Conditional│
   │    Go     │        │    Go     │         │    Go     │
   │Pre-IND    │        │           │         │           │
   │regulatory │        │IND-style. │         │AI-assisted│
   │strategy.  │        │Author-at- │         │Bounded    │
   │Agency     │        │risk.      │         │disclosure.│
   │questions  │        │Lock pts.  │         │Human auth │
   │framed.    │        │           │         │preserved. │
   └───────────┘        └───────────┘         └───────────┘
```

---

## Record Comparison

| Record | Outcome | Key Governance Pattern | Read When You Need |
|--------|---------|----------------------|-------------------|
| [`rgds-dec-0001`](rgds-dec-0001.json) | conditional_go | Explicit conditions with owned verification deadlines | The canonical starting point |
| [`rgds-dec-0002`](rgds-dec-0002-no-go.json) | no_go | Defensible refusal with documented re-entry path | To understand governed stopping |
| [`rgds-dec-0003`](rgds-dec-0003-defer-required-evidence.json) | defer_with_required_evidence | Structured pause with evidence gap documentation | When evidence is incomplete |
| [`rgds-dec-0004`](rgds-dec-0004-regulatory-interaction.json) | conditional_go | Agency-facing decision framing and question strategy | Pre-IND or FDA interaction |
| [`rgds-dec-0005`](rgds-dec-0005-ind-conditional-go-author-at-risk.json) | conditional_go | Author-at-risk drafting, reviewer triage, lock points | IND authoring and review |
| [`rgds-dec-0006`](rgds-dec-0006-ai-assisted-conditional-go.json) | conditional_go | AI disclosure fields, human override log, authority chain | AI-assisted decisions |

---

`rgds-dec-0004` records a conditional decision about a regulatory interaction. Its escalation path describes governance routing; it does not change the recorded outcome.

## What Each Record Contains

```
Every RGDS decision record carries eight governance dimensions:

  1. Decision Question    → What choice was required, with deadline
  2. Options Considered  → At least two, with rejection rationale
  3. Evidence Base       → Sources with completeness per item
                           (complete / partial / placeholder)
  4. Risk Posture        → Explicit statement of accepted risk
  5. Residual Risk       → What remains true after proceeding
  6. Outcome             → One of five governed types
  7. Accountability      → Named decision owner + named approvers
  8. AI Assistance       → Required disclosure object (used=true or false)
```

---

## AI Usage in Examples

`rgds-dec-0006` is the **only** record demonstrating AI-assisted decision preparation. All other records are fully human-authored.

This is a design choice: RGDS is AI-optional. Every decision must remain defensible in the absence of AI assistance. AI involvement in one record does not imply AI involvement in governance as a default.

The AI governance policy governing all records: [`docs/ai-assistance-policy.md`](../docs/ai-assistance-policy.md)

---

## How to Read a Decision Record

The following paths identify the main sections in each JSON record:

| Path | What to inspect |
|------|-----------------|
| `decision_id`, `decision_title`, `decision_question` | Identity and question |
| `gate.decision_deadline` | Deadline |
| `options_considered[]` | `option_id`, `description`, `pros`, `cons`, `estimated_impact` |
| `evidence.evidence_items[]` | Sources and `completeness_state` |
| `risk_posture`, `risk_assessment` | Accepted posture and residual risk |
| `decision_outcome` | `outcome`, `selected_option_id`, `conditions`, `rationale_summary` |
| `governance` | Owner, approvers, reviewers, approvals, and final signoff |
| `ai_assistance` | Required disclosure object and any recorded AI use |

`risk_assessment.residual_risk_items` is optional. A condition records `condition`, `owner`, `due_date`, and `evidence_to_close`. Validation checks structure and selected internal consistency rules; it does not verify the quality of the underlying decision.

Executives and auditors should be able to answer "why was this decision reasonable?" from the record alone, without interviews or supplemental documents.

---

*All records schema-validated against [`decision-log.schema.json`](../decision-log/decision-log.schema.json). Apache 2.0.*
