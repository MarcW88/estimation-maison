#!/usr/bin/env python3
"""Bespoke evidence-led overrides for the 8 comparison pages still on the legacy renderer.

This script intentionally avoids a universal ranking template. Each page owns a distinct
decision architecture derived from its intent. It runs after `_generate_comparatifs.py`
so legacy output can never be the final canonical comparison output.
"""
from pathlib import Path
from html import escape
import json
import re

BASE = Path(__file__).resolve().parent
UPDATED = "09/09/2026"
UPDATED_ISO = "2026-09-09"
MODELS = json.loads((BASE / ".content/models/model-evidence.json").read_text(encoding="utf-8"))["models"]

EXTERNAL = {
    "karcher-wd7": {
        "name": "Kärcher WD 7 Control P S 30/6/35/T",
        "brand": "Kärcher",
        "dust_class": "Non classé L/M/H",
        "source": "https://www.kaercher.com/fr/home-garden/aspirateurs-eau-et-poussieres/wd-7-control-p-s-30-6-35-t-eu-iii-16283860.html",
        "local": "/marques/karcher/",
        "specs": {
            "Débit d’air max.": "80 L/s",
            "Dépression max.": "290 mbar",
            "Cuve": "30 L inox",
            "Prise outil": "Oui",
            "Nettoyage du filtre": "Par impulsion à la demande",
            "Poids sans accessoires": "8,7 kg",
            "Eau + poussière": "Oui",
        },
    },
    "festool-ctm-midi-ac": {
        "name": "Festool CTM MIDI I AC",
        "brand": "Festool",
        "dust_class": "M",
        "source": "https://www.festool.fr/produits/aspirateurs/aspirateurs-compact/578552---ctm-midi-i-ac",
        "local": "/marques/festool/",
        "specs": {
            "Classe": "M",
            "Réservoir / sac filtre": "15 / 12,5 L",
            "Débit max.": "3 700 L/min (≈61,7 L/s)",
            "Dépression max.": "24 000 Pa",
            "Décolmatage": "AUTOCLEAN",
            "Prise outil": "Oui",
            "Poids": "11,8 kg",
        },
    },
    "bosch-gas-18v-12-mc": {
        "name": "Bosch Professional GAS 18V-12 MC",
        "brand": "Bosch Professional",
        "dust_class": "M",
        "source": "https://www.bosch-professional.com/be/fr/products/gas-18v-12-mc-06019K2000",
        "local": "/marques/bosch/",
        "specs": {
            "Batterie": "18 V Professional / AMPShare",
            "Classe": "M",
            "Débit max. (turbine)": "30 L/s",
            "Dépression max. (turbine)": "170 mbar",
            "Cuve": "12 L brut / 8 L net / 6 L eau",
            "Nettoyage du filtre": "SFC semi-automatique",
            "Auto-Start": "Via module GCT 30-42",
            "Poids sans batterie": "7 kg",
        },
    },
    "dewalt-dcv586m": {
        "name": "DeWalt DCV586M",
        "brand": "DeWalt",
        "dust_class": "M",
        "source": "https://www.dewalt.fr/fr-fr/produit/dcv586mn-xj/aspirateur-tstak-xr-flexvolt-54v-brushless-eau-et-poussieres-classe-m",
        "local": "/marques/dewalt/",
        "specs": {
            "Batterie": "XR FLEXVOLT 54 V",
            "Classe": "M",
            "Filtration": "Double filtre HEPA",
            "Nettoyage du filtre": "Automatique toutes les 30 s",
            "Activation": "Télécommande sans fil",
            "Eau + poussière": "Oui",
            "Rangement": "Compatible TSTAK",
        },
    },
    "karcher-ivc60m": {
        "name": "Kärcher IVC 60/24-2 Tact² M",
        "brand": "Kärcher",
        "dust_class": "M",
        "source": "https://www.kaercher.com/be-fr/professional/solutions-industrielles-aspiration-et-depoussierage/aspirateurs-industriels/aspirateurs-industriels-solides-poussieres/ivc-60-24-2-tact2-m-15761050.html",
        "local": None,
        "specs": {
            "Alimentation": "220–240 V monophasé",
            "Puissance": "2,4 kW",
            "Classe": "M",
            "Débit": "148 L/s",
            "Dépression": "254 mbar",
            "Cuve": "60 L inox",
            "Décolmatage": "Tact² automatique",
            "Poids": "60 kg",
        },
    },
    "karcher-ivr60m": {
        "name": "Kärcher IVR 60/30 Sc M ACD",
        "brand": "Kärcher",
        "dust_class": "M",
        "source": "https://www.kaercher.com/be-fr/professional/solutions-industrielles-aspiration-et-depoussierage/aspirateurs-industriels/aspirateurs-industriels-solides-poussieres/ivr-60-30-sc-m-acd-99906430.html",
        "local": None,
        "specs": {
            "Alimentation": "400 V triphasé",
            "Puissance": "3 kW",
            "Classe": "M",
            "Débit": "88 L/s",
            "Dépression": "260 mbar",
            "Cuve": "60 L acier",
            "Usage": "Fonctionnement continu en trois-huit",
            "Décolmatage": "Manuel par levier vibrant",
            "Poids": "142 kg",
        },
    },
    "nilfisk-s3-l100": {
        "name": "Nilfisk S3 L100 LC",
        "brand": "Nilfisk",
        "dust_class": "Famille certifiée L/M/H selon version",
        "source": "https://www.nilfisk.com/fr-fr/professionnel/produits/aspirateurs-industriels/poussiere-dangereuse/monophase/s3-l100-lc%2B4010300177/",
        "local": None,
        "specs": {
            "Type": "Aspirateur industriel monophasé",
            "Puissance": "3 kW",
            "Filtration": "Versions certifiées L/M/H",
            "Nettoyage du filtre": "Secouage manuel ou électrique",
            "Option": "HEPA 14 disponible",
        },
    },
    "nilfisk-vho200": {
        "name": "Nilfisk VHO200",
        "brand": "Nilfisk",
        "dust_class": "Usage industriel huile/copeaux",
        "source": "https://www.nilfisk.com/fr-fr/professionnel/produits/aspirateurs-industriels/huile-et-copeaux/vho200%2B4010400037/",
        "local": None,
        "specs": {
            "Usage": "Collecte d’huile, liquides et copeaux",
            "Capacité liquides": "75 L",
            "Séparation": "Panier à copeaux",
            "Vidange": "Vanne de répartition / soufflage",
            "Option": "Filtre brouillard d’huile",
        },
    },
}

def product(pid):
    if pid in MODELS:
        d = dict(MODELS[pid])
        d["local"] = f"/modeles/{pid}/"
        return d
    return EXTERNAL[pid]

def fact_text(pid, limit=6):
    d = product(pid)
    specs = d.get("specs", {})
    items = [f"{k} : {v}" for k, v in specs.items()]
    return " · ".join(items[:limit])

def product_link(pid):
    d = product(pid)
    target = d.get("local") or d["source"]
    attrs = "" if d.get("local") else ' rel="nofollow noopener" target="_blank"'
    return f'<a href="{escape(target)}"{attrs}>{escape(d["name"])}</a>'

