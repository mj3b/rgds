# RGDS — Regulated Gate Decision Support

## Canonical Reference Decisions

If you read only one thing in this repository, read the canonical examples in `examples/`:

- `rgds-dec-0001.json` — **CANONICAL conditional_go**  
  GO with explicit conditions, risk posture, and fallback planning

- `rgds-dec-0002-no-go.json` — **CANONICAL no_go**  
  No-Go with defensible rationale and re-entry path

- `rgds-dec-0003-defer-required-evidence.json` — **CANONICAL defer_with_required_evidence**  
  Deferral with explicit missing evidence and decision re-trigger

- `rgds-dec-0004-regulatory-interaction.json` — **CANONICAL regulatory_interaction_decision**  
  Pre-IND / FDA interaction strategy as a first-class decision artifact

- `rgds-dec-0005-conditional-go-author-at-risk.json` — **CANONICAL author_at_risk conditional_go**  
  Controlled placeholder drafting with verification criteria and fallback

- `rgds-dec-0006-go-pre-ind-strategy.json` — **CANONICAL go with regulatory posture**  
  Phase-appropriate risk posture with contingency planning

These examples demonstrate the intended RGDS operating model:
**human-governed, evidence-linked, schema-validated, and explicitly non-agentic**.

RGDS is a human-governed system for producing **defensible phase-gate decisions** in regulated environments.

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

---

## What This Repository Is (and Is Not)

### This is:
- a decision-support operating model for phase-gated workflows
- a structured method for making decisions defensible at the time they are made
- a human-governed system with explicit ownership and approval
- compatible with regulated delivery, quality review, and audit expectations

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
Each file represents a single, concrete decision at a gate, such as a conditional-go, defer, or no-go.

Each decision record shows:
- what was decided
- why it was decided
- what evidence was used (and its quality)
- what risks and gaps were accepted
- who owned, reviewed, and approved the decision
- what conditions, follow-ups, or fallback actions exist

Executives, quality reviewers, and auditors should be able to understand **why a decision was reasonable** without reading code.

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

### Risk Posture & Conditional Decisions (v1.2)

RGDS v1.2 makes previously implicit judgment calls explicit:

- **risk_posture**  
  Phase-appropriate tolerance and trade-offs are stated, not inferred.

- **author_at_risk_items[]**  
  Placeholder drafting is treated as a governed risk with verification criteria.

- **review_plan**  
  Reviewer triage (required vs optional) is captured as a decision, not process trivia.

- **scope_change_events[]**  
  Late discoveries and scope volatility become auditable decision inputs.

- **regulatory_interaction_decision**  
  FDA / pre-IND interaction strategy is modeled as a first-class decision.

- **fallback_plan (required for conditional_go)**  
  Proceeding under uncertainty requires an explicit contingency.

These additions reflect real execution realities without introducing automation risk.

---

### Evaluation

RGDS evaluates:
- decision readiness and confidence
- evidence quality and sufficiency
- time-to-decision
- governance execution
- AI-assisted task performance (when used)

Evaluation focuses on **decision quality**, not model performance in isolation.

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

## Where AI Fits in the System

AI may be used only for bounded, reviewable support tasks such as:
- summarization
- extraction
- comparison
- structured drafting

AI outputs:
- are never evidence of record by default
- never approve or reject decisions
- always require human review and disposition

Every decision remains defensible **without AI outputs present**.

### Why v1.x Contains No AI Components

RGDS v1.x deliberately excludes AI components to establish a defensible, human-governed decision baseline before introducing automation.

In regulated environments, primary failure modes are governance, ownership, and auditability — not analytical capability.

AI may be layered in later only as bounded, reviewable assistance.

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
│   ├── rgds-dec-0005-conditional-go-author-at-risk.json
│   ├── rgds-dec-0006-go-pre-ind-strategy.json
│   └── README.md
├── evaluation/
│   ├── evaluation-plan.md
│   ├── evidence-quality-rubric.md
│   └── scorecard-template.csv
├── docs/
│   ├── decision-log.md
│   ├── governance.md
│   ├── change-control-log.md
│   └── ai-assistance-policy.md
├── scripts/
│   ├── validate_decision_log.py
│   └── validate_all_examples.py
├── .github/workflows/
│   └── validate.yml
├── Makefile
└── requirements.txt
```
---

## Why This Matters in Production

RGDS prevents failure modes that routinely appear in regulated delivery:

- silent risk acceptance  
- undocumented scope changes  
- unclear reviewer accountability  
- decisions without fallback planning  
- late discovery of misalignment after a gate closes  

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

**v1.2 — Reference implementation complete.**

Includes:

- decision log schema with enforcement  
- canonical examples grounded in real IND execution  
- evaluation and governance artifacts  
- CI validation  

This repository is an independent case study, not a production system.
