#!/usr/bin/env python3
"""Apply the latest brand-cluster audit decisions without fabricating publish state.

The cluster audit classifies the amount of editorial work needed per URL. It does
not grant READY_FOR_HUMAN_VALIDATION; that remains controlled by v2 run evidence
and the per-page PUBLISH_REVIEW.
"""
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
AUDIT_ARTIFACT = '.content/brands/cluster-audit-2026-09-10.md'
AUDIT_COMMIT = '3a79ddb899fe9c17f210e4b413738d68f19df705'
AUDIT_DATE = '2026-09-10'

VERDICTS = {
    'karcher': ('DEEP_REWRITE', 0.95),
    'makita': ('DEEP_REWRITE', 0.95),
    'parkside': ('DEEP_REWRITE', 0.95),
    'nilfisk': ('DEEP_REWRITE', 0.95),
    'bosch': ('LIGHT_UPDATE', 0.90),
    'festool': ('LIGHT_UPDATE', 0.90),
    'dewalt': ('LIGHT_UPDATE', 0.90),
    'mirka': ('LIGHT_UPDATE', 0.90),
}

for slug, (verdict, confidence) in VERDICTS.items():
    path = BASE / '.content' / 'brands' / f'{slug}.yaml'
    data = json.loads(path.read_text(encoding='utf-8'))

    existing = data.get('cluster_audit') if isinstance(data.get('cluster_audit'), dict) else {}
    data['cluster_audit'] = {
        **existing,
        'audit_artifact': AUDIT_ARTIFACT,
        'audited_snapshot': AUDIT_COMMIT,
        'date': AUDIT_DATE,
        'verdict': verdict,
        'confidence': confidence,
        'next_step': 'brand-content-workflow',
        'order_gate': 'CLUSTER_AUDIT -> PER_PAGE_SHARED_WORKFLOW -> PUBLISH_REVIEW -> HUMAN_VALIDATION',
    }
    data['recovery_verdict'] = verdict

    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'✓ cluster verdict {slug}: {verdict}')
