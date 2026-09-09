# Change Control Log

This log records controlled changes to RGDS schemas, validators, documentation, and canonical examples.

Its purpose is to:
- preserve auditability over time
- explain why changes were made
- make evolution explicit and reviewable

This is **not** a marketing changelog.  
It is a governance record.

---


## v2.0.1 (2026-09-09)

Publishes the P0 and P1 corrections recorded below, together with the intervening documentation, evaluation, checklist, and NOTICE changes since `v.2.0.0`. The earlier entries retain their wording as records of their status when prepared.

Release preparation adds versioned citation metadata and release references, and restores the complete Apache 2.0 terms from the historical release while retaining the current copyright notice. See the [release notes](releases/v2.0.1.md) for cumulative scope and compatibility limits.

The decision schemas, template, and six canonical JSON records remain unchanged from `v.2.0.0`. Historical tags and releases are preserved. Repository validation is recorded separately for the release commit; publication does not itself establish Node & Norm admission.

---

## Unreleased: RGDS P1 citation, claim, and validation corrections (2026-09-09)

The owner authorized this pass after the P0 merge in PR #8. The public ORCID and Zenodo records were inspected to resolve the citation mismatch.

| Area | Correction and boundary |
|------|-------------------------|
| Citation | Added `CITATION.cff` for this implementation. The DOI `10.5281/zenodo.20242004` identifies the independent study v1.4; retained it as a related reference and preserved the previous citation in `citation-provenance.md`. |
| Claims and relationships | Replaced headline RTM coverage with explicit limits for fourteen internal requirements. Clarified the roles of GDI, RGDS, the working AI method, and the historical study. Distinguished policy expectations from machine checks and field evidence. |
| Validation | Batch validation now imports the existing single-record semantic checks. Single-record validation now checks schema date formats. Warning severity remains unchanged. The script version advances to 1.0.1; the decision schema is unchanged. |
| Regression checks | Added nine tests covering canonical records, AI disclosure failures, warning severity, invalid dates, and all five outcome values through derived cases. CI runs the tests after validating examples. |
| Links | Corrected the README governance destination and added stable gap-table anchors for RTM links. |

The six canonical JSON records, schema files, template, license, NOTICE, historical change-log entries, tags, and releases remain unchanged. New validation behavior may reject records that previously passed through a validator gap. Corrections remain unreleased; a future release must receive a new version without renaming `v.2.0.0`.

Codex assisted with source inspection, edits, and testing under the owner's authorization and E5 writing rules. Repository checks do not constitute independent research review or Node & Norm admission. ORCID, Zenodo, sibling repositories, and organization settings were not edited.

---

## Unreleased: RGDS P0 documentation corrections (2026-09-09)

Applied the RGDS P0 scope of the Node & Norm Repository Remediation Audit v0.1 to the current documentation.

| Files | Correction | Basis |
|-------|------------|-------|
| `README.md`, `examples/README.md` | Preserve the five schema outcomes; distinguish escalation as a governance action; identify DEC-0003 as `defer_with_required_evidence` and DEC-0004 as `conditional_go`; report three-outcome example coverage | Existing JSON Schema, validators, and six JSON examples |
| `README.md` | Remove the unsupported FDA failure-rate, causal, reconstruction-time, and retrieval-time claims; state the design question and evidence limits | P0 claim corrections identified by the audit |
| `README.md`, `examples/README.md` | Use actual field paths and types; distinguish required fields, optional extensions, semantic checks, and CI scope | Existing contract and validation code |
| `README.md` | Identify the exact historical tag and describe version-controlled record history | Existing Git tag `v.2.0.0` |

The schema, validators, templates, and canonical JSON records are unchanged. Existing release entries below retain their historical wording. This correction creates no new release and changes no historical tags, release assets, authorship, or citation identifiers. Validation of the corrected working tree is reported separately for review.

AI assistance: Codex prepared these documentation corrections and the accompanying validation report at the repository owner's request. Human review of this change remains pending.

---

## v2.0.0 — Whitepaper-aligned decision discipline (breaking)

**Summary**  
Formalized the RGDS minimum decision record requirements described in the RGDS whitepaper.
This release converts previously optional or implicit practices into **mandatory, schema-enforced governance controls**.

v2.0.0 is a **breaking governance update**: decision records that passed validation under v1.x may fail under v2.0.0 if required fields are missing.

### Controlled changes

| Date | Change | Rationale | Impacted Files | Approved By |
|---|---|---|---|---|
| 2026-01-04 | Required explicit options enumeration (`options_considered[]`, ≥2) | Prevent false binary framing and undocumented “default” decisions | [`decision-log.schema.json`](../decision-log/decision-log.schema.json), [`decision-log.schema.yaml`](../decision-log/decision-log.schema.yaml) | N/A (reference implementation) |
| 2026-01-04 | Enforced evidence completeness per evidence item (`completeness_state`) | Eliminate false confidence from placeholders and in-flight data | [`decision-log.schema.json`](../decision-log/decision-log.schema.json) | N/A |
| 2026-01-04 | Added explicit residual risk capture | Make accepted risk visible *after* decision execution | [`decision-log.schema.json`](../decision-log/decision-log.schema.json) | N/A |
| 2026-01-04 | Required named human accountability (owner + approvers) | Preserve decision authority and auditability under compressed timelines | [`decision-log.schema.json`](../decision-log/decision-log.schema.json), [`docs/governance.md`](governance.md) | N/A |
| 2026-01-04 | Replaced optional AI transparency with structured AI disclosure when used | Make AI assistance reviewable without granting authority | [`decision-log.schema.json`](../decision-log/decision-log.schema.json), [`docs/ai-assistance-policy.md`](ai-assistance-policy.md) | N/A |
| 2026-01-04 | Strengthened semantic validation for options count and AI disclosure integrity | Prevent formally valid but governance-incomplete decisions | [`validate_decision_log.py`](../scripts/validate_decision_log.py) | N/A |
| 2026-01-04 | Updated all canonical examples to meet v2.0.0 minimum requirements | Ensure examples remain authoritative and reviewable | [`examples/`](../examples/) | N/A |
| 2026-01-04 | Updated decision log template to reflect new minimum fields | Prevent drift between schema and authoring practice | [`decision-log.template.yaml`](../decision-log/decision-log.template.yaml) | N/A |

**Effective date**  
2026-01-04

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
