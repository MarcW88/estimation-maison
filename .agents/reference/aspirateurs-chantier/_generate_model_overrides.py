#!/usr/bin/env python3
"""Render verified model pages after the legacy site generator.

The evidence file remains the source of truth for model facts. During the model
workflow migration, a page may optionally provide a bespoke editorial body and
metadata under .content/models/pages/. Models without an override keep the legacy
body until they have completed the model workflow.
"""
from pathlib import Path
from html import escape
import json
import re

BASE = Path(__file__).resolve().parent
DATA = json.loads((BASE / '.content/models/model-evidence.json').read_text(encoding='utf-8'))
PAGES_DIR = BASE / '.content' / 'models' / 'pages'
UPDATED = DATA['updated_at'].split('-')
UPDATED_FR = f"{UPDATED[2]}/{UPDATED[1]}/{UPDATED[0]}"

RELATED = {
    'karcher-wd2': [('Kärcher WD 5', '/modeles/karcher-wd5/'), ('Kärcher', '/marques/karcher/'), ('Eau et poussière', '/comparatifs/aspirateur-eau-poussiere/')],
    'karcher-wd5': [('Kärcher WD 6', '/modeles/karcher-wd6/'), ('Kärcher', '/marques/karcher/'), ('Bricolage et rénovation', '/usages/aspirateur-bricolage-renovation/')],
    'karcher-wd6': [('Kärcher NT 30/1 Tact', '/modeles/karcher-nt-30-1-tact/'), ('Kärcher', '/marques/karcher/'), ('Gravats', '/usages/aspirateur-gravats/')],
    'karcher-nt-30-1-tact': [('Classe M', '/comparatifs/aspirateur-classe-m/'), ('Classes L/M/H', '/guides/classes-l-m-h/'), ('Kärcher', '/marques/karcher/')],
    'bosch-advancedvac-20': [('Bosch GAS 12-25 PL', '/modeles/bosch-gas-12-25-pl/'), ('Bosch', '/marques/bosch/'), ('Bricolage et rénovation', '/usages/aspirateur-bricolage-renovation/')],
    'bosch-gas-12-25-pl': [('Bosch GAS 35 L AFC', '/modeles/bosch-gas-35-l-afc/'), ('Bosch', '/marques/bosch/'), ('Classes L/M/H', '/guides/classes-l-m-h/')],
    'bosch-gas-18v-10-l': [('Sans fil', '/comparatifs/aspirateur-chantier-sans-fil/'), ('Bosch', '/marques/bosch/'), ('Classes L/M/H', '/guides/classes-l-m-h/')],
    'bosch-gas-35-l-afc': [('Bosch GAS 35 M AFC', '/modeles/bosch-gas-35-m-afc/'), ('Décolmatage automatique', '/guides/decolmatage-automatique/'), ('Bosch', '/marques/bosch/')],
    'bosch-gas-35-m-afc': [('Classe M', '/comparatifs/aspirateur-classe-m/'), ('Décolmatage automatique', '/guides/decolmatage-automatique/'), ('Bosch', '/marques/bosch/')],
    'makita-vc2512l': [('Makita VC4210MX', '/modeles/makita-vc4210mx/'), ('Makita', '/marques/makita/'), ('Atelier', '/usages/aspirateur-atelier/')],
    'makita-vc4210mx': [('Makita VC2512L', '/modeles/makita-vc2512l/'), ('Classe M', '/comparatifs/aspirateur-classe-m/'), ('Makita', '/marques/makita/')],
    'festool-ctl-midi': [('Ponceuse', '/usages/aspirateur-ponceuse/'), ('Festool', '/marques/festool/'), ('Classes L/M/H', '/guides/classes-l-m-h/')],
    'nilfisk-multi-ii-30-t': [('Nilfisk', '/marques/nilfisk/'), ('Eau et poussière', '/comparatifs/aspirateur-eau-poussiere/'), ('Atelier', '/usages/aspirateur-atelier/')],
}


def li(items):
    return ''.join(f'<li>{escape(x)}</li>' for x in items)


def specs_table(specs):
    rows = ''.join(f'<tr><td class="sk">{escape(k)}</td><td class="sv">{escape(v)}</td></tr>' for k, v in specs.items())
    return f'<div class="table-wrap"><table class="spec-table"><tbody>{rows}</tbody></table></div>'