def source_box(ids):
    seen = set()
    lis = []
    for pid in ids:
        if pid in seen:
            continue
        seen.add(pid)
        d = product(pid)
        lis.append(
            f'<li><a href="{escape(d["source"])}" rel="nofollow noopener" target="_blank">'
            f'{escape(d["brand"])} — {escape(d["name"])}</a></li>'
        )
    return (
        '<div class="related-box"><strong>Sources primaires consultées</strong><ul>'
        + "".join(lis)
        + "</ul></div>"
    )

def write_ledger(slug, query, page_type, user_job, constraint, boundary, ids, criteria, recs, exclusions=None, measurement_notes=None):
    universe = []
    evidence = []
    for pid in ids:
        d = product(pid)
        universe.append({
            "id": pid,
            "name": d["name"],
            "brand": d["brand"],
            "status": "ELIGIBLE",
            "role": next((r["scenario"] for r in recs if r["product_id"] == pid), "Reference"),
            "source": d["source"],
        })
        evidence.append({
            "product": pid,
            "criterion": "product_identity_and_role",
            "claim": fact_text(pid),
            "source": d["source"],
            "source_date": UPDATED_ISO,
            "evidence_class": "VERIFIED",
        })
    ledger = {
        "slug": slug,
        "url": f"/comparatifs/{slug}/",
        "updated_at": UPDATED_ISO,
        "status": "REWRITTEN_AFTER_CLUSTER_AUDIT",
        "intent": {
            "query": query,
            "type": page_type,
            "user_job": user_job,
            "primary_constraint": constraint,
            "boundary": boundary,
        },
        "scope": {
            "selection_rule": "références représentatives choisies pour couvrir les décisions qui changent réellement le choix ; pas de census exhaustif ni de ranking universel",
            "candidates": universe,
            "major_exclusions": exclusions or [],
        },
        "product_universe": universe,
        "criteria": [{"id": cid, "label": label} for cid, label in criteria],
        "evidence": evidence,
        "recommendation_logic": recs,
        "measurement_notes": measurement_notes or [],
        "notes": {
            "scoring_used": False,
            "affiliate_commission_used_in_ranking": False,
            "desk_research_only": True,
            "noindex_during_rollout": False,
            "hands_on_test": False,
        },
    }
    target = BASE / ".content" / "comparisons" / f"{slug}.json"
    target.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def replace_once(pattern, repl, text, flags=0, label="pattern"):
    out, count = re.subn(pattern, repl, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"{label}: expected one replacement, got {count}")
    return out

