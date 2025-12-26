# RGDS — Regulated Gate Decision Support


## Canonical Reference Decisions

If you read only one thing in this repository, read:

- `examples/rgds-dec-0001.json` — **CANONICAL conditional_go** (GO with explicit, owned conditions)
- `examples/rgds-dec-0002-no-go.json` — **CANONICAL no_go** (No-Go with defensible rationale and re-entry path)

These examples demonstrate the intended RGDS operating model: human-governed, evidence-linked, schema-validated, and explicitly non-agentic.

A human-governed system for producing defensible, phase-gate decisions in regulated environments.

This repository is not about building AI agents.
It exists to close the gap between:

- delivery evidence scattered across teams and tools, and
- decisions that must survive governance review, audit, and executive accountability.

RGDS treats the decision itself as the primary artifact.

---

## What Problem This Solves

In regulated programs, decisions often fail after they are made.

Not because teams lacked expertise, but because:

- evidence was fragmented and loosely connected
- assumptions were implicit rather than recorded
- risk acceptance was unclear or undocumented
- alignment happened too late
- decision context could not be reconstructed later

Traditional documentation focuses on inputs such as documents and analyses.
RGDS focuses on decision integrity.

---

## What This Repository Is (and Is Not)

### This is:
- a decision-support operating model for phase-gated workflows
- a structured method for making decisions defensible at the time they are made
- a human-governed system with explicit ownership and approvals
- compatible with regulated delivery, quality review, and audit

### This is not:
- an autonomous decision system
- an AI agent platform
- a recommendation engine
- a compliance checkbox or documentation dump

No component in this repository is allowed to silently decide, approve, or accept risk.

---

## How to Read This Repository (Non-Technical Overview)

This repository is organized around decisions, not tools or models.

Start with the examples directory.
Each file represents a single, concrete decision, such as a conditional-go or a no-go at a data readiness gate.

Open an example decision record first.
It shows:

- what was decided
- what evidence was used
- what risks and gaps were identified
- who owned and approved the outcome
- what conditions or actions followed

You do not need to read code to understand the decision.
The structure is designed so executives, quality, and auditors can understand why a decision was defensible.

---

## Core Concepts

### Decision Log

The primary artifact of RGDS.

A Decision Log records:
- the decision question and outcome
- options considered
- evidence used with confidence ratings
- known gaps and assumptions
- risk posture and residual risk
- named decision owner and approvers
- conditions, actions, and audit trail

The Decision Log is the system of record for governance.

---

### Evaluation

RGDS evaluates:
- decision readiness and confidence
- time-to-decision
- evidence quality
- AI-assisted task performance when used
- governance execution

Evaluation focuses on decision quality, not model performance in isolation.

---

### Governance

RGDS encodes governance directly into the decision artifact, including:
- explicit decision ownership
- separation of reviewers and approvers
- support for conditional-go and no-go outcomes
- escalation and re-review rules
- bounded and disclosed AI assistance

Stopping early is treated as risk reduction, not failure.

---

## Where AI Fits in the System

AI may be used only for bounded, reviewable support tasks such as:
- summarization
- extraction
- comparison
- drafting structured content

AI outputs:
- are never evidence of record by default
- never approve or reject decisions
- always require human review and disposition

Every decision remains defensible without AI outputs.

### Why v1 Contains No AI Components

RGDS v1 deliberately excludes AI components to establish a defensible, human-governed decision baseline before introducing automation.

In regulated environments, the primary failure modes are governance, ownership, and auditability—not analytical capability.

v1 proves the decision system stands on its own; AI may be layered in later only as bounded, reviewable assistance without altering decision authority or compliance posture.

---
## Repository Structure
```text
rgds/
├── decision-log/
│   ├── decision-log.schema.json
│   └── decision-log.schema.yaml
├── examples/
│   ├── rgds-dec-0001.json
│   ├── rgds-dec-0002-no-go.json
│   └── README.md
├── evaluation/
│   ├── evaluation-plan.md
│   ├── evidence-quality-rubric.md
│   └── scorecard-template.csv
├── docs/
│   ├── decision-log.md
│   ├── governance.md
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
- decisions made without a clear owner
- evidence that cannot be reconstructed later
- late discovery of misalignment after a gate closes
- rework caused by undocumented assumptions

By forcing decisions, evidence, risk, and ownership into a single, governed record, RGDS enables faster decisions without sacrificing confidence or auditability.

It is designed for environments where decisions must be defensible, not merely fast.

---

## Who This Is For

RGDS is written for:
- Principal AI Business Analysts
- Program and delivery leaders in regulated environments
- Quality, governance, and risk stakeholders
- Executives responsible for phase-gate approvals

It assumes familiarity with regulated delivery, not machine learning research.

---

## Status

v1 — Reference implementation complete: decision spine, evaluation artifacts, governance model, and CI enforcement.  
This repository is an independent case study, not a production system.

