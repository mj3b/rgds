# RGDS AI Assistance Policy
**Bounded use of AI in decision-support workflows**

---

## Purpose

This policy defines how AI assistance may be used within RGDS while preserving:

- human decision ownership
- auditability
- regulatory defensibility

AI in RGDS assists with **preparation and analysis**, not approval or risk acceptance.

---

## Permitted AI use cases

AI assistance may be used for:

- summarization of existing documents
- extraction of structured data from unstructured sources
- comparison of versions or datasets
- drafting of narratives or checklists
- classification of known categories

All AI-assisted outputs must be reviewable by humans.

---

## Prohibited AI use cases

AI assistance must not:

- make approval or rejection decisions
- accept or reject risk
- generate evidence of record
- override human judgment
- operate autonomously across gates

AI outputs are not authoritative by default.

---

## Disclosure requirements

When AI assistance is used:

- the use case is disclosed in the Decision Log
- inputs and outputs are referenced
- human disposition is recorded (accepted / edited / rejected)
- controls and constraints are documented

Silent AI usage is not permitted.

---

## Controls and constraints

Each AI-assisted artifact must document:

- prompt or instruction reference
- schema or format constraints
- versioning information
- safety or limitation notes

These controls ensure repeatability and traceability.

---

## Review and acceptance

- AI outputs are reviewed by qualified humans
- Reviewers may accept, edit, or reject outputs
- Rejection does not require justification, but disposition is recorded

Human review is mandatory.

---

## Risk posture

AI assistance is treated as a **potential risk amplifier** if misused.

Therefore:
- AI use is optional, not assumed
- decisions must remain defensible without AI outputs
- removal of AI assistance must not block the decision process

---

## Policy violations

If AI is used outside this policy:

- the decision must be paused or re-reviewed
- misuse is documented
- corrective action is taken before proceeding

Governance takes precedence over convenience.

---

## Policy evolution

This policy is reviewed periodically and updated as:
- regulatory expectations evolve
- tooling changes
- new risks are identified

All policy changes are versioned and auditable.


## v1.4.0 trust signals (non-authoritative)
RGDS v1.4.0 allows optional disclosure fields inside `ai_assistance`:

- **confidence_band:** `low` | `medium` | `high` (a coarse signal, not a score)
- **human_override:** whether a human changed, rejected, or replaced AI-supported content

These are recorded for transparency and post-hoc review. They never grant AI decision authority.

