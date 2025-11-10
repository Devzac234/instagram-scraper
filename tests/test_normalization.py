import os
import sys

HERE = os.path.dirname(__file__)
SRC = os.path.abspath(os.path.join(HERE, "..", "src"))
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from extractors.contacts_normalizer import extract_emails, extract_phones  # type: ignore
from extractors.profile_parser import parse_profile  # type: ignore
from pipelines.validators import validate_profile_dict  # type: ignore

def test_email_extraction_basic():
    text = "Reach us at hello@example.com or support@example.co.uk"
    emails = extract_emails(text)
    assert "hello@example.com" in emails
    assert "support@example.co.uk" in emails

def test_phone_extraction_basic():
    text = "Call +1 (202) 555-0199 or 0300-1234567 today!"
    phones = extract_phones(text)
    assert any("12025550199" in p or "03001234567" in p for p in phones)

def test_parse_profile_and_validate():
    prof = parse_profile("https://www.instagram.com/example_user")
    ok, errors = validate_profile_dict(prof)
    assert ok, f"Profile should validate, errors: {errors}"
    assert prof["username"] == "example_user"
    assert prof["URL"].endswith("/example_user")