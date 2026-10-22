#!/usr/bin/env python3
"""Apply production-ready guide content after `_generate.py`.

This file is the editorial source of truth for /guides/. The main generator keeps
site-wide layout/navigation; this post-generator replaces guide placeholders,
answer boxes and TOCs while preserving the global HTML/CSS shell.

Recommended regeneration order:
    python _generate.py
    python _generate_guides.py
"""
from pathlib import Path
import re

BASE = Path(__file__).resolve().parent
VERIFIED = "09/2026"

SOURCES = {
    "iec": "https://webstore.iec.ch/en/publication/64777",
    "festool_classes": "https://www.festool.fr/produits/aspirateurs/aspirateurs-de-chantier/577891---ctl-36-ei-ac-renofix",
    "bosch_gas35": "https://www.bosch-professional.com/fr/fr/products/gas-35-m-afc-06019C31W0/",
    "inrs_wood": "https://www.inrs.fr/media.html?refINRS=ED+6052",
    "inrs_asbestos": "https://www.inrs.fr/risques/amiante/prevention-risque-amiante.html",
    "inrs_silica": "https://www.inrs.fr/risques/silice-cristalline/ce-qu-il-faut-retenir.html",
    "hepa": "https://airfiltration.mann-hummel.com/en-uk/insights/filter-classification/din-en-1822.html",
}


def sources(*keys):
    labels = {
        "iec": "IEC 60335-2-69:2021 — exigences applicables aux aspirateurs commerciaux et poussières dangereuses",
        "festool_classes": "Festool — synthèse des classes de poussières L, M et H issue d’EN/IEC 60335-2-69",
        "bosch_gas35": "Bosch Professional — données techniques et nettoyage automatique du GAS 35 M AFC",
        "inrs_wood": "INRS ED 6052 — aspiration des poussières de bois sur machines portatives",
        "inrs_asbestos": "INRS — prévention du risque amiante et cahier des charges des aspirateurs",
        "inrs_silica": "INRS — prévention des expositions à la silice cristalline",
        "hepa": "MANN+HUMMEL — classification EN 1822 des filtres EPA/HEPA/ULPA",
    }
    items = "\n".join(
        f'<li><a href="{SOURCES[k]}" target="_blank" rel="noopener noreferrer">{labels[k]}</a></li>'
        for k in keys
    )
    return f'''<h2 id="sources">Sources et références</h2>
<p>Les données normatives et techniques ci-dessus ont été recoupées avec les sources suivantes. Les exigences de prévention peuvent dépendre du matériau, du procédé et de la réglementation applicable à votre situation : en contexte professionnel, la fiche de données de sécurité, l’évaluation des risques et la notice de l’appareil priment sur un guide généraliste.</p>
<ul>{items}</ul>'''


def related(*pairs):
    return " ".join(f'<a href="{url}">{label}</a>' for label, url in pairs)


