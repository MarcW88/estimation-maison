#!/usr/bin/env python3
"""Evidence-led Kärcher brand-hub generator.

This is the bespoke rendering layer for /marques/karcher/. It runs after the
shared shell/seed and generic brand overrides, but the editorial architecture
comes from the persisted brand workflow run, not from the BRAND_HUB page type.

Desk research only. Evidence checked 2026-09-11.
"""
from pathlib import Path
from html import escape
import json
import re

BASE = Path(__file__).resolve().parent
UPDATED_DISPLAY = "11/09/2026"
UPDATED_ISO = "2026-09-11"
TITLE = "Aspirateurs Kärcher : choisir entre WD, NT, Tact et classes M/H"
DESC = "Kärcher WD ou NT : comprendre les gammes, Tact, Ap, classes M/H, ACD, volumes 30/50 L et consommables pour choisir selon le chantier."

SOURCES = [
    ("S1", "Kärcher — comment choisir un aspirateur WD", "https://www.kaercher.com/fr/home-garden/comment-choisir-son-aspirateur-eau-et-poussieres-wd.html", "primary"),
    ("S2", "Kärcher WD 7 Control P S 30/6/35/T", "https://www.kaercher.com/fr/home-garden/aspirateurs-eau-et-poussieres/wd-7-control-p-s-30-6-35-t-eu-iii-16283860.html", "primary"),
    ("S3", "Kärcher Professional — aspirateurs eau et poussières", "https://www.kaercher.com/fr/professional/aspirateurs-eau-et-poussieres.html", "primary"),
    ("S4", "Kärcher — aspirateurs de sécurité", "https://www.kaercher.com/fr/professional/aspirateurs-eau-et-poussieres/aspirateurs-de-securite.html", "primary"),
    ("S5", "Kärcher NT 30/1 Tact Te M ACD", "https://www.kaercher.com/fr/professional/aspirateurs-eau-et-poussieres/aspirateurs-de-securite/nt-30-1-tact-te-m-acd-11482350.html", "primary"),
    ("S6", "Kärcher NT 50/1 Tact Te M ACD", "https://www.kaercher.com/fr/professional/aspirateurs-eau-et-poussieres/aspirateurs-de-securite/nt-50-1-tact-te-m-acd-11484350.html", "primary"),
    ("S7", "Kärcher — sacs rénovation WD/KWD 4–7 KFI 489", "https://www.kaercher.com/fr/accessoires/sachet-filtre-ouate-renovation-wd-kwd-4-5-6-kfi-489-paquet-de-4-28633550.html", "primary"),
    ("S8", "Kärcher — sacs non tissés NT 30/1", "https://www.kaercher.com/fr/accessoires/sacs-filtrants-non-tisses-5-piece-s-nt-30-1-28891540.html", "primary"),
    ("S9", "INRS — aspirateurs de chantier : évolution des performances en cours d’utilisation", "https://www.inrs.fr/inrs/recherche/etudes-publications-communications/doc/communication.html?refINRS=NOETUDE%2FC2026-013", "independent_authority"),
    ("S10", "INRS — prévention du risque amiante", "https://www.inrs.fr/risques/amiante/prevention-risque-amiante.html", "independent_authority"),
    ("S11", "Ideal Home — test Kärcher WD 6 P Premium", "https://www.idealhome.co.uk/buying-guide-reviews/karcher-wd-6-p-premium-wet-and-dry-vacuum-cleaner-review-304161", "independent_test"),
    ("S12", "Homes & Gardens — test Kärcher WD 6 P", "https://www.homesandgardens.com/solved/karcher-wd-6-p-vacuum-review", "independent_test"),
]


def sources_html():
    return "".join(
        f'<li><a href="{escape(url)}" rel="nofollow noopener">{escape(label)}</a> <small>({escape(ref)})</small></li>'
        for ref, label, url, _kind in SOURCES
    )


