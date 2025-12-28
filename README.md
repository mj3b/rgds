# RGDS — Regulated Gate Decision Support

## Canonical Reference Decisions

If you read only one thing in this repository, read:

- `examples/rgds-dec-0001.json` — **CANONICAL conditional_go** (GO with explicit, owned conditions)
- `examples/rgds-dec-0002-no-go.json` — **CANONICAL no_go** (No-Go with defensible rationale and re-entry path)
- `examples/rgds-dec-0003-defer-required-evidence.json` — **CANONICAL defer / abstain** (Decision deferred pending required evidence; explicit gaps)
- `examples/rgds-dec-0004-regulatory-interaction.json` — **CANONICAL regulatory interaction / escalation** (Pre-engagement or agency-facing decision logic + rationale capture)
- `examples/rgds-dec-0005-ind-conditional-go-author-at-risk.json` — **CANONICAL IND-style conditional_go** (author-at-risk + reviewer triage + publishing lock points)

These examples demonstrate the intended RGDS operating model: human-governed, evidence-linked, schema-validated, and explicitly non-agentic.

---

## What’s New in v1.4.0

Version 1.4.0 makes previously implicit governance decisions explicit, based on
observed failure modes in real IND delivery and cross-functional review.

Newly formalized concepts include:
- explicit evidence completeness states (complete / partial / placeholder)
- downstream propagation declarations when evidence or decisions change
- risk posture benchmarking (not just declaration)
- explicit decision authority scope and escalation paths
- bounded AI assistance disclosure (confidence band + human override)

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

For the evidence-to-design rationale behind RGDS, see: `docs/why-rgds-exists.md`.

---

## What This Repository Is (and Is Not)

### This is:
- a decision-support operating model for phase-gated workflows
- a structured method for making decisions defensible at the time they are made
- a human-governed system with explicit ownership and approval
- compatible with regulated delivery, quality review, and audit expectations
- a schema-backed decision log system that makes decision context, risk, and ownership auditable

### This is not:
- an autonomous decision system
- an AI agent platform
- a recommendation engine
- a compliance checkbox or document dump

No component in this repository is allowed to silently decide, approve, or accept risk.

---

## How to Read This Repository (Non-Technical Overview)

This repository is organized around **decisions**, not tools or models.

Start with the `examples/` directory.  

A typical review path is:
1. Read one canonical example (0001, 0003, or 0005)
2. Review the decision-log schema to see what is enforced
3. Skim the evaluation plan to understand how decision quality is assessed

Each file represents a single, concrete decision at a gate, such as a conditional-go, defer, or no-go.

Each decision record shows:
- what was decided
- why it was decided
- what evidence was used (and its quality)
- what risks and gaps were accepted
- who owned, reviewed, and approved the decision
- what conditions, follow-ups, or fallback actions exist
- the completeness state of evidence (complete, partial, placeholder)
- whether downstream artifacts must be updated if this decision changes

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

- **risk_posture**: phase-appropriate tolerance and trade-offs are stated, not inferred.
- **author-at-risk drafting**: placeholder drafting is treated as governed risk with verification criteria.
- **review_plan**: reviewer triage (required vs optional) is captured explicitly.
- **scope_change_events[]**: late discoveries and scope volatility become auditable decision inputs.
- **dependency_map[]**: interdependencies are captured as decision inputs (prevents cascading surprises).
- **data_readiness_status[]**: tracks rate-limiting evidence readiness (draft → audited draft → final), now formalized under evidence completeness in v1.4.0.
- **publishing_plan**: rolling publishing and lock points become explicit constraints.
- **tpp_links[]**: tie decisions back to Target Product Profile expectations.

The existing `decision_category` + `regulatory_context` fields model pre-IND / FDA interaction strategy as a first-class decision.

These additions reflect real execution realities without introducing automation risk.

For a cross-role view of who owns what, see: `docs/role-decision-artifact-matrix.md`.

---

### Evaluation

RGDS evaluates:
- explicit authority scope, escalation paths, and downstream propagation requirements
- disclosure of AI assistance usage when applicable

Evaluation focuses on **decision quality**, not model performance in isolation.

Evaluation is performed through structured review criteria and scorecards, not automated model metrics.

Evaluation explicitly considers evidence completeness, declared risk posture, and downstream propagation awareness.

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
→ [https://github.com/mj3b/rgds-ai-governance]

---

## Where AI Fits in the System

RGDS is valid with **no AI at all**.

When AI is used, it is used only as **bounded assistance** to help humans produce or review
decision artifacts faster—without changing who owns the decision or what counts as evidence.

### Permitted AI-Assisted Tasks (Bounded)

AI may be used for reviewable support tasks such as:

- **Summarization**: produce a draft summary of a source report or meeting notes for human edit
- **Extraction**: pull structured fields (dates, study IDs, endpoints, risks) into a draft template
- **Comparison / diffing**: highlight inconsistencies across artifacts (e.g., IB vs M2.6 vs Protocol)
- **Structured drafting**: draft sections of a decision log entry (context, options, risks) for human completion
- **Checklist support**: flag missing required fields or mismatches against schema expectations

### Prohibited Uses (Non-Agentic Boundary)

AI must not:

- decide, approve, or reject a gate outcome
- act as an “evidence of record” source by default
- silently accept scope changes, risk posture, or reviewer routing
- execute actions (publishing, submissions, notifications) without explicit human authorization
- fabricate citations, source data, or regulatory rationale

### What Gets Logged When AI Is Used (v1.4.0)

If AI assistance is used for a decision artifact, the usage must be disclosed in the decision log:

- whether AI was used (`ai_assist.used`)
- the confidence band reported by the assistant (`ai_assist.confidence_band`)
- whether a human override occurred (`ai_assist.human_override`)

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

- `docs/why-rgds-exists.md` — evidence-to-design rationale (signals → RGDS mechanisms)
- `docs/decision-log.md` — how to interpret decision logs
- `docs/governance.md` — governance rules and enforcement intent

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
