#!/usr/bin/env python3
from pathlib import Path
import re

from comparison_content import COMPARISON_CONTENT
from comparison_bespoke_output import BESPOKE_COMPARISON_META
from comparison_bespoke_priority_20260909 import META as PRIORITY_META
from comparison_bespoke_remaining_20260909 import META as REMAINING_META

ROOT = Path(__file__).resolve().parent
ALL_META = {**BESPOKE_COMPARISON_META, **PRIORITY_META, **REMAINING_META}


def replace_once(html: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, replacement, html, count=1, flags=re.S | re.I)
    if count != 1:
        raise SystemExit(f'Could not replace {label}')
    return updated


for slug, body in COMPARISON_CONTENT.items():
    page = ROOT / 'comparatifs' / slug / 'index.html'
    if not page.exists():
        raise SystemExit(f'Missing comparison page: {page}')

    html = page.read_text(encoding='utf-8')
    article = re.search(r'(<article class="content-main">)(.*?)(</article>)', html, re.S | re.I)
    if not article:
        raise SystemExit(f'article.content-main missing: {slug}')

    html = html[:article.start(2)] + '\n      ' + body + '\n    ' + html[article.end(2):]

    meta = ALL_META.get(slug)
    if meta:
        html = replace_once(html, r'<title>.*?</title>', f'<title>{meta["title"]}</title>', f'{slug}: title')
        html = replace_once(html, r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{meta["description"]}">', f'{slug}: meta description')
        html = replace_once(html, r'<h1>.*?</h1>', f'<h1>{meta["h1"]}</h1>', f'{slug}: H1')
        html = replace_once(html, r'<p class="lead">.*?</p>', f'<p class="lead">{meta["lead"]}</p>', f'{slug}: lead')
        html = replace_once(html, r'<span class="page-meta-item">.*?</span>', f'<span class="page-meta-item">{meta["status_label"]}</span>', f'{slug}: status label')

    if '<!-- Contenu à rédiger -->' in html:
        raise SystemExit(f'Placeholder still present: {slug}')
    if not re.search(r'<meta\s+name="robots"\s+content="[^"]+"\s*/?>', html, re.I):
        raise SystemExit(f'robots meta missing: {slug}')

    page.write_text(html, encoding='utf-8')
    print('updated', slug)
