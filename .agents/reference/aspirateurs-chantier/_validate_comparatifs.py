#!/usr/bin/env python3
"""Machine-integrity QA for comparison pages.

This validator deliberately does NOT enforce editorial quotas, scoring, ranking,
weights, hard gates or a fixed article architecture. Those decisions belong to
comparison-analysis-workflow / PUBLISH_REVIEW.
"""
from pathlib import Path
import json
import re

BASE = Path(__file__).resolve().parent
SLUGS = [
    "meilleur-aspirateur-de-chantier",
    "aspirateur-eau-poussiere",
    "aspirateur-chantier-sans-fil",
    "aspirateur-chantier-sans-sac",
    "aspirateur-chantier-puissant",
    "aspirateur-professionnel",
    "aspirateur-industriel",
    "aspirateur-classe-m",
    "petit-aspirateur-de-chantier",
]

PLACEHOLDERS = (
    "<!-- Contenu à rédiger -->",
    "<!-- Contenu test à rédiger -->",
    "MM/AAAA",
    "TODO CONTENT",
)

# Positive first-hand claims only. Negative/disclosure statements such as
# "nous n'avons pas testé" are intentionally excluded.
FAKE_HANDS_ON_PATTERNS = [
    r"\bnous avons test[ée]s?\b",
    r"\blors de nos tests?\b",
    r"\bapr[eè]s nos tests?\b",
    r"\bnous l['’]avons utilis[ée]\b",
    r"\bpendant notre test\b",
]


def plain_text(html):
    text = re.sub(r"<script.*?</script>|<style.*?</style>", " ", html, flags=re.S | re.I)
    return re.sub(r"<[^>]+>", " ", text)


def heading_signature(html):
    return tuple(
        re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", value)).strip().lower()
        for value in re.findall(r"<h2\b[^>]*>(.*?)</h2>", html, flags=re.S | re.I)
    )


def long_paragraphs(html):
    values = []
    for raw in re.findall(r"<p\b[^>]*>(.*?)</p>", html, flags=re.S | re.I):
        text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", raw)).strip()
        if len(text) >= 180:
            values.append(text)
    return values


errors = []
warnings = []
html_by_slug = {}

for slug in SLUGS:
    page = BASE / "comparatifs" / slug / "index.html"
    data = BASE / ".content" / "comparisons" / f"{slug}.json"

    if not page.exists():
        errors.append(f"{slug}: missing HTML")
        continue
    if not data.exists():
        errors.append(f"{slug}: missing comparison JSON")
        continue

    html = page.read_text(encoding="utf-8")
    html_by_slug[slug] = html

    try:
        obj = json.loads(data.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{slug}: invalid JSON ({exc})")
        continue

    expected_canonical = f'https://aspirateurs-chantier.fr/comparatifs/{slug}/'
    canonical = re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"', html, flags=re.I)
    robots = re.search(r'<meta\s+name="robots"\s+content="([^"]+)"', html, flags=re.I)
    h1_count = len(re.findall(r"<h1\b", html, flags=re.I))

    if canonical is None or canonical.group(1) != expected_canonical:
        errors.append(f"{slug}: canonical mismatch")
    if robots is None or "index" not in robots.group(1).lower() or "follow" not in robots.group(1).lower():
        errors.append(f"{slug}: draft robots must contain index, follow")
    if h1_count != 1:
        errors.append(f"{slug}: expected exactly one H1, got {h1_count}")
    for placeholder in PLACEHOLDERS:
        if placeholder.lower() in html.lower():
            errors.append(f"{slug}: placeholder present: {placeholder}")

    lower_text = plain_text(html).lower()
    for pattern in FAKE_HANDS_ON_PATTERNS:
        if re.search(pattern, lower_text, flags=re.I):
            errors.append(f"{slug}: possible fake hands-on language: {pattern}")

    if obj.get("slug") and obj["slug"] != slug:
        errors.append(f"{slug}: JSON slug mismatch ({obj['slug']})")
    expected_url = f"/comparatifs/{slug}/"
    if obj.get("url") and obj["url"] != expected_url:
        errors.append(f"{slug}: JSON url mismatch ({obj['url']})")

    notes = obj.get("notes", {})
    if notes.get("affiliate_commission_used_in_ranking") not in (None, False):
        errors.append(f"{slug}: affiliate commission cannot influence recommendation/ranking")

    # Warnings are useful review signals, not machine blockers.
    if not re.search(r"<h2\b", html, flags=re.I):
        warnings.append(f"{slug}: no H2 found")
    if 'class="answer-box"' not in html:
        warnings.append(f"{slug}: no answer-box; acceptable if the page has another strong opening")
    if 'href="https://' not in html:
        warnings.append(f"{slug}: no external source link found")
    if not any(marker in lower_text for marker in ("analyse documentaire", "sans test physique", "sans prétendre à un test physique", "sans prétention de test physique")):
        warnings.append(f"{slug}: no explicit desk-research disclosure detected")

# Cluster-level anti-industrialisation warnings.
signatures = {}
for slug, html in html_by_slug.items():
    sig = heading_signature(html)
    if sig:
        signatures.setdefault(sig, []).append(slug)
for sig, slugs in signatures.items():
    if len(slugs) >= 3:
        warnings.append("identical H2 signature across >=3 comparisons: " + ", ".join(slugs))

paragraph_usage = {}
for slug, html in html_by_slug.items():
    for paragraph in set(long_paragraphs(html)):
        paragraph_usage.setdefault(paragraph, []).append(slug)
for paragraph, slugs in paragraph_usage.items():
    if len(slugs) >= 3:
        warnings.append(
            "identical long paragraph across >=3 comparisons: "
            + ", ".join(slugs)
            + f" :: {paragraph[:120]}…"
        )

for warning in warnings:
    print("WARN", warning)

if errors:
    for error in errors:
        print("FAIL", error)
    raise SystemExit(1)

print(f"PASS: {len(SLUGS)} comparison pages satisfy machine-integrity QA.")
print("NOTE: machine integrity is not editorial approval; run comparison-analysis-workflow / PUBLISH_REVIEW before human validation.")
