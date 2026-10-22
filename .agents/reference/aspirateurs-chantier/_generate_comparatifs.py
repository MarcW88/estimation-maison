#!/usr/bin/env python3
"""Generate auditable comparison pages from explicit criteria, evidence and scores."""
from pathlib import Path
from html import escape
import json
import re

from _generate import breadcrumb, content_page

BASE = Path(__file__).resolve().parent
UPDATED = "08/09/2026"

PRODUCTS = {
    "bosch-gas35m": {
        "name": "Bosch Professional GAS 35 M AFC",
        "source": "https://www.bosch-professional.com/fr/fr/products/gas-35-m-afc-06019C31W0",
        "local": "/modeles/bosch-gas-35-m-afc/",
        "facts": "classe M, 35 L brut / 23 L net, 74 l/s et 254 mbar à la turbine, nettoyage automatique AFC, 12,4 kg",
        "best": "travail régulier avec poussières fines lorsque la classe M est adaptée au risque",
        "limit": "plus lourd et nettement plus coûteux qu'un aspirateur eau/poussière grand public",
        "class": "M", "capacity": 35, "airflow": 74, "vacuum": 254, "weight": 12.4,
    },
    "karcher-wd7": {
        "name": "Kärcher WD 7 Control P S 30/6/35/T",
        "source": "https://www.kaercher.com/fr/home-garden/aspirateurs-eau-et-poussieres/wd-7-control-p-s-30-6-35-t-eu-iii-16283860.html",
        "local": "/marques/karcher/",
        "facts": "30 L, 80 l/s, 290 mbar, 315 W de puissance d'aspiration annoncée, prise asservie et télécommande 2-en-1, 8,7 kg",
        "best": "nettoyage eau/poussière, gravats et atelier quand une certification M n'est pas requise",
        "limit": "ce n'est pas un aspirateur de sécurité de classe M ; les chiffres de turbine ne remplacent pas une évaluation du risque poussière",
        "class": "consumer", "capacity": 30, "airflow": 80, "vacuum": 290, "weight": 8.7,
    },
    "karcher-wd6": {
        "name": "Kärcher WD 6 P S V-30/6/22/T",
        "source": "https://www.kaercher.com/be-fr/home-garden/aspirateurs-multifonction/wd-6-p-s-v-30-6-22-t-16283610.html",
        "local": "/modeles/karcher-wd6/",
        "facts": "30 L, 75 l/s, 280 mbar, prise asservie, nettoyage du filtre par impulsion et 9,3 kg",
        "best": "rénovation et atelier polyvalents avec eau, poussières et outil électroportatif",
        "limit": "nettoyage du filtre à la demande, pas certification de classe M",
        "class": "consumer", "capacity": 30, "airflow": 75, "vacuum": 280, "weight": 9.3,
    },
    "karcher-wd3": {
        "name": "Kärcher WD 3 V-17/4/20",
        "source": "https://www.kaercher.com/fr/home-garden/aspirateurs-eau-et-poussieres/wd-3-v-17-4-20-16281300.html",
        "local": "/marques/karcher/",
        "facts": "17 L, 45 l/s, 230 mbar, 4,5 kg, filtre cartouche permettant eau et poussière sans changement de filtre",
        "best": "petits nettoyages, garage et bricolage quand compacité et simplicité priment",
        "limit": "pas de prise asservie sur cette version et pas de certification de classe M",
        "class": "consumer", "capacity": 17, "airflow": 45, "vacuum": 230, "weight": 4.5,
    },
    "bosch-advancedvac20": {
        "name": "Bosch AdvancedVac 20",
        "source": "https://www.bosch-diy.com/fr/fr/p/advancedvac-20-06033d12w0",
        "local": "/modeles/bosch-advancedvac-20/",
        "facts": "20 L, 70 l/s, 260 mbar, prise asservie, évacuation d'eau et 7,6 kg",
        "best": "atelier de bricolage avec outils filaires et besoin eau/poussière",
        "limit": "positionnement bricolage ; pas de certification M pour poussières nécessitant ce niveau de protection",
        "class": "consumer", "capacity": 20, "airflow": 70, "vacuum": 260, "weight": 7.6,
    },
    "bosch-gas18": {
        "name": "Bosch Professional GAS 18V-10 L",
        "source": "https://www.bosch-professional.com/fr/fr/products/gas-18v-10-l-06019C6302",
        "local": "/modeles/bosch-gas-18v-10-l/",
        "facts": "18 V, classe L, 10 L brut / 6 L net, 34 l/s, 115 mbar, sans sac, 4,7 kg sans batterie, autonomie annoncée 4 min/Ah",
        "best": "interventions mobiles courtes et nettoyage sans prise dans l'écosystème Bosch 18 V",
        "limit": "cuve et autonomie limitées ; classe L, donc pas un substitut à un aspirateur M quand le risque l'exige",
        "class": "L", "capacity": 10, "airflow": 34, "vacuum": 115, "weight": 4.7,
    },
    "karcher-wd318": {
        "name": "Kärcher WD 3-18 S",
        "source": "https://www.kaercher.com/fr/home-garden/aspirateurs-eau-et-poussieres/wd-3-18-s-avec-la-batterie-amovible-16285760.html",
        "local": "/marques/karcher/",
        "facts": "18 V, 17 L, 30 l/s, 110 mbar, environ 20 min avec batterie 5 Ah, 4,1 kg sans accessoires",
        "best": "nettoyage eau/poussière sans fil lorsque la capacité compte plus qu'un débit élevé",
        "limit": "performances nettement sous les modèles filaires et pas de classification M",
        "class": "consumer", "capacity": 17, "airflow": 30, "vacuum": 110, "weight": 4.1,
    },
    "festool-ctc-midi": {
        "name": "Festool CTC MIDI I",
        "source": "https://www.festool.fr/campagnes/microsites/aspiration",
        "local": "/marques/festool/",
        "facts": "aspirateur sans fil 36 V (2 batteries 18 V), cuve 15 L, 10,2 kg, autonomie 10–20 min avec 2×4 Ah, jusqu'à 24–45 min avec 2×8 Ah",
        "best": "montage et aspiration mobile avec outils Festool, où le déclenchement Bluetooth et l'écosystème comptent",
        "limit": "coût du système batteries élevé et autonomie dépendante du niveau d'aspiration",
        "class": "L", "capacity": 15, "airflow": 52, "vacuum": 190, "weight": 10.2,
    },
    "festool-ctm-midi-ac": {
        "name": "Festool CTM MIDI I AC",
        "source": "https://www.festool.fr/produits/aspirateurs/aspirateurs-compact/578552---ctm-midi-i-ac",
        "local": "/marques/festool/",
        "facts": "classe M, 15 L / sac 12,5 L, 3 700 l/min (≈61,7 l/s), 24 000 Pa, AUTOCLEAN, prise 2 400 W, 11,8 kg",
        "best": "professionnels qui veulent classe M et décolmatage automatique dans un format compact",
        "limit": "petite cuve et positionnement premium ; moins adapté aux gros volumes de déchets",
        "class": "M", "capacity": 15, "airflow": 61.7, "vacuum": 240, "weight": 11.8,
    },
    "karcher-nt30m": {
        "name": "Kärcher NT 30/1 Tact Te M ACD",
        "source": "https://www.kaercher.com/fr/professional/aspirateurs-eau-et-poussieres/aspirateurs-de-securite/nt-30-1-tact-te-m-acd-11482350.html",
        "local": "/modeles/karcher-nt-30-1-tact/",
        "facts": "classe M, ACD, 30 L, 74 l/s, 273 mbar, Tact commandé par capteur, prise asservie, 14,2 kg",
        "best": "chantier professionnel avec fortes quantités de poussières fines et besoin d'un décolmatage automatique robuste",
        "limit": "poids élevé et prix professionnel ; ACD ne signifie pas automatiquement adapté à toute atmosphère explosive",
        "class": "M", "capacity": 30, "airflow": 74, "vacuum": 273, "weight": 14.2,
    },
    "karcher-nt50m": {
        "name": "Kärcher NT 50/1 Tact Te M ACD",
        "source": "https://www.kaercher.com/fr/professional/aspirateurs-eau-et-poussieres/aspirateurs-de-securite/nt-50-1-tact-te-m-acd-11484350.html",
        "local": "/marques/karcher/",
        "facts": "classe M, ACD, 50 L, 74 l/s, 273 mbar, Tact automatique, flexible de vidange, 19 kg",
        "best": "gros volumes de poussières, déchets et liquides sur chantier ou atelier professionnel",
        "limit": "très encombrant pour les déplacements fréquents et surdimensionné pour les petits travaux",
        "class": "M", "capacity": 50, "airflow": 74, "vacuum": 273, "weight": 19.0,
    },
}

