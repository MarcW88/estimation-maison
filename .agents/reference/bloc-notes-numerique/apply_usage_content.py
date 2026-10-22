#!/usr/bin/env python3
"""Apply reviewed Usage outputs after the generic site generator.

This script is intentionally idempotent. It owns only the reviewed `/usages/`
editorial overrides, the approved PDF merge, and the navigation language needed
to keep Usage/Guide roles clear. It does not index Usage pages.
"""

from pathlib import Path
import re

from usage_bespoke_output import (
    MERGED_USAGE_REDIRECTS,
    USAGE_BESPOKE_CONTENT,
    USAGE_META_OVERRIDES,
)

ROOT = Path(__file__).resolve().parent
ACTIVE_USAGE_PATHS = [
    "/usages/prise-de-notes-professionnelle/",
    "/usages/prise-de-notes-etudiant/",
    "/usages/prise-de-notes-reunion/",
    "/usages/lecture-et-prise-de-notes/",
    "/usages/dessin/",
    "/usages/remplacer-cahiers-papier/",
]
PDF_GUIDE = "/guides/annoter-pdf-tablette-e-ink/"
PDF_MERGE_START = "<!-- USAGE-PDF-MERGE:START -->"
PDF_MERGE_END = "<!-- USAGE-PDF-MERGE:END -->"


def route_file(route: str) -> Path:
    return ROOT / route.strip("/") / "index.html"


def replace_once(text: str, pattern: str, repl: str, label: str) -> str:
    out, count = re.subn(pattern, repl, text, count=1, flags=re.S | re.I)
    if count != 1:
        raise RuntimeError(f"Could not replace {label}: found {count}")
    return out


def apply_usage_badge(html: str) -> str:
    """Give Usage its own taxonomy class without depending on generator state."""
    return re.sub(
        r'<span class="content-type type-(?:guide|usage)">(?:Guide|Par usage)</span>',
        '<span class="content-type type-usage">Par usage</span>',
        html,
        count=1,
        flags=re.I,
    )


def apply_body(route: str, body: str) -> None:
    fp = route_file(route)
    html = fp.read_text(encoding="utf-8")
    html = replace_once(
        html,
        r'(<article class="content-main">).*?(</article>)',
        lambda m: f'{m.group(1)}\n{body.strip()}\n    {m.group(2)}',
        f"article body {route}",
    )

    meta = USAGE_META_OVERRIDES.get(route)
    if meta:
        html = replace_once(html, r"<title>.*?</title>", f"<title>{meta['title']}</title>", f"title {route}")
        html = replace_once(
            html,
            r'<meta name="description" content="[^"]*">',
            f'<meta name="description" content="{meta["description"]}">',
            f"description {route}",
        )
        html = replace_once(html, r"<h1>.*?</h1>", f"<h1>{meta['title']}</h1>", f"h1 {route}")
        html = replace_once(html, r'<p class="lead">.*?</p>', f'<p class="lead">{meta["description"]}</p>', f"lead {route}")

    html = apply_usage_badge(html)
    if 'name="robots" content="noindex,follow"' not in html:
        raise RuntimeError(f"Usage noindex missing before write: {route}")
    fp.write_text(html, encoding="utf-8")
    print("usage applied", route)


def apply_keep_badge(route: str) -> None:
    fp = route_file(route)
    html = fp.read_text(encoding="utf-8")
    html = apply_usage_badge(html)
    fp.write_text(html, encoding="utf-8")


def merge_pdf_usage_into_guide() -> None:
    fp = route_file(PDF_GUIDE)
    html = fp.read_text(encoding="utf-8")
    html = re.sub(
        re.escape(PDF_MERGE_START) + r".*?" + re.escape(PDF_MERGE_END),
        "",
        html,
        flags=re.S,
    )
    merged = f'''{PDF_MERGE_START}
<h2 id="usage-fit">Avant la méthode : vérifiez que l’E Ink convient à votre flux PDF</h2>
<p>Le bon test ne s’arrête pas à la possibilité d’écrire sur une page. Prenez un document réel et suivez le cycle <strong>PDF entrant → annotation → PDF sortant</strong>. Le fichier doit pouvoir entrer sans perdre une fonction indispensable, rester lisible à la taille de votre écran, puis ressortir avec des annotations visibles dans un lecteur PDF standard.</p>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Étape</th><th>Test à faire</th><th>Signal d’alerte</th></tr></thead><tbody>
<tr><td>Entrée</td><td>ouvrir votre PDF le plus complexe par la méthode réellement utilisée</td><td>DRM, mot de passe, conversion ou fonctions perdues</td></tr>
<tr><td>Lecture</td><td>afficher une page dense sans zoom permanent</td><td>texte trop petit, recadrage constant</td></tr>
<tr><td>Annotation</td><td>écrire, surligner et naviguer entre plusieurs marques</td><td>outils trop limités pour votre tâche</td></tr>
<tr><td>Sortie</td><td>ouvrir le fichier exporté sur un autre ordinateur</td><td>annotations absentes ou dépendantes d’une app propriétaire</td></tr>
</tbody></table></div>
<p>L’E Ink est moins cohérente si vos PDF sont surtout des formulaires avancés, des présentations très colorées, des plans nécessitant zoom et déplacement constants, des documents multimédias ou des fichiers protégés que l’appareil ne sait pas annoter. Dans ces cas, une tablette LCD ou un ordinateur équipé d’un lecteur PDF complet peut rester plus efficace.</p>
{PDF_MERGE_END}'''
    answer = re.search(r'(<p class="article-answer">.*?</p>)', html, re.S | re.I)
    if not answer:
        raise RuntimeError("PDF guide article-answer not found")
    html = html[:answer.end()] + "\n\n" + merged + html[answer.end():]
    fp.write_text(html, encoding="utf-8")
    print("merged usage PDF into guide")