GUIDES = {
"comment-choisir-aspirateur-de-chantier": {
"answer": "Pour choisir un aspirateur de chantier, commencez par la poussière à capter et le mode de travail, pas par les watts du moteur. La classe de poussières, la qualité du captage à la source, le débit et la dépression réellement disponibles, puis le décolmatage et la connexion à l’outil déterminent l’adéquation d’un appareil à votre usage.",
"toc": [("priorites", "Les critères à regarder en priorité"), ("classe", "Choisir la classe de poussières"), ("performance", "Débit, dépression et puissance"), ("equipements", "Décolmatage, prise et flexible"), ("capacite", "Cuve, mobilité et consommables"), ("cas", "Choisir selon son chantier"), ("erreurs", "Les erreurs à éviter"), ("sources", "Sources")],
"body": f'''
<h2 id="priorites">Les critères à regarder en priorité</h2>
<p>Un bon aspirateur de chantier n’est pas simplement un aspirateur domestique plus puissant. Il doit capter les poussières au plus près de leur émission, résister à un environnement chargé en débris et conserver des performances suffisantes lorsque le filtre se charge. La première question est donc : <strong>qu’allez-vous aspirer et avec quel outil ?</strong> Une ponceuse à plâtre produit un flux continu de poussières fines ; une scie génère beaucoup de particules et de copeaux ; le nettoyage de gravats sollicite davantage la dépression et la robustesse du flexible.</p>
<p>La hiérarchie utile est généralement la suivante : nature du contaminant et classe de poussières, captage à la source, performance aéraulique, gestion du filtre, compatibilité avec l’outil, puis capacité et confort de transport. Cette logique évite d’acheter un modèle surdimensionné sur un critère marketing mais inadapté au risque ou au travail réel.</p>

<h2 id="classe">Choisir la classe de poussières avant la puissance</h2>
<p>Les classes L, M et H renvoient à la gestion des poussières par l’appareil complet selon la famille de normes EN/IEC 60335-2-69. Elles ne doivent pas être confondues avec la seule classe du média filtrant. Les degrés de séparation couramment repris par les fabricants sont supérieurs à 99 % pour L, 99,9 % pour M et 99,995 % pour H, avec des domaines d’usage différents. La classe pertinente dépend du danger associé à la poussière et des règles applicables à l’activité.</p>
<p>Pour un particulier, cela signifie qu’il ne faut pas déduire la classe nécessaire du seul nom du matériau. En professionnel, l’évaluation des risques, la VLEP lorsqu’elle existe, la fiche de données de sécurité et les prescriptions nationales doivent guider le choix. Pour l’amiante, par exemple, l’INRS demande un aspirateur de classe H répondant à des exigences complémentaires. Notre <a href="/guides/classes-l-m-h/">guide des classes L, M et H</a> détaille ces différences sans transformer une recommandation générale en règle universelle.</p>

<h2 id="performance">Débit d’air, dépression et watts : trois données différentes</h2>
<p>La <strong>dépression</strong>, exprimée notamment en kPa ou mbar, décrit la capacité du système à créer une différence de pression. Elle compte lorsqu’il faut vaincre des pertes de charge ou déplacer des déchets plus lourds. Le <strong>débit d’air</strong>, en L/s ou m³/h, indique le volume d’air déplacé et devient central pour capter des poussières à la source. Ces deux valeurs se complètent ; aucune ne résume seule la performance.</p>
<p>La puissance électrique en watts renseigne surtout sur la consommation ou la puissance absorbée du moteur. Elle ne permet pas de comparer proprement deux machines de conceptions différentes. Vérifiez également le point de mesure : une valeur maximale à la turbine n’est pas identique à une mesure au bout du flexible. Pour aller plus loin, consultez nos guides sur la <a href="/guides/depression-kpa-mbar-air-watt/">dépression et les unités</a>, le <a href="/guides/debit-air-aspirateur/">débit d’air</a> et la <a href="/guides/puissance-aspiration/">puissance d’un aspirateur de chantier</a>.</p>

<h2 id="equipements">Décolmatage, prise asservie et flexible : ce qui change le travail quotidien</h2>
<p>Avec des poussières fines, le filtre se charge rapidement. Un système de nettoyage automatique ou semi-automatique peut limiter la perte de débit et espacer les interventions manuelles. Les technologies varient selon les marques : l’intérêt n’est pas le nom commercial mais la capacité à maintenir le système exploitable pendant une tâche poussiéreuse. Pour du ponçage intensif, c’est souvent un équipement beaucoup plus déterminant qu’un gain marginal de puissance moteur.</p>
<p>La <a href="/guides/prise-asservie/">prise asservie</a> simplifie l’usage avec un outil filaire en déclenchant l’aspirateur quand l’outil démarre. Il faut toutefois respecter la puissance admissible indiquée par le fabricant. Le diamètre, la longueur et la souplesse du flexible influencent aussi les pertes de charge et la maniabilité. Enfin, un raccord qui fuit ou un adaptateur mal ajusté peut ruiner l’efficacité d’un ensemble pourtant performant sur le papier.</p>

<h2 id="capacite">Cuve, mobilité et consommables : dimensionner sans suracheter</h2>
<p>La capacité annoncée est souvent une capacité brute. Le volume réellement utilisable peut être sensiblement inférieur à cause du filtre, du sac et, en aspiration de liquides, du niveau d’arrêt. Une grande cuve réduit les vidages mais ajoute de l’encombrement et du poids lorsque l’appareil est plein. Pour une machine déplacée d’étage en étage, la compacité peut avoir plus de valeur qu’une réserve de dix litres supplémentaire.</p>
<p>Regardez aussi le coût et la disponibilité des sacs, filtres et raccords. Le choix <a href="/guides/sac-ou-sans-sac/">avec ou sans sac</a> n’est pas seulement économique : un sac adapté facilite la gestion des poussières fines et limite leur remise en suspension au vidage. La bonne capacité est donc celle qui correspond au rythme de collecte, à la mobilité et au mode de déchet, pas un nombre maximal à atteindre.</p>

<h2 id="cas">Choisir selon son chantier : raisonner par contrainte dominante</h2>
<p>Pour le ponçage ou le plâtre, la continuité du débit, la gestion du filtre et le raccordement à l’outil sont prioritaires. Pour le bois et la sciure, le captage à la source et le débit prennent une importance particulière. Pour les gravats ou l’eau, la robustesse de la cuve, l’aptitude eau/poussière et le système d’arrêt de liquide deviennent essentiels. Dans un atelier, la longueur du flexible, la mobilité, le bruit et la disponibilité des consommables peuvent peser autant que les valeurs maximales.</p>
<p>Une fois les contraintes fixées, comparez des appareils de même catégorie dans notre <a href="/comparatifs/meilleur-aspirateur-de-chantier/">comparatif général</a> ou partez d’un usage précis : <a href="/usages/aspirateur-ponceuse/">ponceuse</a>, <a href="/usages/aspirateur-platre/">plâtre</a>, <a href="/usages/aspirateur-bois-sciure-copeaux/">bois et sciure</a> ou <a href="/usages/aspirateur-gravats/">gravats</a>. Cette approche réduit les comparaisons inutiles.</p>

<h2 id="erreurs">Les erreurs à éviter avant l’achat</h2>
<p>Évitez de choisir uniquement sur le nombre de watts, de considérer « HEPA » comme synonyme de classe H, ou d’acheter une grande cuve sans regarder le volume net. Méfiez-vous aussi des fiches qui mélangent débit à la turbine et débit disponible à l’outil. Deux chiffres proches ne sont comparables que si les conditions de mesure le sont également.</p>
<p>Enfin, n’utilisez pas un aspirateur standard comme solution improvisée pour une poussière dangereuse. Le captage, le confinement, le mode de vidage et la maintenance font partie du système de prévention. Le meilleur appareil est celui qui est correctement dimensionné, raccordé, entretenu et utilisé pour le risque prévu — pas celui qui affiche la plus grosse valeur isolée.</p>
{sources("iec", "festool_classes", "bosch_gas35", "inrs_silica")}
'''
},

"classes-l-m-h": {
"answer": "Les classes L, M et H classent les aspirateurs destinés aux poussières selon le niveau de risque et les performances de séparation du système. En simplifiant, L vise les poussières à risque plus faible, M des poussières plus préoccupantes comme de nombreux poussières de bois et minérales, et H les poussières hautement dangereuses. Le choix doit suivre l’évaluation du risque et les règles applicables, pas seulement le matériau affiché sur un tableau.",
"toc": [("norme", "Ce que signifient L, M et H"), ("differences", "Les différences essentielles"), ("materiaux", "Matériaux et cas d’usage"), ("hepa", "Classe H et HEPA : ne pas confondre"), ("choix", "Comment choisir sans se tromper"), ("entretien", "Vidage et maintenance"), ("sources", "Sources")],
"body": f'''
<h2 id="norme">Ce que signifient réellement les classes L, M et H</h2>
<p>Les classes de poussières L, M et H sont utilisées pour les extracteurs de poussières commerciaux couverts par EN/IEC 60335-2-69. Elles décrivent une combinaison d’exigences sur l’appareil et sa capacité à gérer certaines poussières dangereuses. Il ne s’agit donc pas d’un simple autocollant posé sur un filtre. L’étanchéité du système, le dispositif de collecte, le contrôle du débit et les modalités de vidage peuvent aussi entrer en jeu selon la classe et la conception de la machine.</p>
<p>Les fabricants reprennent généralement les degrés de séparation suivants : plus de 99 % pour la classe L, plus de 99,9 % pour M et plus de 99,995 % pour H. Ces chiffres aident à comprendre l’échelle, mais ils ne suffisent pas à sélectionner un appareil. Les valeurs limites d’exposition et les règles nationales restent déterminantes, surtout en environnement professionnel.</p>

<h2 id="differences">Les différences essentielles entre L, M et H</h2>
<p>La classe L correspond au niveau le moins exigeant des trois pour la gestion des poussières. La classe M impose une séparation supérieure et est couramment associée aux poussières de bois, d’enduits, de plâtre, de ciment, de béton ou de certaines peintures dans la documentation des fabricants. La classe H vise les poussières hautement dangereuses, notamment certaines poussières cancérigènes ou pathogènes.</p>
<p>Cette graduation ne signifie pas qu’un matériau appartient toujours à une classe unique, quelles que soient les conditions. La composition du produit, la présence de silice cristalline, le procédé de travail et la réglementation peuvent changer l’évaluation. Pour les professionnels, le bon réflexe est de partir de l’analyse du risque et des documents du matériau avant de choisir l’extracteur.</p>

<h2 id="materiaux">Plâtre, bois, béton, silice : pourquoi le nom du matériau ne suffit pas</h2>
<p>Le ponçage du plâtre produit des poussières fines qui colmatent rapidement un filtre ; le bois génère à la fois poussières et copeaux, avec des risques spécifiques selon les essences et procédés ; le béton ou la pierre peuvent exposer à de la silice cristalline. L’INRS recommande, pour les opérations exposant à la silice, de privilégier le captage à la source et de raccorder les outils aspirants à des systèmes d’aspiration à haute dépression.</p>
<p>Autrement dit, une classe de poussières ne remplace pas une stratégie de captage. Si vous travaillez surtout le plâtre, consultez aussi notre guide <a href="/usages/aspirateur-platre/">aspirateur pour plâtre</a>. Pour le bois, la page <a href="/usages/aspirateur-bois-sciure-copeaux/">bois, sciure et copeaux</a> traite du débit et des raccordements. Pour une sélection commerciale ciblée, notre <a href="/comparatifs/aspirateur-classe-m/">comparatif des aspirateurs classe M</a> regroupe les modèles correspondant à cette catégorie.</p>

<h2 id="hepa">Classe H et filtre HEPA : deux classifications différentes</h2>
<p>HEPA décrit la performance d’un filtre selon une norme de filtration comme EN 1822 ; H13 et H14 sont des classes de filtres mesurées à la taille de particule la plus pénétrante. La classe H d’un aspirateur relève, elle, de la norme de l’appareil complet. Un aspirateur vendu avec un filtre HEPA n’est donc pas automatiquement un aspirateur de classe H.</p>
<p>Cette distinction est cruciale pour les usages à haut risque. Pour l’amiante, l’INRS demande explicitement un aspirateur de classe H selon IEC 60335-2-69 et un filtre à très haute efficacité au minimum H13 ou H14, avec d’autres dispositions de sécurité. Notre guide <a href="/guides/filtre-hepa-aspirateur/">HEPA H13/H14</a> explique ce que le marquage du filtre dit — et ce qu’il ne dit pas — sur l’appareil.</p>

<h2 id="choix">Comment choisir la bonne classe sans surdimensionner</h2>
<p>Pour un chantier banal de collecte de saletés non dangereuses, une classe supérieure n’est pas automatiquement nécessaire. À l’inverse, choisir une classe trop faible pour une poussière réglementée n’est pas compensé par une forte puissance moteur. Le bon choix se fait en reliant la poussière, sa dangerosité, la valeur limite applicable, le mode de captage et le protocole de nettoyage.</p>
<p>Si vous hésitez entre plusieurs appareils, commencez par filtrer le marché sur la classe requise, puis comparez la <a href="/guides/debit-air-aspirateur/">capacité de débit</a>, le <a href="/guides/decolmatage-automatique/">décolmatage</a>, la prise asservie et le coût des consommables. Cela évite de comparer des machines qui ne répondent pas au même besoin de prévention.</p>

<h2 id="entretien">La classe ne vaut que si le vidage et la maintenance restent maîtrisés</h2>
<p>Une machine correctement classée peut perdre une partie de son intérêt si le filtre est endommagé, si les joints fuient ou si le vidage remet la poussière dans l’air. Les sacs de collecte, obturateurs, systèmes de fermeture et procédures de maintenance ne sont donc pas des détails. Pour certaines poussières dangereuses, la maintenance elle-même doit être réalisée avec des précautions spécifiques.</p>
<p>Respectez la notice du fabricant, remplacez les consommables par des références compatibles et évitez les opérations qui dispersent la poussière, comme souffler un filtre contaminé à l’air comprimé. Pour les règles d’entretien courant, consultez notre <a href="/guides/entretien-aspirateur-chantier/">guide d’entretien</a> et notre page <a href="/guides/sac-ou-sans-sac/">sac ou sans sac</a>.</p>
{sources("iec", "festool_classes", "inrs_asbestos", "inrs_silica")}
'''
},

"decolmatage-automatique": {
"answer": "Le décolmatage sert à débarrasser périodiquement le filtre d’une partie des poussières qui l’obstruent afin de limiter la chute de débit. Sur les travaux produisant en continu des poussières fines, comme le ponçage, il peut faire une différence majeure. Les systèmes ne fonctionnent toutefois pas tous de la même manière et ne dispensent ni du bon sac ni de l’entretien du filtre.",
"toc": [("fonctionnement", "Pourquoi le filtre se colmate"), ("technologies", "Comment fonctionne le décolmatage"), ("utile", "Quand il devient vraiment utile"), ("limites", "Ce qu’il ne résout pas"), ("comparaison", "Comment comparer deux systèmes"), ("entretien", "Bonnes pratiques"), ("sources", "Sources")],
"body": f'''
<h2 id="fonctionnement">Pourquoi un filtre colmaté fait chuter l’aspiration</h2>
<p>À mesure que les poussières s’accumulent sur le média filtrant, la résistance au passage de l’air augmente. Le moteur peut continuer à tourner au même régime alors que le débit disponible au flexible diminue. Sur un chantier qui produit peu de poussière, la perte peut être progressive et acceptable. Avec une ponceuse à plâtre ou une rainureuse, le filtre peut en revanche se charger rapidement et dégrader le captage à la source.</p>
<p>Le problème est donc moins « nettoyer le filtre pour le garder propre » que <strong>maintenir une circulation d’air utile pendant le travail</strong>. C’est pourquoi les fabricants mettent en avant des systèmes de nettoyage automatique sur leurs gammes professionnelles ; Bosch indique par exemple que l’AFC de son GAS 35 M vise à maintenir une aspiration puissante et constante.</p>

<h2 id="technologies">Comment fonctionne le décolmatage automatique</h2>
<p>Le terme recouvre plusieurs technologies. Certains appareils utilisent des impulsions ou inversions de flux d’air, d’autres sollicitent mécaniquement le filtre, et les séquences peuvent être continues, périodiques ou déclenchées selon le modèle. Il faut donc éviter de considérer tous les systèmes « auto clean », « AFC » ou équivalents comme identiques.</p>
<p>Le résultat attendu est le même : détacher une partie du gâteau de poussière qui se forme sur le filtre et le faire retomber dans le sac ou la cuve. Un système bien adapté au type de poussière retarde la perte de débit ; il ne rend pas le filtre inusable et ne supprime pas les contrôles prévus par la notice.</p>

<h2 id="utile">Quand le décolmatage devient vraiment utile</h2>
<p>Il prend tout son sens avec les poussières fines produites en continu : ponçage d’enduits, plâtre, certains travaux sur béton ou pierre, ou longues sessions avec un outil raccordé. Dans ces situations, le débit doit rester suffisamment stable pour capter la poussière au point d’émission. Une machine puissante mais rapidement colmatée peut être moins efficace en pratique qu’un extracteur dont les valeurs maximales sont plus modestes mais mieux maintenues.</p>
<p>Pour un usage occasionnel de nettoyage, de copeaux grossiers ou de petits débris, un bon nettoyage manuel ou semi-automatique peut suffire. La page <a href="/usages/aspirateur-ponceuse/">aspirateur pour ponceuse</a> et le guide <a href="/usages/aspirateur-platre/">aspiration du plâtre</a> montrent les cas où la continuité du débit devient prioritaire.</p>

<h2 id="limites">Ce que le décolmatage ne résout pas</h2>
<p>Il ne compense pas une classe de poussières inadaptée, un flexible trop restrictif, une fuite au raccord ou un filtre endommagé. Il ne transforme pas non plus un aspirateur en appareil certifié pour des poussières dangereuses. Le choix de la classe, du filtre, du sac et du mode de collecte reste indépendant de la présence d’un système de nettoyage.</p>
<p>Un décolmatage agressif peut aussi être bruyant ou provoquer de brèves variations de l’aspiration selon la technologie. Pour certains outils ou finitions sensibles, la façon dont le fabricant gère la séquence compte. La documentation technique et les essais comparables sont donc plus utiles qu’un simple oui/non sur une fiche produit.</p>

<h2 id="comparaison">Comment comparer deux systèmes de nettoyage de filtre</h2>
<p>Commencez par vérifier si le nettoyage est réellement automatique, semi-automatique ou manuel. Regardez ensuite si le fabricant indique un usage recommandé avec poussières fines, la classe de poussières de l’appareil et la disponibilité des filtres compatibles. Les données de débit et de dépression doivent être lues avec leur point de mesure ; elles ne permettent pas à elles seules de prédire le comportement après plusieurs minutes de ponçage.</p>
<p>Dans nos fiches, nous distinguons donc la performance maximale de la capacité à la maintenir. Vous pouvez croiser ce critère avec le <a href="/guides/debit-air-aspirateur/">débit d’air</a>, la <a href="/guides/prise-asservie/">prise asservie</a> et la classe de filtration. Le <a href="/modeles/bosch-gas-35-m-afc/">Bosch GAS 35 M AFC</a> illustre un appareil où le nettoyage automatique est une caractéristique structurante plutôt qu’un accessoire.</p>

<h2 id="entretien">Décolmatage automatique ne signifie pas zéro entretien</h2>
<p>Inspectez régulièrement le filtre, les joints, le sac et la cuve selon la notice. Un filtre humide, déchiré ou saturé par un matériau inadapté ne sera pas remis à neuf par le système automatique. N’utilisez pas de méthode de nettoyage non autorisée — lavage, soufflage à l’air comprimé ou brossage agressif — si le fabricant ne la prévoit pas.</p>
<p>Sur des poussières dangereuses, le nettoyage et la maintenance peuvent exposer l’opérateur ; les procédures de confinement et de remplacement sont alors prioritaires. Pour l’entretien courant, notre <a href="/guides/entretien-aspirateur-chantier/">guide de maintenance</a> complète cette page.</p>
{sources("bosch_gas35", "iec", "inrs_silica")}
'''
},

"prise-asservie": {
"answer": "Une prise asservie permet à l’aspirateur de détecter la mise en marche d’un outil filaire branché sur sa prise et de démarrer automatiquement l’aspiration. Elle est très pratique avec une ponceuse, une scie ou une rainureuse, mais la puissance maximale admissible de l’outil dépend du modèle d’aspirateur et doit être vérifiée dans la notice ou sur la plaque signalétique.",
"toc": [("principe", "Comment fonctionne une prise asservie"), ("usage", "Pourquoi c’est utile avec un outil"), ("puissance", "Puissance maximale et sécurité"), ("sansfil", "Et avec les outils sans fil ?"), ("raccord", "Le raccordement compte autant que la prise"), ("choix", "Quand en faire un critère d’achat"), ("sources", "Sources")],
"body": f'''
<h2 id="principe">Comment fonctionne une prise asservie</h2>
<p>La prise intégrée à l’aspirateur alimente un outil électroportatif et surveille sa consommation. Lorsque l’outil démarre, l’électronique déclenche le moteur d’aspiration ; lorsque l’outil s’arrête, de nombreux appareils maintiennent brièvement l’aspiration pour évacuer les poussières restantes dans le flexible. Le comportement exact et la temporisation varient selon la machine.</p>
<p>L’intérêt principal est d’automatiser le captage : l’utilisateur ne doit plus penser à allumer puis éteindre l’aspirateur à chaque coupe ou passe de ponçage. Sur une journée de travail, ce détail réduit les moments où l’outil fonctionne sans aspiration.</p>

<h2 id="usage">Pourquoi c’est particulièrement utile avec une ponceuse ou une scie</h2>
<p>Avec une <a href="/usages/aspirateur-ponceuse/">ponceuse</a>, le flux de poussières commence dès que l’abrasif travaille ; l’aspiration synchronisée évite un démarrage tardif. Avec une <a href="/usages/aspirateur-scie/">scie</a>, elle simplifie les séries de coupes et garde le tuyau en dépression pendant l’opération. C’est surtout un gain de régularité et d’ergonomie, pas une augmentation intrinsèque de la puissance d’aspiration.</p>
<p>La prise n’a toutefois d’intérêt que si l’outil peut être raccordé correctement. Un capot mal conçu ou un adaptateur qui laisse entrer beaucoup d’air parasite limite la collecte, même avec une synchronisation parfaite. Le système doit être pensé comme un ensemble : outil, capot, raccord, flexible, aspirateur et filtre.</p>

<h2 id="puissance">Puissance maximale : ne retenez pas une valeur « standard »</h2>
<p>La puissance admissible sur la prise varie selon le modèle, la tension, le pays et la puissance que l’aspirateur consomme lui-même. Il est donc risqué d’appliquer une règle générale du type « toutes les prises asservies acceptent 2 000 ou 2 200 W ». La valeur à respecter est celle indiquée par le fabricant pour la référence exacte de votre appareil.</p>
<p>Un outil dont l’appel de courant est élevé peut dépasser ce que le circuit de l’aspirateur accepte. Vérifiez la notice, la plaque signalétique et les protections électriques du chantier. N’utilisez pas une multiprise pour contourner la limite. La prise asservie est un dispositif de commande pratique, pas un moyen d’augmenter la capacité du réseau électrique.</p>

<h2 id="sansfil">Que faire avec un outil sans fil ?</h2>
<p>Un outil sur batterie ne tire évidemment aucun courant depuis la prise de l’aspirateur, donc le déclenchement classique par détection de consommation ne fonctionne pas. Certaines marques proposent une télécommande sur le flexible, une liaison Bluetooth ou un autre système radio. Ces solutions peuvent reproduire le confort du démarrage synchronisé, mais leur compatibilité dépend souvent de l’écosystème de la marque.</p>
<p>Si vous travaillez avec plusieurs plateformes de batteries, une commande manuelle déportée peut être plus universelle qu’une intégration propriétaire. Pour comparer les machines mobiles, consultez aussi notre <a href="/comparatifs/aspirateur-chantier-sans-fil/">comparatif des aspirateurs sans fil</a>.</p>

<h2 id="raccord">Le raccordement pneumatique compte autant que la prise électrique</h2>
<p>Une prise asservie peut déclencher l’aspirateur au bon moment, mais elle ne corrige pas une mauvaise étanchéité. Vérifiez le diamètre de sortie de l’outil, la forme du manchon et la liberté de mouvement du flexible. Un adaptateur conique universel peut dépanner, tandis qu’un raccord dédié offre souvent une meilleure tenue mécanique.</p>
<p>Le diamètre du tuyau influence aussi la vitesse d’air et les pertes de charge. Réduire fortement un flexible pour l’adapter à un petit embout peut modifier le fonctionnement du système. Notre page sur les <a href="/accessoires/adaptateur-outil-electroportatif/">adaptateurs pour outils électroportatifs</a> détaille ces points.</p>

<h2 id="choix">Quand faire de la prise asservie un critère d’achat</h2>
<p>Si l’aspirateur sert principalement au nettoyage du sol ou à l’aspiration d’eau, la prise est secondaire. Si vous poncez, sciez ou rainurez régulièrement avec un outil filaire, elle devient un vrai critère de confort et de discipline de captage. Associez-la alors au <a href="/guides/decolmatage-automatique/">décolmatage automatique</a> et à une classe de poussières adaptée.</p>
<p>Pour une décision d’achat, notez la puissance admissible, le comportement après arrêt, la position physique de la prise et la compatibilité des raccords. Ce sont des données plus utiles qu’un simple badge « prise outil » dans une fiche comparative.</p>
{sources("bosch_gas35", "iec", "inrs_wood")}
'''
},

"puissance-aspiration": {
"answer": "Les watts du moteur ne mesurent pas directement la puissance d’aspiration. Pour comparer des aspirateurs de chantier, regardez plutôt la dépression, le débit d’air, la façon dont ces valeurs sont mesurées et la capacité de l’appareil à les maintenir avec un filtre chargé. Deux machines de même puissance électrique peuvent fournir des performances très différentes au bout du flexible.",
"toc": [("watts", "Ce que signifient les watts"), ("depression", "La dépression"), ("debit", "Le débit d’air"), ("ensemble", "Pourquoi il faut lire les valeurs ensemble"), ("mesure", "Comparer des fiches techniques"), ("usage", "Quelle performance selon l’usage"), ("sources", "Sources")],
"body": f'''
<h2 id="watts">Les watts indiquent d’abord la puissance électrique absorbée</h2>
<p>Sur une fiche produit, la valeur en watts correspond généralement à la puissance absorbée par l’appareil ou à une donnée de la turbine. Elle renseigne sur l’énergie consommée, mais pas directement sur le débit disponible à l’outil. Le rendement du moteur, la turbine, le chemin de l’air, le filtre, le flexible et les pertes de charge déterminent ce qui reste réellement exploitable.</p>
<p>C’est pourquoi un classement fondé uniquement sur « 1 200 W contre 1 600 W » est peu pertinent. Bosch, par exemple, publie pour le GAS 35 M AFC à la fois la puissance absorbée, le débit maximal à la turbine et la dépression maximale : ce sont des grandeurs différentes et elles doivent être interprétées comme telles.</p>

<h2 id="depression">La dépression : utile pour vaincre la résistance et soulever des déchets</h2>
<p>La <a href="/guides/depression-kpa-mbar-air-watt/">dépression</a> est la différence de pression que l’aspirateur peut créer. Elle est exprimée en pascals, kPa ou mbar. Une forte dépression aide lorsqu’il faut maintenir l’aspiration à travers un circuit résistant ou déplacer des éléments plus lourds. Mais une valeur maximale est souvent obtenue dans une condition de débit très faible : elle ne décrit pas toute la courbe de fonctionnement.</p>
<p>Sur chantier, la dépression devient particulièrement importante avec des flexibles longs, des petits diamètres ou des outils qui imposent des pertes de charge. Elle doit néanmoins être lue avec le débit d’air, car un aspirateur qui « tire fort » mais déplace peu d’air peut être moins bon pour capter un nuage de poussière.</p>

<h2 id="debit">Le débit d’air : central pour le captage à la source</h2>
<p>Le <a href="/guides/debit-air-aspirateur/">débit d’air</a> exprime le volume d’air déplacé, souvent en litres par seconde ou mètres cubes par heure. Il intervient directement dans la capacité à entraîner des particules dans un capot de ponceuse, une buse de scie ou un flexible. L’INRS insiste sur le captage à la source et l’aspiration haute dépression pour plusieurs situations de poussières professionnelles.</p>
<p>Le débit annoncé peut toutefois être mesuré à la turbine, sans flexible ni filtre chargé. Au poste de travail, les pertes de charge et le colmatage réduisent la valeur disponible. La présence d’un <a href="/guides/decolmatage-automatique/">décolmatage automatique</a> peut donc compter davantage qu’un petit écart de débit maximal sur la fiche.</p>

<h2 id="ensemble">Débit et dépression décrivent ensemble le point de fonctionnement</h2>
<p>Un système d’aspiration fonctionne toujours à un compromis entre débit et dépression. À circuit ouvert, le débit peut être élevé ; quand la résistance augmente, le débit diminue et la dépression change. Les « Air Watts » cherchent à combiner pression et débit en une mesure de puissance aéraulique, mais cette donnée est loin d’être publiée de façon homogène sur les aspirateurs de chantier européens.</p>
<p>Pour comparer proprement deux modèles, il vaut donc mieux disposer de valeurs de débit et de dépression mesurées selon des conditions comparables que d’un score composite opaque. Si le fabricant publie une courbe complète ou une valeur au raccord d’aspiration, c’est encore plus instructif.</p>

<h2 id="mesure">Comment lire une fiche technique sans comparer des pommes et des poires</h2>
<p>Repérez les mentions « turbine », « moteur », « raccord », « flexible » ou « appareil ». Un débit de 74 L/s à la turbine n’est pas directement comparable à une valeur mesurée au bout d’un tuyau avec accessoires. Faites aussi attention aux variantes de tension : une même référence peut afficher des caractéristiques légèrement différentes selon le marché.</p>
<p>Notre méthode consiste à conserver le point de mesure avec la valeur et à éviter de combler une donnée absente par une estimation. Dans le <a href="/comparatifs/aspirateur-chantier-puissant/">comparatif des aspirateurs puissants</a>, un modèle n’est donc pas valorisé uniquement parce que son moteur consomme davantage.</p>

<h2 id="usage">Quelle « puissance » faut-il selon l’usage ?</h2>
<p>Pour des copeaux et poussières légères, le débit et la qualité du captage sont souvent prioritaires. Pour des débris plus lourds, une bonne dépression et un flexible robuste gagnent en importance. Pour le ponçage fin, la capacité à maintenir le débit avec un filtre chargé, la classe de poussières et le décolmatage sont déterminants.</p>
<p>Au lieu de chercher une valeur universelle, partez de votre tâche puis éliminez les appareils mal adaptés. Vous pouvez utiliser notre <a href="/guides/comment-choisir-aspirateur-de-chantier/">guide de choix général</a> pour transformer ces métriques en critères concrets.</p>
{sources("bosch_gas35", "iec", "inrs_silica")}
'''
},

"depression-kpa-mbar-air-watt": {
"answer": "La dépression d’un aspirateur peut être exprimée en kPa, mbar, Pa ou parfois en mmH₂O. La conversion de base est simple : 1 kPa = 10 mbar et correspond à environ 102 mmH₂O. Les Air Watts combinent pression et débit, mais ils sont rarement publiés de manière homogène sur les aspirateurs de chantier ; pour comparer deux modèles, privilégiez des mesures réalisées au même point et dans les mêmes conditions.",
"toc": [("definition", "Ce que mesure la dépression"), ("conversion", "Convertir kPa, mbar et mmH₂O"), ("airwatts", "Comprendre les Air Watts"), ("debit", "Dépression et débit ne s’opposent pas"), ("fiches", "Lire les fiches fabricants"), ("usage", "Quelle métrique selon le chantier"), ("sources", "Sources")],
"body": f'''
<h2 id="definition">Ce que mesure la dépression d’un aspirateur</h2>
<p>La dépression est une différence de pression entre l’intérieur du circuit d’aspiration et l’air ambiant. Plus l’aspirateur peut créer une dépression importante, plus il peut vaincre certaines résistances du circuit et maintenir une force d’aspiration lorsque l’ouverture se réduit. Elle ne signifie pas pour autant que le débit d’air est élevé dans toutes les situations.</p>
<p>Les fabricants parlent parfois de « pression d’aspiration », « vacuum pressure » ou « dépression maximale ». Le mot maximal est important : cette valeur correspond à un point particulier de fonctionnement et ne décrit pas automatiquement la performance avec un flexible, un outil et un filtre chargé.</p>

<h2 id="conversion">Convertir kPa, mbar et mmH₂O</h2>
<p>Le pascal est l’unité SI de pression. Un kilopascal vaut 1 000 Pa et <strong>1 kPa = 10 mbar</strong>. Ainsi, un appareil annoncé à 25,4 kPa correspond à 254 mbar. Pour la colonne d’eau, 1 kPa équivaut approximativement à 101,97 mmH₂O ; arrondir à 102 mmH₂O suffit pour une lecture de fiche technique.</p>
<p>Ces conversions permettent de remettre deux fiches dans la même unité. Elles ne rendent pas comparables des mesures effectuées à des endroits différents. Un chiffre à la turbine peut rester supérieur à une mesure au flexible, même après conversion parfaite.</p>

<h2 id="airwatts">Que sont les Air Watts ?</h2>
<p>Les Air Watts cherchent à représenter une puissance aéraulique en combinant pression et débit. En unités SI, une pression en pascals multipliée par un débit volumique en m³/s donne une puissance en watts. Dans l’industrie de l’aspiration domestique, des formules pratiques utilisent d’autres unités et coefficients de conversion.</p>
<p>Le concept est intéressant parce qu’il rappelle qu’une bonne aspiration nécessite à la fois du débit et de la dépression. Mais l’Air Watt n’est pas systématiquement publié sur les extracteurs de chantier et les méthodes commerciales peuvent différer. Une valeur isolée sans conditions de mesure ne doit donc pas devenir votre seul critère.</p>

<h2 id="debit">Dépression et débit d’air : deux faces du même système</h2>
<p>Quand le circuit est très ouvert, le moteur peut déplacer beaucoup d’air avec une dépression modérée. Quand l’ouverture est fortement restreinte, la dépression augmente et le débit chute. Le point réellement utilisé avec une ponceuse ou une scie se situe quelque part entre ces extrêmes, selon le diamètre du tuyau, le capot et le filtre.</p>
<p>Pour cette raison, notre guide sur le <a href="/guides/debit-air-aspirateur/">débit d’air</a> doit être lu avec celui-ci. Le guide sur la <a href="/guides/puissance-aspiration/">puissance moteur</a> explique aussi pourquoi une consommation électrique élevée n’est pas un substitut à ces deux mesures.</p>

<h2 id="fiches">Comment comparer les chiffres des fabricants</h2>
<p>Conservez toujours l’unité et le point de mesure. Bosch indique par exemple pour certaines variantes du GAS 35 M AFC une dépression maximale de 254 mbar à la turbine avec un débit maximal également mesuré à la turbine. Ces données sont utiles pour comparer au sein d’une gamme documentée de manière cohérente.</p>
<p>Si une marque donne 27 kPa au raccord et une autre 27 kPa à la turbine, il faut résister à la tentation de les classer ex aequo. Cherchez la notice, la fiche technique détaillée ou une mesure indépendante réalisée selon le même protocole. Dans nos <a href="/comparatifs/meilleur-aspirateur-de-chantier/">comparatifs</a>, une donnée non comparable est signalée plutôt que normalisée artificiellement.</p>

<h2 id="usage">Quelle métrique regarder selon le chantier ?</h2>
<p>Pour aspirer des débris lourds ou travailler à travers un circuit très résistant, la dépression prend davantage de poids. Pour capter des poussières et copeaux au point d’émission, le débit et le dessin du capot sont centraux. Pour le ponçage fin, ajoutez la capacité à maintenir ces performances lorsque le filtre se charge.</p>
<p>La bonne décision n’est donc pas « kPa ou L/s », mais une combinaison cohérente avec l’usage, la classe de poussières et le système de filtration. Consultez le <a href="/guides/comment-choisir-aspirateur-de-chantier/">guide de choix</a> pour replacer ces unités dans l’ensemble des critères.</p>
{sources("bosch_gas35", "iec", "inrs_wood")}
'''
},

"debit-air-aspirateur": {
"answer": "Le débit d’air indique le volume d’air déplacé par l’aspirateur. Il est généralement exprimé en L/s ou en m³/h, avec la conversion 1 L/s = 3,6 m³/h. Pour le captage de poussières à la source, c’est une donnée essentielle, mais il faut vérifier où elle est mesurée et comment elle évolue avec le flexible, l’outil et le colmatage du filtre.",
"toc": [("definition", "Ce que mesure le débit"), ("unites", "L/s et m³/h"), ("captage", "Pourquoi le débit compte au captage"), ("mesure", "Débit turbine et débit réel"), ("colmatage", "Effet du filtre et du décolmatage"), ("choix", "Comment utiliser ce chiffre pour choisir"), ("sources", "Sources")],
"body": f'''
<h2 id="definition">Ce que mesure le débit d’air</h2>
<p>Le débit volumique correspond à la quantité d’air qui traverse le circuit pendant un temps donné. Dans un aspirateur de chantier, ce flux entraîne les poussières, copeaux et particules depuis le point de captage jusqu’au sac ou à la cuve. Il ne mesure pas directement la force nécessaire pour vaincre une restriction : ce rôle est davantage décrit par la dépression.</p>
<p>Pour les outils qui génèrent un nuage continu de poussière, le débit disponible au capot est crucial. Un captage efficace vise à créer un mouvement d’air suffisant là où les particules sont produites, avant qu’elles se dispersent dans la zone de travail.</p>

<h2 id="unites">Passer de L/s à m³/h sans se tromper</h2>
<p>Les deux unités sont courantes. La conversion est exacte : <strong>1 L/s = 3,6 m³/h</strong>. Un débit de 50 L/s correspond donc à 180 m³/h. Cette conversion est utile lorsqu’un fabricant publie en litres par seconde et un autre en mètres cubes par heure.</p>
<p>Comme pour la dépression, convertir l’unité ne suffit pas à rendre deux chiffres comparables. La fiche doit préciser si la mesure est prise à la turbine, au raccord de l’appareil ou avec un flexible et des accessoires.</p>

<h2 id="captage">Pourquoi le débit compte autant pour le captage à la source</h2>
<p>L’INRS recommande le captage des poussières au plus près de leur émission pour plusieurs activités, notamment le bois et la silice cristalline. Avec une ponceuse ou une scie, le débit disponible doit traverser le capot et le raccord à un niveau suffisant pour entraîner les particules vers le flexible. Un moteur puissant ne garantit pas ce résultat si le circuit est mal conçu.</p>
<p>Le besoin dépend aussi du diamètre et de la géométrie du système. Une machine à bois qui produit des copeaux volumineux n’a pas les mêmes contraintes qu’une petite ponceuse. Consultez nos pages <a href="/usages/aspirateur-bois-sciure-copeaux/">bois et sciure</a> et <a href="/usages/aspirateur-ponceuse/">ponceuse</a> pour raisonner par usage plutôt que par seuil universel.</p>

<h2 id="mesure">Débit à la turbine, au raccord ou au bout du flexible</h2>
<p>La valeur maximale à la turbine est une caractéristique du groupe d’aspiration. Une fois l’air passé dans les conduits, le filtre, le flexible et les accessoires, le débit disponible peut être inférieur. Un tuyau long, un petit diamètre, un coude serré ou un adaptateur mal dimensionné ajoute des pertes de charge.</p>
<p>Lors d’une comparaison, conservez la mention du point de mesure. Bosch publie par exemple le débit maximal de turbine de certains modèles professionnels. Il serait incorrect de mettre ce chiffre directement en concurrence avec une valeur mesurée à l’extrémité d’un flexible par un autre fabricant.</p>

<h2 id="colmatage">Le filtre chargé fait évoluer le débit pendant le chantier</h2>
<p>Les poussières fines forment progressivement une couche sur le média filtrant. Cette couche augmente la résistance à l’air et peut réduire le débit. C’est la raison pour laquelle les systèmes de <a href="/guides/decolmatage-automatique/">décolmatage automatique</a> sont particulièrement intéressants dans les usages continus et poussiéreux.</p>
<p>Le sac influence aussi le circuit. Un sac adapté répartit parfois mieux la poussière et facilite le vidage, tandis qu’un consommable saturé peut étrangler le flux. La page <a href="/guides/sac-ou-sans-sac/">sac ou sans sac</a> explique le compromis entre filtration, coût et entretien.</p>

<h2 id="choix">Comment utiliser le débit pour choisir un aspirateur</h2>
<p>Ne cherchez pas un seuil magique valable pour tous les outils. Commencez par les recommandations de l’outil et de l’aspirateur, vérifiez la compatibilité du raccord et assurez-vous que la classe de poussières est adaptée. Comparez ensuite le débit dans des conditions documentées similaires et regardez comment l’appareil gère le colmatage.</p>
<p>Enfin, lisez le débit avec la <a href="/guides/depression-kpa-mbar-air-watt/">dépression</a>. Un système performant combine les deux au point de fonctionnement utile. Le <a href="/guides/comment-choisir-aspirateur-de-chantier/">guide de choix complet</a> vous aide à pondérer ces données avec la cuve, la prise asservie et la filtration.</p>
{sources("bosch_gas35", "inrs_wood", "inrs_silica")}
'''
},

"capacite-cuve": {
"answer": "La capacité de cuve ne dit rien sur la puissance d’aspiration et la capacité brute annoncée n’est pas toujours le volume réellement disponible. Le filtre, le sac et le dispositif d’arrêt pour les liquides réduisent souvent le volume utile. Choisissez donc la cuve selon la fréquence de vidage, le type de déchets et la mobilité souhaitée, plutôt qu’en visant systématiquement le plus grand nombre de litres.",
"toc": [("brutnet", "Capacité brute et volume utile"), ("mobilite", "Grande cuve ou appareil compact"), ("dechets", "Adapter la cuve au déchet"), ("eau", "Cas de l’aspiration de liquides"), ("sac", "Impact du sac et du filtre"), ("choix", "Méthode simple pour dimensionner"), ("sources", "Sources")],
"body": f'''
<h2 id="brutnet">Capacité brute, capacité nette : pourquoi les chiffres diffèrent</h2>
<p>Le volume inscrit dans le nom commercial ou la fiche marketing correspond souvent à la capacité brute du récipient. La capacité nette disponible pour la poussière peut être nettement inférieure, car le filtre, le sac, les éléments internes et les marges de fonctionnement occupent de la place. Pour les liquides, le niveau d’arrêt se situe généralement encore plus bas.</p>
<p>Le Bosch GAS 35 M AFC illustre bien cette différence : Bosch indique une cuve brute de 35 L, une contenance nette de 23 L et un volume net à eau de 19,2 L pour la variante française consultée. Ces chiffres montrent pourquoi « 35 litres » ne doit pas être interprété comme 35 litres de déchets utilisables.</p>

<h2 id="mobilite">Grande cuve ou appareil compact : le vrai compromis</h2>
<p>Une grande cuve espace les vidages, ce qui est appréciable en atelier ou sur un chantier stable. En contrepartie, le corps de l’appareil est plus encombrant, prend davantage de place dans un véhicule et devient lourd à déplacer une fois rempli. Pour travailler dans des escaliers, des logements occupés ou des espaces étroits, un format plus compact peut gagner du temps au quotidien.</p>
<p>La taille doit donc être comparée avec les roues, la poignée, le rangement du flexible et la masse de l’appareil. Le guide <a href="/comparatifs/petit-aspirateur-de-chantier/">petits aspirateurs de chantier</a> s’adresse aux usages où la mobilité prime sur l’autonomie de collecte.</p>

<h2 id="dechets">Adapter la cuve au type de déchets</h2>
<p>Les copeaux et déchets volumineux remplissent rapidement un récipient sans être très lourds ; une cuve plus grande peut être confortable. Les poussières fines sont plus denses et peuvent nécessiter un sac de collecte, ce qui change le volume réellement disponible. Les gravats lourds posent un autre problème : une cuve géante peut devenir difficile ou risquée à soulever lorsqu’elle est chargée.</p>
<p>Pour le nettoyage de <a href="/usages/aspirateur-gravats/">gravats</a>, privilégiez donc aussi la robustesse et la facilité de vidage. Pour l’<a href="/usages/aspirateur-atelier/">atelier</a>, la capacité peut être plus généreuse si l’appareil reste généralement au même endroit.</p>

<h2 id="eau">Aspiration d’eau : le volume utile est spécifique</h2>
<p>Un aspirateur eau et poussière dispose d’un système de limitation ou d’arrêt lorsque le niveau de liquide atteint une certaine hauteur. Le volume d’eau admissible doit être lu dans la documentation, et il peut être nettement inférieur au volume brut de la cuve. Le filtre ou le sac doivent parfois être retirés ou remplacés selon le mode humide : suivez impérativement la notice.</p>
<p>Ne remplissez pas la cuve jusqu’au bord sous prétexte que sa capacité brute le permet. Le fonctionnement du flotteur, des électrodes ou du dispositif de coupure doit rester libre. Notre <a href="/comparatifs/aspirateur-eau-poussiere/">comparatif eau et poussière</a> prend cette distinction en compte.</p>

<h2 id="sac">Le sac, le filtre et le décolmatage réduisent mais sécurisent le volume</h2>
<p>Un sac filtrant occupe une partie de la cuve et ne doit pas toujours être rempli à son volume géométrique maximal. Mais il facilite la collecte des poussières fines et limite la remise en suspension au vidage. Le filtre principal et son mécanisme de décolmatage occupent eux aussi de l’espace.</p>
<p>Il serait donc contre-productif de retirer un élément prévu par le fabricant uniquement pour gagner quelques litres. Le guide <a href="/guides/sac-ou-sans-sac/">sac ou sans sac</a> explique quand le consommable apporte une vraie valeur de filtration et de propreté.</p>

<h2 id="choix">Une méthode simple pour dimensionner la cuve</h2>
<p>Estimez d’abord la quantité de déchets produite entre deux moments où vous pouvez raisonnablement vider l’appareil. Ajoutez le poids que vous êtes prêt à déplacer, puis vérifiez la capacité nette et non seulement brute. Pour un outil raccordé en continu, la classe de poussières et le débit restent prioritaires sur la taille de la cuve.</p>
<p>Enfin, comparez les consommables et la logistique. Une cuve légèrement plus petite avec des sacs facilement disponibles peut être plus pratique qu’un grand modèle dont les sacs sont rares. Pour une décision globale, revenez au <a href="/guides/comment-choisir-aspirateur-de-chantier/">guide de choix</a>.</p>
{sources("bosch_gas35", "iec", "inrs_wood")}
'''
},

"filtre-hepa-aspirateur": {
"answer": "H13 et H14 sont des classes de filtres HEPA selon EN 1822, avec une efficacité intégrale minimale respectivement de 99,95 % et 99,995 % à la taille de particule la plus pénétrante. Cela ne signifie pas qu’un aspirateur équipé d’un filtre H13 est automatiquement un aspirateur de classe H. Pour les poussières dangereuses, il faut considérer la certification de l’appareil complet et les exigences de l’activité.",
"toc": [("hepa", "Ce que signifie HEPA"), ("h13h14", "Différence entre H13 et H14"), ("classeh", "HEPA et classe H : différence"), ("chantier", "Quand un HEPA est utile"), ("amiante", "Cas particulier de l’amiante"), ("entretien", "Entretien et remplacement"), ("sources", "Sources")],
"body": f'''
<h2 id="hepa">Ce que signifie réellement HEPA</h2>
<p>HEPA signifie High Efficiency Particulate Air. En Europe, la classification EN 1822 distingue les filtres EPA, HEPA et ULPA et mesure leur performance autour de la MPPS, la taille de particule la plus pénétrante pour le média. Ce point est important : la référence correcte n’est pas simplement « toutes les particules de 0,3 µm ».</p>
<p>Un filtre HEPA peut améliorer fortement la rétention des particules fines, mais son efficacité nominale ne décrit pas à elle seule les fuites potentielles autour du filtre, l’étanchéité de la cuve ou la sécurité du mode de vidage. C’est pourquoi la performance du filtre et la classe de poussières de l’aspirateur doivent être lues séparément.</p>

<h2 id="h13h14">H13 et H14 : une différence faible en pourcentage, forte en pénétration</h2>
<p>Selon les valeurs de classification EN 1822 reprises par les fabricants de filtration, un H13 atteint au moins 99,95 % d’efficacité intégrale à la MPPS, tandis qu’un H14 atteint au moins 99,995 %. La différence paraît n’être que de 0,045 point de pourcentage, mais la pénétration maximale passe de 0,05 % à 0,005 %, soit dix fois moins.</p>
<p>Un H14 impose donc un niveau de filtration supérieur, avec potentiellement davantage de perte de charge selon la conception. Il n’est pas automatiquement préférable pour chaque aspirateur : le moteur, la surface filtrante et le système complet doivent être conçus pour fonctionner ensemble.</p>

<h2 id="classeh">Pourquoi un filtre H13 n’est pas synonyme d’aspirateur classe H</h2>
<p>La classe H d’un extracteur relève de la norme EN/IEC 60335-2-69 et concerne l’appareil prévu pour certaines poussières hautement dangereuses. La classe H13/H14 relève de la norme de filtre EN 1822. Les deux lettres H désignent donc des choses différentes.</p>
<p>Un appareil grand public peut être vendu avec un média présenté comme HEPA sans répondre aux exigences d’un extracteur classe H. Si votre activité exige une classe de poussières, vérifiez la certification de l’appareil, pas seulement le type de cartouche. Notre <a href="/guides/classes-l-m-h/">guide L/M/H</a> détaille cette distinction.</p>

<h2 id="chantier">Quand un filtre HEPA apporte une valeur sur chantier</h2>
<p>Pour les poussières fines, un filtre à haute efficacité limite les rejets, à condition que le reste du circuit soit étanche et correctement entretenu. Il peut être pertinent dans des environnements sensibles ou lorsque le fabricant l’intègre à un système conçu pour cette performance. Mais pour une aspiration de copeaux grossiers, un HEPA très restrictif n’est pas nécessairement le premier critère de choix.</p>
<p>Pour le plâtre ou le bois, regardez d’abord la classe de poussières requise, la qualité du captage, le <a href="/guides/debit-air-aspirateur/">débit</a> et la gestion du colmatage. Le meilleur filtre théorique ne compense pas un flexible mal raccordé ou une aspiration qui s’effondre après quelques minutes.</p>

<h2 id="amiante">Amiante : l’exemple qui montre pourquoi le système complet compte</h2>
<p>L’INRS précise que les aspirateurs utilisés pour des travaux sur matériaux contenant de l’amiante doivent être de classe H selon IEC 60335-2-69 et comporter des filtres à très haute efficacité, au minimum H13 ou H14 selon NF EN 1822-1, ainsi que d’autres équipements spécifiques. Cette exigence associe explicitement la classe de l’aspirateur et celle du filtre.</p>
<p>Un aspirateur de bricolage marqué HEPA ne doit donc jamais être considéré comme une alternative improvisée pour l’amiante. Les procédures de confinement, de décontamination et de gestion des déchets font partie du dispositif de prévention et nécessitent des compétences adaptées.</p>

<h2 id="entretien">Un filtre performant doit rester intact et correctement monté</h2>
<p>Respectez le sens de montage, les joints et la référence prévue par le fabricant. Un filtre déchiré, mal assis ou encore humide après un lavage non prévu peut dégrader fortement le système. N’aspirez pas un matériau incompatible avec le média filtrant et remplacez le filtre selon les critères de la notice, pas uniquement lorsqu’il semble sale.</p>
<p>Pour les poussières dangereuses, la dépose du filtre peut exposer l’opérateur ; suivez les procédures spécifiques. Pour l’entretien général et le stockage, consultez notre <a href="/guides/entretien-aspirateur-chantier/">guide d’entretien</a> et notre page sur les <a href="/accessoires/filtres-aspirateur-chantier/">filtres de remplacement</a>.</p>
{sources("hepa", "iec", "inrs_asbestos", "festool_classes")}
'''
},

"sac-ou-sans-sac": {
"answer": "Sur un aspirateur de chantier, le sac n’est pas seulement un consommable : il peut faciliter la collecte des poussières fines et surtout réduire leur remise en suspension au vidage. L’utilisation sans sac est pratique pour certains déchets grossiers ou liquides, mais elle expose davantage le filtre principal et demande un vidage plus salissant. Pour les poussières dangereuses, suivez la configuration de collecte imposée par l’appareil et la réglementation.",
"toc": [("role", "À quoi sert le sac"), ("sanssac", "Quand le sans-sac est pratique"), ("fines", "Poussières fines et colmatage"), ("classes", "Classes M/H et collecte"), ("cout", "Coût réel des consommables"), ("choix", "Comment choisir"), ("sources", "Sources")],
"body": f'''
<h2 id="role">Le sac protège le filtre et simplifie surtout le vidage</h2>
<p>Dans un aspirateur de chantier, le sac collecte les poussières avant qu’elles se répandent dans la cuve. Selon sa matière, il peut aussi jouer un rôle de préfiltration. Le filtre principal reçoit alors moins de charge et peut conserver plus longtemps un passage d’air correct. L’avantage le plus visible reste le vidage : un sac fermé limite le nuage de poussière qui apparaît lorsqu’on retourne une cuve à sec.</p>
<p>Il existe cependant plusieurs types de sacs : papier, non-tissé, sacs filtrants ou sacs de collecte conçus pour fonctionner avec des classes de poussières spécifiques. Il faut utiliser une référence autorisée par le fabricant, surtout lorsque la sécurité dépend du système de collecte.</p>

<h2 id="sanssac">Quand l’utilisation sans sac est pratique</h2>
<p>Pour des déchets grossiers, des copeaux ou certaines opérations de nettoyage, l’aspiration directe dans la cuve évite le coût d’un consommable et permet de vider rapidement. En aspiration de liquides, la notice peut imposer le retrait du sac filtrant ; le mode de configuration varie selon le modèle.</p>
<p>Le revers est que toute la poussière arrive dans le récipient et sur le filtre principal. Le vidage devient plus salissant et les poussières fines peuvent se remettre en suspension. Un appareil « sans sac » n’est donc pas automatiquement plus économique si les filtres s’usent plus vite ou demandent davantage de nettoyage.</p>

<h2 id="fines">Poussières fines : le sac aide à maîtriser le colmatage</h2>
<p>Le plâtre, les enduits et certaines poussières minérales forment une couche dense sur les filtres. Un sac adapté peut retenir une partie de cette charge avant le filtre principal. Combiné à un <a href="/guides/decolmatage-automatique/">décolmatage automatique</a>, il contribue à stabiliser le fonctionnement pendant les travaux prolongés.</p>
<p>Ce bénéfice dépend de la conception du sac et de l’appareil. Un sac trop plein ou incompatible peut au contraire réduire le débit. Surveillez donc les indicateurs de remplissage et les consignes du fabricant plutôt que de chercher à utiliser chaque litre disponible.</p>

<h2 id="classes">Classes M et H : le mode de collecte fait partie de la sécurité</h2>
<p>Avec des poussières dangereuses, le sujet n’est plus seulement le confort. Les exigences de l’appareil peuvent prévoir des sacs ou dispositifs de collecte permettant de retirer les déchets avec un minimum de dispersion. Pour l’amiante, l’INRS décrit notamment des exigences spécifiques de double sac et de fermeture.</p>
<p>Ne retirez pas un sac prévu par la configuration certifiée sous prétexte de gagner du volume ou de réduire le coût. La <a href="/guides/classes-l-m-h/">classe de poussières</a> concerne le système complet, et le vidage est l’un des moments où l’exposition peut être la plus importante.</p>

<h2 id="cout">Le vrai coût : sacs, filtres, temps de nettoyage et propreté</h2>
<p>Comparer uniquement le prix d’un paquet de sacs donne une image incomplète. Il faut intégrer la durée de vie du filtre, le temps passé à nettoyer la cuve, le risque de colmatage et la disponibilité des consommables. Pour un professionnel, quelques minutes de maintenance répétées peuvent peser davantage que le coût d’un sac.</p>
<p>Avant l’achat, vérifiez le prix et la disponibilité des <a href="/accessoires/sacs-aspirateur-chantier/">sacs compatibles</a> et des <a href="/accessoires/filtres-aspirateur-chantier/">filtres</a>. Un appareil peu cher avec des consommables rares ou coûteux peut devenir moins intéressant sur plusieurs années.</p>

<h2 id="choix">Sac ou sans sac : une décision par type de chantier</h2>
<p>Pour les poussières fines et les travaux où la propreté du vidage compte, le sac est souvent le choix le plus pratique. Pour des déchets grossiers ou un usage eau/poussière compatible, le sans-sac peut être pertinent. Pour une poussière dangereuse, la notice, la classe de l’appareil et la procédure de collecte dictent la configuration.</p>
<p>Si vous hésitez, partez de la nature du déchet et de votre fréquence de vidage, puis regardez la <a href="/guides/capacite-cuve/">capacité utile de la cuve</a> et l’<a href="/guides/entretien-aspirateur-chantier/">entretien</a>. C’est plus fiable qu’un choix de principe « toujours avec » ou « toujours sans » sac.</p>
{sources("iec", "inrs_asbestos", "bosch_gas35")}
'''
},

"entretien-aspirateur-chantier": {
"answer": "Un aspirateur de chantier dure plus longtemps si l’on évite de faire travailler le moteur avec un filtre colmaté, un flexible bouché ou des joints fuyards. Après usage, videz ou remplacez le collecteur selon la notice, contrôlez le filtre, laissez sécher les éléments ayant aspiré de l’humidité et inspectez régulièrement flexible, raccords et système d’arrêt de liquide. Les poussières dangereuses exigent des procédures de maintenance spécifiques.",
"toc": [("apres", "Après chaque chantier"), ("filtre", "Entretenir le filtre"), ("cuve", "Cuve et aspiration d’eau"), ("tuyau", "Flexible et raccords"), ("moteur", "Protéger le moteur"), ("dangereux", "Poussières dangereuses"), ("sources", "Sources")],
"body": f'''
<h2 id="apres">Après chaque chantier : cinq minutes qui évitent beaucoup de pannes</h2>
<p>Débranchez l’appareil avant toute intervention. Vérifiez le niveau du sac ou de la cuve, retirez les gros débris et regardez si le flexible est obstrué. Un sac trop plein ou un coude bouché augmente la résistance du circuit et réduit le débit. Rangez ensuite le câble et le flexible sans pli serré afin de ne pas endommager leur gaine.</p>
<p>Si vous avez aspiré de l’eau, suivez la procédure de vidage du fabricant et laissez sécher les parties qui doivent l’être avant de repasser en mode poussière. L’humidité mélangée à des poussières fines peut former une pâte qui colmate rapidement le filtre et les conduits.</p>

<h2 id="filtre">Entretenir le filtre sans l’abîmer</h2>
<p>Un filtre n’a pas besoin d’être visuellement neuf pour fonctionner, mais il doit rester intact et dans les limites prévues par la machine. Utilisez le <a href="/guides/decolmatage-automatique/">système de décolmatage</a> lorsqu’il existe et remplacez le filtre lorsqu’il est endommagé, saturé ou arrivé à l’échéance indiquée par le fabricant.</p>
<p>Ne lavez pas un filtre simplement parce qu’il paraît sale : certains médias sont lavables, d’autres non. De même, le soufflage à l’air comprimé peut endommager le média et disperser des poussières. La méthode autorisée figure dans la notice de la référence exacte. Si un filtre lavable a été rincé, il doit être complètement sec avant remontage lorsque le fabricant l’exige.</p>

<h2 id="cuve">Cuve, sacs et aspiration de liquides</h2>
<p>Nettoyez les résidus qui pourraient gêner les joints, le flotteur ou les capteurs de niveau. Les appareils eau/poussière disposent d’un dispositif destiné à limiter la montée de liquide ; s’il reste bloqué par des débris, la protection peut ne pas fonctionner comme prévu. N’utilisez pas la capacité brute comme niveau de remplissage cible.</p>
<p>Pour les poussières, remplacez le <a href="/accessoires/sacs-aspirateur-chantier/">sac</a> avant qu’il n’étrangle le flux. Le guide <a href="/guides/sac-ou-sans-sac/">sac ou sans sac</a> explique pourquoi le mode de collecte influence à la fois le débit, la propreté et la maintenance.</p>

<h2 id="tuyau">Flexible, raccords et joints : les fuites invisibles coûtent du débit</h2>
<p>Inspectez le tuyau sur toute sa longueur, en particulier près des manchons où les torsions sont fréquentes. Une fissure aspire de l’air parasite et réduit le captage à l’outil. Nettoyez les raccords qui s’encrassent et vérifiez que les adaptateurs restent correctement emboîtés.</p>
<p>Les joints de cuve et de couvercle doivent être propres et non pincés. Sur un appareil de classe de poussières, l’étanchéité fait partie de la performance du système. Remplacez une pièce endommagée par une référence compatible plutôt que d’improviser un joint ou un ruban adhésif.</p>

<h2 id="moteur">Protéger le moteur : éviter la surchauffe plutôt que la réparer</h2>
<p>Le moteur dépend du flux d’air et des protections prévues par le constructeur. Un filtre saturé, un sac plein ou des grilles de refroidissement obstruées peuvent augmenter les contraintes thermiques. Gardez les entrées d’air dégagées et interrompez l’utilisation si le bruit, l’odeur ou la température changent anormalement.</p>
<p>Ne démontez pas le groupe moteur pour un entretien courant si la notice ne le prévoit pas. Les charbons, roulements et composants électriques relèvent généralement du service technique. Pour préserver la machine, la meilleure stratégie reste de maintenir un circuit propre et de traiter rapidement les pertes de débit.</p>

<h2 id="dangereux">Poussières dangereuses : la maintenance est une opération à risque</h2>
<p>Avec des poussières de classe H ou des contaminants comme l’amiante, ouvrir la cuve, retirer le filtre ou remplacer le sac peut exposer l’opérateur. L’INRS prévoit des exigences spécifiques de maintenance et de décontamination pour ces équipements. Un entretien « comme à la maison » n’est pas approprié.</p>
<p>Respectez les procédures de l’entreprise, les équipements de protection et la filière de déchets prévue. Le <a href="/guides/classes-l-m-h/">guide L/M/H</a> donne le cadre général, mais les documents réglementaires et la notice restent la référence pour ces interventions.</p>
{sources("iec", "inrs_asbestos", "bosch_gas35", "inrs_wood")}
'''
},
}