PAGES = {
    "meilleur-aspirateur-de-chantier": {
        "title": "Meilleur aspirateur de chantier — Comparatif 2026",
        "desc": "Comparatif 2026 fondé sur les usages, la filtration, le maintien des performances et les données fabricants, sans prétendre à un test physique.",
        "query": "meilleur aspirateur de chantier", "type": "best_overall",
        "job": "choisir un aspirateur réellement adapté au chantier, pas seulement le modèle ayant le plus gros chiffre de dépression",
        "constraint": "équilibrer sécurité poussière, endurance, aspiration et praticité",
        "products": ["bosch-gas35m", "karcher-nt30m", "karcher-wd7"],
        "criteria": [("safety","Adéquation poussières et filtration",25,True),("endurance","Maintien des performances",25,False),("suction","Débit et dépression",20,False),("workflow","Prise, flexible et usage outil",15,False),("mobility","Mobilité et volume utile",15,False)],
        "scores": {"bosch-gas35m":[9,9,8,9,7],"karcher-nt30m":[10,10,9,9,6],"karcher-wd7":[5,7,10,9,9]},
        "answer": "Pour un chantier où la poussière fine fait partie du quotidien, notre choix 2026 est le <strong>Kärcher NT 30/1 Tact Te M ACD</strong>. Le <strong>Bosch GAS 35 M AFC</strong> est l'alternative la plus équilibrée. Le <strong>Kärcher WD 7 Control</strong> est plus pertinent pour le nettoyage polyvalent eau, poussière et gravats lorsque la classe M n'est pas requise.",
        "decision": "Sur une requête aussi large, nous refusons de confondre puissance et adéquation. Un modèle grand public peut afficher d'excellents chiffres de turbine mais rester un mauvais choix face à une poussière qui impose une classe de sécurité supérieure.",
    },
    "aspirateur-eau-poussiere": {
        "title": "Meilleur aspirateur eau et poussière de chantier — Comparatif 2026",
        "desc": "Comparaison 2026 des aspirateurs eau et poussière pour rénovation, garage et chantier : capacité, vidange, aspiration et polyvalence.",
        "query": "aspirateur eau poussière chantier", "type": "feature_specific",
        "job": "aspirer aussi bien des liquides que des déchets secs sans transformer chaque changement d'usage en contrainte",
        "constraint": "polyvalence eau/poussière, capacité et facilité de vidange",
        "products": ["karcher-wd7","karcher-wd6","bosch-advancedvac20"],
        "criteria": [("wetdry","Polyvalence eau/poussière",25,True),("suction","Débit et dépression",25,False),("capacity","Capacité et vidange",20,False),("workflow","Prise et outils",15,False),("mobility","Mobilité et entretien",15,False)],
        "scores": {"karcher-wd7":[10,10,10,10,8],"karcher-wd6":[10,9,10,9,8],"bosch-advancedvac20":[9,8,8,9,9]},
        "answer": "Le <strong>Kärcher WD 7 Control</strong> arrive en tête pour l'eau et la poussière grâce à sa cuve de 30 L, son débit annoncé de 80 l/s et sa vidange. Le <strong>WD 6 P S</strong> reste très proche et plus simple. Le <strong>Bosch AdvancedVac 20</strong> est une option plus compacte pour l'atelier de bricolage.",
        "decision": "Ici, une classe M n'est pas le critère dominant : l'intention porte d'abord sur la polyvalence humide/sec. En revanche, dès que les poussières deviennent dangereuses, il faut sortir de ce comparatif et raisonner par classe de poussière.",
    },
    "aspirateur-chantier-sans-fil": {
        "title": "Meilleur aspirateur de chantier sans fil — Comparatif 2026",
        "desc": "Comparatif 2026 des aspirateurs de chantier sur batterie : autonomie, aspiration, capacité, mobilité et coût du système batterie.",
        "query": "aspirateur chantier sans fil", "type": "feature_specific",
        "job": "travailler sans prise pour des interventions courtes, du montage ou du nettoyage mobile",
        "constraint": "autonomie réelle du système, mobilité et niveau d'aspiration",
        "products": ["bosch-gas18","festool-ctc-midi","karcher-wd318"],
        "criteria": [("cordless","Fonctionnement réellement sans fil",20,True),("runtime","Autonomie et batteries",25,False),("suction","Aspiration",20,False),("mobility","Poids et encombrement",20,False),("workflow","Écosystème et usage outil",15,False)],
        "scores": {"bosch-gas18":[10,8,8,10,9],"festool-ctc-midi":[10,9,9,6,10],"karcher-wd318":[10,8,7,9,7]},
        "answer": "Le <strong>Bosch GAS 18V-10 L</strong> est notre choix le plus équilibré pour une intervention mobile : compact, classe L et sans sac. Le <strong>Festool CTC MIDI I</strong> est plus cohérent pour un professionnel déjà équipé en Festool. Le <strong>Kärcher WD 3-18 S</strong> privilégie la capacité eau/poussière.",
        "decision": "Le piège du sans-fil est de comparer seulement la tension de batterie. L'autonomie dépend de la capacité, du niveau d'aspiration et du nombre de batteries disponibles ; le coût du système complet compte autant que le prix de l'appareil nu.",
    },
    "aspirateur-chantier-sans-sac": {
        "title": "Aspirateur de chantier sans sac — Les meilleurs choix en 2026",
        "desc": "Quel aspirateur de chantier utiliser sans sac en 2026 ? Comparaison des solutions réellement adaptées et des limites avec les poussières fines.",
        "query": "aspirateur chantier sans sac", "type": "feature_specific",
        "job": "limiter les consommables sans sacrifier la filtration ni encrasser prématurément le filtre",
        "constraint": "fonctionnement sans sac crédible et entretien du filtre",
        "products": ["bosch-gas18","karcher-wd7","karcher-wd3"],
        "criteria": [("bagless","Conception ou usage sans sac",25,True),("filter","Gestion du filtre",25,False),("suction","Aspiration",20,False),("emptying","Vidage et entretien",15,False),("mobility","Mobilité",15,False)],
        "scores": {"bosch-gas18":[10,9,7,9,10],"karcher-wd7":[8,9,10,8,8],"karcher-wd3":[7,7,6,8,10]},
        "answer": "Si le critère principal est vraiment le sans-sac, le <strong>Bosch GAS 18V-10 L</strong> est le choix le plus clair : Bosch le présente explicitement comme une conception sans sac. Le <strong>Kärcher WD 7</strong> est plus puissant, mais l'usage sans sac doit rester cohérent avec la nature des déchets et la protection du filtre.",
        "decision": "« Sans sac » n'est pas synonyme de « sans consommable » ni de « mieux filtré ». Pour les poussières fines, un sac peut protéger le filtre, faciliter l'élimination et réduire l'exposition lors du vidage. Le bon choix dépend donc du déchet, pas d'une préférence absolue.",
    },
    "aspirateur-chantier-puissant": {
        "title": "Aspirateur de chantier puissant — Comparatif 2026",
        "desc": "Comparatif des aspirateurs de chantier puissants en 2026 : débit, dépression, maintien des performances et limites des chiffres fabricants.",
        "query": "aspirateur chantier puissant", "type": "feature_specific",
        "job": "choisir un aspirateur capable de déplacer un fort volume d'air et de garder une aspiration utile sous charge",
        "constraint": "ne pas confondre watts électriques, débit et dépression",
        "products": ["karcher-wd7","karcher-nt30m","bosch-gas35m"],
        "criteria": [("suction","Débit et dépression annoncés",35,True),("endurance","Maintien du débit filtre chargé",25,False),("dust","Gestion des poussières fines",20,False),("workflow","Connexion outils",10,False),("mobility","Rapport puissance/encombrement",10,False)],
        "scores": {"karcher-wd7":[10,7,5,9,9],"karcher-nt30m":[9,10,10,9,6],"bosch-gas35m":[8,10,10,9,7]},
        "answer": "Sur les chiffres bruts de turbine, le <strong>Kärcher WD 7 Control</strong> est le plus impressionnant de cette sélection avec 80 l/s et 290 mbar annoncés. Pour les poussières fines et le travail prolongé, le <strong>Kärcher NT 30/1 Tact Te M ACD</strong> devient toutefois plus cohérent grâce à la classe M et au Tact automatique.",
        "decision": "Nous distinguons volontairement le gagnant des chiffres bruts du meilleur choix de chantier. Un débit maximal neuf ne dit pas comment l'appareil se comporte avec un filtre chargé, un long flexible, un outil raccordé ou une poussière qui impose une filtration spécifique.",
    },
    "aspirateur-professionnel": {
        "title": "Meilleur aspirateur de chantier professionnel — Comparatif 2026",
        "desc": "Comparatif 2026 pour les professionnels : classe M, décolmatage, prise asservie, endurance, mobilité et capacité.",
        "query": "aspirateur chantier professionnel", "type": "best_for_use_case",
        "job": "travailler régulièrement avec des outils électroportatifs et des poussières fines sans perdre du temps à nettoyer le filtre",
        "constraint": "sécurité, endurance quotidienne et intégration aux outils",
        "products": ["karcher-nt30m","bosch-gas35m","festool-ctm-midi-ac"],
        "criteria": [("safety","Classe M et surveillance",25,True),("endurance","Décolmatage et endurance",25,False),("workflow","Prise, antistatique, outils",20,False),("suction","Aspiration",15,False),("mobility","Mobilité sur chantier",15,False)],
        "scores": {"karcher-nt30m":[10,10,10,9,7],"bosch-gas35m":[10,10,9,8,8],"festool-ctm-midi-ac":[10,10,10,8,9]},
        "answer": "Pour un usage professionnel polyvalent, le <strong>Festool CTM MIDI I AC</strong> arrive en tête de notre scoring grâce à son format compact, sa classe M, son AUTOCLEAN et son intégration aux outils. Le <strong>Kärcher NT 30/1 Tact Te M ACD</strong> est plus pertinent lorsque capacité et gros volumes de poussières priment. Le <strong>Bosch GAS 35 M AFC</strong> reste un excellent généraliste.",
        "decision": "Le classement professionnel donne plus de poids à la classe de poussière, au décolmatage et au workflow outil qu'au prix d'achat. Sur une journée de chantier, les arrêts de nettoyage, le flexible, la prise asservie et le vidage pèsent davantage qu'un écart marginal de puissance.",
    },
    "aspirateur-industriel": {
        "title": "Meilleur aspirateur industriel mobile — Comparatif 2026",
        "desc": "Comparatif 2026 des aspirateurs industriels mobiles pour gros volumes : cuve, poussières fines, liquides, décolmatage et manutention.",
        "query": "aspirateur industriel chantier", "type": "best_for_use_case",
        "job": "collecter des volumes importants de déchets, poussières ou liquides dans un cadre professionnel mobile",
        "constraint": "capacité, endurance et sécurité sans basculer vers une installation d'aspiration fixe",
        "products": ["karcher-nt50m","karcher-nt30m","bosch-gas35m"],
        "criteria": [("capacity","Capacité et vidange",25,True),("endurance","Décolmatage et endurance",25,False),("safety","Classe M et filtration",20,False),("suction","Aspiration",15,False),("handling","Manutention",15,False)],
        "scores": {"karcher-nt50m":[10,10,10,9,6],"karcher-nt30m":[8,10,10,9,8],"bosch-gas35m":[8,9,10,8,8]},
        "answer": "Pour de gros volumes dans un format encore mobile, le <strong>Kärcher NT 50/1 Tact Te M ACD</strong> est notre premier choix : 50 L, classe M, Tact automatique et flexible de vidange. Le <strong>NT 30/1</strong> est plus facile à déplacer. Le <strong>Bosch GAS 35 M AFC</strong> est l'alternative polyvalente.",
        "decision": "Nous employons ici « industriel » au sens d'un aspirateur professionnel mobile à grande capacité. Une aspiration centralisée, ATEX ou destinée à un procédé industriel continu relève d'un autre univers produit et ne doit pas être mélangée avec ces machines de chantier.",
    },
    "aspirateur-classe-m": {
        "title": "Meilleur aspirateur classe M — Comparatif 2026",
        "desc": "Comparatif 2026 des aspirateurs de chantier classe M : filtration, surveillance du débit, décolmatage, aspiration et mobilité.",
        "query": "aspirateur classe M", "type": "feature_specific",
        "job": "sélectionner un aspirateur certifié M adapté aux poussières et au rythme de travail visés",
        "constraint": "la certification M est un hard gate, pas un bonus marketing",
        "products": ["karcher-nt30m","bosch-gas35m","festool-ctm-midi-ac"],
        "criteria": [("classm","Certification classe M",30,True),("endurance","Décolmatage",25,False),("monitoring","Surveillance et sécurité",20,False),("suction","Aspiration",15,False),("mobility","Mobilité",10,False)],
        "scores": {"karcher-nt30m":[10,10,10,9,7],"bosch-gas35m":[10,10,9,8,8],"festool-ctm-midi-ac":[10,10,9,8,9]},
        "answer": "Le <strong>Kärcher NT 30/1 Tact Te M ACD</strong> est notre choix classe M pour les gros volumes de poussières fines. Le <strong>Bosch GAS 35 M AFC</strong> est très équilibré. Le <strong>Festool CTM MIDI I AC</strong> se distingue par son format compact et son intégration aux outils.",
        "decision": "Une classe M n'est pas une note de qualité globale : c'est une classification liée à la gestion de certaines poussières. Le matériau, l'opération, la valeur limite d'exposition et les règles applicables doivent guider le choix ; ce comparatif ne remplace pas l'évaluation du risque.",
    },
    "petit-aspirateur-de-chantier": {
        "title": "Petit aspirateur de chantier — Comparatif compact 2026",
        "desc": "Comparatif 2026 des petits aspirateurs de chantier : poids, encombrement, capacité, aspiration et usage mobile.",
        "query": "petit aspirateur de chantier", "type": "best_for_use_case",
        "job": "gagner de la place et transporter facilement l'aspirateur sans le rendre inutile dès que les déchets s'accumulent",
        "constraint": "compacité, poids et capacité suffisante",
        "products": ["karcher-wd3","bosch-gas18","festool-ctm-midi-ac"],
        "criteria": [("compact","Compacité",25,True),("weight","Poids",20,False),("capacity","Capacité utile",20,False),("suction","Aspiration",20,False),("workflow","Usage chantier",15,False)],
        "scores": {"karcher-wd3":[10,10,9,8,7],"bosch-gas18":[10,9,6,7,9],"festool-ctm-midi-ac":[8,5,8,9,10]},
        "answer": "Pour un petit aspirateur simple et facile à déplacer, le <strong>Kärcher WD 3 V-17/4/20</strong> offre le meilleur compromis : 4,5 kg et 17 L. Le <strong>Bosch GAS 18V-10 L</strong> gagne si le sans-fil est prioritaire. Le <strong>Festool CTM MIDI I AC</strong> vise le professionnel qui veut classe M dans un format compact.",
        "decision": "Compact ne signifie pas uniquement léger. La longueur du flexible, le rangement, la taille de cuve et la fréquence de vidage changent l'expérience. Pour les poussières nécessitant une classe M, la priorité à la sécurité peut aussi justifier un appareil plus lourd.",
    },
}

