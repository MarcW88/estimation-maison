from comparison_products import COMPARISON_PRODUCTS
from comparison_pages import COMPARISON_PAGES, CRITERIA_LABELS
from comparison_bespoke_output import bespoke_body
from comparison_bespoke_priority_20260909 import CONTENT as PRIORITY_CONTENT
from comparison_bespoke_remaining_20260909 import CONTENT as REMAINING_CONTENT

# IMPORTANT:
# `render_legacy_comparison` only preserves comparison pages that have not yet
# been migrated. It is not an editorial template. As of the 9 Sep 2026 cluster
# rewrite, all 14 comparison URLs have bespoke content; the legacy renderer is
# retained only as a safety fallback for future unmigrated slugs.


def link_for(pid):
    return {'remarkable_pure': '/marques/remarkable/', 'remarkable_pro': '/marques/remarkable/remarkable-paper-pro/', 'remarkable_move': '/marques/remarkable/', 'kindle_scribe3': '/marques/kindle-scribe/', 'kindle_colorsoft': '/marques/kindle-scribe/', 'boox_go2': '/marques/boox/', 'boox_go_lumi': '/marques/boox/', 'boox_air5c': '/marques/boox/', 'boox_notemax': '/marques/boox/', 'kobo_elipsa': '/marques/kobo-elipsa/', 'supernote_manta': '/marques/supernote/', 'supernote_nomad': '/marques/supernote/'}[pid]


def why_score(pid, p):
    prod=COMPARISON_PRODUCTS[pid]
    top=sorted(p["weights"].items(), key=lambda x:-x[1])[:3]
    return ", ".join(f"{CRITERIA_LABELS[c].lower()} ({prod['scores'][c]}/10)" for c,_ in top)


def render_legacy_comparison(slug):
    """Legacy safety fallback only; never use as an editorial skeleton."""
    p=COMPARISON_PAGES[slug]
    products=COMPARISON_PRODUCTS
    winner=p['ranking'][0][0]; wp=products[winner]; head=p['type']=='head_to_head'
    intro=(f'<p class="article-answer"><strong>Notre grille place {wp["name"]} en tête pour cette intention.</strong> Ce verdict vient de critères définis avant le classement pour le besoin « {p["job"]} ». Il s’agit d’une analyse documentaire, pas d’un test physique : les notes servent à rendre les arbitrages visibles et non à simuler des mesures de laboratoire.</p>')
    meth=(f'<h2 id="methode">Comment nous avons construit ce comparatif</h2><p>Nous avons d’abord défini l’intention — {p["job"]} — puis sélectionné uniquement des appareils actuellement documentés par leurs fabricants. Les critères ont été pondérés avant le calcul. Une note élevée ne signifie donc pas qu’un produit est meilleur en général : elle signifie qu’il répond mieux à cette requête précise.</p><p>Les scores sont des jugements éditoriaux fondés sur les fonctions vérifiées. Une spécification officielle est traitée comme un fait ; le passage de cette spécification à une note reste une déduction éditoriale. La commission d’affiliation n’entre jamais dans le calcul.</p>')
    rows=''.join(f'<tr><td>{CRITERIA_LABELS[c]}</td><td>{w}%</td><td>{"Critère majeur" if w>=20 else "Critère secondaire"}</td></tr>' for c,w in p['weights'].items())
    crit=(f'<h2 id="criteres">Les critères qui déterminent le classement</h2><div class="table-wrapper"><table class="comp-table"><thead><tr><th>Critère</th><th>Poids</th><th>Rôle</th></tr></thead><tbody>{rows}</tbody></table></div>')
    rankrows=''.join(f'<tr><td>{i}</td><td><a href="{link_for(pid)}">{products[pid]["name"]}</a></td><td>{score:.1f}/10</td><td>{products[pid]["best"]}</td><td>{products[pid]["limit"]}</td></tr>' for i,(pid,score) in enumerate(p['ranking'],1))
    ranking=(f'<h2 id="classement">Classement issu de la grille</h2><div class="table-wrapper"><table class="comp-table"><thead><tr><th>#</th><th>Modèle</th><th>Score éditorial</th><th>Point fort</th><th>Limite</th></tr></thead><tbody>{rankrows}</tbody></table></div>')
    blocks=[]
    for i,(pid,score) in enumerate(p['ranking'][:(2 if head else 4)],1):
        pr=products[pid]
        blocks.append(f'<h2 id="produit-{i}">{i}. {pr["name"]}</h2><p>{pr["best"]}. Limite : {pr["limit"]}.</p>')
    srcs=[]
    for pid in p['products']:
        pr=products[pid]
        if pr['source'] not in [x[0] for x in srcs]: srcs.append((pr['source'],pr['source_label']))
    sources='<h2 id="sources">Sources officielles consultées</h2><ul class="source-list">'+''.join(f'<li><a href="{u}" rel="noopener noreferrer">{lab}</a></li>' for u,lab in srcs)+'</ul>'
    return intro+meth+crit+ranking+''.join(blocks)+sources


def reviewed_body(slug: str) -> str:
    if slug in PRIORITY_CONTENT:
        return PRIORITY_CONTENT[slug].strip()
    if slug in REMAINING_CONTENT:
        return REMAINING_CONTENT[slug].strip()
    return bespoke_body(slug, render_legacy_comparison(slug)).strip()


COMPARISON_CONTENT = {slug: reviewed_body(slug) for slug in COMPARISON_PAGES}
