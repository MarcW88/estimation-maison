#!/usr/bin/env python3
from pathlib import Path
import re
from brand_pages import PAGES
from brand_data import VERIFIED_AT, BRANDS
from brand_publication import INDEXATION_SCOPE, ROBOTS_DIRECTIVE
from brand_reviewed_output import reviewed_body
from brand_enriched_output import enriched_body
from brand_bespoke_output import bespoke_body, bespoke_metadata
from brand_hub_bespoke_output import hub_body, hub_metadata
from brand_light_update_output import light_body, light_metadata

ROOT = Path(__file__).resolve().parent


def html_path(url):
    rel = url.strip('/')
    return ROOT / rel / 'index.html' if rel else ROOT / 'index.html'


def replace_first(pattern, repl, text, flags=0, required=True):
    out, count = re.subn(pattern, repl, text, count=1, flags=flags)
    if required and count != 1:
        raise SystemExit(f'Expected one match for {pattern!r}, got {count}')
    return out


for url, page_data in PAGES.items():
    if not url.startswith(INDEXATION_SCOPE):
        raise SystemExit(f'Brand renderer received URL outside approved scope: {url}')

    page = html_path(url)
    if not page.exists():
        raise SystemExit(f'Missing brand page: {page}')

    html = page.read_text(encoding='utf-8')
    title = page_data['title']
    description = page_data['description']
    title, description = bespoke_metadata(url, title, description)
    title, description = hub_metadata(url, title, description)
    title, description = light_metadata(url, title, description)
    body = reviewed_body(url, page_data).strip()
    body = enriched_body(url, body).strip()
    body = bespoke_body(url, body).strip()
    body = hub_body(url, body).strip()
    body = light_body(url, body).strip()

    # The reMarkable light refresh adds the current Connect source. Keep it
    # in the source list even when the upstream body contains earlier <ul>s.
    if url == '/marques/remarkable/':
        connect_source = '<li><a href="https://remarkable.com/shop/connect" rel="noopener noreferrer">reMarkable Connect — fonctions 2026</a></li>'
        body = body.replace(connect_source, '')
        body = body.replace('<ul class="source-list">', '<ul class="source-list">' + connect_source, 1)

    brand_key = page_data.get('brand')
    if page_data.get('page_type') == 'BRAND_HUB' and brand_key in BRANDS:
        positioning = BRANDS[brand_key]['positioning']
        bad = f'<p>{positioning.capitalize()}.</p>'
        good = f'<p>{positioning[0].upper() + positioning[1:]}.</p>'
        body = body.replace(bad, good)

    if url == '/marques/remarkable/remarkable-2/':
        body = body.replace(
            '<h2 id="compatibilite">Le principal piège reste la génération des accessoires</h2>',
            '<h2 id="compatibilite">Compatibilités et limites : le principal piège reste la génération des accessoires</h2>',
        )

    if url == '/marques/remarkable/remarkable-2-avis/':
        body = body.replace(
            '<h2 id="methode">Sur quoi repose cet avis ?</h2>',
            '<h2 id="methode">Sur quoi repose cet avis ?</h2>\n<p><strong>Il s’agit d’une analyse documentaire, pas d’un test physique réalisé par nos soins.</strong></p>',
        )
        body = body.replace(
            '<h2 id="sources">Sources consultées</h2>',
            '<h2 id="sources">Sources consultées</h2>\n<p>Statut, support et sources vérifiés le 9 septembre 2026.</p>',
        )

    if url == '/marques/boox/boox-tab-ultra/':
        body = body.replace(
            '<h2 id="limites">Pourquoi l’ancienneté du système compte</h2>',
            '<h2 id="limites">Les limites liées à l’ancienneté du système</h2>',
        )
        body = body.replace(
            '<h2 id="android">Android 12 est un facteur de génération, pas une date d’obsolescence</h2>',
            '<h2 id="android">Android 12 : une limite de génération, pas une date d’obsolescence</h2>',
        )
        body = body.replace(
            '<h2 id="choix">Quand le Tab Ultra C Pro garde-t-il du sens ?</h2>',
            '<h2 id="choix">Pour qui le Tab Ultra C Pro garde-t-il du sens ?</h2>',
        )

    html = replace_first(r'<title>.*?</title>', f'<title>{title}</title>', html, re.S)
    html = replace_first(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{description}">',
        html,
    )
    html = replace_first(
        r'<meta name="robots" content="[^"]*">',
        f'<meta name="robots" content="{ROBOTS_DIRECTIVE}">',
        html,
    )
    html = replace_first(r'<h1>.*?</h1>', f'<h1>{title}</h1>', html, re.S)
    html = replace_first(
        r'<p class="lead">.*?</p>',
        f'<p class="lead">{description}</p>',
        html,
        re.S,
    )

    article_section = f'''\n<section class="section">\n  <div class="container">\n    <div class="content-layout">\n      <article class="content-main">\n      {body}\n      </article>\n      <aside class="content-sidebar" aria-label="Sommaire de la page">\n        <div class="sidebar-box">\n          <h4>Sur cette page</h4>\n          <nav class="sidebar-toc" aria-label="Sommaire"></nav>\n        </div>\n      </aside>\n    </div>\n  </div>\n</section>\n'''

    main_pattern = r'(<section class="page-hero">.*?</section>)(.*?)(</main>)'
    m = re.search(main_pattern, html, re.S)
    if not m:
        raise SystemExit(f'Unable to locate hero/main boundary: {url}')
    html = html[:m.end(1)] + article_section + html[m.start(3):]

    html = html.replace(
        '<span class="page-meta-item">Contenu en préparation</span>',
        f'<span class="page-meta-item">Sources vérifiées le {VERIFIED_AT}</span>'
    )
    html = html.replace(
        '<span class="update-tag">Analyse en préparation</span>',
        f'<span class="update-tag">Sources vérifiées le {VERIFIED_AT}</span>'
    )

    if '<!-- Contenu à rédiger -->' in html:
        raise SystemExit(f'Placeholder still present: {url}')
    if 'Contenu en préparation' in html or 'Analyse en préparation' in html:
        raise SystemExit(f'Preparation label still present: {url}')
    if f'name="robots" content="{ROBOTS_DIRECTIVE}"' not in html:
        raise SystemExit(f'approved robots directive missing: {url}')
    if '<article class="content-main">' not in html:
        raise SystemExit(f'content-main absent after render: {url}')
    if '<nav class="sidebar-toc" aria-label="Sommaire"></nav>' not in html:
        raise SystemExit(f'brand TOC sidebar absent after render: {url}')

    page.write_text(html, encoding='utf-8')
    print('updated', url)
