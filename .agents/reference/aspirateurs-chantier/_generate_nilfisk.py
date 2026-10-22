#!/usr/bin/env python3
"""Evidence-led Nilfisk brand-hub generator.

Bespoke rendering layer for /marques/nilfisk/. Nilfisk is treated as a progression
from general wet/dry cleanup to professional dust extraction, with the distinction
between Push&Clean, InfiniClean and certified dust classes kept explicit.

Desk research only. Evidence checked 2026-09-11.
"""
from pathlib import Path
from html import escape
import json
import re

BASE = Path(__file__).resolve().parent
UPDATED_DISPLAY = "11/09/2026"
UPDATED_ISO = "2026-09-11"
TITLE = "Aspirateurs Nilfisk : Multi II, ATTIX, InfiniClean et classes L/M/H"
DESC = "Nilfisk : choisir entre Buddy, Multi II et ATTIX, comprendre Push&Clean, InfiniClean, FlowSensor, classes L/M/H et la différence entre filtre et certification."

SOURCES = [
    ("S1", "Nilfisk — Buddy II 18", "https://shop.nilfisk.com/fr-fr/products/buddy-ii-18-aspirateur-eau-et-poussiere", "primary"),
    ("S2", "Nilfisk — gamme Multi II", "https://shop.nilfisk.com/fr-fr/collections/multi-aspirateur-eau-poussiere", "primary"),
    ("S3", "Nilfisk — Multi II 30 T", "https://shop.nilfisk.com/fr-fr/products/multi-ii-30-t-aspirateur-eau-et-poussiere", "primary"),
    ("S4", "Nilfisk — ATTIX 33-2L IC", "https://www.nilfisk.com/fr-be/professional/produits/aspirateurs-industriels/aspirateurs-eau-et-poussiere-monophases/attix-33-2l-ic-%2B107412103/", "primary"),
    ("S5", "Nilfisk — ATTIX 44-2M IC", "https://www.nilfisk.com/fr-fr/professionnel/produits/aspirateurs-industriels/poussiere-dangereuse/monophase/attix-44-2m-ic%2B107412182/", "primary"),
    ("S6", "Nilfisk — ATTIX 44-2H IC", "https://www.nilfisk.com/fr-be/professional/produits/aspirateurs-industriels/poussiere-dangereuse/monophase/attix-44-m-h%2B107412186/", "primary"),
    ("S7", "Nilfisk — filtres et systèmes de nettoyage", "https://www.nilfisk.com/fr-fr/professionnel/pages/accessoires-aspirateurs-industriels/filtres-et-systemes-de-nettoyage-de-filtre/", "primary"),
    ("S8", "BricoZone — retours d'usage Nilfisk Multi II 30 T", "https://www.bricozone.be/t/aspirateur-nilfisk-multi-ii-30-t.105379/", "user_experience"),
]


def sources_html():
    return "".join(
        f'<li><a href="{escape(url)}" rel="nofollow noopener">{escape(label)}</a> <small>({escape(ref)})</small></li>'
        for ref, label, url, _kind in SOURCES
    )


