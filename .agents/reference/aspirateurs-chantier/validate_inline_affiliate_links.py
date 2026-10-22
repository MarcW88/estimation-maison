#!/usr/bin/env python3
"""Validate exact-model Amazon CTAs generated only from verified ASINs."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parent
REGISTRY = ROOT / ".content/products/registry.json"
AFFILIATE = ROOT / ".content/products/affiliate.json"
INLINE = ROOT / ".content/products/inline-affiliate.json"
LINK_RE = re.compile(r'<a\b[^>]*data-affiliate-link="amazon"[^>]*data-product-key="([^"]+)"[^>]*>', re.I)
HREF_RE = re.compile(r'href="([^"]+)"', re.I)
REL_RE = re.compile(r'rel="([^"]+)"', re.I)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def fail(msg: str) -> None:
    raise SystemExit(f"FAIL: {msg}")


def expected_url(product: dict, affiliate: dict) -> str:
    asin = (product.get("amazon", {}).get("asin") or "").strip()
    if not asin:
        return ""
    cfg = affiliate["amazon_fr"]
    return f"{cfg['base_url'].rstrip('/')}/dp/{asin}/ref=nosim?tag={cfg['tracking_id']}"


def main() -> None:
    products = load(REGISTRY)["products"]
    affiliate = load(AFFILIATE)
    config = load(INLINE)
    expected = {(path, pid) for pid, cfg in config["products"].items() for path in cfg.get("subject_paths", [])}
    seen = set()
    total = 0
    for root_name in config.get("roots", []):
        root = ROOT / root_name
        if not root.exists():
            continue
        for page in sorted(root.glob("**/index.html")):
            page_path = page.relative_to(ROOT).as_posix()
            text = page.read_text(encoding="utf-8")
            matches = list(LINK_RE.finditer(text))
            if page_path not in {p for p, _ in expected} and 'data-inline-affiliate-product=' in text:
                fail(f"unapproved inline CTA on {page_path}")
            for match in matches:
                pid = match.group(1)
                if (page_path, pid) not in expected:
                    fail(f"unexpected product CTA {pid} on {page_path}")
                product = products.get(pid)
                if not product:
                    fail(f"unknown product {pid}")
                expected_href = expected_url(product, affiliate)
                if not expected_href:
                    fail(f"{pid}: subject CTA configured without verified ASIN")
                tag = match.group(0)
                href_match = HREF_RE.search(tag)
                href = html.unescape(href_match.group(1) if href_match else "")
                if href != expected_href:
                    fail(f"{page_path}: wrong Amazon URL for {pid}")
                rel = REL_RE.search(tag)
                if not {"sponsored", "nofollow", "noopener", "noreferrer"}.issubset(set((rel.group(1) if rel else "").lower().split())):
                    fail(f"{page_path}: missing rel tokens")
                if parse_qs(urlsplit(href).query).get("tag") != [affiliate["amazon_fr"]["tracking_id"]]:
                    fail(f"{page_path}: wrong tracking id")
                seen.add((page_path, pid))
                total += 1
    if seen != expected:
        fail(f"missing configured exact-model CTA(s): {sorted(expected - seen)}")
    if total != 7:
        fail(f"expected 7 verified exact-model CTAs, got {total}")
    print(f"PASS: {total} exact-model Amazon CTA(s) use verified ASINs and tracking id {affiliate['amazon_fr']['tracking_id']}")


if __name__ == "__main__":
    main()
