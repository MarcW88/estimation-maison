#!/usr/bin/env python3
"""Bespoke Bosch brand-hub generator.

Runs after _generate_brands.py so the Bosch page is not forced back into the
shared brand template. Desk research only; evidence checked 2026-09-09.
"""
from pathlib import Path
from html import escape
import json
import re

BASE = Path(__file__).resolve().parent
UPDATED_DISPLAY = "09/09/2026"
UPDATED_ISO = "2026-09-09"
TITLE = "Aspirateurs de chantier Bosch : DIY, GAS et 18 V en 2026"
DESC = "Bosch : comprendre les gammes PAS, AdvancedVac et GAS, les classes L/M, AFC, Click & Clean et les deux plateformes 18 V avant de choisir."

SOURCES = [
    ("Bosch DIY — gamme aspirateurs eau et poussière", "https://www.bosch-diy.com/fr/fr/outils-de-nettoyage/aspirateurs-eau-et-poussiere"),
    ("Bosch DIY PAS30-240PRS", "https://www.bosch-diy.com/fr/fr/p/pas30-240prs-06033e73w0"),
    ("Bosch DIY AdvancedVac 20", "https://www.bosch-diy.com/fr/fr/p/advancedvac-20-06033d12w0"),
    ("Bosch DIY AdvancedVac 18V-8", "https://www.bosch-diy.com/fr/fr/p/advancedvac-18v-8-06033e1000"),
    ("Bosch Professional GAS 18V-10 L", "https://www.bosch-professional.com/fr/fr/products/gas-18v-10-l-06019C6302/"),
    ("Bosch Professional GAS 35 M AFC", "https://www.bosch-professional.com/fr/fr/products/gas-35-m-afc-06019C31W0"),
    ("Bosch Professional GAS 55 M AFC", "https://www.bosch-professional.com/fr/fr/products/gas-55-m-afc-06019C33W0"),
    ("Bosch Professional — AMPShare", "https://www.bosch-professional.com/fr/fr/ampshare/"),
]


def sources_html():
    return "".join(
        f'<li><a href="{escape(url)}" rel="nofollow noopener">{escape(label)}</a></li>'
        for label, url in SOURCES
    )


