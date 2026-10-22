#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

from comparison_publication import INDEXABLE_COMPARISON_ROUTES

ROOT = Path(__file__).resolve().parent
FAIL = []
WARN = []

ALLOWED_EVIDENCE = {
    'VERIFIED', 'SUPPORTED', 'INFERRED', 'USER_PATTERN', 'FIRST_HAND',
    'UNKNOWN', 'OUTDATED', 'CONTRADICTED'
}


def fail(label):
    FAIL.append(label)


def warn(label):
    WARN.append(label)


def robots_value(html: str):
    match = re.search(r'<meta\s+name="robots"\s+content="([^"]+)"\s*/?>', html, re.I)
    return match.group(1).lower().replace(' ', '') if match else None


seen_routes = set()

for fp in sorted((ROOT / '.content' / 'comparisons').glob('*.json')):
    try:
        data = json.loads(fp.read_text(encoding='utf-8'))
    except Exception as exc:
        fail(f'{fp.name}: invalid json ({exc})')
        continue

    slug = data.get('slug') or fp.stem
    url = data.get('url')
    intent = data.get('intent')
    criteria = data.get('criteria')
    universe = data.get('product_universe')
    scores = data.get('scores')
    ranking = data.get('ranking')

    if not isinstance(url, str) or not url.startswith('/comparatifs/'):
        fail(f'{fp.name}: comparison url')
    else:
        seen_routes.add(url)

    if not isinstance(intent, dict) or not intent.get('query'):
        fail(f'{fp.name}: intent/query')
    elif not (intent.get('user_job') or intent.get('decision')):
        warn(f'{fp.name}: intent has no explicit user_job/decision')

    # Candidate scope is optional as a formal data structure. If persisted, validate it.
    universe_ids = []
    if universe is not None:
        if not isinstance(universe, list) or not universe:
            fail(f'{fp.name}: malformed product universe')
            universe = []
        universe_ids = [p.get('id') for p in universe if isinstance(p, dict)]
        if len(universe_ids) != len(universe) or any(not x for x in universe_ids):
            fail(f'{fp.name}: product ids')
        if len(set(universe_ids)) != len(universe_ids):
            fail(f'{fp.name}: duplicate product ids')
        for product in universe:
            if not isinstance(product, dict):
                continue
            if not product.get('name'):
                fail(f'{fp.name}: incomplete product universe entry')
            if product.get('status') in {'ELIGIBLE', 'CONDITIONALLY_ELIGIBLE'} and not product.get('source'):
                fail(f'{fp.name}: eligible product without source ({product.get("id")})')

    # Criteria and weighting are optional. If weights are used, they must be coherent.
    criterion_ids = []
    if criteria is not None:
        if not isinstance(criteria, list) or not criteria:
            fail(f'{fp.name}: malformed criteria')
            criteria = []
        criterion_ids = [c.get('id') for c in criteria if isinstance(c, dict)]
        if len(criterion_ids) != len(criteria) or any(not x for x in criterion_ids):
            fail(f'{fp.name}: criterion ids')
        if len(set(criterion_ids)) != len(criterion_ids):
            fail(f'{fp.name}: duplicate criteria')

        weight_presence = [isinstance(c, dict) and c.get('weight') is not None for c in criteria]
        if any(weight_presence):
            if not all(weight_presence):
                fail(f'{fp.name}: partial criterion weighting')
            else:
                weights = [c.get('weight') for c in criteria]
                if any(not isinstance(w, (int, float)) for w in weights):
                    fail(f'{fp.name}: criterion weights')
                elif abs(sum(weights) - 100) > 1e-9:
                    fail(f'{fp.name}: weights must sum to 100 when weighting is used')

    if data.get('affiliate_commission_used_in_ranking') is True:
        fail(f'{fp.name}: affiliate commission must not affect ranking')

    # Scoring is optional. Validate only what is actually persisted.
    if scores is not None:
        if not isinstance(scores, dict):
            fail(f'{fp.name}: malformed scores')
            scores = {}
        if not criterion_ids:
            fail(f'{fp.name}: scores persisted without criteria')

        for product_id, product_scores in scores.items():
            if universe_ids and product_id not in universe_ids:
                fail(f'{fp.name}: scored product outside universe ({product_id})')
            if not isinstance(product_scores, dict):
                fail(f'{fp.name}: malformed score set ({product_id})')
                continue
            for criterion_id, cell in product_scores.items():
                if criterion_ids and criterion_id not in criterion_ids:
                    fail(f'{fp.name}: score for unknown criterion {product_id}/{criterion_id}')
                if not isinstance(cell, dict):
                    fail(f'{fp.name}: malformed score {product_id}/{criterion_id}')
                    continue
                value = cell.get('score')
                if not isinstance(value, (int, float)) or not (0 <= value <= 10):
                    fail(f'{fp.name}: invalid score {product_id}/{criterion_id}')
                evidence = cell.get('evidence_class')
                if evidence is not None and evidence not in ALLOWED_EVIDENCE:
                    fail(f'{fp.name}: invalid evidence class {product_id}/{criterion_id}')
                if evidence in {'UNKNOWN', 'CONTRADICTED', 'OUTDATED'}:
                    fail(f'{fp.name}: unstable evidence used for score {product_id}/{criterion_id}')
                justification = cell.get('justification')
                if justification is not None and (not isinstance(justification, str) or not justification.strip()):
                    fail(f'{fp.name}: empty score justification {product_id}/{criterion_id}')

    # Ranking is optional. It can be ordinal without a numeric score.
    if ranking is not None:
        if not isinstance(ranking, list) or not ranking:
            fail(f'{fp.name}: malformed ranking')
            ranking = []
        ranking_ids = []
        for row in ranking:
            if not isinstance(row, dict):
                fail(f'{fp.name}: malformed ranking row')
                continue
            product_id = row.get('product_id')
            ranking_ids.append(product_id)
            if not product_id:
                fail(f'{fp.name}: ranking row without product_id')
            if universe_ids and product_id not in universe_ids:
                fail(f'{fp.name}: ranked product outside universe ({product_id})')
            if not isinstance(row.get('rank'), int) or row.get('rank') < 1:
                fail(f'{fp.name}: invalid rank ({product_id})')
            if row.get('score') is not None and not isinstance(row.get('score'), (int, float)):
                fail(f'{fp.name}: invalid optional ranking score ({product_id})')

        if len(set(ranking_ids)) != len(ranking_ids):
            fail(f'{fp.name}: duplicate ranked products')
        ranks = [r.get('rank') for r in ranking if isinstance(r, dict) and isinstance(r.get('rank'), int)]
        if ranks and sorted(ranks) != list(range(1, len(ranks) + 1)):
            fail(f'{fp.name}: non-contiguous ranking')

    if not data.get('methodology_note'):
        warn(f'{fp.name}: methodology note absent')

    page = ROOT / 'comparatifs' / slug / 'index.html'
    if not page.exists():
        fail(f'{fp.name}: page missing')
        continue

    html = page.read_text(encoding='utf-8')
    article = re.search(r'<article class="content-main">(.*?)</article>', html, re.S | re.I)
    if not article:
        fail(f'{slug}: article.content-main')
        continue
    body = article.group(1)

    if '<!-- Contenu à rédiger -->' in body:
        fail(f'{slug}: placeholder')

    robots = robots_value(html)
    if url in INDEXABLE_COMPARISON_ROUTES:
        if robots != 'index,follow':
            fail(f'{slug}: approved page must be index,follow (found {robots})')
    elif robots != 'noindex,follow':
        fail(f'{slug}: unapproved page must remain noindex,follow (found {robots})')

    if len(re.findall(r'<h1\b', html, re.I)) != 1:
        fail(f'{slug}: expected exactly one H1')
    if not re.search(r'<link rel="canonical" href="https://bloc-notes-numeriques\.fr/comparatifs/[^\"]+/">', html, re.I):
        fail(f'{slug}: canonical')
    if not re.search(r'href="https?://', body, re.I):
        fail(f'{slug}: no external evidence source rendered')

    fake_hands_on = re.search(
        r'\b(?:nous avons testé|nous avons mesuré|après (?:plusieurs|quelques) (?:jours|semaines) de test|lors de notre test)\b',
        re.sub(r'<[^>]+>', ' ', body),
        re.I,
    )
    if fake_hands_on:
        fail(f'{slug}: possible undocumented hands-on language')

# Validate the hub publication state separately because it has no comparison JSON.
hub_route = '/comparatifs/'
hub = ROOT / 'comparatifs' / 'index.html'
if not hub.exists():
    fail('comparison hub missing')
else:
    hub_robots = robots_value(hub.read_text(encoding='utf-8'))
    expected = 'index,follow' if hub_route in INDEXABLE_COMPARISON_ROUTES else 'noindex,follow'
    if hub_robots != expected:
        fail(f'comparison hub robots must be {expected} (found {hub_robots})')

# The manifest must not silently contain unknown detail routes.
unknown_approved = INDEXABLE_COMPARISON_ROUTES - seen_routes - {hub_route}
for route in sorted(unknown_approved):
    fail(f'indexation manifest contains unknown comparison route: {route}')

if WARN:
    print('\n'.join('WARN ' + x for x in WARN))
if FAIL:
    print('\n'.join('FAIL ' + x for x in FAIL))
    sys.exit(1)

print('PASS: comparison pages have no machine-detectable publication blockers')
print('PASS: robots state matches the explicit comparison indexation manifest')
print('NOTE: scoring, weights, rankings and TSC are optional; when present, persisted data is checked for consistency')