def make_toc(items):
    return "\n".join(f'<a href="#{anchor}">{label}</a>' for anchor, label in items)


def replace_block(html, start_marker, end_marker, new_content, placeholder=None):
    pattern = re.compile(re.escape(start_marker) + r".*?" + re.escape(end_marker), re.S)
    wrapped = f"{start_marker}\n{new_content.strip()}\n{end_marker}"
    if pattern.search(html):
        return pattern.sub(wrapped, html, count=1)
    if placeholder and placeholder in html:
        return html.replace(placeholder, wrapped, 1)
    raise RuntimeError(f"Could not find replace target for {start_marker}")


def apply_guide(slug, data):
    path = BASE / "guides" / slug / "index.html"
    html = path.read_text(encoding="utf-8")

    answer_pattern = re.compile(
        r'<div class="(?:article-answer )?answer-box"><p>.*?</p></div>', re.S
    )
    answer_html = f'<div class="article-answer answer-box"><p>{data["answer"]}</p></div>'
    if answer_pattern.search(html):
        html = answer_pattern.sub(answer_html, html, count=1)
    else:
        # The maintenance page initially has no answer box.
        article_open = '<article class="content-main">'
        html = html.replace(article_open, article_open + "\n      " + answer_html, 1)

    html = replace_block(
        html,
        "<!-- GUIDE_CONTENT_START -->",
        "<!-- GUIDE_CONTENT_END -->",
        data["body"],
        "<!-- Contenu à rédiger -->",
    )
    html = replace_block(
        html,
        "<!-- GUIDE_TOC_START -->",
        "<!-- GUIDE_TOC_END -->",
        make_toc(data["toc"]),
        "<!-- TOC générée -->",
    )
    html = html.replace("Vérifié : MM/AAAA", f"Vérifié : {VERIFIED}")
    path.write_text(html, encoding="utf-8")
    print(f"✓ {path.relative_to(BASE)}")


def main():
    missing = [slug for slug in GUIDES if not (BASE / "guides" / slug / "index.html").exists()]
    if missing:
        raise SystemExit(f"Guide pages missing: {', '.join(missing)}")
    for slug, data in GUIDES.items():
        apply_guide(slug, data)
    print(f"\n{len(GUIDES)} guides enriched; robots directives preserved.")


if __name__ == "__main__":
    main()
