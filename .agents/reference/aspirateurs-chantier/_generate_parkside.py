#!/usr/bin/env python3
"""Evidence-led Parkside brand-hub generator.

Bespoke rendering layer for /marques/parkside/. The shared brand workflow stays
common, but Parkside is treated as a stock/generation/usage decision rather than
a stable professional catalogue.

Desk research only. Evidence checked 2026-09-11.
"""
from pathlib import Path
from html import escape
import json
import re

BASE = Path(__file__).resolve().parent
UPDATED_DISPLAY = "11/09/2026"
UPDATED_ISO = "2026-09-11"
TITLE = "Aspirateurs Parkside : PWD, PAWD X20V, filtres et limites chantier"
DESC = "Parkside : choisir entre PWD 12/20/25/30 et PAWD X20V, comprendre générations, IAN, sacs, prise outil, nettoyage du filtre et limites en poussière fine."

SOURCES = [
    ("S1", "Lidl France — Parkside PWD 12 B1", "https://www.lidl.fr/p/parkside-aspirateur-eau-et-poussiere-pwd-12-b1/p100406420", "primary"),
    ("S2", "Lidl France — Parkside PWD 20 C3", "https://www.lidl.fr/p/parkside-aspirateur-eau-et-poussiere-pwd-20-c3-19-8-l-1300-w/p100397254", "primary"),
    ("S3", "Lidl France — Parkside PWD 25 C4", "https://www.lidl.fr/p/parkside-aspirateur-eau-et-poussiere-pwd-25-c4-25-l-1400-w/p100395330", "primary"),
    ("S4", "Lidl France — Parkside PWD 30 C1", "https://www.lidl.fr/p/parkside-aspirateur-eau-et-poussiere-pwd-30-c1/p100407117", "primary"),
    ("S5", "Lidl France — Parkside PAWD 20-Li A1", "https://www.lidl.fr/p/parkside-aspirateur-eau-et-poussiere-sans-fil-pawd-20-li-a1-8-l-20-v/p100406180", "primary"),
    ("S6", "Parkside — recherche de manuels par référence IAN", "https://parkside-diy.com/fr/service/manuals", "primary"),
    ("S7", "Parkside — service, garantie et pièces de rechange", "https://parkside-diy.com/fr/service", "primary"),
    ("S8", "Lidl France — sacs 20 L compatibles PWD 12/PWD 20", "https://www.lidl.fr/p/parkside-sacs-pour-aspirateur/p100397672", "primary"),
    ("S9", "Lidl France — sacs 30 L compatibles PWD 25/PWD 30", "https://www.lidl.fr/p/parkside-sacs-pour-aspirateur-30-l/p100396593003", "primary"),
    ("S10", "BricoZone — retours d'usage Parkside PWD en rénovation", "https://www.bricozone.be/t/aspirateur-de-chantier-aspirer-tout-couplage-ponceuse-rainureuse.160266/", "user_experience"),
]


def sources_html():
    return "".join(
        f'<li><a href="{escape(url)}" rel="nofollow noopener">{escape(label)}</a> <small>({escape(ref)})</small></li>'
        for ref, label, url, _kind in SOURCES
    )