def dust_badge(value):
    if value in {'L', 'M', 'H'}:
        return f'<span class="badge badge-{value.lower()}">Classe {value}</span>'
    return '<span class="badge badge-gray">Pas de classe L/M/H documentée</span>'


def load_page_override(slug):
    body_path = PAGES_DIR / f'{slug}.html'
    meta_path = PAGES_DIR / f'{slug}.meta.json'
    if not body_path.exists() and not meta_path.exists():
        return None
    if not body_path.exists() or not meta_path.exists():
        raise SystemExit(f'Incomplete bespoke page override for {slug}: body and meta are both required')
    meta = json.loads(meta_path.read_text(encoding='utf-8'))
    body = body_path.read_text(encoding='utf-8').strip()
    if not body:
        raise SystemExit(f'Empty bespoke body for {slug}')
    toc = meta.get('toc')
    if not isinstance(toc, list) or not toc:
        raise SystemExit(f'Missing bespoke toc for {slug}')
    return {'body': body, 'meta': meta}


def render_toc(items):
    links = []
    for item in items:
        if not isinstance(item, list) or len(item) != 2:
            raise SystemExit('Each bespoke toc item must be [id, label]')
        anchor, label = item
        links.append(f'<a href="#{escape(str(anchor), quote=True)}">{escape(str(label))}</a>')
    return ''.join(links)


def legacy_body(d):
    return f'''<div class="answer-box"><p>{escape(d['summary'])}</p></div>
      <h2 id="lecture">Comment lire cette référence</h2>
      <p>Cette fiche sert à vérifier une référence précise, pas à refaire le comparatif de toute la marque. Les caractéristiques ci-dessus viennent de la documentation fabricant consultée le {UPDATED_FR}. Lorsqu'un débit ou une dépression est indiqué à la turbine, il ne doit être comparé qu'à une mesure prise au même point.</p>
      <h2 id="pour-qui">Quand ce modèle est cohérent</h2>
      <ul>{li(d['best_for'])}</ul>
      <h2 id="limites">Limites et garde-fous</h2>
      <ul>{li(d['limits'])}</ul>
      <p>Pour les poussières potentiellement dangereuses, la classe de l'appareil doit être choisie à partir du risque réel et des prescriptions applicables. Un filtre HEPA, une forte puissance ou un débit élevé ne permettent pas de déduire une classe L, M ou H.</p>
      <h2 id="source">Source fabricant</h2>
      <p><a href="{escape(d['source'], quote=True)}" rel="nofollow noopener">Documentation officielle consultée pour {escape(d['name'])}</a>.</p>
      <p><small>Analyse documentaire, sans test physique. Les liens affiliés éventuels n'influencent pas les caractéristiques retenues.</small></p>'''


def render_main(slug, d):
    rel = ''.join(f'<a href="{url}">{escape(label)}</a>' for label, url in RELATED.get(slug, []))
    override = load_page_override(slug)
    if override:
        body = override['body']
        toc = render_toc(override['meta']['toc'])
        verified_date = override['meta'].get('verified_date', UPDATED_FR)
    else:
        body = legacy_body(d)
        toc = '<a href="#lecture">Lire la référence</a><a href="#pour-qui">Quand la choisir</a><a href="#limites">Limites</a><a href="#source">Source</a>'
        verified_date = UPDATED_FR

    return f'''<main>
<div class="container"><nav class="breadcrumb"><a href="/">Accueil</a><span class="sep">/</span> <a href="/modeles/">Modèles</a> <span class="sep">/</span> <span>{escape(d['name'])}</span></nav></div>
<section class="model-hero">
  <div class="container">
    <div class="model-hero-inner">
      <div>
        <div class="model-badges">{dust_badge(d['dust_class'])}<span class="badge badge-blue">{escape(d['brand'])}</span><span class="ctype ctype-modele">Fiche modèle</span></div>
        <h1 class="model-title">{escape(d['name'])}</h1>
        <p class="model-tagline lead">{escape(d['description'])}</p>
        <div class="page-meta"><span class="meta-tag">Vérifié : {escape(verified_date)}</span><span class="meta-tag">Recherche documentaire</span></div>
      </div>
      <div class="spec-sheet">
        <div class="spec-sheet-header"><span>Repères vérifiés</span><span class="verified">Source primaire</span></div>
        {specs_table(d['specs'])}
      </div>
    </div>
  </div>
</section>
<div class="container">
  <div class="content-layout">
    <article class="content-main">
      {body}
      <div class="related-box"><h4>À lire aussi</h4><div class="related-links">{rel}</div></div>
    </article>
    <aside class="content-sidebar">
      <div class="sidebar-box"><div class="sidebar-box-head">Statut</div><div class="sidebar-box-body">{dust_badge(d['dust_class'])}</div></div>
      <div class="sidebar-box"><div class="sidebar-box-head">Sommaire</div><div class="sidebar-box-body"><nav class="toc-list">{toc}</nav></div></div>
      <div class="sidebar-box"><div class="sidebar-box-head">Affiliation</div><div class="sidebar-box-body"><p class="affil-note">Ce site contient des liens affiliés. Nos analyses restent documentaires et indépendantes. <a href="/transparence-affiliation/">En savoir plus.</a></p></div></div>
    </aside>
  </div>
</div>
</main>'''


