#!/usr/bin/env python3
"""Small presentation patch applied after Usage editorial rendering."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Hub role labels.
fp = ROOT / "usages" / "index.html"
html = fp.read_text(encoding="utf-8")
html = html.replace(
    '<a href="/usages/prise-de-notes-professionnelle/" class="hub-link"><span>Travail et réunions</span>',
    '<a href="/usages/prise-de-notes-professionnelle/" class="hub-link"><span>Travail / usage professionnel</span>',
)
fp.write_text(html, encoding="utf-8")

# The cluster was re-researched and reviewed on 9 September 2026. Keep the
# visible freshness marker aligned with the evidence records after regeneration.
active_slugs = [
    "prise-de-notes-professionnelle",
    "prise-de-notes-etudiant",
    "prise-de-notes-reunion",
    "lecture-et-prise-de-notes",
    "dessin",
    "remplacer-cahiers-papier",
]
for slug in active_slugs:
    page = ROOT / "usages" / slug / "index.html"
    page_html = page.read_text(encoding="utf-8")
    page_html = page_html.replace(
        "Vérifié le 8 septembre 2026",
        "Vérifié le 9 septembre 2026",
    )
    page.write_text(page_html, encoding="utf-8")

print("usage hub role labels and review dates aligned")
