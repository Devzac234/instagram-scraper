import json
import os
import sys

# Ensure src/ is on path so implicit namespace packages import.
HERE = os.path.dirname(__file__)
SRC = os.path.abspath(os.path.join(HERE, "..", "src"))
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from pipelines.validators import validate_profile_dict  # type: ignore

def test_sample_output_schema_keys():
    sample_path = os.path.join(HERE, "..", "data", "sample_output.json")
    with open(sample_path, "r", encoding="utf-8") as f:
        rows = json.load(f)
    assert isinstance(rows, list) and rows, "sample_output.json should contain at least one record"
    ok, errors = validate_profile_dict(rows[0])
    assert ok, f"sample output should validate, got errors: {errors}"