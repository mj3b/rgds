#!/usr/bin/env python3
"""
RGDS Validation Script — validate_decision_log.py

Purpose
-------
Validates a single RGDS decision log instance.

Modes
-----
1) Schema-only (default)
   - Ensures the JSON instance conforms to decision-log.schema.json

2) Schema + semantic checks (--semantic)
   - Enforces governance invariants that schema alone cannot express
   - Emits non-fatal warnings for strongly recommended patterns

3) Strict mode (--strict / --warn-as-error)
   - Treats semantic warnings as failures (program-policy option)

Design intent
-------------
- These scripts support governance; they do not replace it.
- Passing validation means the record is structurally sound and internally coherent.
- It does not mean the decision is correct, approved, or risk-free.
"""

import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]

DEFAULT_SCHEMA = ROOT / "decision-log" / "decision-log.schema.json"
DEFAULT_INSTANCE = ROOT / "examples" / "rgds-dec-0001.json"


def load_json(path: Path):
    """Load JSON from disk or exit with a clear error."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[ERROR] Failed to read JSON: {path}\n  {e}")
        sys.exit(2)


def format_path(err_path) -> str:
    """Format jsonschema error paths as a JSONPath-like string."""
    out = "$"
    for p in err_path:
        if isinstance(p, int):
            out += f"[{p}]"
        else:
            out += f".{p}"
    return out


def semantic_checks(instance: dict) -> tuple[list[str], list[str]]:
    """
    Semantic governance checks that JSON Schema cannot express.

    Returns:
        (errors, warnings)
        - errors: semantic invariants (fail CI / fail validation)
        - warnings: strong recommendations (non-fatal unless strict mode)

    NOTE: Keep this aligned with validate_all_examples.py to prevent drift.
    """
    errs: list[str] = []
    warns: list[str] = []

    decision_outcome = instance.get("decision_outcome", {}) or {}
    outcome = decision_outcome.get("outcome")

    conditions = decision_outcome.get("conditions") or []
    actions = instance.get("actions") or []
    gaps = (instance.get("known_gaps_and_assumptions", {}) or {}).get("gaps") or []

    # ---------------------------------------------------------------------
    # Outcome invariants
    # ---------------------------------------------------------------------

    # v1.0+ (core RGDS): conditional_go must have explicit conditions.
    if outcome == "conditional_go":
        if len(conditions) == 0:
            errs.append("conditional_go requires decision_outcome.conditions (at least 1)")

        # v1.0+ (recommended): conditions should be operationalized via actions.
        if len(actions) == 0:
            warns.append("conditional_go has no actions; consider adding actions to operationalize conditions")

    # v1.1+ (introduced defer_with_required_evidence): must include explicit gaps + re-entry mechanics.
    if outcome == "defer_with_required_evidence":
        if len(gaps) == 0:
            errs.append("defer_with_required_evidence requires known_gaps_and_assumptions.gaps (at least 1)")
        if len(conditions) == 0:
            errs.append("defer_with_required_evidence requires decision_outcome.conditions (at least 1)")
        if len(actions) == 0:
            errs.append("defer_with_required_evidence requires actions (at least 1)")

    # v1.0+ (recommended): defer should not be a content-free pause.
    if outcome == "defer":
        if len(gaps) == 0 and len(actions) == 0:
            warns.append("defer has no gaps or actions; consider recording re-entry criteria or follow-up actions")

    # ---------------------------------------------------------------------
    # Evidence completeness coherence
    # ---------------------------------------------------------------------

    # v1.4.0 (introduced evidence_completeness): incomplete evidence should be explicitly supported.
    ec = instance.get("evidence_completeness")
    if isinstance(ec, dict):
        state = ec.get("state")
        if state in ("partial", "placeholder"):
            # v1.4.0 (recommended): if evidence is incomplete, record gaps and/or author-at-risk items.
            author_at_risk_items = instance.get("author_at_risk_items") or []
            if len(gaps) == 0 and len(author_at_risk_items) == 0:
                warns.append(
                    "evidence_completeness is partial/placeholder, but no known gaps or author_at_risk_items recorded"
                )

            # v1.4.0 (recommended): placeholders benefit from an expected resolution date.
            if state == "placeholder" and not ec.get("expected_resolution_date"):
                warns.append("evidence_completeness.state=placeholder; consider setting expected_resolution_date")

    # ---------------------------------------------------------------------
    # Governance coherence (authority / escalation)
    # ---------------------------------------------------------------------

    # v1.4.0 (introduced governance.authority_scope + governance.escalation_path)
    gov = instance.get("governance", {}) or {}
    authority_scope = gov.get("authority_scope")
    escalation_path = gov.get("escalation_path") or []

    # v1.4.0+: if authority_scope is present, a decision_owner must exist (auditable authority).
    if authority_scope in ("recommend", "decide", "veto"):
        owner = gov.get("decision_owner")
        if not owner:
            errs.append("governance.authority_scope is present but governance.decision_owner is missing")

    # v1.4.0 (recommended): if escalation_path key exists, prefer at least one resolver.
    if "escalation_path" in gov and isinstance(escalation_path, list) and len(escalation_path) == 0:
        warns.append("governance.escalation_path is present but empty; consider specifying deadlock resolver(s)")

    # ---------------------------------------------------------------------
    # AI assistance disclosure integrity
    # ---------------------------------------------------------------------

    # v1.0+ (AI policy): AI use must be explicit and reviewable when used=true.
    ai = instance.get("ai_assistance", {}) or {}
    used = ai.get("used", False)

    if used:
        # v1.0+: required disclosure elements should be meaningful (not empty placeholders).
        use_cases = ai.get("use_cases") or []
        artifacts = ai.get("artifacts") or []
        controls = ai.get("controls") or {}

        if len(use_cases) == 0:
            errs.append("ai_assistance.used=true requires ai_assistance.use_cases (at least 1)")
        if len(artifacts) == 0:
            errs.append("ai_assistance.used=true requires ai_assistance.artifacts (at least 1)")

        # v1.0+ (recommended): controls fields should not be empty strings.
        for k in ("prompt_or_instruction_ref", "schema_or_format_constraints", "versioning", "safety_notes"):
            v = controls.get(k)
            if not isinstance(v, str) or not v.strip():
                warns.append(f"ai_assistance.controls.{k} is empty; consider adding a concrete reference")

        # v1.4.0 (optional trust signals): if confidence_band is set, consider recording override status.
        conf_band = ai.get("confidence_band")
        human_override = ai.get("human_override")
        if conf_band is not None and human_override is None:
            warns.append("ai_assistance.confidence_band is set but human_override is null; consider recording override status")

    else:
        # v1.0+ (recommended): avoid ambiguous disclosure where used=false but content exists.
        if ai.get("use_cases") or ai.get("artifacts"):
            warns.append(
                "ai_assistance.used=false but use_cases/artifacts are present; consider setting used=true or clearing fields"
            )

    return errs, warns


def main():
    """
    Usage:
        python3 scripts/validate_decision_log.py [schema.json] [instance.json] [--semantic] [--strict|--warn-as-error]

    Notes:
    - Without --semantic, this script validates schema only.
    - With --semantic, this script validates schema + semantic checks.
    - With --strict (or --warn-as-error), semantic warnings become failures.
    """
    semantic = "--semantic" in sys.argv
    strict = ("--strict" in sys.argv) or ("--warn-as-error" in sys.argv)

    args = [a for a in sys.argv[1:] if a not in ("--semantic", "--strict", "--warn-as-error")]

    schema_path = Path(args[0]).resolve() if len(args) > 0 else DEFAULT_SCHEMA
    instance_path = Path(args[1]).resolve() if len(args) > 1 else DEFAULT_INSTANCE

    if not schema_path.exists():
        print(f"[ERROR] Schema not found: {schema_path}")
        sys.exit(2)
    if not instance_path.exists():
        print(f"[ERROR] Instance not found: {instance_path}")
        sys.exit(2)

    schema = load_json(schema_path)
    instance = load_json(instance_path)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))

    if errors:
        print("[FAIL] Decision log does NOT conform to schema.")
        for e in errors:
            print(f" - {format_path(e.path)}: {e.message}")
        sys.exit(1)

    print("[PASS] Decision log conforms to schema (schema-only).")
    print(f"  Schema:   {schema_path}")
    print(f"  Instance: {instance_path}")

    if semantic:
        sem_errs, sem_warns = semantic_checks(instance)

        if sem_errs:
            print("\n[FAIL] Semantic invariants failed.")
            for msg in sem_errs:
                print(f" - {msg}")
            sys.exit(1)

        if sem_warns:
            if strict:
                print("\n[FAIL] Semantic recommendations treated as errors (--strict).")
                for msg in sem_warns:
                    print(f" - {msg}")
                sys.exit(1)

            print("\n[WARN] Semantic recommendations:")
            for msg in sem_warns:
                print(f" - {msg}")

        print("\n[PASS] Semantic invariants satisfied (with possible warnings).")

    sys.exit(0)


if __name__ == "__main__":
    main()
