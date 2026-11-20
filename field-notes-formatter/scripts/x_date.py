#!/usr/bin/env python3
"""Print the date of an X (Twitter) post from its link, in US Pacific time.

Usage: python3 x_date.py <x.com link> [more links...]
Example output: https://x.com/IFM_AI/status/2120199814696828942: 10 NOV 2026

X post IDs carry the moment the post was published (the top bits of the ID are
milliseconds since 4 Nov 2010), so no web access is needed.
"""
import datetime as dt
import re
import sys

X_EPOCH_MS = 1288834974657


def pacific(t_utc):
    try:
        from zoneinfo import ZoneInfo
        return t_utc.astimezone(ZoneInfo("America/Los_Angeles"))
    except Exception:
        return t_utc - dt.timedelta(hours=8)  # fallback: standard Pacific offset


def x_date(link):
    m = re.search(r"(?:x|twitter)\.com/[^/\s]+/status/(\d+)", link)
    if not m:
        return None
    ms = (int(m.group(1)) >> 22) + X_EPOCH_MS
    t = pacific(dt.datetime.fromtimestamp(ms / 1000, dt.timezone.utc))
    return f"{t.day} {t.strftime('%b').upper()} {t.year}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for arg in sys.argv[1:]:
        print(f"{arg}: {x_date(arg) or 'not an X post link'}")
