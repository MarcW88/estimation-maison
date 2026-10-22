#!/usr/bin/env python3
from pathlib import Path
import json,sys
ALLOWED_EVIDENCE={'VERIFIED','SUPPORTED','INFERRED','USER_PATTERN','FIRST_HAND'}
ALLOWED_STATUS={'ELIGIBLE','CONDITIONALLY_ELIGIBLE','OUTDATED','NOT_COMPARABLE','EXCLUDED'}
def fail(msg): print('FAIL:',msg); raise SystemExit(1)
def main():
    if len(sys.argv)!=2: raise SystemExit('Usage: validate_comparison_data.py comparison.json')
    data=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    if not data.get('intent',{}).get('query'): fail('missing intent.query')
    products=data.get('product_universe',[])
    if len(products)<2: fail('need at least 2 products')
    for p in products:
        if p.get('status') not in ALLOWED_STATUS: fail(f"invalid product status: {p.get('id')}")
        if p.get('status') in {'OUTDATED','NOT_COMPARABLE','EXCLUDED'} and not p.get('exclusion_reason'): fail(f"excluded product missing reason: {p.get('id')}")
    criteria=data.get('criteria',[])
    if len(criteria)<3: fail('need at least 3 criteria')
    if sum(c.get('weight',0) for c in criteria)!=100: fail('criteria weights must sum to 100')
    if data.get('affiliate_commission_used_in_ranking') is not False and data.get('notes',{}).get('affiliate_commission_used_in_ranking') is not False: fail('affiliate commission must not be used in ranking')
    scores=data.get('scores',{}); eligible=[p['id'] for p in products if p['status'] in {'ELIGIBLE','CONDITIONALLY_ELIGIBLE'}]
    for pid in eligible:
        if pid not in scores: fail(f'missing scores for {pid}')
        for criterion in criteria:
            cid=criterion['id']; e=scores[pid].get(cid)
            if not e: fail(f'missing score {pid}/{cid}')
            if e.get('evidence_class') not in ALLOWED_EVIDENCE: fail(f'invalid evidence {pid}/{cid}')
            if not e.get('justification','').strip(): fail(f'missing justification {pid}/{cid}')
    print('PASS: comparison data methodology is structurally valid')
if __name__=='__main__': main()
