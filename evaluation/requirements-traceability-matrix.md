# Requirements Traceability Matrix (RTM)

This matrix maps fourteen author-declared requirements to RGDS artifacts. The requirement IDs are internal identifiers. They do not identify a complete set of FDA requirements or establish regulatory compliance.

“Implemented” means that a reference artifact exists for the declared requirement. Some rows describe machine checks; others describe optional fields or human review duties. The notes below identify those limits. No percentage in this matrix measures field effectiveness or regulatory coverage.

---

## Traceability Model

Each requirement follows the traceability chain below:

**IND / Regulated Delivery Requirement**  
→ **Observed Gap** ([IND-GAP-XXX](./ind-requirements-gap-log.md))  
→ **Backlog Item** ([P0 / P1 / P2-BL-XXX](../backlog/ind-aligned-backlog.md))  
→ **RGDS Artifact(s)**

---

## Requirements Traceability Table

| Requirement ID | Requirement Description | Gap ID(s) | Backlog Item ID(s) | RGDS Artifact(s) | Status | Implementation boundary |
|----------------|--------------------------|-----------|--------------------|------------------|--------|-------|
| **IND-PREIND-008** | Pre-IND interactions, pauses, and regulatory questions must be traceable and reviewable | [IND-GAP-001](./ind-requirements-gap-log.md#ind-gap-001) | [P0-BL-001](../backlog/ind-aligned-backlog.md#p0-bl-001--add-ind--regulatory-interaction-decision-pattern--example) | [rgds-dec-0003-defer-required-evidence.json](../examples/rgds-dec-0003-defer-required-evidence.json)<br>[decision-log.md](../docs/decision-log.md)<br>[governance.md](../docs/governance.md) | Implemented | Records a pause and evidence obligations; does not verify agency acceptance |
| **IND-TPP-009** | Decisions must be traceable to Target Product Profile (TPP) intent | [IND-GAP-002](./ind-requirements-gap-log.md#ind-gap-002) | [P0-BL-002](../backlog/ind-aligned-backlog.md#p0-bl-002--link-decisions-to-target-product-profile-tpp-claims) | [decision-log.schema.json](../decision-log/decision-log.schema.json)<br>[decision-log.md](../docs/decision-log.md) | Implemented | TPP fields are optional; alignment requires human review |
| **IND-PHASE-004** | Conditional decisions must explicitly document unmet evidence and follow-up actions | [IND-GAP-003](./ind-requirements-gap-log.md#ind-gap-003), [IND-GAP-005](./ind-requirements-gap-log.md#ind-gap-005) | [P0-BL-003](../backlog/ind-aligned-backlog.md#p0-bl-003--add-semantic-validator-enforcing-completeness-for-gated-decisions), [P1-BL-004](../backlog/ind-aligned-backlog.md#p1-bl-004--add-decision_outcome-enum-defer_with_required_evidence) | [decision-log.schema.json](../decision-log/decision-log.schema.json)<br>[examples/](../examples/)<br>[validate_all_examples.py](../scripts/validate_all_examples.py) | Implemented | Conditions and required-evidence deferral obligations have semantic checks |
| **IND-FLEX-007** | Deferred decisions must retain ownership and accountability | [IND-GAP-004](./ind-requirements-gap-log.md#ind-gap-004) | [P0-BL-003](../backlog/ind-aligned-backlog.md#p0-bl-003--add-semantic-validator-enforcing-completeness-for-gated-decisions) | [validate_all_examples.py](../scripts/validate_all_examples.py)<br>[validate.yml](../.github/workflows/validate.yml) | Implemented | Owner is required; continued accountability requires review |
| **IND-ALIGN-010** | Identifiers must remain consistent across evidence and decisions | [IND-GAP-006](./ind-requirements-gap-log.md#ind-gap-006) | [P1-BL-005](../backlog/ind-aligned-backlog.md#p1-bl-005--add-nomenclature--identifier-guidance--optional-consistency-checks) | [decision-log.md](../docs/decision-log.md)<br>[docs/ai-checks/](../docs/ai-checks/) | Implemented | Guidance and checklists; no cross-record identifier validator |
| **IND-BENCH-011** | Submission timelines and benchmarks must be explicit at decision time | [IND-GAP-007](./ind-requirements-gap-log.md#ind-gap-007) | [P2-BL-006](../backlog/ind-aligned-backlog.md#p2-bl-006--add-timeline-and-benchmark-capture-fields-in-program_context) | [decision-log.schema.json](../decision-log/decision-log.schema.json)<br>[decision-log.md](../docs/decision-log.md) | Implemented | Optional context fields; no benchmark adequacy test |
| **IND-DEC-OPT-012** | Decisions must explicitly enumerate options considered and select one | — | *(Whitepaper-aligned v2.0)* | [decision-log.schema.json](../decision-log/decision-log.schema.json)<br>[decision-log.template.yaml](../decision-log/decision-log.template.yaml)<br>[decision-log.md](../docs/decision-log.md) | Implemented | At least two options required; selected ID membership is not cross-checked |
| **IND-RISK-013** | Residual risk must be explicitly documented when proceeding | — | *(Whitepaper-aligned v2.0)* | [decision-log.schema.json](../decision-log/decision-log.schema.json)<br>[decision-log.md](../docs/decision-log.md) | Implemented | Statement field required but may be empty; substantive adequacy requires review |
| **IND-EVID-014** | Evidence must declare completeness per item (complete / partial / placeholder) | — | *(Whitepaper-aligned v2.0)* | [decision-log.schema.json](../decision-log/decision-log.schema.json)<br>[examples/](../examples/)<br>[evidence-quality-rubric.md](./evidence-quality-rubric.md) | Implemented | Each item requires a label; truth and package consistency are not verified |
| **IND-AI-015** | AI assistance must be transparently disclosed when it materially influences a decision | — | *(Whitepaper-aligned v2.0)* | [ai-assistance-policy.md](../docs/ai-assistance-policy.md)<br>[decision-log.schema.json](../decision-log/decision-log.schema.json)<br>[rgds-dec-0006-ai-assisted-conditional-go.json](../examples/rgds-dec-0006-ai-assisted-conditional-go.json) | Implemented | Disclosure structure and semantic checks; undisclosed actual use is not detectable |
| **IND-AUTH-016** | Decisions must record named human ownership and approval | — | *(Whitepaper-aligned v2.0)* | [decision-log.schema.json](../decision-log/decision-log.schema.json)<br>[governance.md](../docs/governance.md) | Implemented | Person objects required; identity and effective participation are not verified |
| **IND-AUTH-017** | Decision authority scope and escalation paths must be auditable | — | *(Whitepaper-aligned v2.0)* | [decision-log.schema.json](../decision-log/decision-log.schema.json)<br>[governance.md](../docs/governance.md) | Implemented | Authority and escalation fields are optional; deadlock resolution is not verified |
| **IND-PROP-018** | Decisions with cross-artifact impact must declare downstream propagation | — | *(Whitepaper-aligned v2.0)* | [decision-log.schema.json](../decision-log/decision-log.schema.json)<br>[decision-log.md](../docs/decision-log.md) | Implemented | Propagation field is optional; downstream execution is not verified |
| **IND-AUD-019** | Decision history and supersession must be reconstructible | — | *(Whitepaper-aligned v2.0)* | [decision-log.schema.json](../decision-log/decision-log.schema.json)<br>[change-control-log.md](../docs/change-control-log.md) | Implemented | Audit fields required; history integrity depends on repository and retention controls |

---

## Artifact Index (Authoritative)

- **IND Requirements Gap Log**  
  → [evaluation/ind-requirements-gap-log.md](./ind-requirements-gap-log.md)

- **IND-Aligned Backlog**  
  → [backlog/ind-aligned-backlog.md](../backlog/ind-aligned-backlog.md)

- **Decision Log Schema**  
  → [decision-log/decision-log.schema.json](../decision-log/decision-log.schema.json)

- **Decision Log Interpretation**  
  → [docs/decision-log.md](../docs/decision-log.md)

- **Governance Model**  
  → [docs/governance.md](../docs/governance.md)

- **AI Assistance Policy**  
  → [docs/ai-assistance-policy.md](../docs/ai-assistance-policy.md)

- **Evaluation Plan**  
  → [evaluation/evaluation-plan.md](./evaluation-plan.md)

---

## Notes on Usage

- A single requirement may map to multiple gaps or backlog items.
- Backlog IDs are the authoritative execution linkage.
- “Implemented” records an internal artifact mapping. Review the implementation boundary for each row before relying on it.
- This RTM must be updated if schema, validators, or canonical examples change.

**Reviewer test:**  
If someone asks *“Why does this field exist?”*  
the answer should be traceable here in ≤2 clicks.

