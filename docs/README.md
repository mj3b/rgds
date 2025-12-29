# RGDS Documentation

This folder contains governance, policy, and supporting artifacts
for **Regulated Gate Decision Support (RGDS)**.

Not all documents here carry equal authority.
This README exists to help reviewers and contributors **start in the right place**.

---

## Authoritative artifacts

The following documents define **how decisions are made, governed, and audited**.
They are the primary references for reviewers, auditors, and decision owners.

- **Decision Log** — the system of record  
  → [`decision-log.md`](decision-log.md)

- **Governance Model** — ownership, approvals, escalation  
  → [`governance.md`](governance.md)

- **Role–Decision–Artifact Matrix** — who owns what, and where it is recorded  
  → [`role-decision-artifact-matrix.md`](role-decision-artifact-matrix.md)

- **AI Assistance Policy** — bounded, non-authoritative use of AI  
  → [`ai-assistance-policy.md`](ai-assistance-policy.md)

---

## Supporting artifacts

The following documents **support decision preparation and review**,
but do **not** carry decision authority on their own.

- **AI Checks** — informational, human-reviewed consistency and dependency checks  
  → [`ai-checks/`](ai-checks/README.md)

- **Change Control Log** — governed evolution of schemas and rules  
  → [`change-control-log.md`](change-control-log.md)

- **Why RGDS Exists** — rationale and signal grounding  
  → [`why-rgds-exists.md`](why-rgds-exists.md)

All supporting artifacts must roll up into the **Decision Log**
to affect an actual decision.

---

## Reviewer guidance

If you are reviewing a decision artifact:

1. Start with the **Decision Log**  
   → [`decision-log.md`](decision-log.md)

2. Use supporting artifacts to understand **context and constraints**  
   (AI checks, dependency summaries, rationale)

3. Confirm **governance completeness**  
   → [`governance.md`](governance.md)

4. Ensure disposition, ownership, and approvals are **explicitly recorded**

RGDS prioritizes **clarity over volume** and **explicit judgment over implicit process**.
