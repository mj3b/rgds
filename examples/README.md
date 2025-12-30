# Examples

These are illustrative RGDS decision records intended to show how the
Decision Log schema is used in practice across common phase-gate scenarios
in regulated delivery.

Each example represents a **single, concrete decision** with explicit
ownership, evidence linkage, risk posture, and governance controls.

---

## Canonical examples (start here)

The following examples are considered canonical because they collectively
demonstrate the full RGDS operating model across common decision outcomes.

- `rgds-dec-0001.json` — **Canonical conditional_go**  
  Go decision with explicit, owned conditions, governance approvals, and
  clearly bounded follow-up actions.

- `rgds-dec-0002-no-go.json` — **Canonical no_go**  
  Defensible refusal with documented rationale, risks, and a defined
  re-entry path.

- `rgds-dec-0003-defer-required-evidence.json` — **Canonical defer / abstain**  
  Decision deferred pending required evidence, with explicit gaps and
  re-review criteria.

- `rgds-dec-0004-regulatory-interaction.json` — **Canonical regulatory interaction / escalation**  
  Pre-IND or agency-facing decision framing, including questions, strategy,
  and governance rationale.

- `rgds-dec-0005-ind-conditional-go-author-at-risk.json` — **Canonical IND-style conditional_go**  
  IND readiness decision demonstrating author-at-risk drafting, reviewer
  triage, and publishing lock points.

- `rgds-dec-0006-ai-assisted-conditional-go.json` — **Canonical AI-assisted conditional_go**  
  Conditional-go decision demonstrating bounded AI assistance with explicit
  disclosure, preserved human authority, and full auditability.

---

## Notes on AI usage in examples

`rgds-dec-0006-ai-assisted-conditional-go.json` is the **only** example in this
repository that demonstrates AI-assisted decision preparation.

All other examples are fully human-authored and remain valid demonstrations
of the RGDS operating model without any AI involvement.

This is intentional: RGDS is designed to be **AI-optional**, and all decisions
must remain defensible in the absence of AI assistance.

