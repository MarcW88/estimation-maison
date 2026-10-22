#!/usr/bin/env python3
"""Add one Amazon CTA to configured exact model pages with verified ASINs."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REGISTRY = ROOT / ".content/products/registry.json"
AFFILIATE = ROOT / ".content/products/affiliate.json"
INLINE = ROOT / ".content/products/inline-affiliate.json"
SCRIPT_TAG = '<script src="/assets/product-affiliate.js" defer></script>'
GENERATED_RE = re.compile(r'[ \t\r\n]*<!-- INLINE_AFFILIATE:[^>]+:START -->.*?<!-- INLINE_AFFILIATE:[^>]+:END -->[ \t\r\n]*', re.S)
ANSWER_BOX_RE = re.compile(r'(<div\b[^>]*class="[^"]*answer-box[^"]*"[^>]*>.*?</div>)', re.S | re.I)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def affiliate_url(product: dict, affiliate: dict) -> str:
    asin = (product.get("amazon", {}).get("asin") or "").strip()
    if not asin:
        return ""
    cfg = affiliate["amazon_fr"]
    return f"{cfg['base_url'].rstrip('/')}/dp/{asin}/ref=nosim?tag={cfg['tracking_id']}"


def ensure_asset(text: str, tag: str, before: str) -> str:
    if tag in text:
        return text
    if before not in text:
        raise SystemExit(f"Could not place asset tag before {before}")
    return text.replace(before, f"  {tag}\n{before}", 1)


def render(product_id: str, product: dict, affiliate: dict, page_path: str) -> str:
    url = affiliate_url(product, affiliate)
    if not url:
        return ""
    return (
        f'<!-- INLINE_AFFILIATE:{product_id}:SUBJECT:START -->\n'
        f'<div class="inline-affiliate-action" data-inline-affiliate-product="{html.escape(product_id)}">'
        f'<a class="product-card__cta" href="{html.escape(url, quote=True)}" target="_blank" '
        'rel="sponsored nofollow noopener noreferrer" data-affiliate-link="amazon" '
        f'data-product-key="{html.escape(product_id)}" data-placement="inline-model:{html.escape(page_path)}">'
        'Voir le prix sur Amazon →</a>'
        '<span class="product-card__disclosure">Lien rémunéré</span>'
        '</div>\n'
        f'<!-- INLINE_AFFILIATE:{product_id}:SUBJECT:END -->'
    )


def main() -> None:
    products = load(REGISTRY)["products"]
    affiliate = load(AFFILIATE)
    config = load(INLINE)
    expected_paths = {path: pid for pid, cfg in config["products"].items() for path in cfg.get("subject_paths", [])}
    changed = 0
    inserted = 0
    for root_name in config.get("roots", []):
        root = ROOT / root_name
        if not root.exists():
            continue
        for page in sorted(root.glob("**/index.html")):
            page_path = page.relative_to(ROOT).as_posix()
            original = page.read_text(encoding="utf-8")
            text = GENERATED_RE.sub("\n", original)
            pid = expected_paths.get(page_path)
            if pid:
                product = products.get(pid)
                if not product:
                    raise SystemExit(f"Unknown configured product: {pid}")
                block = render(pid, product, affiliate, page_path)
                if block:
                    match = ANSWER_BOX_RE.search(text)
                    if not match:
                        raise SystemExit(f"No answer-box found on {page_path}")
                    before = text[:match.end()].rstrip()
                    after = text[match.end():].lstrip("\r\n")
                    text = before + "\n" + block + "\n" + after
                    # CSS is provided by the sitewide /style.css entry point.
                    text = ensure_asset(text, SCRIPT_TAG, "</body>")
                    inserted += 1
            if text != original:
                page.write_text(text, encoding="utf-8")
                changed += 1
                print(f"inline affiliate maintained: {page_path}")
    print(f"Inline affiliate pass: {inserted} CTA(s) across {changed} changed page(s)")


if __name__ == "__main__":
    main()