def article():
    return f'''<!-- BRAND_CONTENT_START -->
<div class="answer-box"><p><strong>Chez Parkside, la première question n'est pas « 20, 25 ou 30 litres ? ».</strong> Il faut d'abord décider si vous cherchez un aspirateur eau/poussière filaire pour le bricolage, un petit modèle mobile X20V, ou un véritable extracteur pour poussières fines soutenues. Ensuite seulement viennent la capacité, la prise outil et le prix. La référence exacte — suffixe compris — et l'IAN sont essentiels pour retrouver le bon manuel, les sacs et les filtres.</p></div>

<h2 id="achat-parkside">Parkside s'achète comme une offre datée, pas comme un catalogue professionnel figé</h2>
<p>Au 11 septembre 2026, Lidl France référence simultanément les <strong>PWD 12 B1, PWD 20 C3, PWD 25 C4 et PWD 30 C1</strong>, ainsi qu'un <strong>PAWD 20-Li A1</strong> sans fil de la plateforme X20V Team. Cela permet enfin de comparer une vraie gamme actuelle, mais il faut garder une particularité Parkside en tête : les suffixes et disponibilités changent plus vite qu'une gamme professionnelle stabilisée sur plusieurs années.</p>
<p>Le nom « PWD 30 » ne suffit donc pas pour commander un filtre ou reprendre une ancienne recommandation. Un PWD 30 C1 actuel n'est pas automatiquement identique à un ancien PWD 30 A1 ou à une série PNTS. Pour un appareil déjà possédé, la démarche la plus sûre est de relever <strong>la référence complète et l'IAN</strong> sur la plaque signalétique, puis d'utiliser la recherche de manuels Parkside.</p>
<p>Cette logique change aussi la manière de lire un prix promotionnel : la bonne affaire n'est pas le modèle le moins cher du jour, mais celui dont les fonctions et consommables correspondent à votre usage réel.</p>

<h2 id="pwd-pawd">PWD filaire ou PAWD X20V : c'est le premier embranchement utile</h2>
<p>Les PWD actuels sont des aspirateurs eau/poussière sur secteur. Le <strong>PAWD 20-Li A1</strong> suit une autre logique : cuve de 8 L, 60 AirWatt annoncés, modes Eco et Power, 3,6 kg sans batterie et compatibilité X20V Team. Lidl recommande une batterie 4 Ah, vendue séparément.</p>
<p>Le PAWD est donc intéressant pour nettoyer une voiture, intervenir rapidement dans un garage ou suivre de petits travaux sans chercher une prise. Il ne faut pas le lire comme un « PWD 30 sans câble » : le volume, la puissance d'aspiration annoncée et l'autonomie disponible appartiennent à une autre catégorie d'usage.</p>
<p>Si la mobilité est votre contrainte principale, comparez-le avec notre <a href="/comparatifs/aspirateur-chantier-sans-fil/">comparatif des aspirateurs de chantier sans fil</a>. Si vous cherchez surtout à aspirer eau, gravats et saletés de rénovation, les PWD filaires restent le point de départ logique.</p>

<h2 id="formats-actuels">PWD 12, 20, 25 et 30 : la montée en taille apporte surtout capacité et fonctions</h2>
<div class="table-wrap"><table><thead><tr><th>Référence actuelle</th><th>Données Lidl</th><th>Ce que cela change</th></tr></thead><tbody>
<tr><td>PWD 12 B1</td><td>12 L brut · 1 200 W · env. 180 AirWatt</td><td>Très compact, logique pour voiture, garage et appoint.</td></tr>
<tr><td>PWD 20 C3</td><td>19,8 L · 1 300 W · 200 AirWatt</td><td>Premier format réellement polyvalent pour bricolage courant.</td></tr>
<tr><td>PWD 25 C4</td><td>25 L · 1 400 W · 240 AirWatt</td><td>Plus de volume et nettoyage du filtre par interrupteur.</td></tr>
<tr><td>PWD 30 C1</td><td>30 L brut / 22,3 L net · 1 500 W · max. 260 AirWatt</td><td>Prise outil automatique, post-fonctionnement court, débit réglable et tuyau de 3 m.</td></tr>
</tbody></table></div>
<p>Cette progression ne doit pas être transformée en classement absolu. Un PWD 12 de 3,1 kg environ peut être plus rationnel qu'un PWD 30 de 8,5 kg si l'appareil doit être porté souvent. À l'inverse, le PWD 30 prend du sens lorsque la prise outil, le rayon d'action et la capacité sont effectivement utilisés.</p>
<p>Pour un achat orienté uniquement capacité et polyvalence eau/poussière, notre <a href="/comparatifs/aspirateur-eau-poussiere/">comparatif eau et poussière</a> permet de sortir du seul univers Parkside.</p>

<h2 id="fonctions-chantier">Prise outil et bouton de nettoyage : utiles, mais ce ne sont pas des classes de poussière</h2>
<p>Le <strong>PWD 30 C1</strong> est la référence Parkside actuelle la plus intégrée au travail avec un outil : prise avec marche/arrêt automatique jusqu'à 2 200 W, court post-fonctionnement pour reprendre la poussière résiduelle, régulation du débit d'air et nettoyage du filtre par bouton. Le <strong>PWD 25 C4</strong> dispose lui aussi d'un nettoyage du filtre commandé par interrupteur.</p>
<p>Ces fonctions améliorent le confort, mais un nettoyage manuel déclenché par bouton n'est pas l'équivalent d'un décolmatage automatique qui maintient périodiquement le filtre pendant de longues séquences. C'est particulièrement important avec du ponçage ou une rainureuse, où le colmatage peut devenir la contrainte principale avant même la puissance moteur.</p>
<p>Autre limite à garder explicite : les fiches officielles actuelles consultées pour ces PWD et le PAWD ne les présentent pas comme aspirateurs de sécurité de classe L, M ou H. Sans documentation de la référence exacte attestant une classe, il ne faut pas en déduire une à partir des watts, d'un filtre plissé ou de la mention « poussière de ponçage ». Pour ces usages, commencez par le <a href="/guides/classes-l-m-h/">guide des classes L/M/H</a> et le <a href="/guides/decolmatage-automatique/">guide du décolmatage automatique</a>.</p>

<h2 id="ian-consommables">IAN, sacs et filtres : Parkside oblige à raisonner par génération</h2>
<p>Parkside donne un bon indice de compatibilité dans ses consommables actuels. Les sacs 20 L commercialisés par Lidl sont annoncés pour les <strong>PWD 12, PWD 20, PNTS 1250 et PNTS 1300</strong>. Une autre famille de sacs 30 L couvre les <strong>PNTS 1400, PNTS 1500, PWD 25 et PWD 30</strong>. Cela montre pourquoi « sac Parkside universel » est une mauvaise méthode d'achat.</p>
<p>Pour un appareil ancien, l'IAN devient particulièrement utile : Parkside indique que ce numéro figure sur la plaque signalétique et permet de retrouver le bon manuel. Le service officiel prévoit aussi un canal pour les pièces de rechange et les réparations. Cette infrastructure est plus rassurante qu'une simple promotion Lidl, mais elle ne supprime pas la nécessité de vérifier chaque consommable.</p>
<p>Avant achat, vérifiez donc la famille de sacs, le filtre sec/humide requis, le diamètre de raccord et la disponibilité du consommable. Notre page sur les <a href="/accessoires/sacs-aspirateur-chantier/">sacs d'aspirateur de chantier</a> aide à traiter cette question séparément du choix de la machine.</p>

<h2 id="usage-limite">La vraie frontière Parkside apparaît avec la poussière fine soutenue</h2>
<p>Les retours d'utilisateurs à long terme sont utiles ici à condition de ne pas les transformer en test normatif. Dans une discussion BricoZone de mars 2026, des propriétaires d'anciens PWD rapportent plusieurs années de rénovation avec gravats, sciure et eau. L'un d'eux précise toutefois avoir loué un aspirateur professionnel pour une rainureuse et souligne l'absence de décolmatage automatique.</p>
<p>Ce signal est cohérent avec l'architecture actuelle des PWD : Parkside peut être très pertinent pour nettoyer après les travaux, aspirer eau et débris ou accompagner ponctuellement une ponceuse. Plus l'aspiration devient une fonction de production continue — rainurage, ponçage intensif, poussière fine réglementée — plus la stabilité du débit, la classe de poussière et la gestion automatique du filtre prennent le dessus sur le prix d'achat.</p>
<p>Nous n'avons pas testé physiquement ces machines. Les caractéristiques restent celles publiées par Lidl/Parkside et les retours communautaires servent uniquement à identifier des points de vigilance.</p>

<h2 id="quel-parkside">Quel Parkside regarder selon votre usage ?</h2>
<div class="table-wrap"><table><thead><tr><th>Besoin dominant</th><th>Point de départ</th><th>Pourquoi</th><th>Point de vigilance</th></tr></thead><tbody>
<tr><td>Voiture, cave, petit nettoyage</td><td>PWD 12 B1</td><td>Compact, léger, eau/poussière.</td><td>Petite cuve et fonctions chantier limitées.</td></tr>
<tr><td>Bricolage polyvalent à petit budget</td><td>PWD 20 C3</td><td>Format intermédiaire simple.</td><td>Vérifier que les fonctions du 25/30 ne vous manquent pas.</td></tr>
<tr><td>Rénovation domestique avec plus de volume</td><td>PWD 25 C4</td><td>25 L et nettoyage du filtre par interrupteur.</td><td>Pas de prise outil documentée sur la fiche actuelle.</td></tr>
<tr><td>Scie/ponceuse occasionnelle avec démarrage automatique</td><td>PWD 30 C1</td><td>Prise outil, post-fonctionnement, débit réglable.</td><td>Nettoyage du filtre manuel, pas de classe L/M/H documentée.</td></tr>
<tr><td>Mobilité X20V et petits travaux</td><td>PAWD 20-Li A1</td><td>8 L, 60 AirWatt, Eco/Power, batterie X20V.</td><td>Batterie séparée et catégorie de puissance différente des PWD filaires.</td></tr>
</tbody></table></div>
<p>Si votre besoin principal est une poussière fine soutenue ou réglementée, ne cherchez pas le « meilleur Parkside » : changez d'abord de catégorie de produit et comparez des extracteurs dont la classe et le système de décolmatage sont documentés. Pour un usage domestique ou une rénovation ponctuelle, Parkside reste en revanche intéressant précisément parce qu'il concentre beaucoup de fonctions à un coût d'entrée bas.</p>
<p>Pour continuer selon l'usage plutôt que la marque, consultez <a href="/usages/aspirateur-bricolage-renovation/">bricolage et rénovation</a>, <a href="/guides/prise-asservie/">la prise asservie</a> ou le <a href="/comparatifs/petit-aspirateur-de-chantier/">comparatif petit format</a>.</p>

<h2 id="sources">Sources consultées</h2>
<p>Les caractéristiques et compatibilités proviennent en priorité des fiches Lidl/Parkside consultées le {UPDATED_DISPLAY}. Les disponibilités et promotions pouvant évoluer, elles ne sont pas utilisées comme critères éditoriaux durables. Le retour communautaire est traité comme un signal d'usage, jamais comme une preuve de certification ou de performance normalisée.</p>
<ul>{sources_html()}</ul>
<p><small>Mise à jour : {UPDATED_DISPLAY}. Analyse documentaire, sans test physique. Les liens affiliés éventuels n'influencent ni les caractéristiques retenues ni l'orientation éditoriale.</small></p>
<!-- BRAND_CONTENT_END -->'''


