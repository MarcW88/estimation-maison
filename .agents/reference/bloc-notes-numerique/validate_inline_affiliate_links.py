#!/usr/bin/env python3
"""Validate generated inline Amazon CTAs for verified products."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parent
REGISTRY_PATH = ROOT / ".content" / "products" / "registry.json"
AFFILIATE_PATH = ROOT / ".content" / "products" / "affiliate.json"
INLINE_PATH = ROOT / ".content" / "products" / "inline-affiliate.json"

ROW_RE = re.compile(r"<tr\b[^>]*>.*?</tr>", re.S | re.I)
TD_RE = re.compile(r"<td\b[^>]*>(.*?)</td>", re.S | re.I)
TAG_RE = re.compile(r"<[^>]+>", re.S)
INLINE_LINK_RE = re.compile(
    r'<a\b[^>]*data-affiliate-link="amazon"[^>]*data-product-key="([^"]+)"[^>]*>',
    re.I,
)
HREF_RE = re.compile(r'href="([^"]+)"', re.I)
REL_RE = re.compile(r'rel="([^"]+)"', re.I)
INLINE_PRODUCT_RE = re.compile(r'data-inline-affiliate-product="([^"]+)"', re.I)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def clean_text(value: str) -> str:
    value = TAG_RE.sub(" ", value)
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def expected_url(product: dict, affiliate: dict) -> str:
    asin = (product.get("amazon", {}).get("asin") or "").strip()
    if not asin:
        return ""
    tracking_id = affiliate["amazon_fr"]["tracking_id"]
    base_url = affiliate["amazon_fr"]["base_url"].rstrip("/")
    return f"{base_url}/dp/{asin}/ref=nosim?tag={tracking_id}"


def find_product_for_row(row_html: str, configs: dict[str, dict]) -> str | None:
    cells = [clean_text(cell) for cell in TD_RE.findall(row_html)]
    for product_id, config in configs.items():
        aliases = set(config.get("row_aliases", []))
        if any(cell in aliases for cell in cells):
            return product_id
    return None


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def validate_link(tag: str, product_id: str, products: dict[str, dict], affiliate: dict, page: Path) -> None:
    if product_id not in products:
        fail(f"{page.relative_to(ROOT)}: unknown product key {product_id}")
    href_match = HREF_RE.search(tag)
    if not href_match:
        fail(f"{page.relative_to(ROOT)}: Amazon CTA without href")
    href = html.unescape(href_match.group(1))
    expected = expected_url(products[product_id], affiliate)
    if not expected or href != expected:
        fail(f"{page.relative_to(ROOT)}: wrong Amazon URL for {product_id}")

    parsed = urlsplit(href)
    expected_tag = affiliate["amazon_fr"]["tracking_id"]
    actual_tag = parse_qs(parsed.query).get("tag", [""])[0]
    if actual_tag != expected_tag:
        fail(f"{page.relative_to(ROOT)}: wrong tracking id for {product_id}")

    rel_match = REL_RE.search(tag)
    rel_tokens = set((rel_match.group(1) if rel_match else "").lower().split())
    required = {"sponsored", "nofollow", "noopener", "noreferrer"}
    if not required.issubset(rel_tokens):
        fail(f"{page.relative_to(ROOT)}: missing required rel tokens for {product_id}")


def main() -> None:
    products = load_json(REGISTRY_PATH)["products"]
    affiliate = load_json(AFFILIATE_PATH)
    config = load_json(INLINE_PATH)
    configs = config["products"]

    total_links = 0
    subject_expected = {
        (path, product_id)
        for product_id, product_config in configs.items()
        for path in product_config.get("subject_paths", [])
        if expected_url(products.get(product_id, {}), affiliate)
    }

    seen_subjects: set[tuple[str, str]] = set()
    for root_name in config.get("roots", []):
        root = ROOT / root_name
        if not root.exists():
            continue
        for page in sorted(root.glob("**/index.html")):
            page_path = page.relative_to(ROOT).as_posix()
            text = page.read_text(encoding="utf-8")

            for tag_match in INLINE_LINK_RE.finditer(text):
                product_id = tag_match.group(1)
                validate_link(tag_match.group(0), product_id, products, affiliate, page)
                total_links += 1

            for product_id in INLINE_PRODUCT_RE.findall(text):
                if (page_path, product_id) in subject_expected:
                    seen_subjects.add((page_path, product_id))

            subject_products = {
                product_id
                for product_id, product_config in configs.items()
                if page_path in product_config.get("subject_paths", [])
            }
            for row in ROW_RE.findall(text):
                product_id = find_product_for_row(row, configs)
                if not product_id or product_id in subject_products:
                    continue
                if not expected_url(products.get(product_id, {}), affiliate):
                    continue
                if f'data-inline-affiliate-product="{product_id}"' not in row:
                    fail(f"{page_path}: missing inline CTA in row for {product_id}")

    missing_subjects = sorted(subject_expected - seen_subjects)
    if missing_subjects:
        rendered = ", ".join(f"{path}:{product_id}" for path, product_id in missing_subjects)
        fail(f"missing subject-page CTA(s): {rendered}")

    if total_links == 0:
        fail("no inline Amazon CTAs found")

    print(f"PASS: {total_links} inline Amazon CTA(s) use verified ASINs and tracking id {affiliate['amazon_fr']['tracking_id']}")
    print("PASS: configured subject pages and matching product table rows carry inline CTAs")


if __name__ == "__main__":
    main()
