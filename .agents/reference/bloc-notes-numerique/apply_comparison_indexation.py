#!/usr/bin/env python3
"""Apply robots indexation state to explicitly approved comparison routes."""

from pathlib import Path
import re

from comparison_publication import INDEXABLE_COMPARISON_ROUTES

ROOT = Path(__file__).resolve().parent


def path_for_route(route: str) -> Path:
    if not route.startswith("/comparatifs/"):
        raise SystemExit(f"Refusing non-comparison route: {route}")
    relative = route.strip("/")
    return ROOT / relative / "index.html"


for route in sorted(INDEXABLE_COMPARISON_ROUTES):
    page = path_for_route(route)
    if not page.exists():
        raise SystemExit(f"Missing approved comparison page: {route}")

    html = page.read_text(encoding="utf-8")
    updated, count = re.subn(
        r'<meta\s+name="robots"\s+content="[^"]*"\s*/?>',
        '<meta name="robots" content="index,follow">',
        html,
        count=1,
        flags=re.I,
    )
    if count != 1:
        raise SystemExit(f"Could not set robots meta for {route}")

    page.write_text(updated, encoding="utf-8")
    print("indexable", route)
