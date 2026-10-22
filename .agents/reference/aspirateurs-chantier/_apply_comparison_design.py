#!/usr/bin/env python3
"""Apply the comparison-cluster design layer after canonical content generation.

Idempotent by design: it scopes JS through `.comparison-page`, adds the shared
script once, and replaces one intent-specific decision module per article page.
CSS is provided by the sitewide /style.css entry point.
"""
from html import escape
from pathlib import Path
import re

BASE = Path(__file__).resolve().parent

MODULES = {
    "meilleur-aspirateur-de-chantier": {
        "layout": "steps",
        "title": "Choisir sans faux vainqueur universel",
        "nodes": [
            ("1", "Poussière et risque", "Commencer par le matériau et la classe requise."),
            ("2", "Mode de travail", "Décider entre mobilité sans fil, outil filaire et usage stationnaire."),
            ("3", "Volume et durée", "Adapter cuve et décolmatage au rythme réel du chantier."),
            ("4", "Comparatif spécialisé", "Basculer vers M, sans fil, eau/poussière ou industriel si nécessaire."),
        ],
    },
    "aspirateur-eau-poussiere": {
        "layout": "axis",
        "title": "Le vrai arbitrage eau / poussière",
        "nodes": [
            ("", "Poussière sèche", "Filtration, sac et protection du filtre restent prioritaires."),
            ("", "Liquides", "Vérifier arrêt flotteur, capacité utile et facilité de vidange."),
            ("", "Usage mixte", "La transition sec/humide doit rester simple et documentée."),
            ("", "Poussière à risque", "Wet/dry ne remplace jamais une classe L/M/H exigée."),
        ],
    },
    "aspirateur-chantier-sans-fil": {
        "layout": "axis",
        "title": "Sans fil : quatre paramètres qui changent le choix",
        "nodes": [
            ("", "Plateforme batterie", "Choisir d'abord l'écosystème déjà possédé ou réellement envisagé."),
            ("", "Classe poussière", "L ou M reste une contrainte distincte de la batterie."),
            ("", "Déclenchement outil", "Auto-Start, télécommande ou activation manuelle changent le flux de travail."),
            ("", "Autonomie", "Comparer des scénarios documentés, pas seulement une tension nominale."),
        ],
    },
    "aspirateur-chantier-sans-sac": {
        "layout": "steps",
        "title": "Sans sac ne signifie pas toujours sans consommable",
        "nodes": [
            ("1", "Conception", "Distinguer une machine réellement conçue sans sac d'un usage occasionnel sans sac."),
            ("2", "Type de déchets", "Liquides, gros débris et poussières fines ne se collectent pas de la même façon."),
            ("3", "Protection filtre", "Le sac peut rester utile pour les poussières fines même si la cuve accepte la collecte directe."),
        ],
    },
    "aspirateur-chantier-puissant": {
        "layout": "axis",
        "title": "Puissance utile : ne pas mélanger les mesures",
        "nodes": [
            ("", "Débit d'air", "Utile pour déplacer un volume d'air, mais dépend du point de mesure."),
            ("", "Dépression", "Utile face aux pertes de charge, sans être un score universel."),
            ("", "Point de mesure", "Turbine, flexible ou appareil complet ne sont pas directement équivalents."),
            ("", "Usage réel", "Poussière, outil, flexible et filtre déterminent ce qui compte vraiment."),
        ],
    },
    "aspirateur-professionnel": {
        "layout": "steps",
        "title": "Professionnel : partir du travail, pas du badge",
        "nodes": [
            ("1", "Risque poussière", "Définir d'abord la classe nécessaire."),
            ("2", "Mobilité", "Intervention mobile, atelier ou gros volume ne demandent pas la même machine."),
            ("3", "Continuité", "Décolmatage et prise outil comptent davantage sur les longues sessions."),
            ("4", "Écosystème", "Batterie, flexible et accessoires peuvent faire basculer la décision."),
        ],
    },
    "aspirateur-industriel": {
        "layout": "axis",
        "title": "Industriel : raisonner par process",
        "nodes": [
            ("", "Matière", "Poussières, huiles, copeaux ou déchets de production impliquent des architectures différentes."),
            ("", "Cycle de service", "Intermittent, continu ou trois-huit change le type de machine requis."),
            ("", "Mobilité", "Mobile lourd, stationnaire ou intégré au process : ce n'est plus un simple critère de poids."),
            ("", "Sécurité", "Classe poussière, ACD et ATEX doivent être vérifiés séparément."),
        ],
    },
    "aspirateur-classe-m": {
        "layout": "steps",
        "title": "Classe M : le prérequis avant les compromis",
        "nodes": [
            ("1", "Certification M", "Écarter toute référence non documentée M lorsque le risque l'exige."),
            ("2", "Mobilité", "Sans fil, compact ou gros filaire répondent à des contraintes différentes."),
            ("3", "Décolmatage", "SFC, AFC, Tact, InfiniClean ou AUTOCLEAN changent la continuité de travail."),
            ("4", "Volume", "Adapter la cuve au rythme de déplacement et de vidange."),
        ],
    },
    "petit-aspirateur-de-chantier": {
        "layout": "axis",
        "title": "Compact : regarder l'encombrement réel",
        "nodes": [
            ("", "Gabarit", "La forme et le rangement comptent autant qu'un nombre de litres."),
            ("", "Masse", "Poids machine, batterie et accessoires déterminent la mobilité réelle."),
            ("", "Cuve utile", "Une petite empreinte peut cacher un compromis sur la fréquence de vidange."),
            ("", "Fonction", "Compact atelier, mobile sans fil et aspirateur eau/poussière ne sont pas interchangeables."),
        ],
    },
}


