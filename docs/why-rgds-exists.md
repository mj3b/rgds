# Why RGDS Exists

## Purpose

RGDS (Regulated Gate Decision Support) exists to address repeated, observable failure modes
in regulated, phase-gated delivery—particularly during IND preparation and review—where
decisions fail **after** they are made.

These failures are not primarily caused by lack of expertise or analytical capability.
They emerge from **implicit judgment, undocumented trade-offs, and governance gaps** that
surface only under time pressure or external scrutiny.

RGDS translates these recurring patterns into **explicit, auditable decision structure**.

---

## Source attribution note

The signal patterns described in this document are derived from:

- public IND submission webinars  
- public regulatory strategy discussions  
- structured operational interviews  

Individuals are referenced by **first name and functional role** to preserve context.
They are cited as **signal sources**, not as decision owners, endorsers, or evaluators.

---

## Signal Group 1 — Execution & Writing Reality  
*(Kasturi — Medical Writing, Public IND Webinar)*

### Observed execution patterns

Across IND execution discussions, the following patterns recur:

- **Hidden scope surfaces late**  
  Reports, tables, or analyses assumed “out of scope” emerge during drafting or review.

- **Late source reports create false certainty**  
  Teams proceed with placeholders while downstream timelines implicitly assume final data.

- **Cross-document dependencies are manually tracked**  
  A change in one module requires mental tracking of narrative and data propagation.

- **Placeholder discomfort is cultural, not technical**  
  Risk aversion delays explicit acknowledgment of uncertainty.

- **Reviewer bottlenecks appear late**  
  Required reviewers are identified only after content is already drafted.

- **Late-breaking studies force compressed reviews**  
  Inclusion decisions are made under time pressure.

- **Source discrepancies propagate silently**  
  Writers flag issues, but no system enforces correction traceability.

- **Parallel authoring increases narrative drift**  
  Speed optimizations create misalignment across sections.

### Failure modes if unmanaged

- late rework and timeline slips  
- internally inconsistent narratives  
- reviewer confusion or distrust  
- increased regulatory questioning  
- erosion of submission credibility  

### RGDS design response (v1.4.0)

These signals directly informed:

- **evidence_completeness**  
  Explicit declaration of complete, partial, or placeholder evidence.

- **propagation_required**  
  Required downstream updates are declared at decision time.

- **author-at-risk modeling**  
  Placeholder drafting is treated as governed risk, not informal practice.

- **review_plan**  
  Reviewer requirements are explicit, not assumed.

- **dependency awareness**  
  Cross-artifact impacts are recorded as decision inputs.

RGDS does not prevent uncertainty.  
It prevents **undocumented uncertainty**.

---

## Signal Group 2 — Regulatory Strategy & Risk  
*(Drew — Regulatory Leadership, Public IND Webinar)*

### Observed strategic patterns

Regulatory planning discussions consistently surface:

- **Implicit risk tolerance**  
  Teams lack shared clarity on how aggressive is “acceptable.”

- **Discovery mindset persists into regulatory phases**  
  Language and expectations fail to reset at phase transitions.

- **FDA sufficiency thresholds are opaque**  
  Decisions rely on experience rather than documented rationale.

- **Internal disagreement precedes external exposure**  
  Misalignment is discovered by regulators, not resolved internally.

- **Pre-IND timing is under-structured**  
  Engagement decisions lack explicit trade-off capture.

- **Novel approaches lack justification trails**  
  Innovation decisions are hard to defend retroactively.

- **Contingency planning is informal**  
  “What if FDA says no?” is rarely logged as a decision.

- **Complex CMC maturity gates dominate timelines**  
  Acceptance decisions lack explicit dependency logic.

- **Target Product Profile drift occurs silently**  
  Decisions detach from original development intent.

- **Claims outpace substantiation**  
  Support gaps surface late, often at NDA stage.

### Failure modes if unmanaged

- decision paralysis or over-conservatism  
- regulatory surprises  
- late-stage rework at higher cost  
- loss of institutional confidence  
- weakened regulatory trust  

### RGDS design response (v1.4.0)

These signals informed:

- **explicit risk_posture with benchmarking**  
  Risk tolerance is declared and contextualized.

- **decision_category + regulatory_context**  
  Phase intent is explicit, not inferred.

- **rationale capture**  
  “Why this was sufficient” is preserved.

- **authority_scope + escalation_path**  
  Strategic ownership is visible and auditable.

- **re-entry paths**  
  No-go and defer decisions include forward options.

- **TPP linkage**  
  Decisions remain anchored to stated program intent.

RGDS does not choose strategy.  
It ensures strategy is **explainable**.

---

## Signal Group 3 — Operations, Culture, and AI Adoption  
*(Gabby — Operations & AI Enablement, Structured Interview)*

### Observed operational patterns

Operational and AI adoption discussions reveal:

- **Decision paralysis under shared ownership**  
  Authority is unclear across teams.

- **Process friction accumulates quietly**  
  “Red tape” obscures missing decision clarity.

- **Resource constraints drive hidden trade-offs**  
  Capacity limits are rarely explicit at decision time.

- **Change resistance follows trust gaps**  
  AI skepticism stems from unclear accountability.

- **Executive reporting abstracts away decision logic**  
  Status decks replace decision traceability.

### Failure modes if unmanaged

- delayed decisions  
- burnout and quality erosion  
- failed adoption of new systems  
- executive misalignment  
- loss of delivery confidence  

### RGDS design response (v1.4.0)

These signals informed:

- **decision ownership fields**  
  Someone is always accountable.

- **authority mapping**  
  Who decides vs who advises is explicit.

- **capacity-aware decisions**  
  Trade-offs are visible, not implied.

- **AI assistance disclosure**  
  Trust is built through transparency, not capability claims.

- **decision summaries**  
  Executives see *why*, not just status.

RGDS treats culture as a **governance input**, not an afterthought.

---

## What RGDS explicitly rejects

RGDS is intentionally **not**:

- an autonomous decision system  
- an AI agent framework  
- a recommendation engine  
- a compliance artifact generator  

It explicitly rejects:

- silent risk acceptance  
- undocumented scope change  
- opaque AI involvement  
- retrospective justification  

---

## Why this is a system (not a template)

Templates capture information.  
Systems enforce **decision discipline**.

RGDS combines:

- enforced schema  
- explicit governance fields  
- evaluation criteria  
- validation tooling  
- canonical examples  

to ensure decisions remain **defensible under scrutiny**, not merely reasonable at the
moment they were made.

---

## Relationship to v1.4.0

Version 1.4.0 formalizes what these signals demanded:

- explicit evidence completeness  
- downstream propagation awareness  
- authority and escalation clarity  
- risk benchmarking  
- AI assistance disclosure  

RGDS v1.4.0 is not more complex.  
It is more **honest**.

---

## Closing

RGDS exists because regulated programs do not fail for lack of intelligence.
They fail when **decisions cannot be reconstructed, defended, or trusted**.

This repository represents one principled response to that reality.
