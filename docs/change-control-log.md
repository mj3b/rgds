# Change Control Log

This log records controlled changes to RGDS schemas, validators, documentation, and canonical examples.

Its purpose is to:
- preserve auditability over time
- explain why changes were made
- make evolution explicit and reviewable

This is **not** a marketing changelog.  
It is a governance record.

---

## v1.4.0 — Decision authority & trust transparency

**Summary**  
Introduced explicit authority and escalation modeling, strengthened evidence completeness signaling, and added non-authoritative AI transparency fields. This version formalizes decision accountability under compressed timelines.

| Date | Change | Rationale | Impacted Files | Approved By |
|---|---|---|---|---|
| 2025-12-30 | Added canonical AI-assisted conditional_go example | Demonstrate bounded AI assistance with explicit disclosure and preserved human authority | [`rgds-dec-0006-ai-assisted-conditional-go.json`](../examples/rgds-dec-0006-ai-assisted-conditional-go.json) | N/A |
| 2025-12-27 | Added evidence completeness, propagation declaration, and risk benchmarking basis | Make downstream impact and evidence sufficiency explicit at decision time | [`decision-log.schema.json`](../decision-log/decision-log.schema.json) | N/A (reference implementation) |
| 2025-12-27 | Added authority scope and escalation path fields | Make decision rights and deadlock resolution auditable | [`decision-log.schema.json`](../decision-log/decision-log.schema.json), [`governance.md`](governance.md) | N/A |
| 2025-12-27 | Added optional AI transparency signals | Support post-hoc review without granting AI authority | [`decision-log.schema.json`](../decision-log/decision-log.schema.json), [`ai-assistance-policy.md`](ai-assistance-policy.md) | N/A |
| 2025-12-27 | Extended data readiness statuses | Explicitly model placeholders and in-flight data | [`decision-log.schema.json`](../decision-log/decision-log.schema.json) | N/A |

---

## v1.3.0 — IND-aligned delivery realism

**Summary**  
Expanded RGDS to model real IND execution constraints such as author-at-risk drafting, reviewer triage, dependency pressure, and rolling publishing.

| Date | Change | Rationale | Impacted Files | Approved By |
|---|---|---|---|---|
| 2025-12-27 | Introduced IND-aligned decision fields | Capture delivery realities that commonly cause late failure | [`decision-log.schema.json`](../decision-log/decision-log.schema.json), [`decision-log.md`](decision-log.md) | N/A |
| 2025-12-27 | Added author-at-risk modeling | Prevent silent placeholder risk | [`decision-log.schema.json`](../decision-log/decision-log.schema.json) | N/A |
| 2025-12-27 | Added review plan and triage rules | Make compressed review governance explicit | [`decision-log.schema.json`](../decision-log/decision-log.schema.json) | N/A |
| 2025-12-27 | Added dependency map and publishing plan | Surface interdependencies and lock points | [`decision-log.schema.json`](../decision-log/decision-log.schema.json) | N/A |

---

## v1.2.0 — Governance-first framing

**Summary**  
Established RGDS as a human-governed decision system rather than a delivery tracker or AI framework.

| Date | Change | Rationale | Impacted Files | Approved By |
|---|---|---|---|---|
| 2025-12-26 | Clarified decision outcomes and lifecycle | Distinguish go, no-go, conditional, and defer decisions | [`decision-log.schema.json`](../decision-log/decision-log.schema.json), [`decision-log.md`](decision-log.md) | N/A |
| 2025-12-26 | Added explicit governance sections | Ensure ownership, approval, and auditability | [`governance.md`](governance.md) | N/A |

---

## v1.1.0 — Deferral and re-entry support

**Summary**  
Added explicit support for pausing decisions when evidence is insufficient but termination is not warranted.

| Date | Change | Rationale | Impacted Files | Approved By |
|---|---|---|---|---|
| 2025-12-25 | Added `defer_with_required_evidence` outcome | Support defensible pause-and-re-enter decisions | [`decision-log.schema.json`](../decision-log/decision-log.schema.json) | N/A |
| 2025-12-25 | Added canonical defer example | Provide concrete exemplar for reviewers | [`rgds-dec-0003-defer-required-evidence.json`](../examples/rgds-dec-0003-defer-required-evidence.json) | N/A |

---

## v1.0.0 — Initial reference implementation

**Summary**  
Established the core RGDS decision log schema and validation approach as a reference implementation.

| Date | Change | Rationale | Impacted Files | Approved By |
|---|---|---|---|---|
| 2025-12-24 | Initial decision log schema | Create a structured, auditable decision record | [`decision-log.schema.json`](../decision-log/decision-log.schema.json) | N/A |
| 2025-12-24 | Initial canonical examples | Demonstrate intended usage patterns | [`examples/`](../examples/) | N/A |
| 2025-12-24 | Initial validation scripts | Ensure examples conform to schema | [`validate_all_examples.py`](../scripts/validate_all_examples.py) | N/A |
