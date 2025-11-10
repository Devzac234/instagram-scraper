import re
from typing import Dict, List, Tuple

EMAIL_SIMPLE = re.compile(r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$")

REQUIRED_KEYS = [
    "insta_id",
    "URL",
    "username",
    "followers",
    "followings",
    "last_post_date",
    "timeline_media",
]

def validate_profile_dict(profile: Dict) -> Tuple[bool, List[str]]:
    errors: List[str] = []

    for k in REQUIRED_KEYS:
        if k not in profile:
            errors.append(f"missing:{k}")

    if "business_email" in profile and profile["business_email"]:
        if not EMAIL_SIMPLE.match(profile["business_email"]):
            errors.append("invalid:business_email")

    if "ExtractedEmails" in profile and profile["ExtractedEmails"]:
        for e in str(profile["ExtractedEmails"]).split(","):
            e = e.strip()
            if e and not EMAIL_SIMPLE.match(e):
                errors.append(f"invalid:ExtractedEmails:{e}")

    # sanity on counts
    for k in ("followers", "followings", "highlight_reel_count"):
        if k in profile and (not isinstance(profile[k], int) or profile[k] < 0):
            errors.append(f"invalid_int:{k}")

    ok = len(errors) == 0
    return ok, errors