def render_page(slug, title, desc, h1, lead, body, toc):
    path = BASE / "comparatifs" / slug / "index.html"
    html = path.read_text(encoding="utf-8")
    html = replace_once(r"<title>.*?</title>", f"<title>{escape(title)}</title>", html, flags=re.S, label=f"{slug} title")
    html = replace_once(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{escape(desc)}">', html, label=f"{slug} desc")
    html = replace_once(r'<h1[^>]*>.*?</h1>', f'<h1 style="margin-top:10px;">{escape(h1)}</h1>', html, flags=re.S, label=f"{slug} h1")
    html = replace_once(r'<p class="lead">.*?</p>', f'<p class="lead">{escape(lead)}</p>', html, flags=re.S, label=f"{slug} lead")
    html = replace_once(
        r"<!-- COMPARISON_CONTENT_START -->.*?<!-- COMPARISON_CONTENT_END -->",
        "<!-- COMPARISON_CONTENT_START -->\n" + body.strip() + "\n<!-- COMPARISON_CONTENT_END -->",
        html,
        flags=re.S,
        label=f"{slug} comparison content",
    )
    toc_html = "".join(f'<a href="#{anchor}">{escape(label)}</a>' for anchor, label in toc)
    html = replace_once(r'<nav class="toc-list">.*?</nav>', f'<nav class="toc-list">{toc_html}</nav>', html, flags=re.S, label=f"{slug} toc")
    html = html.replace("Vérifié : 08/09/2026", f"Vérifié : {UPDATED}")
    path.write_text(html, encoding="utf-8")

def table(headers, rows):
    head = "".join(f"<th>{escape(h)}</th>" for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="table-wrap"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'

industrial_ids = ["karcher-ivc60m", "karcher-ivr60m", "nilfisk-s3-l100", "nilfisk-vho200"]
industrial_recs = [
    {"scenario": "Nettoyage mobile de machines et zones de production avec poussières M", "product_id": "karcher-ivc60m", "why": "Monophasé, 60 L, Tact² automatique et vraie architecture industrielle mobile.", "main_tradeoff": "60 kg : ce n’est déjà plus un aspirateur de chantier à déplacer dans des escaliers."},
    {"scenario": "Fonctionnement continu / process en triphasé", "product_id": "karcher-ivr60m", "why": "Moteur triphasé, compresseur à canal latéral et usage continu en trois-huit.", "main_tradeoff": "142 kg et 400 V : logique d’installation/process, pas de mobilité chantier classique."},
    {"scenario": "Poussières dangereuses avec famille industrielle configurable", "product_id": "nilfisk-s3-l100", "why": "Famille industrielle monophasée avec versions L/M/H et options de filtration.", "main_tradeoff": "La configuration exacte doit être vérifiée : une famille L/M/H ne signifie pas qu’une même référence couvre toutes les classes."},
    {"scenario": "Huiles, liquides et copeaux", "product_id": "nilfisk-vho200", "why": "Architecture dédiée à la séparation liquides/copeaux et à la vidange de 75 L.", "main_tradeoff": "Ce profil n’est pas un aspirateur de poussières fines de sécurité et ne doit pas être comparé comme tel."},
]
write_ledger(
    "aspirateur-industriel", "aspirateur industriel", "best_for_process",
    "identifier le type d’aspirateur industriel adapté au process : poussières, fonctionnement continu, huiles/copeaux ou exigences de filtration",
    "ne pas confondre grande cuve de chantier et machine industrielle conçue pour production/process",
    "les NT, GAS et CT de chantier restent des aspirateurs professionnels mobiles ; ils ne sont pas des pairs automatiques des familles IVC/IVR/S3/VHO",
    industrial_ids,
    [("process","Type de process et matière"),("duty","Cycle de service / continu"),("power","Alimentation mono ou triphasée"),("dust","Classe/filtration documentée"),("emptying","Vidage et collecte")],
    industrial_recs,
    exclusions=[
        {"name":"Kärcher NT 50/1 Tact Te M ACD","reason":"grande capacité professionnelle, mais gamme NT eau/poussière de chantier distincte des familles industrielles IVC/IVR"},
        {"name":"Bosch GAS 55 M AFC","reason":"aspirateur de chantier classe M grande cuve ; ne représente pas à lui seul l’intention process/industrielle"},
    ],
)
industrial_rows = [[f"<strong>{escape(r['scenario'])}</strong>", product_link(r["product_id"]), escape(product(r["product_id"])["dust_class"]), escape(r["why"])] for r in industrial_recs]
industrial_body = f"""
<div class="answer-box"><p><strong>Un aspirateur industriel n’est pas simplement un aspirateur de chantier avec une cuve plus grande.</strong> Le bon choix dépend d’abord du process : nettoyage de machines, aspiration continue, poussières dangereuses, huiles ou copeaux. Dès qu’on parle de triphasé, fonctionnement en trois-huit, séparation de liquides ou intégration stationnaire, on change réellement d’univers produit.</p></div>
<h2 id="frontiere">Où commence réellement l’aspiration industrielle ?</h2>
<p>Les aspirateurs professionnels de chantier comme les NT, GAS ou CT restent mobiles et centrés sur l’outil, le nettoyage et les poussières de chantier. Les familles industrielles ajoutent d’autres contraintes : fonctionnement continu, moteurs triphasés ou à canal latéral, collecte de process, vidage spécifique, usage stationnaire et configurations pour matières particulières.</p>
<h2 id="process">Quatre profils industriels qui ne demandent pas la même machine</h2>
{table(["Process", "Référence repère", "Classe / rôle", "Pourquoi"], industrial_rows)}
<h2 id="continu">Le cycle de service compte plus que la taille de cuve</h2>
<p>Le Kärcher IVR 60/30 Sc M ACD est documenté pour un fonctionnement continu en trois-huit avec alimentation 400 V et moteur à canal latéral. Le IVC 60/24-2 Tact² M reste monophasé et plus mobile. Deux cuves de 60 L peuvent donc répondre à des contraintes totalement différentes.</p>
<h2 id="matieres">Poussières, copeaux et liquides : ne mélangez pas les architectures</h2>
<p>Le Nilfisk S3 L100 illustre une famille tournée vers les poussières dangereuses et la filtration configurable. Le VHO200 est au contraire pensé pour les huiles, liquides et copeaux avec panier séparateur. Un classement unique entre ces deux profils serait artificiel.</p>
<h2 id="atex">ACD, classe M et ATEX ne sont pas des synonymes</h2>
<p>Une classe M décrit une exigence de filtration de l’appareil ; ACD concerne la collecte de poussières combustibles selon le cadre documenté par le fabricant ; une compatibilité ATEX ou zone explosive doit être explicitement certifiée pour la référence et la zone concernées. Le Kärcher IVR retenu ici est par exemple présenté pour des zones sans risque d’explosion malgré sa mention ACD.</p>
<h2 id="sortie">Quand revenir vers un aspirateur de chantier professionnel ?</h2>
<p>Si votre besoin est surtout de raccorder une ponceuse, une scie ou un perforateur, de déplacer l’appareil de pièce en pièce et de travailler en classe L ou M, utilisez plutôt le <a href="/comparatifs/aspirateur-professionnel/">comparatif professionnel</a> ou le <a href="/comparatifs/aspirateur-classe-m/">comparatif classe M</a>. L’industriel commence lorsque le process lui-même devient une contrainte de dimensionnement.</p>
<h2 id="sources">Sources et méthode</h2>
<p>Comparaison documentaire de familles et références industrielles actuelles. Il ne s’agit pas d’un essai physique ni d’un dimensionnement d’installation. Pour un process industriel, le choix final doit intégrer matière, débit process, durée de fonctionnement, environnement électrique/explosif et exigences réglementaires.</p>
{source_box(industrial_ids)}
<p><small>Mise à jour : {UPDATED}. Desk research. Aucune commission d’affiliation n’influence la sélection.</small></p>
"""
render_page("aspirateur-industriel", "Aspirateur industriel : quel type de machine selon le process ? — 2026", "Comparatif 2026 des aspirateurs industriels par process : poussières, usage continu, triphasé, huiles, copeaux et filtration.", "Aspirateur industriel : quel type de machine selon le process ?", "Production, fonctionnement continu, poussières, huiles et copeaux : l’industriel ne se résume pas à une grande cuve.", industrial_body, [("frontiere","Industriel ou chantier ?"),("process","4 profils"),("continu","Cycle de service"),("matieres","Matières"),("atex","ACD / ATEX"),("sortie","Quand sortir"),("sources","Sources")])

power_ids = ["karcher-wd7", "karcher-nt-30-1-tact", "bosch-gas-35-m-afc", "makita-vc4210mx"]
power_recs = [
    {"scenario":"Nettoyage/gravats avec maxima élevés publiés", "product_id":"karcher-wd7", "why":"80 L/s et 290 mbar annoncés par Kärcher, avec 30 L et usage eau/poussière.", "main_tradeoff":"Pas de classe L/M/H documentée ; ces chiffres ne remplacent pas une exigence de sécurité poussière."},
    {"scenario":"Poussières fines classe M + maintien du débit", "product_id":"karcher-nt-30-1-tact", "why":"74 L/s, 273 mbar, classe M et Tact commandé par capteur.", "main_tradeoff":"Plus lourd et professionnel ; le gain vient surtout de l’ensemble filtration/décolmatage, pas d’un podium de mbar."},
    {"scenario":"Classe M avec données explicitement à la turbine", "product_id":"bosch-gas-35-m-afc", "why":"74 L/s et 254 mbar à la turbine avec AFC.", "main_tradeoff":"Le point de mesure est explicitement la turbine : ne pas le comparer naïvement à une valeur publiée dans un autre contexte."},
    {"scenario":"Gros volume M avec InfiniClean", "product_id":"makita-vc4210mx", "why":"75 L/s, 250 mbar, 42 L et InfiniClean.", "main_tradeoff":"16 kg sans câble ; puissance utile et mobilité ne vont pas toujours ensemble."},
]
write_ledger("aspirateur-chantier-puissant", "aspirateur chantier puissant", "feature_specific", "comprendre ce qui rend un aspirateur réellement performant pour le déchet et le workflow plutôt que chercher un chiffre unique", "séparer débit, dépression, point de mesure, filtration et maintien des performances", "la page générale choisit par usage ; cette page explique la performance d’aspiration et les limites de comparabilité", power_ids, [("airflow","Débit d’air et contexte de mesure"),("vacuum","Dépression et contexte de mesure"),("filter","Maintien du débit filtre chargé"),("dust","Classe / nature des poussières"),("hose","Flexible, diamètre et pertes")], power_recs, measurement_notes=["Bosch publie les maxima du GAS 35 M AFC à la turbine.", "Kärcher et Makita publient des maxima fabricant qui ne sont pas assimilés automatiquement à un même protocole de mesure.", "Aucun score cross-brand de puissance n’est calculé lorsque l’équivalence de mesure n’est pas démontrée."])
power_rows = [[product_link(pid), escape(product(pid).get("specs",{}).get("Débit d’air max.", product(pid).get("specs",{}).get("Débit d’air", product(pid).get("specs",{}).get("Débit max. (turbine)", product(pid).get("specs",{}).get("Débit","—"))))), escape(product(pid).get("specs",{}).get("Dépression max.", product(pid).get("specs",{}).get("Dépression", product(pid).get("specs",{}).get("Dépression max. (turbine)","—")))), escape(product(pid)["dust_class"])] for pid in power_ids]
power_body = f"""
<div class="answer-box"><p><strong>Il n’existe pas de classement fiable du “plus puissant” à partir d’un seul chiffre constructeur.</strong> Débit et dépression décrivent deux choses différentes, et leur valeur dépend aussi du point de mesure. Pour choisir, partez du déchet à déplacer puis vérifiez si les mesures comparées sont réellement équivalentes.</p></div>
<h2 id="deux-mesures">Débit et dépression : deux forces différentes</h2><p>La dépression aide à vaincre une résistance et à soulever des déchets lourds ; le débit déplace un volume d’air utile au transport de poussières et copeaux. Une machine peut être forte sur l’un sans dominer l’autre. Les watts électriques ne remplacent aucune de ces deux mesures.</p>
<h2 id="chiffres">Ce que publient les fabricants sur quatre références</h2>{table(["Référence", "Débit annoncé", "Dépression annoncée", "Classe"], power_rows)}<p>Ce tableau expose les valeurs, mais <strong>ne crée volontairement pas de podium</strong>. Bosch précise par exemple “à la turbine” sur le GAS 35 M AFC. Sans démonstration d’un protocole et d’un point de mesure équivalents, un écart de quelques L/s ou mbar ne justifie pas un classement scientifique.</p>
<h2 id="charge">La puissance utile se juge aussi filtre chargé</h2><p>Sur poussières fines, le maintien du débit dépend fortement de la surface filtrante et du décolmatage. Tact, AFC ou InfiniClean peuvent devenir plus importants qu’un avantage de quelques mbar annoncé à filtre propre.</p>
<h2 id="scenarios">Quel profil regarder selon le travail ?</h2>{table(["Situation", "Repère", "Pourquoi"], [[f"<strong>{escape(r['scenario'])}</strong>", product_link(r["product_id"]), escape(r["why"])] for r in power_recs])}
<h2 id="limite">Quand “plus puissant” devient la mauvaise question</h2><p>Si une classe M ou H est requise, elle devient un gate avant la puissance. Pour le ponçage, l’endurance du filtre et le raccordement à l’outil peuvent dominer. Pour les liquides et gravats, cuve, vidange et diamètre du flexible prennent plus de poids. La page <a href="/guides/depression-kpa-mbar-air-watt/">kPa, mbar et Air Watts</a> détaille ces métriques.</p>
<h2 id="sources">Sources et méthode</h2><p>Desk research sur données fabricants. Les valeurs sont affichées dans leur contexte publié ; elles ne sont pas normalisées artificiellement entre marques.</p>{source_box(power_ids)}<p><small>Mise à jour : {UPDATED}. Sans test physique ni score d’affiliation.</small></p>
"""
render_page("aspirateur-chantier-puissant", "Aspirateur de chantier puissant : débit, dépression et vraies limites — 2026", "Comparatif 2026 des aspirateurs de chantier puissants : débit, dépression, point de mesure, décolmatage et limites des chiffres fabricants.", "Aspirateur de chantier puissant : que comparer vraiment ?", "Débit, dépression et maintien des performances : les gros chiffres ne sont utiles que si l’on sait ce qu’ils mesurent.", power_body, [("deux-mesures","Débit vs dépression"),("chiffres","Valeurs fabricants"),("charge","Filtre chargé"),("scenarios","Profils"),("limite","Mauvaise question ?"),("sources","Sources")])

best_ids = ["karcher-wd7","bosch-gas-18v-12-mc","karcher-nt-30-1-tact","makita-vc4210mx","bosch-advancedvac-20"]
best_recs = [
    {"scenario":"Rénovation polyvalente eau/poussière sans exigence de classe", "product_id":"karcher-wd7", "why":"30 L, prise outil, vidange, haut débit annoncé et fonctions orientées rénovation.", "main_tradeoff":"Aucune certification L/M/H documentée sur cette référence Home & Garden."},
    {"scenario":"Mobilité sans fil avec exigence classe M", "product_id":"bosch-gas-18v-12-mc", "why":"Classe M sur une seule batterie 18 V, Auto-Start via GCT et format compact.", "main_tradeoff":"Cuve nette 8 L et débit turbine 30 L/s : la mobilité se paie en capacité et performance brute."},
    {"scenario":"Chantier classe M polyvalent autour de 30 L", "product_id":"karcher-nt-30-1-tact", "why":"Tact automatique, prise outil, antistatique, ACD et 30 L.", "main_tradeoff":"14,2 kg et budget professionnel."},
    {"scenario":"Classe M gros volume", "product_id":"makita-vc4210mx", "why":"42 L, InfiniClean et prise outil pour les sessions longues.", "main_tradeoff":"16 kg sans câble : peu pertinent si l’aspirateur change constamment de zone."},
    {"scenario":"Atelier/bricolage compact avec outil filaire", "product_id":"bosch-advancedvac-20", "why":"20 L, démarrage avec outil et eau/poussière pour un usage DIY documenté.", "main_tradeoff":"Pas de classe L/M/H documentée."},
]
write_ledger("meilleur-aspirateur-de-chantier", "meilleur aspirateur de chantier", "best_overall", "orienter vers le bon type d’aspirateur selon le chantier et les contraintes dominantes plutôt que fabriquer un gagnant universel", "identifier d’abord le risque poussière, le besoin filaire/sans-fil, le volume et la fréquence de travail", "les pages spécialisées portent ensuite les décisions classe M, sans fil, eau/poussière, puissant, industriel ou compact", best_ids, [("dust","Risque et classe requise"),("use","Type de chantier/déchet"),("mobility","Mobilité et alimentation"),("endurance","Décolmatage / endurance"),("capacity","Capacité et vidage")], best_recs)
best_body = f"""
<div class="answer-box"><p><strong>Le meilleur aspirateur de chantier dépend du chantier.</strong> Pour de la poussière nécessitant M, un WD grand public sort du périmètre ; pour du nettoyage humide et des gravats non dangereux, un gros M peut être inutilement lourd et coûteux. La bonne page générale doit donc vous orienter vers un profil, pas imposer un vainqueur unique.</p></div>
<h2 id="choix-rapide">Choix rapide selon votre contrainte principale</h2>{table(["Votre situation", "Référence repère", "Pourquoi"], [[f"<strong>{escape(r['scenario'])}</strong>", product_link(r["product_id"]), escape(r["why"])] for r in best_recs])}
<h2 id="ordre">Le bon ordre : risque → usage → mobilité → capacité</h2><p>Commencez par la poussière et les règles applicables. Une classe nécessaire élimine les appareils non certifiés. Ensuite seulement, arbitrez eau/poussière, autonomie, prise outil, décolmatage, volume et fréquence de déplacement.</p>
<h2 id="pas-un-score">Pourquoi nous avons supprimé le score global</h2><p>Un score unique forçait à additionner des qualités qui ne compensent pas toujours leurs opposés : une classe M ne “rattrape” pas une machine trop lourde pour un technicien mobile, et 290 mbar ne transforment pas un appareil Home & Garden en aspirateur de sécurité. Nous préférons rendre les compromis visibles.</p>
<h2 id="specialises">Quand basculer vers un comparatif spécialisé</h2><ul><li><a href="/comparatifs/aspirateur-classe-m/">Classe M</a> si cette certification est déjà requise.</li><li><a href="/comparatifs/aspirateur-chantier-sans-fil/">Sans fil</a> si la batterie et l’autonomie sont centrales.</li><li><a href="/comparatifs/aspirateur-eau-poussiere/">Eau/poussière</a> pour nettoyage humide, garage et rénovation.</li><li><a href="/comparatifs/aspirateur-chantier-puissant/">Puissant</a> pour comprendre débit/dépression sans faux podium.</li><li><a href="/comparatifs/aspirateur-industriel/">Industriel</a> dès qu’on parle process, fonctionnement continu ou collecte spécialisée.</li></ul>
<h2 id="sources">Sources et méthode</h2><p>Sélection de références repères, non exhaustive, fondée sur sources fabricants et scénarios d’usage. Aucune note universelle ni commission d’affiliation n’entre dans la recommandation.</p>{source_box(best_ids)}<p><small>Mise à jour : {UPDATED}. Recherche documentaire, sans test physique.</small></p>
"""
render_page("meilleur-aspirateur-de-chantier", "Meilleur aspirateur de chantier 2026 : choisir selon le chantier", "Quel aspirateur de chantier choisir en 2026 ? Orientation par poussière, classe, mobilité, eau/poussière, capacité et rythme de travail.", "Meilleur aspirateur de chantier : lequel selon votre chantier ?", "Il n’y a pas un gagnant universel : la classe, le déchet, la mobilité et le volume changent la bonne réponse.", best_body, [("choix-rapide","Choix rapide"),("ordre","Ordre de décision"),("pas-un-score","Pourquoi pas de score"),("specialises","Comparatifs spécialisés"),("sources","Sources")])

m_ids = ["bosch-gas-18v-12-mc","festool-ctm-midi-ac","karcher-nt-30-1-tact","bosch-gas-35-m-afc","makita-vc4210mx"]
m_recs = [
    {"scenario":"Classe M sans fil / mobilité", "product_id":"bosch-gas-18v-12-mc", "why":"18 V, classe M, 12 L brut et Auto-Start via module.", "main_tradeoff":"Petite cuve et SFC semi-automatique : pas le même rythme qu’un gros filaire AFC/Tact/InfiniClean."},
    {"scenario":"Classe M compacte / écosystème Festool", "product_id":"festool-ctm-midi-ac", "why":"15 L, AUTOCLEAN et forte intégration outil dans un format compact.", "main_tradeoff":"Volume limité et intérêt maximal surtout dans un parc Festool."},
    {"scenario":"Classe M 30 L + Tact/antistatique/ACD", "product_id":"karcher-nt-30-1-tact", "why":"Tact commandé par capteur, système antistatique complet et 30 L.", "main_tradeoff":"14,2 kg ; ACD n’équivaut pas à une homologation ATEX universelle."},
    {"scenario":"Classe M 35 L + AFC", "product_id":"bosch-gas-35-m-afc", "why":"35 L brut, AFC et prise outil avec métriques turbine documentées.", "main_tradeoff":"12,4 kg et valeurs turbine à ne pas utiliser comme podium cross-brand."},
    {"scenario":"Classe M gros volume", "product_id":"makita-vc4210mx", "why":"42 L, InfiniClean, prise outil et avertisseur de débit.", "main_tradeoff":"16 kg sans câble : choix davantage orienté volume que mobilité."},
]
write_ledger("aspirateur-classe-m", "aspirateur classe M", "feature_specific", "choisir entre plusieurs aspirateurs réellement certifiés M selon mobilité, décolmatage, capacité et workflow", "la classe M est un gate d’entrée : elle n’est ni un bonus marketing ni une note globale", "la page professionnel reste plus large et peut inclure L ou M ; ici seuls les appareils documentés M entrent dans le comparatif", m_ids, [("class","Certification M"),("cleaning","Décolmatage / nettoyage filtre"),("monitor","Surveillance et fonctions de sécurité"),("mobility","Mobilité"),("capacity","Capacité / vidage"),("tool","Intégration outil")], m_recs)
m_body = f"""
<div class="answer-box"><p><strong>Sur cette page, la classe M est un prérequis, pas un score.</strong> Une fois ce gate franchi, le vrai choix se fait entre mobilité, décolmatage, capacité, surveillance du débit et intégration à l’outil. Un petit M sans fil et un 42 L InfiniClean peuvent tous les deux être pertinents, mais pas pour le même travail.</p></div>
<h2 id="gate">Ce que la classe M décide — et ce qu’elle ne décide pas</h2><p>La certification M doit correspondre au risque et aux règles applicables. Elle ne dit pas qu’un appareil est “meilleur” sur tous les autres critères. HEPA, puissance, débit et décolmatage restent des caractéristiques distinctes.</p>
<h2 id="profils">Cinq profils M réellement différents</h2>{table(["Profil", "Référence", "Pourquoi", "Limite"], [[f"<strong>{escape(r['scenario'])}</strong>", product_link(r["product_id"]), escape(r["why"]), escape(r["main_tradeoff"])] for r in m_recs])}
<h2 id="decolmatage">AFC, Tact, InfiniClean, AUTOCLEAN ou SFC : même but, rythmes différents</h2><p>Le nettoyage du filtre influence la continuité de travail, mais il ne remplace pas la certification M. Les systèmes automatiques sont surtout intéressants sur poussières fines et sessions longues ; un système semi-automatique peut rester cohérent sur un appareil mobile compact.</p>
<h2 id="volume">Le volume utile oppose mobilité et fréquence de vidage</h2><p>Entre 12, 15, 30, 35 et 42 L brut, le “meilleur” dépend de la fréquence de déplacement et du volume de déchets. Un technicien mobile gagne rarement à transporter 42 L ; un poste fixe peut au contraire perdre du temps avec une petite cuve.</p>
<h2 id="mesures">Pourquoi le débit ne tranche pas ce comparatif</h2><p>Les fabricants ne documentent pas toujours les mesures au même point. Les valeurs Bosch sont notamment publiées à la turbine. Nous n’utilisons donc pas les L/s ou mbar comme score universel entre marques.</p>
<h2 id="sources">Sources et méthode</h2><p>Seules des références documentées classe M sont retenues ici. Le matériau et l’évaluation du risque restent prioritaires ; ce comparatif ne remplace pas les règles de prévention.</p>{source_box(m_ids)}<p><small>Mise à jour : {UPDATED}. Desk research, sans test physique ni classement sponsorisé.</small></p>
"""
render_page("aspirateur-classe-m", "Aspirateur classe M : comparatif par profil 2026", "Comparatif 2026 des aspirateurs classe M : sans fil, compact, 30–35 L, gros volume, décolmatage et intégration à l’outil.", "Aspirateur classe M : lequel selon votre profil de travail ?", "La certification M est le point d’entrée ; mobilité, décolmatage et capacité départagent ensuite les machines.", m_body, [("gate","Le gate M"),("profils","5 profils"),("decolmatage","Décolmatage"),("volume","Volume"),("mesures","Mesures"),("sources","Sources")])

EXTERNAL["karcher-wd3-18"] = {"name":"Kärcher WD 3-18 S","brand":"Kärcher","dust_class":"Non classé L/M/H","source":"https://www.kaercher.com/fr/home-garden/aspirateurs-eau-et-poussieres/wd-3-18-s-avec-la-batterie-amovible-16285760.html","local":"/marques/karcher/","specs":{"Batterie":"18 V Kärcher Battery Power","Cuve":"17 L","Débit max.":"30 L/s","Dépression max.":"110 mbar","Autonomie indicative":"env. 20 min avec 5 Ah","Poids":"4,1 kg sans accessoires","Eau + poussière":"Oui"}}
cord_ids = ["bosch-gas-18v-10-l","bosch-gas-18v-12-mc","dewalt-dcv586m","karcher-wd3-18"]
cord_recs = [
    {"scenario":"Classe L légère / Professional 18 V", "product_id":"bosch-gas-18v-10-l", "why":"4,7 kg sans batterie, 10 L brut et classe L.", "main_tradeoff":"Autonomie annoncée 4 min/Ah et petite cuve."},
    {"scenario":"Classe M sur une seule batterie 18 V", "product_id":"bosch-gas-18v-12-mc", "why":"Classe M, antistatique et Auto-Start via GCT 30-42.", "main_tradeoff":"7 kg sans batterie, 8 L net et nettoyage SFC semi-automatique."},
    {"scenario":"Classe M 54 V / parc DeWalt", "product_id":"dewalt-dcv586m", "why":"FLEXVOLT 54 V, classe M, nettoyage automatique et commande à distance.", "main_tradeoff":"Coût et autonomie dépendent fortement du parc FLEXVOLT ; outil vendu sans batterie sur la variante documentée."},
    {"scenario":"Eau/poussière grand public sur batterie", "product_id":"karcher-wd3-18", "why":"17 L et usage wet/dry pour nettoyage mobile.", "main_tradeoff":"Pas de classe L/M/H documentée et performances inférieures aux gros filaires."},
]
write_ledger("aspirateur-chantier-sans-fil", "aspirateur chantier sans fil", "feature_specific", "choisir un aspirateur batterie selon classe, plateforme, autonomie, capacité et activation avec l’outil", "le voltage seul ne permet pas de comparer les systèmes ; la plateforme et la classe peuvent éliminer un candidat", "la page généraliste traite tous les types d’alimentation ; ici la contrainte sans-fil est centrale", cord_ids, [("class","Classe / risque poussière"),("platform","Plateforme batterie"),("runtime","Autonomie documentée"),("capacity","Capacité"),("tool","Activation / workflow outil"),("weight","Poids")], cord_recs)
cord_body = f"""
<div class="answer-box"><p><strong>Le meilleur aspirateur sans fil est d’abord celui qui correspond à votre classe de poussière et à votre parc batteries.</strong> Une batterie 54 V n’est pas automatiquement “meilleure” qu’un 18 V : classe M ou L, autonomie, poids, capacité et déclenchement avec l’outil changent davantage le workflow.</p></div>
<h2 id="profils">Quatre façons très différentes de travailler sans fil</h2>{table(["Profil", "Référence", "Pourquoi", "Compromis"], [[f"<strong>{escape(r['scenario'])}</strong>", product_link(r["product_id"]), escape(r["why"]), escape(r["main_tradeoff"])] for r in cord_recs])}
<h2 id="classe">Sans fil n’efface pas la question L/M/H</h2><p>Le GAS 18V-10 L est classe L, tandis que le GAS 18V-12 MC et le DeWalt DCV586M sont documentés classe M. Le Kärcher WD 3-18 S est un wet/dry grand public sans classe L/M/H documentée. Ces appareils ne sont donc pas interchangeables dès qu’une classe précise est requise.</p>
<h2 id="batteries">La plateforme batterie est une partie du prix et de l’autonomie</h2><p>Un aspirateur nu peut sembler compétitif alors que batteries et chargeur représentent une part majeure du système. À l’inverse, posséder déjà des batteries Bosch Professional/AMPShare, DeWalt FLEXVOLT ou Kärcher Battery Power peut inverser la décision.</p>
<h2 id="autonomie">Comparez l’autonomie avec la méthode annoncée</h2><p>Bosch publie 4 min/Ah sur le GAS 18V-10 L ; Kärcher annonce environ 20 minutes avec 5 Ah sur le WD 3-18 S. Ces formats ne sont pas identiques et les niveaux d’aspiration, batteries et conditions de travail influencent le résultat. Nous refusons de convertir ces chiffres en score commun sans protocole équivalent.</p>
<h2 id="outil">Déclenchement avec l’outil : prise, module ou télécommande</h2><p>Sans prise secteur, le workflow change. Bosch utilise notamment le module GCT 30-42 sur le GAS 18V-12 MC ; DeWalt fournit une télécommande d’activation. Ce détail peut être plus important qu’un petit écart de débit pour le ponçage ou le perçage.</p>
<h2 id="sources">Sources et méthode</h2><p>Références choisies pour représenter des systèmes batterie et classes différentes, pas pour produire un podium universel.</p>{source_box(cord_ids)}<p><small>Mise à jour : {UPDATED}. Recherche documentaire, sans test physique.</small></p>
"""
render_page("aspirateur-chantier-sans-fil", "Aspirateur de chantier sans fil : comparatif par plateforme 2026", "Comparatif 2026 des aspirateurs de chantier sans fil : Bosch 18 V, classe M, DeWalt FLEXVOLT, Kärcher, autonomie et workflow outil.", "Aspirateur de chantier sans fil : lequel selon votre plateforme ?", "Classe L/M, batteries, autonomie, poids et déclenchement : le voltage seul ne suffit pas.", cord_body, [("profils","4 profils"),("classe","Classes"),("batteries","Batteries"),("autonomie","Autonomie"),("outil","Workflow outil"),("sources","Sources")])

wet_ids = ["karcher-wd7","karcher-wd6","bosch-advancedvac-20","nilfisk-multi-ii-30-t"]
wet_recs = [
    {"scenario":"Rénovation 30 L très équipée", "product_id":"karcher-wd7", "why":"30 L, bouchon de vidange, prise outil, contrôle du filtre et hautes valeurs annoncées.", "main_tradeoff":"Pas de classe L/M/H documentée."},
    {"scenario":"30 L simple avec prise outil", "product_id":"karcher-wd6", "why":"Cuve inox 30 L, prise asservie et nettoyage du filtre par bouton.", "main_tradeoff":"Nettoyage manuel, pas Tact/AFC ; pas de classe de sécurité documentée."},
    {"scenario":"Atelier bricolage 20 L", "product_id":"bosch-advancedvac-20", "why":"20 L, démarrage avec outil, vidange d’eau et tuyau antistatique.", "main_tradeoff":"Positionnement DIY et pas de classe L/M/H documentée."},
    {"scenario":"Grand public 30 L hors Kärcher", "product_id":"nilfisk-multi-ii-30-t", "why":"30 L, wet/dry et gamme grand public dédiée garage/atelier.", "main_tradeoff":"Options variant selon suffixe et pas de classe L/M/H documentée sur la fiche grand public."},
]
write_ledger("aspirateur-eau-poussiere", "aspirateur eau poussière chantier", "feature_specific", "choisir un wet/dry selon vidange, capacité, prise outil et entretien sans confondre polyvalence humide/sec avec sécurité poussière", "l’aptitude eau/poussière est un gate fonctionnel ; la classe de poussière reste une décision séparée", "si la poussière exige M/H, utiliser les pages classe/sécurité plutôt qu’un comparatif grand public wet/dry", wet_ids, [("wetdry","Aptitude humide/sec"),("drain","Vidange des liquides"),("tool","Prise / démarrage outil"),("filter","Entretien du filtre"),("capacity","Capacité"),("safety","Classe documentée")], wet_recs)
wet_body = f"""
<div class="answer-box"><p><strong>Pour un aspirateur eau et poussière, regardez d’abord ce qui simplifie le passage du sec au liquide.</strong> Cuve, vidange, filtre, prise outil et entretien comptent davantage qu’un score général. Et “eau/poussière” ne signifie jamais automatiquement “aspirateur de sécurité”.</p></div>
<h2 id="situations">Quatre profils wet & dry</h2>{table(["Usage", "Référence", "Atout", "Limite"], [[f"<strong>{escape(r['scenario'])}</strong>", product_link(r["product_id"]), escape(r["why"]), escape(r["main_tradeoff"])] for r in wet_recs])}
<h2 id="liquides">Pour les liquides, la vidange compte autant que la puissance</h2><p>Une grosse cuve n’est utile que si elle se vide facilement. Le WD 7 et l’AdvancedVac 20 documentent des solutions de vidange d’eau ; c’est une différence pratique pour garage, rénovation et incidents humides.</p>
<h2 id="filtre">Passer du sec à l’humide sans maltraiter le filtre</h2><p>Le type de filtre et les consignes fabricant déterminent s’il faut retirer un sac, changer une configuration ou simplement poursuivre. Le nettoyage du filtre par bouton sur WD 6/WD 7 aide à l’entretien, mais ne correspond pas à un décolmatage automatique de sécurité.</p>
<h2 id="outil">Avec un outil électroportatif, le démarrage change l’expérience</h2><p>WD 6, WD 7 et AdvancedVac 20 offrent une intégration à l’outil documentée. Pour une production régulière de poussières fines, passez toutefois à une page dédiée à la classe requise et au décolmatage.</p>
<h2 id="securite">Wet & dry n’est pas une classe de poussière</h2><p>Les quatre références retenues ici sont surtout des appareils grand public/atelier. Si votre évaluation de risque impose M ou H, le critère wet/dry devient secondaire face à la certification de l’appareil.</p>
<h2 id="sources">Sources et méthode</h2><p>Comparatif de fonctionnalités humide/sec et de workflow, sans score universel de puissance.</p>{source_box(wet_ids)}<p><small>Mise à jour : {UPDATED}. Desk research, sans test physique.</small></p>
"""
render_page("aspirateur-eau-poussiere", "Aspirateur eau et poussière de chantier : comparatif 2026", "Comparatif 2026 des aspirateurs eau et poussière : vidange, cuve, filtre, prise outil et différence avec une classe de sécurité.", "Aspirateur eau et poussière : lequel pour atelier et rénovation ?", "Humide/sec, vidange, filtre et prise outil : la polyvalence compte plus qu’un podium de puissance.", wet_body, [("situations","4 profils"),("liquides","Liquides"),("filtre","Filtre"),("outil","Outil"),("securite","Sécurité"),("sources","Sources")])

bag_ids = ["bosch-gas-18v-10-l","karcher-wd7","karcher-wd6","bosch-gas-35-m-afc"]
bag_recs = [
    {"scenario":"Conception mobile explicitement sans sac", "product_id":"bosch-gas-18v-10-l", "why":"Référence retenue historiquement pour son usage sans sac et sa compacité classe L.", "main_tradeoff":"Vidage direct plus exposant et filtre à protéger sur poussières fines ; petite cuve."},
    {"scenario":"Cuve wet/dry pour déchets grossiers / liquides", "product_id":"karcher-wd7", "why":"Wet/dry 30 L ; l’usage direct en cuve peut être pertinent selon déchet et consignes.", "main_tradeoff":"Le fabricant fournit et valorise aussi un sac filtrant : “peut fonctionner sans sac” n’est pas “optimisé sans consommable”."},
    {"scenario":"Wet/dry 30 L avec entretien manuel", "product_id":"karcher-wd6", "why":"Cuve 30 L et filtre nettoyable par bouton pour différents déchets.", "main_tradeoff":"Pour poussières fines, le sac peut rester utile à la protection du filtre et au vidage."},
    {"scenario":"Classe M / collecte contrôlée", "product_id":"bosch-gas-35-m-afc", "why":"Contre-exemple utile : sur poussières M, le mode de collecte et l’élimination sûre priment sur l’objectif “zéro sac”.", "main_tradeoff":"Chercher à éviter tout consommable peut dégrader le workflow de sécurité."},
]
write_ledger("aspirateur-chantier-sans-sac", "aspirateur chantier sans sac", "feature_specific", "comprendre quels appareils sont réellement pensés pour un usage sans sac et quand le sac reste préférable", "séparer conception sans sac, possibilité de collecte directe en cuve et gestion sûre des poussières fines", "la page wet/dry compare humide/sec ; ici le mode de collecte et ses compromis sont centraux", bag_ids, [("collection","Mode de collecte documenté"),("dust","Nature du déchet"),("filter","Protection/entretien filtre"),("emptying","Vidage et exposition"),("consumables","Consommables")], bag_recs)
bag_body = f"""
<div class="answer-box"><p><strong>“Sans sac” n’est pas une qualité absolue.</strong> Pour de l’eau, des copeaux ou certains déchets grossiers, la collecte directe en cuve peut être logique. Pour de la poussière fine, un sac peut protéger le filtre et surtout rendre le vidage plus propre. Il faut donc comparer le mode de collecte, pas seulement le prix des consommables.</p></div>
<h2 id="definitions">Trois choses différentes derrière “sans sac”</h2><ul><li><strong>Conçu explicitement sans sac</strong> : architecture où le fabricant présente le fonctionnement direct comme normal.</li><li><strong>Peut collecter en cuve</strong> : wet/dry pouvant être utilisé sans sac pour certains déchets ou liquides.</li><li><strong>Devrait utiliser un système de collecte</strong> : poussières fines/dangereuses où la protection du filtre et l’élimination comptent davantage que l’économie d’un sac.</li></ul>
<h2 id="profils">Quatre repères pour comprendre les compromis</h2>{table(["Cas", "Référence", "Lecture correcte", "Limite"], [[f"<strong>{escape(r['scenario'])}</strong>", product_link(r["product_id"]), escape(r["why"]), escape(r["main_tradeoff"])] for r in bag_recs])}
<h2 id="fines">Sur poussière fine, le sac peut être une fonction et non un défaut</h2><p>Une poussière fine charge rapidement un filtre. Le sac peut agir comme pré-collecteur, réduire l’encrassement et limiter la remise en suspension au vidage. Sur des poussières nécessitant une classe de sécurité, suivez toujours le système de collecte prévu par le fabricant.</p>
<h2 id="cout">Le coût total ne se limite pas au sac</h2><p>Économiser des sacs peut augmenter les nettoyages de filtre ou accélérer leur remplacement. Le bon calcul inclut donc filtres, temps de maintenance, propreté du vidage et nature des déchets.</p>
<h2 id="sources">Sources et méthode</h2><p>Cette page compare des modes de collecte. Elle ne présente pas tous les wet/dry comme “bagless” et ne recommande pas de supprimer un sac lorsque le fabricant ou le risque impose une autre procédure.</p>{source_box(bag_ids)}<p><small>Mise à jour : {UPDATED}. Recherche documentaire, sans test physique.</small></p>
"""
render_page("aspirateur-chantier-sans-sac", "Aspirateur de chantier sans sac : quand est-ce vraiment pertinent ? — 2026", "Guide comparatif 2026 des aspirateurs de chantier sans sac : collecte directe, filtre, vidage, poussières fines et consommables.", "Aspirateur de chantier sans sac : bonne idée ou faux avantage ?", "Collecte directe, poussière fine et vidage : éviter le sac n’est pertinent que dans certains usages.", bag_body, [("definitions","3 définitions"),("profils","4 repères"),("fines","Poussière fine"),("cout","Coût total"),("sources","Sources")])

compact_ids = ["karcher-wd2","bosch-gas-18v-10-l","bosch-gas-18v-12-mc","festool-ctl-midi"]
compact_recs = [
    {"scenario":"Petit wet/dry économique", "product_id":"karcher-wd2", "why":"15 L et 4,4 kg : simple à transporter pour petits travaux.", "main_tradeoff":"Pas de prise outil ni classe L/M/H documentée."},
    {"scenario":"Très mobile sur batterie classe L", "product_id":"bosch-gas-18v-10-l", "why":"4,7 kg sans batterie et 10 L brut.", "main_tradeoff":"6 L net et autonomie limitée."},
    {"scenario":"Compact sans fil classe M", "product_id":"bosch-gas-18v-12-mc", "why":"12 L brut, 7 kg sans batterie et certification M.", "main_tradeoff":"Plus lourd qu’un petit wet/dry et petite capacité nette."},
    {"scenario":"Compact filaire orienté outil", "product_id":"festool-ctl-midi", "why":"15 L, classe L, Bluetooth et intégration CLEANTEC/Systainer.", "main_tradeoff":"11,4 kg : “compact” décrit l’encombrement/workflow plus que le poids minimal."},
]
write_ledger("petit-aspirateur-de-chantier", "petit aspirateur de chantier", "best_for_use_case", "choisir un aspirateur réellement facile à transporter sans réduire le compact à un seuil arbitraire de litres", "combiner poids, dimensions, poignée/rangement, alimentation et capacité utile", "la page sans fil traite la batterie ; ici la priorité est l’encombrement et la manutention, filaire ou non", compact_ids, [("weight","Poids"),("dimensions","Encombrement"),("capacity","Capacité utile"),("power","Filaire / batterie"),("dust","Classe"),("handling","Transport / rangement")], compact_recs)
compact_rows = [[product_link(pid), escape(product(pid).get("specs",{}).get("Poids sans accessoires", product(pid).get("specs",{}).get("Poids sans batterie", product(pid).get("specs",{}).get("Poids","—")))), escape(product(pid).get("specs",{}).get("Cuve", product(pid).get("specs",{}).get("Réservoir / sac filtre","—"))), escape(product(pid)["dust_class"])] for pid in compact_ids]
compact_body = f"""
<div class="answer-box"><p><strong>Un petit aspirateur de chantier ne se définit pas par “moins de 15 L”.</strong> La facilité de transport dépend du poids, des dimensions, de la poignée, du rangement du flexible, de la batterie et de la capacité réellement utile. Un 15 L de 11 kg peut être compact sans être léger.</p></div>
<h2 id="definition">Notre définition du compact</h2><p>Nous regardons quatre dimensions : masse à transporter, encombrement, capacité utile et fréquence de déplacement. Le seuil de litres du vieux hub est supprimé car il excluait arbitrairement des appareils pourtant conçus comme compacts.</p>
<h2 id="reperes">Quatre références qui illustrent quatre compacités</h2>{table(["Référence", "Poids documenté", "Capacité", "Classe"], compact_rows)}
<h2 id="profils">Quel petit format selon votre travail ?</h2>{table(["Profil", "Repère", "Pourquoi", "Compromis"], [[f"<strong>{escape(r['scenario'])}</strong>", product_link(r["product_id"]), escape(r["why"]), escape(r["main_tradeoff"])] for r in compact_recs])}
<h2 id="escaliers">Escaliers, véhicule et rangement : les vrais tests pratiques</h2><p>Si l’appareil change d’étage toute la journée, quelques kilos comptent davantage qu’une grande cuve. Dans un véhicule ou un système de rangement, la géométrie et l’intégration à des coffrets peuvent compter davantage que le volume nominal.</p>
<h2 id="classe">Compact ne doit jamais faire oublier la classe</h2><p>Le WD 2 n’a pas de classe L/M/H documentée ; le GAS 18V-10 L et le CTL MIDI I sont classe L ; le GAS 18V-12 MC est classe M. Dès qu’une classe précise est requise, la taille ne peut pas compenser son absence.</p>
<h2 id="sources">Sources et méthode</h2><p>Comparatif orienté manutention et encombrement, sans seuil arbitraire de capacité ni score universel.</p>{source_box(compact_ids)}<p><small>Mise à jour : {UPDATED}. Desk research, sans test physique.</small></p>
"""
render_page("petit-aspirateur-de-chantier", "Petit aspirateur de chantier : comparatif compact 2026", "Comparatif 2026 des petits aspirateurs de chantier : poids, capacité, encombrement, classe et mobilité sans seuil arbitraire de litres.", "Petit aspirateur de chantier : lequel est vraiment facile à transporter ?", "Poids, encombrement, capacité et classe : un petit format ne se résume pas au volume de cuve.", compact_body, [("definition","Définition"),("reperes","4 références"),("profils","Profils"),("escaliers","Transport"),("classe","Classe"),("sources","Sources")])

hub = BASE / "comparatifs" / "index.html"
hub_html = hub.read_text(encoding="utf-8")
hub_html = hub_html.replace("Comparatifs basés sur des données techniques vérifiées. Chaque tableau présente les métriques réelles : dépression, débit, classe de filtration.", "Comparatifs fondés sur l’intention, les contraintes d’usage et des données fabricants vérifiées. Les pages n’utilisent un score que lorsqu’il apporte une vraie valeur à la décision.")
for old, new in {"Hub · page principale":"Orientation par usage et contrainte","Wet & dry":"Humide / sec, vidange et filtre","18V / 36V / 54V":"Plateforme, autonomie et classe","Vidage direct":"Mode de collecte et entretien","Dépression &gt; 25 kPa":"Débit et dépression contextualisés","Usage intensif":"Scénarios professionnels","Grande capacité":"Process, continu, huiles et copeaux","Poussières dangereuses modérées":"Certification classe M","&lt; 15 litres":"Mobilité et encombrement"}.items():
    hub_html = hub_html.replace(old, new)
hub.write_text(hub_html, encoding="utf-8")

print("✓ bespoke comparison overrides: 8 pages + comparison hub")
