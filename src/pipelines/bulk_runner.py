import logging
from typing import Dict, Iterable, List

from extractors.profile_parser import parse_profile
from pipelines.validators import validate_profile_dict

log = logging.getLogger(__name__)

class BulkRunner:
    """
    Orchestrates parsing and validation for a list of usernames/URLs.
    """

    def __init__(self, settings: Dict | None = None) -> None:
        self.settings = settings or {}
        self.fail_fast = bool(self.settings.get("fail_fast", False))

    def run_bulk(self, inputs: Iterable[str]) -> List[Dict]:
        results: List[Dict] = []
        for idx, raw in enumerate(inputs, start=1):
            try:
                prof = parse_profile(raw)
                ok, errors = validate_profile_dict(prof)
                if not ok:
                    if self.fail_fast:
                        raise ValueError(f"Validation errors: {errors}")
                    log.warning("Validation warnings for %s: %s", raw, errors)
                results.append(prof)
            except Exception as e:
                log.exception("Failed to process input #%d '%s': %s", idx, raw, e)
                if self.fail_fast:
                    raise
        return results