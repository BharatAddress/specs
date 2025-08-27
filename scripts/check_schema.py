#!/usr/bin/env python3
import json
from pathlib import Path
from jsonschema import Draft202012Validator


def main():
    schema_path = Path(__file__).parent.parent / "address-register.schema.json"
    schema = json.loads(schema_path.read_text())
    # Validate meta-syntax
    Draft202012Validator.check_schema(schema)
    print("Schema syntax OK (Draft 2020-12)")


if __name__ == "__main__":
    main()