def article():
    return f'''<!-- BRAND_CONTENT_START -->
<div class="answer-box"><p>Chez Bosch, le premier choix n'est pas entre deux références mais entre <strong>trois univers</strong> : les aspirateurs Home &amp; Garden pour le bricolage et l'eau/poussière, les GAS Professional filaires pour le chantier et les besoins de classe L ou M, puis le GAS 18V-10 L pour la mobilité professionnelle. Cette séparation compte aussi pour les batteries : POWER FOR ALL et Professional 18V / AMPShare ne sont pas compatibles.</p></div>

<h2 id="univers-bosch">Commencez par choisir l'univers Bosch, pas le modèle</h2>
<p>Le catalogue Bosch mélange des produits verts Home &amp; Garden et des produits bleus Professional qui ne répondent pas au même cahier des charges. Les AdvancedVac, UniversalVac et PAS sont avant tout des aspirateurs eau et poussière pour la maison, le garage et l'atelier. La famille GAS Professional ajoute, selon la référence, une classe de poussière documentée, le raccordement Click &amp; Clean et des fonctions pensées pour travailler avec des outils électroportatifs sur chantier.</p>
<p>Cette distinction évite un raccourci fréquent : un aspirateur DIY peut afficher un débit ou une dépression élevés sans devenir pour autant un aspirateur de sécurité de classe M. Inversement, un GAS M n'est pas automatiquement le meilleur achat pour nettoyer un garage : sa classe, son décolmatage et son équipement n'ont d'intérêt que si le travail les justifie.</p>
<p>Cette page est une analyse documentaire des gammes et fiches Bosch disponibles le {UPDATED_DISPLAY}. Nous n'avons pas réalisé de test physique de ces machines ; les performances chiffrées ci-dessous sont celles publiées par Bosch et sont indiquées avec leur contexte de mesure lorsqu'il est disponible.</p>

<h2 id="home-garden">Home &amp; Garden : PAS, AdvancedVac et UniversalVac couvrent désormais plusieurs paliers</h2>
<p>La gamme française eau et poussière ne se limite plus à l'AdvancedVac 20. Bosch liste actuellement sept références : PAS15-200, UniversalVac 15, PAS15-220, AdvancedVac 18V-8, PAS20-220P, AdvancedVac 20 et PAS30-240PRS. Pour lire cette offre sans transformer la page en catalogue, il est plus utile de la regrouper par format et usage.</p>
<div class="table-wrap"><table><thead><tr><th>Segment DIY</th><th>Références actuelles</th><th>Repère utile</th></tr></thead><tbody>
<tr><td><strong>15 L filaire</strong></td><td>PAS15-200, UniversalVac 15, PAS15-220</td><td>Formats compacts pour nettoyage et bricolage courant.</td></tr>
<tr><td><strong>20 L filaire</strong></td><td>PAS20-220P, AdvancedVac 20</td><td>L'AdvancedVac 20 annonce 70 l/s et 260 mbar à la turbine et peut démarrer avec un outil raccordé.</td></tr>
<tr><td><strong>30 L filaire</strong></td><td>PAS30-240PRS</td><td>30 L, 67 l/s et 265 mbar à la turbine, nettoyage de filtre semi-automatique et Auto-Start.</td></tr>
<tr><td><strong>18 V DIY</strong></td><td>AdvancedVac 18V-8</td><td>8 L, 29 l/s à la turbine, batterie POWER FOR ALL 18V.</td></tr>
</tbody></table></div>
<p>Pour un atelier domestique, l'<a href="/modeles/bosch-advancedvac-20/">AdvancedVac 20</a> reste un point d'entrée simple à comprendre. Le PAS30-240PRS devient plus intéressant lorsque le volume de cuve, la connexion aux outils et le nettoyage semi-automatique du filtre comptent davantage. Aucun de ces arguments ne permet toutefois de déduire une classe M : si la nature de la poussière impose une classe de sécurité, il faut passer à une référence certifiée pour ce besoin.</p>

<h2 id="gas-professional">GAS Professional : la classe et le décolmatage changent davantage le choix que la puissance</h2>
<p>Chez Bosch Professional, trois références illustrent bien les décisions à prendre. Le GAS 18V-10 L privilégie la mobilité et reste classe L. Les GAS 35 M AFC et GAS 55 M AFC sont des aspirateurs filaires classe M avec nettoyage automatique du filtre AFC. Bosch publie pour ces deux modèles M les mêmes maxima à la turbine, 74 l/s et 254 mbar : le passage du 35 au 55 se joue donc surtout sur le volume et la mobilité, pas sur un chiffre d'aspiration supérieur.</p>
<div class="table-wrap"><table><thead><tr><th>Modèle</th><th>Classe</th><th>Cuve</th><th>Débit / dépression max.</th><th>Ce qui change la décision</th></tr></thead><tbody>
<tr><td><strong>GAS 18V-10 L</strong></td><td>L</td><td>10 L brut / 6 L net</td><td>34 l/s / 115 mbar à la turbine</td><td>Sans fil, 4,7 kg sans batterie, cyclonique, Click &amp; Clean.</td></tr>
<tr><td><strong>GAS 35 M AFC</strong></td><td>M</td><td>35 L brut / 23 L net</td><td>74 l/s / 254 mbar à la turbine</td><td>AFC, Click &amp; Clean, L-BOXX, 12,4 kg.</td></tr>
<tr><td><strong>GAS 55 M AFC</strong></td><td>M</td><td>55 L brut / 43 L net</td><td>74 l/s / 254 mbar à la turbine</td><td>Même logique AFC, mais 16,2 kg et davantage de capacité.</td></tr>
</tbody></table></div>
<p>Le <a href="/modeles/bosch-gas-35-m-afc/">GAS 35 M AFC</a> est donc le point de comparaison le plus équilibré lorsque la classe M est adaptée au risque et que la machine doit encore être déplacée régulièrement. Le GAS 55 M AFC gagne surtout en capacité. Le <a href="/modeles/bosch-gas-18v-10-l/">GAS 18V-10 L</a>, lui, répond à une autre question : travailler sans câble avec une classe L documentée. Un filtre HEPA présent sur ce dernier ne transforme pas sa classe L en classe M.</p>

<h2 id="deux-systemes-18v">18 V Bosch : POWER FOR ALL et Professional 18V / AMPShare sont deux plateformes différentes</h2>
<p>Le nom Bosch 18 V peut prêter à confusion. L'AdvancedVac 18V-8 appartient à l'alliance <strong>POWER FOR ALL</strong>, destinée à l'univers Home &amp; Garden. Le GAS 18V-10 L appartient au <strong>Professional 18V System</strong> et est compatible AMPShare. Bosch précise explicitement que les batteries AMPShare et POWER FOR ALL ne sont pas compatibles entre elles.</p>
<p>Cette séparation a une conséquence directe sur le coût réel d'un aspirateur sans fil. Si vous possédez déjà des batteries Bosch Professional 18 V, le GAS 18V-10 L s'intègre à ce parc et aux batteries AMPShare compatibles. Si votre équipement est surtout Home &amp; Garden / POWER FOR ALL, l'AdvancedVac 18V-8 évite de créer un second parc de batteries. Le voltage identique ne suffit donc pas à établir une compatibilité.</p>

<h2 id="quel-bosch">Quel aspirateur Bosch regarder selon le travail réel ?</h2>
<p>Une fois l'univers identifié, le choix devient beaucoup plus court. Le tableau ci-dessous n'est pas un classement : il indique le point d'entrée Bosch à examiner selon le besoin, avec la limite qui doit rester visible.</p>
<div class="table-wrap"><table><thead><tr><th>Besoin</th><th>Point d'entrée Bosch</th><th>Pourquoi</th><th>Vigilance</th></tr></thead><tbody>
<tr><td>Garage, atelier, eau et poussière</td><td>AdvancedVac 20 / PAS30-240PRS</td><td>Formats filaires DIY avec connexion aux outils ; 20 ou 30 L selon le besoin.</td><td>Ne pas les substituer à une classe de sécurité requise.</td></tr>
<tr><td>Nettoyage mobile DIY</td><td>AdvancedVac 18V-8</td><td>8 L et plateforme POWER FOR ALL.</td><td>Autonomie et puissance d'aspiration inférieures aux grands filaires.</td></tr>
<tr><td>Intervention mobile professionnelle</td><td>GAS 18V-10 L</td><td>Professional 18V / AMPShare, classe L, format compact.</td><td>La classe L doit correspondre au risque réel.</td></tr>
<tr><td>Poussières pour lesquelles une classe M est appropriée</td><td>GAS 35 M AFC</td><td>Classe M, AFC, 35 L et intégration Click &amp; Clean / L-BOXX.</td><td>Plus lourd et plus coûteux qu'un aspirateur DIY.</td></tr>
<tr><td>Classe M avec gros volume</td><td>GAS 55 M AFC</td><td>43 L nets avec la même logique AFC.</td><td>16,2 kg : le volume se paie en mobilité.</td></tr>
</tbody></table></div>
<p>Pour une poussière fine liée au ponçage, la classe ne suffit pas à elle seule : le raccord à l'outil et le maintien du débit comptent aussi. Nos pages sur l'<a href="/usages/aspirateur-ponceuse/">aspiration avec une ponceuse</a>, le <a href="/guides/decolmatage-automatique/">décolmatage automatique</a> et la <a href="/guides/prise-asservie/">prise asservie</a> permettent de vérifier ces critères séparément.</p>

<h2 id="limites-bosch">Ce que le logo Bosch ne règle pas à votre place</h2>
<p>Trois vérifications restent nécessaires quelle que soit la référence. D'abord, la classe de poussière doit correspondre au matériau et aux prescriptions applicables : ni la puissance moteur, ni le filtre HEPA, ni un débit élevé ne permettent de déduire une classe M ou H. Ensuite, les chiffres de débit et de dépression doivent être comparés avec prudence lorsqu'ils ne sont pas mesurés au même point ou selon le même protocole. Enfin, une compatibilité d'écosystème se vérifie au niveau de la batterie, du flexible, des raccords et des consommables, pas simplement au logo sur la machine.</p>
<p>Si votre priorité est déjà structurée autour d'un autre système de batteries, de coffrets ou de raccords d'outils, l'avantage d'intégration Bosch diminue. C'est souvent plus décisif que quelques litres de cuve ou quelques mbar supplémentaires. Pour clarifier la partie sécurité, consultez le <a href="/guides/classes-l-m-h/">guide des classes L, M et H</a> ; pour les chiffres d'aspiration, notre guide sur le <a href="/guides/debit-air-aspirateur/">débit d'air</a> remet les valeurs fabricants dans leur contexte.</p>

<h2 id="suite">Les pages Bosch et comparatifs à consulter ensuite</h2>
<p>Si vous avez identifié votre univers, poursuivez directement vers la fiche correspondante : <a href="/modeles/bosch-advancedvac-20/">Bosch AdvancedVac 20</a>, <a href="/modeles/bosch-gas-18v-10-l/">Bosch GAS 18V-10 L</a> ou <a href="/modeles/bosch-gas-35-m-afc/">Bosch GAS 35 M AFC</a>. Pour comparer Bosch au reste du marché, utilisez le <a href="/comparatifs/aspirateur-chantier-sans-fil/">comparatif sans fil</a>, le <a href="/comparatifs/aspirateur-classe-m/">comparatif classe M</a> ou le <a href="/comparatifs/aspirateur-professionnel/">comparatif professionnel</a> selon le besoin déjà défini.</p>

<h2 id="sources">Sources consultées</h2>
<p>Les statuts de gamme, classes, capacités, compatibilités et performances indiqués ici proviennent des pages officielles Bosch consultées le {UPDATED_DISPLAY}. Les valeurs de débit et de dépression sont reprises comme données fabricant et ne sont pas des mesures réalisées par notre rédaction.</p>
<ul>{sources_html()}</ul>
<p><small>Mise à jour : {UPDATED_DISPLAY}. Analyse documentaire, sans test physique. Les liens affiliés éventuels n'influencent ni les classes, ni les caractéristiques retenues, ni l'orientation éditoriale.</small></p>
<!-- BRAND_CONTENT_END -->'''


