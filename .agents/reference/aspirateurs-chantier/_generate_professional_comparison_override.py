#!/usr/bin/env python3
"""Bespoke pilot for /comparatifs/aspirateur-professionnel/.

The professional comparison is intentionally scenario-led. It must not collapse
into a class-M ranking, because the correct dust class is a contextual gate and
professional work also differs by mobility, filter cleaning, tool integration
and capacity.

This override owns both the rendered HTML and the method-neutral evidence ledger
for this one pilot URL so generation cannot recreate the legacy scoring drift.
"""
from pathlib import Path
from html import escape
import json
import re

BASE = Path(__file__).resolve().parent
MODELS_PATH = BASE / '.content/models/model-evidence.json'
LEDGER_PATH = BASE / '.content/comparisons/aspirateur-professionnel.json'
HTML_PATH = BASE / 'comparatifs/aspirateur-professionnel/index.html'
MODELS = json.loads(MODELS_PATH.read_text(encoding='utf-8'))['models']
UPDATED = '09/09/2026'
UPDATED_ISO = '2026-09-09'

CANDIDATES = [
    {
        'profile': 'Interventions sans prise',
        'slug': 'bosch-gas-18v-10-l',
        'decision': 'À privilégier si la mobilité 18 V est prioritaire et si la classe L convient au risque.',
        'tradeoff': 'La cuve nette de 6 L et l’autonomie annoncée imposent des interventions plus courtes qu’avec un filaire.'
    },
    {
        'profile': 'Classe L simple avec outil filaire',
        'slug': 'makita-vc2512l',
        'decision': 'Un choix simple pour l’atelier ou le chantier en classe L avec marche/arrêt automatique de l’outil.',
        'tradeoff': 'Le nettoyage Push & Clean est manuel : sur poussière fine, il interrompt davantage le travail qu’un système automatique.'
    },
    {
        'profile': 'Classe L compacte / parc Festool',
        'slug': 'festool-ctl-midi',
        'decision': 'Pertinent pour les interventions de montage et les utilisateurs Festool qui valorisent le format compact, le Bluetooth et le système CLEANTEC.',
        'tradeoff': 'La référence CTL MIDI I reste classe L et n’intègre pas AUTOCLEAN : il ne faut pas la confondre avec un CTM MIDI I AC.'
    },
    {
        'profile': 'Classe M polyvalente autour de 35 L',
        'slug': 'bosch-gas-35-m-afc',
        'decision': 'Le repère le plus équilibré ici si vous avez besoin d’une classe M, d’un AFC automatique et d’un volume de cuve intermédiaire.',
        'tradeoff': 'Les 74 L/s et 254 mbar publiés par Bosch sont des maxima à la turbine : ils ne servent pas de classement direct face aux autres marques.'
    },
    {
        'profile': 'Classe M avec Tact, antistatique et ACD',
        'slug': 'karcher-nt-30-1-tact',
        'decision': 'À regarder en priorité si Tact commandé par capteur, système antistatique complet et certification ACD sont réellement décisionnels pour votre travail.',
        'tradeoff': 'Avec 14,2 kg annoncés sans accessoires, il est moins agréable à déplacer qu’un compact ; ACD ne signifie pas adapté à toute atmosphère explosive.'
    },
    {
        'profile': 'Classe M gros volume',
        'slug': 'makita-vc4210mx',
        'decision': 'Le choix logique quand 42 L et InfiniClean comptent davantage que la compacité.',
        'tradeoff': 'Ses 16 kg sans câble le rendent moins pertinent pour des déplacements fréquents ou de petites interventions.'
    },
]


def local_url(slug):
    return f'/modeles/{slug}/'


def key_facts(d):
    specs = d.get('specs', {})
    preferred = [
        'Classe', 'Classe de poussière', 'Cuve', 'Réservoir / sac filtre',
        'Décolmatage', 'Nettoyage du filtre', 'Prise outil', 'Prise outil asservie',
        'Auto-Start outil', 'Bluetooth', 'Antistatique', 'Batterie',
        'Poids', 'Poids sans câble', 'Poids sans batterie'
    ]
    facts = []
    for key in preferred:
        if key in specs:
            fact = f'{key} : {specs[key]}'
            if fact not in facts:
                facts.append(fact)
    return facts[:5]


