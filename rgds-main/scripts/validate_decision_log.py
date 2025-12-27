#!/usr/bin/env python3
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]

DEFAULT_SCHEMA = ROOT / "decision-log" / "decision-log.schema.json"
DEFAULT_INSTANCE = ROOT / "examples" / "rgds-dec-0001.json"

def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[ERROR] Failed to read JSON: {path}\n  {e}")
        sys.exit(2)

def main():
    schema_path = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT_SCHEMA
    instance_path = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else DEFAULT_INSTANCE

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
            path = "$" + "".join([f"[{repr(p)}]" if isinstance(p, int) else f".{p}" for p in e.path])
            print(f" - {path}: {e.message}")
        sys.exit(1)

    print("[PASS] Decision log conforms to schema.")
    print(f"  Schema:   {schema_path}")
    print(f"  Instance: {instance_path}")
    sys.exit(0)

if __name__ == "__main__":
    main()
