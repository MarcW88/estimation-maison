#!/usr/bin/env python3
"""Keep brand ledgers honest about workflow execution.

Generators may create or refresh draft content, but they are not allowed to grant a
publish-review PASS. READY_FOR_HUMAN_VALIDATION is retained only when a valid v2 run
file exists and records the final analysis PASS. Otherwise the page remains a draft
requiring a full shared-skill rerun.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
SLUGS = ['karcher','bosch','makita','festool','dewalt','parkside','nilfisk','mirka']
READY = 'READY_FOR_HUMAN_VALIDATION'
REQUIRES = 'REQUIRES_WORKFLOW_RERUN'


def run_is_ready(slug):
    path = ROOT / '.content' / 'brands' / 'runs' / f'{slug}.json'
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
        ledger = ROOT / '.content' / 'brands' / f'{slug}.yaml'
        obj = json.loads(ledger.read_text(encoding='utf-8'))
        editorial = obj.setdefault('editorial', {})
        editorial['workflow_contract_version'] = 2
        editorial['publish_review'] = READY if run_is_ready(slug) else REQUIRES
        editorial['run_evidence'] = f'.content/brands/runs/{slug}.json'
        ledger.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

        audit_dir = ROOT / '.content' / 'brands' / 'audits'
        candidates = sorted(audit_dir.glob(f'{slug}-*.md'))
        for audit in candidates:
            text = audit.read_text(encoding='utf-8')
            status = READY if run_is_ready(slug) else REQUIRES
            text = re.sub(r'(?m)^- Statut\s*:\s*\*\*.*?\*\*\.?$', f'- Statut : **{status}**.', text)
            if 'workflow contract v2' not in text.lower():
                text += '\n- Workflow contract v2 : run-evidence requis avant tout nouveau PASS de publication.\n'
            audit.write_text(text, encoding='utf-8')

        print(slug, editorial['publish_review'])


if __name__ == '__main__':
    main()
