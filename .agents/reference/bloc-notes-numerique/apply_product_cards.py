#!/usr/bin/env python3
"""Apply conservative product-decision modules to explicitly approved editorial pages."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from product_cards import load_placements, load_registry, render_section

ROOT = Path(__file__).resolve().parent
STYLE_TAG = '<link rel="stylesheet" href="/assets/product-cards.css">'
SCRIPT_TAG = '<script src="/assets/product-affiliate.js" defer></script>'
ALLOWED_SECTIONS = {"comparisons", "usages", "guides"}


def strip_previous_block(text: str, section: str, slug: str) -> str:
    patterns = [
        re.compile(
            rf'\n?<!-- PRODUCT_MODULE:{re.escape(section)}:{re.escape(slug)}:START -->.*?'
            rf'<!-- PRODUCT_MODULE:{re.escape(section)}:{re.escape(slug)}:END -->\n?',
            re.S,
        ),
        re.compile(
            rf'\n?<!-- PRODUCT_PILOT:{re.escape(slug)}:START -->.*?'
            rf'<!-- PRODUCT_PILOT:{re.escape(slug)}:END -->\n?',
            re.S,
        ),
    ]
    for pattern in patterns:
        text = pattern.sub("\n", text)
    return text


def ensure_asset_tag(text: str, tag: str, before: str) -> str:
    if tag in text:
        return text
    if before not in text:
        raise SystemExit(f"Could not place asset tag before {before}")
    return text.replace(before, f"  {tag}\n{before}", 1)


def apply_page(section: str, base_path: str, slug: str, config: dict, registry: dict[str, dict]) -> None:
    page = ROOT / base_path / slug / "index.html"
    if not page.exists():
        raise SystemExit(f"Missing configured product-module page: {page}")

    text = page.read_text(encoding="utf-8")
    text = strip_previous_block(text, section, slug)
    text = ensure_asset_tag(text, STYLE_TAG, "</head>")
    text = ensure_asset_tag(text, SCRIPT_TAG, "</body>")

    missing = [product_id for product_id in config["products"] if product_id not in registry]
    if missing:
        raise SystemExit(f"{section}/{slug}: missing products in registry: {', '.join(missing)}")

    anchor_id = config["insert_before_heading_id"]
    anchor = re.search(rf'<h2\s+id="{re.escape(anchor_id)}"[^>]*>', text, re.I)
    if not anchor:
        raise SystemExit(f"{section}/{slug}: insertion heading #{anchor_id} not found")

    block = render_section(slug, config, registry, section=section)
    text = text[:anchor.start()] + block + "\n\n" + text[anchor.start():]
    page.write_text(text, encoding="utf-8")
    print(f"product module applied: {section}/{slug} ({len(config['products'])} products)")


def apply_section(section: str, registry: dict[str, dict]) -> None:
    section_config = load_placements(section)
    base_path = section_config["base_path"]
    for slug, config in section_config["pages"].items():
        apply_page(section, base_path, slug, config, registry)


def main() -> None:
    requested = sys.argv[1] if len(sys.argv) > 1 else "comparisons"
    registry = load_registry()

    if requested == "all":
        sections = ["comparisons", "usages", "guides"]
    elif requested in ALLOWED_SECTIONS:
        sections = [requested]
    else:
        raise SystemExit("Usage: python apply_product_cards.py [comparisons|usages|guides|all]")

    for section in sections:
        apply_section(section, registry)


if __name__ == "__main__":
    main()
