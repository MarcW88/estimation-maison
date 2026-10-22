#!/usr/bin/env python3
"""Machine-detectable publication blockers for /guides/.

This validator deliberately does not score editorial quality with word counts,
heading quotas, link quotas, source quotas or mandatory article shapes. Those
questions belong to guide-analysis-workflow / PUBLISH_REVIEW.
"""
from pathlib import Path
import html as html_lib
import re
from urllib.parse import urlsplit

from publication_indexation import INDEXABLE_GUIDE_ROUTES

ROOT = Path(__file__).resolve().parent
GUIDES = ROOT / "guides"
SITE_ORIGIN = "https://bloc-notes-numeriques.fr"

ARTICLE_RE = re.compile(
    r'<article\b[^>]*class="[^"]*content-main[^"]*"[^>]*>(.*?)</article>',
    re.S | re.I,
)
H1_RE = re.compile(r'<h1\b[^>]*>(.*?)</h1>', re.S | re.I)
TITLE_RE = re.compile(r'<title>(.*?)</title>', re.S | re.I)
META_DESCRIPTION_RE = re.compile(
    r'<meta\b[^>]*name="description"[^>]*content="([^"]*)"[^>]*>', re.I
)
CANONICAL_RE = re.compile(
    r'<link\b[^>]*rel="canonical"[^>]*href="([^"]+)"[^>]*>', re.I
)
ROBOTS_RE = re.compile(
    r'<meta\b[^>]*name="robots"[^>]*content="([^"]+)"[^>]*>', re.I
)
ID_RE = re.compile(r'\bid="([^"]+)"', re.I)
HREF_RE = re.compile(r'<a\b[^>]*href="([^"]+)"', re.I)
TAG_RE = re.compile(r"<[^>]+>", re.S)
SOURCES_H2_RE = re.compile(r'<h2\b[^>]*id="sources"[^>]*>', re.I)
EXTERNAL_LINK_RE = re.compile(r'<a\b[^>]*href="https?://', re.I)

PLACEHOLDER_PATTERNS = (
    "<!-- Contenu à rédiger -->",
    "Lorem ipsum",
    "TODO_CONTENT",
    "CONTENT_PLACEHOLDER",
)


def clean_text(raw: str) -> str:
    raw = TAG_RE.sub(" ", raw)
    raw = html_lib.unescape(raw)
    return re.sub(r"\s+", " ", raw).strip()


def route_for_page(page: Path) -> str:
    return f"/guides/{page.parent.name}/"


def expected_canonical(page: Path) -> str:
    return f"{SITE_ORIGIN}{route_for_page(page)}"


def expected_robots(route: str) -> str:
    return "index,follow" if route in INDEXABLE_GUIDE_ROUTES else "noindex,follow"


def local_target_exists(href: str) -> bool:
    parsed = urlsplit(href)
    path = parsed.path
    if not path or not path.startswith("/") or path.startswith("//"):
        return True
    target = ROOT / path.lstrip("/")
    if target.is_dir():
        target = target / "index.html"
    return target.exists()


def inspect(page: Path):
    page_html = page.read_text(encoding="utf-8")
    issues = []
    route = route_for_page(page)

    article_matches = ARTICLE_RE.findall(page_html)
    if len(article_matches) != 1:
        issues.append(f"article.content-main count={len(article_matches)} (expected 1)")
        article = article_matches[0] if article_matches else ""
    else:
        article = article_matches[0]

    if not clean_text(article):
        issues.append("article.content-main empty")

    for marker in PLACEHOLDER_PATTERNS:
        if marker.lower() in page_html.lower():
            issues.append(f"placeholder present: {marker}")

    title = TITLE_RE.findall(page_html)
    if len(title) != 1 or not clean_text(title[0]):
        issues.append("missing or empty <title>")

    descriptions = META_DESCRIPTION_RE.findall(page_html)
    if len(descriptions) != 1 or not descriptions[0].strip():
        issues.append("missing or empty meta description")

    h1s = H1_RE.findall(page_html)
    if len(h1s) != 1 or not clean_text(h1s[0]):
        issues.append(f"H1 count={len(h1s)} (expected one non-empty H1)")

    robots = ROBOTS_RE.findall(page_html)
    normalized_robots = [
        ",".join(part.strip().lower() for part in value.split(","))
        for value in robots
    ]
    expected = expected_robots(route)
    if expected not in normalized_robots:
        issues.append(f"robots publication state mismatch: expected {expected}")

    canonicals = CANONICAL_RE.findall(page_html)
    expected_canonical_url = expected_canonical(page)
    if len(canonicals) != 1:
        issues.append(f"canonical count={len(canonicals)} (expected 1)")
    elif canonicals[0] != expected_canonical_url:
        issues.append(f"canonical mismatch: {canonicals[0]} != {expected_canonical_url}")

    ids = ID_RE.findall(page_html)
    duplicates = sorted({value for value in ids if ids.count(value) > 1})
    if duplicates:
        issues.append("duplicate IDs: " + ", ".join(duplicates))
    id_set = set(ids)

    for href in HREF_RE.findall(article):
        if href.startswith("#"):
            anchor = href[1:]
            if anchor and anchor not in id_set:
                issues.append(f"broken in-page anchor: {href}")
            continue
        if href.startswith("/") and not local_target_exists(href):
            issues.append(f"broken internal link: {href}")

    if SOURCES_H2_RE.search(article):
        after_sources = re.split(SOURCES_H2_RE, article, maxsplit=1)[-1]
        if not EXTERNAL_LINK_RE.search(after_sources):
            issues.append("Sources section present but no external source link found")

    return issues


def inspect_hub() -> list[str]:
    page = GUIDES / "index.html"
    issues = []
    html = page.read_text(encoding="utf-8")
    if '<meta name="robots" content="index,follow">' not in html:
        issues.append("Guide hub expected index,follow")
    canonical = CANONICAL_RE.findall(html)
    if canonical != [f"{SITE_ORIGIN}/guides/"]:
        issues.append("Guide hub canonical mismatch")
    return issues


def main():
    pages = sorted(GUIDES.glob("*/index.html"))
    failures = {}

    hub_issues = inspect_hub()
    if hub_issues:
        failures["_hub"] = hub_issues

    for page in pages:
        issues = inspect(page)
        if issues:
            failures[page.parent.name] = issues

    if failures:
        for slug, issues in failures.items():
            print(f"FAIL {slug}")
            for issue in issues:
                print(f"  - {issue}")
        raise SystemExit(1)

    print(
        f"PASS: {len(pages) + 1} Guide routes have no machine-detectable "
        "publication blockers and match explicit indexation approval"
    )
    print(
        "NOTE: machine validation does not replace guide-analysis-workflow / "
        "PUBLISH_REVIEW or human editorial judgment."
    )


if __name__ == "__main__":
    main()
