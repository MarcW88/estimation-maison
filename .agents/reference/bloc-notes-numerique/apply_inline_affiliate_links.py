#!/usr/bin/env python3
"""Add conservative Amazon CTAs where a verified product is already present.

This complements the existing product modules. It only touches brand/deal pages,
adds one CTA on configured subject pages, and adds a compact CTA to table rows
whose cells clearly identify a verified product.
"""

from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REGISTRY_PATH = ROOT / ".content" / "products" / "registry.json"
AFFILIATE_PATH = ROOT / ".content" / "products" / "affiliate.json"
INLINE_PATH = ROOT / ".content" / "products" / "inline-affiliate.json"

STYLE_TAG = '<link rel="stylesheet" href="/assets/product-cards.css">'
INLINE_STYLE_TAG = '<link rel="stylesheet" href="/assets/inline-affiliate.css">'
SCRIPT_TAG = '<script src="/assets/product-affiliate.js" defer></script>'
GENERATED_RE = re.compile(
    r"\n?<!-- INLINE_AFFILIATE:[^>]+:START -->.*?<!-- INLINE_AFFILIATE:[^>]+:END -->\n?",
    re.S,
)
ROW_RE = re.compile(r"<tr\b[^>]*>.*?</tr>", re.S | re.I)
TD_RE = re.compile(r"<td\b[^>]*>(.*?)</td>", re.S | re.I)
TAG_RE = re.compile(r"<[^>]+>", re.S)
ARTICLE_ANSWER_RE = re.compile(
    r'(<p\b[^>]*class="[^"]*article-answer[^"]*"[^>]*>.*?</p>)', re.S | re.I
)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def clean_text(value: str) -> str:
    value = TAG_RE.sub(" ", value)
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def affiliate_url(product: dict, affiliate: dict) -> str:
    asin = (product.get("amazon", {}).get("asin") or "").strip()
    if not asin:
        return ""
    tracking_id = affiliate["amazon_fr"]["tracking_id"]
    base_url = affiliate["amazon_fr"]["base_url"].rstrip("/")
    return f"{base_url}/dp/{asin}/ref=nosim?tag={tracking_id}"


def marker(product_id: str, kind: str, body: str) -> str:
    return (
        f"<!-- INLINE_AFFILIATE:{product_id}:{kind}:START -->\n"
        f"{body}\n"
        f"<!-- INLINE_AFFILIATE:{product_id}:{kind}:END -->"
    )


def cta(product_id: str, product: dict, affiliate: dict, placement: str, table: bool = False) -> str:
    url = affiliate_url(product, affiliate)
    if not url:
        return ""
    wrapper = "inline-affiliate-action inline-affiliate-action--table" if table else "inline-affiliate-action"
    return (
        f'<div class="{wrapper}" data-inline-affiliate-product="{html.escape(product_id)}">'
        f'<a class="product-card__cta" href="{html.escape(url, quote=True)}" '
        'target="_blank" rel="sponsored nofollow noopener noreferrer" '
        f'data-affiliate-link="amazon" data-product-key="{html.escape(product_id)}" '
        f'data-placement="{html.escape(placement)}">Voir le prix sur Amazon →</a>'
        '<span class="product-card__disclosure">Lien rémunéré</span>'
        '</div>'
    )


def ensure_assets(page_html: str) -> str:
    if STYLE_TAG not in page_html:
        page_html = page_html.replace("</head>", f"  {STYLE_TAG}\n</head>", 1)
    if INLINE_STYLE_TAG not in page_html:
        page_html = page_html.replace("</head>", f"  {INLINE_STYLE_TAG}\n</head>", 1)
    if SCRIPT_TAG not in page_html:
        page_html = page_html.replace("</body>", f"{SCRIPT_TAG}\n</body>", 1)
    return page_html


def add_subject_cta(page_html: str, product_id: str, product: dict, affiliate: dict, page_path: str) -> tuple[str, bool]:
    block = cta(product_id, product, affiliate, f"inline-subject:{page_path}")
    if not block:
        return page_html, False
    match = ARTICLE_ANSWER_RE.search(page_html)
    if not match:
        return page_html, False
    rendered = marker(product_id, "SUBJECT", block)
    page_html = page_html[: match.end()] + "\n" + rendered + page_html[match.end() :]
    return page_html, True


def find_product_for_row(row_html: str, configs: dict[str, dict]) -> str | None:
    cells = [clean_text(cell) for cell in TD_RE.findall(row_html)]
    if not cells:
        return None
    for product_id, config in configs.items():
        aliases = set(config.get("row_aliases", []))
        if any(cell in aliases for cell in cells):
            return product_id
    return None


def add_row_ctas(page_html: str, configs: dict[str, dict], products: dict[str, dict], affiliate: dict, page_path: str, subject_products: set[str]) -> tuple[str, int]:
    count = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal count
        row = match.group(0)
        product_id = find_product_for_row(row, configs)
        if not product_id or product_id in subject_products:
            return row
        product = products.get(product_id)
        if not product or not affiliate_url(product, affiliate):
            return row
        cells = list(TD_RE.finditer(row))
        if not cells:
            return row
        last = cells[-1]
        block = cta(product_id, product, affiliate, f"inline-row:{page_path}", table=True)
        rendered = marker(product_id, "ROW", block)
        new_cell = last.group(0)
        new_cell = new_cell[:-5] + "\n" + rendered + "</td>"
        count += 1
        return row[: last.start()] + new_cell + row[last.end() :]

    return ROW_RE.sub(repl, page_html), count


def process_page(path: Path, configs: dict[str, dict], products: dict[str, dict], affiliate: dict) -> tuple[bool, int]:
    page_path = path.relative_to(ROOT).as_posix()
    original = path.read_text(encoding="utf-8")
    page_html = GENERATED_RE.sub("\n", original)

    subject_products = {
        product_id
        for product_id, config in configs.items()
        if page_path in config.get("subject_paths", [])
    }

    inserted = 0
    for product_id in sorted(subject_products):
        product = products.get(product_id)
        if not product or not affiliate_url(product, affiliate):
            continue
        page_html, changed = add_subject_cta(page_html, product_id, product, affiliate, page_path)
        inserted += int(changed)

    page_html, row_count = add_row_ctas(
        page_html, configs, products, affiliate, page_path, subject_products
    )
    inserted += row_count

    if inserted:
        page_html = ensure_assets(page_html)

    if page_html != original:
        path.write_text(page_html, encoding="utf-8")
        return True, inserted
    return False, inserted


def main() -> None:
    registry = load_json(REGISTRY_PATH)["products"]
    affiliate = load_json(AFFILIATE_PATH)
    config = load_json(INLINE_PATH)
    configs = config["products"]
    allowed_roots = config.get("roots", [])
    requested_roots = sys.argv[1:] or allowed_roots
    unknown_roots = sorted(set(requested_roots) - set(allowed_roots))
    if unknown_roots:
        raise SystemExit("Unknown inline-affiliate root(s): " + ", ".join(unknown_roots))

    changed_pages = 0
    total_ctas = 0
    for root_name in requested_roots:
        root = ROOT / root_name
        if not root.exists():
            continue
        for path in sorted(root.glob("**/index.html")):
            changed, inserted = process_page(path, configs, registry, affiliate)
            if changed:
                changed_pages += 1
                print(f"inline affiliate links applied: {path.relative_to(ROOT)} ({inserted} CTA(s))")
            total_ctas += inserted

    print(f"Inline affiliate pass: {total_ctas} CTA(s) across {changed_pages} changed page(s)")


if __name__ == "__main__":
    main()
