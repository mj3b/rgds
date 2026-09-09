#!/usr/bin/env python3
"""
RGDS Validation Script — validate_all_examples.py

Purpose
-------
Validates all canonical RGDS decision examples against:
1) The JSON Schema (structural correctness)
2) Semantic governance invariants (decision discipline)

This script is intentionally conservative.
It blocks changes that would weaken decision defensibility.

What this script enforces
-------------------------
HARD FAILS (block CI):
- JSON Schema violations
- Missing required governance elements for certain decision outcomes
- Inconsistent AI disclosure when AI is marked as used

WARNINGS (do NOT block CI by default):
- Weak but allowed governance patterns
- Missing strongly recommended fields
- Situations that increase risk but may be intentional

Warnings are signals, not noise.
They are printed to force explicit consideration.

Strict mode (optional)
----------------------
If run with --strict (or --warn-as-error), warnings become failures.
This is a program-policy lever for higher-assurance environments.

Typical usage
-------------
    python3 scripts/validate_all_examples.py

Strict usage (program policy)
-----------------------------
    python3 scripts/validate_all_examples.py --strict

Exit codes
----------
0 — All examples pass (warnings allowed unless strict)
1 — Schema, semantic invariant, or (in strict mode) warning failure
2 — Script/configuration error (missing files, unreadable JSON)
"""

import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

if __package__:
    from .validate_decision_log import semantic_checks
else:
    from validate_decision_log import semantic_checks

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "decision-log" / "decision-log.schema.json"
EXAMPLES_DIR = ROOT / "examples"


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



def main():
    """
    Entry point.

    Validates every JSON file in /examples:
    - Schema validation first
    - Semantic validation second

    Output conventions:
    - [PASS]  — schema + semantic invariants satisfied
    - [WARN]  — governance recommendations (non-fatal unless --strict)
    - [FAIL]  — schema or semantic invariant violation (blocks CI)
    """
    strict = ("--strict" in sys.argv) or ("--warn-as-error" in sys.argv)

    if not SCHEMA_PATH.exists():
        print(f"[ERROR] Schema not found: {SCHEMA_PATH}")
        sys.exit(2)

    schema = load_json(SCHEMA_PATH)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

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

        # If strict, warnings are treated as failures
        if sem_warns and strict:
            failed = True
            print(f"\n[FAIL] {example.name} (warnings treated as errors --strict)")
            for msg in sem_warns:
                print(f"  - {msg}")
            continue

        print(f"[PASS] {example.name} (schema + semantic)")

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
    print("\nLegend: PASS = schema + semantic invariants satisfied; WARN = recommendations (non-fatal unless --strict).")
    sys.exit(0)


if __name__ == "__main__":
    main()
