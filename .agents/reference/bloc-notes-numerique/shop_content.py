#!/usr/bin/env python3
"""Render the affiliation shop from the guarded product registry."""

from __future__ import annotations

import html
import json
from pathlib import Path

from product_cards import amazon_affiliate_url

ROOT = Path(__file__).resolve().parent
REGISTRY_PATH = ROOT / ".content" / "products" / "registry.json"


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def product_facets(product_id: str, product: dict) -> dict[str, str]:
    specs = " ".join(item.get("value", "") for item in product.get("specs", [])).lower()
    name = product.get("name", "").lower()

    if product_id.startswith("remarkable"):
        brand = "remarkable"
    elif product_id.startswith("boox"):
        brand = "boox"
    elif product_id.startswith("kindle"):
        brand = "kindle"
    elif product_id.startswith("kobo"):
        brand = "kobo"
    else:
        brand = "supernote"

    if "couleur" in specs:
        display = "couleur"
    else:
        display = "monochrome"

    if "13,3" in specs:
        size = "grand"
    elif "7,3" in specs or "7,8" in specs or "compact" in specs:
        size = "compact"
    else:
        size = "standard"

    search = " ".join((name, specs, product.get("best_for", "").lower()))
    return {"brand": brand, "display": display, "size": size, "search": search}


def render_product(product_id: str, product: dict) -> str:
    facets = product_facets(product_id, product)
    affiliate_url = amazon_affiliate_url(product)
    specs = "".join(
        f'<div class="shop-product__spec"><dt>{esc(item["label"])}</dt><dd>{esc(item["value"])}</dd></div>'
        for item in product.get("specs", [])[:3]
    )

    image = product.get("image", {})
    image_url = (image.get("url") or "").strip()
    if image_url:
        visual = (
            '<div class="shop-product__visual shop-product__visual--image">'
            f'<img src="{esc(image_url)}" alt="{esc(product["name"])}" loading="lazy" decoding="async">'
            '</div>'
        )
    else:
        brand_label = {
            "remarkable": "reMarkable",
            "boox": "BOOX",
            "kindle": "Kindle",
            "kobo": "Kobo",
            "supernote": "Supernote",
        }[facets["brand"]]
        visual = (
            '<div class="shop-product__visual" aria-hidden="true">'
            '<span class="shop-product__device"><span></span></span>'
            f'<span class="shop-product__brand">{esc(brand_label)}</span>'
            '</div>'
        )

    if affiliate_url:
        commerce = (
            f'<a class="shop-product__buy" href="{esc(affiliate_url)}" target="_blank" '
            'rel="sponsored nofollow noopener noreferrer" data-affiliate-link="amazon" '
            f'data-product-key="{esc(product_id)}" data-placement="shop:catalogue">'
            'Voir le prix sur Amazon <span aria-hidden="true">↗</span></a>'
            '<span class="shop-product__disclosure">Lien affilié — prix et disponibilité chez Amazon</span>'
        )
    else:
        commerce = '<span class="shop-product__unavailable">Aucun lien marchand vérifié actuellement</span>'

    return f"""
<article class="shop-product" data-shop-product data-brand="{facets['brand']}" data-display="{facets['display']}" data-size="{facets['size']}" data-search="{esc(facets['search'])}">
  {visual}
  <div class="shop-product__content">
    <p class="shop-product__meta">{esc(facets['display'].capitalize())} · {esc({'compact': 'Format compact', 'standard': 'Environ 10 pouces', 'grand': 'Grand format'}[facets['size']])}</p>
    <h2>{esc(product['name'])}</h2>
    <p class="shop-product__best"><strong>Adapté à :</strong> {esc(product['best_for'])}</p>
    <dl class="shop-product__specs">{specs}</dl>
    <div class="shop-product__links">
      <a class="shop-product__review" href="{esc(product['internal_url'])}">Lire notre analyse <span aria-hidden="true">→</span></a>
      <div class="shop-product__commerce">{commerce}</div>
    </div>
  </div>
</article>"""


def render_shop_content() -> str:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))["products"]
    products = "\n".join(render_product(product_id, product) for product_id, product in registry.items())
    return f"""
<section class="shop-hero">
  <div class="container shop-hero__inner">
    <div>
      <p class="shop-eyebrow">Boutique d’affiliation</p>
      <h1>Les bloc-notes numériques déjà analysés sur le site</h1>
      <p class="lead">Retrouvez les modèles cités dans nos comparatifs et guides. Filtrez-les selon vos contraintes, consultez notre analyse, puis vérifiez le prix chez le marchand.</p>
    </div>
    <aside class="shop-hero__notice" aria-label="Fonctionnement de la boutique">
      <strong>Notre sélection reste éditoriale</strong>
      <p>Nous n’ajoutons pas un produit parce qu’il possède un lien affilié. Certains modèles sont donc présentés sans bouton marchand.</p>
      <a href="/transparence-affiliation/">Comment fonctionne l’affiliation →</a>
    </aside>
  </div>
</section>

<section class="shop-catalogue" aria-labelledby="catalogue-title">
  <div class="container">
    <div class="shop-catalogue__heading">
      <div>
        <p class="shop-eyebrow">Catalogue</p>
        <h2 id="catalogue-title">Comparer les modèles</h2>
      </div>
      <p><strong data-result-count>{len(registry)}</strong> modèles affichés</p>
    </div>

    <form class="shop-filters" data-shop-filters aria-label="Filtrer les produits">
      <label class="shop-search">
        <span>Rechercher</span>
        <input type="search" name="query" placeholder="Ex. BOOX, couleur, PDF…" autocomplete="off">
      </label>
      <label>
        <span>Marque</span>
        <select name="brand">
          <option value="">Toutes les marques</option>
          <option value="remarkable">reMarkable</option>
          <option value="boox">BOOX</option>
          <option value="kindle">Kindle</option>
          <option value="kobo">Kobo</option>
          <option value="supernote">Supernote</option>
        </select>
      </label>
      <label>
        <span>Affichage</span>
        <select name="display">
          <option value="">Tous les affichages</option>
          <option value="couleur">Couleur</option>
          <option value="monochrome">Monochrome</option>
        </select>
      </label>
      <label>
        <span>Format</span>
        <select name="size">
          <option value="">Tous les formats</option>
          <option value="compact">Compact</option>
          <option value="standard">Environ 10 pouces</option>
          <option value="grand">Grand format</option>
        </select>
      </label>
      <button type="reset">Réinitialiser</button>
    </form>

    <p class="shop-empty" data-shop-empty hidden>Aucun modèle ne correspond à ces filtres. Essayez d’élargir votre recherche.</p>
    <div class="shop-grid" data-shop-grid>
      {products}
    </div>
  </div>
</section>

<section class="shop-help">
  <div class="container shop-help__inner">
    <div>
      <p class="shop-eyebrow">Avant d’acheter</p>
      <h2>Le bon modèle dépend surtout de votre usage</h2>
      <p>Un grand écran, la couleur ou Android ne sont pas automatiquement préférables. Commencez par vos documents, vos applications indispensables et la manière dont vous exportez vos notes.</p>
    </div>
    <a class="shop-help__link" href="/guides/choisir-bloc-notes-numerique/">Consulter le guide de choix <span aria-hidden="true">→</span></a>
  </div>
</section>
"""