# Persist a method-neutral comparison ledger aligned with the rendered page.
product_universe = []
evidence = []
recommendations = []
for item in CANDIDATES:
    d = MODELS[item['slug']]
    product_universe.append({
        'id': item['slug'],
        'name': d['name'],
        'brand': d['brand'],
        'status': 'ELIGIBLE',
        'role': item['profile'],
        'source': d['source'],
    })
    evidence.append({
        'product': item['slug'],
        'criterion': 'product_identity_and_role',
        'claim': '; '.join(key_facts(d)),
        'source': d['source'],
        'source_date': UPDATED_ISO,
        'evidence_class': 'VERIFIED',
    })
    recommendations.append({
        'scenario': item['profile'],
        'product_id': item['slug'],
        'why': item['decision'],
        'main_tradeoff': item['tradeoff'],
    })

ledger = {
    'slug': 'aspirateur-professionnel',
    'url': '/comparatifs/aspirateur-professionnel/',
    'updated_at': UPDATED_ISO,
    'status': 'PILOT_REWRITE',
    'intent': {
        'query': 'aspirateur chantier professionnel',
        'type': 'best_for_use_case',
        'user_job': 'choisir un aspirateur professionnel adapté au risque poussière et au workflow réel sans confondre niveau de gamme, classe de sécurité et puissance',
        'primary_constraint': 'déterminer la classe nécessaire avant d’arbitrer mobilité, décolmatage, raccordement à l’outil et capacité',
        'boundary': 'la requête aspirateur classe M reste portée par /comparatifs/aspirateur-classe-m/'
    },
    'scope': {
        'selection_rule': 'références actuelles représentatives de situations professionnelles distinctes ; pas de census exhaustif ni de ranking universel',
        'candidates': product_universe,
        'major_exclusions': [],
    },
    'product_universe': product_universe,
    'criteria': [
        {'id': 'dust_requirement', 'label': 'Classe de poussière requise et fonctions de sécurité réellement nécessaires'},
        {'id': 'filter_endurance', 'label': 'Mode de nettoyage du filtre et continuité de travail'},
        {'id': 'tool_workflow', 'label': 'Prise asservie, Bluetooth, raccords et antistatique selon le workflow'},
        {'id': 'mobility', 'label': 'Batterie, poids, encombrement et fréquence des déplacements'},
        {'id': 'capacity', 'label': 'Capacité utile, fréquence de vidage et consommables'},
    ],
    'evidence': evidence,
    'recommendation_logic': recommendations,
    'measurement_notes': [
        'Les valeurs de débit et de dépression sont conservées dans les ledgers modèles mais ne sont pas utilisées pour classer directement les marques lorsque le point ou le protocole de mesure n’est pas démontré équivalent.',
        'Bosch publie notamment plusieurs maxima à la turbine ; ces chiffres ne sont pas assimilés automatiquement aux valeurs publiées sans précision équivalente par d’autres fabricants.',
        'Classe appareil, filtre HEPA, décolmatage et puissance restent des dimensions distinctes.'
    ],
    'notes': {
        'scoring_used': False,
        'affiliate_commission_used_in_ranking': False,
        'desk_research_only': True,
        'noindex_during_pilot': False,
        'hands_on_test': False,
    }
}
LEDGER_PATH.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

rows = []
for item in CANDIDATES:
    d = MODELS[item['slug']]
    rows.append(
        '<tr>'
        f'<td><strong>{escape(item["profile"])}</strong></td>'
        f'<td><a href="{local_url(item["slug"])}">{escape(d["name"])}</a></td>'
        f'<td>{escape(d["dust_class"])}</td>'
        f'<td>{escape(item["decision"])}</td>'
        '</tr>'
    )

blocks = []
for item in CANDIDATES:
    d = MODELS[item['slug']]
    facts = ' · '.join(key_facts(d))
    blocks.append(
        f'<h3>{escape(d["name"])}</h3>'
        f'<p><strong>{escape(item["profile"])}.</strong> {escape(item["decision"])} {escape(facts)}.</p>'
        f'<p><strong>Limite à garder en tête :</strong> {escape(item["tradeoff"])} '
        f'<a href="{local_url(item["slug"])}">Voir la fiche modèle</a>.</p>'
    )