def article():
    return f'''<!-- BRAND_CONTENT_START -->
<div class="answer-box"><p><strong>Chez Nilfisk, la décision utile n'est pas de chercher le plus gros réservoir.</strong> Il faut d'abord situer le travail sur une échelle : nettoyage eau/poussière occasionnel, atelier avec outil électroportatif, poussière fine soutenue, puis poussière exigeant une classe certifiée. Cette progression sépare assez nettement Buddy, Multi II et ATTIX — et surtout Push&amp;Clean, InfiniClean et les variantes L/M/H.</p></div>

<h2 id="deux-univers">Nilfisk couvre en réalité trois niveaux de besoin, pas seulement « grand public ou pro »</h2>
<p><strong>Buddy II</strong> reste un aspirateur eau/poussière simple pour garage, voiture et nettoyage ponctuel. <strong>Multi II</strong> ajoute davantage de capacité et, selon la version, une prise outil, un indicateur de saturation et le nettoyage semi-automatique Push&amp;Clean. <strong>ATTIX</strong> change ensuite de logique : construction professionnelle, filtration plus structurée, InfiniClean sur les versions IC et classes documentées selon la référence.</p>
<p>Le saut important n'est donc pas seulement le prix. Il correspond à la fréquence de colmatage, à la nécessité de maintenir le débit et, éventuellement, à une exigence de sécurité poussière. Un Multi II peut être très cohérent en rénovation domestique tout en restant une mauvaise réponse si le chantier exige une classe M.</p>
<p>Pour comparer hors marque, utilisez notre <a href="/comparatifs/aspirateur-eau-poussiere/">comparatif eau et poussière</a> pour les besoins généraux, puis le <a href="/comparatifs/aspirateur-professionnel/">comparatif professionnel</a> lorsque le captage devient une fonction de production.</p>

<h2 id="buddy-multi">Buddy et Multi II : le bon niveau quand le besoin reste nettoyage et bricolage</h2>
<p>Le Buddy II 18 actuel est un 18 L de 1 200 W avec fonction soufflerie, filtre mixte lavable et rangement d'accessoires. C'est une machine de nettoyage polyvalente, pas un extracteur de poussières dangereuses.</p>
<p>La gamme Multi II actuelle monte à 22 et 30 L. Sur le <strong>Multi II 30 T</strong>, Nilfisk documente une cuve de 30 L, un moteur de 1 400 W, une prise outil, un flexible de 4 m, un témoin de saturation du filtre et la fonction <strong>Push&amp;Clean</strong>. Ce dernier point est important : Nilfisk le décrit comme un nettoyage semi-automatique du filtre. Il faut donc l'opposer à un vrai système automatique qui intervient pendant le travail.</p>
<p>Pour un atelier où l'on coupe du bois de temps en temps, aspire de l'eau ou nettoie après chantier, le Multi II peut être plus rationnel qu'un ATTIX. Si l'usage principal devient le ponçage continu, la rainureuse ou une poussière fine qui colmate vite, le critère décisif bascule vers la gestion du filtre.</p>

<h2 id="pushclean-vs-ic">Push&amp;Clean et InfiniClean ne répondent pas au même rythme de travail</h2>
<p>Nilfisk distingue plusieurs systèmes de nettoyage de filtre. Dans sa documentation professionnelle, <strong>InfiniClean</strong> est décrit comme complètement automatique et autonome : il nettoie le filtre pendant que l'aspirateur fonctionne. Sur les ATTIX IC, Nilfisk indique une impulsion de 0,2 seconde toutes les 15 secondes. À l'inverse, Push&amp;Clean demande une intervention de l'utilisateur.</p>
<p>Cette différence est plus concrète que quelques watts de moteur. En aspiration de poussière fine, la productivité dépend de la capacité à éviter les interruptions et la chute de débit. C'est pourquoi notre <a href="/guides/decolmatage-automatique/">guide du décolmatage automatique</a> doit être lu avant de surpayer une cuve plus grande.</p>
<p>Un ancien retour BricoZone sur le Multi II 30 T illustre bien cette frontière : le système semi-automatique y est jugé beaucoup moins convaincant pour les séquences très poussiéreuses qu'un décolmatage automatique. Ce témoignage reste un signal d'usage, pas une mesure de performance du modèle actuel.</p>

<h2 id="infiniclean">ATTIX avec InfiniClean : la gamme où Nilfisk devient réellement un spécialiste du captage</h2>
<p>L'<strong>ATTIX 33-2L IC</strong> actuel est un bon exemple de cette logique : cuve de 30 L, InfiniClean, système antistatique et certification de filtration de classe L. Nilfisk indique aussi qu'il peut recevoir un filtre plat PTFE référencé « classe M ».</p>
<p>Cette coexistence est précisément un piège de lecture : <strong>un filtre portant une classe ne transforme pas à lui seul l'aspirateur en machine certifiée de cette classe</strong>. L'ATTIX 33-2L IC reste documenté comme classe L. Pour acheter sur une exigence réglementaire ou de prévention, il faut vérifier la certification de l'appareil complet et la référence exacte, pas seulement la cartouche montée.</p>
<p>Le même raisonnement vaut pour toutes les variantes ATTIX. Le nombre 33 ou 44 renseigne surtout la famille et la capacité ; les suffixes L, M, H, IC ou PC changent davantage la destination réelle de la machine.</p>

<h2 id="classes-attix">ATTIX M et H : FlowSensor, filtration et confinement passent devant la capacité</h2>
<p>L'<strong>ATTIX 44-2M IC</strong> est une variante classe M de 42 L. Nilfisk documente InfiniClean, un système FlowSensor avec alarme sonore et visuelle lorsque la vitesse d'air descend sous 20 m/s, la sélection du diamètre de flexible, le fonctionnement antistatique et la marche/arrêt automatique pour outils électriques.</p>
<p>Les variantes H vont plus loin dans la filtration et le confinement. Sur l'ATTIX 44-2H IC, Nilfisk documente notamment une certification H et un filtre HEPA H14. Il ne faut pas pour autant choisir H « au cas où » : la classe doit correspondre au risque réel, aux prescriptions applicables et au mode de collecte prévu.</p>
<p>Pour ce type de décision, commencez par notre <a href="/guides/classes-l-m-h/">guide des classes L/M/H</a> puis, si la classe M est pertinente, par le <a href="/comparatifs/aspirateur-classe-m/">comparatif des aspirateurs classe M</a>.</p>

<h2 id="reference-complete">Chez Nilfisk, le suffixe de référence est plus informatif que le nom ATTIX</h2>
<p>Deux ATTIX 33 peuvent partager une grande partie de leur carrosserie tout en divergeant sur la classe, le système de nettoyage du filtre, l'équipement électrique ou le kit d'accessoires. Les suffixes tels que <strong>2L, 2M, 2H, IC, PC ou MOBILE</strong> ne sont donc pas des détails commerciaux.</p>
<p>La méthode d'achat la plus sûre est de relever la référence produit complète, vérifier la classe documentée par Nilfisk, puis le système de décolmatage, la prise outil et le flexible. C'est particulièrement important en occasion ou chez un revendeur qui raccourcit le nom du produit.</p>
<p>Pour un atelier multimarque, cette neutralité peut être un avantage : l'écosystème Nilfisk se concentre sur flexibles, filtres, sacs et accessoires d'aspiration plutôt que sur une plateforme de batteries d'outillage.</p>

<h2 id="quel-nilfisk">Quel Nilfisk regarder selon le travail ?</h2>
<div class="table-wrap"><table><thead><tr><th>Besoin dominant</th><th>Point de départ</th><th>Pourquoi</th><th>À vérifier</th></tr></thead><tbody>
<tr><td>Voiture, garage, liquide, nettoyage ponctuel</td><td>Buddy II 12/18</td><td>Simple, compact, eau/poussière.</td><td>Pas de fonctions avancées de captage.</td></tr>
<tr><td>Atelier et rénovation domestique</td><td>Multi II 22/30</td><td>Plus de capacité ; prise outil selon version.</td><td>Push&amp;Clean reste semi-automatique.</td></tr>
<tr><td>Poussière fine soutenue sans exigence M</td><td>ATTIX 33-2L IC</td><td>InfiniClean, antistatique, classe L documentée.</td><td>Ne pas confondre filtre PTFE classe M et certification de la machine.</td></tr>
<tr><td>Travail nécessitant une classe M</td><td>ATTIX 44-2M IC</td><td>Classe M, FlowSensor, InfiniClean, antistatique.</td><td>Référence complète et diamètre de flexible.</td></tr>
<tr><td>Risque relevant d'une classe H</td><td>ATTIX H selon référence</td><td>Architecture et filtration dédiées.</td><td>Valider l'exigence de sécurité avant achat.</td></tr>
</tbody></table></div>
<p>En résumé, Nilfisk devient vraiment différenciant quand votre problème n'est plus « ramasser les saletés » mais <strong>maintenir une aspiration propre et stable pendant le travail</strong>. Pour les gravats et le nettoyage général, comparez aussi notre page <a href="/usages/aspirateur-gravats/">aspirateur pour gravats</a>. Pour un poste fixe ou semi-fixe, consultez <a href="/usages/aspirateur-atelier/">aspirateur d'atelier</a>.</p>
<p>Nous n'avons pas testé physiquement ces machines. Les caractéristiques et certifications retenues proviennent des pages officielles Nilfisk ; le retour communautaire sert uniquement à contextualiser la différence entre nettoyage semi-automatique et automatique.</p>

<h2 id="sources">Sources consultées</h2>
<p>Sources officielles Nilfisk consultées le {UPDATED_DISPLAY}, complétées par un retour communautaire ancien utilisé uniquement comme signal qualitatif d'usage.</p>
<ul>{sources_html()}</ul>
<p><small>Mise à jour : {UPDATED_DISPLAY}. Analyse documentaire, sans test physique. Les liens affiliés éventuels n'influencent ni les classes, ni les caractéristiques retenues, ni l'orientation éditoriale.</small></p>
<!-- BRAND_CONTENT_END -->'''


