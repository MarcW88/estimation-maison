#!/usr/bin/env python3
"""Bespoke brand-hub overrides for all non-Bosch brands.

Run after `_generate_brands.py` (and alongside `_generate_bosch.py`). The goal is
not to create seven new templates, but to preserve the shared site shell while
letting each brand page follow its own decision logic.

Desk research only. Evidence checked 2026-09-09.
"""
from pathlib import Path
from html import escape
import json
import re

BASE = Path(__file__).resolve().parent
UPDATED_DISPLAY = "09/09/2026"
UPDATED_ISO = "2026-09-09"

SOURCES = {
    "karcher": [
        ("Kärcher WD 7 Control", "https://www.kaercher.com/fr/home-garden/aspirateurs-eau-et-poussieres/wd-7-control-p-s-30-6-35-t-eu-iii-16283860.html"),
        ("Kärcher NT 30/1 Tact Te M ACD", "https://www.kaercher.com/fr/professional/aspirateurs-eau-et-poussieres/aspirateurs-de-securite/nt-30-1-tact-te-m-acd-11482350.html"),
        ("Kärcher NT 50/1 Tact Te M ACD", "https://www.kaercher.com/fr/professional/aspirateurs-eau-et-poussieres/aspirateurs-de-securite/nt-50-1-tact-te-m-acd-11484350.html"),
        ("Kärcher — aspirateurs de sécurité", "https://www.kaercher.com/fr/professional/aspirateurs-eau-et-poussieres/aspirateurs-de-securite.html"),
    ],
    "festool": [
        ("Festool CTM MIDI I AC", "https://www.festool.fr/produits/aspirateurs/aspirateurs-compact/578552---ctm-midi-i-ac"),
        ("Festool CTH MIDI I AC", "https://www.festool.fr/produits/aspirateurs/aspirateurs-pour-amiante/578558---cth-midi-i-ac"),
        ("Festool — gamme aspirateurs", "https://www.festool.fr/produits/aspirateurs"),
    ],
    "makita": [
        ("Makita VC2512L — fiche produit", "https://www.makita.fr/data/sr/productinfo/generated/vc2512l_fiche_produit.pdf"),
        ("Makita — brochure gamme aspiration", "https://www.makita.fr/data/pam/public/Content-Pages/Media/CatalogsAndBrochures/2023_leaflet_aspi_web.pdf"),
        ("Makita — références sous garantie", "https://www.makita.fr/data/pam/public/Content-Pages/Media/CatalogsAndBrochures/GARANTY/21032025_-_refs_sous_garantie_%28web%29.pdf"),
    ],
    "dewalt": [
        ("DeWalt DCV586MN — classe M FLEXVOLT", "https://www.dewalt.fr/fr-fr/produit/dcv586mn-xj/aspirateur-tstak-xr-flexvolt-54v-brushless-eau-et-poussieres-classe-m"),
        ("DeWalt DCV584L — hybride classe L", "https://www.dewalt.fr/fr-fr/produit/dcv584l-qw/aspirateur-sur-secteur-ou-batterie-xr-et-xr-flexvolt-1854v-classe-l-sans"),
        ("DeWalt Perform & Protect", "https://prod.dewalt.fr/fr-fr/solutions-chantier/perform-protect"),
    ],
    "parkside": [
        ("Lidl / Parkside PWD 30 C1", "https://www.lidl.fr/p/parkside-aspirateur-eau-et-poussiere-pwd-30-c1/p100407117"),
        ("Lidl / Parkside PWD 20 C3", "https://www.lidl.fr/p/parkside-aspirateur-eau-et-poussiere-pwd-20-c3-19-8-l-1300-w/p100397254"),
        ("Lidl / Parkside PWD 25 C4", "https://www.lidl.fr/p/parkside-aspirateur-eau-et-poussiere-pwd-25-c4-25-l-1400-w/p100395330"),
        ("Lidl / Parkside PWD 12 B1", "https://www.lidl.fr/p/parkside-aspirateur-eau-et-poussiere-pwd-12-b1/p100406420"),
    ],
    "nilfisk": [
        ("Nilfisk Multi II 30 T", "https://shop.nilfisk.com/fr-fr/products/multi-ii-30-t-aspirateur-eau-et-poussiere"),
        ("Nilfisk ATTIX 44-2M IC", "https://www.nilfisk.com/fr-fr/professionnel/produits/aspirateurs-industriels/poussiere-dangereuse/monophase/attix-44-2m-ic%2B107412182/"),
        ("Nilfisk — aspirateurs professionnels", "https://www.nilfisk.com/fr-fr/professionnel/produits/aspirateurs-industriels/"),
    ],
    "mirka": [
        ("Mirka DEXOS 1217 M AFC", "https://www.mirka.com/fr-fr/produits/top-brands/extracteur-de-poussiere-mirka-dexos/"),
        ("Mirka DEXOS 1230 M AFC", "https://www.mirka.com/fr-fr/p/Mirka-DEXOS-1230-M-AFC-M/"),
        ("Mirka — lancement DEXOS 1230 M AFC", "https://www.mirka.com/fr-fr/entreprise/actualites/mirka-dexos-1230-m-afc--concu-pour-lextraction-efficace-de-la-poussiere/"),
    ],
}


def sources_html(slug):
    return "".join(
        f'<li><a href="{escape(url)}" rel="nofollow noopener">{escape(label)}</a></li>'
        for label, url in SOURCES[slug]
    )


