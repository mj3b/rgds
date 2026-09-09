# RGDS — Regulated Gate Decision Support

[![Status: Independent Case Study](https://img.shields.io/badge/status-independent%20case%20study-5b6cff)](#status)
[![Human Governed](https://img.shields.io/badge/governance-human--governed-3bb273)](#governance)
[![Non-Agentic](https://img.shields.io/badge/AI-explicitly%20non--agentic-2d7ff9)](#ai-governance)
[![Schema Enforced](https://img.shields.io/badge/schema-decision%20log%20enforced-1f6feb)](#decision-log-schema)
[![RTM Coverage](https://img.shields.io/badge/RTM-100%25%20coverage-2ea44f)](#evaluation)
[![CI Validation](https://img.shields.io/github/actions/workflow/status/mj3b/rgds/validate.yml)](https://github.com/mj3b/rgds/actions/workflows/validate.yml)
[![License](https://img.shields.io/github/license/mj3b/rgds)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20242004-blue)](https://doi.org/10.5281/zenodo.20242004)
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
| `gate.decision_deadline` | Required date string | Decision deadline |
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

The single-record validator requires nonempty tool name, tool purpose, and human review when AI is used. It recommends an AI risk confidence band. Both validators require nonempty use cases and artifacts; the batch validator used by CI does not repeat the single-record validator's additional AI checks. `human_override_log` is optional. The `ai_assistance` object remains required when `used=false`.

**Evidence rule:** AI output is never treated as primary evidence. If an AI output influences a decision, the human owner must link to the underlying source and record the AI output as a drafting aid. Every decision must remain defensible without the AI output present.

Authoritative AI governance covenants: **[rgds-ai-governance](https://github.com/mj3b/rgds-ai-governance)**

---

## IND Alignment — Execution Realities → RGDS Mechanisms

RGDS formalizes failure modes observed during IND preparation. Each mechanism addresses a specific, named execution pattern.

| Execution Reality | Failure Mode Prevented | RGDS Mechanism |
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
│   ├── requirements-traceability-matrix.md ← 100% RTM coverage
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

## v2.0.0 — What Changed

The historical release uses the exact tag [`v.2.0.0`](https://github.com/mj3b/rgds/releases/tag/v.2.0.0). The documentation corrections recorded in the [change control log](docs/change-control-log.md) are unreleased. The historical tag, release, and citation identifiers are preserved.

v2.0.0 tightens decision defensibility. It does not add automation or autonomy.

| Change | What it enforces | Failure mode prevented |
|--------|-----------------|----------------------|
| Options enumeration (≥2 required) | At least two options must be considered | Single-option rationalization passing as governance |
| Evidence completeness per item | `complete` / `partial` / `placeholder` on every evidence item | False confidence from undocumented placeholders |
| Residual risk capture | Required `risk_assessment.residual_risk_statement`; optional `residual_risk_items[]` | Provides fields for recording residual risk; content adequacy requires review |
| Named human accountability | Decision owner + approvers as individuals, not roles | "Who approved this?" questions with no traceable answer |
| AI assistance disclosure | Required schema fields when `ai_assistance.used=true` | AI-assisted drafting without disclosure contaminating provenance |

---

## Evaluation

Decision quality is assessed across four dimensions.

| Dimension | What is evaluated | Instrument |
|-----------|------------------|------------|
| Decision readiness | Evidence completeness, option coverage, risk explicitness | Evidence quality rubric |
| Governance execution | Accountability chain, approval separation, escalation logic | Reviewer audit checklist |
| AI assistance safety | Disclosure completeness, human override documentation | AI governance policy + dec-0006 |
| Requirements coverage | End-to-end traceability from program objectives to decisions | Requirements traceability matrix (100% coverage) |

Evaluation focuses on decision quality and governance execution. It does not benchmark model performance in isolation.

---

## Relationship to GDI

RGDS is the biopharma reference implementation. GDI (Governed Decision Intelligence) generalizes the decision-layer architecture to domain-agnostic deployment.

```
RGDS (this repository)                 GDI
Biopharma / IND / BLA context  →  Domain-agnostic open specification
Phase-gate decision logs        →  Governed Decision Records (GDR)
IND-specific field vocabulary   →  Universal schema
FDA reconstructability focus    →  NIST AI RMF / ISO 42001 / EU AI Act
170+ commits, 6 canonical       →  Reference implementation +
  examples, CI enforcement           IETF conformance driver
```

| Repository | Purpose | DOI |
|------------|---------|-----|
| **[mj3b/rgds](https://github.com/mj3b/rgds)** | Biopharma reference implementation (this repo) | [10.5281/zenodo.20242004](https://doi.org/10.5281/zenodo.20242004) |
| **[mj3b/rgds-independent-study](https://github.com/mj3b/rgds-independent-study)** | Ten-question independent study | [10.5281/zenodo.20242004](https://doi.org/10.5281/zenodo.20242004) |
| **[mj3b/governed-decision-intelligence](https://github.com/mj3b/governed-decision-intelligence)** | GDI v3.0 open specification | [10.5281/zenodo.20244601](https://doi.org/10.5281/zenodo.20244601) |
| **[mj3b/rgds-ai-governance](https://github.com/mj3b/rgds-ai-governance)** | AI governance covenants | — |

---

## Status

**v2.0.0 — Biopharma reference implementation of the GDI v3.0 open specification.**

RGDS implements the decision-layer governance architecture defined in [GDI v3: The Decision Architecture for Governed AI](https://github.com/mj3b/governed-decision-intelligence/blob/main/spec/GDI_v3_The_Decision_Architecture_for_Governed_AI.pdf) (DOI: [10.5281/zenodo.20244601](https://doi.org/10.5281/zenodo.20244601)) for the biopharma/IND context specifically.

- Schema checks for options, evidence completeness labels, and a residual risk statement field
- Six canonical decision records covering three of the five schema outcomes
- Bounded, disclosed AI assistance (non-agentic by design)
- CI validation through the batch validator on pushes and pull requests to `main`, with manual runs available
- 100% requirements traceability matrix coverage
- Independent case study — not a production system, not regulatory advice

---

## Citation

```bibtex
@software{banasihan2026rgds,
  author    = {Banasihan, Mark Julius},
  title     = {{RGDS}: Regulated Gate Decision Support},
  year      = {2026},
  version   = {2.0.0},
  doi       = {10.5281/zenodo.20242004},
  url       = {https://doi.org/10.5281/zenodo.20242004},
  license   = {Apache-2.0}
}
```

---

## Author

**Mark Julius Banasihan**
Decision governance systems for regulated, high-stakes environments.

[GitHub](https://github.com/mj3b) · [LinkedIn](https://linkedin.com/in/markjuliusbanasihan) · [ORCID](https://orcid.org/0009-0001-8121-2878) · Atlanta, Georgia, United States
