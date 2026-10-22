#!/usr/bin/env python3
"""Render reusable editorial product modules from the central product registry."""

from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REGISTRY_PATH = ROOT / ".content" / "products" / "registry.json"
PLACEMENTS_PATH = ROOT / ".content" / "products" / "placements.json"
AFFILIATE_CONFIG_PATH = ROOT / ".content" / "products" / "affiliate.json"
LEGACY_PILOT_PATH = ROOT / ".content" / "products" / "pilot-comparisons.json"
ALLOWED_LAYOUTS = {"recommendation_list", "comparison_cards"}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_registry() -> dict[str, dict]:
    return load_json(REGISTRY_PATH)["products"]


def load_placements(section: str | None = None) -> dict:
    data = load_json(PLACEMENTS_PATH)
    sections = data["sections"]
    if section is None:
        return sections
    if section not in sections:
        raise KeyError(f"Unknown product-placement section: {section}")
    return sections[section]


def load_pilot() -> dict[str, dict]:
    """Backward-compatible loader while old workflow commits drain."""
    if LEGACY_PILOT_PATH.exists():
        return load_json(LEGACY_PILOT_PATH)["pages"]
    return load_placements("comparisons")["pages"]


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def amazon_affiliate_url(product: dict) -> str:
    """Return an explicit affiliate URL or build the canonical Amazon.fr link from ASIN."""
    amazon = product.get("amazon", {})
    affiliate_url = (amazon.get("affiliate_url") or "").strip()
    if affiliate_url:
        return affiliate_url

    asin = (amazon.get("asin") or "").strip()
    if not asin:
        return ""

    config = load_json(AFFILIATE_CONFIG_PATH)["amazon_fr"]
    base_url = config["base_url"].rstrip("/")
    tracking_id = config["tracking_id"]
    return f"{base_url}/dp/{asin}/ref=nosim?tag={tracking_id}"


def render_commerce(product_id: str, product: dict, placement: str) -> str:
    affiliate_url = amazon_affiliate_url(product)
    if affiliate_url:
        return (
            f'<a class="product-card__cta" href="{esc(affiliate_url)}" '
            'target="_blank" rel="sponsored nofollow noopener noreferrer" '
            f'data-affiliate-link="amazon" data-product-key="{esc(product_id)}" '
            f'data-placement="{esc(placement)}">Voir le prix sur Amazon →</a>'
            '<span class="product-card__disclosure">Lien rémunéré</span>'
        )
    return (
        f'<a class="product-card__internal" href="{esc(product["internal_url"])}">'
        "Voir notre analyse →</a>"
    )


def render_card(product_id: str, product: dict, placement: str) -> str:
    image = product.get("image", {})
    image_url = (image.get("url") or "").strip()
    image_html = ""
    if image_url:
        image_html = (
            '<div class="product-card__media">'
            f'<img src="{esc(image_url)}" alt="{esc(product["name"])}" loading="lazy" decoding="async">'
            "</div>"
        )

    specs = "".join(
        '<div class="product-card__spec">'
        f'<dt>{esc(item["label"])}</dt><dd>{esc(item["value"])}</dd>'
        "</div>"
        for item in product.get("specs", [])[:5]
    )
    commerce_html = render_commerce(product_id, product, placement)

    return (
        f'<div class="product-card" data-product-id="{esc(product_id)}">'
        f'{image_html}'
        '<div class="product-card__body">'
        f'<h3 class="product-card__title">{esc(product["name"])}</h3>'
        f'<p class="product-card__best"><strong>À privilégier pour :</strong> {esc(product["best_for"])}</p>'
        f'<dl class="product-card__specs">{specs}</dl>'
        f'<div class="product-card__actions">{commerce_html}</div>'
        "</div></div>"
    )


def render_recommendation_row(product_id: str, product: dict, placement: str) -> str:
    image = product.get("image", {})
    image_url = (image.get("url") or "").strip()
    media_html = ""
    row_class = "product-recommendation-row"
    if image_url:
        row_class += " product-recommendation-row--with-media"
        media_html = (
            '<div class="product-recommendation-row__media">'
            f'<img src="{esc(image_url)}" alt="{esc(product["name"])}" loading="lazy" decoding="async">'
            "</div>"
        )

    specs = "".join(
        '<div class="product-recommendation-row__spec">'
        f'<dt>{esc(item["label"])}</dt><dd>{esc(item["value"])}</dd>'
        "</div>"
        for item in product.get("specs", [])[:5]
    )
    commerce_html = render_commerce(product_id, product, placement)

    return (
        f'<div class="{row_class}" data-product-id="{esc(product_id)}">'
        f'{media_html}'
        '<div class="product-recommendation-row__content">'
        f'<h3 class="product-recommendation-row__title">{esc(product["name"])}</h3>'
        f'<p class="product-recommendation-row__best"><strong>À privilégier pour :</strong> {esc(product["best_for"])}</p>'
        f'<dl class="product-recommendation-row__specs">{specs}</dl>'
        "</div>"
        f'<div class="product-recommendation-row__actions">{commerce_html}</div>'
        "</div>"
    )


def render_section(
    page_slug: str,
    config: dict,
    registry: dict[str, dict],
    section: str | None = None,
) -> str:
    layout = config.get("layout")
    if layout not in ALLOWED_LAYOUTS:
        raise ValueError(f"{page_slug}: unsupported product layout {layout!r}")

    placement = f"{section}:{page_slug}" if section else page_slug
    if layout == "comparison_cards":
        products_html = "".join(
            render_card(product_id, registry[product_id], placement)
            for product_id in config["products"]
        )
        module_html = (
            '<div class="product-card-grid product-card-grid--2">'
            f'{products_html}</div>'
        )
        section_class = "product-card-section product-card-section--comparison"
    else:
        products_html = "".join(
            render_recommendation_row(product_id, registry[product_id], placement)
            for product_id in config["products"]
        )
        module_html = (
            '<div class="product-recommendation-list">'
            f'{products_html}</div>'
        )
        section_class = "product-card-section product-card-section--recommendations"

    if section:
        start_marker = f'<!-- PRODUCT_MODULE:{esc(section)}:{esc(page_slug)}:START -->'
        end_marker = f'<!-- PRODUCT_MODULE:{esc(section)}:{esc(page_slug)}:END -->'
        module_attr = 'data-product-module="true"'
    else:
        start_marker = f'<!-- PRODUCT_PILOT:{esc(page_slug)}:START -->'
        end_marker = f'<!-- PRODUCT_PILOT:{esc(page_slug)}:END -->'
        module_attr = 'data-product-pilot="true"'

    return (
        f'{start_marker}\n'
        f'<section class="{section_class}" {module_attr} '
        f'data-product-placement="{esc(placement)}" data-product-layout="{esc(layout)}">\n'
        f'  <h2 id="{esc(config["section_id"])}">{esc(config["section_title"])}</h2>\n'
        f'  <p class="product-card-section__intro">{esc(config["intro"])}</p>\n'
        f'  {module_html}\n'
        '</section>\n'
        f'{end_marker}'
    )