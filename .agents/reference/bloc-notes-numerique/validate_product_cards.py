#!/usr/bin/env python3
"""Machine guards for conservative editorial product modules."""

from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parent
REGISTRY = ROOT / ".content" / "products" / "registry.json"
PLACEMENTS = ROOT / ".content" / "products" / "placements.json"
AFFILIATE_CONFIG = ROOT / ".content" / "products" / "affiliate.json"
EXPECTED_SCOPE = {
    "comparisons": {
        "meilleur-bloc-notes-numerique",
        "tablette-e-ink",
        "bloc-notes-numerique-professionnel",
        "bloc-notes-numerique-etudiant",
        "bloc-notes-numerique-couleur",
        "bloc-notes-numerique-a4",
        "bloc-notes-numerique-sans-abonnement",
        "bloc-notes-numerique-pas-cher",
        "kindle-scribe-vs-remarkable",
        "kindle-scribe-vs-kobo-elipsa",
        "remarkable-vs-boox",
        "remarkable-vs-supernote",
        "boox-vs-supernote",
        "kobo-elipsa-vs-remarkable",
    },
    "usages": {
        "prise-de-notes-professionnelle",
        "prise-de-notes-etudiant",
        "lecture-et-prise-de-notes",
    },
    "guides": {
        "choisir-bloc-notes-numerique",
        "annoter-pdf-tablette-e-ink",
    },
}
PROHIBITED_MODULE_ROOTS = {"marques", "bons-plans"}
ALLOWED_IMAGE_SOURCES = {"UNSET", "OWN", "MANUFACTURER_AUTHORIZED", "AMAZON_CREATORS_API"}
ALLOWED_AFFILIATE_HOSTS = {"amazon.fr", "www.amazon.fr", "amazon.com.be", "www.amazon.com.be"}
FORBIDDEN_COMMERCE_KEYS = {"price", "current_price", "reference_price", "discount", "discount_pct"}
STYLE_TAG = '<link rel="stylesheet" href="/assets/product-cards.css">'
SCRIPT_TAG = '<script src="/assets/product-affiliate.js" defer></script>'
ASIN_RE = re.compile(r"^[A-Z0-9]{10}$")


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def walk_keys(value):
    if isinstance(value, dict):
        for key, child in value.items():
            yield key
            yield from walk_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_keys(child)


def has_amazon_link(product: dict) -> bool:
    amazon = product.get("amazon", {})
    return bool((amazon.get("asin") or "").strip() or (amazon.get("affiliate_url") or "").strip())


def validate_registry(registry_data: dict, affiliate_data: dict) -> dict[str, dict]:
    products = registry_data.get("products", {})
    forbidden = FORBIDDEN_COMMERCE_KEYS & set(walk_keys(registry_data))
    if forbidden:
        fail("static commerce data is forbidden in product registry: " + ", ".join(sorted(forbidden)))

    amazon_config = affiliate_data.get("amazon_fr", {})
    tracking_id = (amazon_config.get("tracking_id") or "").strip()
    base_url = (amazon_config.get("base_url") or "").strip()
    parsed_base = urlsplit(base_url)
    if not tracking_id:
        fail("Amazon.fr tracking_id is missing")
    if parsed_base.scheme != "https" or parsed_base.hostname not in {"amazon.fr", "www.amazon.fr"}:
        fail("Amazon.fr base_url must be an HTTPS amazon.fr URL")

    for product_id, product in products.items():
        for key in ("name", "internal_url", "image", "amazon", "specs", "best_for"):
            if key not in product:
                fail(f"{product_id}: missing {key}")
        if not product["internal_url"].startswith("/"):
            fail(f"{product_id}: internal_url must be site-relative")
        if not 1 <= len(product.get("specs", [])) <= 5:
            fail(f"{product_id}: keep 1 to 5 decision-useful specs")

        image = product["image"]
        source_type = image.get("source_type")
        image_url = (image.get("url") or "").strip()
        if source_type not in ALLOWED_IMAGE_SOURCES:
            fail(f"{product_id}: invalid image source {source_type}")
        if image_url and source_type == "UNSET":
            fail(f"{product_id}: image URL requires an explicit source type")
        if source_type == "MANUFACTURER_AUTHORIZED" and image_url and not image.get("rights_checked"):
            fail(f"{product_id}: manufacturer image requires rights_checked=true")
        if source_type == "AMAZON_CREATORS_API" and image_url and not image_url.startswith("https://"):
            fail(f"{product_id}: Creators API image must remain a remote HTTPS URL")

        amazon = product["amazon"]
        asin = (amazon.get("asin") or "").strip()
        if asin and not ASIN_RE.fullmatch(asin):
            fail(f"{product_id}: invalid Amazon ASIN {asin!r}")

        affiliate_url = (amazon.get("affiliate_url") or "").strip()
        if affiliate_url:
            parsed = urlsplit(affiliate_url)
            if parsed.scheme != "https" or parsed.hostname not in ALLOWED_AFFILIATE_HOSTS:
                fail(f"{product_id}: unsupported Amazon affiliate URL")
            if parse_qs(parsed.query).get("tag") != [tracking_id]:
                fail(f"{product_id}: Amazon affiliate URL must use tracking id {tracking_id}")
            if asin and f"/dp/{asin}" not in parsed.path:
                fail(f"{product_id}: affiliate URL does not match configured ASIN {asin}")
    return products


