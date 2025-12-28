# IND Requirements Gap Log

This log documents observed gaps between IND regulatory expectations and common delivery practices, as identified through IND-focused webinars and practitioner discussion.
Each gap is traceably linked to one or more RGDS backlog items.

This artifact exists to provide evidence-backed justification for RGDS backlog work and to preserve traceability from external requirements to internal execution decisions.

---

## Gap Table

| Gap ID | Source | Source Reference | Requirement ID | Observed Gap | Gap Type | RGDS Impact | Linked Backlog Item | Evidence Reference | Notes |
|------|--------|------------------|----------------|--------------|----------|-------------|---------------------|-------------------|-------|
| IND-GAP-001 | IND Webinar | Pre-IND interaction discussion | IND-PREIND-008 | Programs lack a structured way to log pre-IND pauses, regulator questions, and interim outcomes | Decision traceability | Unlogged regulatory interactions create downstream audit and rationale gaps | [P0-BL-001](../backlog/ind-aligned-backlog.md#p0-bl-001--add-ind--regulatory-interaction-decision-pattern--example) | IND Webinar transcript | Observed across multiple programs |
| IND-GAP-002 | IND Webinar | TPP alignment discussion | IND-TPP-009 | Decision rationales are not explicitly linked to Target Product Profile claims | Traceability | Rationale cannot be traced to label-oriented program goals | [P0-BL-002](../backlog/ind-aligned-backlog.md#p0-bl-002--link-decisions-to-target-product-profile-tpp-claims) | IND Webinar transcript | Leads to late-stage misalignment |
| IND-GAP-003 | IND Webinar | Conditional approvals discussion | IND-PHASE-004 | Conditional approvals lack explicit documentation of unmet evidence and follow-up actions | Decision completeness | Conditions are accepted implicitly without enforceable re-entry criteria | [P0-BL-003](../backlog/ind-aligned-backlog.md#p0-bl-003--add-semantic-validator-enforcing-completeness-for-gated-decisions) | IND Webinar transcript | Common source of rework |
| IND-GAP-004 | IND Webinar | Phase flexibility discussion | IND-FLEX-007 | Teams defer decisions without clearly documenting required evidence and ownership | Governance | Deferred decisions lose accountability over time | [P0-BL-003](../backlog/ind-aligned-backlog.md#p0-bl-003--add-semantic-validator-enforcing-completeness-for-gated-decisions) | IND Webinar transcript | Accountability diffusion observed |
| IND-GAP-005 | IND Webinar | Decision outcome taxonomy discussion | IND-PHASE-004 | Decision outcomes are overloaded and do not distinguish deferral with required evidence | Decision semantics | Ambiguous outcomes reduce reviewer clarity | [P1-BL-004](../backlog/ind-aligned-backlog.md#p1-bl-004--add-decision_outcome-enum-defer_with_required_evidence) | IND Webinar transcript | Creates inconsistent interpretations |
| IND-GAP-006 | IND Webinar | Naming and identifiers discussion | IND-ALIGN-010 | Inconsistent compound and study identifiers across documents and evidence | Consistency | Evidence linkage breaks during review | [P1-BL-005](../backlog/ind-aligned-backlog.md#p1-bl-005--add-nomenclature--identifier-guidance--optional-consistency-checks) | IND Webinar transcript | Manual reconciliation required |
| IND-GAP-007 | IND Webinar | Timeline planning discussion | IND-BENCH-011 | Key submission timelines and benchmarks are not captured at decision time | Planning context | Decisions cannot be evaluated against downstream timing constraints | [P2-BL-006](../backlog/ind-aligned-backlog.md#p2-bl-006--add-timeline-and-benchmark-capture-fields-in-program_context) | IND Webinar transcript | Timing assumptions lost over phases |

---

## Traceability Rule

Each gap must reference one or more backlog items by backlog ID.
Backlog IDs are the authoritative execution linkage for RGDS planning artifacts.
