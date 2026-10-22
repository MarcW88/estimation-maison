#!/usr/bin/env python3
"""Machine guards for conservative product modules on aspirateurs-chantier."""

from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parent
REGISTRY = ROOT / ".content/products/registry.json"
PLACEMENTS = ROOT / ".content/products/placements.json"
AFFILIATE = ROOT / ".content/products/affiliate.json"
EXPECTED_SCOPE = {
    "comparisons": {
        "meilleur-aspirateur-de-chantier", "aspirateur-classe-m", "aspirateur-chantier-sans-fil",
        "aspirateur-eau-poussiere", "aspirateur-chantier-sans-sac", "aspirateur-chantier-puissant",
        "aspirateur-professionnel", "petit-aspirateur-de-chantier"
    },
    "usages": {
        "aspirateur-ponceuse", "aspirateur-platre", "aspirateur-scie",
        "aspirateur-bricolage-renovation", "aspirateur-gravats"
    },
    "guides": {"comment-choisir-aspirateur-de-chantier"},
}
PROHIBITED_MODULE_ROOTS = {"marques", "modeles", "accessoires"}
ALLOWED_IMAGE_SOURCES = {"UNSET", "OWN", "MANUFACTURER_AUTHORIZED", "AMAZON_CREATORS_API"}
FORBIDDEN_COMMERCE_KEYS = {"price", "current_price", "reference_price", "discount", "discount_pct", "stock"}
ASIN_RE = re.compile(r"^[A-Z0-9]{10}$")
STYLE_TAG = '<link rel="stylesheet" href="/style.css">'
SCRIPT_TAG = '<script src="/assets/product-affiliate.js" defer></script>'


def fail(msg: str) -> None:
    raise SystemExit(f"FAIL: {msg}")


def walk_keys(value):
    if isinstance(value, dict):
        for key, child in value.items():
            yield key
            yield from walk_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_keys(child)


def has_amazon(product: dict) -> bool:
    amazon = product.get("amazon", {})
    return bool((amazon.get("asin") or "").strip() or (amazon.get("affiliate_url") or "").strip())


def validate_registry(data: dict, affiliate: dict) -> dict[str, dict]:
    forbidden = FORBIDDEN_COMMERCE_KEYS & set(walk_keys(data))
    if forbidden:
        fail("static commerce data forbidden: " + ", ".join(sorted(forbidden)))
    products = data.get("products", {})
    cfg = affiliate.get("amazon_fr", {})
    tracking = (cfg.get("tracking_id") or "").strip()
    base = urlsplit((cfg.get("base_url") or "").strip())
    if not tracking or base.scheme != "https" or base.hostname not in {"amazon.fr", "www.amazon.fr"}:
        fail("invalid Amazon.fr affiliate configuration")
    for pid, product in products.items():
        for key in ("name", "internal_url", "image", "amazon", "specs", "best_for"):
            if key not in product:
                fail(f"{pid}: missing {key}")
        if not product["internal_url"].startswith("/"):
            fail(f"{pid}: internal_url must be site-relative")
        if not 1 <= len(product["specs"]) <= 5:
            fail(f"{pid}: keep 1 to 5 specs")
        image = product["image"]
        if image.get("source_type") not in ALLOWED_IMAGE_SOURCES:
            fail(f"{pid}: invalid image source")
        if (image.get("url") or "").strip() and image.get("source_type") == "UNSET":
            fail(f"{pid}: image URL without provenance")
        if image.get("source_type") == "MANUFACTURER_AUTHORIZED" and image.get("url") and not image.get("rights_checked"):
            fail(f"{pid}: manufacturer image rights not checked")
        asin = (product["amazon"].get("asin") or "").strip()
        if asin and not ASIN_RE.fullmatch(asin):
            fail(f"{pid}: invalid ASIN {asin}")
        override = (product["amazon"].get("affiliate_url") or "").strip()
        if override:
            parsed = urlsplit(override)
            if parsed.scheme != "https" or parsed.hostname not in {"amazon.fr", "www.amazon.fr"}:
                fail(f"{pid}: unsupported affiliate URL")
            if parse_qs(parsed.query).get("tag") != [tracking]:
                fail(f"{pid}: wrong tracking id")
    return products