def validate_policy(placements_data: dict) -> None:
    policy = placements_data.get("policy", {})
    if policy.get("max_modules_per_page") != 1:
        fail("product policy must keep max_modules_per_page at 1")
    if policy.get("max_products_per_module") != 3:
        fail("product policy must keep max_products_per_module at 3")
    if policy.get("purpose") != "decision_support_only":
        fail("product modules must remain decision-support only")
    excluded = set(policy.get("excluded_sections", []))
    required = {"brands", "deals", "hubs", "informational_guides"}
    if not required.issubset(excluded):
        fail("anti-overoptimization exclusions were weakened")


def validate_config(placements_data: dict, products: dict[str, dict]) -> None:
    sections = placements_data.get("sections", {})
    if set(sections) != set(EXPECTED_SCOPE):
        fail("product-placement sections changed without explicit validator update")

    total_pages = 0
    for section, expected_slugs in EXPECTED_SCOPE.items():
        section_config = sections[section]
        pages = section_config.get("pages", {})
        if set(pages) != expected_slugs:
            fail(f"{section}: placement scope changed without explicit validator update")
        total_pages += len(pages)

        for slug, config in pages.items():
            layout = config.get("layout")
            configured_products = config.get("products", [])
            if layout == "comparison_cards" and len(configured_products) != 2:
                fail(f"{section}/{slug}: comparison_cards requires exactly 2 products")
            if layout == "recommendation_list" and not 2 <= len(configured_products) <= 3:
                fail(f"{section}/{slug}: recommendation_list requires 2 or 3 products")
            if layout not in {"comparison_cards", "recommendation_list"}:
                fail(f"{section}/{slug}: unsupported layout {layout}")
            if len(configured_products) != len(set(configured_products)):
                fail(f"{section}/{slug}: duplicate product in one module")
            unknown = [pid for pid in configured_products if pid not in products]
            if unknown:
                fail(f"{section}/{slug}: unknown products: {', '.join(unknown)}")
            if not config.get("insert_before_heading_id") or not config.get("section_id"):
                fail(f"{section}/{slug}: insertion and section IDs are required")

    if total_pages != 19:
        fail(f"approved product-module scope must remain 19 pages, got {total_pages}")


