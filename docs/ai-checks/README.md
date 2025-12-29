# RGDS AI Checks

This folder contains **informational, non-authoritative artifacts**
designed to support **human review** under compressed timelines.

AI checks in RGDS:
- do **not** recommend decisions
- do **not** accept or reject risk
- do **not** override human judgment
- do **not** operate autonomously

They exist to surface **potential inconsistencies, gaps, and dependencies**
so humans can decide deliberately.

---

## How these artifacts are used

AI checks may be:
- completed manually, or
- partially drafted using AI assistance

All outputs **must be reviewed by humans**.  
Reviewer disposition must be recorded.

Unreviewed AI-generated outputs are **not valid governance inputs**.

---

## Authority boundary (important)

AI checks **do not carry decision authority**.

If an AI check identifies a material issue, the outcome must be reflected in the **Decision Log**, not resolved here.

→ See: [`docs/decision-log.md`](../decision-log.md)

Governance, escalation, and approval rules are defined elsewhere.

→ See: [`docs/governance.md`](../governance.md)

AI usage constraints and disclosure requirements are defined here.

→ See: [`docs/ai-assistance-policy.md`](../ai-assistance-policy.md)

---

## Included AI checks

Each file in this folder follows the same pattern:
informational → human-reviewed → disposition recorded.

- **AI Consistency Check**  
  Cross-document alignment (dosing, safety, terminology)  
  → `ai-consistency-check.md`

- **AI Dependency Summary**  
  Snapshot of rate-limiting dependencies affecting gate timing  
  → `ai-dependency-summary.md`

- **AI Evidence Completeness Check**  
  Explicit acknowledgment of final, draft, and placeholder evidence  
  → `ai-evidence-completeness-check.md`

- **AI Regulatory Interaction Consistency Check**  
  Interpretation integrity for regulatory feedback  
  → `ai-regulatory-interaction-consistency-check.md`

---

## Design principle

AI checks exist to improve **decision quality**, not decision speed.

If a check matters, it must be:
- acknowledged,
- owned,
- and recorded in the Decision Log.

RGDS favors **explicit judgment over implicit automation**.
