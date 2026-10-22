#!/usr/bin/env python3
"""Evidence-led Makita brand-hub generator.

Bespoke rendering layer for /marques/makita/. The editorial architecture comes
from the persisted v2 brand workflow run. The shared shell/design system stays
common, but Makita is not allowed to inherit a generic BRAND_HUB structure.

Desk research only. Evidence checked 2026-09-11.
"""
from pathlib import Path
from html import escape
import json
import re

BASE = Path(__file__).resolve().parent
UPDATED_DISPLAY = "11/09/2026"
UPDATED_ISO = "2026-09-11"
TITLE = "Aspirateurs Makita : classe L/M, LXT, XGT, AWS et modèles VC"
DESC = "Makita : choisir entre aspirateurs filaires, LXT et XGT, comprendre les classes L/M, AWS, Makpac, InfiniClean, autonomie et consommables."

SOURCES = [
    ("S1", "Makita France — gamme aspiration", "https://www.makita.fr/data/pam/public/Content-Pages/Media/CatalogsAndBrochures/2023_leaflet_aspi_web.pdf", "primary"),
    ("S2", "Makita France — brochure Charpentiers / Couvreurs", "https://www.makita.fr/data/pam/public/Content-Pages/Media/CatalogsAndBrochures/BROCHURE_PRODUIT/makita_leaflet_charpentier_couvreur_-_web.pdf", "primary"),
    ("S3", "Makita VC2512L — fiche produit", "https://www.makita.fr/data/sr/productinfo/generated/vc2512l_fiche_produit.pdf", "primary"),
    ("S4", "Makita France — tract aspiration", "https://www.makita.fr/data/pam/public/content-pages/media/catalogsandbrochures/catalogs/tract_01_2025_vsp_bd.pdf", "primary"),
    ("S5", "Makita VC4210MX — fiche produit", "https://www.makita.fr/data/sr/productinfo/generated/vc4210mx_fiche_produit.pdf", "primary"),
    ("S6", "KlusVisie — essai Makita XGT avec VC004GL", "https://www.klusvisie.nl/gereedschap/makitas-schurende-scheurijzers/19254/", "independent_test"),
    ("S7", "Coolblue — avis utilisateurs Makita VC4210M", "https://www.coolblue.be/fr/produit/816681/makita-vc4210m.html", "user_review_aggregate"),
]


def sources_html():
    return "".join(
        f'<li><a href="{escape(url)}" rel="nofollow noopener">{escape(label)}</a> <small>({escape(ref)})</small></li>'
        for ref, label, url, _kind in SOURCES
    )