def write_redirect(route: str, target: str) -> None:
    fp = route_file(route)
    depth = route.count("/") - 1
    css = "../" * depth + "style.css"
    html = f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Annotation PDF : guide déplacé</title>
  <meta name="description" content="Le contenu sur l’annotation de PDF a été consolidé dans notre guide pratique dédié.">
  <meta name="robots" content="noindex,follow">
  <link rel="canonical" href="https://bloc-notes-numeriques.fr{target}">
  <meta http-equiv="refresh" content="0; url={target}">
  <link rel="stylesheet" href="{css}">
</head>
<body>
<main>
  <section class="page-hero"><div class="container">
    <span class="content-type type-guide">Guide</span>
    <h1>Le guide d’annotation PDF a été consolidé</h1>
    <p class="lead">Cette page a été regroupée avec notre guide complet afin d’éviter deux contenus couvrant le même besoin.</p>
    <p><a class="btn btn-primary" href="{target}">Accéder au guide d’annotation PDF</a></p>
  </div></section>
</main>
<script>window.location.replace({target!r});</script>
</body>
</html>'''
    fp.write_text(html, encoding="utf-8")
    print("redirect written", route, "->", target)


def update_global_navigation() -> None:
    old_pro = '<a href="/usages/prise-de-notes-professionnelle/">Travail et réunions</a>'
    new_pro = '<a href="/usages/prise-de-notes-professionnelle/">Travail</a>\n      <a href="/usages/prise-de-notes-reunion/">Réunions</a>'
    old_pdf = '      <a href="/usages/annotation-pdf/">Annoter des PDF</a>\n'

    for fp in ROOT.rglob("*.html"):
        html = fp.read_text(encoding="utf-8")
        updated = html.replace(old_pro, new_pro).replace(old_pdf, "")
        # Internal references should point directly to the surviving owner URL.
        updated = updated.replace('href="/usages/annotation-pdf/"', f'href="{PDF_GUIDE}"')
        if updated != html:
            fp.write_text(updated, encoding="utf-8")


def update_usage_hub() -> None:
    fp = ROOT / "usages" / "index.html"
    html = fp.read_text(encoding="utf-8")
    html = replace_once(
        html,
        r"<title>.*?</title>",
        "<title>Par usage — Définir vos besoins avant de choisir</title>",
        "usage hub title",
    )
    html = replace_once(
        html,
        r'<meta name="description" content="[^"]*">',
        '<meta name="description" content="Travail, études, réunions, lecture, dessin ou remplacement du papier : partez de votre workflow avant de comparer les appareils.">',
        "usage hub description",
    )
    html = replace_once(html, r"<h1>.*?</h1>", "<h1>Quel bloc-notes numérique selon votre usage ?</h1>", "usage hub h1")
    html = replace_once(
        html,
        r'<p class="lead">.*?</p>',
        '<p class="lead">Partez de ce que vous devez réellement accomplir : documents entrants, geste d’écriture, organisation, sortie et contraintes. Les comparatifs produits viennent ensuite.</p>',
        "usage hub lead",
    )
    # PDF is now owned by Guides; remove its obsolete Usage card if a generator restored it.
    html = re.sub(r'<a href="/guides/annoter-pdf-tablette-e-ink/" class="hub-link">.*?</a>\s*', '', html, flags=re.S)
    fp.write_text(html, encoding="utf-8")


def main() -> None:
    for route, body in USAGE_BESPOKE_CONTENT.items():
        apply_body(route, body)
    apply_keep_badge("/usages/remplacer-cahiers-papier/")
    merge_pdf_usage_into_guide()
    write_redirect("/usages/annotation-pdf/", PDF_GUIDE)
    update_global_navigation()
    update_usage_hub()
    print("usage cluster editorial application complete")


if __name__ == "__main__":
    main()
