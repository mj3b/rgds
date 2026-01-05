# Requirements Traceability Matrix (RTM)

This matrix provides **end-to-end traceability** from external IND expectations and
observed delivery risks to:

- documented delivery gaps,
- RGDS backlog work,
- and concrete RGDS implementation artifacts.

It exists to support **governance review, audit readiness, and decision defensibility**.

This RTM documents **alignment and intent**.  
It does **not** prescribe tooling or implementation choices.

---

## Traceability Model

Each requirement follows the traceability chain below:

**IND / Regulated Delivery Requirement**  
→ **Observed Gap** ([IND-GAP-XXX](./ind-requirements-gap-log.md))  
→ **Backlog Item** ([P0 / P1 / P2-BL-XXX](../backlog/ind-aligned-backlog.md))  
→ **RGDS Artifact(s)**

---

## Requirements Traceability Table

| Requirement ID | Requirement Description | Gap ID(s) | Backlog Item ID(s) | RGDS Artifact(s) | Status | Notes |
|----------------|--------------------------|-----------|--------------------|------------------|--------|-------|
| **IND-PREIND-008** | Pre-IND interactions, pauses, and regulatory questions must be traceable and reviewable | IND-GAP-001 | P0-BL-001 | examples/rgds-dec-0003-defer-required-evidence.json<br>docs/decision-log.md<br>docs/governance.md | Implemented | Prevents undocumented regulatory pauses |
| **IND-TPP-009** | Decisions must be traceable to Target Product Profile (TPP) intent | IND-GAP-002 | P0-BL-002 | decision-log.schema.json<br>docs/decision-log.md | Implemented | Prevents silent drift from development intent |
| **IND-PHASE-004** | Conditional decisions must explicitly document unmet evidence and follow-up actions | IND-GAP-003, IND-GAP-005 | P0-BL-003, P1-BL-004 | decision-log.schema.json<br>examples/<br>scripts/validate_all_examples.py | Implemented | Separates approval vs defer semantics |
| **IND-FLEX-007** | Deferred decisions must retain ownership and accountability | IND-GAP-004 | P0-BL-003 | scripts/validate_all_examples.py<br>.github/workflows/validate.yml | Implemented | Prevents accountability decay over time |
| **IND-ALIGN-010** | Identifiers must remain consistent across evidence and decisions | IND-GAP-006 | P1-BL-005 | docs/decision-log.md<br>docs/ai-checks/* | Implemented | Reduces manual reconciliation during review |
| **IND-BENCH-011** | Submission timelines and benchmarks must be explicit at decision time | IND-GAP-007 | P2-BL-006 | decision-log.schema.json<br>docs/decision-log.md | Implemented | Enables timing-aware decisions |
| **IND-DEC-OPT-012** | Decisions must explicitly enumerate options considered and select one | — | P0-BL-007 | decision-log.schema.json<br>decision-log.template.yaml<br>docs/decision-log.md | Implemented | Prevents implicit default decisions |
| **IND-RISK-013** | Residual risk must be explicitly documented when proceeding | — | P0-BL-008 | decision-log.schema.json<br>docs/decision-log.md | Implemented | Makes accepted risk auditable |
| **IND-EVID-014** | Evidence must declare completeness per item (complete / partial / placeholder) | — | P0-BL-009 | decision-log.schema.json<br>examples/<br>evaluation/evidence-quality-rubric.md | Implemented | Prevents false confidence from placeholders |
| **IND-AI-015** | AI assistance must be transparently disclosed when it materially influences a decision | — | P0-BL-010 | docs/ai-assistance-policy.md<br>decision-log.schema.json<br>examples/rgds-dec-0006-ai-assisted-conditional-go.json | Implemented | Preserves trust without granting AI authority |
| **IND-AUTH-016** | Decisions must record named human ownership and approval | — | P0-BL-011 | decision-log.schema.json<br>docs/governance.md | Implemented | Eliminates anonymous accountability |
| **IND-AUTH-017** | Decision authority scope and escalation paths must be auditable when ambiguous | — | P1-BL-012 | decision-log.schema.json<br>docs/governance.md | Implemented | Prevents deadlock and post-hoc blame |
| **IND-PROP-018** | Decisions with cross-artifact impact must declare downstream propagation requirements | — | P1-BL-013 | decision-log.schema.json<br>docs/decision-log.md | Implemented | Prevents silent ripple effects |
| **IND-AUD-019** | Decision history and supersession must be reconstructible over time | — | P1-BL-014 | decision-log.schema.json<br>docs/change-control-log.md | Implemented | Enables long-horizon audit reconstruction |

---

## Artifact References

- **IND Requirements Gap Log**  
  evaluation/ind-requirements-gap-log.md

- **IND-Aligned Backlog**  
  backlog/ind-aligned-backlog.md

- **Decision Log Schema**  
  decision-log/decision-log.schema.json

- **Decision Log Interpretation**  
  docs/decision-log.md

- **Governance Model**  
  docs/governance.md

- **AI Assistance Policy**  
  docs/ai-assistance-policy.md

- **Evaluation Plan**  
  evaluation/evaluation-plan.md

---

## Notes on Usage

- A single requirement may map to multiple gaps or backlog items.
- Backlog IDs are the authoritative execution linkage.
- Status reflects **reference-implementation completeness**, not production adoption.
- This RTM is expected to evolve as RGDS governance matures.

**If a reviewer asks _“Why does this field exist?”_  
the answer should be traceable here.**

