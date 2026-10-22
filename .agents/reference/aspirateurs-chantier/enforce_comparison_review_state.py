#!/usr/bin/env python3
"""Keep comparison ledgers honest about workflow execution.

Generators may refresh noindex drafts, but cannot grant a publish-review PASS. A
comparison reaches READY_FOR_HUMAN_VALIDATION only when a valid v2 run-evidence file
exists and records the final analysis PASS.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
SLUGS = [
    'meilleur-aspirateur-de-chantier',
    'aspirateur-professionnel',
    'aspirateur-classe-m',
    'aspirateur-chantier-puissant',
    'aspirateur-eau-poussiere',
    'aspirateur-chantier-sans-fil',
    'aspirateur-chantier-sans-sac',
    'petit-aspirateur-de-chantier',
    'aspirateur-industriel',
]
READY = 'READY_FOR_HUMAN_VALIDATION'
REQUIRES = 'REQUIRES_WORKFLOW_RERUN'


def run_is_ready(slug):
    path = ROOT / '.content' / 'comparisons' / 'runs' / f'{slug}.json'
    if not path.exists():
        return False
    try:
        obj = json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return False
    return (
        obj.get('contract_version') == 2
        and obj.get('slug') == slug
        and obj.get('status') == 'PASS'
        and obj.get('publish_review') == 'PASS — READY_FOR_HUMAN_VALIDATION'
    )


def main():
    for slug in SLUGS:
        ledger = ROOT / '.content' / 'comparisons' / f'{slug}.json'
        obj = json.loads(ledger.read_text(encoding='utf-8'))
        editorial = obj.setdefault('editorial', {})
        editorial['workflow_contract_version'] = 2
        editorial['publish_review'] = READY if run_is_ready(slug) else REQUIRES
        editorial['run_evidence'] = f'.content/comparisons/runs/{slug}.json'
        editorial['generator_role'] = 'shell_and_components_only'
        ledger.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(slug, editorial['publish_review'])


if __name__ == '__main__':
    main()
