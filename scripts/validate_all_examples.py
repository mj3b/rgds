#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "decision-log" / "decision-log.schema.json"
EXAMPLES_DIR = ROOT / "examples"


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[ERROR] Failed to read JSON: {path}\n  {e}")
        sys.exit(2)


def format_path(err_path) -> str:
    out = "$"
    for p in err_path:
        if isinstance(p, int):
            out += f"[{p}]"
        else:
            out += f".{p}"
    return out


def semantic_checks(instance: dict) -> tuple[list[str], list[str]]:
    """
    Returns (errors, warnings).
    - errors: fail CI (semantic invariants)
    - warnings: printed but do not fail CI (strong recommendations)
    """
    errs: list[str] = []
    warns: list[str] = []

    decision_outcome = instance.get("decision_outcome", {}) or {}
    outcome = decision_outcome.get("outcome")

    conditions = decision_outcome.get("conditions") or []
    actions = instance.get("actions") or []
    gaps = (instance.get("known_gaps_and_assumptions", {}) or {}).get("gaps") or []

    # --- Outcome invariants (hard fail) ---
    if outcome == "conditional_go":
        if len(conditions) == 0:
            errs.append("conditional_go requires decision_outcome.conditions (at least 1)")
        # Strongly recommended but not required by schema
        if len(actions) == 0:
            warns.append("conditional_go has no actions; consider adding actions to operationalize conditions")

    if outcome == "defer_with_required_evidence":
        if len(gaps) == 0:
            errs.append("defer_with_required_evidence requires known_gaps_and_assumptions.gaps (at least 1)")
        if len(conditions) == 0:
            errs.append("defer_with_required_evidence requires decision_outcome.conditions (at least 1)")
        if len(actions) == 0:
            errs.append("defer_with_required_evidence requires actions (at least 1)")

    if outcome == "defer":
        # Not a schema requirement, but helps prevent "content-free defer"
        if len(gaps) == 0 and len(actions) == 0:
            warns.append("defer has no gaps or actions; consider recording re-entry criteria or follow-up actions")

    # --- Evidence completeness coherence (v1.4.0) ---
    # Top-level evidence_completeness is optional; if present and partial/placeholder, it should be supported
    ec = instance.get("evidence_completeness")
    if isinstance(ec, dict):
        state = ec.get("state")
        if state in ("partial", "placeholder"):
            # If evidence is incomplete, strongly prefer gaps or author-at-risk signaling
            author_at_risk_items = instance.get("author_at_risk_items") or []
            if len(gaps) == 0 and len(author_at_risk_items) == 0:
                warns.append(
                    "evidence_completeness is partial/placeholder, but no known gaps or author_at_risk_items recorded"
                )
            # If placeholder, expected_resolution_date is strongly recommended
            if state == "placeholder" and not ec.get("expected_resolution_date"):
                warns.append("evidence_completeness.state=placeholder; consider setting expected_resolution_date")

    # --- Governance coherence (v1.4.0 authority/escalation) ---
    gov = instance.get("governance", {}) or {}
    authority_scope = gov.get("authority_scope")
    escalation_path = gov.get("escalation_path") or []

    # Schema already validates enum/defaults; semantic checks focus on "non-empty when used"
    if authority_scope in ("recommend", "decide", "veto"):
        owner = gov.get("decision_owner")
        if not owner:
            errs.append("governance.authority_scope is present but governance.decision_owner is missing")

    # Escalation path is optional, but if present should contain at least one person_ref
    # (Your schema allows empty array by default; treat as warning, not error)
    if "escalation_path" in gov and isinstance(escalation_path, list) and len(escalation_path) == 0:
        warns.append("governance.escalation_path is present but empty; consider specifying deadlock resolver(s)")

    # --- AI assistance disclosure integrity ---
    ai = instance.get("ai_assistance", {}) or {}
    used = ai.get("used", False)

    if used:
        use_cases = ai.get("use_cases") or []
        artifacts = ai.get("artifacts") or []
        controls = ai.get("controls") or {}

        # These are required by schema, but semantic checks improve diagnostics and catch empty content
        if len(use_cases) == 0:
            errs.append("ai_assistance.used=true requires ai_assistance.use_cases (at least 1)")
        if len(artifacts) == 0:
            errs.append("ai_assistance.used=true requires ai_assistance.artifacts (at least 1)")
        # Controls required fields exist by schema; check for non-empty strings to avoid hollow compliance
        for k in ("prompt_or_instruction_ref", "schema_or_format_constraints", "versioning", "safety_notes"):
            v = controls.get(k)
            if not isinstance(v, str) or not v.strip():
                warns.append(f"ai_assistance.controls.{k} is empty; consider adding a concrete reference")

        # Optional trust signals: schema validates types/enums; semantic checks ensure they make sense together
        conf_band = ai.get("confidence_band")
        human_override = ai.get("human_override")
        if conf_band is not None and human_override is None:
            warns.append("ai_assistance.confidence_band is set but human_override is null; consider recording override status")

    else:
        # If not used, but fields are populated, warn about inconsistency
        if ai.get("use_cases") or ai.get("artifacts"):
            warns.append("ai_assistance.used=false but use_cases/artifacts are present; consider setting used=true or clearing fields")

    return errs, warns


def main():
    if not SCHEMA_PATH.exists():
        print(f"[ERROR] Schema not found: {SCHEMA_PATH}")
        sys.exit(2)

    schema = load_json(SCHEMA_PATH)
    validator = Draft202012Validator(schema)

    examples = sorted(EXAMPLES_DIR.glob("*.json"))
    if not examples:
        print("[ERROR] No example JSON files found.")
        sys.exit(2)

    failed = False
    warned_any = False

    for example in examples:
        instance = load_json(example)
        errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))

        if errors:
            failed = True
            print(f"\n[FAIL] {example.name}")
            for e in errors:
                print(f"  - {format_path(e.path)}: {e.message}")
            continue

        sem_errs, sem_warns = semantic_checks(instance)

        if sem_errs:
            failed = True
            print(f"\n[FAIL] {example.name} (semantic)")
            for msg in sem_errs:
                print(f"  - {msg}")
            continue

        print(f"[PASS] {example.name}")

        if sem_warns:
            warned_any = True
            print(f"[WARN] {example.name}")
            for msg in sem_warns:
                print(f"  - {msg}")

    if failed:
        sys.exit(1)

    if warned_any:
        print("\nAll example decision logs conform to schema and semantic invariants (with warnings).")
    else:
        print("\nAll example decision logs conform to schema and semantic invariants.")
    sys.exit(0)


if __name__ == "__main__":
    main()
