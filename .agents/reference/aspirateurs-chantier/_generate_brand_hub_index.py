#!/usr/bin/env python3
"""Render the /marques/ hub without unsupported tier labels."""
from pathlib import Path
import re

BASE = Path(__file__).resolve().parent
PATH = BASE / 'marques' / 'index.html'

BRANDS = [
    ('Kärcher','/marques/karcher/','WD pour eau/poussière · NT pour le professionnel et les classes de sécurité'),
    ('Bosch','/marques/bosch/','Home & Garden · GAS Professional · Professional 18V / AMPShare'),
    ('Makita','/marques/makita/','VC filaire · LXT/XGT · AWS · classes selon référence'),
    ('Festool','/marques/festool/','CTL / CTM / CTH · CLEANTEC · AUTOCLEAN · CTC sans fil'),
    ('DeWalt','/marques/dewalt/','DCV586M / DCV584L · FLEXVOLT · AIRLOCK · TSTAK'),
    ('Parkside','/marques/parkside/','PWD 12 à 30 · disponibilité Lidl · positionnement bricolage'),
    ('Nilfisk','/marques/nilfisk/','Buddy / Multi pour le grand public · ATTIX pour le professionnel'),
    ('Mirka','/marques/mirka/','DEXOS · DEROS/DEOS · écosystème de ponçage sans poussière'),
]

cards = ''.join(
    f'<a href="{url}" class="hub-link"><div><div>{name}</div><div class="hub-link-meta">{meta}</div></div><span class="hub-link-right">→</span></a>'
    for name, url, meta in BRANDS
)

body = f'''<main>
<div class="container"><nav class="breadcrumb"><a href="/">Accueil</a><span class="sep">/</span><span>Marques</span></nav></div>
<section class="page-hero"><div class="container"><h1>Marques d'aspirateurs de chantier</h1><p class="lead">Comprendre la logique de gamme et l’écosystème de chaque fabricant avant de descendre vers un modèle, un usage ou un comparatif.</p><div class="page-meta"><span class="meta-tag">Cluster audité : 09/09/2026</span></div></div></section>
<section class="section"><div class="container">
<div class="answer-box"><p>Nous n’imposons pas de hiérarchie arbitraire entre les fabricants sans critère mesurable. Chaque hub explique ce que la marque change réellement dans le choix : famille de produits, classe, décolmatage, raccords, batteries, consommables ou usage spécialisé.</p></div>
<div class="hub-grid">{cards}</div>
</div></section>
</main>'''

html = PATH.read_text(encoding='utf-8')
html = re.sub(r'<title>.*?</title>', "<title>Marques d'aspirateurs de chantier — gammes et écosystèmes</title>", html, count=1, flags=re.S)
html = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Kärcher, Bosch, Makita, Festool, DeWalt, Parkside, Nilfisk et Mirka : comprendre leurs gammes, technologies et usages avant de choisir.">', html, count=1)
html = re.sub(r'<main>.*?</main>', body, html, count=1, flags=re.S)
PATH.write_text('\n'.join(line.rstrip() for line in html.splitlines()) + '\n', encoding='utf-8')
print('✓ brand hub index')
