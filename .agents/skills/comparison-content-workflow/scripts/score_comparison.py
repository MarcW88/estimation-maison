#!/usr/bin/env python3
from pathlib import Path
import json,sys
CONFIDENCE={"VERIFIED":1.00,"FIRST_HAND":1.00,"SUPPORTED":0.95,"INFERRED":0.85,"USER_PATTERN":0.80}
def main():
    if len(sys.argv)!=2: raise SystemExit('Usage: score_comparison.py comparison.json')
    data=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    criteria=data['criteria']; products={p['id']:p for p in data['product_universe']}
    if sum(c['weight'] for c in criteria)!=100: raise SystemExit('FAIL: weights must sum to 100')
    cm={c['id']:c for c in criteria}; results=[]
    for pid,sm in data['scores'].items():
        product=products.get(pid)
        if not product: raise SystemExit(f'FAIL: unknown product {pid}')
        if product.get('status') not in {'ELIGIBLE','CONDITIONALLY_ELIGIBLE'}: continue
        raw=adjusted=0.0; gate=False
        for cid,c in cm.items():
            if cid not in sm: raise SystemExit(f'FAIL: missing score {pid}/{cid}')
            e=sm[cid]; score=float(e['score'])
            if not 0<=score<=10: raise SystemExit(f'FAIL: score outside 0-10 {pid}/{cid}')
            ec=e.get('evidence_class','UNKNOWN')
            if ec not in CONFIDENCE: raise SystemExit(f'FAIL: invalid evidence {pid}/{cid}')
            if not e.get('justification','').strip(): raise SystemExit(f'FAIL: missing justification {pid}/{cid}')
            w=float(c['weight']); raw+=(score*w)/10; adjusted+=(score*CONFIDENCE[ec]*w)/10
            if c.get('hard_gate') and score<float(c.get('hard_gate_min',5)): gate=True
        results.append({'product_id':pid,'name':product.get('name',pid),'raw_score':round(raw,2),'confidence_adjusted_score':round(adjusted,2),'hard_gate_failed':gate})
    ranked=sorted(results,key=lambda x:(x['hard_gate_failed'],-x['confidence_adjusted_score']))
    for idx,item in enumerate(ranked,1): item['rank']=None if item['hard_gate_failed'] else idx
    print(json.dumps(ranked,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
