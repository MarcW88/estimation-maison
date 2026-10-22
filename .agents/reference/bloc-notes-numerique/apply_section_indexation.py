#!/usr/bin/env python3
"""Apply explicit publication state to approved editorial sections.

Approved routes become ``index,follow``. Any other route inside the same scope
remains or is reset to ``noindex,follow``. The script also rebuilds a sitemap
from the explicit publication registry and writes a minimal robots.txt.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from xml.sax.saxutils import escape

from publication_indexation import (
    INDEXABLE_ROUTES_BY_SCOPE,
    SCOPE_ROOTS,
    SITEMAP_APPROVED_ROUTES,
)

ROOT = Path(__file__).resolve().parent
SITE_ORIGIN = "https://bloc-notes-numeriques.fr"
ROBOTS_RE = re.compile(r'<meta\s+name="robots"\s+content="[^"]*"\s*/?>', re.I)
CANONICAL_RE = re.compile(
    r'<link\b[^>]*rel="canonical"[^>]*href="([^"]+)"[^>]*>', re.I
)


def route_for_page(page: Path) -> str:
    relative = page.relative_to(ROOT).as_posix()
    if not relative.endswith("/index.html"):
        raise SystemExit(f"Unsupported page path: {relative}")
    return "/" + relative[: -len("index.html")]


def page_for_route(route: str) -> Path:
    return ROOT / route.strip("/") / "index.html"


def canonical_for_html(html: str) -> str | None:
    match = CANONICAL_RE.search(html)
    return match.group(1) if match else None


def set_robots(page: Path, directive: str) -> None:
    html = page.read_text(encoding="utf-8")
    replacement = f'<meta name="robots" content="{directive}">'
    updated, count = ROBOTS_RE.subn(replacement, html, count=1)
    if count != 1:
        raise SystemExit(f"Could not set robots meta for {page.relative_to(ROOT)}")
    if updated != html:
        page.write_text(updated, encoding="utf-8")


def require_self_canonical(route: str) -> Path:
    page = page_for_route(route)
    if not page.exists():
        raise SystemExit(f"Missing approved route: {route}")
    html = page.read_text(encoding="utf-8")
    expected = f"{SITE_ORIGIN}{route}"
    canonical = canonical_for_html(html)
    if canonical != expected:
        raise SystemExit(
            f"Refusing publication for non-self-canonical route {route}: "
            f"canonical={canonical!r}, expected={expected!r}"
        )
    return page


def apply_scope(scope: str) -> None:
    approved = INDEXABLE_ROUTES_BY_SCOPE[scope]
    root = ROOT / SCOPE_ROOTS[scope]

    for route in sorted(approved):
        require_self_canonical(route)

    index_count = 0
    noindex_count = 0
    for page in sorted(root.rglob("index.html")):
        route = route_for_page(page)
        if route in approved:
            set_robots(page, "index,follow")
            index_count += 1
        else:
            set_robots(page, "noindex,follow")
            noindex_count += 1

    print(
        f"PASS {scope}: {index_count} approved route(s) index,follow; "
        f"{noindex_count} unapproved route(s) noindex,follow"
    )


def rebuild_sitemap() -> None:
    urls = []
    for route in sorted(SITEMAP_APPROVED_ROUTES):
        require_self_canonical(route)
        urls.append(f"{SITE_ORIGIN}{route}")

    body = "\n".join(
        f"  <url><loc>{escape(url)}</loc></url>" for url in urls
    )
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{body}\n"
        "</urlset>\n"
    )
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\n"
        f"Sitemap: {SITE_ORIGIN}/sitemap.xml\n",
        encoding="utf-8",
    )
    print(f"PASS sitemap: {len(urls)} approved self-canonical URL(s)")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "scope",
        choices=[*INDEXABLE_ROUTES_BY_SCOPE.keys(), "all"],
        help="Editorial section whose publication state should be applied",
    )
    args = parser.parse_args()

    scopes = INDEXABLE_ROUTES_BY_SCOPE.keys() if args.scope == "all" else (args.scope,)
    for scope in scopes:
        apply_scope(scope)
    rebuild_sitemap()


if __name__ == "__main__":
    main()