def toc_html():
    items = [
        ("achat-parkside", "Comment acheter Parkside"),
        ("pwd-pawd", "PWD ou PAWD X20V"),
        ("formats-actuels", "PWD 12 à 30"),
        ("fonctions-chantier", "Fonctions chantier et classes"),
        ("ian-consommables", "IAN et consommables"),
        ("usage-limite", "Limite en poussière fine"),
        ("quel-parkside", "Quel Parkside choisir ?"),
        ("sources", "Sources"),
    ]
    return "".join(f'<a href="#{escape(anchor)}">{escape(label)}</a>' for anchor, label in items)


def replace_once(pattern, repl, text, label, flags=0):
    out, count = re.subn(pattern, repl, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f'{label}: expected one replacement, got {count}')
    return out


def patch_page():
    path = BASE / "marques" / "parkside" / "index.html"
    html = path.read_text(encoding="utf-8")
    html = replace_once(r'<title>.*?</title>', f'<title>{escape(TITLE)}</title>', html, 'title', re.S)
    html = replace_once(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{escape(DESC, quote=True)}">', html, 'meta')
    html = replace_once(r'<h1 style="margin-top:10px;">.*?</h1>', f'<h1 style="margin-top:10px;">{escape(TITLE)}</h1>', html, 'h1', re.S)
    html = replace_once(r'<p class="lead">.*?</p>', f'<p class="lead">{escape(DESC)}</p>', html, 'lead', re.S)
    html = replace_once(r'<span class="meta-tag">[^<]*</span>', f'<span class="meta-tag">Vérifié : {UPDATED_DISPLAY}</span>', html, 'verified')
    html = replace_once(r'<!-- BRAND_CONTENT_START -->.*?<!-- BRAND_CONTENT_END -->', article(), html, 'article', re.S)
    html = replace_once(
        r'(<div class="sidebar-box-head">Sommaire</div>\s*<div class="sidebar-box-body">\s*<nav class="toc-list">).*?(</nav>)',
        lambda m: m.group(1) + toc_html() + m.group(2),
        html,
        'toc',
        re.S,
    )
    path.write_text('\n'.join(line.rstrip() for line in html.splitlines()) + '\n', encoding='utf-8')


def data_record():
    evidence = [
        {"ref": ref, "status": "VERIFIED" if kind == "primary" else "SUPPORTED", "tier": 1 if kind == "primary" else 4, "source": url, "source_type": kind, "label": label}
        for ref, label, url, kind in SOURCES
    ]
    source_map = {ref: {"label": label, "url": url, "source_type": kind} for ref, label, url, kind in SOURCES}
    return {
        "slug": "parkside",
        "brand": "Parkside",
        "page_type": "BRAND_HUB",
        "updated_at": UPDATED_ISO,
        "source_of_truth": "_generate_parkside.py",
        "structure_strategy": "bespoke_stock_generation_use_case_logic",
        "recovery_verdict": "DEEP_REWRITE",
        "entity_map": {
            "brand": "Parkside",
            "families": ["PWD filaire", "PAWD X20V Team", "anciennes séries PNTS"],
            "products": ["PWD 12 B1", "PWD 20 C3", "PWD 25 C4", "PWD 30 C1", "PAWD 20-Li A1"],
            "technologies": ["X20V Team", "prise outil automatique", "nettoyage du filtre par bouton", "IAN"],
            "use_cases": ["voiture", "garage", "bricolage", "rénovation domestique", "aspiration eau/poussière", "ponçage occasionnel"],
            "competitors": ["Kärcher", "Bosch", "Makita", "Festool", "DeWalt", "Nilfisk", "Mirka"],
        },
        "brand_positioning": {
            "summary": "Parkside se choisit comme une offre de bricolage datée et référencée précisément : type d'usage, filaire ou X20V, fonctions utiles, puis génération/IAN et consommables.",
            "core_decisions": [
                "PWD filaire ou PAWD X20V selon mobilité et charge de travail ?",
                "quelle capacité et quelles fonctions sont réellement utiles ?",
                "la poussière exige-t-elle une classe ou un décolmatage automatique absent de cette catégorie ?",
                "quels sacs, filtres et manuels correspondent à la génération exacte ?",
            ],
        },
        "evidence": evidence,
        "key_claims": [
            {"claim": "PWD 12 B1, PWD 20 C3, PWD 25 C4 et PWD 30 C1 sont des références actuelles Lidl France consultées le 11/09/2026.", "evidence_refs": ["S1", "S2", "S3", "S4"], "status": "VERIFIED"},
            {"claim": "PAWD 20-Li A1 est un modèle X20V Team 8 L annoncé à 60 AirWatt, vendu sans batterie ni chargeur.", "evidence_refs": ["S5"], "status": "VERIFIED"},
            {"claim": "PWD 30 C1 dispose d'une prise outil automatique jusqu'à 2200 W, d'un court post-fonctionnement et d'un nettoyage du filtre par bouton.", "evidence_refs": ["S4"], "status": "VERIFIED"},
            {"claim": "Les sacs 20 L et 30 L Parkside documentent deux groupes de compatibilité qui recoupent PWD et anciennes séries PNTS.", "evidence_refs": ["S8", "S9"], "status": "VERIFIED"},
            {"claim": "Parkside recommande l'IAN pour retrouver précisément le manuel correspondant à un appareil.", "evidence_refs": ["S6"], "status": "VERIFIED"},
            {"claim": "Des retours communautaires de rénovation montrent qu'un ancien PWD peut durer sur des usages variés tout en atteignant ses limites sur une rainureuse sans décolmatage automatique.", "evidence_refs": ["S10"], "status": "SUPPORTED"},
        ],
        "internal_links": [
            {"label": "sans fil", "url": "/comparatifs/aspirateur-chantier-sans-fil/"},
            {"label": "eau et poussière", "url": "/comparatifs/aspirateur-eau-poussiere/"},
            {"label": "petit format", "url": "/comparatifs/petit-aspirateur-de-chantier/"},
            {"label": "classes L/M/H", "url": "/guides/classes-l-m-h/"},
            {"label": "décolmatage automatique", "url": "/guides/decolmatage-automatique/"},
            {"label": "prise asservie", "url": "/guides/prise-asservie/"},
            {"label": "sacs", "url": "/accessoires/sacs-aspirateur-chantier/"},
            {"label": "bricolage et rénovation", "url": "/usages/aspirateur-bricolage-renovation/"},
        ],
        "editorial": {
            "desk_research_only": True,
            "affiliate_influence": False,
            "human_validation_required": True,
            "publish_review": "READY_FOR_HUMAN_VALIDATION",
            "workflow_contract_version": 2,
            "run_evidence": ".content/brands/runs/parkside.json",
        },
        "sources": source_map,
    }


def write_ledger():
    path = BASE / ".content" / "brands" / "parkside.yaml"
    path.write_text(json.dumps(data_record(), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    patch_page()
    write_ledger()
    print('✓ parkside evidence-led brand hub')


if __name__ == '__main__':
    main()
