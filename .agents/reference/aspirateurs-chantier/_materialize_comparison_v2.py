#!/usr/bin/env python3
"""Materialize authored v2 comparison fragments into the existing HTML shell.

This renderer does not research, brief, write, fact-check, humanize or grant publish
approval. Editorial fragments and metadata are persisted separately under
.content/comparisons/v2/. Publish state remains derived exclusively from v2 run evidence.
"""
from pathlib import Path
from html import escape
import json
import re

ROOT = Path(__file__).resolve().parent
V2 = ROOT / ".content" / "comparisons" / "v2"
META = json.loads((V2 / "render-map.json").read_text(encoding="utf-8"))
UPDATED_ISO = "2026-09-11"
UPDATED_LABEL = "11/09/2026"


def replace_once(text, pattern, repl, label, flags=0):
    out, count = re.subn(pattern, repl, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"{label}: expected one replacement, got {count}")
    return out


def render(slug, cfg):
    page = ROOT / "comparatifs" / slug / "index.html"
    fragment = V2 / f"{slug}.html"
    if not fragment.exists():
        raise RuntimeError(f"missing authored v2 fragment for {slug}")
    html = page.read_text(encoding="utf-8")
    body = fragment.read_text(encoding="utf-8").strip()

    html = replace_once(html, r"<title>.*?</title>", f"<title>{escape(cfg['title'])}</title>", f"{slug} title", re.S)
    html = replace_once(
        html,
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{escape(cfg["description"])}">',
        f"{slug} description",
    )
    html = replace_once(html, r'<h1[^>]*>.*?</h1>', f'<h1 style="margin-top:10px;">{escape(cfg["h1"])}</h1>', f"{slug} h1", re.S)
    html = replace_once(html, r'<p class="lead">.*?</p>', f'<p class="lead">{escape(cfg["lead"])}</p>', f"{slug} lead", re.S)

    if "<!-- COMPARISON_CONTENT_START -->" in html:
        html = replace_once(
            html,
            r"<!-- COMPARISON_CONTENT_START -->.*?<!-- COMPARISON_CONTENT_END -->",
            "<!-- COMPARISON_CONTENT_START -->\n" + body + "\n<!-- COMPARISON_CONTENT_END -->",
            f"{slug} content markers",
            re.S,
        )
    else:
        html = replace_once(
            html,
            r'(<article class="content-main">).*?(</article>)',
            r"\1\n" + body + r"\n\2",
            f"{slug} article body",
            re.S,
        )

    toc = "".join(f'<a href="#{escape(anchor)}">{escape(label)}</a>' for anchor, label in cfg["toc"])
    html = replace_once(html, r'<nav class="toc-list">.*?</nav>', f'<nav class="toc-list">{toc}</nav>', f"{slug} toc", re.S)
    html = re.sub(r"Vérifié\s*:\s*\d{2}/\d{2}/\d{4}", f"Vérifié : {UPDATED_LABEL}", html)
    html = re.sub(r"Vérifié\s*:\s*\d{2}/\d{4}", f"Vérifié : {UPDATED_LABEL}", html)

    if '<meta name="robots" content="index, follow">' not in html:
        raise RuntimeError(f"{slug}: index, follow missing after materialization")

    page.write_text(html, encoding="utf-8")

    ledger_path = ROOT / ".content" / "comparisons" / f"{slug}.json"
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    ledger["updated_at"] = UPDATED_ISO
    ledger["status"] = "V2_EDITORIAL_REWRITE"
    notes = ledger.setdefault("notes", {})
    notes["v2_editorial_source"] = f".content/comparisons/v2/{slug}.html"
    notes["v2_editorial_date"] = UPDATED_ISO
    notes["generator_authored_content"] = False
    notes["noindex_during_rollout"] = False
    ledger_path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"✓ {slug}: v2 fragment materialized")


def main():
    expected = {
        "meilleur-aspirateur-de-chantier",
        "aspirateur-professionnel",
        "aspirateur-classe-m",
        "aspirateur-chantier-puissant",
        "aspirateur-industriel",
        "aspirateur-chantier-sans-fil",
        "aspirateur-eau-poussiere",
        "petit-aspirateur-de-chantier",
    }
    if set(META) != expected:
        raise RuntimeError(f"render-map slugs mismatch: expected {sorted(expected)}, got {sorted(META)}")
    for slug, cfg in META.items():
        render(slug, cfg)
    print("✓ comparison v2 materialization complete; publish state remains run-evidence gated")


if __name__ == "__main__":
    main()
