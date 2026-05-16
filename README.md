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

> *In regulated programs, decisions fail after they are made — not because teams lacked expertise, but because decision logic could not be reconstructed under scrutiny.*

RGDS is the reference implementation for decision-layer governance in phase-gated regulated environments. It treats **the decision itself as the primary artifact** — structured, schema-validated, and written before memory decay and handoff loss make reconstruction impossible.

---

## The Problem RGDS Solves

FDA Complete Response Letters cite "insufficient information" in 50% of first-cycle submissions. In most of those cases, the underlying science is defensible. What organizations cannot produce is a coherent account of *why* specific decisions were made 6–18 months earlier.

```
Traditional documentation model:          RGDS model:

Documents → Analysis → Meeting            Decision Question
        ↓                                       ↓
Implicit decision                         Options Considered (≥2)
        ↓                                       ↓
Memory + email threads                    Evidence Base + Completeness
        ↓                                       ↓
Reconstruction attempt                    Risk Posture + Residual Risk
(2–3 weeks, FDA pressure)                       ↓
                                          Named Human Accountability
                                                ↓
                                          Schema Validation → Git
                                                ↓
                                          2-minute retrieval
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
│  │  evidence_base       (completeness) │                        │
│  │  risk_posture        (explicit)     │                        │
│  │  residual_risk       (structured)   │                        │
│  │  outcome             (5 types)      │                        │
│  │  accountability      (named humans) │                        │
│  │  ai_assistance       (if used)      │                        │
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
│  │  Immutable timestamps               │                        │
│  │  2-minute retrieval under FDA query │                        │
│  │  Reconstruction without interviews  │                        │
│  └─────────────────────────────────────┘                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## The Five Decision Outcomes

Every RGDS decision resolves to one of five governed outcomes. Each carries equal structural rigor — stopping is governed the same way proceeding is.

```
                    ┌──────────────────┐
                    │  Phase Gate      │
                    │  Decision Point  │
                    └────────┬─────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
          ▼                  ▼                  ▼
   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
   │     GO      │   │  CONDITIONAL│   │    DEFER    │
   │             │   │     GO      │   │             │
   │ Full conf.  │   │             │   │ Insufficient│
   │ Complete    │   │ Explicit    │   │ evidence.   │
   │ evidence.   │   │ conditions. │   │ Re-entry    │
   │ Proceed.    │   │ Named owner.│   │ criteria    │
   │             │   │ Deadline.   │   │ defined.    │
   └─────────────┘   └─────────────┘   └─────────────┘

          ┌──────────────────────────────────┐
          │                                  │
          ▼                                  ▼
   ┌─────────────┐                  ┌─────────────┐
   │   NO-GO     │                  │  ESCALATE   │
   │             │                  │             │
   │ Rejected.   │                  │ Exceeds     │
   │ Rationale   │                  │ authority   │
   │ documented. │                  │ scope.      │
   │ Re-entry    │                  │ Senior human│
   │ logic set.  │                  │ required.   │
   └─────────────┘                  └─────────────┘
```

**Defer and No-Go are first-class outcomes.** A governed No-Go is indistinguishable from a governed Go in audit quality. An ungoverned stop is indistinguishable from a failure.

---

## Decision Log Schema

The schema enforces governance-completeness at the artifact level. A decision that cannot satisfy the schema cannot be finalized.

```
decision_log/
├── decision-log.schema.json    ← Machine-enforced
├── decision-log.schema.yaml    ← Human-readable companion
└── decision-log.template.yaml  ← Starting point for new decisions
```

### Required Fields (v2.0.0)

| Field | Type | Governance Purpose |
|-------|------|--------------------|
| `decision_question` | string | Defines what choice was required |
| `decision_deadline` | date | Forces temporal accountability |
| `options_considered` | array (≥2) | Eliminates single-option rationalization |
| `evidence_base` | object | Links claims to sources |
| `evidence.completeness_state` | enum | `complete` / `partial` / `placeholder` |
| `risk_posture` | string | Forces explicit risk acceptance |
| `risk_assessment.residual_risk_items` | array | Captures what remains true after proceeding |
| `outcome` | enum | One of five governed decision types |
| `accountability.decision_owner` | string | Named human, not a role or team |
| `accountability.approvers` | array | Named humans with authority scope |
| `ai_assistance.used` | boolean | Disclosure trigger |

### Evidence Completeness Model

```
Evidence Item
     │
     ├── complete     → Final validated data. Decision proceeds on confirmed evidence.
     │
     ├── partial      → Preliminary data. Final report pending. Explicit condition
     │                  required if proceeding. Owner and deadline named.
     │
     └── placeholder  → Estimated or assumed. Must be flagged as governance gap.
                        False confidence from undocumented placeholders is the
                        failure mode this field prevents.
