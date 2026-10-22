#!/usr/bin/env python3
"""
Score a comparison YAML-like JSON file exported as JSON.

Input schema mirrors references/comparison-data-template.yaml.
For portability this script uses JSON in execution:
python score_comparison.py comparison.json

The YAML template is intended for human editing. Convert YAML to JSON in your
runtime if PyYAML is unavailable.
"""
from pathlib import Path
import json
import sys

CONFIDENCE = {
    "VERIFIED": 1.00,
    "FIRST_HAND": 1.00,
    "SUPPORTED": 0.95,
    "INFERRED": 0.85,
    "USER_PATTERN": 0.80,
}

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: score_comparison.py comparison.json")

    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))

    criteria = data["criteria"]
    products = {p["id"]: p for p in data["product_universe"]}

    weight_sum = sum(c["weight"] for c in criteria)
    if weight_sum != 100:
        raise SystemExit(f"FAIL: weights sum to {weight_sum}, expected 100")

    criterion_map = {c["id"]: c for c in criteria}
    results = []

    for product_id, score_map in data["scores"].items():
        product = products.get(product_id)
        if not product:
            raise SystemExit(f"FAIL: unknown product {product_id}")

        if product.get("status") not in {"ELIGIBLE", "CONDITIONALLY_ELIGIBLE"}:
            continue

        raw_total = 0.0
        adjusted_total = 0.0
        hard_gate_failed = False

        for cid, criterion in criterion_map.items():
            if cid not in score_map:
                raise SystemExit(f"FAIL: missing score for {product_id}/{cid}")

            entry = score_map[cid]
            score = float(entry["score"])
            if not 0 <= score <= 10:
                raise SystemExit(f"FAIL: score outside 0-10 for {product_id}/{cid}")

            evidence_class = entry.get("evidence_class", "UNKNOWN")
            if evidence_class not in CONFIDENCE:
                raise SystemExit(
                    f"FAIL: invalid or unknown evidence class for {product_id}/{cid}: "
                    f"{evidence_class}"
                )

            if not entry.get("justification", "").strip():
                raise SystemExit(f"FAIL: missing justification for {product_id}/{cid}")

            weight = float(criterion["weight"])
            raw_total += (score * weight) / 10
            adjusted_total += (score * CONFIDENCE[evidence_class] * weight) / 10

            if criterion.get("hard_gate") and score < float(criterion.get("hard_gate_min", 5)):
                hard_gate_failed = True

        results.append({
            "product_id": product_id,
            "name": product.get("name", product_id),
            "raw_score": round(raw_total, 2),
            "confidence_adjusted_score": round(adjusted_total, 2),
            "hard_gate_failed": hard_gate_failed,
        })

    ranked = sorted(
        results,
        key=lambda x: (x["hard_gate_failed"], -x["confidence_adjusted_score"])
    )

    for idx, item in enumerate(ranked, start=1):
        item["rank"] = None if item["hard_gate_failed"] else idx

    print(json.dumps(ranked, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