def module_html(slug, spec):
    nodes = []
    for step, title, text in spec["nodes"]:
        step_attr = f' data-step="{escape(step)}"' if step else ""
        nodes.append(
            f'<div class="comparison-decision-node"{step_attr}>'
            f'<strong>{escape(title)}</strong><span>{escape(text)}</span></div>'
        )
    return (
        f'<section class="comparison-decision-module" data-layout="{escape(spec["layout"])}" '
        f'aria-label="Repères de décision">'
        '<span class="comparison-decision-kicker">Repères de décision</span>'
        f'<h2 class="comparison-decision-title">{escape(spec["title"])}</h2>'
        f'<div class="comparison-decision-flow">{"".join(nodes)}</div></section>'
    )


def ensure_body_class(html):
    match = re.search(r"<body([^>]*)>", html)
    if not match:
        raise RuntimeError("body tag missing")
    attrs = match.group(1)
    class_match = re.search(r'class="([^"]*)"', attrs)
    if class_match:
        classes = class_match.group(1).split()
        if "comparison-page" not in classes:
            classes.append("comparison-page")
        attrs = attrs[:class_match.start()] + f'class="{" ".join(classes)}"' + attrs[class_match.end():]
    else:
        attrs += ' class="comparison-page"'
    return html[:match.start()] + f"<body{attrs}>" + html[match.end():]


def apply_assets(html):
    if '/comparison-pages.js' not in html:
        html = html.replace('</body>', '  <script src="/comparison-pages.js" defer></script>\n</body>', 1)
    return html


def apply_module(html, slug):
    spec = MODULES.get(slug)
    if not spec:
        return html
    html = re.sub(r'\n?<section class="comparison-decision-module".*?</section>\n?', '\n', html, flags=re.S)
    module = module_html(slug, spec)
    answer = re.search(r'(<div class="answer-box">.*?</div>)', html, flags=re.S)
    if not answer:
        raise RuntimeError(f"{slug}: answer-box missing")
    return html[:answer.end()] + '\n' + module + html[answer.end():]


def main():
    root = BASE / "comparatifs"
    pages = sorted(root.glob("*/index.html"))
    hub = root / "index.html"
    if hub.exists():
        pages.insert(0, hub)

    for page in pages:
        slug = "" if page == hub else page.parent.name
        html = page.read_text(encoding="utf-8")
        html = ensure_body_class(html)
        html = apply_assets(html)
        html = apply_module(html, slug)
        page.write_text(html, encoding="utf-8")

    print(f"✓ comparison design layer applied to {len(pages)} pages")


if __name__ == "__main__":
    main()