BRANDS = {
"karcher": {
    "brand": "Kärcher",
    "verdict": "MAJOR",
    "strategy": "bespoke_wd_vs_nt_safety_ladder",
    "title": "Aspirateurs de chantier Kärcher : WD, NT, Tact et classes M/H",
    "desc": "Kärcher : comprendre la différence entre WD et NT, Tact, ACD et classes M/H pour choisir selon le chantier plutôt que selon la puissance.",
    "toc": [("wd-vs-nt", "WD ou NT ?"), ("gamme-wd", "Gamme WD"), ("gamme-nt", "Gamme NT"), ("tact-acd", "Tact et ACD"), ("quel-karcher", "Quel Kärcher ?"), ("points-vigilance", "Points de vigilance"), ("sources", "Sources")],
    "body": '''
<div class="answer-box"><p>Chez Kärcher, la bonne décision commence par une séparation simple : <strong>WD</strong> pour l’eau, les saletés, le garage et la rénovation courante ; <strong>NT Professional</strong> lorsque la gestion de poussières fines, la classe de sécurité, le décolmatage et le travail avec des outils deviennent structurants. Comparer un WD 7 et un NT M uniquement sur le débit ou la dépression ferait donc perdre l’essentiel.</p></div>
<h2 id="wd-vs-nt">WD ou NT : deux familles qui ne répondent pas au même cahier des charges</h2>
<p>Les WD Home &amp; Garden sont des aspirateurs eau et poussière polyvalents. Leur intérêt tient à la robustesse, au volume de cuve et, selon le modèle, à la prise outil, au nettoyage de filtre ou à des fonctions de confort. Les NT Professional ajoutent des éléments beaucoup plus liés au chantier : classe de poussière documentée, surveillance du débit, accessoires conducteurs, antistatique et systèmes de décolmatage conçus pour maintenir les performances avec des poussières fines.</p>
<p>La conséquence est importante : un WD peut aspirer très fort sans devenir un aspirateur de sécurité. Si la poussière impose une classe M ou H, le choix se fait dans la gamme appropriée et selon l’évaluation du risque, pas en cherchant le plus gros chiffre de puissance.</p>
<h2 id="gamme-wd">La gamme WD : du nettoyage polyvalent à l’atelier mieux équipé</h2>
<p>Les WD 3 à WD 6 couvrent l’essentiel des besoins domestiques et de rénovation légère. Plus on monte en gamme, plus la cuve, l’ergonomie et les fonctions liées au travail avec un outil prennent de l’importance. Le WD 7 Control se place encore plus haut dans cette logique avec une grande cuve, une prise pour outil et des fonctions de contrôle pensées pour les travaux soutenus.</p>
<p>Pour un garage, des gravats non dangereux, de l’eau ou un atelier domestique, cette famille est généralement plus rationnelle qu’un aspirateur de sécurité professionnel. Nos fiches <a href="/modeles/karcher-wd5/">WD5</a> et <a href="/modeles/karcher-wd6/">WD6</a> permettent de descendre au niveau modèle lorsque le besoin est déjà défini.</p>
<h2 id="gamme-nt">La gamme NT : la classe de poussière et le maintien du débit passent devant la taille de cuve</h2>
<p>Les NT changent de logique. Un NT 30/1 Tact Te M ACD est d’abord un appareil classe M avec surveillance du débit, prise asservie, antistatique et décolmatage Tact. Le passage vers un NT 50 ajoute surtout du volume pour des travaux plus lourds. Les variantes H répondent à un niveau de risque différent et ne doivent pas être choisies uniquement parce qu’elles filtrent davantage.</p>
<p>Pour un usage professionnel, commencez donc par la <a href="/guides/classes-l-m-h/">classe nécessaire</a>, puis regardez la capacité, le type de décolmatage, la longueur du flexible et la fréquence de déplacement. Le <a href="/modeles/karcher-nt-30-1-tact/">NT 30/1 Tact</a> illustre bien cette logique plus technique.</p>
<h2 id="tact-acd">Tact et ACD : deux mentions importantes, mais pour des raisons différentes</h2>
<p><strong>Tact</strong> désigne le système de décolmatage automatique Kärcher. Sur les versions récentes, le nettoyage est piloté selon le besoin afin de limiter le colmatage lors de l’aspiration de poussières fines. C’est un vrai critère de productivité avec une ponceuse ou un outil générant beaucoup de poussière, mais il ne remplace jamais une classe de sécurité adaptée.</p>
<p><strong>ACD</strong> concerne la collecte de poussières combustibles dans le cadre décrit par Kärcher et la norme applicable. Cette certification ne doit pas être transformée en promesse générale de compatibilité avec n’importe quelle atmosphère explosive. Là encore, la référence exacte et le contexte d’utilisation priment.</p>
<h2 id="quel-karcher">Quel Kärcher regarder selon le besoin ?</h2>
<div class="table-wrap"><table><thead><tr><th>Besoin</th><th>Famille à regarder</th><th>Pourquoi</th></tr></thead><tbody>
<tr><td>Garage, eau, gravats courants</td><td>WD 3 à WD 6</td><td>Polyvalence et coût plus cohérents.</td></tr>
<tr><td>Atelier / rénovation avec prise outil</td><td>WD 6 / WD 7</td><td>Plus de fonctions sans basculer inutilement vers un aspirateur de sécurité.</td></tr>
<tr><td>Poussières fines avec classe M requise</td><td>NT Tact M</td><td>Classe M, surveillance du débit et décolmatage adapté.</td></tr>
<tr><td>Risque relevant de la classe H</td><td>NT H</td><td>Appareil conçu et certifié pour ce niveau de risque.</td></tr>
</tbody></table></div>
<p>Pour comparer Kärcher au reste du marché, partez ensuite vers le <a href="/comparatifs/aspirateur-classe-m/">comparatif classe M</a>, le <a href="/comparatifs/aspirateur-professionnel/">comparatif professionnel</a> ou notre page <a href="/usages/aspirateur-gravats/">gravats</a> selon la contrainte dominante.</p>
<h2 id="points-vigilance">Ce que la largeur de gamme Kärcher oblige à vérifier</h2>
<p>La proximité des noms peut masquer des différences plus importantes que la puissance : WD, NT L, NT M et NT H ne sont pas interchangeables. Vérifiez aussi la génération exacte, les consommables compatibles et le système de flexible. Enfin, si votre priorité est un écosystème batterie d’outillage, Kärcher est moins intégré qu’un Makita, DeWalt ou Bosch.</p>
''',
},
"festool": {
    "brand": "Festool",
    "verdict": "MAJOR",
    "strategy": "bespoke_system_workflow_ctl_ctm_cth_autoclean",
    "title": "Aspirateurs Festool : CTL, CTM, CTH, AUTOCLEAN et système CLEANTEC",
    "desc": "Festool : choisir entre CTL, CTM et CTH, comprendre AUTOCLEAN, CLEANTEC, Bluetooth, Systainer et les modèles sans fil CTC/CTMC.",
    "toc": [("logique-systeme", "La logique Festool"), ("classes-ct", "CTL, CTM, CTH"), ("midi-autoclean", "MIDI et AUTOCLEAN"), ("sans-fil", "Sans fil CTC/CTMC"), ("ecosysteme", "CLEANTEC et Systainer"), ("quand-festool", "Quand Festool a du sens"), ("sources", "Sources")],
    "body": '''
<div class="answer-box"><p>Festool est rarement le choix le plus rationnel si l’on cherche seulement une cuve qui aspire. La marque devient intéressante quand l’aspirateur fait partie d’un <strong>workflow complet</strong> : ponceuse ou scie, flexible CLEANTEC, Systainer, démarrage Bluetooth et classe de poussière adaptée. Il faut donc choisir d’abord entre CTL, CTM et CTH, puis entre format, AUTOCLEAN et alimentation.</p></div>
<h2 id="logique-systeme">Chez Festool, l’aspirateur se choisit comme une pièce du système de travail</h2>
<p>Le principal avantage de Festool n’est pas une valeur isolée de débit ou de dépression. C’est l’intégration avec les outils de la marque : raccords conçus pour tenir sur les machines, flexible lisse, rangement des coffrets, démarrage à distance et organisation du poste. Cet avantage est réel pour un artisan déjà équipé en Festool ; il perd beaucoup de valeur si l’aspirateur doit fonctionner seul avec des outils d’autres univers.</p>
<p>Cette page reste une analyse documentaire. Nous ne présentons pas l’écosystème comme une preuve de performance absolue : la classe, le captage et le maintien du débit doivent toujours être adaptés au travail réel.</p>
<h2 id="classes-ct">CTL, CTM et CTH : la lettre est plus importante que la ressemblance entre les machines</h2>
<p>La nomenclature Festool est assez lisible : CTL correspond à la classe L, CTM à la classe M et CTH à la classe H. Deux MIDI très proches visuellement peuvent donc répondre à des obligations différentes. Un CTL équipé d’un bon filtre n’est pas un substitut à un CTM ou un CTH lorsque le niveau de risque exige une autre classe.</p>
<p>Le <a href="/guides/classes-l-m-h/">guide L/M/H</a> doit être utilisé avant le choix du modèle. Une fois la classe déterminée, la compacité, le décolmatage et l’intégration avec les outils deviennent les critères secondaires.</p>
<h2 id="midi-autoclean">MIDI I et AUTOCLEAN : le compact devient crédible pour les poussières colmatantes</h2>
<p>Les générations MIDI I existent désormais dans plusieurs classes, avec des variantes AC équipées d’AUTOCLEAN. Le CTM MIDI I AC combine ainsi classe M, format compact et nettoyage automatique du filtre. Le CTH MIDI I AC reprend la logique dans une classe H. Ce positionnement est particulièrement intéressant pour le ponçage, où le maintien du débit et la mobilité comptent davantage qu’une cuve surdimensionnée.</p>
<p>Le revers est évident : une cuve compacte se remplit plus vite. Pour des déchets volumineux ou un atelier fixe qui produit beaucoup de matière, un CTM 26 ou un autre format plus grand peut être plus cohérent.</p>
<h2 id="sans-fil">CTC et CTMC : le sans-fil sert surtout la mobilité autour de l’outil</h2>
<p>Les solutions CTC/CTMC prolongent l’écosystème dans le sans-fil. Elles ont du sens quand l’utilisateur veut supprimer le câble secteur sur des interventions courtes ou mobiles, surtout s’il possède déjà les batteries compatibles. Cela ne change pas la hiérarchie de décision : classe d’abord, autonomie et volume ensuite.</p>
<p>Pour comparer avec d’autres marques mobiles, utilisez le <a href="/comparatifs/aspirateur-chantier-sans-fil/">comparatif sans fil</a> plutôt que de comparer un CTC à un gros extracteur filaire sur la seule capacité.</p>
<h2 id="ecosysteme">CLEANTEC, Systainer et Bluetooth : pourquoi le surcoût peut être rationnel</h2>
<p>Le manchon CLEANTEC verrouille le flexible sur les outils compatibles, les Systainer structurent le transport et Bluetooth peut déclencher l’aspiration via une batterie ou une télécommande. L’intérêt est surtout de réduire les petites frictions : tuyau qui se décroche, coffret séparé, aspirateur à allumer manuellement.</p>
<p>Pour un atelier où la <a href="/usages/aspirateur-ponceuse/">ponceuse</a> est centrale, ces détails peuvent compter plus qu’une différence modeste de caractéristiques brutes. À l’inverse, pour nettoyer un garage ou aspirer de l’eau, ils justifient rarement à eux seuls le prix premium.</p>
<h2 id="quand-festool">Quand Festool est un bon choix — et quand regarder ailleurs</h2>
<div class="table-wrap"><table><thead><tr><th>Situation</th><th>Lecture</th></tr></thead><tbody>
<tr><td>Parc Festool + ponçage fréquent</td><td>Très cohérent : l’écosystème est réellement utilisé.</td></tr>
<tr><td>Besoin classe M compact</td><td>CTM MIDI I / AC est un point d’entrée logique.</td></tr>
<tr><td>Besoin classe H</td><td>Regarder CTH, selon les prescriptions applicables.</td></tr>
<tr><td>Garage, gravats, gros volume à bas coût</td><td>Le premium Festool est moins facile à justifier.</td></tr>
</tbody></table></div>
<p>Mirka est l’alternative la plus naturelle si le besoin est encore plus centré sur le ponçage ; Kärcher ou Nilfisk deviennent plus logiques si la priorité est le volume ou le nettoyage généraliste.</p>
''',
},
"makita": {
    "brand": "Makita",
    "verdict": "MAJOR",
    "strategy": "bespoke_reference_decoding_lxt_xgt_aws",
    "title": "Aspirateurs Makita : comprendre VC, LXT, XGT, AWS et les classes L/M/H",
    "desc": "Makita : décoder les références VC, choisir entre filaire, LXT et XGT, comprendre AWS, Makpac et les variantes de classes L/M/H.",
    "toc": [("lire-reference", "Lire la référence"), ("filaire-vc", "Filaire VC"), ("lxt-xgt", "LXT ou XGT"), ("aws-makpac", "AWS et Makpac"), ("classe-dabord", "Classe avant plateforme"), ("quel-makita", "Quel Makita ?"), ("sources", "Sources")],
    "body": '''
<div class="answer-box"><p>Makita offre beaucoup de choix, mais c’est justement ce qui rend la marque facile à mal lire. Avant de comparer les performances, vérifiez <strong>la référence complète</strong>, la classe L/M/H et la plateforme : filaire VC, LXT 18 V / 18Vx2 ou XGT 40 V. AWS et Makpac peuvent ensuite faire la différence si vous possédez déjà un parc Makita.</p></div>
<h2 id="lire-reference">Chez Makita, le suffixe et la plateforme peuvent changer la décision</h2>
<p>Une mention comme VC4210 ne suffit pas toujours. Les variantes L et M ne répondent pas au même besoin, et les suffixes peuvent signaler une fourniture ou un marché différent. Même prudence sur les machines sans fil : LXT et XGT ne sont pas une seule plateforme malgré le logo Makita commun.</p>
<p>La bonne méthode est donc de partir de la référence exacte, puis de vérifier la classe, la source d’énergie, les batteries nécessaires, le système de filtre et le contenu du kit. Cette étape évite la majorité des erreurs de comparaison sur la marque.</p>
<h2 id="filaire-vc">Les VC filaires : du classe L accessible aux gros volumes M/H</h2>
<p>Le <a href="/modeles/makita-vc2512l/">VC2512L</a> représente bien l’entrée de gamme chantier filaire : classe L, eau/poussière, prise outil et nettoyage Push & Clean. Plus haut, les VC4210 existent en variantes L ou M avec une grande cuve et un système de nettoyage automatique plus adapté aux poussières fines soutenues. Les VC2211/3211 complètent l’offre en classes M ou H selon les références.</p>
<p>Pour un atelier fixe, ces modèles filaires restent souvent plus simples à dimensionner qu’un aspirateur batterie : pas de coût d’autonomie, plus de volume et une offre de classes plus large.</p>
<h2 id="lxt-xgt">LXT, 18Vx2 et XGT : trois lectures différentes du sans-fil</h2>
<p>Makita propose des aspirateurs sur batterie dans plusieurs familles. Les DVC exploitent l’univers LXT, parfois avec deux batteries 18 V, tandis que les VC001G à VC007G appartiennent à XGT 40 V. Ces machines sont intéressantes lorsque les batteries sont déjà disponibles dans le parc ; sinon le coût total peut vite dépasser celui d’une solution filaire.</p>
<p>Ne choisissez pas une plateforme avant d’avoir vérifié la classe. Certaines références sans fil sont L, d’autres M selon les variantes. Le fait d’utiliser une batterie XGT ne dit rien, à lui seul, sur le niveau de protection contre les poussières.</p>
<h2 id="aws-makpac">AWS et Makpac : l’intégration Makita devient utile quand l’outil et l’aspirateur travaillent ensemble</h2>
<p>AWS permet à des outils compatibles de communiquer avec l’aspirateur pour déclencher l’extraction sans câble de commande. Makpac facilite le rangement et le transport avec le reste du parc. Ces fonctions ont une vraie valeur avec une scie, une ponceuse ou un outil Makita utilisé quotidiennement ; elles sont secondaires pour du nettoyage de sol.</p>
<p>Le raccordement reste tout aussi important : diamètre de flexible, adaptateur et étanchéité influencent le captage. Notre guide sur les <a href="/accessoires/adaptateur-outil-electroportatif/">adaptateurs d’outils</a> complète cette vérification.</p>
<h2 id="classe-dabord">Classe de poussière avant batterie, AWS ou puissance moteur</h2>
<p>Makita couvre plusieurs classes, ce qui est un avantage uniquement si l’on ne les mélange pas. Une référence L ne doit pas être présentée comme équivalente à une M parce qu’elle partage la même plateforme de batteries. Pour les poussières réglementées, utilisez d’abord le <a href="/guides/classes-l-m-h/">guide L/M/H</a>, puis comparez le décolmatage et le maintien du débit.</p>
<p>Cette hiérarchie est particulièrement importante pour le bois et la poussière fine. Le <a href="/comparatifs/aspirateur-classe-m/">comparatif classe M</a> permet ensuite de comparer Makita aux alternatives équivalentes.</p>
<h2 id="quel-makita">Quel Makita regarder selon votre parc ?</h2>
<div class="table-wrap"><table><thead><tr><th>Situation</th><th>Point de départ</th></tr></thead><tbody>
<tr><td>Besoin filaire simple classe L</td><td>VC2512L</td></tr>
<tr><td>Grand volume / classe M</td><td>VC4210M ou famille VC M</td></tr>
<tr><td>Parc LXT existant</td><td>DVC / 18Vx2 selon classe requise</td></tr>
<tr><td>Parc XGT 40 V</td><td>VC00xG selon classe, volume et kit</td></tr>
</tbody></table></div>
<p>Makita est très cohérent pour un utilisateur déjà équipé. Pour quelqu’un qui part de zéro, comparez le coût complet avec Bosch, DeWalt ou Festool avant de payer batteries, chargeurs et accessoires supplémentaires.</p>
''',
},
"dewalt": {
    "brand": "DeWalt",
    "verdict": "MAJOR",
    "strategy": "bespoke_flexvolt_airlock_tstak_dust_control",
    "title": "Aspirateurs DeWalt : DCV586M, FLEXVOLT, AIRLOCK et classe M",
    "desc": "DeWalt : comprendre le DCV586M classe M, le DCV584L hybride classe L, FLEXVOLT, TSTAK et AIRLOCK pour l’extraction sur chantier.",
    "toc": [("systeme-chantier", "Le système DeWalt"), ("dcv586m", "DCV586M"), ("dcv584l", "DCV584L"), ("airlock", "AIRLOCK"), ("flexvolt-tstak", "FLEXVOLT et TSTAK"), ("quand-dewalt", "Quand choisir DeWalt"), ("sources", "Sources")],
    "body": '''
<div class="answer-box"><p>DeWalt n’a pas besoin d’une gamme immense pour être pertinent : son intérêt se concentre sur le <strong>chantier sans fil</strong>. Le DCV586M est la pièce maîtresse, avec FLEXVOLT 54 V, classe M, nettoyage automatique et compatibilité TSTAK. Le DCV584L répond à un autre besoin : un petit eau/poussière hybride, mais qui reste classe L malgré son filtre HEPA.</p></div>
<h2 id="systeme-chantier">DeWalt se comprend mieux comme système de captage que comme catalogue d’aspirateurs</h2>
<p>La marque relie l’énergie XR/FLEXVOLT, le rangement TSTAK et les raccords AIRLOCK. Elle propose aussi des systèmes d’extraction directement associés aux outils. Pour un artisan déjà équipé, cette cohérence peut valoir davantage qu’une large liste de cuves et de moteurs.</p>
<p>À l’inverse, si le besoin principal est un aspirateur filaire de 30 à 50 litres disponible dans plusieurs classes, Kärcher, Nilfisk ou Makita proposent une lecture plus large du marché.</p>
<h2 id="dcv586m">DCV586M : le vrai argument DeWalt est le sans-fil classe M</h2>
<p>Le DCV586M combine une batterie XR FLEXVOLT 54 V, une classe M documentée, deux filtres avec nettoyage automatique, une alarme de baisse de performance et une télécommande. Il est aussi conçu pour s’intégrer à TSTAK. Cela en fait une option rare pour qui veut déplacer un extracteur M sans câble secteur sur le chantier.</p>
<p>Le coût doit cependant être lu avec les batteries. La version machine seule n’inclut pas nécessairement batterie ni chargeur. Si le parc FLEXVOLT existe déjà, l’équation change complètement ; sinon il faut comparer le système complet à une solution filaire.</p>
<h2 id="dcv584l">DCV584L : polyvalent et hybride, mais toujours classe L</h2>
<p>Le DCV584L peut fonctionner sur secteur ou avec des batteries XR/FLEXVOLT compatibles et accepte l’eau comme les poussières. Son filtre HEPA est un avantage de filtration, mais il ne transforme pas l’appareil en classe M. Cette distinction est précisément le type de raccourci que notre méthodologie interdit.</p>
<p>Il est donc cohérent pour du nettoyage mobile, des interventions courtes ou une poussière compatible avec la classe L. Pour un besoin M, le DCV586M ou un concurrent certifié M doit rester le point de comparaison.</p>
<h2 id="airlock">AIRLOCK : la connexion à l’outil est un vrai différenciateur</h2>
<p>AIRLOCK vise à simplifier le raccordement entre l’aspirateur et les outils compatibles. L’intérêt dépasse le confort : un raccord stable et correctement dimensionné aide le captage à la source et évite qu’un flexible se décroche en plein travail. DeWalt complète ce système avec des accessoires d’extraction dédiés au perçage et au burinage.</p>
<p>Cette logique est plus importante pour une ponceuse, une scie ou un perforateur que pour le simple nettoyage d’un atelier. Notre page <a href="/usages/aspirateur-ponceuse/">aspirateur pour ponceuse</a> permet de remettre le raccordement dans le contexte du débit et du colmatage.</p>
<h2 id="flexvolt-tstak">FLEXVOLT et TSTAK : la valeur dépend de ce que vous possédez déjà</h2>
<p>Les batteries FLEXVOLT peuvent alimenter des outils 54 V et être utilisées dans l’écosystème XR 18 V compatible. TSTAK, lui, structure le transport des coffrets. Pour un utilisateur DeWalt, l’aspirateur s’intègre donc dans un parc existant plutôt que de créer une nouvelle plateforme.</p>
<p>Ce bénéfice disparaît presque entièrement si vous n’avez ni batteries ni coffrets DeWalt. Dans ce cas, comparez le prix du système complet et pas seulement celui de la machine nue.</p>
<h2 id="quand-dewalt">Quand choisir DeWalt plutôt qu’une gamme plus large ?</h2>
<div class="table-wrap"><table><thead><tr><th>Besoin</th><th>Lecture</th></tr></thead><tbody>
<tr><td>Classe M mobile + parc FLEXVOLT</td><td>DCV586M très cohérent.</td></tr>
<tr><td>Nettoyage hybride secteur/batterie classe L</td><td>DCV584L pertinent.</td></tr>
<tr><td>Gros volume filaire multi-classes</td><td>Regarder aussi Kärcher, Nilfisk ou Makita.</td></tr>
<tr><td>Extraction directement à l’outil</td><td>AIRLOCK et Perform & Protect donnent du sens à la marque.</td></tr>
</tbody></table></div>
<p>Pour la sécurité, gardez toujours la <a href="/guides/classes-l-m-h/">classe de poussière</a> devant la plateforme de batterie.</p>
''',
},
"parkside": {
    "brand": "Parkside",
    "verdict": "MAJOR",
    "strategy": "bespoke_budget_stock_generation_logic",
    "title": "Aspirateurs Parkside : PWD 12, 20, 25 et 30 — pour quels usages ?",
    "desc": "Parkside : comparer les PWD 12, 20, 25 et 30, comprendre disponibilité, prise outil, nettoyage de filtre et limites face aux classes M/H.",
    "toc": [("logique-parkside", "La logique Parkside"), ("gamme-pwd", "PWD 12 à 30"), ("disponibilite", "Disponibilité"), ("prise-filtre", "Prise et filtre"), ("securite", "Limites sécurité"), ("quand-parkside", "Quand Parkside suffit"), ("sources", "Sources")],
    "body": '''
<div class="answer-box"><p>Parkside est d’abord une proposition de <strong>rapport équipement/prix</strong>. Les PWD 12, 20, 25 et 30 couvrent le nettoyage eau/poussière, le garage et le bricolage avec des cuves et des équipements différents. La question n’est pas de savoir si Parkside « vaut » une marque pro, mais si votre usage exige réellement une classe de sécurité, un décolmatage automatique ou un SAV/consommables plus structurés.</p></div>
<h2 id="logique-parkside">Parkside : choisir par usage et disponibilité, pas par hiérarchie professionnelle</h2>
<p>La gamme Lidl évolue au rythme des références et des stocks. Un modèle intéressant aujourd’hui peut être remplacé par une nouvelle révision quelques mois plus tard. Cette instabilité est moins gênante pour un achat occasionnel que pour un professionnel qui veut standardiser filtres, sacs et pièces sur plusieurs années.</p>
<p>Pour un particulier, l’avantage reste clair : beaucoup d’équipement pour un prix contenu. Il faut simplement résister à la tentation de comparer un PWD à un aspirateur M professionnel uniquement sur les watts ou les Air Watts.</p>
<h2 id="gamme-pwd">PWD 12, 20, 25 et 30 : quatre formats, pas quatre niveaux de sécurité</h2>
<div class="table-wrap"><table><thead><tr><th>Modèle</th><th>Format</th><th>Usage logique</th></tr></thead><tbody>
<tr><td>PWD 12 B1</td><td>12 L</td><td>Petit nettoyage, voiture, appoint.</td></tr>
<tr><td>PWD 20 C3</td><td>≈20 L</td><td>Garage et bricolage polyvalent.</td></tr>
<tr><td>PWD 25 C4</td><td>25 L</td><td>Rénovation domestique et volume intermédiaire.</td></tr>
<tr><td>PWD 30 C1</td><td>30 L</td><td>Grand format DIY avec davantage d’équipement.</td></tr>
</tbody></table></div>
<p>Le volume doit être choisi selon la fréquence de vidage et la mobilité. Une cuve de 30 L n’est pas automatiquement meilleure si l’appareil doit monter des escaliers ou être rangé dans un petit atelier.</p>
<h2 id="disponibilite">La référence exacte compte plus chez Parkside que chez une gamme professionnelle stable</h2>
<p>Les suffixes B1, C3, C4 ou C1 identifient des révisions précises. Les accessoires, filtres et sacs ne doivent donc pas être commandés uniquement sur le mot « Parkside ». Vérifiez toujours la génération indiquée sur l’appareil et la fiche Lidl correspondante.</p>
<p>C’est aussi une raison de ne pas reprendre aveuglément une ancienne recommandation PNTS trouvée en ligne : ces séries peuvent rester pertinentes pour un parc existant sans représenter l’offre actuelle.</p>
<h2 id="prise-filtre">Prise outil et nettoyage du filtre : utiles, mais pas équivalents aux systèmes pro</h2>
<p>Les grandes références Parkside peuvent proposer une prise outil, un adaptateur et un bouton de nettoyage du filtre. Pour du bricolage occasionnel, c’est très pratique. En revanche, un nettoyage déclenché manuellement n’est pas la même chose qu’un Tact, AFC ou InfiniClean conçu pour maintenir le débit pendant de longues séquences de poussière fine.</p>
<p>Si votre usage principal est le ponçage intensif, comparez le <a href="/guides/decolmatage-automatique/">décolmatage automatique</a> et la disponibilité des filtres avant de privilégier le prix d’achat.</p>
<h2 id="securite">Un filtre plissé ou une forte puissance ne donnent pas une classe M ou H</h2>
<p>Les PWD sont présentés comme aspirateurs eau et poussière de bricolage. Sans certification explicite de la référence, il ne faut pas leur attribuer une classe M ou H. Si la poussière impose une classe de sécurité, la bonne comparaison se fait avec des machines certifiées de cette classe.</p>
<p>Notre <a href="/guides/classes-l-m-h/">guide L/M/H</a> explique pourquoi la classe concerne l’appareil complet et pas seulement le filtre.</p>
<h2 id="quand-parkside">Quand Parkside est une bonne affaire — et quand le prix initial devient secondaire</h2>
<p>Parkside est cohérent pour un garage, un véhicule, des petits gravats non dangereux ou une rénovation occasionnelle. Le PWD 20 ou 25 représente souvent un compromis plus facile à déplacer qu’un grand 30 L. Le PWD 30 devient intéressant si la prise outil et la capacité sont réellement utilisées.</p>
<p>Pour un usage quotidien professionnel, regardez au-delà du prix : disponibilité des consommables, endurance du filtre, procédure de décolmatage, bruit, SAV et classe de poussière. Dans ce contexte, Kärcher, Nilfisk, Makita ou Bosch peuvent coûter plus cher à l’achat tout en offrir un workflow plus stable.</p>
''',
},
"nilfisk": {
    "brand": "Nilfisk",
    "verdict": "MAJOR",
    "strategy": "bespoke_cleaning_specialist_multi_vs_attix",
    "title": "Aspirateurs Nilfisk : Multi II, ATTIX, InfiniClean et classes M/H",
    "desc": "Nilfisk : comprendre Multi II vs ATTIX, InfiniClean, FlowSensor, antistatique et les variantes de classes M/H pour atelier et chantier.",
    "toc": [("deux-univers", "Deux univers"), ("buddy-multi", "Buddy et Multi"), ("attix", "ATTIX"), ("infiniclean", "InfiniClean"), ("specialiste", "Spécialiste aspiration"), ("quel-nilfisk", "Quel Nilfisk ?"), ("sources", "Sources")],
    "body": '''
<div class="answer-box"><p>Nilfisk sépare assez bien deux besoins : <strong>Buddy/Multi</strong> pour l’eau, les saletés et l’atelier grand public ; <strong>ATTIX</strong> pour l’aspiration professionnelle, avec InfiniClean et des variantes L, M ou H selon les références. La marque a moins d’intégration avec des batteries d’outillage, mais davantage de profondeur comme spécialiste de l’aspiration.</p></div>
<h2 id="deux-univers">Nilfisk : le bon choix dépend d’abord de Multi ou ATTIX</h2>
<p>Un Multi II et un ATTIX peuvent tous deux aspirer poussières et liquides, mais ils ne jouent pas le même rôle. Multi vise la polyvalence domestique et l’atelier ; ATTIX ajoute des architectures de filtration, de décolmatage et de surveillance conçues pour des usages professionnels et, selon la variante, des poussières dangereuses.</p>
<p>Cette séparation est plus utile que de chercher un classement unique de tous les Nilfisk.</p>
<h2 id="buddy-multi">Buddy II et Multi II : simples, robustes et cohérents pour le garage</h2>
<p>Buddy II couvre les petits formats de nettoyage occasionnel. Multi II monte en capacité et en équipement, notamment avec des variantes 22 ou 30 litres et une prise outil selon le modèle. Le Multi II 30 T est donc un point de départ logique pour un atelier ou une rénovation courante sans besoin de classe de sécurité supérieure.</p>
<p>Ce type de machine reste à comparer aux autres <a href="/comparatifs/aspirateur-eau-poussiere/">aspirateurs eau et poussière</a>, pas à un ATTIX M sur la seule taille de cuve.</p>
<h2 id="attix">ATTIX : la classe et le système de filtration définissent la machine</h2>
<p>La famille ATTIX 33/44 existe dans plusieurs variantes. Un ATTIX 44-2M IC combine une cuve d’environ 42 L, une classe M documentée, surveillance du débit, antistatique et InfiniClean. Les versions H ajoutent une architecture correspondant à un niveau de risque différent.</p>
<p>Le nom ATTIX seul ne suffit donc pas : il faut lire la référence complète, la classe et le type de filtre. C’est particulièrement important sur le marché de l’occasion ou lorsque plusieurs variantes proches apparaissent chez les revendeurs.</p>
<h2 id="infiniclean">InfiniClean : le vrai différenciateur Nilfisk avec les poussières colmatantes</h2>
<p>InfiniClean nettoie automatiquement le filtre par impulsions régulières afin de limiter la perte de performance pendant l’aspiration. Sur la documentation ATTIX, Nilfisk met en avant un nettoyage automatique combiné à un filtre PTFE anti-adhérent. Ce système a surtout de la valeur lorsque le filtre se charge vite.</p>
<p>Pour de simples gravats grossiers, ce bénéfice est moins déterminant. Pour du ponçage ou des poussières fines, le <a href="/guides/decolmatage-automatique/">décolmatage</a> devient un critère central avec la classe et le raccordement à l’outil.</p>
<h2 id="specialiste">L’absence de plateforme d’outillage peut aussi être un avantage</h2>
<p>Nilfisk ne cherche pas à vous enfermer dans une batterie de perceuse ou un coffret propriétaire. L’écosystème se concentre sur l’aspiration : flexibles, filtres, sacs, accessoires, antistatique et adaptateurs de rangement. Pour quelqu’un qui utilise plusieurs marques d’outils, cette neutralité peut être plus pratique qu’un système très intégré à un seul fabricant.</p>
<p>En contrepartie, vous ne mutualisez pas batteries et chargeurs comme chez Makita, DeWalt ou Bosch.</p>
<h2 id="quel-nilfisk">Quel Nilfisk regarder selon le travail ?</h2>
<div class="table-wrap"><table><thead><tr><th>Besoin</th><th>Point de départ</th></tr></thead><tbody>
<tr><td>Nettoyage occasionnel</td><td>Buddy II</td></tr>
<tr><td>Garage / atelier / eau</td><td>Multi II 22 ou 30</td></tr>
<tr><td>Poussières fines professionnelles, classe M</td><td>ATTIX M avec InfiniClean</td></tr>
<tr><td>Risque relevant de H</td><td>ATTIX H selon référence et prescriptions</td></tr>
</tbody></table></div>
<p>Pour une décision sécurité, commencez toujours par les <a href="/guides/classes-l-m-h/">classes L/M/H</a> avant de regarder le volume ou le système de rangement.</p>
''',
},
"mirka": {
    "brand": "Mirka",
    "verdict": "MAJOR",
    "strategy": "bespoke_dust_free_sanding_dexos_workflow",
    "title": "Aspirateurs Mirka : DEXOS 1217/1230, AFC et système de ponçage",
    "desc": "Mirka : comprendre DEXOS 1217 et 1230 classe M, AFC, Bluetooth, myMirka et l’intégration avec DEROS/DEOS pour le ponçage.",
    "toc": [("poncage-dabord", "Le ponçage d’abord"), ("dexos", "Génération DEXOS"), ("1217-1230", "1217 vs 1230"), ("deros-deos", "DEROS / DEOS"), ("workflow", "Workflow Mirka"), ("limites", "Limites"), ("sources", "Sources")],
    "body": '''
<div class="answer-box"><p>Mirka n’est pas une marque d’aspirateurs généralistes devenue bonne en ponçage : son point de départ est justement le <strong>ponçage sans poussière</strong>. Les DEXOS 1217 M AFC et 1230 M AFC sont donc à lire avec les ponceuses DEROS/DEOS, les abrasifs maillés, les flexibles et le poste de travail. Pour des gravats ou un garage, cet écosystème premium a beaucoup moins de sens.</p></div>
<h2 id="poncage-dabord">Chez Mirka, l’aspiration est une extension du système de ponçage</h2>
<p>La valeur de Mirka apparaît lorsque l’on capte la poussière directement au plateau de ponçage. Les abrasifs maillés, les ponceuses et les extracteurs sont pensés ensemble. Dans ce contexte, la constance du débit, l’ergonomie du flexible et le contrôle de l’aspirateur ont plus d’importance qu’une très grande cuve.</p>
<p>C’est aussi ce qui rend Mirka moins universel : l’investissement est difficile à justifier pour un usage essentiellement eau/poussière ou gravats.</p>
<h2 id="dexos">DEXOS remplace progressivement la lecture centrée sur les anciens DE</h2>
<p>La génération DEXOS structure désormais l’offre actuelle. Le 1217 M AFC est un compact 17 L de classe M avec moteur brushless, nettoyage automatique du filtre et connectivité Bluetooth. Le 1230 M AFC porte la même logique vers 30 L et un poste de travail plus complet.</p>
<p>Les anciens DE 1230/1242 restent pertinents pour un parc existant, mais ils ne doivent plus être utilisés comme seuls repères pour décrire Mirka en 2026.</p>
<h2 id="1217-1230">DEXOS 1217 ou 1230 : mobilité contre capacité, pas « entrée de gamme » contre « pro »</h2>
<div class="table-wrap"><table><thead><tr><th>Modèle</th><th>Atout principal</th><th>Compromis</th></tr></thead><tbody>
<tr><td>DEXOS 1217 M AFC</td><td>Compact, 17 L, facile à déplacer</td><td>Vidages plus fréquents</td></tr>
<tr><td>DEXOS 1230 M AFC</td><td>30 L, deux prises auto et workstation possible</td><td>Plus volumineux</td></tr>
</tbody></table></div>
<p>Les deux restent des appareils classe M. Le passage au 1230 répond donc surtout au besoin de capacité et d’organisation du poste, pas à un changement de classe de sécurité.</p>
<h2 id="deros-deos">DEROS II, DEOS II et DEROS RS donnent son sens à l’extracteur</h2>
<p>Le système Mirka est particulièrement logique avec les ponceuses de la marque. Un bon captage réduit la poussière autour du plateau et améliore le confort de travail, mais la classe M de l’extracteur doit toujours correspondre au risque réel. Mirka ne doit pas être présenté comme une solution universelle à toutes les poussières dangereuses.</p>
<p>Pour les travaux de finition, consultez aussi notre page <a href="/usages/aspirateur-ponceuse/">aspirateur pour ponceuse</a> afin de comparer le captage, le débit et le décolmatage.</p>
<h2 id="workflow">Bluetooth, myMirka et workstation : des fonctions de workflow, pas des gadgets</h2>
<p>La connectivité Bluetooth permet d’intégrer le DEXOS à l’application myMirka, et une télécommande dédiée peut simplifier le pilotage. Sur le 1230, la workstation transforme l’extracteur en chariot mobile pour outils et abrasifs. Ces fonctions ont une vraie valeur dans un atelier de finition où l’on répète les mêmes gestes toute la journée.</p>
<p>Pour un utilisateur occasionnel, elles peuvent au contraire devenir du coût sans bénéfice concret. La bonne question est donc moins « quelle technologie est disponible ? » que « quelle partie du workflow vais-je réellement utiliser ? »</p>
<h2 id="limites">Les limites du système Mirka doivent rester visibles</h2>
<p>Mirka reste premium, spécialisé et surtout centré sur la classe M dans la gamme DEXOS actuelle. Si votre besoin principal concerne de très gros volumes, des liquides, des gravats ou une classe H, d’autres marques ont une offre plus large. Si vous utilisez déjà Festool pour le ponçage et les coffrets, le gain à changer d’écosystème peut également être faible.</p>
<p>Pour comparer les machines M sur des bases équivalentes, utilisez notre <a href="/comparatifs/aspirateur-classe-m/">comparatif classe M</a> et le guide sur le <a href="/guides/decolmatage-automatique/">décolmatage automatique</a>.</p>
''',
},
}