source_items = []
for item in CANDIDATES:
    d = MODELS[item['slug']]
    source_items.append(
        f'<li><a href="{escape(d["source"])}" rel="nofollow noopener" target="_blank">'
        f'{escape(d["brand"])} — {escape(d["name"])}</a></li>'
    )

body = f'''<main>
<div class="container"><nav class="breadcrumb"><a href="/">Accueil</a><span class="sep">/</span> <a href="/comparatifs/">Comparatifs</a> <span class="sep">/</span> <span>Aspirateur professionnel</span></nav></div>
<section class="page-hero"><div class="container"><span class="ctype ctype-comp">Comp</span><h1 style="margin-top:10px;">Aspirateur de chantier professionnel : lequel choisir selon votre travail ?</h1><p class="lead">Classe L ou M, mobilité, décolmatage, prise outil et volume : ici, le meilleur choix change avec le chantier.</p><div class="page-meta"><span class="meta-tag">Vérifié : {UPDATED}</span><span class="meta-tag">Recherche documentaire</span><span class="meta-tag">Sans classement sponsorisé</span></div></div></section>
<div class="container"><div class="content-layout"><article class="content-main">
<div class="answer-box"><p><strong>Commencez par la poussière, pas par la puissance.</strong> Si votre travail impose une classe M, comparez ensuite le décolmatage, l’intégration à l’outil, la capacité et la mobilité. Si la classe L est suffisante, un modèle plus léger ou sans fil peut être un meilleur outil de travail quotidien qu’un gros M. Il n’y a donc pas de gagnant professionnel universel.</p></div>

<h2 id="raccourci">Le raccourci : quel profil professionnel correspond à votre chantier ?</h2>
<div class="table-wrap"><table><thead><tr><th>Situation</th><th>Référence repère</th><th>Classe</th><th>Pourquoi elle est ici</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div>
<p>Cette sélection n’est pas un classement de 1 à 6. Elle couvre six décisions différentes avec des références actuelles et documentées. Un produit peut être meilleur dans son scénario tout en étant un mauvais achat dans un autre.</p>

<h2 id="frontiere">Professionnel et classe M ne sont pas synonymes</h2>
<p>« Professionnel » décrit un contexte de travail ; <strong>L, M ou H décrivent des exigences liées aux poussières et à l’appareil</strong>. La classe M ne doit donc pas devenir un badge de gamme supérieure. Si votre besoin est spécifiquement de comparer des appareils M, la page <a href="/comparatifs/aspirateur-classe-m/">aspirateurs classe M</a> est plus précise.</p>
<p>À l’inverse, pour une intervention courte où la classe L correspond au risque, un appareil compact sur batterie peut être plus cohérent qu’un aspirateur M de 30 ou 40 litres. Le bon ordre est : <strong>risque → classe nécessaire → workflow → machine</strong>.</p>

<h2 id="arbitrages">Quatre arbitrages font vraiment basculer le choix</h2>
<h3>1. Le niveau de poussière requis est un gate, pas une note</h3>
<p>Un filtre HEPA, un débit élevé ou un moteur puissant ne permettent pas d’inférer une classe L, M ou H. Dès qu’une classe précise est nécessaire, les modèles qui ne la possèdent pas sortent simplement du périmètre.</p>
<h3>2. Le décolmatage compte surtout quand le filtre se charge vite</h3>
<p>Sur des sessions longues avec poussières fines, AFC, Tact ou InfiniClean peuvent réduire les interruptions. Sur une utilisation plus ponctuelle en classe L, un nettoyage manuel ou semi-automatique peut rester un compromis rationnel. Le décolmatage n’est pas une certification de sécurité.</p>
<h3>3. Le meilleur workflow outil n’est pas le même partout</h3>
<p>Une prise asservie est très pratique avec un outil filaire ; le Bluetooth et les systèmes de raccordement prennent davantage de sens dans certains écosystèmes. L’antistatique devient aussi une caractéristique distincte à vérifier plutôt qu’un bénéfice supposé.</p>
<h3>4. La capacité se paie en poids et en encombrement</h3>
<p>Une cuve de 42 L réduit la fréquence de vidage, mais elle n’est pas automatiquement meilleure qu’un 15 ou 25 L lorsque la machine monte des escaliers, entre dans un véhicule ou change de zone plusieurs fois par jour.</p>

<h2 id="modeles">Les six modèles repères, avec leurs vraies limites</h2>
{''.join(blocks)}

<h2 id="mesures">Pourquoi nous ne classons pas ces machines sur le débit ou la dépression</h2>
<p>Les fabricants ne documentent pas toujours le même point de mesure. Bosch précise par exemple des maxima <strong>à la turbine</strong> sur plusieurs GAS. D’autres fiches publient un débit et une dépression maximum sans préciser le même contexte. Afficher les chiffres reste utile, mais les transformer en podium cross-brand donnerait une précision que les sources ne permettent pas.</p>
<p>La conséquence pratique est simple : utilisez débit et dépression pour comprendre une machine et comparer des données réellement équivalentes, pas comme un score universel qui écrase la classe, l’état du filtre, le flexible, le raccord ou le type de poussière.</p>

<h2 id="sortie">Quand utiliser un autre comparatif</h2>
<p>Si la classe M est déjà certaine, passez au <a href="/comparatifs/aspirateur-classe-m/">comparatif classe M</a>. Si la mobilité est la question principale, consultez les <a href="/comparatifs/aspirateur-chantier-sans-fil/">aspirateurs sans fil</a>. Pour un besoin lié au matériau ou à l’outil, les pages <a href="/usages/aspirateur-platre/">plâtre</a>, <a href="/usages/aspirateur-ponceuse/">ponceuse</a> ou <a href="/usages/aspirateur-bois-sciure-copeaux/">bois et sciure</a> évitent de faire porter à cette page toutes les intentions du site.</p>
<p>Pour comprendre les critères avant de choisir un modèle, utilisez les guides sur les <a href="/guides/classes-l-m-h/">classes L, M et H</a>, le <a href="/guides/decolmatage-automatique/">décolmatage</a> et la <a href="/guides/prise-asservie/">prise asservie</a>.</p>

<h2 id="sources">Sources et méthode</h2>
<p>Ce comparatif est une <strong>recherche documentaire</strong> vérifiée le {UPDATED}. Il ne prétend pas reproduire un test physique en conditions identiques. Les rôles attribués aux modèles sont des recommandations éditoriales dérivées de caractéristiques officielles et des contraintes du scénario, pas des mesures de laboratoire réalisées par le site.</p>
<div class="related-box"><strong>Sources primaires consultées</strong><ul>{''.join(source_items)}</ul></div>
<p><small>Desk research, sans test physique. Les commissions d’affiliation n’entrent ni dans la sélection ni dans la recommandation.</small></p>
</article>
<aside class="content-sidebar"><div class="sidebar-box"><div class="sidebar-box-head">Sommaire</div><div class="sidebar-box-body"><nav class="toc-list"><a href="#raccourci">Quel profil ?</a><a href="#frontiere">Professionnel ≠ M</a><a href="#arbitrages">4 arbitrages</a><a href="#modeles">6 modèles repères</a><a href="#mesures">Débit & dépression</a><a href="#sortie">Autres comparatifs</a><a href="#sources">Sources</a></nav></div></div><div class="sidebar-box"><div class="sidebar-box-head">Affiliation</div><div class="sidebar-box-body"><p class="affil-note">Ce site contient des liens affiliés. Nos analyses restent indépendantes. <a href="/transparence-affiliation/">En savoir plus.</a></p></div></div></aside>
</div></div>
</main>'''

html = HTML_PATH.read_text(encoding='utf-8')
html = re.sub(r'<title>.*?</title>', '<title>Aspirateur de chantier professionnel : comparatif par usage 2026</title>', html, count=1, flags=re.S)
html = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Quel aspirateur de chantier professionnel choisir en 2026 ? Comparaison par classe L/M, mobilité, décolmatage, prise outil et volume.">', html, count=1)
html = re.sub(r'<main>.*?</main>', body, html, count=1, flags=re.S)
HTML_PATH.write_text('\n'.join(line.rstrip() for line in html.splitlines()) + '\n', encoding='utf-8')
print('✓ professional comparison pilot: evidence ledger + bespoke HTML')
