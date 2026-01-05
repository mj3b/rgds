# RGDS Reviewer Checklist
**Common audit questions → traceable answers**

This checklist maps common reviewer and auditor questions
to concrete RGDS artifacts and RTM rows.

It exists to make review **finite, navigable, and defensible**.

---

## 1. “Why does this field exist?”

**Answer path:**
RTM → Gap → Backlog → Artifact

| Question | Where to Look |
|--------|---------------|
| Why require evidence completeness per item? | RTM → IND-EVID-014 |
| Why must options be enumerated? | RTM → IND-DEC-OPT-012 |
| Why require residual risk? | RTM → IND-RISK-013 |
| Why record authority scope? | RTM → IND-AUTH-017 |

→ [`evaluation/requirements-traceability-matrix.md`](../evaluation/requirements-traceability-matrix.md)

---

## 2. “How do you prevent silent risk acceptance?”

| Control | Artifact |
|------|----------|
| Residual risk required | `decision-log.schema.json` |
| Conditional actions enforced | Canonical examples |
| Deferral with required evidence | `rgds-dec-0003` |
| Governance escalation paths | `docs/governance.md` |

RTM reference: **IND-RISK-013**, **IND-PHASE-004**

---

## 3. “How do you know AI didn’t decide?”

| Safeguard | Evidence |
|---------|----------|
| AI disclosure required when used | `ai-assistance-policy.md` |
| Human approvals mandatory | `decision-log.schema.json` |
| AI outputs non-authoritative | Governance + AI Checks |
| Worked AI example | `rgds-dec-0006-ai-assisted-conditional-go.json` |

RTM reference: **IND-AI-015**, **IND-AUTH-016**

---

## 4. “What happens if evidence changes after approval?”

| Mechanism | Where Recorded |
|---------|----------------|
| Propagation declaration | Decision Log |
| Superseding decisions | Audit trail |
| Change control | `docs/change-control-log.md` |

RTM reference: **IND-PROP-018**, **IND-AUD-019**

---

## 5. “How do deferred decisions stay accountable?”

| Control | Artifact |
|-------|----------|
| Owner retained | Decision Log |
| Required evidence listed | Defer outcome |
| Re-entry logic | Canonical example 0003 |

RTM reference: **IND-FLEX-007**

---

## 6. “How do executives review this without reading JSON?”

| Tool | Purpose |
|----|---------|
| Decision Gate Extract | Flattened review view |
| Power BI sample | Portfolio visibility |
| Drill-through links | Audit traceability |

→ `evaluation/decision-gate-extract.md`  
→ `evaluation/decision-gate-extract-powerbi-sample.md`

---

## 7. “Is this a compliance framework?”

**No.**

RGDS is:
- a **decision-governance reference system**
- not regulatory advice
- not a submission template
- not an autonomous system

This is documented in:
- `README.md`
- `docs/governance.md`
- RTM scope notes

---

## Reviewer Exit Test

A reviewer should be able to:
- trace any field to a real failure mode
- find enforcement in schema or validators
- inspect at least one concrete example
- reconstruct why a decision was reasonable at the time

If not, the RTM is incomplete.
