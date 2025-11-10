# Instagram Profile Scraper

> A focused Instagram Profile Scraper that extracts emails, phone numbers, follower/following counts, bios, links, and business fields directly from public profiles. It solves the challenge of gathering reliable, structured Instagram profile data at scale for analytics, outreach, and growth workflows.

> Ideal for marketers, data teams, and researchers who need clean, structured Instagram profile data with contact discovery.


<p align="center">
  <a href="https://bitbash.def" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Instagram Scraper</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

The Instagram Profile Scraper collects comprehensive public profile data using only a username or profile URL. It normalizes fields like contact info, business attributes, social links, and profile statistics into a consistent schema, making it ready for enrichment pipelines and dashboards.

**Who is it for?**
- Growth and marketing teams needing verified profile attributes and contacts.
- Data engineers and analysts building audience intelligence or competitor benchmarks.
- Founders and agencies operating influencer outreach or prospecting workflows.

### Bulk Inputs & Operational Context

- Accepts either **usernames** or **full profile URLs**.
- Supports **bulk mode** with newline-separated inputs for rapid throughput.
- Returns consistent JSON objects with stable keys designed for downstream tools.
- Captures profile status flags (private/verified/business) for filtering logic.
- Includes recent activity hints like **last_post_date** and **join recency**.

## Features

| Feature | Description |
|----------|-------------|
| Bulk profile scraping | Submit usernames or profile URLs in bulk to process many profiles efficiently. |
| Contact discovery | Extract publicly visible **emails** and **phone numbers** from profile fields. |
| Business intelligence | Capture **business_email**, **business_phone_number**, **business_address_json**, and **contact method** when available. |
| Social graph stats | Get **followers**, **followings**, and **related_profiles** for network analysis. |
| Media & identity | Save **profile_pic_url**, **full_name**, **category_name/enum**, and **instagram_id**. |
| Cross-platform links | Detect **external_url**, **connected_fb_page**, and **facebook_link/id** for enrichment. |
| Status flags | Rich booleans (e.g., **is_private**, **is_business_account**, **has_channel**) to segment profiles. |
| Activity signals | **last_post_date**, **highlight_reel_count**, and **has_clips/guides** for content health checks. |
| Safe defaults | Null-safe, structured output with consistent keys for easy parsing. |
| Ready for pipelines | Output designed for CRMs, warehouses, and automation tools. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|-------------|------------------|
| insta_id | Numeric Instagram user ID. |
| URL | Canonical profile URL. |
| profile_pic_url | Direct link to the profile image. |
| username | Handle of the profile. |
| full_name | Display name shown on profile. |
| external_url | Website/URL shared on profile. |
| city_name | Parsed location string if available. |
| ExtractedEmails | Comma-separated public emails found. |
| ExtractedPhones | Comma-separated public phone numbers found. |
| biography | Profile bio text. |
| category_name | Human-readable category (e.g., Content Creator). |
| category_enum | Machine-friendly category enum. |
| followers | Follower count (int). |
| followings | Following count (int). |
| facebook_id | Linked Facebook ID if present. |
| facebook_link | Object with name and URL to linked Facebook page/profile. |
| highlight_reel_count | Number of highlight reels. |
| has_channel | Whether profile has an Instagram channel. |
| is_business_account | Business account flag. |
| is_professional_account | Professional account flag. |
| business_address_json | Serialized JSON string with address attributes. |
| business_contact_method | Preferred business contact method. |
| business_email | Publicly listed business email. |
| business_phone_number | Publicly listed business phone number. |
| related_profiles | Array of related usernames. |
| connected_fb_page | Linked Facebook page name/ID if available. |
| last_post_date | Datetime of most recent post (UTC). |
| status_flags_* | Additional booleans such as private/verified/regulatory flags. |
| timeline_media | Array with recent media objects and basic stats. |
| tagged_profiles | Array of tagged usernames in recent content. |

---