CONFIDENCE = {"VERIFIED": 1.0, "SUPPORTED": .95, "INFERRED": .85}

def score_page(cfg):
    results = []
    for pid in cfg["products"]:
        raw = adj = 0.0
        hard_fail = False
        for (criterion, label, weight, hard), value in zip(cfg["criteria"], cfg["scores"][pid]):
            evidence = "VERIFIED" if criterion in {"suction","capacity","classm","cordless","safety","wetdry","weight"} else "INFERRED"
            raw += value * weight / 10
            adj += value * weight / 10 * CONFIDENCE[evidence]
            if hard and value < 5:
                hard_fail = True
        results.append({"product_id": pid, "raw_score": round(raw,2), "confidence_adjusted_score": round(adj,2), "hard_gate_failed": hard_fail})
    return sorted(results, key=lambda x: (x["hard_gate_failed"], -x["confidence_adjusted_score"]))

def data_record(slug, cfg):
    evidence = []
    scores = {}
    for pid in cfg["products"]:
        p = PRODUCTS[pid]
        evidence.append({"product": pid, "criterion": "product_identity", "claim": p["facts"], "value": p["facts"], "source": p["source"], "source_date": "2026-09-08", "evidence_class": "VERIFIED"})
        scores[pid] = {}
        for (criterion, label, weight, hard), value in zip(cfg["criteria"], cfg["scores"][pid]):
            cls = "VERIFIED" if criterion in {"suction","capacity","classm","cordless","safety","wetdry","weight"} else "INFERRED"
            scores[pid][criterion] = {"score": value, "evidence_class": cls, "justification": f"Score attribué à partir des caractéristiques officielles de {p['name']} et de leur adéquation à l'intention « {cfg['query']} ». Le score est éditorial et non un résultat de laboratoire."}
    return {
        "slug": slug, "url": f"/comparatifs/{slug}/", "updated_at": "2026-09-08",
        "intent": {"query": cfg["query"], "type": cfg["type"], "user_job": cfg["job"], "primary_constraint": cfg["constraint"]},
        "product_universe": [{"id": pid, "name": PRODUCTS[pid]["name"], "status": "ELIGIBLE", "equivalence": "FUNCTIONALLY_COMPARABLE", "exclusion_reason": None} for pid in cfg["products"]],
        "criteria": [{"id": c, "label": l, "weight": w, "hard_gate": h, "hard_gate_min": 5 if h else None, "rationale": f"Critère retenu avant calcul car il change la décision pour {cfg['query']}."} for c,l,w,h in cfg["criteria"]],
        "evidence": evidence, "scores": scores,
        "ranking": score_page(cfg),
        "notes": {"total_solution_cost_required": slug == "aspirateur-chantier-sans-fil", "affiliate_commission_used_in_ranking": False, "desk_research_only": True}
    }

