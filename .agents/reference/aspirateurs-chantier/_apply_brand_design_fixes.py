#!/usr/bin/env python3
"""Apply visual-design fixes to the brand cluster after content generation.

This is deliberately a post-processing layer: editorial generators remain free to
change their bespoke article structures, while the shared brand UX stays stable.
CSS is provided by the sitewide /style.css entry point.
"""
from pathlib import Path
import re

BASE = Path(__file__).resolve().parent

MODULES = {
    "bosch": '''<section class="brand-decision-module" data-layout="split" aria-label="Repère visuel Bosch"><span class="brand-decision-kicker">Repère de gamme</span><p class="brand-decision-title">Trois univers Bosch à ne pas mélanger</p><div class="brand-decision-flow"><div class="brand-decision-node"><strong>Home & Garden</strong><span>PAS, UniversalVac, AdvancedVac · bricolage et eau/poussière</span></div><div class="brand-decision-node"><strong>GAS Professional filaire</strong><span>Classes L/M selon référence · AFC · Click & Clean</span></div><div class="brand-decision-node"><strong>GAS Professional 18 V</strong><span>Mobilité · Professional 18V / AMPShare</span></div></div></section>''',
    "karcher": '''<section class="brand-decision-module" data-layout="split" aria-label="Repère visuel Kärcher"><span class="brand-decision-kicker">Décision principale</span><p class="brand-decision-title">WD ou NT : choisissez d'abord la famille</p><div class="brand-decision-flow"><div class="brand-decision-node"><strong>WD Home & Garden</strong><span>Eau, saletés, garage, rénovation courante</span></div><div class="brand-decision-node"><strong>NT Professional</strong><span>Poussières fines, classes documentées, Tact, antistatique</span></div></div></section>''',
    "festool": '''<section class="brand-decision-module" data-layout="workflow" aria-label="Repère visuel Festool"><span class="brand-decision-kicker">Workflow Festool</span><p class="brand-decision-title">L'aspirateur prend son sens dans le système complet</p><div class="brand-decision-flow"><div class="brand-decision-node"><strong>Outil</strong><span>Ponceuse, scie ou défonceuse</span></div><div class="brand-decision-node"><strong>CLEANTEC</strong><span>Flexible et raccord au captage</span></div><div class="brand-decision-node"><strong>CTL / CTM / CTH</strong><span>Classe adaptée au risque</span></div><div class="brand-decision-node"><strong>Systainer / Bluetooth</strong><span>Transport et déclenchement</span></div></div></section>''',
    "makita": '''<section class="brand-decision-module" data-layout="ladder" aria-label="Repère visuel Makita"><span class="brand-decision-kicker">Lire la nomenclature</span><p class="brand-decision-title">Trois familles avant de comparer les références</p><div class="brand-decision-flow"><div class="brand-decision-node"><strong>VC filaire</strong><span>Classes et décolmatage selon référence exacte</span></div><div class="brand-decision-node"><strong>LXT 18 V</strong><span>Mobilité si votre parc batterie est déjà LXT</span></div><div class="brand-decision-node"><strong>XGT 40 V</strong><span>Plus de puissance disponible dans l'écosystème XGT</span></div></div></section>''',
    "dewalt": '''<section class="brand-decision-module" data-layout="workflow" aria-label="Repère visuel DeWalt"><span class="brand-decision-kicker">Écosystème chantier</span><p class="brand-decision-title">DeWalt se lit comme une chaîne de compatibilités</p><div class="brand-decision-flow"><div class="brand-decision-node"><strong>XR / FLEXVOLT</strong><span>Parc batterie existant</span></div><div class="brand-decision-node"><strong>DCV</strong><span>Choix de l'extracteur et de sa classe</span></div><div class="brand-decision-node"><strong>AIRLOCK</strong><span>Raccord outil et captage</span></div><div class="brand-decision-node"><strong>TSTAK</strong><span>Transport et organisation</span></div></div></section>''',
    "parkside": '''<section class="brand-decision-module" data-layout="check" aria-label="Repère visuel Parkside"><span class="brand-decision-kicker">Avant achat</span><p class="brand-decision-title">Trois vérifications comptent plus que le prix affiché</p><div class="brand-decision-flow"><div class="brand-decision-node"><strong>Référence actuelle ?</strong><span>Vérifier PWD, génération et disponibilité Lidl</span></div><div class="brand-decision-node"><strong>Prise outil utile ?</strong><span>Ne payer la fonction que si le workflow la demande</span></div><div class="brand-decision-node"><strong>Consommables disponibles ?</strong><span>Sacs, filtres et pièces conditionnent le coût réel</span></div></div></section>''',
    "nilfisk": '''<section class="brand-decision-module" data-layout="ladder" aria-label="Repère visuel Nilfisk"><span class="brand-decision-kicker">Échelle de gamme</span><p class="brand-decision-title">Le saut principal se fait du polyvalent vers ATTIX</p><div class="brand-decision-flow"><div class="brand-decision-node"><strong>Buddy</strong><span>Entrée de gamme eau/poussière</span></div><div class="brand-decision-node"><strong>Multi II</strong><span>Atelier et bricolage mieux équipé</span></div><div class="brand-decision-node"><strong>ATTIX</strong><span>Univers professionnel, classes et InfiniClean selon modèle</span></div></div></section>''',
    "mirka": '''<section class="brand-decision-module" data-layout="workflow" aria-label="Repère visuel Mirka"><span class="brand-decision-kicker">Ponçage sans poussière</span><p class="brand-decision-title">Mirka se comprend comme un circuit de captage</p><div class="brand-decision-flow"><div class="brand-decision-node"><strong>DEROS / DEOS</strong><span>La poussière est captée à la source</span></div><div class="brand-decision-node"><strong>Flexible</strong><span>Diamètre, longueur et raccord comptent</span></div><div class="brand-decision-node"><strong>DEXOS</strong><span>Extraction et décolmatage adaptés au workflow</span></div><div class="brand-decision-node"><strong>Surface</strong><span>Moins de poussière résiduelle à reprendre</span></div></div></section>''',
}


def ensure_assets(html: str) -> str:
    if 'class="brand-page"' not in html:
        html = html.replace('<body>', '<body class="brand-page">', 1)
    if '/brand-pages.js' not in html:
        html = html.replace('</body>', '<script src="/brand-pages.js" defer></script>\n</body>', 1)
    return html


def ensure_module(html: str, slug: str) -> str:
    if 'brand-decision-module' in html:
        return html
    match = re.search(r'(<div class="answer-box">.*?</div>)', html, flags=re.S)
    if not match:
        raise RuntimeError(f'{slug}: answer-box not found')
    return html[:match.end()] + '\n' + MODULES[slug] + html[match.end():]


def patch(path: Path, slug: str | None = None) -> None:
    html = path.read_text(encoding='utf-8')
    html = ensure_assets(html)
    if slug:
        html = ensure_module(html, slug)
    path.write_text(html, encoding='utf-8')


def main() -> None:
    patch(BASE / 'marques' / 'index.html')
    for slug in MODULES:
        patch(BASE / 'marques' / slug / 'index.html', slug)
        print(f'✓ brand design fixes: {slug}')
    print('✓ brand hub design assets')


if __name__ == '__main__':
    main()
