#!/usr/bin/env python3
"""Validate the committed publication state of all approved editorial routes."""

from __future__ import annotations

import re
from pathlib import Path
from xml.etree import ElementTree

from publication_indexation import SITEMAP_APPROVED_ROUTES

ROOT = Path(__file__).resolve().parent
SITE_ORIGIN = "https://bloc-notes-numeriques.fr"
CANONICAL_RE = re.compile(
    r'<link\b[^>]*rel="canonical"[^>]*href="([^"]+)"[^>]*>', re.I
)
ROBOTS_RE = re.compile(
    r'<meta\b[^>]*name="robots"[^>]*content="([^"]+)"[^>]*>', re.I
)
REDIRECT_USAGE_ROUTE = "/usages/annotation-pdf/"
REDIRECT_USAGE_TARGET = "/guides/annoter-pdf-tablette-e-ink/"


def page_for_route(route: str) -> Path:
    return ROOT / route.strip("/") / "index.html"


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def normalized_robots(html: str) -> set[str]:
    return {
        ",".join(part.strip().lower() for part in value.split(","))
        for value in ROBOTS_RE.findall(html)
    }


def main() -> None:
    errors: list[str] = []

    for route in sorted(SITEMAP_APPROVED_ROUTES):
        page = page_for_route(route)
        if not page.exists():
            fail(errors, f"missing approved page: {route}")
            continue
        html = page.read_text(encoding="utf-8")
        if "index,follow" not in normalized_robots(html):
            fail(errors, f"approved route is not index,follow: {route}")
        canonicals = CANONICAL_RE.findall(html)
        expected = f"{SITE_ORIGIN}{route}"
        if canonicals != [expected]:
            fail(errors, f"canonical mismatch for {route}: {canonicals!r}")

    redirect_page = page_for_route(REDIRECT_USAGE_ROUTE)
    if not redirect_page.exists():
        fail(errors, f"missing consolidated redirect: {REDIRECT_USAGE_ROUTE}")
    else:
        html = redirect_page.read_text(encoding="utf-8")
        if "noindex,follow" not in normalized_robots(html):
            fail(errors, f"consolidated redirect must remain noindex: {REDIRECT_USAGE_ROUTE}")
        canonicals = CANONICAL_RE.findall(html)
        expected = f"{SITE_ORIGIN}{REDIRECT_USAGE_TARGET}"
        if canonicals != [expected]:
            fail(errors, f"redirect canonical mismatch: {canonicals!r}")

    sitemap_path = ROOT / "sitemap.xml"
    if not sitemap_path.exists():
        fail(errors, "missing sitemap.xml")
    else:
        try:
            tree = ElementTree.parse(sitemap_path)
            namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            sitemap_urls = {
                node.text.strip()
                for node in tree.findall("sm:url/sm:loc", namespace)
                if node.text
            }
            expected_urls = {f"{SITE_ORIGIN}{route}" for route in SITEMAP_APPROVED_ROUTES}
            missing = expected_urls - sitemap_urls
            unexpected = sitemap_urls - expected_urls
            if missing:
                fail(errors, "sitemap missing: " + ", ".join(sorted(missing)))
            if unexpected:
                fail(errors, "sitemap contains unapproved URLs: " + ", ".join(sorted(unexpected)))
        except ElementTree.ParseError as exc:
            fail(errors, f"invalid sitemap.xml: {exc}")

    robots_path = ROOT / "robots.txt"
    if not robots_path.exists():
        fail(errors, "missing robots.txt")
    else:
        robots = robots_path.read_text(encoding="utf-8")
        if "User-agent: *" not in robots or "Allow: /" not in robots:
            fail(errors, "robots.txt does not allow general crawling")
        if f"Sitemap: {SITE_ORIGIN}/sitemap.xml" not in robots:
            fail(errors, "robots.txt does not declare sitemap.xml")

    if errors:
        print("FAIL")
        for error in errors:
            print("-", error)
        raise SystemExit(1)

    print(
        f"PASS: {len(SITEMAP_APPROVED_ROUTES)} approved routes are index,follow, "
        "self-canonical and present exactly once in the publication sitemap"
    )
    print(
        f"PASS: {REDIRECT_USAGE_ROUTE} remains noindex and canonicalized to "
        f"{REDIRECT_USAGE_TARGET}"
    )


if __name__ == "__main__":
    main()
