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

    if failed:
        sys.exit(1)

    print("\nAll example decision logs conform to schema.")
    sys.exit(0)

if __name__ == "__main__":
    main()
