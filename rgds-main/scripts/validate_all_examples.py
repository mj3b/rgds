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


def semantic_errors(instance: dict) -> list[str]:
    errs: list[str] = []
    outcome = instance.get("decision_outcome", {}).get("outcome")

    # Evidence items should always carry confidence + quality notes for auditability
    for i, ev in enumerate(instance.get("evidence", {}).get("evidence_items", [])):
        if not ev.get("confidence"):
            errs.append(f"evidence.evidence_items[{i}].confidence is missing/empty")
        if not ev.get("quality_notes"):
            errs.append(f"evidence.evidence_items[{i}].quality_notes is missing/empty")

    conditions = instance.get("decision_outcome", {}).get("conditions") or []
    actions = instance.get("actions") or []
    gaps = instance.get("known_gaps_and_assumptions", {}).get("gaps") or []

    if outcome in ("conditional_go",):
        if len(conditions) == 0:
            errs.append("conditional_go requires decision_outcome.conditions (at least 1)")
    if outcome in ("defer_with_required_evidence",):
        if len(gaps) == 0:
            errs.append("defer_with_required_evidence requires known_gaps_and_assumptions.gaps (at least 1)")
        if len(conditions) == 0:
            errs.append("defer_with_required_evidence requires decision_outcome.conditions (at least 1)")
        if len(actions) == 0:
            errs.append("defer_with_required_evidence requires actions (at least 1)")

    return errs

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

    for example in examples:
        instance = load_json(example)
        errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))

        if errors:
            failed = True
            print(f"\n[FAIL] {example.name}")
            for e in errors:
                path = "$" + "".join(
                    [f"[{repr(p)}]" if isinstance(p, int) else f".{p}" for p in e.path]
                )
                print(f"  - {path}: {e.message}")
        else:
            print(f"[PASS] {example.name}")
            sem_errs = semantic_errors(instance)
            if sem_errs:
                failed = True
                print(f"\n[FAIL] {example.name} (semantic)")
                for msg in sem_errs:
                    print(f"  - {msg}")

    if failed:
        sys.exit(1)

    print("\nAll example decision logs conform to schema.")
    sys.exit(0)

if __name__ == "__main__":
    main()