def article():
    return f'''<!-- BRAND_CONTENT_START -->
<div class="answer-box"><p><strong>Le premier choix chez Kärcher n’est pas un modèle : c’est WD ou NT.</strong> Les WD Home &amp; Garden conviennent surtout au garage, aux liquides, aux gravats courants et à la rénovation domestique. Les NT Professional ajoutent des architectures de filtre et de décolmatage pensées pour un usage plus soutenu ; certaines références sont en plus certifiées M ou H. Un WD très puissant ne devient donc pas un aspirateur de sécurité, et un NT H n’est pas automatiquement « meilleur » pour tous les travaux.</p></div>

<h2 id="wd-vs-nt">WD ou NT : séparer le nettoyage intensif de la gestion des poussières professionnelles</h2>
<p>Kärcher entretient deux univers qui se recouvrent visuellement mais ne répondent pas au même cahier des charges. La gamme WD vise l’eau et la poussière dans la maison, le garage, l’atelier et la rénovation. Le sélecteur officiel de la marque oriente les usages occasionnels vers WD 2/3, les usages plus réguliers vers WD 3/4 et les travaux de bricolage plus importants vers WD 5/6. Le <strong>WD 7 Control</strong> ajoute aujourd’hui une couche de confort intéressante : cuve de 30&nbsp;L, prise pour outil filaire et télécommande qui peut détecter les vibrations d’un outil sans fil pour déclencher l’aspirateur.</p>
<p>Ce dernier point est utile si vous poncez ou sciez avec des outils à batterie, mais il ne change pas la nature de la gamme. Les WD restent des aspirateurs eau/poussière Home &amp; Garden. Si votre décision part d’une poussière dont la classe de sécurité doit être documentée, il faut regarder la gamme NT appropriée plutôt que monter simplement du WD 5 au WD 7.</p>
<p>Pour un besoin essentiellement domestique, nos fiches <a href="/modeles/karcher-wd5/">Kärcher WD5</a> et <a href="/modeles/karcher-wd6/">Kärcher WD6</a> permettent de descendre au niveau modèle. Pour comparer cette logique au reste du marché, utilisez plutôt le <a href="/comparatifs/aspirateur-eau-poussiere/">comparatif eau et poussière</a>.</p>

<h2 id="nt-architecture">Chez les NT, Ap, Tact et Safety correspondent à des problèmes différents</h2>
<p>« NT » ne signifie pas à lui seul « aspirateur classe M ». Kärcher découpe sa gamme professionnelle en plusieurs logiques. Les modèles Standard/Classic sont pensés pour les salissures grossières et les liquides ; les <strong>Ap</strong> ajoutent un décolmatage semi-automatique pour des quantités petites à moyennes de poussières fines ; les <strong>Tact</strong> automatisent davantage le nettoyage du filtre pour les charges de poussière plus importantes ; les aspirateurs de sécurité ajoutent ensuite la classe M ou H selon la référence.</p>
<div class="table-wrap"><table><thead><tr><th>Besoin dominant</th><th>Famille Kärcher à examiner</th><th>Ce qui doit décider</th></tr></thead><tbody>
<tr><td>Liquides, déchets grossiers, nettoyage pro</td><td>NT Standard / Classic</td><td>Robustesse, capacité et facilité de vidage.</td></tr>
<tr><td>Poussière fine intermittente</td><td>NT Ap</td><td>Le décolmatage semi-automatique suffit-il au rythme de travail ?</td></tr>
<tr><td>Poussière fine soutenue</td><td>NT Tact</td><td>Maintien du débit, raccord à l’outil et fréquence de décolmatage.</td></tr>
<tr><td>Poussière nécessitant une classe documentée</td><td>NT Safety M/H</td><td>Classe requise, système complet et procédure de collecte.</td></tr>
</tbody></table></div>
<p>Cette lecture évite un mauvais achat fréquent : payer un NT Tact M pour nettoyer occasionnellement un garage, ou au contraire choisir un gros WD parce que ses chiffres d’aspiration semblent élevés alors que le chantier exige une classe de poussière déterminée.</p>

<h2 id="tact-acd">Tact, classe M/H et ACD : trois notions à ne pas fusionner</h2>
<p><strong>Tact</strong> concerne le maintien du filtre. Sur les modèles Tact M/H actuels, Kärcher indique que la machine mesure la pression différentielle et choisit elle-même un intervalle de nettoyage du filtre — 7, 15 ou 60 secondes, voire aucun déclenchement si ce n’est pas nécessaire. La fonction vise donc à limiter le colmatage ; elle ne définit pas à elle seule la classe de sécurité.</p>
<p><strong>M et H</strong> décrivent un autre niveau de décision. Les NT 30/1 et 50/1 Tact Te M ACD sont annoncés avec une efficacité de filtration de 99,9&nbsp;% et une surveillance électronique du débit. Les variantes H utilisent une architecture de filtration plus exigeante. Il serait pourtant dangereux d’en déduire qu’un H est toujours le meilleur choix : l’INRS a montré en laboratoire que, sur les modèles testés, les aspirateurs H pouvaient se colmater plus rapidement que les M. La bonne logique reste donc de choisir la classe exigée par le risque puis d’évaluer le maintien des performances, pas de surclasser « au cas où ».</p>
<p><strong>ACD</strong> est encore autre chose. Kärcher l’emploie pour des machines conçues pour la collecte de poussières combustibles selon le cadre de la norme IEC&nbsp;60335-2-69:2021. Cela ne doit pas être transformé en équivalent générique d’une machine ATEX pour atmosphère explosive : Kärcher commercialise séparément un NT 75/1 Me Ec H Z22 pour la zone&nbsp;22. Si votre chantier implique un risque d’explosion, la référence exacte et l’évaluation de zone priment donc sur le seul logo ACD.</p>
<p>Enfin, pour l’amiante en France, l’INRS demande plus qu’une simple mention « classe H » : filtre à très haute efficacité, préfiltration, dispositif de fermeture et collecte adaptée font partie du cahier des charges. Une page produit H ne remplace donc jamais la vérification du matériel et du mode opératoire. Notre <a href="/guides/classes-l-m-h/">guide des classes L/M/H</a> détaille cette hiérarchie.</p>

<h2 id="30-40-50">NT 30, 40 ou 50 L : la différence est surtout la capacité et la mobilité</h2>
<p>La nomenclature peut donner l’impression qu’un NT 50 « aspire plus » qu’un NT 30. Sur les deux références actuelles <strong>NT 30/1 Tact Te M ACD</strong> et <strong>NT 50/1 Tact Te M ACD</strong>, Kärcher publie pourtant les mêmes maxima : 74&nbsp;l/s et 273&nbsp;mbar, avec un moteur annoncé à 1&nbsp;380&nbsp;W. Ce qui change réellement, c’est la cuve et le poids : 30&nbsp;L et 14,2&nbsp;kg pour le 30/1 contre 50&nbsp;L et 19&nbsp;kg pour le 50/1, ce dernier ajoutant notamment un guidon et un flexible de vidange.</p>
<p>Le 30&nbsp;L est donc plus logique lorsque la machine change souvent d’étage, de véhicule ou de pièce. Le 50&nbsp;L devient intéressant quand les vidages interrompent réellement le travail ou quand les liquides et gros déchets représentent une part importante du besoin. Le 40&nbsp;L occupe l’intervalle entre les deux dans la gamme Tact. Ce choix de volume vient <em>après</em> la classe et le système de filtre, pas avant.</p>
<p>Si votre besoin est principalement classe M, comparez ensuite les marques sur des bases équivalentes avec notre <a href="/comparatifs/aspirateur-classe-m/">comparatif des aspirateurs classe M</a>. Pour le fonctionnement du filtre, voir aussi le guide sur le <a href="/guides/decolmatage-automatique/">décolmatage automatique</a>.</p>

<h2 id="consommables">Sacs, filtres et raccords : le coût réel se joue après l’achat de la machine</h2>
<p>Kärcher a l’avantage d’un catalogue de consommables assez structuré, mais la compatibilité dépend fortement de la famille et parfois de la référence. Côté WD, les sacs rénovation KFI&nbsp;489 sont listés pour les WD&nbsp;4 à WD&nbsp;7 et visent les travaux produisant beaucoup de poussière fine ; les WD&nbsp;4/5/6 partagent aussi un filtre plissé plat dédié. Côté NT&nbsp;30/1, Kärcher référence des sacs non tissés classe M compatibles avec plusieurs variantes Ap et Tact.</p>
<p>La logique change encore en classe H, où la collecte et l’élimination des poussières deviennent partie intégrante du système. Il ne suffit donc pas de comparer le prix de la machine : vérifiez le filtre exact, les sacs autorisés, la possibilité d’aspirer sans sac dans votre usage, le diamètre du flexible, le raccord à l’outil et la disponibilité des pièces.</p>
<p>Cette vérification est particulièrement importante avec une <a href="/usages/aspirateur-ponceuse/">ponceuse</a> : une prise asservie ou Tact ne compense pas un raccord mal adapté. Notre guide sur la <a href="/guides/prise-asservie/">prise asservie</a> explique ce que le démarrage automatique change réellement dans le workflow.</p>

<h2 id="preuves-independantes">Ce que les sources indépendantes ajoutent — et ce qu’elles ne prouvent pas</h2>
<p>Deux essais indépendants du WD&nbsp;6 convergent sur un profil assez clair : c’est une grosse machine eau/poussière adaptée aux travaux salissants, avec un réel intérêt pour les liquides, la sciure et les déchets de rénovation, mais son volume et son encombrement sont des contreparties visibles. Un test Ideal Home le juge très cohérent pour le bricolage lourd avec espace de stockage ; un test Homes &amp; Gardens souligne également la puissance et l’entretien pratique du filtre, tout en étant plus critique sur la tête de sol dans certains usages domestiques.</p>
<p>Nous n’extrapolons pas ces observations aux NT ni au WD&nbsp;7 : elles servent uniquement à rappeler qu’un grand WD gagne en capacité au prix d’un appareil plus encombrant. Pour les NT M/H, la source indépendante la plus utile retenue ici n’est pas un « comparatif produit », mais l’étude INRS sur l’évolution du débit avec le colmatage. Elle confirme qu’en aspiration de poussières fines, la performance doit être lue dans le temps et avec le système de décolmatage, pas seulement à travers le débit maximal publié à neuf.</p>
<p>Cette page reste donc une analyse documentaire. Nous n’avons pas testé physiquement ces machines et nous ne transformons pas un avis utilisateur, un test tiers ou une donnée fabricant en observation maison.</p>

<h2 id="quel-karcher">Quel Kärcher regarder selon votre chantier ?</h2>
<div class="table-wrap"><table><thead><tr><th>Situation</th><th>Point de départ</th><th>À vérifier avant achat</th></tr></thead><tbody>
<tr><td>Garage, voiture, liquide, bricolage occasionnel</td><td>WD 2 à WD 4</td><td>Volume et accessoires réellement nécessaires.</td></tr>
<tr><td>Rénovation régulière sans exigence de classe de poussière</td><td>WD 5 / WD 6 ; WD 7 si ses fonctions de contrôle sont utiles</td><td>Encombrement, sac/filtre et raccord à l’outil.</td></tr>
<tr><td>Poussière fine professionnelle sans besoin de classe M/H spécifique</td><td>NT Ap ou Tact selon intensité</td><td>Fréquence de colmatage, captage à la source et consommation de sacs.</td></tr>
<tr><td>Classe M adaptée au risque</td><td>NT 30/40/50 Tact M selon volume</td><td>Classe exacte, ACD si pertinent, mobilité et méthode de collecte.</td></tr>
<tr><td>Classe H requise</td><td>NT H correspondant au besoin</td><td>Exigences de l’activité ; pour l’amiante, cahier des charges INRS complet.</td></tr>
<tr><td>Atmosphère explosive / Zone 22</td><td>Référence explicitement prévue pour cette zone</td><td>Ne pas assimiler ACD à une certification ATEX universelle.</td></tr>
</tbody></table></div>
<p>Kärcher est particulièrement cohérent si vous voulez rester dans un univers d’aspiration large allant du WD domestique jusqu’aux NT de sécurité. Si votre priorité est plutôt de mutualiser des batteries, coffrets et outils électroportatifs, comparez aussi Makita, DeWalt ou Bosch. Si le ponçage constitue presque tout votre workflow, Festool ou Mirka peuvent proposer une intégration outil-flexible-aspirateur plus centrale à leur offre.</p>

<h2 id="sources">Sources consultées</h2>
<p>Les caractéristiques, statuts de gamme et compatibilités proviennent en priorité des pages Kärcher France consultées le {UPDATED_DISPLAY}. Les points de prévention sont recoupés avec l’INRS ; les deux essais WD&nbsp;6 sont utilisés uniquement pour des observations d’usage propres au modèle testé.</p>
<ul>{sources_html()}</ul>
<p><small>Mise à jour : {UPDATED_DISPLAY}. Analyse documentaire, sans test physique. Les liens affiliés éventuels n’influencent ni les classes, ni les caractéristiques retenues, ni l’orientation éditoriale.</small></p>
<!-- BRAND_CONTENT_END -->'''


