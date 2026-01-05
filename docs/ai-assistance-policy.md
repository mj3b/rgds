# RGDS AI Assistance Policy
**Bounded use of AI in decision-support workflows**

---

## Purpose

This policy defines how AI assistance may be used within RGDS while preserving:

- human decision ownership
- auditability
- regulatory defensibility

AI in RGDS supports **preparation and analysis** only.  
It never approves decisions, accepts risk, or exercises authority.

---

## Scope

This policy applies to any use of AI within RGDS workflows, including:

- decision preparation
- evidence analysis
- narrative drafting
- structured data extraction
- comparison and classification tasks

This policy applies regardless of tool, vendor, or deployment model.

---

## When AI disclosure is mandatory

AI disclosure is required when AI **meaningfully influences** any of the following:

- analysis or classification that informs the decision outcome
- drafting of decision rationale, conditions, or risk statements
- prioritization or triage of evidence and gaps
- cross‑document consistency checks that affect wording or claims

If AI was used for trivial formatting only, disclosure is still recommended — but “meaningful influence” triggers mandatory disclosure.

## Minimum AI disclosure fields

When AI is used (`ai_assistance.used = true`), the decision record must capture at minimum:

- tool name and (if applicable) versioning or configuration
- purpose / use cases
- known limitations relevant to the decision context
- human review tier(s) and reviewer identity
- overrides (what AI suggested vs what human accepted) when applicable
- a simple risk assessment of AI reliance (confidence band + cautions)

## Human override taxonomy

When a human overrides AI output, record a category so overrides can be analyzed across decisions:

- factual error
- interpretive error
- omission
- regulatory / style mismatch
- contextual judgment

This taxonomy is intentionally simple — the goal is governance visibility, not perfect classification.


## Permitted AI use cases

AI assistance **may** be used for:

- summarization of existing documents
- extraction of structured data from unstructured sources
- comparison of document versions or datasets
- drafting of narratives, summaries, or checklists
- classification into predefined categories

All AI-assisted outputs must be **human-reviewable and reversible**.

---

## Prohibited AI use cases

AI assistance must **not**:

- make approval, rejection, or go/no-go decisions
- accept, reject, or optimize risk posture
- generate evidence of record
- override or substitute for expert judgment
- operate autonomously across phase gates
- initiate actions without explicit human instruction

AI outputs are **never authoritative by default**.

---

## Disclosure requirements

When AI assistance is used, the following must be recorded in the Decision Log:

- the AI use case
- references to inputs and outputs
- human disposition (`accepted` / `edited` / `rejected`)
- applicable controls and constraints

Silent or undisclosed AI usage is **not permitted**.

---

## Controls and constraints

AI usage within RGDS is governed by the **Non-Agentic AI Contract** and the
**AI Removability Proof** maintained in the AI Governance repository.

These documents define system-level prohibitions and guarantees that apply
regardless of implementation, tooling, or workflow context.

Each AI-assisted artifact must document, at minimum:

- prompt or instruction reference
- schema, template, or format constraints
- versioning or configuration identifiers
- known limitations or safety notes

These controls exist to ensure **traceability, repeatability, and audit readiness**.

---

## Review and acceptance

- All AI outputs are reviewed by qualified humans
- Reviewers may accept, edit, or reject outputs
- Rejection does not require justification, but disposition is recorded

Human review is **mandatory and non-delegable**.

---

## Risk posture

AI assistance is treated as a **potential risk amplifier** if misused.

Accordingly:

- AI use is optional, never assumed
- decisions must remain defensible without AI assistance
- removal or failure of AI tools must not block decision-making

AI is a support mechanism, not a dependency.

---

## Policy violations

If AI is used outside this policy:

- the affected decision is paused or re-reviewed
- misuse is documented in the governance record
- corrective action is taken before proceeding

Governance takes precedence over convenience or speed.

---

## Policy evolution

This policy is reviewed periodically and updated as:

- regulatory expectations evolve
- tooling or deployment models change
- new risks are identified

All policy changes are versioned, approved, and auditable.

---

## v1.4.0 transparency signals (non-authoritative)

RGDS v1.4.0 supports optional transparency fields within `ai_assistance`:

- **`confidence_band`** — `low` | `medium` | `high`  
  *(a coarse signal for context, not a performance score)*

- **`human_override`** — whether a human changed, rejected, or replaced AI-supported content

These fields exist solely for **transparency and post-hoc review**.  
They never grant AI decision authority or evidentiary weight.
