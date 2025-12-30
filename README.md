# RGDS — Regulated Gate Decision Support
<!-- RGDS governance + repository signals -->
[![Status: Independent Case Study](https://img.shields.io/badge/status-independent%20case%20study-5b6cff)](#status)
[![Human Governed](https://img.shields.io/badge/governance-human--governed-3bb273)](#governance)
[![Non-Agentic](https://img.shields.io/badge/AI-explicitly%20non--agentic-2d7ff9)](#prohibited-uses-non-agentic-boundary)
[![Decision Defensibility](https://img.shields.io/badge/outcome-decision%20defensibility-6f42c1)](#what-problem-this-solves)
[![Audit Ready](https://img.shields.io/badge/property-audit--ready%20artifacts-0aa2c0)](#evaluation)
[![No Autonomy](https://img.shields.io/badge/constraint-no%20autonomous%20execution-ff7a00)](#what-this-repository-is-and-is-not)

[![License](https://img.shields.io/github/license/mj3b/rgds)](LICENSE)
[![Stars](https://img.shields.io/github/stars/mj3b/rgds)](https://github.com/mj3b/rgds/stargazers)
[![CI Validation](https://img.shields.io/github/actions/workflow/status/mj3b/rgds/validate.yml)](https://github.com/mj3b/rgds/actions/workflows/validate.yml)

[![Schema Enforced](https://img.shields.io/badge/schema-decision%20log%20enforced-1f6feb)](#decision-log)

A human-governed system for producing defensible, phase-gate decisions in regulated environments.

This repository demonstrates the RGDS operating model: **human-governed, evidence-linked, schema-validated, and explicitly non-agentic.**

---

## Table of Contents

- [Canonical Reference Decisions](#canonical-reference-decisions)
- [What’s New in v1.4.0](#whats-new-in-v140)
- [What Problem This Solves](#what-problem-this-solves)
- [What This Repository Is (and Is Not)](#what-this-repository-is-and-is-not)
  - [This is](#this-is)
  - [This is not](#this-is-not)
  - [Important Notice](#important-notice)
- [How to Read This Repository (Non-Technical Overview)](#how-to-read-this-repository-non-technical-overview)
- [Core Concepts](#core-concepts)
  - [Decision Log](#decision-log)
  - [IND Delivery Alignment (v1.3 → v1.4)](#ind-delivery-alignment-v13--v14)
  - [Evaluation](#evaluation)
  - [Governance](#governance)
  - [AI Governance Reference](#ai-governance-reference)
- [Where AI Fits in the System](#where-ai-fits-in-the-system)
  - [Permitted AI-Assisted Tasks (Bounded)](#permitted-ai-assisted-tasks-bounded)
  - [Prohibited Uses (Non-Agentic Boundary)](#prohibited-uses-non-agentic-boundary)
  - [What Gets Logged When AI Is Used (v1.4.0)](#what-gets-logged-when-ai-is-used-v140)
  - [Evidence Rule](#evidence-rule)
  - [Why RGDS v1.x Contains No Built-In AI Components](#why-rgds-v1x-contains-no-built-in-ai-components)
- [Repository Structure](#repository-structure)
- [Key Docs](#key-docs)
- [Why This Matters in Production](#why-this-matters-in-production)
- [Who This Is For](#who-this-is-for)
- [Status](#status)

---

## Canonical Reference Decisions

If you read only one thing in this repository, read:

| File | Canonical Outcome | What it demonstrates |
|---|---|---|
| `examples/rgds-dec-0001.json` | **CANONICAL conditional_go** | GO with explicit, owned conditions |
| `examples/rgds-dec-0002-no-go.json` | **CANONICAL no_go** | No-Go with defensible rationale and re-entry path |
| `examples/rgds-dec-0003-defer-required-evidence.json` | **CANONICAL defer / abstain** | Decision deferred pending required evidence; explicit gaps |
| `examples/rgds-dec-0004-regulatory-interaction.json` | **CANONICAL regulatory interaction / escalation** | Pre-engagement or agency-facing decision logic + rationale capture |
| `examples/rgds-dec-0005-ind-conditional-go-author-at-risk.json` | **CANONICAL IND-style conditional_go** | author-at-risk + reviewer triage + publishing lock points |

These examples demonstrate the intended RGDS operating model: **human-governed, evidence-linked, schema-validated, and explicitly non-agentic.**

---

## What’s New in v1.4.0

Version 1.4.0 makes previously implicit governance decisions explicit, based on
observed failure modes in real IND delivery and cross-functional review.

### Newly formalized concepts (v1.4.0)

| Concept | What is now explicit | Why it matters |
|---|---|---|
| Evidence completeness | complete / partial / placeholder | prevents “false confidence” from undocumented placeholders |
| Downstream propagation | declarations when evidence or decisions change | prevents silent ripple effects across artifacts |
| Risk posture benchmarking | not just declaration | forces defensible rationale for tolerance/assumptions |
| Decision authority scope | scope + escalation paths | prevents unclear accountability and “who approved this?” gaps |
| Bounded AI disclosure | confidence band + human override | makes AI use reviewable without changing accountability |

These changes do not introduce automation or autonomy.  
They tighten decision defensibility.

---

## What Problem This Solves

In regulated programs, decisions often fail **after** they are made.

Not because teams lacked expertise, but because:

- scope changed late without being logged
- assumptions and risk posture were implicit
- reviewer routing decisions were undocumented
- contingency plans existed only informally
- decision context could not be reconstructed later

Traditional documentation emphasizes inputs (documents, analyses, reports).  
**RGDS treats the decision itself as the primary artifact.**

RGDS is informed by synthesis of real delivery experience, including public IND
submission discussions, regulatory strategy perspectives, and operational interviews.
These sources are treated as signal inputs, not prescriptions, and are translated
into explicit, auditable decision structure.

For the evidence-to-design rationale behind RGDS, see:  
→ `docs/why-rgds-exists.md`

---

## What This Repository Is (and Is Not)

### This is

| Statement | Practical meaning |
|---|---|
| a decision-support operating model for phase-gated workflows | decisions become governed artifacts, not informal meeting outcomes |
| a structured method for making decisions defensible at the time they are made | captures rationale before memory decay and handoff loss |
| a human-governed system with explicit ownership and approval | named owner + reviewer(s) + approver(s), with escalation |
| compatible with regulated delivery, quality review, and audit expectations | decision records designed for audit reconstruction |
| a schema-backed decision log system that makes decision context, risk, and ownership auditable | required fields and validation discipline enforce completeness |

### This is not

| Statement | What is explicitly excluded |
|---|---|
| an autonomous decision system | no autonomous gate outcomes |
| an AI agent platform | no agents, orchestration, or self-directed execution |
| a recommendation engine | no “system decides” or “system recommends” authority |
| a compliance checkbox or document dump | evidence must be linked and interpreted as decision inputs |

No component in this repository is allowed to silently decide, approve, or accept risk.

---

## Important Notice

RGDS is an **independent reference implementation** intended to demonstrate
decision-governance patterns in regulated, phase-gated environments.

It is:

- not a production system
- not regulatory advice
- not a compliance framework
- not an autonomous or agentic system

RGDS does not make decisions.  
It records how decisions are made, governed, and defended.

All regulatory, quality, and approval responsibilities remain with the
human decision-makers and organizations using this material.

---

## How to Read This Repository (Non-Technical Overview)

This repository is organized around **decisions**, not tools or models.

Start with the `examples/` directory.

### A typical review path

| Step | What to read | Why |
|---|---|---|
| 1 | one canonical example (`0001`, `0003`, or `0005`) | see the operating model in a real decision |
| 2 | the decision-log schema | see what is enforced vs. optional |
| 3 | the evaluation plan | see how decision quality is assessed |

Each file represents a single, concrete decision at a gate, such as a conditional-go, defer, or no-go.

### Each decision record shows

| Dimension | What is captured |
|---|---|
| Decision | what was decided |
| Rationale | why it was decided |
| Evidence | what evidence was used (and its quality) |
| Risk | what risks and gaps were accepted |
| Accountability | who owned, reviewed, and approved the decision |
| Controls | what conditions, follow-ups, or fallback actions exist |
| Evidence completeness | complete / partial / placeholder |
| Propagation | whether downstream artifacts must be updated if the decision changes |

Executives, quality reviewers, and auditors should be able to understand **why a decision was reasonable** without reading code.

This repository reflects the role of a principal-level analyst translating complex delivery realities into durable decision infrastructure.

It is intended to demonstrate how delivery experience, governance constraints and applied AI considerations can be translated into defensible decision systems.

---

## Core Concepts

### Decision Log

The primary artifact of RGDS.

A Decision Log records:

- the decision question and outcome
- options considered
- evidence used with confidence ratings
- known gaps, assumptions, and scope changes
- explicit risk posture and residual risk
- named decision owner, reviewers, and approvers
- conditions, actions, and fallback plans
- a durable audit trail

The Decision Log is the **system of record for governance**.

---

### IND Delivery Alignment (v1.3 → v1.4)

RGDS formalizes execution realities observed during IND preparation:

| Execution reality observed in IND delivery | RGDS mechanism / field |
|---|---|
| phase-appropriate tolerance and trade-offs must be stated | **risk_posture** |
| placeholders must be governed and verified | **author-at-risk drafting** + evidence completeness |
| reviewer triage decisions must be explicit | **review_plan** |
| late discoveries and scope volatility must be auditable | **scope_change_events[]** |
| cross-module surprises must be prevented | **dependency_map[]** |
| evidence readiness is rate limiting | **data_readiness_status[]** → formalized under evidence completeness in v1.4.0 |
| publishing is constrained by lock points | **publishing_plan** |
| decisions must tie back to program intent | **tpp_links[]** |

The existing `decision_category` + `regulatory_context` fields model pre-IND / FDA interaction strategy as a first-class decision.

These additions reflect real execution realities without introducing automation risk.

For a cross-role view of who owns what, see:  
→ `docs/role-decision-artifact-matrix.md`

---

### Evaluation

RGDS evaluates:

| Evaluation focus | How it is assessed |
|---|---|
| authority scope, escalation paths, and downstream propagation requirements | structured review criteria |
| AI assistance disclosure (when applicable) | explicit decision-log disclosure fields |
| evidence completeness, risk posture, propagation awareness | scorecards and rubrics |

Evaluation focuses on **decision quality**, not model performance in isolation.

Evaluation is performed through structured review criteria and scorecards, not automated model metrics.

---

### Governance

Governance is encoded directly into the decision artifact:

- explicit ownership and accountability
- separation of reviewers and approvers
- support for conditional-go, defer, and no-go outcomes
- escalation and re-review rules
- bounded, disclosed AI assistance

Stopping early is treated as **risk reduction**, not failure.

---

#### AI Governance Reference

RGDS supports optional, bounded AI assistance under explicit governance constraints.

The formal governance covenants that define:

- permitted AI assistance,
- explicit prohibitions (including non-agentic requirements), and
- human ownership and approval obligations

are maintained externally to preserve separation of concerns.

RGDS remains fully valid in the absence of AI.

For the authoritative governance definition, see:  
**RGDS AI Governance (Covenants)**  
→ https://github.com/mj3b/rgds-ai-governance

---

## Where AI Fits in the System

RGDS is valid with **no AI at all**.

When AI is used, it is used only as **bounded assistance** to help humans produce or review
decision artifacts faster—without changing who owns the decision or what counts as evidence.

### Permitted AI-Assisted Tasks (Bounded)

AI may be used for reviewable support tasks such as:

| Task | Example use | Constraint |
|---|---|---|
| **Summarization** | draft summary of a source report or meeting notes | human edits and signs off |
| **Extraction** | pull structured fields (dates, study IDs, endpoints, risks) | output treated as draft |
| **Comparison / diffing** | highlight inconsistencies (e.g., IB vs M2.6 vs Protocol) | human resolves conflicts |
| **Structured drafting** | draft decision-log sections (context, options, risks) | owner finalizes content |
| **Checklist support** | flag missing fields or schema mismatches | does not “approve” compliance |

### Prohibited Uses (Non-Agentic Boundary)

AI must not:

- decide, approve, or reject a gate outcome
- act as an “evidence of record” source by default
- silently accept scope changes, risk posture, or reviewer routing
- execute actions (publishing, submissions, notifications) without explicit human authorization
- fabricate citations, source data, or regulatory rationale

### What Gets Logged When AI Is Used (v1.4.0)

If AI assistance is used for a decision artifact, the usage must be disclosed in the decision log:

| Disclosure | Field | Meaning |
|---|---|---|
| AI used? | `ai_assist.used` | transparency |
| Confidence band | `ai_assist.confidence_band` | informational only |
| Human override | `ai_assist.human_override` | records corrective intervention |

This disclosure is informational only. It does not change accountability:  
**the decision owner remains responsible for final content and outcome.**

### Evidence Rule

AI output is never treated as evidence by default.

If an AI output influences a decision, the human owner must:

- link to the underlying source artifacts used, and
- record the AI output as a *drafting aid* or *analysis note*, not as primary evidence.

Every decision must remain defensible **without the AI output present**.

### Why RGDS v1.x Contains No Built-In AI Components

RGDS v1.x intentionally contains no bundled AI models, agents, or orchestration logic.

This is deliberate:

- the core problem in regulated programs is usually **governance failure**, not lack of analysis
- adding automation before decision discipline increases risk (silent changes, unclear ownership, weak audit trails)
- RGDS must remain usable in environments where AI is restricted or not trusted

AI can be layered later as optional tooling around RGDS (e.g., diffing, extraction, drafting),
but the governed decision record and validation discipline remain the foundation.

---

## Repository Structure

```text
rgds/
├── decision-log/
│   ├── decision-log.schema.json
│   ├── decision-log.schema.yaml
│   └── decision-log.template.yaml
├── examples/
│   ├── rgds-dec-0001.json
│   ├── rgds-dec-0002-no-go.json
│   ├── rgds-dec-0003-defer-required-evidence.json
│   ├── rgds-dec-0004-regulatory-interaction.json
│   ├── rgds-dec-0005-ind-conditional-go-author-at-risk.json
│   └── README.md
├── evaluation/
│   ├── evaluation-plan.md
│   ├── evidence-quality-rubric.md
│   └── scorecard-template.csv
├── docs/
│   ├── why-rgds-exists.md
│   ├── decision-log.md
│   ├── governance.md
│   ├── change-control-log.md
│   ├── ai-assistance-policy.md
│   └── role-decision-artifact-matrix.md
├── scripts/
│   ├── validate_decision_log.py
│   └── validate_all_examples.py
├── .github/workflows/
│   └── validate.yml
├── Makefile
└── requirements.txt
```
---

## Key Docs

| File | What it is |
|---|---|
| `docs/why-rgds-exists.md` | Evidence-to-design rationale (signals → RGDS mechanisms) |
| `docs/decision-log.md` | How to interpret decision logs |
| `docs/governance.md` | Governance rules and enforcement intent |

---

## Why This Matters in Production

RGDS prevents failure modes that routinely appear in regulated delivery:

- silent risk acceptance  
- undocumented scope changes and downstream ripple effects  
- unclear reviewer accountability  
- decisions without fallback planning  
- late discovery of misalignment after a gate closes  
- false confidence created by undocumented placeholders  

By forcing decisions, evidence, risk, ownership, and contingency into a single governed record, RGDS enables faster decisions without sacrificing auditability.

---

## Who This Is For

RGDS is written for:

- Principal AI Business Analysts  
- Program and delivery leaders in regulated environments  
- Quality, governance, and risk stakeholders  
- Executives responsible for phase-gate approvals  

It assumes familiarity with regulated delivery — not machine learning research.

---

## Status

**v1.4.0 — Reference implementation with explicit governance deltas.**

Includes:

- decision log schema with enforcement  
- canonical examples grounded in real IND execution  
- evaluation and governance artifacts  
- CI validation  

This repository is an independent case study, not a production system.