def article_html(slug):
    cfg = BRANDS[slug]
    return '<!-- BRAND_CONTENT_START -->\n' + cfg['body'].strip() + f'''\n<h2 id="sources">Sources consultées</h2>\n<p>Cette page est une analyse documentaire des fiches et gammes officielles consultées le {UPDATED_DISPLAY}. Nous ne présentons pas ces éléments comme des mesures réalisées par notre rédaction.</p>\n<ul>{sources_html(slug)}</ul>\n<p><small>Mise à jour : {UPDATED_DISPLAY}. Analyse documentaire, sans test physique. Les liens affiliés éventuels n’influencent ni les classes, ni les caractéristiques retenues, ni l’orientation éditoriale.</small></p>\n<!-- BRAND_CONTENT_END -->'''


def toc_html(slug):
    return ''.join(f'<a href="#{escape(anchor)}">{escape(label)}</a>' for anchor, label in BRANDS[slug]['toc'])


def replace_once(pattern, repl, text, label, flags=0):
    out, n = re.subn(pattern, repl, text, count=1, flags=flags)
    if n != 1:
        raise RuntimeError(f'{label}: expected one replacement, got {n}')
    return out


def patch_page(slug):
    cfg = BRANDS[slug]
    path = BASE / 'marques' / slug / 'index.html'
    html = path.read_text(encoding='utf-8')

    html = replace_once(r'<title>.*?</title>', f'<title>{cfg["title"]}</title>', html, f'{slug} title', re.S)
    html = replace_once(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{escape(cfg["desc"], quote=True)}">', html, f'{slug} meta')
    html = replace_once(r'<h1 style="margin-top:10px;">.*?</h1>', f'<h1 style="margin-top:10px;">{cfg["title"]}</h1>', html, f'{slug} h1', re.S)
    html = replace_once(r'<p class="lead">.*?</p>', f'<p class="lead">{cfg["desc"]}</p>', html, f'{slug} lead', re.S)
    html = replace_once(r'<span class="meta-tag">[^<]*</span>', f'<span class="meta-tag">Vérifié : {UPDATED_DISPLAY}</span>', html, f'{slug} verified')
    html = replace_once(r'<!-- BRAND_CONTENT_START -->.*?<!-- BRAND_CONTENT_END -->', article_html(slug), html, f'{slug} article', re.S)
    html = replace_once(
        r'(<div class="sidebar-box-head">Sommaire</div>\s*<div class="sidebar-box-body">\s*<nav class="toc-list">).*?(</nav>)',
        lambda m: m.group(1) + toc_html(slug) + m.group(2),
        html,
        f'{slug} toc',
        re.S,
    )
    path.write_text(html, encoding='utf-8')


def patch_ledger(slug):
    path = BASE / '.content' / 'brands' / f'{slug}.yaml'
    obj = json.loads(path.read_text(encoding='utf-8'))
    obj['updated_at'] = UPDATED_ISO
    obj['source_of_truth'] = '_generate_brand_overrides.py'
    obj['structure_strategy'] = BRANDS[slug]['strategy']
    obj['recovery_verdict'] = BRANDS[slug]['verdict']
    obj.setdefault('editorial', {})['desk_research_only'] = True
    obj['editorial']['affiliate_influence'] = False
    obj['editorial']['human_validation_required'] = True
    obj['editorial']['publish_review'] = 'READY_FOR_HUMAN_VALIDATION'
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def write_audit(slug):
    cfg = BRANDS[slug]
    path = BASE / '.content' / 'brands' / 'audits' / f'{slug}-2026-09-09.md'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f'''# Audit marque — {cfg['brand']} — 2026-09-09\n\n- Verdict recovery : **{cfg['verdict']}**\n- Stratégie : `{cfg['strategy']}`\n- Conservation : faits, sources primaires, modèles actuels, liens internes utiles et design du site.\n- Réécriture : structure éditoriale clonée, transitions génériques et blocs forces/limites/pour qui/éviter lorsque ceux-ci imposaient le même squelette que les autres marques.\n- Méthode : stack partagé 80/20 + couche métier aspirateurs-chantier.\n- Statut : **READY_FOR_HUMAN_VALIDATION**.\n- Indexation : `noindex, follow` conservé.\n''', encoding='utf-8')


def main():
    for slug in BRANDS:
        patch_page(slug)
        patch_ledger(slug)
        write_audit(slug)
        print(f'✓ bespoke brand override: {slug}')


if __name__ == '__main__':
    main()