def table_html(cfg, ranking):
    rows = []
    for i, r in enumerate(ranking, 1):
        p = PRODUCTS[r["product_id"]]
        rows.append(f"<tr><td><strong>{i}. {escape(p['name'])}</strong></td><td>{r['confidence_adjusted_score']:.1f}/100</td><td>{escape(p['best'])}</td><td>{escape(p['limit'])}</td></tr>")
    return '<div class="table-wrap"><table><thead><tr><th>Modèle</th><th>Score ajusté</th><th>À privilégier pour</th><th>Limite principale</th></tr></thead><tbody>' + "".join(rows) + "</tbody></table></div>"

def product_block(pid, rank, score, cfg):
    p = PRODUCTS[pid]
    return f"""
<h3>{rank}. {escape(p['name'])}</h3>
<p><strong>Pourquoi il est classé ici.</strong> {escape(p['name'])} se distingue dans ce comparatif par son adéquation à l'intention « {escape(cfg['query'])} ». Les données fabricant que nous avons retenues sont les suivantes : {escape(p['facts'])}. Ces chiffres servent à comparer des ordres de grandeur et des fonctions, pas à simuler un essai que nous n'avons pas réalisé.</p>
<p>Son meilleur terrain est {escape(p['best'])}. Sa limite déterminante est claire : {escape(p['limit'])}. C'est précisément ce point qui peut faire préférer le modèle classé juste après, même avec un score global inférieur. Le score ajusté de <strong>{score:.1f}/100</strong> rend l'arbitrage lisible, mais ne doit pas être lu comme une mesure scientifique.</p>
<p><a href="{p['local']}">Voir la page liée à {escape(p['name'])}</a> ou consulter la <a href="{p['source']}" rel="nofollow noopener">source fabricant</a>.</p>
"""