def validate_config(data: dict, products: dict[str, dict]) -> None:
    policy = data.get("policy", {})
    if policy.get("max_modules_per_page") != 1 or policy.get("max_products_per_module") != 3:
        fail("module caps must remain 1 module / 3 products")
    if policy.get("purpose") != "decision_support_only":
        fail("purpose must remain decision_support_only")
    required_exclusions = {"brands", "industrial", "hubs", "accessories", "technical_guides"}
    if not required_exclusions.issubset(set(policy.get("excluded_sections", []))):
        fail("anti-overoptimization exclusions were weakened")
    sections = data.get("sections", {})
    if set(sections) != set(EXPECTED_SCOPE):
        fail("placement sections changed without validator update")
    total = 0
    for section, expected in EXPECTED_SCOPE.items():
        pages = sections[section].get("pages", {})
        if set(pages) != expected:
            fail(f"{section}: placement scope changed without validator update")
        total += len(pages)
        for slug, config in pages.items():
            ids = config.get("products", [])
            if config.get("layout") != "recommendation_list" or not 2 <= len(ids) <= 3:
                fail(f"{section}/{slug}: expected a 2-3 product recommendation list")
            if len(ids) != len(set(ids)):
                fail(f"{section}/{slug}: duplicate product")
            unknown = [pid for pid in ids if pid not in products]
            if unknown:
                fail(f"{section}/{slug}: unknown products {unknown}")
            if not config.get("insert_before_heading_id") or not config.get("section_id"):
                fail(f"{section}/{slug}: insertion IDs required")
    if total != 14:
        fail(f"approved scope must remain 14 pages, got {total}")


def validate_prohibited_roots() -> None:
    for root_name in PROHIBITED_MODULE_ROOTS:
        root = ROOT / root_name
        if not root.exists():
            continue
        for page in root.glob("**/index.html"):
            if 'data-product-module="true"' in page.read_text(encoding="utf-8"):
                fail(f"product module forbidden under {root_name}: {page.relative_to(ROOT)}")


def validate_rendered(section: str, placements: dict, products: dict[str, dict], affiliate: dict) -> None:
    config = placements["sections"][section]
    base = ROOT / config["base_path"]
    expected = config["pages"]
    found = set()
    for page in base.glob("*/index.html"):
        text = page.read_text(encoding="utf-8")
        if 'data-product-module="true"' in text:
            found.add(page.parent.name)
    if found != set(expected):
        fail(f"{section}: rendered scope mismatch; expected {sorted(expected)}, got {sorted(found)}")
    tracking = affiliate["amazon_fr"]["tracking_id"]
    for slug, page_cfg in expected.items():
        page = base / slug / "index.html"
        text = page.read_text(encoding="utf-8")
        if text.count(f'<!-- PRODUCT_MODULE:{section}:{slug}:START -->') != 1:
            fail(f"{section}/{slug}: start marker missing/duplicated")
        if text.count('data-product-module="true"') != 1:
            fail(f"{section}/{slug}: exactly one module required")
        if STYLE_TAG not in text or SCRIPT_TAG not in text:
            fail(f"{section}/{slug}: product assets missing")
        if text.count('class="product-recommendation-row"') != len(page_cfg["products"]):
            fail(f"{section}/{slug}: product count mismatch")
        expected_aff = sum(1 for pid in page_cfg["products"] if has_amazon(products[pid]))
        tags = re.findall(r'<a\b[^>]*data-affiliate-link="amazon"[^>]*>', text, re.I)
        if len(tags) != expected_aff:
            fail(f"{section}/{slug}: expected {expected_aff} Amazon CTAs, got {len(tags)}")
        for tag in tags:
            rel = re.search(r'rel="([^"]+)"', tag, re.I)
            if not {"sponsored", "nofollow", "noopener", "noreferrer"}.issubset(set((rel.group(1) if rel else "").lower().split())):
                fail(f"{section}/{slug}: missing rel tokens")
            href = re.search(r'href="([^"]+)"', tag, re.I)
            url = html.unescape(href.group(1) if href else "")
            if parse_qs(urlsplit(url).query).get("tag") != [tracking]:
                fail(f"{section}/{slug}: wrong tracking id")


def main() -> None:
    requested = sys.argv[1] if len(sys.argv) > 1 else "all"
    if requested == "all":
        sections = list(EXPECTED_SCOPE)
    elif requested in EXPECTED_SCOPE:
        sections = [requested]
    else:
        fail("usage: validate_product_cards.py [comparisons|usages|guides|all]")
    registry_data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    placements = json.loads(PLACEMENTS.read_text(encoding="utf-8"))
    affiliate = json.loads(AFFILIATE.read_text(encoding="utf-8"))
    products = validate_registry(registry_data, affiliate)
    validate_config(placements, products)
    validate_prohibited_roots()
    for section in sections:
        validate_rendered(section, placements, products, affiliate)
    print(f"PASS: guarded product modules validated for {', '.join(sections)}")
    print("PASS: scope capped at 14 decision-support pages; no static prices or unverified Amazon links")


if __name__ == "__main__":
    main()
