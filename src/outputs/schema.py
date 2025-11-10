from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional

@dataclass
class FacebookLink:
    url: Optional[str] = None
    name: Optional[str] = None

@dataclass
class TimelineMediaNode:
    __typename: str
    id: str
    shortcode: str
    dimensions: Dict[str, int]
    display_url: str
    edge_media_to_caption: Dict[str, Any]
    edge_media_to_comment: Dict[str, Any]
    comments_disabled: bool
    taken_at_timestamp: int
    edge_liked_by: Dict[str, Any]
    is_video: bool
    owner: Dict[str, Any]

@dataclass
class Profile:
    insta_id: str
    URL: str
    profile_pic_url: Optional[str]
    username: str
    full_name: Optional[str]
    external_url: Optional[str]
    city_name: Optional[str]
    ExtractedEmails: str
    ExtractedPhones: str
    biography: Optional[str]
    category_name: Optional[str]
    category_enum: Optional[str]
    followers: int
    followings: int
    facebook_id: Optional[str]
    facebook_link: Optional[FacebookLink]
    highlight_reel_count: int
    has_channel: bool
    is_business_account: bool
    is_professional_account: bool
    business_address_json: str
    business_contact_method: Optional[str]
    business_email: Optional[str]
    business_phone_number: Optional[str]
    related_profiles: List[str] = field(default_factory=list)
    connected_fb_page: Optional[str] = None
    last_post_date: Optional[str] = None
    # status flags
    has_blocked_viewer: bool = False
    has_clips: bool = False
    has_guides: bool = False
    has_onboarded_to_text_post_app: bool = False
    has_requested_viewer: bool = False
    hide_like_and_view_counts: bool = False
    is_embeds_disabled: bool = False
    is_guardian_of_viewer: bool = False
    is_joined_recently: bool = False
    is_private: bool = False
    is_regulated_c18: bool = False
    is_supervised_by_viewer: bool = False
    is_supervised_user: bool = False
    is_supervision_enabled: bool = False
    is_verified: bool = False
    is_verified_by_mv4b: bool = False
    pinned_channels_list_count: int = 0
    remove_message_entrypoint: bool = False
    requested_by_viewer: bool = False
    restricted_by_viewer: Optional[bool] = None
    should_show_category: bool = True
    should_show_public_contacts: bool = True
    show_account_transparency_details: bool = False
    timeline_media: List[Dict[str, Any]] = field(default_factory=list)
    tagged_profiles: List[str] = field(default_factory=list)

def to_dict(profile: "Profile") -> Dict[str, Any]:
    """
    Convert Profile dataclass (with nested dataclasses) to a plain dict.
    """
    d = asdict(profile)
    if isinstance(d.get("facebook_link"), dict):
        # Already flattened by asdict
        pass
    return d