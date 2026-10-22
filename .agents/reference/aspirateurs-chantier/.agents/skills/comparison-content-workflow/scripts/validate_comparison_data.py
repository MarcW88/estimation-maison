#!/usr/bin/env python3
"""Validate comparison JSON structure without imposing a scoring methodology.

This validator checks integrity of the fields that are actually present. Editorial
quality and recommendation validity remain the responsibility of
comparison-analysis-workflow / PUBLISH_REVIEW.
"""
from pathlib import Path
import json
import sys

ALLOWED_EVIDENCE = {
    "VERIFIED", "SUPPORTED", "INFERRED", "USER_PATTERN",
    "FIRST_HAND", "UNKNOWN", "PROHIBITED"
}
ALLOWED_STATUS = {
    "ELIGIBLE", "CONDITIONALLY_ELIGIBLE", "OUTDATED",
    "NOT_COMPARABLE", "EXCLUDED"
}


def fail(msg):
    print("FAIL:", msg)
    raise SystemExit(1)


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: validate_comparison_data.py comparison.json")

    path = Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8"))

    intent = data.get("intent", {})
    if not intent.get("query"):
        fail("missing intent.query")

    products = data.get("product_universe")
    if products is None:
        products = data.get("scope", {}).get("candidates", [])
    if products and len(products) < 2:
        fail("comparison scope contains fewer than 2 candidates")

    for product in products or []:
        status = product.get("status")
        if status and status not in ALLOWED_STATUS:
            fail(f"invalid product status: {product.get('id')}")
        if status in {"OUTDATED", "NOT_COMPARABLE", "EXCLUDED"} and not product.get("exclusion_reason"):
            # Newer method-neutral files may document exclusions centrally.
            central = data.get("scope", {}).get("major_exclusions", [])
            if not central:
                fail(f"excluded product missing reason: {product.get('id')}")

    criteria = data.get("criteria", [])
    ids = [criterion.get("id") for criterion in criteria if criterion.get("id")]
    if len(ids) != len(set(ids)):
        fail("duplicate criterion ids")

    for evidence in data.get("evidence", []):
        evidence_class = evidence.get("evidence_class")
        if evidence_class and evidence_class not in ALLOWED_EVIDENCE:
            fail(f"invalid evidence class: {evidence_class}")

    notes = data.get("notes", {})
    if "affiliate_commission_used_in_ranking" in notes and notes["affiliate_commission_used_in_ranking"] is not False:
        fail("affiliate commission must not be used in recommendation/ranking")

    # Scoring is optional. If a page deliberately uses it, validate its internal
    # consistency without requiring every comparison to have scores or weights.
    scores = data.get("scores")
    if scores:
        if not criteria:
            fail("scores present without criteria")
        eligible_ids = {
            p.get("id") for p in (products or [])
            if p.get("id") and p.get("status", "ELIGIBLE") in {"ELIGIBLE", "CONDITIONALLY_ELIGIBLE"}
        }
        for product_id, product_scores in scores.items():
            if eligible_ids and product_id not in eligible_ids:
                fail(f"scores reference unknown/non-eligible product: {product_id}")
            for criterion_id, entry in product_scores.items():
                if ids and criterion_id not in ids:
                    fail(f"score references unknown criterion: {product_id}/{criterion_id}")
                evidence_class = entry.get("evidence_class") if isinstance(entry, dict) else None
                if evidence_class and evidence_class not in ALLOWED_EVIDENCE:
                    fail(f"invalid score evidence class: {product_id}/{criterion_id}")

    # Support both legacy criterion-level weights and newer top-level weights.
    legacy_weights = [c.get("weight") for c in criteria if c.get("weight") is not None]
    top_weights = data.get("weights")
    if legacy_weights and len(legacy_weights) != len(criteria):
        fail("partial criterion weighting: either weight all criteria or none")
    if legacy_weights and sum(legacy_weights) != 100:
        fail(f"explicit criterion weights sum to {sum(legacy_weights)}, expected 100")
    if isinstance(top_weights, dict) and top_weights and sum(top_weights.values()) != 100:
        fail(f"explicit weights sum to {sum(top_weights.values())}, expected 100")

    print("PASS: comparison data is structurally valid; scoring remains optional")


if __name__ == "__main__":
    main()
