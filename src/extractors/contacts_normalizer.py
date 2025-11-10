import re
from typing import List

EMAIL_RE = re.compile(
    r"(?:mailto:)?([A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,})",
    re.IGNORECASE,
)

# International-ish phone finder; focuses on +country and common national forms.
PHONE_RE = re.compile(
    r"(?:(?:\+?\d{1,3}[\s\-\.]?)?(?:\(?\d{2,4}\)?[\s\-\.]?)\d{3,4}[\s\-\.]?\d{3,4})"
)

def extract_emails(text: str) -> List[str]:
    if not text:
        return []
    found = [m.group(1) if m.lastindex else m.group(0) for m in EMAIL_RE.finditer(text)]
    # Deduplicate while preserving order
    seen = set()
    out = []
    for e in found:
        e = e.strip().strip(",.;")
        if e not in seen:
            seen.add(e)
            out.append(e)
    return out

def extract_phones(text: str) -> List[str]:
    if not text:
        return []
    found = []
    for m in PHONE_RE.finditer(text):
        num = re.sub(r"[^\d+]", "", m.group(0))
        if len(num) >= 7:
            found.append(num)
    # Deduplicate
    seen = set()
    out = []
    for p in found:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out