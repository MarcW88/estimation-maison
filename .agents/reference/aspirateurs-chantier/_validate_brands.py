#!/usr/bin/env python3
"""Repository-specific QA gate for generated brand hubs.

Machine-observable integrity only. The substantive workflow still lives in the
shared skills + brand-analysis-workflow, but this gate blocks obvious template
industrialisation and any false READY_FOR_HUMAN_VALIDATION state.
"""
from pathlib import Path
from html import unescape
from collections import defaultdict
import json
import re

from validate_brand_run_evidence import validate_slug as validate_run_evidence

BASE = Path(__file__).resolve().parent
SLUGS = ['karcher','bosch','makita','festool','dewalt','parkside','nilfisk','mirka']
TAG = re.compile(r'<[^>]+>', re.S)
H2 = re.compile(r'<h2\b[^>]*id="([^"]+)"[^>]*>(.*?)</h2>', re.S | re.I)
P = re.compile(r'<p\b[^>]*>(.*?)</p>', re.S | re.I)
EXT = re.compile(r'<a\b[^>]*href="https?://', re.I)
READY = 'READY_FOR_HUMAN_VALIDATION'
LEGACY_TEMPLATE_IDS = {'distinction','gamme','ecosysteme','forces','limites','choisir','eviter','alternatives'}


def clean(s):
    return re.sub(r'\s+', ' ', unescape(TAG.sub(' ', s))).strip()


def editorial_before_sources(body):
    """Exclude shared sourcing/disclosure boilerplate from clone detection."""
    parts = re.split(r'<h2\b[^>]*id="sources"[^>]*>', body, maxsplit=1, flags=re.I)
    return parts[0]


def fail(msgs):
    for msg in msgs:
        print('FAIL', msg)
    raise SystemExit(1)


def main():
    issues = []
    warnings = []
    heading_signatures = defaultdict(list)
    shared_paragraphs = defaultdict(list)

    for slug in SLUGS:
        page = BASE / 'marques' / slug / 'index.html'
        if not page.exists():
            issues.append(f'{slug}: page absente')
            continue

        html = page.read_text(encoding='utf-8')
        m = re.search(r'<article\b[^>]*class="[^"]*content-main[^"]*"[^>]*>(.*?)</article>', html, re.S | re.I)
        body = m.group(1) if m else ''
        text = clean(body).lower()
        clone_body = editorial_before_sources(body)

        if not body:
            issues.append(f'{slug}: article absent')
        if '<!-- contenu à rédiger -->' in body.lower():
            issues.append(f'{slug}: placeholder présent')
        if '<meta name="robots" content="index, follow">' not in html:
            issues.append(f'{slug}: noindex draft absent')
        if body.count('<!-- BRAND_CONTENT_START -->') != 1:
            issues.append(f'{slug}: marqueur BRAND_CONTENT_START invalide')
        if body.count('<!-- BRAND_CONTENT_END -->') != 1:
            issues.append(f'{slug}: marqueur BRAND_CONTENT_END invalide')
        if not re.search(r'<h1\b[^>]*>.*?</h1>', html, re.S | re.I):
            issues.append(f'{slug}: H1 absent')

        expected_canonical = f'https://aspirateurs-chantier.fr/marques/{slug}/'
        canonical = re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"', html, re.I)
        if not canonical or canonical.group(1) != expected_canonical:
            issues.append(f'{slug}: canonical incorrect ou absent')

        for term in [
            'nous avons testé',
            'lors de notre test',
            'pendant notre test',
            'après plusieurs semaines d’utilisation',
            "après plusieurs semaines d'utilisation",
        ]:
            if term in text:
                issues.append(f'{slug}: faux langage de test: {term}')

        data = BASE / '.content' / 'brands' / f'{slug}.yaml'
        if not data.exists():
            issues.append(f'{slug}: fichier de preuves absent')
            continue
        try:
            obj = json.loads(data.read_text(encoding='utf-8'))
        except Exception as exc:
            issues.append(f'{slug}: fichier de preuves illisible: {exc}')
            continue

        if obj.get('slug') != slug:
            issues.append(f'{slug}: slug incohérent dans les données')
        if obj.get('page_type') != 'BRAND_HUB':
            warnings.append(f'{slug}: page_type différent de BRAND_HUB')
        if not obj.get('evidence'):
            issues.append(f'{slug}: evidence ledger vide')
        if not obj.get('editorial', {}).get('desk_research_only'):
            issues.append(f'{slug}: desk_research_only absent ou faux')

        publish_status = obj.get('editorial', {}).get('publish_review')
        if publish_status == READY:
            issues.extend(validate_run_evidence(slug, require_run=True))
        elif publish_status not in {'REQUIRES_WORKFLOW_RERUN', 'PENDING', None}:
            warnings.append(f'{slug}: statut éditorial non standard: {publish_status}')

        h2_ids = tuple(match[0] for match in H2.findall(clone_body))
        if h2_ids:
            heading_signatures[h2_ids].append(slug)
        else:
            issues.append(f'{slug}: aucun H2 éditorial détecté')

        legacy_count = len(LEGACY_TEMPLATE_IDS.intersection(h2_ids))
        if legacy_count >= 5:
            issues.append(f'{slug}: legacy generic brand skeleton detected ({legacy_count} template sections)')

        for para_html in P.findall(clone_body):
            para = clean(para_html)
            if len(para) >= 180:
                shared_paragraphs[para].append(slug)

        source_links = len(EXT.findall(body))
        if source_links == 0:
            warnings.append(f'{slug}: aucun lien source externe dans le rendu')

        print(f'{slug}: machine integrity OK ({publish_status or "UNSET"})')

    for signature, slugs in heading_signatures.items():
        if len(slugs) >= 3:
            issues.append(
                'structure H2 identique sur plusieurs marques '
                f"({', '.join(slugs)}): {' > '.join(signature)}"
            )

    for para, slugs in shared_paragraphs.items():
        unique_slugs = sorted(set(slugs))
        if len(unique_slugs) >= 3:
            excerpt = para[:110] + ('…' if len(para) > 110 else '')
            issues.append(
                f"long paragraphe éditorial partagé entre {', '.join(unique_slugs)}: {excerpt}"
            )

    for warning in warnings:
        print('WARN', warning)
    if issues:
        fail(issues)

    print('PASS: machine integrity, anti-template and publish-state checks completed for 8 brand hubs.')
    print('NOTE: a substantive READY still requires a v2 run evidence file produced by the shared-skill workflow.')


if __name__ == '__main__':
    main()