def toc_html():
    items = [
        ("wd-vs-nt", "WD ou NT ?"),
        ("nt-architecture", "Ap, Tact et Safety"),
        ("tact-acd", "Tact, M/H et ACD"),
        ("30-40-50", "30, 40 ou 50 L"),
        ("consommables", "Sacs et filtres"),
        ("preuves-independantes", "Preuves indépendantes"),
        ("quel-karcher", "Quel Kärcher ?"),
        ("sources", "Sources"),
    ]
    return "".join(f'<a href="#{escape(anchor)}">{escape(label)}</a>' for anchor, label in items)


def replace_once(pattern, repl, text, label, flags=0):
    out, count = re.subn(pattern, repl, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f'{label}: expected one replacement, got {count}')
    return out


def patch_page():
    path = BASE / "marques" / "karcher" / "index.html"
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
    source_map = {ref: {"label": label, "url": url, "source_type": kind} for ref, label, url, kind in SOURCES}
    return {
        "slug": "karcher",
        "brand": "Kärcher",
        "page_type": "BRAND_HUB",
        "updated_at": UPDATED_ISO,
        "source_of_truth": "_generate_karcher.py",
        "structure_strategy": "bespoke_wd_nt_productivity_safety_cost",
        "recovery_verdict": "DEEP_REWRITE",
        "entity_map": {
            "brand": "Kärcher",
            "families": ["WD Home & Garden", "NT Standard/Classic", "NT Ap", "NT Tact", "NT Safety"],
            "products": [
                "WD 5", "WD 6", "WD 7 Control",
                "NT 30/1 Tact Te M ACD", "NT 40/1 Tact Te M ACD", "NT 50/1 Tact Te M ACD",
                "NT 30/1 Tact Te H ACD", "NT 50/1 Tact Te H ACD", "NT 75/1 Me Ec H Z22",
            ],
            "technologies": ["Tact", "Ap", "ACD", "antistatique", "prise asservie"],
            "use_cases": ["garage", "rénovation", "gravats", "ponçage", "poussières fines", "liquides"],
            "competitors": ["Bosch", "Makita", "Festool", "DeWalt", "Nilfisk", "Mirka", "Parkside"],
        },
        "brand_positioning": {
            "summary": "Kärcher couvre un spectre inhabituellement large, du WD domestique au NT de sécurité. La valeur de la page consiste à router le lecteur vers la bonne architecture avant de comparer les modèles.",
            "core_decisions": [
                "WD ou NT ?",
                "NT Ap, Tact ou Safety ?",
                "classe L/M/H et ACD/Zone 22 selon le risque ?",
                "30, 40 ou 50 L selon mobilité et volume ?",
                "quels sacs, filtres et raccords conditionnent le coût réel ?",
            ],
        },
        "evidence": [
            {"ref": ref, "status": "VERIFIED" if kind == "primary" else "SUPPORTED", "tier": 1 if kind == "primary" else 3, "source": url, "source_type": kind, "label": label}
            for ref, label, url, kind in SOURCES
        ],
        "key_claims": [
            {"claim": "Le sélecteur WD distingue usage occasionnel, régulier et intensif plutôt qu'une classe de sécurité.", "evidence_refs": ["S1"], "status": "VERIFIED"},
            {"claim": "Le WD 7 Control ajoute télécommande Bluetooth et détection de vibrations d'un outil sans fil.", "evidence_refs": ["S2"], "status": "VERIFIED"},
            {"claim": "Les gammes NT Standard/Classic, Ap, Tact et Safety répondent à des charges de poussière et niveaux de sécurité différents.", "evidence_refs": ["S3", "S4"], "status": "VERIFIED"},
            {"claim": "Sur les Tact M/H, le décolmatage peut être piloté selon la pression différentielle et la charge du filtre.", "evidence_refs": ["S3"], "status": "VERIFIED"},
            {"claim": "Les NT 30/1 et 50/1 Tact Te M ACD cités publient 74 l/s et 273 mbar ; leur différence majeure porte donc sur volume et mobilité.", "evidence_refs": ["S5", "S6"], "status": "VERIFIED"},
            {"claim": "ACD ne doit pas être présenté comme équivalent à une certification universelle pour Zone 22.", "evidence_refs": ["S4"], "status": "VERIFIED"},
            {"claim": "Pour l'amiante en France, l'INRS exige un cahier des charges plus complet qu'une simple mention de classe H.", "evidence_refs": ["S10"], "status": "VERIFIED"},
            {"claim": "Les essais indépendants WD6 retenus convergent sur un usage gros travaux/atelier, mais avec un compromis d'encombrement.", "evidence_refs": ["S11", "S12"], "status": "SUPPORTED"},
            {"claim": "L'INRS a observé dans son protocole que les appareils H testés se colmataient plus rapidement que les M testés.", "evidence_refs": ["S9"], "status": "SUPPORTED"},
        ],
        "internal_links": [
            {"label": "Kärcher WD5", "url": "/modeles/karcher-wd5/"},
            {"label": "Kärcher WD6", "url": "/modeles/karcher-wd6/"},
            {"label": "Kärcher NT 30/1 Tact", "url": "/modeles/karcher-nt-30-1-tact/"},
            {"label": "eau et poussière", "url": "/comparatifs/aspirateur-eau-poussiere/"},
            {"label": "classe M", "url": "/comparatifs/aspirateur-classe-m/"},
            {"label": "professionnel", "url": "/comparatifs/aspirateur-professionnel/"},
            {"label": "classes L/M/H", "url": "/guides/classes-l-m-h/"},
            {"label": "décolmatage automatique", "url": "/guides/decolmatage-automatique/"},
            {"label": "prise asservie", "url": "/guides/prise-asservie/"},
            {"label": "ponceuse", "url": "/usages/aspirateur-ponceuse/"},
        ],
        "editorial": {
            "desk_research_only": True,
            "affiliate_influence": False,
            "human_validation_required": True,
            "publish_review": "PENDING",
            "workflow_contract_version": 2,
            "run_evidence": ".content/brands/runs/karcher.json",
        },
        "cluster_audit": {
            "date": "2026-09-10",
            "verdict": "DEEP_REWRITE",
            "reason": "Large range and strong WD/NT distinction were under-developed; evidence layer too manufacturer-heavy and sections too uniformly shallow.",
        },
        "sources": source_map,
    }


def write_ledger():
    path = BASE / ".content" / "brands" / "karcher.yaml"
    path.write_text(json.dumps(data_record(), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    patch_page()
    write_ledger()
    print('✓ karcher evidence-led brand hub')


if __name__ == '__main__':
    main()
