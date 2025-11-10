import hashlib
import logging
import re
from datetime import datetime, timedelta, timezone
from typing import Dict, Tuple

from .contacts_normalizer import extract_emails, extract_phones

log = logging.getLogger(__name__)

PROFILE_URL_RE = re.compile(r"(?:https?://)?(?:www\.)?instagram\.com/([A-Za-z0-9._]+)", re.IGNORECASE)

def _canonicalize_username_or_url(s: str) -> Tuple[str, str]:
    """
    Returns (username, url)
    """
    s = s.strip()
    m = PROFILE_URL_RE.search(s)
    if m:
        username = m.group(1).strip(".")
    else:
        username = s.lstrip("@")
    url = f"https://www.instagram.com/{username}"
    return username, url

def _deterministic_int(seed: str, min_val: int, max_val: int) -> int:
    """Deterministically map seed to an integer in [min_val, max_val]."""
    h = hashlib.sha256(seed.encode("utf-8")).hexdigest()
    n = int(h[:12], 16)
    return min_val + (n % (max_val - min_val + 1))

def _deterministic_bool(seed: str, salt: str) -> bool:
    h = hashlib.sha256((seed + salt).encode("utf-8")).hexdigest()
    return int(h[-1], 16) % 2 == 0

def parse_profile(username_or_url: str) -> Dict:
    """
    Offline-friendly deterministic profile parser that mocks a realistic schema.
    It pulls contact signals from the input string (if present).
    """
    username, url = _canonicalize_username_or_url(username_or_url)

    # Derive deterministic attributes
    insta_id = str(_deterministic_int(username, 10_000_000, 9_999_999_999))
    followers = _deterministic_int(username + "#f", 100, 1_000_000)
    followings = _deterministic_int(username + "#g", 10, 5_000)
    is_private = _deterministic_bool(username, "private")
    is_business = _deterministic_bool(username, "biz")
    is_professional = is_business or _deterministic_bool(username, "pro")
    is_verified = _deterministic_bool(username, "verified")
    highlight_reel_count = _deterministic_int(username + "#hr", 0, 20)
    pinned_channels_list_count = _deterministic_int(username + "#pc", 0, 3)
    has_channel = _deterministic_bool(username, "channel")
    has_clips = _deterministic_bool(username, "clips")
    has_guides = _deterministic_bool(username, "guides")
    joined_recently = _deterministic_bool(username, "jr")

    # Last post time: spread within ~2 years
    days_ago = _deterministic_int(username + "#lp", 0, 730)
    last_post_dt = datetime.now(timezone.utc) - timedelta(days=days_ago)
    last_post_date = last_post_dt.strftime("%Y-%m-%d %H:%M:%S")

    biography = f"Hi, this is @{username}. Contact: {username}@example.com | +1-202-555-01{str(followers % 90).zfill(2)}"
    ext_url = f"https://{username}.example.com"
    prof_pic = f"https://cdn.example.com/ig/{username}/profile.jpg"
    full_name = username.replace(".", " ").title()
    category_enum = "CONTENT_CREATOR" if followers > 1000 else "PERSONAL"
    category_name = "Content Creator" if category_enum == "CONTENT_CREATOR" else "Personal"

    # Extract contact signals from synthesized bio and ext url
    emails = extract_emails(biography + " " + ext_url)
    phones = extract_phones(biography)

    business_email = emails[0] if emails else None
    business_phone_number = phones[0] if phones else None

    profile = {
        "insta_id": insta_id,
        "URL": url,
        "profile_pic_url": prof_pic,
        "username": username,
        "full_name": full_name,
        "external_url": ext_url,
        "city_name": None,
        "ExtractedEmails": ",".join(emails) if emails else "",
        "ExtractedPhones": ",".join(phones) if phones else "",
        "biography": biography,
        "category_name": category_name,
        "category_enum": category_enum,
        "followers": followers,
        "followings": followings,
        "facebook_id": None,
        "facebook_link": None,
        "highlight_reel_count": highlight_reel_count,
        "has_channel": has_channel,
        "is_business_account": is_business,
        "is_professional_account": is_professional,
        "business_address_json": '{"city_name": null, "city_id": null, "latitude": null, "longitude": null, "street_address": null, "zip_code": null}',
        "business_contact_method": "UNKNOWN",
        "business_email": business_email,
        "business_phone_number": business_phone_number,
        "related_profiles": [f"{username}_friend1", f"{username}_friend2"],
        "connected_fb_page": None,
        "last_post_date": last_post_date,
        # flags
        "has_blocked_viewer": False,
        "has_clips": has_clips,
        "has_guides": has_guides,
        "has_onboarded_to_text_post_app": False,
        "has_requested_viewer": False,
        "hide_like_and_view_counts": False,
        "is_embeds_disabled": False,
        "is_guardian_of_viewer": False,
        "is_joined_recently": joined_recently,
        "is_private": is_private,
        "is_regulated_c18": False,
        "is_supervised_by_viewer": False,
        "is_supervised_user": False,
        "is_supervision_enabled": False,
        "is_verified": is_verified,
        "is_verified_by_mv4b": False,
        "pinned_channels_list_count": pinned_channels_list_count,
        "remove_message_entrypoint": False,
        "requested_by_viewer": False,
        "restricted_by_viewer": None,
        "should_show_category": True,
        "should_show_public_contacts": True,
        "show_account_transparency_details": False,
        # media stubs (one deterministic post)
        "timeline_media": [
            {
                "node": {
                    "__typename": "GraphImage",
                    "id": str(_deterministic_int(username + "#post", 10_000_000_000, 99_999_999_999)),
                    "shortcode": f"{username[:10]}Short",
                    "dimensions": {"height": 1080, "width": 1080},
                    "display_url": f"https://cdn.example.com/ig/{username}/last_post.jpg",
                    "edge_media_to_caption": {"edges": [{"node": {"text": f"Hello from @{username}!"}}]},
                    "edge_media_to_comment": {"count": _deterministic_int(username + "#c", 0, 5000)},
                    "comments_disabled": False,
                    "taken_at_timestamp": int(last_post_dt.timestamp()),
                    "edge_liked_by": {"count": _deterministic_int(username + "#l", 0, 50000)},
                    "is_video": False,
                    "owner": {"id": insta_id, "username": username},
                }
            }
        ],
        "tagged_profiles": [f"{username}_friend1", f"{username}_friend2"],
    }
    return profile