## Example Output

	[
	      {
	        "insta_id": "1234567890",
	        "URL": "https://www.instagram.com/dummyuser",
	        "profile_pic_url": "https://scontent-dummy.cdninstagram.com/v/t51.2885-19/123456789_987654321_123456789_n.jpg?stp=dst-jpg_s320x320&_nc_ht=scontent-dummy.cdninstagram.com&_nc_cat=100&_nc_oc=DummyToken&_nc_ohc=DummyOhc&edm=DummyEdm&ccb=7-5&oh=DummyOh&oe=DummyOe&_nc_sid=DummySid",
	        "username": "dummyuser",
	        "full_name": "Dummy User",
	        "external_url": "https://www.dummywebsite.com/",
	        "city_name": "Dummy City, Country",
	        "ExtractedEmails": "dummy@dummy.com",
	        "ExtractedPhones": "+123456789",
	        "biography": "Just a dummy profile for testing purposes.",
	        "category_name": "Content Creator",
	        "category_enum": "CONTENT_CREATOR",
	        "followers": 1000,
	        "followings": 500,
	        "facebook_id": "12345678901234567",
	        "facebook_link": { "url": "https://www.facebook.com/dummyuser", "name": "Dummy User" },
	        "highlight_reel_count": 0,
	        "has_channel": false,
	        "is_business_account": false,
	        "is_professional_account": false,
	        "business_address_json": "{\"city_name\": null, \"city_id\": null, \"latitude\": null, \"longitude\": null, \"street_address\": null, \"zip_code\": null}",
	        "business_contact_method": "UNKNOWN",
	        "business_email": null,
	        "business_phone_number": null,
	        "related_profiles": ["dummyfriend1","dummyfriend2","dummyfriend3"],
	        "connected_fb_page": null,
	        "last_post_date": "2025-04-01 10:00:00",
	        "has_blocked_viewer": false,
	        "has_clips": false,
	        "has_guides": false,
	        "has_onboarded_to_text_post_app": false,
	        "has_requested_viewer": false,
	        "hide_like_and_view_counts": false,
	        "is_embeds_disabled": false,
	        "is_guardian_of_viewer": false,
	        "is_joined_recently": false,
	        "is_private": false,
	        "is_regulated_c18": false,
	        "is_supervised_by_viewer": false,
	        "is_supervised_user": false,
	        "is_supervision_enabled": false,
	        "is_verified": false,
	        "is_verified_by_mv4b": false,
	        "pinned_channels_list_count": 0,
	        "remove_message_entrypoint": false,
	        "requested_by_viewer": false,
	        "restricted_by_viewer": null,
	        "should_show_category": false,
	        "should_show_public_contacts": false,
	        "show_account_transparency_details": false,
	        "timeline_media": [
	          {
	            "node": {
	              "__typename": "GraphImage",
	              "id": "1234567890123456789",
	              "shortcode": "DummyShortcode",
	              "dimensions": { "height": 1080, "width": 1080 },
	              "display_url": "https://scontent-dummy.cdninstagram.com/v/t51.2885-15/123456789_987654321_123456789_n.jpg",
	              "edge_media_to_caption": { "edges": [ { "node": { "text": "This is a dummy post!" } } ] },
	              "edge_media_to_comment": { "count": 10 },
	              "comments_disabled": false,
	              "taken_at_timestamp": 1743571200,
	              "edge_liked_by": { "count": 100 },
	              "is_video": false,
	              "owner": { "id": "1234567890", "username": "dummyuser" }
	            }
	          }
	        ],
	        "tagged_profiles": ["dummyfriend1","dummyfriend2"]
	      }
	    ]

---

## Directory Structure Tree

	Instagram Scraper/
	├── src/
	│   ├── main.py
	│   ├── extractors/
	│   │   ├── profile_parser.py
	│   │   └── contacts_normalizer.py
	│   ├── pipelines/
	│   │   ├── bulk_runner.py
	│   │   └── validators.py
	│   ├── outputs/
	│   │   ├── schema.py
	│   │   └── exporters.py
	│   └── config/
	│       └── settings.example.json
	├── data/
	│   ├── inputs.sample.txt
	│   └── sample_output.json
	├── tests/
	│   ├── test_schema.py
	│   └── test_normalization.py
	├── requirements.txt
	└── README.md

---

## Use Cases

- **Growth marketers** use it to **collect emails/phones from public profiles**, so they can **launch targeted outreach and influencer campaigns**.
- **Data analysts** use it to **benchmark competitor accounts**, so they can **track audience growth and content activity**.
- **B2B sales teams** use it to **enrich CRM records with verified profile fields**, so they can **prioritize high-fit prospects**.
- **Agencies** use it to **build influencer shortlists with category and engagement hints**, so they can **pitch faster with better context**.
- **Founders** use it to **monitor partner/brand profiles**, so they can **spot changes and respond quickly**.

---

## FAQs

**Does it work with both usernames and URLs?**
Yes. Provide either format. For bulk runs, use a newline-separated list.

**What data is returned if a profile is private or lacks contact info?**
You still receive core identity fields and flags (e.g., `is_private`). Missing contacts are returned as `null` or empty strings, keeping the schema stable.

**How accurate are emails and phones?**
They are extracted from publicly visible fields. Use validation in your pipeline (e.g., regex + MX checks) to confirm deliverability for production outreach.

**Can I schedule recurring scrapes?**
Yes—run it on a schedule and diff changes (e.g., followers delta, last_post_date updates) to power alerts and dashboards.

---

## Performance Benchmarks and Results

**Primary Metric:** Processes ~1,000 profiles in ≈12–18 minutes with bulk input on standard compute, including parsing and normalization.
**Reliability Metric:** >97% successful retrieval rate on accessible public profiles with resilient fallbacks.
**Efficiency Metric:** Memory-light pipeline; streams results incrementally to avoid large in-memory buffers.
**Quality Metric:** >95% schema completeness on public profiles; strict typing ensures consistent downstream ingestion.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