```

---

## Canonical Decision Records

Start here. Six examples demonstrate the full operating model across every decision outcome.

| Record | Outcome | Scenario | What It Demonstrates |
|--------|---------|----------|----------------------|
| [`rgds-dec-0001`](examples/rgds-dec-0001.json) | **conditional_go** | Data readiness gate | Explicit conditions, owned follow-ups, named approvers |
| [`rgds-dec-0002`](examples/rgds-dec-0002-no-go.json) | **no_go** | Risk threshold exceeded | Defensible refusal with re-entry logic |
| [`rgds-dec-0003`](examples/rgds-dec-0003-defer-required-evidence.json) | **defer** | Missing required evidence | Structured pause with re-review criteria |
| [`rgds-dec-0004`](examples/rgds-dec-0004-regulatory-interaction.json) | **escalate** | Pre-IND FDA interaction | Agency-facing decision framing and strategy |
| [`rgds-dec-0005`](examples/rgds-dec-0005-ind-conditional-go-author-at-risk.json) | **conditional_go** | IND authoring gate | Author-at-risk drafting, reviewer triage, lock points |
| [`rgds-dec-0006`](examples/rgds-dec-0006-ai-assisted-conditional-go.json) | **conditional_go** | AI-assisted decision | Bounded AI disclosure, preserved human authority |

> All six records are schema-validated in CI/CD on every commit. Reading one takes 5 minutes. Reading all six takes 30.

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
         ▼ When AI is used, these fields are required:
┌──────────────────────────────────────────────────────────────┐
│  ai_assistance.used           → true                         │
│  ai_assistance.tool_name      → which system                 │
│  ai_assistance.tool_purpose   → what task                    │
│  ai_assistance.human_review[] → review tier + findings       │
│  ai_assistance.human_override_log[] → corrections made       │
│  ai_assistance.ai_risk_assessment → confidence band+cautions │
└──────────────────────────────────────────────────────────────┘
         │
         ▼ Human decision owner remains fully responsible.
           AI disclosure transfers no authority, approval
           rights, or risk ownership.
```

**Evidence rule:** AI output is never treated as primary evidence. If an AI output influences a decision, the human owner must link to the underlying source and record the AI output as a drafting aid. Every decision must remain defensible without the AI output present.

Authoritative AI governance covenants: **[rgds-ai-governance](https://github.com/mj3b/rgds-ai-governance)**

---

## IND Alignment — Execution Realities → RGDS Mechanisms

RGDS formalizes failure modes observed during IND preparation. Each mechanism addresses a specific, named execution pattern.

| Execution Reality | Failure Mode Prevented | RGDS Mechanism |
|-------------------|----------------------|----------------|
| Placeholders proceed without governance | False confidence, FDA gap finding | `evidence.completeness_state` + author-at-risk constraints |
| Scope changes emerge late without a trail | Silent ripple effects across modules | `scope_change_events[]` + downstream propagation |
| Reviewer routing is informal | Unclear accountability under audit | `review_plan` + named triage owner |
| Risk posture is implied, not stated | Cannot defend tolerance decisions to FDA | `risk_posture` + `residual_risk_items` |
| Cross-module dependencies are mentally tracked | Late-discovered misalignment after gate closes | `dependency_map[]` |
| Phase-gate tolerance is assumed shared | Silent misalignment between functions | Explicit risk posture field, cross-functional sign-off |
| Regulatory interaction strategy is informal | Weak pre-IND positioning | `decision_category: regulatory_interaction` |
| AI assistance is undisclosed | Provenance contamination, audit exposure | `ai_assistance` disclosure schema (mandatory when used) |

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
│   ├── rgds-dec-0003-defer-*.json   ← Defer (canonical)
│   ├── rgds-dec-0004-regulatory-*.json ← Escalation (canonical)
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

v2.0.0 tightens decision defensibility. It does not add automation or autonomy.

| Change | What it enforces | Failure mode prevented |
|--------|-----------------|----------------------|
| Options enumeration (≥2 required) | At least two options must be considered | Single-option rationalization passing as governance |
| Evidence completeness per item | `complete` / `partial` / `placeholder` on every evidence item | False confidence from undocumented placeholders |
| Structured residual risk | `residual_risk_items[]` array | Risk acceptance without recording what remains true |
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

- Schema-enforced decision logs with mandatory options analysis, evidence completeness, and residual risk
- Six canonical decision records spanning all five outcomes
- Bounded, disclosed AI assistance (non-agentic by design)
- CI/CD validation of schema and semantic invariants on every commit
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