def article():
    return f'''<!-- BRAND_CONTENT_START -->
<div class="answer-box"><p><strong>Chez Makita, ne commencez pas par choisir entre LXT et XGT.</strong> Commencez par la classe de poussière nécessaire, puis décidez si le chantier justifie le filaire ou la batterie. AWS, Makpac et les raccords viennent ensuite. Cette hiérarchie évite de payer un écosystème très complet qui ne répond pas au bon risque — ou, à l'inverse, de choisir une machine mobile qui n'a pas la classe requise.</p></div>

<h2 id="matrice-makita">Makita se lit comme une matrice : classe, alimentation, puis workflow</h2>
<p>La difficulté de la gamme Makita vient de l'empilement de plusieurs logiques. Les références <strong>VC</strong> peuvent être filaires ou sur batterie selon la famille ; les solutions mobiles existent en LXT et XGT ; la classe L ou M dépend de la référence exacte ; AWS peut automatiser le démarrage de certains aspirateurs, y compris un modèle filaire via adaptateur. Une lecture « plus le numéro est haut, plus le modèle est professionnel » serait donc trompeuse.</p>
<p>La méthode la plus robuste est de fixer trois choses dans l'ordre. D'abord la classe adaptée au matériau et au risque. Ensuite la source d'énergie : secteur si l'endurance et le débit continu dominent, batterie si la mobilité apporte un gain réel. Enfin l'intégration : prise asservie, AWS, Makpac, diamètre de flexible, sacs et filtres.</p>
<p>Les pages <a href="/modeles/makita-vc2512l/">VC2512L</a> et <a href="/modeles/makita-vc4210mx/">VC4210MX</a> permettent ensuite de descendre au modèle une fois cette matrice clarifiée.</p>

<h2 id="classe-avant-reference">Classe L ou M : la lettre compte davantage que LXT, XGT ou HEPA</h2>
<p>Le <strong>VC2512L</strong> illustre bien l'entrée de gamme chantier filaire Makita : classe L, cuve annoncée à 25&nbsp;L brut avec 21&nbsp;L pour les poussières et 18&nbsp;L pour les liquides, prise outil et décolmatage manuel. Le <strong>VC4210M</strong> répond à une autre contrainte : classe M, cuve 42&nbsp;L brut, surveillance du débit et décolmatage automatique InfiniClean.</p>
<p>Le piège est de laisser l'écosystème masquer cette différence. Une batterie XGT, un filtre HEPA ou AWS ne transforment pas une machine en classe M. Inversement, un aspirateur filaire peut parfaitement être le choix le plus cohérent lorsqu'il apporte la classe, le maintien du débit et l'autonomie dont le chantier a besoin.</p>
<p>Pour une décision liée à la sécurité, utilisez d'abord notre <a href="/guides/classes-l-m-h/">guide L/M/H</a> puis comparez les machines de même classe dans le <a href="/comparatifs/aspirateur-classe-m/">comparatif classe M</a>.</p>

<h2 id="lxt-xgt">Filaire, LXT ou XGT : la mobilité a un coût énergétique et logistique</h2>
<p>Makita traite LXT et XGT comme deux plateformes de batteries distinctes. LXT reste un parc extrêmement large et certaines machines utilisent deux batteries 18&nbsp;V pour augmenter la puissance disponible. XGT vise des applications plus énergivores avec ses propres batteries 40&nbsp;V max et des machines pouvant aller jusqu'à deux batteries XGT.</p>
<p>Pour un aspirateur, cette distinction se traduit moins par une hiérarchie absolue que par un arbitrage. Une machine filaire comme le VC4210M peut travailler sans gestion d'autonomie et fournir un décolmatage automatique continu. Une machine XGT gagne en liberté autour d'une scie ou d'une ponceuse, mais l'autonomie varie fortement avec le niveau d'aspiration et la capacité des batteries.</p>
<p>La documentation Makita du VC004GL illustre cet écart : la marque annonce 220&nbsp;minutes en réglage bas contre 28&nbsp;minutes en réglage haut avec deux batteries XGT 5&nbsp;Ah. Ce ne sont pas des autonomies « normales » à généraliser, mais la démonstration qu'un choix sans fil doit être dimensionné avec le rythme réel du chantier, les batteries déjà possédées et les temps de recharge.</p>

<h2 id="xgt-deux-logiques">VC004GL et VC006GM : deux usages XGT qui ne racontent pas la même histoire</h2>
<p>Le <strong>VC004GL</strong> est un traîneau XGT compact orienté mobilité et raccordement à l'outil. Makita annonce 1,8&nbsp;m³/min, 230&nbsp;mbar, un sac de 15&nbsp;L et AWS. Avec deux emplacements batterie, il peut prolonger la durée de travail sans câble, mais sa valeur dépend directement de votre parc XGT et du niveau d'aspiration utilisé.</p>
<p>Le <strong>VC006GM</strong> change d'échelle : alimentation 2×40&nbsp;V XGT, cuve de 40&nbsp;L pour les poussières et 30&nbsp;L pour les liquides, filtre de classe M et double filtre auto-nettoyant. Makita publie 2 à 3,7&nbsp;m³/min et 180&nbsp;mbar. Son poids avec batteries atteint environ 18,4 à 20,8&nbsp;kg : le gain n'est donc pas la légèreté, mais la possibilité d'emmener une grosse capacité classe M là où le secteur gêne ou manque.</p>
<p>Cette comparaison suffit à casser un raccourci fréquent : « XGT » n'est pas un segment unique. Un compact AWS et un 40&nbsp;L classe M peuvent partager la plateforme batterie tout en répondant à des contraintes de chantier très différentes.</p>

<h2 id="aws-makpac">AWS et Makpac : utiles pour le workflow, indépendants de la classe</h2>
<p><strong>AWS</strong> automatise le démarrage de l'aspiration avec des outils compatibles. L'intérêt est évident avec une scie ou une ponceuse : on évite d'aller allumer l'aspirateur à chaque cycle et l'extraction suit davantage le travail de l'outil. Mais AWS n'est ni une classe de poussière ni une exclusivité du sans-fil.</p>
<p>Makita propose par exemple l'adaptateur <strong>199773-1 / WUT02</strong> pour déclencher les VC4210L et VC4210M filaires via Bluetooth AWS ; la documentation indique que jusqu'à trois appareils peuvent être associés. Le VC4210M conserve en parallèle sa prise asservie classique. Cela permet de choisir le filaire pour l'endurance tout en gardant une partie du confort d'un workflow sans fil.</p>
<p><strong>Makpac</strong> joue encore un autre rôle : rangement et transport. Le VC4210 accepte un support pour coffrets Makpac sur le dessus. C'est utile si l'aspirateur fait partie d'un poste mobile Makita ; cela n'a pratiquement aucune valeur si vous cherchez seulement une machine fixe d'atelier. L'écosystème ne doit donc être payé que lorsqu'il réduit réellement des frictions de travail.</p>

<h2 id="consommables-raccords">Sacs, filtres et raccords : le vrai coût de l'écosystème apparaît après l'achat</h2>
<p>La documentation Makita distingue plusieurs familles de consommables. Les VC001GL à VC004GL, les VC006GM/VC007GL et les aspirateurs filaires VC4210 ne partagent pas tous les mêmes sacs. Le VC4210 utilise notamment des sacs filtrants en tissu et des sacs d'élimination dédiés ; le VC2512L dispose de ses propres sacs plastiques, filtre et adaptateurs.</p>
<p>Ce point paraît secondaire jusqu'au premier remplacement. En pratique, le bon achat suppose de vérifier le diamètre du flexible, l'adaptateur vers vos outils, le type de sac compatible avec la poussière et le mode de collecte, ainsi que le coût des consommables. Pour le ponçage ou le sciage, un mauvais raccord peut annuler une partie du bénéfice d'AWS ou d'un bon débit.</p>
<p>Le <a href="/guides/prise-asservie/">guide sur la prise asservie</a> et la page <a href="/usages/aspirateur-bois-sciure-copeaux/">bois et sciure</a> permettent de poursuivre selon le workflow réel plutôt que selon la seule marque.</p>

<h2 id="preuves-independantes">Ce que les essais tiers ajoutent à la fiche Makita</h2>
<p>Un essai de KlusVisie autour d'un ensemble de ponçage XGT avec le VC004GL confirme surtout le compromis énergétique : l'absence de câble améliore la mobilité, mais les longues séquences de ponçage demandent de dimensionner sérieusement le parc de batteries. C'est cohérent avec l'écart d'autonomie publié par Makita entre faible et forte aspiration. Nous n'en déduisons pas une autonomie universelle : le niveau choisi, les batteries et l'outil raccordé changent la situation.</p>
<p>Les avis agrégés du VC4210M chez Coolblue donnent un signal complémentaire, mais de niveau inférieur : plusieurs utilisateurs apprécient les raccords et la maniabilité, tandis que certains retours montrent que l'étanchéité du système de filtre peut influencer les alertes de débit. Ces avis ne servent ni à prouver la classe M ni à quantifier les performances ; ils indiquent seulement des points à vérifier en usage.</p>
<p>Nous n'avons pas testé physiquement ces machines. Les observations d'usage sont attribuées à leurs sources et les caractéristiques restent celles publiées par Makita.</p>

<h2 id="quel-makita">Quel Makita regarder selon votre contrainte dominante ?</h2>
<div class="table-wrap"><table><thead><tr><th>Contrainte dominante</th><th>Point de départ</th><th>Pourquoi</th><th>À vérifier avant achat</th></tr></thead><tbody>
<tr><td>Atelier / rénovation en classe L, budget contenu</td><td>VC2512L</td><td>Filaire simple, eau/poussière, prise outil.</td><td>Décolmatage manuel et fréquence de poussière fine.</td></tr>
<tr><td>Classe M filaire avec poussière soutenue</td><td>VC4210M</td><td>InfiniClean, 42 L, prise asservie, AWS possible via adaptateur.</td><td>Poids, encombrement et coût des sacs/filtres.</td></tr>
<tr><td>Mobilité XGT autour d'outils AWS</td><td>VC004GL</td><td>Format plus compact et workflow sans câble.</td><td>Classe requise, autonomie à forte aspiration et parc batterie existant.</td></tr>
<tr><td>Classe M sans câble avec gros volume</td><td>VC006GM</td><td>2×40 V XGT, 40 L, filtre classe M et auto-nettoyage.</td><td>18–21 kg environ avec batteries, investissement batterie et autonomie.</td></tr>
</tbody></table></div>
<p>Si vous partez de zéro sans batteries Makita, comparez le coût du système complet — machine, batteries, chargeur, sacs, filtres et raccords — avec une solution filaire ou une autre marque. Si vous avez déjà un parc Makita, la valeur de LXT/XGT/AWS augmente, mais la classe de poussière reste le premier filtre de décision.</p>
<p>Pour élargir la comparaison, passez au <a href="/comparatifs/aspirateur-chantier-sans-fil/">comparatif sans fil</a> ou au <a href="/comparatifs/aspirateur-professionnel/">comparatif professionnel</a> selon la contrainte principale.</p>

<h2 id="sources">Sources consultées</h2>
<p>Les classes, compatibilités, autonomies annoncées, accessoires et caractéristiques proviennent en priorité des documents Makita France consultés le {UPDATED_DISPLAY}. Les sources tierces sont utilisées uniquement pour des observations d'usage explicitement attribuées.</p>
<ul>{sources_html()}</ul>
<p><small>Mise à jour : {UPDATED_DISPLAY}. Analyse documentaire, sans test physique. Les liens affiliés éventuels n'influencent ni les classes, ni les caractéristiques retenues, ni l'orientation éditoriale.</small></p>
<!-- BRAND_CONTENT_END -->'''