def article_html(slug, cfg):
    ranking = score_page(cfg)
    criteria_li = "".join(f"<li><strong>{escape(label)}</strong> : {weight} %{' — critère éliminatoire' if hard else ''}.</li>" for _,label,weight,hard in cfg["criteria"])
    blocks = "".join(product_block(r["product_id"], i, r["confidence_adjusted_score"], cfg) for i,r in enumerate(ranking,1))
    guide_links = {
        "aspirateur-classe-m": [("Classes L, M et H","/guides/classes-l-m-h/"),("Décolmatage automatique","/guides/decolmatage-automatique/"),("Plâtre","/usages/aspirateur-platre/")],
        "aspirateur-chantier-puissant": [("Débit d'air","/guides/debit-air-aspirateur/"),("Dépression et mbar","/guides/depression-kpa-mbar-air-watt/"),("Puissance d'aspiration","/guides/puissance-aspiration/")],
        "aspirateur-chantier-sans-fil": [("Comment choisir","/guides/comment-choisir-aspirateur-de-chantier/"),("Atelier","/usages/aspirateur-atelier/"),("Bosch","/marques/bosch/")],
    }.get(slug, [("Comment choisir un aspirateur de chantier","/guides/comment-choisir-aspirateur-de-chantier/"),("Classes L, M et H","/guides/classes-l-m-h/"),("Décolmatage automatique","/guides/decolmatage-automatique/")])
    links = " ".join(f'<a href="{u}">{escape(t)}</a>' for t,u in guide_links)
    sources = "".join(f'<li><a href="{PRODUCTS[pid]["source"]}" rel="nofollow noopener">{escape(PRODUCTS[pid]["name"])} — documentation fabricant</a></li>' for pid in cfg["products"])
    return f"""
<!-- COMPARISON_CONTENT_START -->
<div class="answer-box"><p>{cfg['answer']}</p></div>

<h2 id="classement">Notre classement 2026</h2>
<p>{escape(cfg['decision'])}</p>
{table_html(cfg, ranking)}
<p>Le classement est construit à partir de critères définis avant le calcul. Nous ne modifions pas les poids pour faire gagner un modèle et aucune commission d'affiliation n'entre dans le score. Lorsqu'un critère est un <em>hard gate</em>, un produit qui échoue ce seuil ne peut pas remonter grâce à une bonne moyenne ailleurs.</p>

<h2 id="methode">Notre méthode de comparaison</h2>
<p>Cette page repose sur une <strong>recherche documentaire</strong> : fiches fabricants actuelles, caractéristiques techniques et adéquation aux usages. Nous n'avons pas réalisé de test physique de ces appareils et nous ne présentons donc jamais une déduction comme une expérience directe. Le job à résoudre ici est : {escape(cfg['job'])}. La contrainte principale est : {escape(cfg['constraint'])}.</p>
<ul>{criteria_li}</ul>
<p>Les caractéristiques mesurées ou annoncées par les marques reçoivent une preuve « vérifiée » lorsqu'elles viennent d'une source primaire. L'interprétation de l'intérêt pratique reçoit une confiance plus faible, car elle reste un jugement éditorial. Cette pénalité explique pourquoi le score ajusté peut être inférieur au score brut.</p>

<h2 id="modeles">Les modèles retenus et pourquoi</h2>
{blocks}

<h2 id="choisir">Ce qui change réellement le choix</h2>
<p>Commencez par le matériau et le type de déchet. Une forte dépression aide à soulever des débris lourds, tandis qu'un débit élevé est utile pour transporter rapidement poussières, copeaux et saletés dans le flexible. Les deux valeurs ne sont pas interchangeables. Surtout, elles sont souvent données à la turbine : comparer deux appareils reste utile si le point de mesure est similaire, mais cela ne prédit pas exactement la performance au bout d'un flexible, d'un adaptateur ou d'un outil.</p>
<p>Ensuite, regardez le filtre en situation réelle. Sur une poussière fine, un aspirateur puissant peut perdre rapidement de son intérêt si le filtre se charge et doit être nettoyé à la main. Le décolmatage automatique prend donc davantage de poids sur les pages professionnelles, classe M ou « puissant » que sur un simple comparatif de nettoyage eau/poussière.</p>
<p>Enfin, ne réduisez pas le coût à l'appareil nu. Les sacs, filtres, batteries, chargeurs et accessoires de raccordement peuvent changer le coût de la solution. C'est particulièrement vrai en sans-fil : posséder déjà la bonne plateforme de batteries peut inverser le choix entre deux produits proches.</p>

<h2 id="limites">Limites, sécurité et cas où ce classement ne suffit pas</h2>
<p>Une note globale n'annule pas les règles de sécurité. La classe L, M ou H doit être choisie selon le risque, la poussière, la valeur limite d'exposition et les règles applicables au travail réalisé. Un aspirateur eau/poussière grand public n'est pas transformé en aspirateur de sécurité parce que son débit ou sa dépression est supérieur. Pour approfondir ce point, consultez notre <a href="/guides/classes-l-m-h/">guide des classes L, M et H</a>.</p>
<p>Les prix et disponibilités évoluent vite ; nous ne les intégrons donc pas comme vérité permanente dans le score. Les modèles sont vérifiés au {UPDATED}. Le classement doit être réévalué si une nouvelle génération remplace un appareil, si une caractéristique officielle change ou si l'intention de la page évolue.</p>

<h2 id="liens">Guides complémentaires</h2>
<p>{links}. Ces pages permettent de vérifier les critères techniques avant l'achat et évitent de choisir un modèle uniquement sur son nom ou sa puissance électrique.</p>

<h2 id="sources">Sources consultées</h2>
<p>Sources primaires consultées pour cette mise à jour :</p>
<ul>{sources}</ul>
<p><small>Mise à jour : {UPDATED}. Comparatif réalisé par desk research, sans prétention de test physique. Les liens affiliés éventuels n'influencent ni l'inclusion, ni les scores, ni le classement.</small></p>
<!-- COMPARISON_CONTENT_END -->
"""

def build_page(slug, cfg):
    canonical = f"/comparatifs/{slug}/"
    bc = breadcrumb(("Comparatifs", "/comparatifs/"), cfg["title"].split("—")[0].strip())
    html = content_page(cfg["title"], cfg["desc"], canonical, bc, ctype="comp", answer="", related=None)
    html = html.replace("<!-- Contenu à rédiger -->", article_html(slug, cfg))
    html = html.replace("Vérifié : MM/AAAA", f"Vérifié : {UPDATED}")
    toc = "".join(f'<a href="#{anchor}">{label}</a>' for anchor,label in [("classement","Classement"),("methode","Méthode"),("modeles","Modèles"),("choisir","Comment choisir"),("limites","Limites"),("sources","Sources")])
    html = html.replace("<!-- TOC générée -->", toc)
    return html

def main():
    out = BASE / ".content" / "comparisons"
    out.mkdir(parents=True, exist_ok=True)
    for slug, cfg in PAGES.items():
        record = data_record(slug, cfg)
        (out / f"{slug}.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        target = BASE / "comparatifs" / slug / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(build_page(slug, cfg), encoding="utf-8")
    print(f"Generated {len(PAGES)} comparison pages and data files.")

if __name__ == "__main__":
    main()
