#!/usr/bin/env python3
"""Seed comparison metadata without overwriting workflow-authored evidence.

`.content/comparisons/<slug>.json` is a flexible methodological support file.
The comparison workflows may persist criteria, sources, exclusions, scores,
rankings or other decision data when they are useful. This generator therefore
creates a minimal file only when one does not exist; it must never reconstruct a
mandatory scoring schema over a reviewed page.
"""

from pathlib import Path
import json
from comparison_pages import COMPARISON_PAGES

ROOT = Path(__file__).resolve().parent
D = ROOT / '.content' / 'comparisons'
D.mkdir(parents=True, exist_ok=True)

for slug, page in COMPARISON_PAGES.items():
    target = D / f'{slug}.json'

    if target.exists():
        # Validate readability, then preserve the workflow-authored payload.
        try:
            existing = json.loads(target.read_text(encoding='utf-8'))
        except Exception as exc:
            raise SystemExit(f'invalid comparison metadata {target}: {exc}')
        if not isinstance(existing, dict):
            raise SystemExit(f'comparison metadata must be an object: {target}')
        print('metadata preserved', slug)
        continue

    payload = {
        'slug': slug,
        'url': f'/comparatifs/{slug}/',
        'status': 'DRAFT',
        'intent': {
            'query': page.get('query'),
            'type': page.get('type'),
            'user_job': page.get('job'),
        },
        'affiliate_commission_used_in_ranking': False,
        'methodology_note': (
            'Minimal seed generated automatically. Enrich only with fields '
            'actually used by comparison-analysis-workflow or '
            'comparison-content-workflow.'
        ),
    }
    target.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding='utf-8',
    )
    print('metadata seeded', slug)
