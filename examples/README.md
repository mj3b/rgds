# RGDS Canonical Decision Records

Six decision records demonstrate the complete RGDS operating model across every decision outcome and governance scenario. Each record is schema-validated in CI/CD on every commit.

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
   │Conditional│        │  No-Go    │         │  Defer    │
   │    Go     │        │           │         │           │
   │           │        │Risk thresh│         │ Missing   │
   │Conditions │        │exceeded.  │         │ required  │
   │owned.     │        │Re-entry   │         │ evidence. │
   │Deadlines  │        │logic set. │         │ Re-review │
   │named.     │        │           │         │ criteria. │
   └───────────┘        └───────────┘         └───────────┘

         ┌─────────────────────┬─────────────────────┐
         │                     │                     │
         ▼                     ▼                     ▼
   ┌───────────┐        ┌───────────┐         ┌───────────┐
   │  DEC-0004 │        │  DEC-0005 │         │  DEC-0006 │
   │           │        │           │         │           │
   │ Escalate  │        │Conditional│         │Conditional│
   │           │        │    Go     │         │    Go     │
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
| [`rgds-dec-0003`](rgds-dec-0003-defer-required-evidence.json) | defer | Structured pause with evidence gap documentation | When evidence is incomplete |
| [`rgds-dec-0004`](rgds-dec-0004-regulatory-interaction.json) | escalate | Agency-facing decision framing and question strategy | Pre-IND or FDA interaction |
| [`rgds-dec-0005`](rgds-dec-0005-ind-conditional-go-author-at-risk.json) | conditional_go | Author-at-risk drafting, reviewer triage, lock points | IND authoring and review |
| [`rgds-dec-0006`](rgds-dec-0006-ai-assisted-conditional-go.json) | conditional_go | AI disclosure fields, human override log, authority chain | AI-assisted decisions |

---

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
  8. AI Assistance       → Disclosure fields (when AI was used)
```

---

## AI Usage in Examples

`rgds-dec-0006` is the **only** record demonstrating AI-assisted decision preparation. All other records are fully human-authored.

This is a design choice: RGDS is AI-optional. Every decision must remain defensible in the absence of AI assistance. AI involvement in one record does not imply AI involvement in governance as a default.

The AI governance policy governing all records: [`docs/ai-assistance-policy.md`](../docs/ai-assistance-policy.md)

---

## How to Read a Decision Record

```
{
  "decisionid": "RGDS-DEC-0001",        ← Unique identifier
  "decisiontitle": "...",               ← Human-readable summary
  "decisionquestion": "...",            ← The specific choice required
  "decisiondeadline": "...",            ← When decision was required

  "options_considered": [               ← At least 2 required
    { "optionid": "OPT-A",
      "optiontext": "...",
      "rejected": true,
      "rejectionreason": "..." },       ← Why this option was not chosen
    { "optionid": "OPT-B",
      "optiontext": "...",
      "rejected": false }               ← The chosen option
  ],

  "evidence": {
    "evidence_items": [
      { "source": "...",
        "completeness_state": "partial", ← complete / partial / placeholder
        "summary": "..." }
    ]
  },

  "risk_posture": "...",                ← What risk was explicitly accepted
  "risk_assessment": {
    "residual_risk_items": [...]        ← What remains true after proceeding
  },

  "outcome": "conditional_go",          ← One of five governed types
  "conditions": [...],                  ← If conditional: owned + deadline

  "accountability": {
    "decision_owner": "...",            ← Named individual
    "approvers": [...]                  ← Named individuals with scope
  }
}
```

Executives and auditors should be able to answer "why was this decision reasonable?" from the record alone, without interviews or supplemental documents.

---

*All records schema-validated against [`decision-log.schema.json`](../decision-log/decision-log.schema.json). Apache 2.0.*