def data_record():
    return {
        "slug": "bosch",
        "brand": "Bosch",
        "page_type": "BRAND_HUB",
        "updated_at": UPDATED_ISO,
        "source_of_truth": "_generate_bosch.py",
        "structure_strategy": "bespoke_decision_tree_diy_vs_professional_vs_18v",
        "entity_map": {
            "brand": "Bosch",
            "products": [
                "PAS15-200", "UniversalVac 15", "PAS15-220", "AdvancedVac 18V-8",
                "PAS20-220P", "AdvancedVac 20", "PAS30-240PRS", "GAS 18V-10 L",
                "GAS 35 M AFC", "GAS 55 M AFC"
            ],
            "use_cases": ["atelier", "eau et poussière", "ponceuse", "chantier mobile", "poussière classe M"],
            "technologies": ["POWER FOR ALL 18V", "Professional 18V System", "AMPShare", "AFC", "Click & Clean", "L-BOXX"],
            "competitors": ["Kärcher", "Makita", "Festool", "DeWalt", "Nilfisk", "Mirka", "Parkside"]
        },
        "brand_positioning": {
            "summary": "Bosch se lit d'abord comme plusieurs univers distincts : Home & Garden eau/poussière, GAS Professional filaire et Professional 18V mobile.",
            "strengths": [
                "Large couverture du bricolage au chantier professionnel.",
                "GAS 35 M AFC et GAS 55 M AFC documentés en classe M avec AFC.",
                "Professional 18V / AMPShare cohérent pour un parc d'outillage professionnel Bosch."
            ],
            "limitations": [
                "POWER FOR ALL et Professional 18V / AMPShare ne sont pas compatibles.",
                "Les modèles DIY ne remplacent pas un aspirateur de sécurité lorsque la classe M ou H est requise.",
                "Les GAS 35 M et 55 M partagent les mêmes maxima à la turbine ; le 55 apporte surtout du volume au prix d'un poids supérieur."
            ]
        },
        "product_range": [
            {"name":"PAS15-200","status":"CURRENT","role":"DIY 15 L filaire","evidence":"Liste officielle Bosch DIY France 2026."},
            {"name":"UniversalVac 15","status":"CURRENT","role":"DIY 15 L filaire","evidence":"Liste officielle Bosch DIY France 2026."},
            {"name":"PAS15-220","status":"CURRENT","role":"DIY 15 L filaire","evidence":"Liste officielle Bosch DIY France 2026."},
            {"name":"AdvancedVac 18V-8","status":"CURRENT","role":"DIY 18 V mobile","evidence":"8 L, 29 l/s à la turbine, POWER FOR ALL 18V."},
            {"name":"PAS20-220P","status":"CURRENT","role":"DIY 20 L filaire","evidence":"Liste officielle Bosch DIY France 2026."},
            {"name":"AdvancedVac 20","status":"CURRENT","role":"DIY 20 L avec outil","evidence":"20 L, 70 l/s et 260 mbar à la turbine, démarrage avec outil."},
            {"name":"PAS30-240PRS","status":"CURRENT","role":"DIY 30 L atelier","evidence":"30 L, 67 l/s et 265 mbar à la turbine, nettoyage semi-automatique, Auto-Start."},
            {"name":"GAS 18V-10 L","status":"CURRENT","role":"Professional mobile classe L","evidence":"10 L brut, 34 l/s, 115 mbar, 4,7 kg sans batterie, Professional 18V / AMPShare."},
            {"name":"GAS 35 M AFC","status":"CURRENT","role":"Professional classe M mobile","evidence":"35 L brut, 23 L net, 74 l/s, 254 mbar, AFC, Click & Clean, L-BOXX."},
            {"name":"GAS 55 M AFC","status":"CURRENT","role":"Professional classe M gros volume","evidence":"55 L brut, 43 L net, 74 l/s, 254 mbar, AFC, Click & Clean, L-BOXX."}
        ],
        "ecosystem": {
            "summary": [
                "Home & Garden utilise POWER FOR ALL pour l'AdvancedVac 18V-8.",
                "GAS 18V-10 L utilise Professional 18V System et AMPShare.",
                "Bosch confirme que POWER FOR ALL et AMPShare ne sont pas compatibles."
            ],
            "decision_rule": "Choisir d'abord l'univers et la classe nécessaire, puis le volume et la mobilité."
        },
        "evidence": [
            {"claim": label, "status": "VERIFIED", "source": url, "source_type": "primary"}
            for label, url in SOURCES
        ],
        "internal_links": [
            {"label":"Bosch AdvancedVac 20","url":"/modeles/bosch-advancedvac-20/"},
            {"label":"Bosch GAS 18V-10 L","url":"/modeles/bosch-gas-18v-10-l/"},
            {"label":"Bosch GAS 35 M AFC","url":"/modeles/bosch-gas-35-m-afc/"},
            {"label":"aspirateur sans fil","url":"/comparatifs/aspirateur-chantier-sans-fil/"},
            {"label":"aspirateur classe M","url":"/comparatifs/aspirateur-classe-m/"},
            {"label":"aspirateur professionnel","url":"/comparatifs/aspirateur-professionnel/"},
            {"label":"classes L/M/H","url":"/guides/classes-l-m-h/"},
            {"label":"décolmatage automatique","url":"/guides/decolmatage-automatique/"},
            {"label":"prise asservie","url":"/guides/prise-asservie/"},
            {"label":"débit d'air","url":"/guides/debit-air-aspirateur/"},
            {"label":"ponceuse","url":"/usages/aspirateur-ponceuse/"}
        ],
        "editorial": {
            "desk_research_only": True,
            "affiliate_influence": False,
            "human_validation_required": True,
            "publish_review": "PENDING"
        }
    }


