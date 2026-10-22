#!/usr/bin/env python3
"""Render guarded editorial product modules from the central registry."""

from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REGISTRY_PATH = ROOT / ".content" / "products" / "registry.json"
PLACEMENTS_PATH = ROOT / ".content" / "products" / "placements.json"
AFFILIATE_CONFIG_PATH = ROOT / ".content" / "products" / "affiliate.json"
ALLOWED_LAYOUTS = {"recommendation_list", "comparison_cards"}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_registry() -> dict[str, dict]:
    return load_json(REGISTRY_PATH)["products"]


def load_placements(section: str | None = None) -> dict:
    sections = load_json(PLACEMENTS_PATH)["sections"]
    if section is None:
        return sections
    if section not in sections:
        raise KeyError(f"Unknown product-placement section: {section}")
    return sections[section]


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def amazon_affiliate_url(product: dict) -> str:
    amazon = product.get("amazon", {})
    explicit = (amazon.get("affiliate_url") or "").strip()
    if explicit:
        return explicit
    asin = (amazon.get("asin") or "").strip()
    if not asin:
        return ""
    config = load_json(AFFILIATE_CONFIG_PATH)["amazon_fr"]
    return f"{config['base_url'].rstrip('/')}/dp/{asin}/ref=nosim?tag={config['tracking_id']}"


def render_commerce(product_id: str, product: dict, placement: str) -> str:
    url = amazon_affiliate_url(product)
    if url:
        return (
            f'<a class="product-card__cta" href="{esc(url)}" target="_blank" '
            'rel="sponsored nofollow noopener noreferrer" '
            f'data-affiliate-link="amazon" data-product-key="{esc(product_id)}" '
            f'data-placement="{esc(placement)}">Voir le prix sur Amazon →</a>'
            '<span class="product-card__disclosure">Lien rémunéré</span>'
            f'<a class="product-card__internal" href="{esc(product["internal_url"])}">Voir notre analyse →</a>'
        )
    return f'<a class="product-card__internal" href="{esc(product["internal_url"])}">Voir notre analyse →</a>'


def render_specs(product: dict, row: bool) -> str:
    cls = "product-recommendation-row__spec" if row else "product-card__spec"
    return "".join(
        f'<div class="{cls}"><dt>{esc(item["label"])}</dt><dd>{esc(item["value"])}</dd></div>'
        for item in product.get("specs", [])[:5]
    )


def render_card(product_id: str, product: dict, placement: str) -> str:
    return (
        f'<div class="product-card" data-product-id="{esc(product_id)}">'
        '<div class="product-card__body">'
        f'<h3 class="product-card__title">{esc(product["name"])}</h3>'
        f'<p class="product-card__best"><strong>À privilégier pour :</strong> {esc(product["best_for"])}</p>'
        f'<dl class="product-card__specs">{render_specs(product, False)}</dl>'
        f'<div class="product-card__actions">{render_commerce(product_id, product, placement)}</div>'
        '</div></div>'
    )


def render_recommendation_row(product_id: str, product: dict, placement: str) -> str:
    return (
        f'<div class="product-recommendation-row" data-product-id="{esc(product_id)}">'
        '<div class="product-recommendation-row__content">'
        f'<h3 class="product-recommendation-row__title">{esc(product["name"])}</h3>'
        f'<p class="product-recommendation-row__best"><strong>À privilégier pour :</strong> {esc(product["best_for"])}</p>'
        f'<dl class="product-recommendation-row__specs">{render_specs(product, True)}</dl>'
        '</div>'
        f'<div class="product-recommendation-row__actions">{render_commerce(product_id, product, placement)}</div>'
        '</div>'
    )


def render_section(page_slug: str, config: dict, registry: dict[str, dict], section: str) -> str:
    layout = config.get("layout")
    if layout not in ALLOWED_LAYOUTS:
        raise ValueError(f"{page_slug}: unsupported product layout {layout!r}")
    placement = f"{section}:{page_slug}"
    if layout == "comparison_cards":
        products_html = "".join(render_card(pid, registry[pid], placement) for pid in config["products"])
        module_html = f'<div class="product-card-grid product-card-grid--2">{products_html}</div>'
        section_class = "product-card-section product-card-section--comparison"
    else:
        products_html = "".join(render_recommendation_row(pid, registry[pid], placement) for pid in config["products"])
        module_html = f'<div class="product-recommendation-list">{products_html}</div>'
        section_class = "product-card-section product-card-section--recommendations"
    return (
        f'<!-- PRODUCT_MODULE:{esc(section)}:{esc(page_slug)}:START -->\n'
        f'<section class="{section_class}" data-product-module="true" '
        f'data-product-placement="{esc(placement)}" data-product-layout="{esc(layout)}">\n'
        f'  <h2 id="{esc(config["section_id"])}">{esc(config["section_title"])}</h2>\n'
        f'  <p class="product-card-section__intro">{esc(config["intro"])}</p>\n'
        f'  {module_html}\n'
        '</section>\n'
        f'<!-- PRODUCT_MODULE:{esc(section)}:{esc(page_slug)}:END -->'
    )
