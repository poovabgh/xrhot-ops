#!/usr/bin/env python3
"""Extract per-handle max tweet guid from feeds for cheap since_id checks."""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def max_by_creator(feed: Path) -> dict[str, str]:
    text = feed.read_text(encoding="utf-8")
    items = re.findall(r"<item>(.*?)</item>", text, re.S)
    by: dict[str, list[str]] = defaultdict(list)
    for it in items:
        g = re.search(r"<guid[^>]*>(\d+)</guid>", it)
        c = re.search(r"<dc:creator>([^<]+)</dc:creator>", it)
        if g and c:
            by[c.group(1)].append(g.group(1))
    return {h: max(ids, key=int) for h, ids in by.items()}


def main() -> None:
    official = max_by_creator(ROOT / "feeds" / "x-official.xml")
    media = max_by_creator(ROOT / "feeds" / "x-media-kol.xml")
    all_guids = set()
    for feed in (ROOT / "feeds" / "x-official.xml", ROOT / "feeds" / "x-media-kol.xml"):
        all_guids.update(re.findall(r"<guid[^>]*>(\d+)</guid>", feed.read_text(encoding="utf-8")))
    out = {
        "official_max_guid_by_handle": official,
        "media_kol_max_guid_by_handle": media,
        "all_guids_count": len(all_guids),
    }
    json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
