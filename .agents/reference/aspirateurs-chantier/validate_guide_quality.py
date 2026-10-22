#!/usr/bin/env python3
"""Machine-detectable publication blockers for /guides/ on aspirateurs-chantier.fr.

This validator deliberately does not score editorial quality with word counts,
heading quotas, link quotas, source quotas or mandatory article shapes. Substantive
quality belongs to guide-analysis-workflow / PUBLISH_REVIEW.

All Guide routes remain index, follow during recovery. A persisted Guide record
with PASS — READY_FOR_HUMAN_VALIDATION activates stricter finished-draft checks, but
still does not authorize indexation.
"""
from pathlib import Path
import html as html_lib
import json
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
GUIDES = ROOT / "guides"
RECORDS = ROOT / ".content" / "guides"
SITE_ORIGIN = "https://aspirateurs-chantier.fr"
READY = "PASS — READY_FOR_HUMAN_VALIDATION"

ARTICLE_RE = re.compile(r'<article\b[^>]*class="[^"]*content-main[^"]*"[^>]*>(.*?)</article>', re.S | re.I)
H1_RE = re.compile(r'<h1\b[^>]*>(.*?)</h1>', re.S | re.I)
TITLE_RE = re.compile(r'<title>(.*?)</title>', re.S | re.I)
META_DESCRIPTION_RE = re.compile(r'<meta\b[^>]*name="description"[^>]*content="([^"]*)"[^>]*>', re.I)
CANONICAL_RE = re.compile(r'<link\b[^>]*rel="canonical"[^>]*href="([^"]+)"[^>]*>', re.I)
ROBOTS_RE = re.compile(r'<meta\b[^>]*name="robots"[^>]*content="([^"]+)"[^>]*>', re.I)
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


def clean_text(raw):
    raw = TAG_RE.sub(" ", raw)
    raw = html_lib.unescape(raw)
    return re.sub(r"\s+", " ", raw).strip()


def route_for_page(page):
    return f"/guides/{page.parent.name}/"


def expected_canonical(page):
    return f"{SITE_ORIGIN}{route_for_page(page)}"


def normalized_robots(value):
    return ",".join(part.strip().lower() for part in value.split(","))


def record_for_slug(slug):
    path = RECORDS / f"{slug}.json"
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def is_ready(slug):
    record = record_for_slug(slug)
    return bool(record and record.get("editorial", {}).get("publish_review") == READY)


def local_target_exists(href):
    parsed = urlsplit(href)
    path = parsed.path
    if not path or not path.startswith("/") or path.startswith("//"):
        return True
    target = ROOT / path.lstrip("/")
    if target.is_dir():
        target = target / "index.html"
    return target.exists()


def inspect(page):
    page_html = page.read_text(encoding="utf-8")
    slug = page.parent.name
    finished = is_ready(slug)
    issues = []

    article_matches = ARTICLE_RE.findall(page_html)
    if len(article_matches) != 1:
        issues.append(f"article.content-main count={len(article_matches)} (expected 1)")
        article = article_matches[0] if article_matches else ""
    else:
        article = article_matches[0]

    if finished and not clean_text(article):
        issues.append("READY draft has empty article.content-main")

    if finished:
        for marker in PLACEHOLDER_PATTERNS:
            if marker.lower() in page_html.lower():
                issues.append(f"READY draft still contains placeholder: {marker}")

    titles = TITLE_RE.findall(page_html)
    if len(titles) != 1 or not clean_text(titles[0]):
        issues.append("missing or empty <title>")

    descriptions = META_DESCRIPTION_RE.findall(page_html)
    if len(descriptions) != 1 or not descriptions[0].strip():
        issues.append("missing or empty meta description")

    h1s = H1_RE.findall(page_html)
    if len(h1s) != 1 or not clean_text(h1s[0]):
        issues.append(f"H1 count={len(h1s)} (expected one non-empty H1)")

    robots = [normalized_robots(v) for v in ROBOTS_RE.findall(page_html)]
    if "index,follow" not in robots:
        issues.append("Guide recovery state must remain index, follow")

    canonicals = CANONICAL_RE.findall(page_html)
    expected = expected_canonical(page)
    if canonicals != [expected]:
        issues.append(f"canonical mismatch: {canonicals!r} != {[expected]!r}")

    # Duplicate IDs and broken contextual links are blockers even before final review.
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

    if finished and SOURCES_H2_RE.search(article):
        after_sources = re.split(SOURCES_H2_RE, article, maxsplit=1)[-1]
        if not EXTERNAL_LINK_RE.search(after_sources):
            issues.append("READY draft has Sources section but no external source link")

    return issues


def inspect_hub():
    page = GUIDES / "index.html"
    issues = []
    if not page.exists():
        return ["Guide hub missing"]
    html = page.read_text(encoding="utf-8")
    robots = [normalized_robots(v) for v in ROBOTS_RE.findall(html)]
    if "index,follow" not in robots:
        issues.append("Guide hub must remain index, follow during recovery")
    if CANONICAL_RE.findall(html) != [f"{SITE_ORIGIN}/guides/"]:
        issues.append("Guide hub canonical mismatch")
    h1s = H1_RE.findall(html)
    if len(h1s) != 1 or not clean_text(h1s[0]):
        issues.append("Guide hub expected one non-empty H1")
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

    ready_count = sum(1 for page in pages if is_ready(page.parent.name))
    print(f"GUIDE_QUALITY: PASS — {len(pages) + 1} Guide routes have no machine-detectable structural blockers")
    print(f" - READY records under stricter finished-draft checks: {ready_count}")
    print(" - all Guide routes remain index, follow")
    print("NOTE: machine validation does not replace guide-analysis-workflow / PUBLISH_REVIEW or human editorial judgment.")


if __name__ == "__main__":
    main()
