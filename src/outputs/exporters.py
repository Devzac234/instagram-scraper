import csv
import json
from typing import Dict, Iterable, List

def write_json(path: str, rows: List[Dict]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)

def write_jsonl(path: str, rows: Iterable[Dict]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

def write_csv(path: str, rows: List[Dict]) -> None:
    if not rows:
        with open(path, "w", newline="", encoding="utf-8") as f:
            f.write("")  # empty csv
        return
    # Flatten nested structures conservatively
    normalized: List[Dict] = []
    for r in rows:
        rr = r.copy()
        if isinstance(rr.get("facebook_link"), dict):
            rr["facebook_link_url"] = rr["facebook_link"].get("url")
            rr["facebook_link_name"] = rr["facebook_link"].get("name")
            del rr["facebook_link"]
        # keep only a summary for timeline_media
        if "timeline_media" in rr:
            rr["timeline_media_count"] = len(rr["timeline_media"]) if isinstance(rr["timeline_media"], list) else 0
            del rr["timeline_media"]
        normalized.append(rr)
    fieldnames = sorted({k for r in normalized for k in r.keys()})
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in normalized:
            writer.writerow(r)