def validate_rendered_section(
    section: str,
    placements_data: dict,
    products: dict[str, dict],
    affiliate_data: dict,
) -> None:
    section_config = placements_data["sections"][section]
    base_path = section_config["base_path"]
    expected_pages = section_config["pages"]
    tracking_id = affiliate_data["amazon_fr"]["tracking_id"]

    found = set()
    for page in sorted((ROOT / base_path).glob("*/index.html")):
        text = page.read_text(encoding="utf-8")
        slug = page.parent.name
        if 'data-product-module="true"' not in text and 'data-product-pilot="true"' not in text:
            continue
        found.add(slug)
        if slug not in expected_pages:
            fail(f"{section}: product module leaked onto unapproved page {slug}")

    if found != set(expected_pages):
        missing = sorted(set(expected_pages) - found)
        extra = sorted(found - set(expected_pages))
        if missing:
            fail(f"{section}: product modules missing on: {', '.join(missing)}")
        if extra:
            fail(f"{section}: unexpected product modules on: {', '.join(extra)}")

    for slug, config in expected_pages.items():
        page = ROOT / base_path / slug / "index.html"
        text = page.read_text(encoding="utf-8")
        layout = config["layout"]
        expected_count = len(config["products"])
        start = f'<!-- PRODUCT_MODULE:{section}:{slug}:START -->'
        end = f'<!-- PRODUCT_MODULE:{section}:{slug}:END -->'

        if text.count(start) != 1 or text.count(end) != 1:
            fail(f"{section}/{slug}: generic product-module markers missing or duplicated")
        if 'data-product-pilot="true"' in text or '<!-- PRODUCT_PILOT:' in text:
            fail(f"{section}/{slug}: legacy product-pilot markup remains")
        if text.count('data-product-module="true"') != 1:
            fail(f"{section}/{slug}: exactly one product module is allowed per page")
        if text.count(f'data-product-layout="{layout}"') != 1:
            fail(f"{section}/{slug}: rendered layout marker mismatch")
        if STYLE_TAG not in text or SCRIPT_TAG not in text:
            fail(f"{section}/{slug}: product assets missing")

        if layout == "recommendation_list":
            if text.count('class="product-recommendation-list"') != 1:
                fail(f"{section}/{slug}: recommendation list wrapper missing")
            if text.count('class="product-recommendation-row"') != expected_count:
                fail(f"{section}/{slug}: recommendation-row count mismatch")
            if 'product-card-grid--3' in text:
                fail(f"{section}/{slug}: three-card grid regression detected")
        else:
            if text.count('class="product-card-grid product-card-grid--2"') != 1:
                fail(f"{section}/{slug}: two-card comparison grid missing")
            if text.count('class="product-card"') != 2:
                fail(f"{section}/{slug}: product-card count mismatch")
            if 'product-recommendation-list' in text:
                fail(f"{section}/{slug}: duel unexpectedly uses recommendation list")

        expected_affiliate_links = sum(1 for pid in config["products"] if has_amazon_link(products[pid]))
        actual_affiliate_links = text.count('data-affiliate-link="amazon"')
        if actual_affiliate_links != expected_affiliate_links:
            fail(f"{section}/{slug}: expected {expected_affiliate_links} Amazon CTAs, got {actual_affiliate_links}")
        for tag in re.findall(r'<a\b[^>]*data-affiliate-link="amazon"[^>]*>', text, re.I):
            rel = re.search(r'rel="([^"]+)"', tag, re.I)
            tokens = set((rel.group(1) if rel else "").lower().split())
            required = {"sponsored", "nofollow", "noopener", "noreferrer"}
            if not required.issubset(tokens):
                fail(f"{section}/{slug}: Amazon CTA missing required rel tokens")

            href = re.search(r'href="([^"]+)"', tag, re.I)
            if not href:
                fail(f"{section}/{slug}: Amazon CTA missing href")
            rendered_url = html.unescape(href.group(1))
            if parse_qs(urlsplit(rendered_url).query).get("tag") != [tracking_id]:
                fail(f"{section}/{slug}: Amazon CTA missing tracking id {tracking_id}")


def validate_prohibited_roots() -> None:
    for root_name in PROHIBITED_MODULE_ROOTS:
        root = ROOT / root_name
        for page in root.glob("**/index.html"):
            text = page.read_text(encoding="utf-8")
            if 'data-product-module="true"' in text or 'data-product-pilot="true"' in text:
                fail(f"product module forbidden under {root_name}: {page.relative_to(ROOT)}")


def main() -> None:
    requested = sys.argv[1] if len(sys.argv) > 1 else "comparisons"
    if requested == "all":
        sections_to_validate = list(EXPECTED_SCOPE)
    elif requested in EXPECTED_SCOPE:
        sections_to_validate = [requested]
    else:
        fail("usage: python validate_product_cards.py [comparisons|usages|guides|all]")

    registry_data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    placements_data = json.loads(PLACEMENTS.read_text(encoding="utf-8"))
    affiliate_data = json.loads(AFFILIATE_CONFIG.read_text(encoding="utf-8"))
    products = validate_registry(registry_data, affiliate_data)
    validate_policy(placements_data)
    validate_config(placements_data, products)
    validate_prohibited_roots()

    for section in sections_to_validate:
        validate_rendered_section(section, placements_data, products, affiliate_data)

    names = ", ".join(sections_to_validate)
    print(f"PASS: product modules validated for {names}")
    print("PASS: approved scope is capped at 19 decision-support pages")
    print("PASS: brands, deals, hubs and informational guides stay outside product-module scope")
    print("PASS: recommendation lists contain at most 3 products; duels contain exactly 2")
    print("PASS: no static Amazon prices are stored; affiliate CTAs remain conditional and sponsored")
    print(f"PASS: every Amazon CTA carries tracking id {affiliate_data['amazon_fr']['tracking_id']}")


if __name__ == "__main__":
    main()