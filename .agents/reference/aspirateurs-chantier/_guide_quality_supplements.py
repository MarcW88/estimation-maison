#!/usr/bin/env python3
"""Editorial supplements required by the guide quality floor.

Run after `_generate_guides.py`. The supplements are intentionally specific to
pages that remain below 900 words after the first production pass; they add a
useful decision layer rather than generic word-count padding. The script also
keeps the visual `answer-box` wrapper while exposing the exact
`article-answer` class expected by the workflow validator.
"""
from pathlib import Path
import re

BASE = Path(__file__).resolve().parent

SUPPLEMENTS = {
    "capacite-cuve": '''
<h2 id="dimensionnement-exemple">Exemple de dimensionnement : raisonner en fréquence de vidage</h2>
<p>Imaginez deux usages opposés. Dans un petit chantier de rénovation intérieure, l’aspirateur monte des escaliers, passe des portes et doit être rangé dans un véhicule déjà chargé : accepter un vidage supplémentaire peut être préférable à transporter en permanence une cuve volumineuse. Dans un atelier fixe qui produit régulièrement des copeaux, le déplacement compte moins et une réserve plus importante réduit les interruptions. Le bon volume dépend donc du flux de déchets entre deux vidages possibles, pas d’une catégorie « amateur » ou « professionnel » figée.</p>
<p>Pour comparer deux modèles, notez séparément la capacité brute, la capacité nette annoncée, le volume d’eau éventuel, la masse à vide et le mode de collecte. Ajoutez ensuite une contrainte simple : pourriez-vous déplacer ou vider l’appareil lorsqu’il contient réellement cette quantité de déchets ? Cette vérification évite de payer pour une capacité théorique qui devient peu pratique une fois la cuve chargée.</p>
''',
    "debit-air-aspirateur": '''
<h2 id="diagnostic-debit">Comment repérer un problème de débit pendant l’utilisation</h2>
<p>Une aspiration qui devient progressivement moins efficace ne signifie pas forcément que le moteur manque de puissance. Commencez par vérifier les causes les plus simples : sac rempli, filtre chargé, flexible pincé, raccord partiellement bouché ou entrée d’air parasite. Si le captage redevient correct après nettoyage du filtre ou remplacement du sac, le problème venait surtout de la résistance du circuit et non de la valeur maximale annoncée par le fabricant.</p>
<p>Avec un outil raccordé, observez aussi ce qui se passe au point d’émission. Une grande quantité de poussière qui s’échappe alors que le flexible aspire correctement peut révéler un capot mal positionné, un adaptateur trop fuyant ou un débit insuffisant pour la géométrie de l’outil. Ce diagnostic est plus utile qu’une comparaison abstraite de L/s : il relie la donnée technique au fonctionnement réel de l’ensemble outil–flexible–aspirateur.</p>
''',
    "decolmatage-automatique": '''
<h2 id="rentabilite">Le décolmatage vaut-il le surcoût ?</h2>
<p>La réponse dépend surtout du temps passé à produire des poussières fines. Si l’aspirateur sert quelques minutes pour nettoyer un établi ou ramasser des déchets grossiers, un système automatique apporte peu de valeur et ajoute parfois du coût, du bruit ou de la complexité. Si l’appareil reste raccordé à une ponceuse pendant de longues séquences, chaque perte de débit oblige au contraire à interrompre le travail, nettoyer le filtre et relancer l’aspiration.</p>
<p>Pour arbitrer, estimez moins le nombre de chantiers que la durée cumulée de captage continu et le type de poussière. Plus le filtre se charge vite, plus le maintien automatique du débit devient intéressant. Comparez ensuite le prix des filtres et sacs, la procédure de nettoyage manuel et l’accessibilité du filtre. Un bon système automatique se juge sur le temps et la constance qu’il fait gagner, pas sur la présence d’un acronyme dans la fiche produit.</p>
''',
    "depression-kpa-mbar-air-watt": '''
<h2 id="exemple-conversion">Exemple pratique : normaliser deux fiches avant de comparer</h2>
<p>Supposons qu’une fiche annonce 25 kPa et une autre 250 mbar. Après conversion, les deux valeurs de dépression maximale sont numériquement équivalentes puisque 25 kPa valent 250 mbar. Cela ne permet pourtant pas encore de conclure à des performances identiques. Il faut ensuite vérifier le point de mesure, la présence du filtre et du flexible pendant la mesure, ainsi que le débit d’air associé à chaque appareil.</p>
<p>Cette méthode en deux temps — d’abord convertir, ensuite vérifier le protocole — évite la plupart des comparaisons trompeuses. Elle vaut aussi pour le mmH₂O. Une unité impressionnante ou un nombre plus grand ne signifie pas une aspiration supérieure : 2 550 mmH₂O environ, 25 kPa et 250 mbar décrivent presque la même pression. La qualité de la comparaison vient donc davantage du contexte de mesure que de l’unité choisie par le fabricant.</p>
''',
    "entretien-aspirateur-chantier": '''
<h2 id="planning">Quel rythme d’entretien adopter ?</h2>
<p>Il n’existe pas un calendrier universel, car un aspirateur utilisé dix minutes pour des copeaux ne se charge pas comme une machine raccordée plusieurs heures à une ponceuse. Le contrôle le plus pertinent est donc lié à l’usage : inspection rapide après chaque chantier, vérification immédiate si le débit chute, et entretien plus approfondi lorsque la notice le prévoit ou avant une période de stockage. Les consommables se remplacent selon leur état et les instructions du fabricant, pas selon une échéance inventée valable pour toutes les marques.</p>
<p>Conservez si possible une petite trace des remplacements de filtres et des anomalies constatées sur un appareil utilisé professionnellement. Une hausse inhabituelle de la fréquence de colmatage peut signaler un sac inadapté, une fuite, un changement de matériau ou un problème de décolmatage. Cette logique préventive permet d’intervenir sur la cause avant de solliciter inutilement le moteur ou de dégrader le captage.</p>
''',
    "filtre-hepa-aspirateur": '''
<h2 id="achat-hepa">Que vérifier avant d’acheter un aspirateur présenté comme « HEPA » ?</h2>
<p>Le mot HEPA seul est trop vague pour une décision technique. Cherchez la classe exacte du filtre, par exemple H13 ou H14, la norme de référence, puis la classe de poussières éventuelle de l’appareil complet. Vérifiez aussi que le filtre proposé est bien celui prévu pour la référence vendue en France : une gamme peut utiliser plusieurs médias ou configurations selon les marchés et les accessoires.</p>
<p>Regardez enfin la disponibilité du filtre de remplacement et la procédure de changement. Une filtration performante perd son intérêt si le consommable compatible devient introuvable ou si l’utilisateur le remplace par une cartouche générique dont l’étanchéité n’est pas garantie. Pour un besoin de sécurité réglementé, ne basez jamais le choix sur une mention marketing « HEPA » : exigez la documentation de l’appareil et les certifications correspondant au risque traité.</p>
''',
    "prise-asservie": '''
<h2 id="checklist-compatibilite">Checklist de compatibilité avant de brancher l’outil</h2>
<p>Avant la première utilisation, vérifiez quatre éléments dans la documentation : la puissance ou le courant admissible sur la prise outil, la tension prévue, le mode de démarrage automatique et la temporisation éventuelle après l’arrêt. Comparez ensuite cette limite avec les caractéristiques de l’outil lui-même. Si la notice de l’aspirateur prévoit une plage ou une limite spécifique, c’est cette valeur qui fait foi, même si un autre modèle de la même marque accepte davantage.</p>
<p>Contrôlez aussi la partie aspiration avant de considérer l’ensemble compatible. Le diamètre du manchon, la longueur du flexible et la tenue du raccord peuvent être plus limitants que la connexion électrique. Une bonne installation doit permettre à l’outil de bouger sans arracher le tuyau ni créer une fuite importante. Cette vérification simple réduit les déclenchements intempestifs et améliore surtout le captage à la source.</p>
''',
    "puissance-aspiration": '''
<h2 id="comparaison-exemple">Exemple de comparaison : deux moteurs de puissance différente</h2>
<p>Un modèle de 1 400 W n’est pas automatiquement supérieur à un modèle de 1 200 W. Le premier peut consommer davantage tout en ayant un circuit moins efficace, un flexible plus restrictif ou une filtration qui se colmate rapidement. À l’inverse, le second peut fournir un débit utile plus stable grâce à une meilleure conception ou un système de nettoyage du filtre adapté au matériau aspiré. Sans débit, dépression et conditions de mesure, le chiffre en watts ne permet donc pas de classer les deux appareils.</p>
<p>Pour une comparaison exploitable, créez trois colonnes distinctes : puissance absorbée, débit maximal avec point de mesure, dépression maximale avec point de mesure. Ajoutez ensuite les éléments qui influencent la tenue dans le temps — filtre, décolmatage, sac et diamètre de flexible. Cette grille transforme une donnée marketing facile à lire en décision technique cohérente avec le chantier.</p>
''',
    "sac-ou-sans-sac": '''
<h2 id="strategie-consommables">Réduire le coût des sacs sans dégrader le système</h2>
<p>Le moyen le plus sûr d’économiser n’est pas d’utiliser systématiquement l’aspirateur sans sac, mais de réserver chaque configuration aux déchets pour lesquels elle est prévue. Pour les poussières fines, un sac correctement dimensionné peut protéger le filtre principal et réduire le temps de nettoyage. Pour certains déchets grossiers ou pour l’eau, la notice peut autoriser ou imposer une autre configuration. Cette alternance raisonnée évite de consommer des sacs inutilement sans sacrifier la maîtrise des poussières.</p>
<p>Évitez en revanche de réutiliser un sac jetable au-delà de ce que prévoit le fabricant ou de monter un consommable dont la compatibilité n’est pas établie. Un sac moins cher qui fuit, s’effondre ou réduit fortement le débit peut accélérer l’encrassement du filtre et annuler l’économie initiale. Comparez le coût par chantier avec le temps de maintenance et la durée de vie du filtre, pas uniquement le prix à l’unité.</p>
''',
}


def expose_validator_answer(html: str) -> str:
    pattern = re.compile(
        r'<div class="article-answer answer-box"><p>(.*?)</p></div>',
        re.S,
    )
    return pattern.sub(
        r'<div class="answer-box"><div class="article-answer"><p>\1</p></div></div>',
        html,
        count=1,
    )


def main():
    for path in sorted((BASE / "guides").glob("*/index.html")):
        slug = path.parent.name
        html = path.read_text(encoding="utf-8")
        html = expose_validator_answer(html)

        supplement = SUPPLEMENTS.get(slug)
        if supplement:
            marker = '<h2 id="sources">Sources et références</h2>'
            if marker not in html:
                raise RuntimeError(f"Sources marker missing for {slug}")
            html = html.replace(marker, supplement.strip() + "\n" + marker, 1)

        path.write_text(html, encoding="utf-8")
        print(f"✓ quality supplement: {slug}")


if __name__ == "__main__":
    main()
