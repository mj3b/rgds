# RGDS — Regulated Gate Decision Support

[![Status: Independent Case Study](https://img.shields.io/badge/status-independent%20case%20study-5b6cff)](#status)
[![Human Governed](https://img.shields.io/badge/governance-human--governed-3bb273)](docs/governance.md)
[![Non-Agentic](https://img.shields.io/badge/AI-explicitly%20non--agentic-2d7ff9)](#ai-governance)
[![Schema Enforced](https://img.shields.io/badge/schema-decision%20log%20enforced-1f6feb)](#decision-log-schema)
[![CI Validation](https://img.shields.io/github/actions/workflow/status/mj3b/rgds/validate.yml)](https://github.com/mj3b/rgds/actions/workflows/validate.yml)
[![License](https://img.shields.io/github/license/mj3b/rgds)](LICENSE)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0001--8121--2878-brightgreen)](https://orcid.org/0009-0001-8121-2878)

RGDS addresses the loss of decision context when alternatives, evidence gaps, and approval conditions remain scattered across documents and meeting records. This reference implementation records those elements in a structured decision log for phase-gated regulated programs.

The research question is whether that record makes a decision easier to reconstruct later. Repository validation checks structure and selected internal consistency rules. Retrieval speed, field effectiveness, and regulatory outcomes remain unestablished.

---

## The Problem RGDS Addresses

RGDS links the decision question to the options considered, evidence available, residual risk, named authority, and follow-up obligations. It provides a record format for examining implicit judgment and undocumented trade-offs. This design does not establish how often those gaps cause regulatory deficiencies.

```
Traditional documentation model:          RGDS model:

Documents → Analysis → Meeting            Decision Question
        ↓                                       ↓
Implicit decision                         Options Considered (≥2)
        ↓                                       ↓
Memory + email threads                    Evidence Base + Completeness
        ↓                                       ↓
Reconstruction attempt                    Risk Posture + Residual Risk
                                                ↓
                                          Named Human Accountability
                                                ↓
                                          Schema Validation → Git
                                                ↓
                                          Record available for review
```

The decision log is the record. Everything else — analyses, documents, source reports — serves the decision.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    RGDS OPERATING MODEL                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Phase Gate Event                                               │
│       │                                                         │
│       ▼                                                         │
│  ┌─────────────────────────────────────┐                        │
│  │         Decision Log Record         │  ← Primary Artifact    │
│  │                                     │                        │
│  │  decision_question                  │                        │
│  │  options_considered  (≥2 required)  │                        │
│  │  evidence            (completeness) │                        │
│  │  risk_posture        (explicit)     │                        │
│  │  risk_assessment                    │                        │
│  │  decision_outcome    (5 types)      │                        │
│  │  governance          (named people) │                        │
│  │  ai_assistance       (required)     │                        │
│  └─────────────────┬───────────────────┘                        │
│                    │                                            │
│                    ▼                                            │
│  ┌─────────────────────────────────────┐                        │
│  │      Schema Validation (CI/CD)      │  ← Enforcement         │
│  │  decision-log.schema.json           │                        │
│  │  Semantic invariant checks          │                        │
│  │  Required fields enforced           │                        │
│  └─────────────────┬───────────────────┘                        │
│                    │                                            │
│                    ▼                                            │
│  ┌─────────────────────────────────────┐                        │
│  │      Git (Version-Controlled Log)   │  ← Audit Trail         │
│  │  Version-controlled record history  │                        │
│  │  Records linked to source evidence  │                        │
│  │  Context available for review       │                        │
│  └─────────────────────────────────────┘                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## The Five Decision Outcomes

The schema permits exactly five values for `decision_outcome.outcome`:

| Outcome | Meaning and validation behavior |
|---------|---------------------------------|
| `go` | Proceed. The schema and common checks apply. Validation does not establish full confidence or evidence sufficiency. |
| `conditional_go` | Proceed subject to conditions. Semantic validation requires at least one condition and recommends actions to carry it out. Each condition records an owner, due date, and evidence needed for closure. |
| `defer` | Pause the decision. Semantic validation warns when both gaps and actions are absent. |
| `no_go` | Decline to proceed. The schema requires a rationale summary for this outcome, as it does for all outcomes. |
| `defer_with_required_evidence` | Pause pending required evidence. Semantic validation requires gaps, conditions, and actions. |

Escalation is a governance action for routing disagreement or insufficient authority. The optional `governance.escalation_path` records the people responsible for resolving it. `escalate` is not a schema outcome.

---

## Decision Log Schema

The JSON Schema checks the record structure. The validators add selected semantic checks. Passing validation does not establish decision correctness, approval, human judgment, or regulatory compliance.

```
decision-log/
├── decision-log.schema.json    ← Machine-enforced
├── decision-log.schema.yaml    ← Human-readable companion
└── decision-log.template.yaml  ← Starting point for new decisions
```

### Required Fields and Supported Extensions

The [JSON Schema](decision-log/decision-log.schema.json) defines the complete contract. The table lists selected fields using their actual paths.

| Field | Type and requirement | Recorded information |
|-------|----------------------|----------------------|
| `decision_question` | Required string | The choice under review |
| `gate.decision_deadline` | Required date-time string | Decision deadline |
| `options_considered` | Required array, at least two items | Alternatives, pros, cons, and estimated impact |
| `evidence.evidence_items` | Required array | Evidence references and source information |
| `evidence.evidence_items[].completeness_state` | Required enum on each item | `complete` / `partial` / `placeholder` |
| `evidence_completeness.state` | Required enum | Completeness of the evidence package |
| `risk_posture` | Required enum | `risk_minimizing` / `risk_neutral` / `risk_accepting` |
| `risk_assessment.residual_risk_statement` | Required string; may be empty | Residual risk statement |
| `risk_assessment.residual_risk_items` | Optional array | Structured risk, mitigation, and trigger entries |
| `decision_outcome.outcome` | Required enum | One of the five contract outcomes |
| `governance.decision_owner` | Required person object | Name and role of the owner |
| `governance.approvers` | Required array, at least one person | Names and roles of approvers |
| `ai_assistance` | Required object, including when AI is unused | `used`, `use_cases`, `artifacts`, and `controls` |

The person fields record claims about ownership and approval. Validation checks their structure; it cannot verify identity or substantive participation.

### Evidence Completeness Model

Each evidence item records `complete`, `partial`, or `placeholder` in `evidence.evidence_items[].completeness_state`. These are author-assigned classifications. The schema checks the labels without verifying source quality.

At package level, semantic checks warn when `evidence_completeness.state` is `partial` or `placeholder` and the record contains neither gaps nor author-at-risk items. A placeholder package also receives a warning when it lacks an expected resolution date. These warnings become failures in strict mode.

---

## Canonical Decision Records

Six examples cover `conditional_go`, `no_go`, and `defer_with_required_evidence`. There are no canonical `go` or plain `defer` examples in the current set.

| Record | Outcome | Scenario | What It Demonstrates |
|--------|---------|----------|----------------------|
| [`rgds-dec-0001`](examples/rgds-dec-0001.json) | **conditional_go** | Data readiness gate | Explicit conditions, owned follow-ups, named approvers |
| [`rgds-dec-0002`](examples/rgds-dec-0002-no-go.json) | **no_go** | Risk threshold exceeded | Defensible refusal with re-entry logic |
| [`rgds-dec-0003`](examples/rgds-dec-0003-defer-required-evidence.json) | **defer_with_required_evidence** | Missing required evidence | Structured pause with re-review criteria |
| [`rgds-dec-0004`](examples/rgds-dec-0004-regulatory-interaction.json) | **conditional_go** | Pre-IND FDA interaction | Agency-facing decision framing and strategy |
| [`rgds-dec-0005`](examples/rgds-dec-0005-ind-conditional-go-author-at-risk.json) | **conditional_go** | IND authoring gate | Author-at-risk drafting, reviewer triage, lock points |
| [`rgds-dec-0006`](examples/rgds-dec-0006-ai-assisted-conditional-go.json) | **conditional_go** | AI-assisted decision | Bounded AI disclosure, preserved human authority |

All six records are checked by the batch validator on pushes to `main`, pull requests targeting `main`, and manual workflow runs.

---

## AI Governance

RGDS is valid with no AI at all. When AI is used, it operates as bounded assistance only.

```
┌──────────────────────────────────────────────────────────────┐
│                    AI GOVERNANCE BOUNDARY                    │
├─────────────────────────┬────────────────────────────────────┤
│    PERMITTED (bounded)  │         PROHIBITED                 │
├─────────────────────────┼────────────────────────────────────┤
│ Summarization           │ Gate outcome decisions             │
│ Field extraction        │ Evidence of record by default      │
│ Cross-document diffing  │ Silent scope or risk acceptance    │
│ Structured drafting     │ Publishing or submission actions   │
│ Schema completeness     │ Fabricated citations or rationale  │
│   checks                │ Autonomous execution of any kind   │
└─────────────────────────┴────────────────────────────────────┘
         │
         ▼ Additional schema fields when used=true:
┌──────────────────────────────────────────────────────────────┐
│  ai_assistance.used           → true                         │
│  ai_assistance.tool_name      → which system                 │
│  ai_assistance.tool_purpose   → what task                    │
│  ai_assistance.human_review[] → review tier + findings       │
│  ai_assistance.ai_risk_assessment → risk assessment object   │
└──────────────────────────────────────────────────────────────┘
         │
         ▼ Human decision owner remains fully responsible.
           AI disclosure transfers no authority, approval
           rights, or risk ownership.
```

Both validators use the same semantic checks. When AI is used, they require nonempty tool name, tool purpose, human review, use cases, and artifacts. They recommend an AI risk confidence band. Both validate the schema's date and date-time formats. `human_override_log` is optional. The `ai_assistance` object remains required when `used=false`.

**Evidence rule:** AI output is never treated as primary evidence. If an AI output influences a decision, the human owner must link to the underlying source and record the AI output as a drafting aid. Every decision must remain defensible without the AI output present.

The local [AI assistance policy](docs/ai-assistance-policy.md) states the requirements for this implementation. The related [AI Assistance Governance material](https://github.com/mj3b/rgds-ai-governance) remains a working method under separate review. Its claims do not establish properties of this implementation.

---

## IND Context and Record Mechanisms

These design scenarios connect IND preparation concerns to record fields. They are intended uses, not measured reductions in regulatory or operational failures.

| Design scenario | Concern to examine | RGDS mechanism |
|-------------------|----------------------|----------------|
| Placeholders proceed without governance | False confidence, FDA gap finding | `evidence.evidence_items[].completeness_state` + author-at-risk constraints |
| Scope changes emerge late without a trail | Silent ripple effects across modules | `scope_change_events[]` + downstream propagation |
| Reviewer routing is informal | Unclear accountability under audit | `review_plan` + named triage owner |
| Risk posture is implied, not stated | Cannot defend tolerance decisions to FDA | `risk_posture` + `residual_risk_items` |
| Cross-module dependencies are mentally tracked | Late-discovered misalignment after gate closes | `dependency_map[]` |
| Phase-gate tolerance is assumed shared | Silent misalignment between functions | Explicit risk posture field, cross-functional sign-off |
| Regulatory interaction strategy is informal | Weak pre-IND positioning | `decision_category: regulatory_interaction` |
| AI assistance is undisclosed | Provenance contamination, audit exposure | `ai_assistance` disclosure object (always required; additional fields when used) |

---

## Repository Structure

```
rgds/
│
├── decision-log/                    ← Schema and templates
│   ├── decision-log.schema.json     ← Machine-enforced schema
│   ├── decision-log.schema.yaml     ← Human-readable version
│   └── decision-log.template.yaml   ← Starting template
│
├── examples/                        ← Start here
│   ├── README.md                    ← How to read examples
│   ├── rgds-dec-0001.json           ← Conditional go (canonical)
│   ├── rgds-dec-0002-no-go.json     ← No-go (canonical)
│   ├── rgds-dec-0003-defer-*.json   ← Defer with required evidence
│   ├── rgds-dec-0004-regulatory-*.json ← Regulatory conditional go
│   ├── rgds-dec-0005-ind-*.json     ← IND conditional go
│   └── rgds-dec-0006-ai-*.json      ← AI-assisted (only AI example)
│
├── evaluation/                      ← Decision quality assessment
│   ├── evaluation-plan.md           ← Assessment methodology
│   ├── evidence-quality-rubric.md   ← Evidence scoring criteria
│   ├── requirements-traceability-matrix.md ← Internal requirement mapping
│   └── scorecard-template.csv       ← Structured review scorecard
│
├── docs/                            ← Governance documentation
│   ├── why-rgds-exists.md           ← Evidence-to-design rationale
│   ├── decision-log.md              ← How to read decision logs
│   ├── governance.md                ← Rules and enforcement intent
│   ├── ai-assistance-policy.md      ← AI governance policy
│   ├── role-decision-artifact-matrix.md ← Cross-role ownership
│   └── change-control-log.md        ← Schema change history
│
├── scripts/                         ← Validation tooling
│   ├── validate_decision_log.py     ← Single-record validator
│   └── validate_all_examples.py     ← Batch validator (CI)
│
├── .github/workflows/
│   └── validate.yml                 ← CI/CD schema + semantic validation
│
├── Makefile                         ← Local validation commands
└── requirements.txt
```

---

## Reader Navigation Guide

Different readers have different entry points.

```
Are you a...
│
├── Executive / Approver
│   └── README.md → rgds-dec-0001 or rgds-dec-0005
│       Goal: understand what a governed decision looks like
│
├── Quality / Governance Reviewer
│   └── docs/governance.md → docs/decision-log.md → evaluation/
│       Goal: understand review criteria and audit artifacts
│
├── AI Governance Reviewer
│   └── docs/ai-assistance-policy.md → rgds-dec-0006
│       → github.com/mj3b/rgds-ai-governance
│       Goal: understand AI boundaries and disclosure requirements
│
├── Regulatory / FDA Auditor
│   └── examples/ + evaluation/requirements-traceability-matrix.md
│       Goal: reconstruct decision context from governed records
│
└── Technical Implementer
    └── decision-log/decision-log.schema.json → scripts/
        → .github/workflows/validate.yml
        Goal: understand schema enforcement and CI integration
```

---

## Release History

The current patch release is [v2.0.1](https://github.com/mj3b/rgds/releases/tag/v2.0.1). See the [release notes](docs/releases/v2.0.1.md) for cumulative changes and validation boundaries.

The historical release uses the exact tag [`v.2.0.0`](https://github.com/mj3b/rgds/releases/tag/v.2.0.0). It remains unchanged. The [change control log](docs/change-control-log.md) preserves the dated P0 and P1 correction entries and records their inclusion in v2.0.1. No normalized alias or replacement tag has been created.

These corrections preserve the decision-record schema. Batch validation now applies the single-record validator's existing AI checks, and the single-record validator checks date formats. Records previously accepted because of those validation gaps may now fail. Cite a commit when referring to the corrected current implementation.

---

## Evaluation

The evaluation plan proposes four review dimensions. It does not report a completed field evaluation.

| Dimension | What is evaluated | Instrument |
|-----------|------------------|------------|
| Decision readiness | Evidence completeness, option coverage, risk explicitness | Evidence quality rubric |
| Governance execution | Accountability chain, approval separation, escalation logic | Reviewer audit checklist |
| AI assistance safety | Disclosure completeness, human override documentation | AI governance policy + dec-0006 |
| Requirements coverage | End-to-end traceability from program objectives to decisions | Internal requirements traceability matrix |

Evaluation focuses on decision quality and governance execution. It does not benchmark model performance in isolation.

---

## Relationship to GDI

RGDS is a biopharma reference implementation within the proposed NN-DE research program, Decision Evidence & Governed Action. GDI provides the general decision-record architecture; RGDS applies related concepts to regulated phase gates. This relationship does not establish formal GDI conformance.

| Artifact | Role and evidence boundary |
|----------|----------------------------|
| [RGDS](https://github.com/mj3b/rgds) | Schema, validators, and illustrative biopharma decision records. Internal checks establish limited structural and semantic properties. |
| [GDI](https://github.com/mj3b/governed-decision-intelligence) | General decision-record specification and research architecture. |
| [AI Assistance Governance](https://github.com/mj3b/rgds-ai-governance) | Working method for bounded AI participation, under separate remediation. |
| [RGDS Independent Study](https://github.com/mj3b/rgds-independent-study) | Historical exploratory study and modeling work. Its projections do not establish deployment outcomes for this implementation. |

## Status

| Dimension | Current state |
|-----------|---------------|
| Project type | Reference implementation |
| Development state | Working reference implementation; current release `v2.0.1` |
| Evidence state | Internal schema, semantic, and regression checks; six illustrative canonical records |
| Outcome coverage | Three canonical outcomes; derived regression cases also exercise `go` and `defer` |
| Internal requirements | Fourteen declared RTM rows map to implementation artifacts; each row distinguishes machine checks from policy or review expectations |
| External evaluation | Field effectiveness and independent evaluation remain unestablished |
| Regulatory status | No claim of regulatory approval, legal compliance, or demonstrated benefit |
| Node & Norm admission | Candidate for review as a working reference implementation; no transfer or organization change has occurred |

## Citation

Use [CITATION.cff](CITATION.cff) for this implementation and include the Git commit used in reproducible work. No implementation DOI has been verified for this repository.

The [Zenodo record 20242004](https://zenodo.org/records/20242004) archives `rgds-independent-study` v1.4, published on May 16, 2026. Its version DOI is `10.5281/zenodo.20242004`; its all-versions DOI is `10.5281/zenodo.20242003`. Cite that record when using the historical study. It does not identify this repository's v2 implementation.

The [citation and provenance note](docs/citation-provenance.md) records the correction and retains the previous citation verbatim. Authorship remains with [Mark Julius Banasihan](https://orcid.org/0009-0001-8121-2878).

---

## Author

**Mark Julius Banasihan**
Decision governance systems for regulated, high-stakes environments.

[GitHub](https://github.com/mj3b) · [LinkedIn](https://linkedin.com/in/markjuliusbanasihan) · [ORCID](https://orcid.org/0009-0001-8121-2878) · Atlanta, Georgia, United States