def toc_html():
    items = [
        ("matrice-makita", "Comment lire Makita"),
        ("classe-avant-reference", "Classe avant plateforme"),
        ("lxt-xgt", "Filaire, LXT ou XGT"),
        ("xgt-deux-logiques", "Deux logiques XGT"),
        ("aws-makpac", "AWS et Makpac"),
        ("consommables-raccords", "Sacs et raccords"),
        ("preuves-independantes", "Preuves indépendantes"),
        ("quel-makita", "Quel Makita ?"),
        ("sources", "Sources"),
    ]
    return "".join(f'<a href="#{escape(anchor)}">{escape(label)}</a>' for anchor, label in items)


def replace_once(pattern, repl, text, label, flags=0):
    out, count = re.subn(pattern, repl, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f'{label}: expected one replacement, got {count}')
    return out


def patch_page():
    path = BASE / "marques" / "makita" / "index.html"
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
        "slug": "makita",
        "brand": "Makita",
        "page_type": "BRAND_HUB",
        "updated_at": UPDATED_ISO,
        "source_of_truth": "_generate_makita.py",
        "structure_strategy": "bespoke_class_power_workflow_matrix",
        "recovery_verdict": "DEEP_REWRITE",
        "entity_map": {
            "brand": "Makita",
            "families": ["VC filaire", "LXT", "XGT", "XGT 2x40 V"],
            "products": ["VC2512L", "VC4210L", "VC4210M", "VC004GL", "VC006GM"],
            "technologies": ["AWS", "Makpac", "InfiniClean", "HEPA", "XGT", "LXT"],
            "use_cases": ["atelier", "rénovation", "ponçage", "sciage", "poussières fines", "mobilité chantier"],
            "competitors": ["Kärcher", "Bosch", "Festool", "DeWalt", "Nilfisk", "Mirka", "Parkside"],
        },
        "brand_positioning": {
            "summary": "Makita est surtout pertinent quand classe de poussière, source d'énergie et parc d'outillage sont lus séparément. La valeur de la page est de transformer une nomenclature dense en matrice de décision.",
            "core_decisions": [
                "quelle classe de poussière avant toute plateforme ?",
                "filaire, LXT ou XGT selon mobilité et autonomie ?",
                "AWS apporte-t-il une vraie valeur dans le workflow ?",
                "quel coût total en batteries, sacs, filtres et raccords ?",
            ],
        },
        "evidence": [
            {"ref": ref, "status": "VERIFIED" if kind == "primary" else "SUPPORTED", "tier": 1 if kind == "primary" else 3, "source": url, "source_type": kind, "label": label}
            for ref, label, url, kind in SOURCES
        ],
        "key_claims": [
            {"claim": "VC2512L est une référence filaire classe L avec décolmatage manuel.", "evidence_refs": ["S3"], "status": "VERIFIED"},
            {"claim": "VC4210M est classe M, 42 L brut, avec InfiniClean et support Makpac.", "evidence_refs": ["S1", "S2", "S5"], "status": "VERIFIED"},
            {"claim": "VC4210L/M peuvent être déclenchés via AWS grâce à l'adaptateur 199773-1/WUT02.", "evidence_refs": ["S1", "S2"], "status": "VERIFIED"},
            {"claim": "VC004GL est un aspirateur XGT AWS de 15 L dont l'autonomie annoncée varie fortement avec le réglage d'aspiration.", "evidence_refs": ["S2"], "status": "VERIFIED"},
            {"claim": "VC006GM combine XGT 2x40 V, 40 L de poussières, filtre classe M et double filtre auto-nettoyant.", "evidence_refs": ["S2"], "status": "VERIFIED"},
            {"claim": "Un essai tiers du VC004GL confirme que le travail de ponçage soutenu exige de dimensionner le parc batterie.", "evidence_refs": ["S6"], "status": "SUPPORTED"},
        ],
        "internal_links": [
            {"label": "Makita VC2512L", "url": "/modeles/makita-vc2512l/"},
            {"label": "Makita VC4210MX", "url": "/modeles/makita-vc4210mx/"},
            {"label": "sans fil", "url": "/comparatifs/aspirateur-chantier-sans-fil/"},
            {"label": "classe M", "url": "/comparatifs/aspirateur-classe-m/"},
            {"label": "professionnel", "url": "/comparatifs/aspirateur-professionnel/"},
            {"label": "classes L/M/H", "url": "/guides/classes-l-m-h/"},
            {"label": "prise asservie", "url": "/guides/prise-asservie/"},
            {"label": "bois et sciure", "url": "/usages/aspirateur-bois-sciure-copeaux/"},
        ],
        "editorial": {
            "desk_research_only": True,
            "affiliate_influence": False,
            "human_validation_required": True,
            "publish_review": "PENDING",
            "workflow_contract_version": 2,
            "run_evidence": ".content/brands/runs/makita.json",
        },
        "cluster_audit": {
            "date": "2026-09-10",
            "verdict": "DEEP_REWRITE",
            "reason": "Makita's nomenclature, dust classes and battery ecosystems were compressed into a shallow linear structure; the page needed an evidence-led decision matrix.",
        },
        "sources": source_map,
    }


def write_ledger():
    path = BASE / ".content" / "brands" / "makita.yaml"
    path.write_text(json.dumps(data_record(), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    patch_page()
    write_ledger()
    print('✓ makita evidence-led brand hub')


if __name__ == '__main__':
    main()