def replace_article(html):
    start = '<!-- BRAND_CONTENT_START -->'
    end = '<!-- BRAND_CONTENT_END -->'
    if start not in html or end not in html:
        raise RuntimeError('Bosch brand content markers not found')
    return re.sub(re.escape(start) + r'.*?' + re.escape(end), article(), html, count=1, flags=re.S)


def update_shell(html):
    html = re.sub(r'<title>.*?</title>', f'<title>{escape(TITLE)}</title>', html, count=1, flags=re.S)
    html = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{escape(DESC, quote=True)}">', html, count=1)
    html = re.sub(r'<h1 style="margin-top:10px;">.*?</h1>', f'<h1 style="margin-top:10px;">{escape(TITLE)}</h1>', html, count=1, flags=re.S)
    html = re.sub(r'<p class="lead">.*?</p>', f'<p class="lead">{escape(DESC)}</p>', html, count=1, flags=re.S)
    html = re.sub(r'Verifié\s*:\s*\d{2}/\d{2}/\d{4}', f'Verifié : {UPDATED_DISPLAY}', html, count=1)
    toc = ''.join([
        '<a href="#univers-bosch">Choisir l’univers</a>',
        '<a href="#home-garden">Home &amp; Garden</a>',
        '<a href="#gas-professional">GAS Professional</a>',
        '<a href="#deux-systemes-18v">Deux systèmes 18 V</a>',
        '<a href="#quel-bosch">Quel Bosch ?</a>',
        '<a href="#limites-bosch">Points de vigilance</a>',
        '<a href="#suite">À consulter ensuite</a>',
        '<a href="#sources">Sources</a>',
    ])
    html = re.sub(r'(<nav class="toc-list">).*?(</nav>)', r'\1' + toc + r'\2', html, count=1, flags=re.S)
    return html


def main():
    page = BASE / 'marques' / 'bosch' / 'index.html'
    html = page.read_text(encoding='utf-8')
    html = replace_article(html)
    html = update_shell(html)
    page.write_text('\n'.join(line.rstrip() for line in html.splitlines()) + '\n', encoding='utf-8')

    data_path = BASE / '.content' / 'brands' / 'bosch.yaml'
    data_path.write_text(json.dumps(data_record(), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('✓ bosch bespoke brand hub')


if __name__ == '__main__':
    main()