def toc_html():
    items = [
        ("deux-univers", "Les trois niveaux Nilfisk"),
        ("buddy-multi", "Buddy et Multi II"),
        ("pushclean-vs-ic", "Push&Clean vs InfiniClean"),
        ("infiniclean", "ATTIX et InfiniClean"),
        ("classes-attix", "ATTIX M et H"),
        ("reference-complete", "Lire la référence complète"),
        ("quel-nilfisk", "Quel Nilfisk ?"),
        ("sources", "Sources"),
    ]
    return "".join(f'<a href="#{escape(anchor)}">{escape(label)}</a>' for anchor, label in items)


def replace_once(pattern, replacement, text, label, flags=0):
    out, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f'{label}: expected one replacement, got {count}')
    return out


def patch_page():
    path = BASE / "marques" / "nilfisk" / "index.html"
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


def write_ledger():
    path = BASE / '.content' / 'brands' / 'nilfisk.yaml'
    obj = json.loads(path.read_text(encoding='utf-8'))
    evidence = [
        {"ref": ref, "status": "VERIFIED" if kind == "primary" else "SUPPORTED", "tier": 1 if kind == "primary" else 4, "source": url, "source_type": kind, "label": label}
        for ref, label, url, kind in SOURCES
    ]
    obj.update({
        "updated_at": UPDATED_ISO,
        "source_of_truth": "_generate_nilfisk.py",
        "structure_strategy": "bespoke_cleanup_to_certified_extraction_ladder",
        "recovery_verdict": "DEEP_REWRITE",
        "entity_map": {
            "brand": "Nilfisk",
            "families": ["Buddy II", "Multi II", "ATTIX 33", "ATTIX 44"],
            "products": ["Buddy II 18", "Multi II 30 T", "ATTIX 33-2L IC", "ATTIX 44-2M IC", "ATTIX 44-2H IC"],
            "technologies": ["Push&Clean", "InfiniClean", "FlowSensor", "MultiFit", "antistatique"],
            "use_cases": ["garage", "atelier", "rénovation", "ponçage", "poussières fines", "poussières de classe M/H"],
            "competitors": ["Kärcher", "Bosch", "Makita", "Festool", "DeWalt", "Parkside", "Mirka"],
        },
        "brand_positioning": {
            "summary": "Nilfisk se choisit comme une progression du nettoyage eau/poussière vers l'extraction professionnelle : Buddy, Multi II avec Push&Clean, puis ATTIX avec InfiniClean et classes certifiées selon la référence.",
            "core_decisions": [
                "le besoin est-il du nettoyage ponctuel ou du captage pendant le travail ?",
                "Push&Clean suffit-il ou faut-il InfiniClean pour maintenir le débit ?",
                "une classe L, M ou H est-elle réellement requise ?",
                "la référence complète confirme-t-elle la classe et l'équipement attendus ?",
            ],
        },
        "evidence": evidence,
        "key_claims": [
            {"claim": "Le Multi II 30 T actuel est un 30 L de 1400 W avec prise outil, témoin de saturation et Push&Clean.", "evidence_refs": ["S2", "S3"], "status": "VERIFIED"},
            {"claim": "Nilfisk décrit InfiniClean comme un nettoyage automatique du filtre pendant le fonctionnement, contrairement aux systèmes semi-automatiques.", "evidence_refs": ["S7"], "status": "VERIFIED"},
            {"claim": "L'ATTIX 33-2L IC est certifié classe L tout en pouvant utiliser un filtre PTFE référencé classe M.", "evidence_refs": ["S4"], "status": "VERIFIED"},
            {"claim": "L'ATTIX 44-2M IC combine classe M, InfiniClean, FlowSensor et système antistatique.", "evidence_refs": ["S5"], "status": "VERIFIED"},
            {"claim": "L'ATTIX 44-2H IC appartient à la gamme certifiée H et utilise un filtre HEPA H14 dans la configuration documentée.", "evidence_refs": ["S6"], "status": "VERIFIED"},
            {"claim": "Un retour communautaire ancien sur Multi II souligne la limite du nettoyage semi-automatique dans les séquences très poussiéreuses.", "evidence_refs": ["S8"], "status": "SUPPORTED"},
        ],
        "internal_links": [
            {"label": "eau et poussière", "url": "/comparatifs/aspirateur-eau-poussiere/"},
            {"label": "professionnel", "url": "/comparatifs/aspirateur-professionnel/"},
            {"label": "classe M", "url": "/comparatifs/aspirateur-classe-m/"},
            {"label": "décolmatage automatique", "url": "/guides/decolmatage-automatique/"},
            {"label": "classes L/M/H", "url": "/guides/classes-l-m-h/"},
            {"label": "atelier", "url": "/usages/aspirateur-atelier/"},
            {"label": "gravats", "url": "/usages/aspirateur-gravats/"},
        ],
    })
    obj.setdefault('editorial', {}).update({
        "desk_research_only": True,
        "affiliate_influence": False,
        "human_validation_required": True,
        "publish_review": "READY_FOR_HUMAN_VALIDATION",
        "workflow_contract_version": 2,
        "run_evidence": ".content/brands/runs/nilfisk.json",
    })
    obj['sources'] = {ref: {"label": label, "url": url, "source_type": kind} for ref, label, url, kind in SOURCES}
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    patch_page()
    write_ledger()
    print('✓ nilfisk evidence-led brand hub')


if __name__ == '__main__':
    main()
