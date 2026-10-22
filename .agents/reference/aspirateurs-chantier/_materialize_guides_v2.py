#!/usr/bin/env python3
"""Materialize authored Guide v2 fragments into the existing HTML shell.

This renderer does not research, define intent, fact-check, write or approve content.
Editorial fragments and workflow records live under .content/guides/. Publication
state remains controlled by guide-analysis-workflow / PUBLISH_REVIEW.
"""
from pathlib import Path
from html import escape
import json
import re

ROOT = Path(__file__).resolve().parent
V2 = ROOT / ".content" / "guides" / "v2"
META = json.loads((V2 / "render-map.json").read_text(encoding="utf-8"))
UPDATED_LABEL = "11/09/2026"


def replace_once(text, pattern, repl, label, flags=0):
    out, count = re.subn(pattern, repl, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"{label}: expected one replacement, got {count}")
    return out


def render(slug, cfg):
    page = ROOT / "guides" / slug / "index.html"
    fragment = V2 / f"{slug}.html"
    record = ROOT / ".content" / "guides" / f"{slug}.json"
    if not page.exists():
        raise RuntimeError(f"{slug}: page missing")
    if not fragment.exists():
        raise RuntimeError(f"{slug}: authored v2 fragment missing")
    if not record.exists():
        raise RuntimeError(f"{slug}: workflow record missing")

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
    html = replace_once(
        html,
        r'<div class="answer-box"><div class="article-answer"><p>.*?</p></div></div>',
        f'<div class="answer-box"><div class="article-answer"><p>{escape(cfg["answer"])}</p></div></div>',
        f"{slug} answer",
        re.S,
    )
    html = replace_once(
        html,
        r"<!-- GUIDE_CONTENT_START -->.*?<!-- GUIDE_CONTENT_END -->",
        "<!-- GUIDE_CONTENT_START -->\n" + body + "\n<!-- GUIDE_CONTENT_END -->",
        f"{slug} content",
        re.S,
    )

    toc = "\n".join(f'<a href="#{escape(anchor)}">{escape(label)}</a>' for anchor, label in cfg["toc"])
    html = replace_once(
        html,
        r"<!-- GUIDE_TOC_START -->.*?<!-- GUIDE_TOC_END -->",
        "<!-- GUIDE_TOC_START -->\n" + toc + "\n<!-- GUIDE_TOC_END -->",
        f"{slug} toc",
        re.S,
    )
    html = re.sub(r"Vérifié\s*:\s*\d{2}/\d{2}/\d{4}", f"Vérifié : {UPDATED_LABEL}", html)
    html = re.sub(r"Vérifié\s*:\s*\d{2}/\d{4}", f"Vérifié : {UPDATED_LABEL}", html)

    if '<meta name="robots" content="index, follow">' not in html:
        raise RuntimeError(f"{slug}: index, follow missing after materialization")
    if len(re.findall(r"<h1\b", html, re.I)) != 1:
        raise RuntimeError(f"{slug}: materialized page must contain exactly one H1")

    page.write_text(html, encoding="utf-8")
    print(f"✓ {slug}: Guide v2 fragment materialized")


def main():
    if not META:
        raise RuntimeError("render-map is empty")
    for slug, cfg in META.items():
        render(slug, cfg)
    print("✓ Guide v2 materialization complete; renderer grants no publish/index state")


if __name__ == "__main__":
    main()