def render_index(html):
    cards = []
    for slug, d in DATA['models'].items():
        label = f"Classe {d['dust_class']}" if d['dust_class'] in {'L','M','H'} else 'Usage eau/poussière — pas de classe L/M/H documentée'
        cards.append(f'<a href="/modeles/{slug}/" class="hub-link"><div><div>{escape(d["name"])}</div><div class="hub-link-meta">{escape(label)}</div></div><span class="hub-link-right">→</span></a>')
    body = f'''<main>
<div class="container"><nav class="breadcrumb"><a href="/">Accueil</a><span class="sep">/</span><span>Modèles</span></nav></div>
<section class="page-hero"><div class="container"><h1>Fiches modèles vérifiées</h1><p class="lead">Fiches documentaires par référence : classe réellement documentée, débit et dépression avec leur contexte, capacité, décolmatage et limites.</p><div class="page-meta"><span class="meta-tag">Vérifié : {UPDATED_FR}</span></div></div></section>
<section class="section"><div class="container"><div class="answer-box"><p>Une fiche modèle décrit une référence précise. Elle ne doit ni inventer une classe de poussière, ni remplacer un comparatif, ni reprendre les promesses générales d'une page marque.</p></div><div class="hub-grid">{''.join(cards)}</div></div></section>
</main>'''
    return re.sub(r'<main>.*?</main>', body, html, flags=re.S)


def main():
    for slug, d in DATA['models'].items():
        path = BASE / 'modeles' / slug / 'index.html'
        if not path.exists():
            raise SystemExit(f'Missing model page: {path}')
        html = path.read_text(encoding='utf-8')
        override = load_page_override(slug)
        title = override['meta'].get('title') if override else None
        meta_description = override['meta'].get('meta_description') if override else None
        title = title or f'{d["name"]} — fiche technique vérifiée'
        meta_description = meta_description or d['description']
        html = re.sub(r'<title>.*?</title>', f'<title>{escape(title)}</title>', html, count=1, flags=re.S)
        html = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{escape(meta_description, quote=True)}">', html, count=1)
        html = re.sub(r'<main>.*?</main>', render_main(slug, d), html, count=1, flags=re.S)
        path.write_text('\n'.join(line.rstrip() for line in html.splitlines()) + '\n', encoding='utf-8')
        mode = 'bespoke' if override else 'legacy'
        print(f'✓ model {slug} ({mode})')

    idx = BASE / 'modeles' / 'index.html'
    html = idx.read_text(encoding='utf-8')
    html = re.sub(r'<title>.*?</title>', '<title>Fiches modèles vérifiées — Aspirateurs de chantier</title>', html, count=1, flags=re.S)
    html = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Fiches modèles vérifiées : caractéristiques fabricant, classes L/M/H documentées, débit, dépression, capacité et limites.">', html, count=1)
    idx.write_text('\n'.join(line.rstrip() for line in render_index(html).splitlines()) + '\n', encoding='utf-8')
    print('✓ model index')


if __name__ == '__main__':
    main()
