#!/usr/bin/env python3
"""
RGDS Validation Script — validate_decision_log.py

Purpose
-------
Validates a single RGDS decision log instance.

What it can validate
--------------------
1) Schema-only (default)
   - Ensures the JSON instance conforms to decision-log.schema.json

2) Schema + semantic checks (--semantic)
   - Enforces governance invariants that JSON Schema alone cannot express
   - Emits non-fatal warnings for strongly recommended patterns

3) Strict mode (--strict / --warn-as-error)
   - Treats semantic warnings as failures (program-policy option)
   - Auto-enables semantic checks (strict implies semantic)

Design intent
-------------
- These scripts support governance; they do not replace it.
- Passing validation means the record is structurally sound and internally coherent.
- It does not mean the decision is correct, approved, or risk-free.

Enhancements in this version
----------------------------
- argparse CLI with --schema / --instance and clear --help output
- Backward-compatible positional args still supported
- "Instance-first" single-arg convenience (if one *.json is supplied, treat it as instance)
- Optional JSON output (--format json) for CI / tooling
- Stable warning/error codes to support program policy and future "warn promotion"
- Strict mode works consistently: warnings become failures
- Version stamping (--version)

Exit codes
----------
0 — Pass (warnings allowed unless strict)
1 — Validation failure (schema/semantic failure; or warnings in strict mode)
2 — Script/configuration error (missing files, unreadable JSON, etc.)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

from jsonschema import Draft202012Validator

SCRIPT_VERSION = "1.0.0"  # script version (not RGDS schema version)

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "decision-log" / "decision-log.schema.json"
DEFAULT_INSTANCE = ROOT / "examples" / "rgds-dec-0001.json"


# -----------------------------
# Warning / Error Code Catalog
# -----------------------------
# Keep these stable once published.
E_COND_001 = "E-COND-001"
E_DEFERREQ_001 = "E-DEFERREQ-001"
E_GOV_001 = "E-GOV-001"
E_AI_001 = "E-AI-001"
E_AI_002 = "E-AI-002"

W_COND_001 = "W-COND-001"
W_DEFER_001 = "W-DEFER-001"
W_EVID_001 = "W-EVID-001"
W_EVID_002 = "W-EVID-002"
W_GOV_001 = "W-GOV-001"
W_AI_001 = "W-AI-001"
W_AI_002 = "W-AI-002"
W_AI_003 = "W-AI-003"


def load_json(path: Path) -> Any:
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


def schema_version(schema: Any) -> str | None:
    """
    Best-effort extraction of schema version.
    If you later add an explicit field, update this function.
    """
    if isinstance(schema, dict):
        # Common patterns (choose what exists in your repo)
        for key in ("version", "schema_version", "rgds_version"):
            v = schema.get(key)
            if isinstance(v, str) and v.strip():
                return v.strip()

        # Sometimes schema carries version in title/description; don't guess.
    return None


def _msg(code: str, text: str) -> str:
    return f"{code}: {text}"


def semantic_checks(instance: dict) -> Tuple[List[str], List[str]]:
    """
    Semantic governance checks that JSON Schema cannot express.

    Returns:
        (errors, warnings)
        - errors: semantic invariants (fail validation / fail CI)
        - warnings: strong recommendations (non-fatal unless strict)

    NOTE: Keep this aligned with validate_all_examples.py to prevent drift.
    """
    errs: List[str] = []
    warns: List[str] = []

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
            errs.append(_msg(E_COND_001, "conditional_go requires decision_outcome.conditions (at least 1)"))

        # v1.0+ (recommended): conditions should be operationalized via actions.
        if len(actions) == 0:
            warns.append(_msg(W_COND_001, "conditional_go has no actions; consider adding actions to operationalize conditions"))

    # v1.1+ (introduced defer_with_required_evidence): must include explicit gaps + re-entry mechanics.
    if outcome == "defer_with_required_evidence":
        if len(gaps) == 0:
            errs.append(_msg(E_DEFERREQ_001, "defer_with_required_evidence requires known_gaps_and_assumptions.gaps (at least 1)"))
        if len(conditions) == 0:
            errs.append(_msg(E_DEFERREQ_001, "defer_with_required_evidence requires decision_outcome.conditions (at least 1)"))
        if len(actions) == 0:
            errs.append(_msg(E_DEFERREQ_001, "defer_with_required_evidence requires actions (at least 1)"))

    # v1.0+ (recommended): defer should not be a content-free pause.
    if outcome == "defer":
        if len(gaps) == 0 and len(actions) == 0:
            warns.append(_msg(W_DEFER_001, "defer has no gaps or actions; consider recording re-entry criteria or follow-up actions"))

    
    # ---------------------------------------------------------------------
    # Options completeness
    # ---------------------------------------------------------------------

    options = instance.get("options_considered") or []
    if len(options) < 2:
        errs.append(_msg("E_OPT_001", "options_considered must include at least two options"))


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
                warns.append(_msg(W_EVID_001, "evidence_completeness is partial/placeholder, but no known gaps or author_at_risk_items recorded"))

            # v1.4.0 (recommended): placeholders benefit from an expected resolution date.
            if state == "placeholder" and not ec.get("expected_resolution_date"):
                warns.append(_msg(W_EVID_002, "evidence_completeness.state=placeholder; consider setting expected_resolution_date"))

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
            errs.append(_msg(E_GOV_001, "governance.authority_scope is present but governance.decision_owner is missing"))

    # v1.4.0 (recommended): if escalation_path key exists, prefer at least one resolver.
    if "escalation_path" in gov and isinstance(escalation_path, list) and len(escalation_path) == 0:
        warns.append(_msg(W_GOV_001, "governance.escalation_path is present but empty; consider specifying deadlock resolver(s)"))

    # ---------------------------------------------------------------------
    # AI assistance disclosure integrity
    # ---------------------------------------------------------------------

    # v1.0+ (AI policy): AI use must be explicit and reviewable when used=true.
    ai = instance.get("ai_assistance", {}) or {}
    used = ai.get("used", False)

    if used:
        use_cases = ai.get("use_cases") or []
        artifacts = ai.get("artifacts") or []
        controls = ai.get("controls") or {}

        if len(use_cases) == 0:
            errs.append(_msg(E_AI_001, "ai_assistance.used=true requires ai_assistance.use_cases (at least 1)"))

        # v2.0+ (whitepaper-aligned): require tool_name/tool_purpose and human_review when used=true
        tool_name = ai.get("tool_name") or ""
        tool_purpose = ai.get("tool_purpose") or ""
        human_review = ai.get("human_review") or []
        ai_risk = ai.get("ai_risk_assessment") or {}

        if tool_name.strip() == "":
            errs.append(_msg("E_AI_004", "ai_assistance.used=true requires ai_assistance.tool_name"))
        if tool_purpose.strip() == "":
            errs.append(_msg("E_AI_005", "ai_assistance.used=true requires ai_assistance.tool_purpose"))
        if len(human_review) == 0:
            errs.append(_msg("E_AI_006", "ai_assistance.used=true requires at least one human_review record"))
        if not isinstance(ai_risk, dict) or (ai_risk.get("confidence_band") in (None, "")):
            warns.append(_msg("W_AI_002", "ai_assistance.used=true should include ai_risk_assessment.confidence_band"))


        if len(artifacts) == 0:
            errs.append(_msg(E_AI_002, "ai_assistance.used=true requires ai_assistance.artifacts (at least 1)"))

        # v1.0+ (recommended): controls fields should not be empty strings.
        for k in ("prompt_or_instruction_ref", "schema_or_format_constraints", "versioning", "safety_notes"):
            v = controls.get(k)
            if not isinstance(v, str) or not v.strip():
                warns.append(_msg(W_AI_001, f"ai_assistance.controls.{k} is empty; consider adding a concrete reference"))

        # v1.4.0 (optional trust signals): if confidence_band is set, consider recording override status.
        conf_band = ai.get("confidence_band")
        human_override = ai.get("human_override")
        if conf_band is not None and human_override is None:
            warns.append(_msg(W_AI_002, "ai_assistance.confidence_band is set but human_override is null; consider recording override status"))

    else:
        # v1.0+ (recommended): avoid ambiguous disclosure where used=false but content exists.
        if ai.get("use_cases") or ai.get("artifacts"):
            warns.append(_msg(W_AI_003, "ai_assistance.used=false but use_cases/artifacts are present; consider setting used=true or clearing fields"))

    return errs, warns


def parse_args(argv: List[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="validate_decision_log.py",
        description="Validate a single RGDS decision log (schema + optional semantic governance checks).",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    p.add_argument(
        "positional",
        nargs="*",
        help=(
            "Backward-compatible positional args:\n"
            "  [schema.json] [instance.json]\n"
            "Convenience:\n"
            "  If exactly one *.json is provided positionally, it is treated as instance.json.\n"
            "Preferred:\n"
            "  Use --schema and --instance for clarity."
        ),
    )

    p.add_argument("--schema", dest="schema", type=str, default=None, help="Path to decision-log.schema.json")
    p.add_argument("--instance", dest="instance", type=str, default=None, help="Path to decision log instance JSON")

    p.add_argument("--semantic", action="store_true", help="Run semantic governance checks (in addition to schema).")
    p.add_argument("--strict", action="store_true", help="Treat semantic warnings as errors (implies --semantic).")
    p.add_argument("--warn-as-error", dest="warn_as_error", action="store_true", help="Alias for --strict.")

    p.add_argument(
        "--format",
        dest="out_format",
        choices=("text", "json"),
        default="text",
        help="Output format (text or json). Default: text",
    )

    p.add_argument("--version", action="store_true", help="Print script + schema version (if available) and exit.")
    return p.parse_args(argv)


def resolve_paths(args: argparse.Namespace) -> Tuple[Path, Path, bool, bool]:
    """
    Returns:
      (schema_path, instance_path, semantic, strict)
    """
    strict = args.strict or args.warn_as_error
    semantic = args.semantic or strict  # strict implies semantic

    schema_path: Path | None = Path(args.schema).resolve() if args.schema else None
    instance_path: Path | None = Path(args.instance).resolve() if args.instance else None

    # Backward-compatible positional behavior:
    # - If no flags provided, interpret positional as [schema] [instance]
    # - If exactly one positional *.json provided, treat as instance
    pos = [Path(x) for x in (args.positional or [])]

    if schema_path is None and instance_path is None and len(pos) == 1 and pos[0].suffix.lower() == ".json":
        # Most common human expectation: "validate_decision_log.py my_decision.json"
        schema_path = DEFAULT_SCHEMA
        instance_path = pos[0].resolve()

    else:
        if schema_path is None:
            schema_path = pos[0].resolve() if len(pos) > 0 else DEFAULT_SCHEMA
        if instance_path is None:
            instance_path = pos[1].resolve() if len(pos) > 1 else DEFAULT_INSTANCE

    return schema_path, instance_path, semantic, strict


def print_text_result(
    schema_path: Path,
    instance_path: Path,
    schema_ok: bool,
    schema_errors: List[str],
    sem_enabled: bool,
    sem_errors: List[str],
    sem_warnings: List[str],
    strict: bool,
):
    if not schema_ok:
        print("[FAIL] Decision log does NOT conform to schema.")
        for line in schema_errors:
            print(f" - {line}")
        print("\nLegend: PASS = schema + semantic invariants satisfied; WARN = recommendations (non-fatal unless strict).")
        return

    print("[PASS] Decision log conforms to schema (schema-only).")
    print(f"  Schema:   {schema_path}")
    print(f"  Instance: {instance_path}")

    if not sem_enabled:
        return

    if sem_errors:
        print("\n[FAIL] Semantic invariants failed.")
        for msg in sem_errors:
            print(f" - {msg}")
        print("\nLegend: PASS = schema + semantic invariants satisfied; WARN = recommendations (non-fatal unless strict).")
        return

    if sem_warnings:
        if strict:
            print("\n[FAIL] Semantic recommendations treated as errors (--strict/--warn-as-error).")
            for msg in sem_warnings:
                print(f" - {msg}")
            print("\nLegend: PASS = schema + semantic invariants satisfied; WARN = recommendations (non-fatal unless strict).")
            return

        print("\n[WARN] Semantic recommendations:")
        for msg in sem_warnings:
            print(f" - {msg}")

    print("\n[PASS] Semantic invariants satisfied (with possible warnings).")
    print("\nLegend: PASS = schema + semantic invariants satisfied; WARN = recommendations (non-fatal unless strict).")


def emit_json_result(
    schema_path: Path,
    instance_path: Path,
    schema_dict: Any,
    schema_ok: bool,
    schema_errors: List[Dict[str, Any]],
    sem_enabled: bool,
    sem_errors: List[Dict[str, Any]],
    sem_warnings: List[Dict[str, Any]],
    strict: bool,
) -> str:
    sv = schema_version(schema_dict)
    payload = {
        "script": {"name": "validate_decision_log.py", "version": SCRIPT_VERSION},
        "schema": {"path": str(schema_path), "version": sv},
        "instance": {"path": str(instance_path)},
        "modes": {"semantic": sem_enabled, "strict": strict},
        "result": {
            "schema_ok": schema_ok,
            "semantic_ok": (len(sem_errors) == 0) if sem_enabled and schema_ok else None,
            "warnings_as_errors": strict,
        },
        "schema_errors": schema_errors,
        "semantic_errors": sem_errors,
        "semantic_warnings": sem_warnings,
    }
    return json.dumps(payload, indent=2, sort_keys=False)


def to_coded_list(items: List[str]) -> List[Dict[str, Any]]:
    """
    Convert ["CODE: message", ...] to [{"code": "...", "message": "..."}, ...]
    If format does not match, code=None.
    """
    out: List[Dict[str, Any]] = []
    for s in items:
        if isinstance(s, str) and ":" in s:
            code, msg = s.split(":", 1)
            out.append({"code": code.strip(), "message": msg.strip()})
        else:
            out.append({"code": None, "message": str(s)})
    return out


def main(argv: List[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    schema_path, instance_path, semantic, strict = resolve_paths(args)

    if not schema_path.exists():
        print(f"[ERROR] Schema not found: {schema_path}")
        return 2
    if not instance_path.exists():
        print(f"[ERROR] Instance not found: {instance_path}")
        return 2

    schema_dict = load_json(schema_path)

    if args.version:
        sv = schema_version(schema_dict)
        print(f"validate_decision_log.py version: {SCRIPT_VERSION}")
        print(f"schema version: {sv if sv else '(not declared)'}")
        print(f"default schema: {DEFAULT_SCHEMA}")
        return 0

    instance = load_json(instance_path)

    validator = Draft202012Validator(schema_dict)
    schema_iter_errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))

    schema_ok = len(schema_iter_errors) == 0
    schema_errors_text: List[str] = []
    schema_errors_json: List[Dict[str, Any]] = []

    if not schema_ok:
        for e in schema_iter_errors:
            schema_errors_text.append(f"{format_path(e.path)}: {e.message}")
        schema_errors_json = [{"path": format_path(e.path), "message": e.message} for e in schema_iter_errors]

        if args.out_format == "json":
            print(
                emit_json_result(
                    schema_path=schema_path,
                    instance_path=instance_path,
                    schema_dict=schema_dict,
                    schema_ok=False,
                    schema_errors=schema_errors_json,
                    sem_enabled=semantic,
                    sem_errors=[],
                    sem_warnings=[],
                    strict=strict,
                )
            )
        else:
            print_text_result(
                schema_path=schema_path,
                instance_path=instance_path,
                schema_ok=False,
                schema_errors=schema_errors_text,
                sem_enabled=semantic,
                sem_errors=[],
                sem_warnings=[],
                strict=strict,
            )
        return 1

    sem_errs: List[str] = []
    sem_warns: List[str] = []

    if semantic:
        sem_errs, sem_warns = semantic_checks(instance)

    # Strict mode: warnings become failures.
    if semantic and strict and len(sem_warns) > 0:
        if args.out_format == "json":
            print(
                emit_json_result(
                    schema_path=schema_path,
                    instance_path=instance_path,
                    schema_dict=schema_dict,
                    schema_ok=True,
                    schema_errors=[],
                    sem_enabled=True,
                    sem_errors=to_coded_list(sem_errs),
                    sem_warnings=to_coded_list(sem_warns),
                    strict=True,
                )
            )
        else:
            print_text_result(
                schema_path=schema_path,
                instance_path=instance_path,
                schema_ok=True,
                schema_errors=[],
                sem_enabled=True,
                sem_errors=sem_errs,
                sem_warnings=sem_warns,
                strict=True,
            )
        return 1

    # Semantic hard errors fail.
    if semantic and len(sem_errs) > 0:
        if args.out_format == "json":
            print(
                emit_json_result(
                    schema_path=schema_path,
                    instance_path=instance_path,
                    schema_dict=schema_dict,
                    schema_ok=True,
                    schema_errors=[],
                    sem_enabled=True,
                    sem_errors=to_coded_list(sem_errs),
                    sem_warnings=to_coded_list(sem_warns),
                    strict=strict,
                )
            )
        else:
            print_text_result(
                schema_path=schema_path,
                instance_path=instance_path,
                schema_ok=True,
                schema_errors=[],
                sem_enabled=True,
                sem_errors=sem_errs,
                sem_warnings=sem_warns,
                strict=strict,
            )
        return 1

    # Pass (schema OK; semantic OK; warnings may exist if not strict)
    if args.out_format == "json":
        print(
            emit_json_result(
                schema_path=schema_path,
                instance_path=instance_path,
                schema_dict=schema_dict,
                schema_ok=True,
                schema_errors=[],
                sem_enabled=semantic,
                sem_errors=to_coded_list(sem_errs) if semantic else [],
                sem_warnings=to_coded_list(sem_warns) if semantic else [],
                strict=strict,
            )
        )
    else:
        print_text_result(
            schema_path=schema_path,
            instance_path=instance_path,
            schema_ok=True,
            schema_errors=[],
            sem_enabled=semantic,
            sem_errors=sem_errs,
            sem_warnings=sem_warns,
            strict=strict,
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
