#!/usr/bin/env python3
"""Generate all HTML pages for bloc-notes-numerique.fr"""

import os

from usage_content import USAGE_CONTENT
from deal_content import DEAL_CONTENT, DEAL_STATUS_LABEL

BASE = os.path.dirname(os.path.abspath(__file__))

# ── NAV HTML ──────────────────────────────────────────────────────────────────
NAV = """
<nav class="site-nav" id="site-navigation" aria-label="Navigation principale">
  <div class="nav-item">
    <a href="/comparatifs/" class="nav-link">
      Comparatifs
      <svg class="chevron" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
    </a>
    <div class="dropdown">
      <span class="dropdown-label">Sélections</span>
      <a href="/comparatifs/meilleur-bloc-notes-numerique/">Meilleurs bloc-notes numériques</a>
      <a href="/comparatifs/bloc-notes-numerique-professionnel/">Pour les professionnels</a>
      <a href="/comparatifs/bloc-notes-numerique-etudiant/">Pour les étudiants</a>
      <a href="/comparatifs/bloc-notes-numerique-couleur/">Modèles couleur</a>
      <a href="/comparatifs/bloc-notes-numerique-a4/">Formats A4</a>
      <a href="/comparatifs/bloc-notes-numerique-sans-abonnement/">Sans abonnement</a>
      <a href="/comparatifs/bloc-notes-numerique-pas-cher/">Modèles pas chers</a>
      <div class="dropdown-separator"></div>
      <span class="dropdown-label">Comparer les modèles</span>
      <a href="/comparatifs/kindle-scribe-vs-remarkable/">Kindle Scribe vs reMarkable</a>
      <a href="/comparatifs/kindle-scribe-vs-kobo-elipsa/">Kindle Scribe vs Kobo Elipsa</a>
      <a href="/comparatifs/remarkable-vs-boox/">reMarkable vs Boox</a>
      <a href="/comparatifs/remarkable-vs-supernote/">reMarkable vs Supernote</a>
      <a href="/comparatifs/boox-vs-supernote/">Boox vs Supernote</a>
      <a href="/comparatifs/kobo-elipsa-vs-remarkable/">Kobo Elipsa vs reMarkable</a>
    </div>
  </div>
  <div class="nav-item">
    <a href="/marques/" class="nav-link">
      Marques
      <svg class="chevron" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
    </a>
    <div class="dropdown">
      <a href="/marques/remarkable/">reMarkable</a>
      <a href="/marques/kindle-scribe/">Kindle Scribe</a>
      <a href="/marques/kobo-elipsa/">Kobo Elipsa</a>
      <a href="/marques/boox/">Boox</a>
      <a href="/marques/supernote/">Supernote</a>
    </div>
  </div>
  <div class="nav-item">
    <a href="/usages/" class="nav-link">
      Par usage
      <svg class="chevron" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
    </a>
    <div class="dropdown">
      <a href="/usages/prise-de-notes-professionnelle/">Travail et réunions</a>
      <a href="/usages/prise-de-notes-etudiant/">Études et cours</a>
      <a href="/usages/annotation-pdf/">Annoter des PDF</a>
      <a href="/usages/lecture-et-prise-de-notes/">Lire et prendre des notes</a>
      <a href="/usages/dessin/">Dessiner</a>
      <a href="/usages/remplacer-cahiers-papier/">Remplacer le papier</a>
    </div>
  </div>
  <div class="nav-item">
    <a href="/guides/" class="nav-link">
      Guides
      <svg class="chevron" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
    </a>
    <div class="dropdown">
      <span class="dropdown-label">Bien choisir</span>
      <a href="/guides/choisir-bloc-notes-numerique/">Choisir son bloc-notes numérique</a>
      <a href="/guides/liseuse-ou-bloc-notes-numerique/">Liseuse ou bloc-notes ?</a>
      <a href="/guides/tablette-classique-ou-tablette-e-ink/">Tablette classique ou E Ink ?</a>
      <a href="/guides/prix-bloc-notes-numerique/">Prix et budgets</a>
      <div class="dropdown-separator"></div>
      <span class="dropdown-label">Technologie</span>
      <a href="/guides/tablette-e-ink/">Comprendre l'E Ink</a>
      <a href="/guides/encre-electronique-fonctionnement/">Fonctionnement de l'encre électronique</a>
      <div class="dropdown-separator"></div>
      <span class="dropdown-label">Utilisation</span>
      <a href="/guides/exporter-notes/">Exporter ses notes</a>
      <a href="/guides/annoter-pdf-tablette-e-ink/">Annoter des PDF</a>
      <a href="/guides/synchroniser-notes-cloud/">Synchronisation cloud</a>
    </div>
  </div>
  <div class="nav-item">
    <a href="/bons-plans/" class="nav-link">
      Bons plans
      <svg class="chevron" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
    </a>
    <div class="dropdown">
      <a href="/bons-plans/bloc-notes-numerique/">Tous les bons plans</a>
      <a href="/bons-plans/remarkable/">reMarkable</a>
      <a href="/bons-plans/kindle-scribe/">Kindle Scribe</a>
      <a href="/bons-plans/kobo-elipsa/">Kobo Elipsa</a>
      <a href="/bons-plans/boox/">Boox</a>
      <a href="/bons-plans/bloc-notes-numerique-occasion/">Occasion</a>
      <a href="/bons-plans/black-friday/">Black Friday</a>
    </div>
  </div>
</nav>
"""

HEADER = """
<header class="site-header">
  <div class="header-inner">
    <a href="/" class="site-logo">
      <span class="logo-line1">bloc-notes<span class="logo-pen"></span></span>
      <span class="logo-line2">numériques.fr</span>
    </a>
    {nav}
    <a href="/boutique/" class="header-cta">Voir les produits</a>
    <button class="burger" type="button" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="site-navigation">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
""".format(nav=NAV)

FOOTER = """
<footer class="site-footer">
  <div class="container">
    <div class="footer-inner">
      <div class="footer-brand">
        <div class="site-logo">
          <span class="logo-line1">bloc-notes</span>
          <span class="logo-line2">numériques.fr</span>
        </div>
        <p class="footer-tagline">Analyses, comparatifs et guides indépendants pour choisir une tablette de prise de notes adaptée à vos usages.</p>
      </div>
      <div class="footer-col">
        <h4>Comparatifs</h4>
        <a href="/boutique/">Boutique</a>
        <a href="/comparatifs/meilleur-bloc-notes-numerique/">Meilleurs modèles</a>
        <a href="/comparatifs/bloc-notes-numerique-professionnel/">Professionnels</a>
        <a href="/comparatifs/bloc-notes-numerique-etudiant/">Étudiants</a>
        <a href="/comparatifs/bloc-notes-numerique-sans-abonnement/">Sans abonnement</a>
        <a href="/comparatifs/bloc-notes-numerique-pas-cher/">Pas chers</a>
      </div>
      <div class="footer-col">
        <h4>Marques</h4>
        <a href="/marques/remarkable/">reMarkable</a>
        <a href="/marques/kindle-scribe/">Kindle Scribe</a>
        <a href="/marques/kobo-elipsa/">Kobo Elipsa</a>
        <a href="/marques/boox/">Boox</a>
        <a href="/marques/supernote/">Supernote</a>
        <a href="/accessoires/">Accessoires</a>
      </div>
      <div class="footer-col">
        <h4>Le site</h4>
        <a href="/methode-de-test/">Méthode de test</a>
        <a href="/comment-nous-comparons/">Comment nous comparons</a>
        <a href="/a-propos/">À propos</a>
        <a href="/contact/">Contact</a>
        <a href="/transparence-affiliation/">Transparence affiliation</a>
        <a href="/mentions-legales/">Mentions légales</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 bloc-notes numériques.fr — Tous droits réservés</span>
      <span>Ce site contient des liens affiliés. <a href="/transparence-affiliation/">En savoir plus.</a></span>
    </div>
  </div>
</footer>
"""

def html_page(title, description, breadcrumb_html, content_html, canonical="/", robots="noindex,follow"):
    depth = canonical.count("/") - 1
    css_path = ("../" * depth) + "style.css" if depth > 0 else "style.css"
    js_path = ("../" * depth) + "site.js" if depth > 0 else "site.js"
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="{robots}">
  <link rel="canonical" href="https://bloc-notes-numeriques.fr{canonical}">
  <link rel="alternate" hreflang="fr-FR" href="https://bloc-notes-numeriques.fr{canonical}">
  <link rel="stylesheet" href="{css_path}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
</head>
<body>
{HEADER}
<main>
{breadcrumb_html}
{content_html}
</main>
{FOOTER}
<script src="{js_path}" defer></script>
</body>
</html>"""

def breadcrumb(*items):
    """items = list of (label, url) or just label for last"""
    parts = []
    for i, item in enumerate(items):
        if isinstance(item, tuple):
            parts.append(f'<a href="{item[1]}">{item[0]}</a>')
        else:
            parts.append(f'<span>{item}</span>')
        if i < len(items) - 1:
            parts.append('<span class="sep">/</span>')
    return f'<div class="container"><div class="page-breadcrumb"><a href="/">Accueil</a><span class="sep">/</span>{" ".join(parts)}</div></div>'

def hub_page(title, desc, canonical, crumbs, intro, links):
    links_html = "\n".join(
        f'<a href="{url}" class="hub-link"><span>{label}</span><span class="hub-link-arrow">→</span></a>'
        for label, url in links
    )
    content = f"""
<section class="page-hero">
  <div class="container">
    <h1>{title}</h1>
    <p class="lead">{intro}</p>
    <div class="page-meta">
      <span class="update-tag">Mis à jour régulièrement</span>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="hub-grid">
      {links_html}
    </div>
  </div>
</section>
"""
    return html_page(title, desc, crumbs, content, canonical)

def content_page(title, desc, canonical, crumbs, page_type="", body_html="", status_label=None):
    type_badge = f'<span class="content-type type-{page_type.lower()}">{page_type}</span>' if page_type else ""
    article_content = body_html.strip() if body_html else "<!-- Contenu à rédiger -->"
    content_status = status_label or ("Vérifié le 8 septembre 2026" if body_html else "Contenu en préparation")
    content = f"""
<section class="page-hero">
  <div class="container">
    {type_badge}
    <h1>{title}</h1>
    <p class="lead">{desc}</p>
    <div class="page-meta">
      <span class="update-tag">Mis à jour régulièrement</span>
      <span class="page-meta-item">{content_status}</span>
    </div>
  </div>
</section>
<div class="container">
  <div class="content-layout">
    <article class="content-main">
      {article_content}
    </article>
    <aside class="content-sidebar">
      <div class="sidebar-box sidebar-toc">
        <h4>Sommaire</h4>
        <!-- Sommaire généré dynamiquement -->
      </div>
      <div class="sidebar-box">
        <h4>Affiliation</h4>
        <p class="affiliation-note">Ce site contient des liens affiliés. Nos recommandations restent indépendantes. <a href="/transparence-affiliation/">En savoir plus.</a></p>
      </div>
      <a href="/guides/choisir-bloc-notes-numerique/" class="btn btn-primary" style="width:100%;justify-content:center;">Trouver mon modèle</a>
    </aside>
  </div>
</div>
"""
    return html_page(title, desc, crumbs, content, canonical)

def test_page(title, desc, canonical, crumbs, product_name, score="—"):
    content = f"""
<section class="page-hero">
  <div class="container">
    <span class="content-type type-test">Analyse produit</span>
    <h1>{title}</h1>
    <p class="lead">{desc}</p>
    <div class="page-meta">
      <span class="update-tag">Analyse en préparation</span>
    </div>
  </div>
</section>
<div class="container">
  <div class="content-layout">
    <article class="content-main">
      <div class="product-summary">
        <div class="product-summary-header">Résumé — {product_name}</div>
        <div class="product-summary-body">
          <div class="summary-row"><span class="summary-label">Idéal pour</span><span class="summary-val">À compléter</span></div>
          <div class="summary-row"><span class="summary-label">À éviter si</span><span class="summary-val">À compléter</span></div>
          <div class="summary-row"><span class="summary-label">Principal avantage</span><span class="summary-val">À compléter</span></div>
          <div class="summary-row"><span class="summary-label">Principale limite</span><span class="summary-val">À compléter</span></div>
          <div class="summary-row"><span class="summary-label">Prix constaté</span><span class="summary-val">— €</span></div>
        </div>
      </div>
      <p class="draft-notice">Cette page est en préparation. Aucun verdict ni lien marchand ne sera publié avant vérification des informations.</p>
      <!-- Contenu du test à rédiger -->
    </article>
    <aside class="content-sidebar">
      <div class="sidebar-box">
        <h4>Note globale</h4>
        <div class="score-display">
          <span class="score-num">{score}</span>
          <span class="score-max">/10</span>
        </div>
        <div class="score-bars">
          <div class="score-bar-item">
            <span class="score-bar-label"><span>Écriture</span><span>—</span></span>
            <div class="score-bar-track"><div class="score-bar-fill" style="width:0%"></div></div>
          </div>
          <div class="score-bar-item">
            <span class="score-bar-label"><span>Écran</span><span>—</span></span>
            <div class="score-bar-track"><div class="score-bar-fill" style="width:0%"></div></div>
          </div>
          <div class="score-bar-item">
            <span class="score-bar-label"><span>Autonomie</span><span>—</span></span>
            <div class="score-bar-track"><div class="score-bar-fill" style="width:0%"></div></div>
          </div>
          <div class="score-bar-item">
            <span class="score-bar-label"><span>Logiciel &amp; export</span><span>—</span></span>
            <div class="score-bar-track"><div class="score-bar-fill" style="width:0%"></div></div>
          </div>
          <div class="score-bar-item">
            <span class="score-bar-label"><span>Rapport qualité-prix</span><span>—</span></span>
            <div class="score-bar-track"><div class="score-bar-fill" style="width:0%"></div></div>
          </div>
        </div>
      </div>
      <div class="sidebar-box sidebar-toc">
        <h4>Sommaire</h4>
      </div>
      <div class="sidebar-box">
        <h4>Affiliation</h4>
        <p class="affiliation-note">Ce site contient des liens affiliés. <a href="/transparence-affiliation/">En savoir plus.</a></p>
      </div>
    </aside>
  </div>
</div>
"""
    return html_page(title, desc, crumbs, content, canonical)

def write(path, content):
    full = os.path.join(BASE, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ {path}")

# ── HOMEPAGE ─────────────────────────────────────────────────────────────────
homepage = html_page(
    "Bloc-notes numériques — Comparatifs, analyses et guides",
    "Trouvez le bloc-notes numérique adapté à votre usage grâce à des comparatifs, analyses documentées et guides sur reMarkable, Kindle Scribe, Boox, Kobo Elipsa et Supernote.",
    "",
    """
<section class="hero">
  <div class="container">
    <div class="hero-inner">
      <div class="hero-content">
        <span class="hero-tag">Comparatifs &amp; guides indépendants</span>
        <h1 class="hero-title">Le bon bloc-notes numérique,<br>selon votre manière de travailler.</h1>
        <p class="lead hero-desc">Comparatifs, analyses documentées et guides pour choisir une tablette de prise de notes réellement adaptée à vos usages.</p>
        <div class="hero-actions">
          <a href="/comparatifs/meilleur-bloc-notes-numerique/" class="btn btn-primary btn-lg">Comparer les meilleurs modèles</a>
          <a href="/guides/choisir-bloc-notes-numerique/" class="btn btn-secondary btn-lg">Trouver mon bloc-notes numérique</a>
        </div>
      </div>
      <div class="hero-visual">
        <div class="paper-study" aria-hidden="true"><span></span><span></span><span></span></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-heading">
      <p class="eyebrow">Par usage</p>
      <h2>Quel est votre besoin principal ?</h2>
      <p>Chaque usage a ses exigences. Trouvez le modèle adapté à votre situation.</p>
    </div>
    <div class="usage-grid">
      <a href="/usages/prise-de-notes-professionnelle/" class="usage-card">
        <div class="usage-icon"><svg viewBox="0 0 24 24"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg></div>
        <h3>Pour le travail</h3>
        <p>Réunions, annotations, organisation de projets.</p>
      </a>
      <a href="/usages/prise-de-notes-etudiant/" class="usage-card">
        <div class="usage-icon"><svg viewBox="0 0 24 24"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg></div>
        <h3>Pour les études</h3>
        <p>Cours, révisions, prise de notes manuscrite.</p>
      </a>
      <a href="/usages/annotation-pdf/" class="usage-card">
        <div class="usage-icon"><svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg></div>
        <h3>Annoter des PDF</h3>
        <p>Documents, articles, contrats, livres numériques.</p>
      </a>
      <a href="/usages/lecture-et-prise-de-notes/" class="usage-card">
        <div class="usage-icon"><svg viewBox="0 0 24 24"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg></div>
        <h3>Lire et prendre des notes</h3>
        <p>Lecture longue, résumés, fiches de lecture.</p>
      </a>
      <a href="/usages/dessin/" class="usage-card">
        <div class="usage-icon"><svg viewBox="0 0 24 24"><path d="M12 19l7-7 3 3-7 7-3-3z"/><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/><path d="M2 2l7.586 7.586"/><circle cx="11" cy="11" r="2"/></svg></div>
        <h3>Dessiner</h3>
        <p>Croquis, schémas, mind maps, créativité.</p>
      </a>
      <a href="/usages/remplacer-cahiers-papier/" class="usage-card">
        <div class="usage-icon"><svg viewBox="0 0 24 24"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg></div>
        <h3>Remplacer le papier</h3>
        <p>Zéro papier, organisation numérique, durabilité.</p>
      </a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-heading">
      <p class="eyebrow">Comparatif</p>
      <h2>Cinq modèles à comparer</h2>
      <p>Une grille de comparaison commune, complétée au fur et à mesure de nos vérifications.</p>
    </div>
    <div class="table-wrapper">
      <table class="comp-table">
        <thead>
          <tr>
            <th>Modèle</th>
            <th>Idéal pour</th>
            <th>Écran</th>
            <th>Couleur</th>
            <th>Abonnement</th>
            <th>Prix</th>
            <th>Verdict</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>reMarkable Paper Pro</strong></td>
            <td>Écriture, annotation</td>
            <td>11,8″ E Ink</td>
            <td><span class="badge badge-primary">Couleur</span></td>
            <td>Optionnel</td>
            <td>— €</td>
            <td>Positionnement à vérifier</td>
          </tr>
          <tr>
            <td><strong>Kindle Scribe</strong></td>
            <td>Lecture &amp; notes</td>
            <td>10,2″ E Ink</td>
            <td><span class="badge badge-neutral">N&amp;B</span></td>
            <td>Non</td>
            <td>— €</td>
            <td>Positionnement à vérifier</td>
          </tr>
          <tr>
            <td><strong>Boox Note Air 4</strong></td>
            <td>Android ouvert</td>
            <td>10,3″ E Ink</td>
            <td><span class="badge badge-primary">Couleur</span></td>
            <td>Non</td>
            <td>— €</td>
            <td>Positionnement à vérifier</td>
          </tr>
          <tr>
            <td><strong>Kobo Elipsa 2E</strong></td>
            <td>Lecture enrichie</td>
            <td>10,3″ E Ink</td>
            <td><span class="badge badge-neutral">N&amp;B</span></td>
            <td>Non</td>
            <td>— €</td>
            <td>Positionnement à vérifier</td>
          </tr>
          <tr>
            <td><strong>Supernote A5X2</strong></td>
            <td>Écriture précise</td>
            <td>10,2″ E Ink</td>
            <td><span class="badge badge-neutral">N&amp;B</span></td>
            <td>Non</td>
            <td>— €</td>
            <td>Positionnement à vérifier</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div style="text-align:center;margin-top:24px;">
      <a href="/comparatifs/meilleur-bloc-notes-numerique/" class="btn btn-secondary">Voir le comparatif complet</a>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-heading">
      <p class="eyebrow">Profils d’usage</p>
      <h2>Les positionnements à documenter</h2>
    </div>
    <div class="reco-grid">
      <div class="reco-card">
        <div class="reco-card-badge">Écriture et couleur</div>
        <div class="reco-card-img" aria-hidden="true"><span class="product-silhouette"></span></div>
        <div class="reco-card-body">
          <h3>reMarkable Paper Pro</h3>
          <div class="reco-meta">
            <div class="reco-pro">Sensation d'écriture inégalée</div>
            <div class="reco-con">Écosystème fermé</div>
          </div>
          <div class="reco-price">— €</div>
          <div class="reco-actions">
            <a href="/marques/remarkable/remarkable-paper-pro-avis/" class="btn btn-ghost">Lire l’analyse</a>
            <span class="btn btn-accent btn-disabled" aria-disabled="true">Prix à venir</span>
          </div>
        </div>
      </div>
      <div class="reco-card">
        <div class="reco-card-badge accent">Environnement ouvert</div>
        <div class="reco-card-img" aria-hidden="true"><span class="product-silhouette product-silhouette--wide"></span></div>
        <div class="reco-card-body">
          <h3>Boox Tab Ultra C Pro</h3>
          <div class="reco-meta">
            <div class="reco-pro">Android ouvert, apps tierces</div>
            <div class="reco-con">Interface plus complexe</div>
          </div>
          <div class="reco-price">— €</div>
          <div class="reco-actions">
            <a href="/marques/boox/avis/" class="btn btn-ghost">Lire l’analyse</a>
            <span class="btn btn-accent btn-disabled" aria-disabled="true">Prix à venir</span>
          </div>
        </div>
      </div>
      <div class="reco-card">
        <div class="reco-card-badge neutral">Lecture et annotation</div>
        <div class="reco-card-img" aria-hidden="true"><span class="product-silhouette product-silhouette--compact"></span></div>
        <div class="reco-card-body">
          <h3>Kindle Scribe</h3>
          <div class="reco-meta">
            <div class="reco-pro">Prix accessible, écosystème Amazon</div>
            <div class="reco-con">Fonctions notes limitées</div>
          </div>
          <div class="reco-price">— €</div>
          <div class="reco-actions">
            <a href="/marques/kindle-scribe/" class="btn btn-ghost">Lire l’analyse</a>
            <span class="btn btn-accent btn-disabled" aria-disabled="true">Prix à venir</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-heading">
      <p class="eyebrow">Comparaisons populaires</p>
      <h2>Hésitez-vous entre deux modèles ?</h2>
      <p>Ces pages vous aident à trancher selon votre usage précis.</p>
    </div>
    <div class="vs-grid">
      <a href="/comparatifs/kindle-scribe-vs-remarkable/" class="vs-row">
        <div class="vs-brand">Kindle Scribe</div>
        <div class="vs-sep">VS</div>
        <div class="vs-brand vs-brand-right">reMarkable</div>
      </a>
      <a href="/comparatifs/remarkable-vs-boox/" class="vs-row">
        <div class="vs-brand">reMarkable</div>
        <div class="vs-sep">VS</div>
        <div class="vs-brand vs-brand-right">Boox</div>
      </a>
      <a href="/comparatifs/kobo-elipsa-vs-remarkable/" class="vs-row">
        <div class="vs-brand">Kobo Elipsa</div>
        <div class="vs-sep">VS</div>
        <div class="vs-brand vs-brand-right">reMarkable</div>
      </a>
    </div>
    <div style="text-align:center;margin-top:24px;">
      <a href="/comparatifs/" class="btn btn-ghost">Toutes les comparaisons</a>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-heading">
      <p class="eyebrow">Derniers contenus</p>
      <h2>Tests et guides récents</h2>
    </div>
    <div class="content-grid">
      <a href="/marques/remarkable/remarkable-paper-pro-avis/" class="content-card">
        <div class="content-card-img"></div>
        <div class="content-card-body">
          <span class="content-type type-test">Analyse</span>
          <h3>reMarkable Paper Pro — Avis complet</h3>
          <p>Analyse détaillée de l'expérience d'écriture, de l'écran et de l'écosystème.</p>
          <span class="content-date">Contenu en préparation</span>
        </div>
      </a>
      <a href="/comparatifs/meilleur-bloc-notes-numerique/" class="content-card">
        <div class="content-card-img"></div>
        <div class="content-card-body">
          <span class="content-type type-comparatif">Comparatif</span>
          <h3>Quel bloc-notes numérique choisir ?</h3>
          <p>Notre sélection des meilleures tablettes de prise de notes.</p>
          <span class="content-date">Contenu en préparation</span>
        </div>
      </a>
      <a href="/guides/choisir-bloc-notes-numerique/" class="content-card">
        <div class="content-card-img"></div>
        <div class="content-card-body">
          <span class="content-type type-guide">Guide</span>
          <h3>Comment choisir son bloc-notes numérique ?</h3>
          <p>Tous les critères à connaître avant d'acheter.</p>
          <span class="content-date">Contenu en préparation</span>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="section section--white">
  <div class="container">
    <div class="section-heading" style="max-width:600px;margin-left:auto;margin-right:auto;text-align:center;">
      <p class="eyebrow">Méthodologie</p>
      <h2>Comment évaluons-nous les bloc-notes numériques ?</h2>
      <p>Chaque recommandation devra indiquer clairement son niveau de preuve et les informations effectivement vérifiées.</p>
    </div>
    <div class="method-grid">
      <div class="method-card">
        <div class="method-num">01</div>
        <h4>Qualité d'écriture</h4>
        <p>Latence, sensation du stylet, précision, comportement en écriture rapide.</p>
      </div>
      <div class="method-card">
        <div class="method-num">02</div>
        <h4>Organisation &amp; export</h4>
        <p>Structure des notes, formats d'export, OCR, synchronisation cloud.</p>
      </div>
      <div class="method-card">
        <div class="method-num">03</div>
        <h4>Confort de lecture</h4>
        <p>Qualité de l'écran E Ink, éclairage, lisibilité des PDF, fatigue oculaire.</p>
      </div>
      <div class="method-card">
        <div class="method-num">04</div>
        <h4>Coût réel</h4>
        <p>Prix d'achat, abonnements, accessoires nécessaires, durée de vie estimée.</p>
      </div>
    </div>
    <div style="text-align:center;">
      <a href="/methode-de-test/" class="btn btn-secondary">Lire notre méthodologie complète</a>
    </div>
    <div style="text-align:center;margin-top:24px;">
      <span class="handnote">Notre avis : le meilleur écran n'implique pas nécessairement le meilleur outil de prise de notes.</span>
    </div>
  </div>
</section>
""",
    "/"
)

write("/index.html", homepage)

# ── BOUTIQUE D'AFFILIATION ──────────────────────────────────────────────────
from shop_content import render_shop_content

write("/boutique/index.html", html_page(
    "Boutique de bloc-notes numériques — Modèles analysés",
    "Comparez les bloc-notes numériques déjà analysés sur le site et vérifiez leur prix chez nos partenaires marchands.",
    breadcrumb("Boutique"),
    render_shop_content(),
    "/boutique/",
    robots="index,follow",
))

# ── COMPARATIFS ───────────────────────────────────────────────────────────────
write("/comparatifs/index.html", hub_page(
    "Comparatifs de bloc-notes numériques",
    "Tous nos comparatifs de tablettes E Ink et bloc-notes numériques. Trouvez le meilleur modèle selon votre usage et votre budget.",
    "/comparatifs/",
    breadcrumb("Comparatifs"),
    "Nos comparatifs indépendants pour vous aider à choisir le bloc-notes numérique adapté à votre situation.",
    [
        ("Meilleurs bloc-notes numériques", "/comparatifs/meilleur-bloc-notes-numerique/"),
        ("Pour les professionnels", "/comparatifs/bloc-notes-numerique-professionnel/"),
        ("Pour les étudiants", "/comparatifs/bloc-notes-numerique-etudiant/"),
        ("Modèles couleur", "/comparatifs/bloc-notes-numerique-couleur/"),
        ("Formats A4", "/comparatifs/bloc-notes-numerique-a4/"),
        ("Sans abonnement", "/comparatifs/bloc-notes-numerique-sans-abonnement/"),
        ("Modèles pas chers", "/comparatifs/bloc-notes-numerique-pas-cher/"),
        ("Kindle Scribe vs reMarkable", "/comparatifs/kindle-scribe-vs-remarkable/"),
        ("Kindle Scribe vs Kobo Elipsa", "/comparatifs/kindle-scribe-vs-kobo-elipsa/"),
        ("reMarkable vs Boox", "/comparatifs/remarkable-vs-boox/"),
        ("reMarkable vs Supernote", "/comparatifs/remarkable-vs-supernote/"),
        ("Boox vs Supernote", "/comparatifs/boox-vs-supernote/"),
        ("Kobo Elipsa vs reMarkable", "/comparatifs/kobo-elipsa-vs-remarkable/"),
    ]
))

COMPARATIFS = [
    ("/comparatifs/meilleur-bloc-notes-numerique/", "Meilleur bloc-notes numérique — Comparatif & sélection", "Quel bloc-notes numérique choisir ? Notre grille comparative des tablettes E Ink pour la prise de notes.", "comparatif"),
    ("/comparatifs/tablette-e-ink/", "Meilleure tablette E Ink — Comparatif", "Comparaison des principales tablettes E Ink pour comprendre leurs usages et leurs limites.", "comparatif"),
    ("/comparatifs/bloc-notes-numerique-professionnel/", "Meilleur bloc-notes numérique pour les professionnels", "Quel bloc-notes numérique choisir pour une utilisation professionnelle ? Notre sélection pour le travail.", "comparatif"),
    ("/comparatifs/bloc-notes-numerique-etudiant/", "Meilleur bloc-notes numérique pour les étudiants", "Quel bloc-notes numérique choisir pour les études ? Notre comparatif pour les étudiants.", "comparatif"),
    ("/comparatifs/bloc-notes-numerique-couleur/", "Meilleur bloc-notes numérique couleur", "Comparatif des bloc-notes numériques avec écran couleur E Ink.", "comparatif"),
    ("/comparatifs/bloc-notes-numerique-a4/", "Meilleur bloc-notes numérique A4", "Sélection des tablettes de prise de notes au format A4.", "comparatif"),
    ("/comparatifs/bloc-notes-numerique-sans-abonnement/", "Meilleur bloc-notes numérique sans abonnement", "Bloc-notes numériques fonctionnels sans abonnement mensuel.", "comparatif"),
    ("/comparatifs/bloc-notes-numerique-pas-cher/", "Meilleur bloc-notes numérique pas cher", "Les meilleures tablettes E Ink à petit prix pour la prise de notes.", "comparatif"),
    ("/comparatifs/kindle-scribe-vs-remarkable/", "Kindle Scribe vs reMarkable — Lequel choisir ?", "Comparaison détaillée entre le Kindle Scribe et le reMarkable. Quelle tablette convient le mieux à votre usage ?", "comparatif"),
    ("/comparatifs/kindle-scribe-vs-kobo-elipsa/", "Kindle Scribe vs Kobo Elipsa — Comparatif", "Kindle Scribe ou Kobo Elipsa ? Notre analyse comparative pour vous aider à choisir.", "comparatif"),
    ("/comparatifs/remarkable-vs-boox/", "reMarkable vs Boox — Comparatif complet", "reMarkable ou Boox ? Deux philosophies différentes : écosystème fermé vs Android ouvert.", "comparatif"),
    ("/comparatifs/remarkable-vs-supernote/", "reMarkable vs Supernote — Comparatif", "reMarkable ou Supernote ? Deux appareils dédiés à l'écriture avec des approches distinctes.", "comparatif"),
    ("/comparatifs/boox-vs-supernote/", "Boox vs Supernote — Lequel choisir ?", "Boox ou Supernote : notre comparatif pour les amateurs de prise de notes précise.", "comparatif"),
    ("/comparatifs/kobo-elipsa-vs-remarkable/", "Kobo Elipsa vs reMarkable — Comparatif", "Kobo Elipsa ou reMarkable ? Lecture et annotation vs écriture pure.", "comparatif"),
]

for path, title, desc, ptype in COMPARATIFS:
    crumbs = breadcrumb(("Comparatifs", "/comparatifs/"), title.split("—")[0].strip())
    write(path + "index.html", content_page(title, desc, path, crumbs, "Comparatif"))

# ── MARQUES ───────────────────────────────────────────────────────────────────
write("/marques/index.html", hub_page(
    "Marques de bloc-notes numériques",
    "Découvrez tous nos tests, comparatifs et guides par marque : reMarkable, Kindle Scribe, Boox, Kobo Elipsa et Supernote.",
    "/marques/",
    breadcrumb("Marques"),
    "Tout ce que vous devez savoir sur chaque marque : tests, modèles, accessoires et écosystème.",
    [
        ("reMarkable", "/marques/remarkable/"),
        ("Kindle Scribe", "/marques/kindle-scribe/"),
        ("Kobo Elipsa", "/marques/kobo-elipsa/"),
        ("Boox", "/marques/boox/"),
        ("Supernote", "/marques/supernote/"),
    ]
))

# reMarkable hub
write("/marques/remarkable/index.html", hub_page(
    "reMarkable — Tests, comparatifs et guides",
    "Tout sur reMarkable : Paper Pro, reMarkable 2, abonnement Connect, accessoires et alternatives.",
    "/marques/remarkable/",
    breadcrumb(("Marques", "/marques/"), "reMarkable"),
    "Le hub reMarkable : modèles disponibles, tests, comparatifs, accessoires compatibles et questions fréquentes.",
    [
        ("reMarkable Paper Pro", "/marques/remarkable/remarkable-paper-pro/"),
        ("reMarkable 2", "/marques/remarkable/remarkable-2/"),
        ("Avis reMarkable 2", "/marques/remarkable/remarkable-2-avis/"),
        ("Avis reMarkable Paper Pro", "/marques/remarkable/remarkable-paper-pro-avis/"),
        ("Abonnement Connect", "/marques/remarkable/abonnement-connect/"),
        ("Accessoires reMarkable", "/marques/remarkable/accessoires/"),
        ("Alternatives à reMarkable", "/marques/remarkable/alternatives/"),
    ]
))

REMARKABLE_PAGES = [
    ("/marques/remarkable/remarkable-paper-pro/", "reMarkable Paper Pro — Fiche technique et présentation", "Découvrez le reMarkable Paper Pro : caractéristiques, fonctionnalités et pour qui c'est fait."),
    ("/marques/remarkable/remarkable-2/", "reMarkable 2 — Fiche technique et présentation", "Le reMarkable 2 : caractéristiques, fonctionnalités et comparaison avec le Paper Pro."),
    ("/marques/remarkable/remarkable-2-avis/", "reMarkable 2 — Avis et analyse complète", "Analyse détaillée du reMarkable 2 : écriture, écran, logiciel et limites."),
    ("/marques/remarkable/remarkable-paper-pro-avis/", "reMarkable Paper Pro — Avis et analyse complète", "Analyse du reMarkable Paper Pro : écriture, écran couleur, logiciel et limites."),
    ("/marques/remarkable/abonnement-connect/", "Abonnement reMarkable Connect — Vaut-il le coup ?", "Faut-il souscrire à l'abonnement Connect de reMarkable ? Notre analyse détaillée."),
    ("/marques/remarkable/accessoires/", "Accessoires reMarkable — Stylets, housses et étuis", "Les meilleurs accessoires compatibles avec reMarkable 2 et Paper Pro."),
    ("/marques/remarkable/alternatives/", "Alternatives à reMarkable — Que choisir à la place ?", "Les meilleures alternatives au reMarkable : Boox, Supernote, Kindle Scribe et Kobo Elipsa."),
]

for path, title, desc in REMARKABLE_PAGES:
    crumbs = breadcrumb(("Marques", "/marques/"), ("reMarkable", "/marques/remarkable/"), title.split("—")[0].strip())
    is_test = "avis" in path.lower()
    if is_test:
        product = "reMarkable Paper Pro" if "paper-pro" in path else "reMarkable 2"
        write(path + "index.html", test_page(title, desc, path, crumbs, product))
    else:
        write(path + "index.html", content_page(title, desc, path, crumbs))

# Boox hub
write("/marques/boox/index.html", hub_page(
    "Boox — Tests, comparatifs et guides",
    "Tout sur Boox : Note Air, Tab Ultra, avis, accessoires et alternatives.",
    "/marques/boox/",
    breadcrumb(("Marques", "/marques/"), "Boox"),
    "Le hub Boox : modèles disponibles, tests, comparatifs et accessoires pour tablettes E Ink sous Android.",
    [
        ("Boox Note Air", "/marques/boox/boox-note-air/"),
        ("Boox Tab Ultra", "/marques/boox/boox-tab-ultra/"),
        ("Avis Boox", "/marques/boox/avis/"),
        ("Accessoires Boox", "/marques/boox/accessoires/"),
        ("Alternatives à Boox", "/marques/boox/alternatives/"),
    ]
))

BOOX_PAGES = [
    ("/marques/boox/boox-note-air/", "Boox Note Air — Fiche technique et présentation", "Tout sur le Boox Note Air : caractéristiques, fonctionnalités et avis."),
    ("/marques/boox/boox-tab-ultra/", "Boox Tab Ultra — Fiche technique et présentation", "Le Boox Tab Ultra : la tablette E Ink Android la plus complète du marché."),
    ("/marques/boox/avis/", "Boox — Avis et analyses", "Analyses des tablettes Boox : Note Air, Tab Ultra et comparaisons."),
    ("/marques/boox/accessoires/", "Accessoires Boox — Stylets et housses compatibles", "Les meilleurs accessoires pour vos tablettes Boox."),
    ("/marques/boox/alternatives/", "Alternatives à Boox — Que choisir à la place ?", "Les meilleures alternatives à Boox selon votre usage et votre budget."),
]

for path, title, desc in BOOX_PAGES:
    crumbs = breadcrumb(("Marques", "/marques/"), ("Boox", "/marques/boox/"), title.split("—")[0].strip())
    write(path + "index.html", content_page(title, desc, path, crumbs))

# Simple brand pages
BRAND_SIMPLE = [
    ("/marques/kindle-scribe/", "Kindle Scribe — Tests, avis et comparatifs", "Tout sur le Kindle Scribe : avis, comparatifs et guides d'achat.", "Kindle Scribe"),
    ("/marques/kobo-elipsa/", "Kobo Elipsa — Tests, avis et comparatifs", "Tout sur le Kobo Elipsa : avis, comparatifs et guides d'achat.", "Kobo Elipsa"),
    ("/marques/supernote/", "Supernote — Tests, avis et comparatifs", "Tout sur Supernote : avis, comparatifs et guides d'achat.", "Supernote"),
]

for path, title, desc, brand in BRAND_SIMPLE:
    crumbs = breadcrumb(("Marques", "/marques/"), brand)
    related = {
        "Kindle Scribe": [
            ("Kindle Scribe vs reMarkable", "/comparatifs/kindle-scribe-vs-remarkable/"),
            ("Kindle Scribe vs Kobo Elipsa", "/comparatifs/kindle-scribe-vs-kobo-elipsa/"),
            ("Liseuse ou bloc-notes numérique ?", "/guides/liseuse-ou-bloc-notes-numerique/"),
        ],
        "Kobo Elipsa": [
            ("Kobo Elipsa vs reMarkable", "/comparatifs/kobo-elipsa-vs-remarkable/"),
            ("Kindle Scribe vs Kobo Elipsa", "/comparatifs/kindle-scribe-vs-kobo-elipsa/"),
            ("Lire et prendre des notes", "/usages/lecture-et-prise-de-notes/"),
        ],
        "Supernote": [
            ("reMarkable vs Supernote", "/comparatifs/remarkable-vs-supernote/"),
            ("Boox vs Supernote", "/comparatifs/boox-vs-supernote/"),
            ("Prendre des notes au travail", "/usages/prise-de-notes-professionnelle/"),
        ],
    }
    write(path + "index.html", hub_page(
        title, desc, path, crumbs,
        f"Le hub {brand} : tout ce que vous devez savoir avant d'acheter.",
        related[brand]
    ))

# ── USAGES ────────────────────────────────────────────────────────────────────
write("/usages/index.html", hub_page(
    "Bloc-notes numérique par usage — Guides et recommandations",
    "Trouvez le meilleur bloc-notes numérique selon votre usage : travail, études, annotation PDF, dessin.",
    "/usages/",
    breadcrumb("Par usage"),
    "Chaque usage a ses exigences. Nos recommandations ciblées pour vous aider à faire le bon choix.",
    [
        ("Travail et réunions", "/usages/prise-de-notes-professionnelle/"),
        ("Études et cours", "/usages/prise-de-notes-etudiant/"),
        ("Prise de notes en réunion", "/usages/prise-de-notes-reunion/"),
        ("Annoter des PDF", "/usages/annotation-pdf/"),
        ("Lire et prendre des notes", "/usages/lecture-et-prise-de-notes/"),
        ("Dessiner", "/usages/dessin/"),
        ("Remplacer les cahiers papier", "/usages/remplacer-cahiers-papier/"),
    ]
))

USAGES = [
    ("/usages/prise-de-notes-professionnelle/", "Bloc-notes numérique pour le travail : quels usages et critères ?", "Quand un bloc-notes numérique est-il pertinent au travail ? Workflow, critères, limites et alternatives avant de comparer les modèles."),
    ("/usages/prise-de-notes-etudiant/", "Bloc-notes numérique pour les étudiants : usages, critères et limites", "Cours, PDF, révisions, organisation : dans quels cas un bloc-notes numérique est-il réellement adapté aux études ?"),
    ("/usages/prise-de-notes-reunion/", "Prendre des notes en réunion avec un bloc-notes numérique", "Capture, suivi, recherche et partage : les critères qui déterminent si un bloc-notes numérique convient à vos réunions."),
    ("/usages/annotation-pdf/", "Annoter des PDF sur une tablette E Ink : pour quels usages ?", "Évaluez si l'E Ink convient à vos PDF selon la taille, les formats, l'annotation, l'export et votre workflow documentaire."),
    ("/usages/lecture-et-prise-de-notes/", "Lire et prendre des notes avec une tablette E Ink", "Liseuse à stylet, bloc-notes E Ink ou tablette classique : choisissez selon vos livres, PDF, annotations et besoins d'export."),
    ("/usages/dessin/", "Dessiner sur une tablette E Ink : usages et limites", "Croquis, schémas, calques, couleur et export : quand une tablette E Ink convient-elle au dessin, et quand préférer une tablette graphique ?"),
    ("/usages/remplacer-cahiers-papier/", "Remplacer ses cahiers papier par un bloc-notes numérique", "Quand le numérique simplifie-t-il vraiment la prise de notes ? Capture, classement, sauvegarde, export et limites d'un remplacement du papier."),
]

for path, title, desc in USAGES:
    crumbs = breadcrumb(("Par usage", "/usages/"), title)
    body = USAGE_CONTENT.get(path, "")
    write(path + "index.html", content_page(title, desc, path, crumbs, "Guide", body))

# ── GUIDES ────────────────────────────────────────────────────────────────────
write("/guides/index.html", hub_page(
    "Guides — Choisir et utiliser un bloc-notes numérique",
    "Tous nos guides pour choisir, configurer et utiliser un bloc-notes numérique. Technologie E Ink, formats, export, synchronisation.",
    "/guides/",
    breadcrumb("Guides"),
    "Nos guides pratiques pour comprendre la technologie E Ink et faire le meilleur choix.",
    [
        ("Choisir son bloc-notes numérique", "/guides/choisir-bloc-notes-numerique/"),
        ("Liseuse ou bloc-notes numérique ?", "/guides/liseuse-ou-bloc-notes-numerique/"),
        ("Tablette classique ou E Ink ?", "/guides/tablette-classique-ou-tablette-e-ink/"),
        ("Taille d'écran", "/guides/taille-ecran-bloc-notes-numerique/"),
        ("Couleur ou noir et blanc ?", "/guides/bloc-notes-numerique-couleur-ou-noir-et-blanc/"),
        ("Avec ou sans abonnement ?", "/guides/bloc-notes-numerique-avec-ou-sans-abonnement/"),
        ("Prix et budgets", "/guides/prix-bloc-notes-numerique/"),
        ("Comprendre la technologie E Ink", "/guides/tablette-e-ink/"),
        ("Fonctionnement de l'encre électronique", "/guides/encre-electronique-fonctionnement/"),
        ("Latence et écriture", "/guides/latence-ecriture/"),
        ("OCR et manuscrit", "/guides/ocr-manuscrit/"),
        ("Autonomie des tablettes E Ink", "/guides/autonomie-tablette-e-ink/"),
        ("Formats de fichiers compatibles", "/guides/formats-fichiers-compatibles/"),
        ("Exporter ses notes", "/guides/exporter-notes/"),
        ("Synchronisation cloud", "/guides/synchroniser-notes-cloud/"),
        ("Google Drive", "/guides/bloc-notes-numerique-google-drive/"),
        ("OneDrive", "/guides/bloc-notes-numerique-onedrive/"),
        ("Dropbox", "/guides/bloc-notes-numerique-dropbox/"),
        ("Écosystème ouvert ou fermé ?", "/guides/ecosysteme-ouvert-ou-ferme/"),
        ("Annoter des PDF sur tablette E Ink", "/guides/annoter-pdf-tablette-e-ink/"),
        ("Convertir notes manuscrites en texte", "/guides/convertir-notes-manuscrites-en-texte/"),
        ("Organiser ses notes numériques", "/guides/organiser-notes-numeriques/"),
        ("Transférer ses notes vers l'ordinateur", "/guides/transfert-notes-vers-ordinateur/"),
        ("Imprimer ses notes numériques", "/guides/imprimer-notes-numeriques/"),
    ]
))

GUIDES = [
    ("/guides/choisir-bloc-notes-numerique/", "Comment choisir son bloc-notes numérique selon son usage ?", "Choisissez un bloc-notes numérique selon vos documents, vos exports, votre usage du stylet, la taille d’écran et le coût total des accessoires à prévoir."),
    ("/guides/liseuse-ou-bloc-notes-numerique/", "Liseuse ou bloc-notes numérique : quelles différences ?", "Comparez liseuse et bloc-notes numérique selon la lecture, l’écriture au stylet, les PDF, le format de l’appareil et les possibilités d’export de notes."),
    ("/guides/tablette-classique-ou-tablette-e-ink/", "Tablette classique ou tablette E Ink : laquelle choisir ?", "Comparez tablette classique et tablette E Ink selon l’écriture, la lecture, la couleur, les applications, la vidéo et les contraintes d’export de fichiers."),
    ("/guides/taille-ecran-bloc-notes-numerique/", "Quelle taille d’écran pour un bloc-notes numérique ?", "Comparez les formats compacts, 10 pouces et grands écrans selon vos notes, vos PDF, vos déplacements et la surface réellement disponible pour bien écrire."),
    ("/guides/bloc-notes-numerique-couleur-ou-noir-et-blanc/", "Bloc-notes numérique couleur ou noir et blanc : le choix", "Choisissez entre écran E Ink couleur et noir et blanc selon vos documents, vos codes visuels, le contraste attendu et votre usage quotidien du stylet."),
    ("/guides/bloc-notes-numerique-avec-ou-sans-abonnement/", "Bloc-notes numérique avec ou sans abonnement : choisir", "Identifiez les fonctions disponibles sans abonnement, les services payants, les limites du cloud et le coût récurrent avant de choisir votre appareil."),
    ("/guides/prix-bloc-notes-numerique/", "Prix d’un bloc-notes numérique : quel budget prévoir ?", "Calculez le prix réel d’un bloc-notes numérique avec le stylet, la protection, les accessoires, les services éventuels et la durée d’utilisation prévue."),
    ("/guides/tablette-e-ink/", "Comprendre la technologie E Ink", "Qu'est-ce qu'une tablette E Ink ? Fonctionnement, avantages et limites expliqués simplement."),
    ("/guides/encre-electronique-fonctionnement/", "Comment fonctionne l'encre électronique ?", "Le principe de l'encre électronique expliqué : microcapsules, bistabilité et consommation énergétique."),
    ("/guides/latence-ecriture/", "Latence d'écriture sur tablette E Ink — Ce qu'il faut savoir", "Qu'est-ce que la latence d'écriture et comment impacte-t-elle votre expérience ?"),
    ("/guides/ocr-manuscrit/", "OCR et reconnaissance de l'écriture manuscrite", "Comment fonctionne la reconnaissance de texte manuscrit sur les tablettes E Ink ?"),
    ("/guides/autonomie-tablette-e-ink/", "Autonomie des tablettes E Ink — Ce qu'il faut savoir", "Combien de temps dure la batterie d'un bloc-notes numérique ? Notre guide complet."),
    ("/guides/formats-fichiers-compatibles/", "Formats de fichiers compatibles avec les bloc-notes numériques", "PDF, EPUB, DOCX, PNG : quels formats acceptent les tablettes E Ink ?"),
    ("/guides/exporter-notes/", "Comment exporter ses notes depuis un bloc-notes numérique ?", "Toutes les méthodes pour exporter, sauvegarder et partager vos notes numériques."),
    ("/guides/synchroniser-notes-cloud/", "Synchronisation cloud des notes — Guide complet", "Comment synchroniser vos notes numériques avec le cloud ? Toutes les solutions."),
    ("/guides/bloc-notes-numerique-google-drive/", "Bloc-notes numérique et Google Drive — Compatibilité", "Quelles tablettes E Ink fonctionnent avec Google Drive ? Notre guide de compatibilité."),
    ("/guides/bloc-notes-numerique-onedrive/", "Bloc-notes numérique et OneDrive — Compatibilité", "Quelles tablettes E Ink sont compatibles avec Microsoft OneDrive ?"),
    ("/guides/bloc-notes-numerique-dropbox/", "Bloc-notes numérique et Dropbox — Compatibilité", "Quelles tablettes E Ink fonctionnent avec Dropbox ?"),
    ("/guides/ecosysteme-ouvert-ou-ferme/", "Écosystème ouvert ou fermé — Quelle tablette choisir ?", "Android ouvert (Boox) vs écosystème propriétaire (reMarkable) : les vraies différences."),
    ("/guides/annoter-pdf-tablette-e-ink/", "Annoter des PDF sur tablette E Ink — Guide pratique", "Comment annoter efficacement des PDF sur votre tablette E Ink ? Toutes les méthodes."),
    ("/guides/convertir-notes-manuscrites-en-texte/", "Convertir ses notes manuscrites en texte", "Comment transformer votre écriture manuscrite en texte numérique grâce à l'OCR ?"),
    ("/guides/organiser-notes-numeriques/", "Organiser ses notes numériques efficacement", "Dossiers, tags, liens : comment structurer vos notes pour retrouver facilement l'information."),
    ("/guides/transfert-notes-vers-ordinateur/", "Transférer ses notes vers l'ordinateur", "Comment envoyer vos notes depuis votre tablette E Ink vers votre ordinateur ?"),
    ("/guides/imprimer-notes-numeriques/", "Imprimer ses notes numériques", "Comment imprimer les notes créées sur un bloc-notes numérique ?"),
]

GUIDE_CONTENT = {
    "/guides/taille-ecran-bloc-notes-numerique/": """
      <p class="article-answer"><strong>Un écran d’environ 10 pouces offre le compromis le plus courant pour écrire et annoter des PDF.</strong> Un format proche de 7 pouces se transporte mieux, tandis qu’un écran de 11 à 13 pouces donne plus d’espace aux grands documents. La bonne taille dépend toutefois de la page affichée, du poids et de l’encombrement acceptables.</p>

      <h2 id="mesure">La diagonale ne suffit pas</h2>
      <p>La taille annoncée mesure l’écran en diagonale. Elle ne décrit ni ses proportions, ni les bordures, ni l’espace occupé par l’interface. Deux appareils ayant une diagonale proche peuvent donc afficher un document différemment.</p>
      <p>Pour comparer, ouvrez un document représentatif et regardez la largeur de texte obtenue à un niveau de zoom lisible. Cette vérification est plus utile qu’une comparaison abstraite entre pouces et formats de papier.</p>

      <h2 id="formats">Quel format pour quel usage ?</h2>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Taille indicative</th><th>Usage cohérent</th><th>Compromis</th></tr></thead>
        <tbody>
          <tr><td>7 à 8 pouces</td><td>notes brèves, listes, journal et mobilité</td><td>peu d’espace pour les PDF complexes</td></tr>
          <tr><td>Environ 10 pouces</td><td>réunions, cours, carnets et PDF courants</td><td>lecture de documents A4 parfois zoomée</td></tr>
          <tr><td>11 à 13 pouces</td><td>articles, partitions, plans et travail proche de l’A4</td><td>poids, prix et transport plus contraignants</td></tr>
        </tbody>
      </table></div>

      <h2 id="reperes">Trois repères concrets</h2>
      <p>Les gammes actuelles illustrent l’écart entre les formats. reMarkable indique 7,3 pouces pour le Paper Pro Move, 10,3 pouces pour le reMarkable 2 et 11,8 pouces pour le Paper Pro. Ces exemples servent de repères de taille, pas de recommandation de modèle.</p>
      <p>Un petit écran peut convenir à une écriture linéaire, mais devient vite étroit pour afficher deux zones, une grande marge d’annotation ou une page de manuel. À l’inverse, une grande surface perd son intérêt si l’appareil reste à la maison parce qu’il est trop encombrant.</p>

      <h2 id="test">Testez votre document avant l’achat</h2>
      <ol>
        <li>Choisissez le PDF ou le modèle de page que vous utilisez le plus souvent.</li>
        <li>Relevez ses proportions et la taille minimale de texte encore confortable pour vous.</li>
        <li>Vérifiez sur une démonstration ou dans le manuel du produit si la page exige un zoom fréquent.</li>
        <li>Ajoutez l’étui et le stylet lorsque vous comparez poids et dimensions de transport.</li>
      </ol>

      <h2 id="decision">La règle de décision</h2>
      <p>Choisissez le plus petit écran qui affiche correctement votre document principal. Vous évitez ainsi de payer et de transporter une surface inutilisée. Si vous annotez régulièrement des PDF proches de l’A4, le grand format mérite d’être examiné ; pour des carnets et des réunions, 10 pouces reste un point de départ plus équilibré.</p>
      <p>Vous pouvez ensuite vérifier les autres critères dans le guide pour <a href="/guides/choisir-bloc-notes-numerique/">choisir un bloc-notes numérique</a> et comparer <a href="/guides/prix-bloc-notes-numerique/">le budget total</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/s/article/About-reMarkable-Paper-Pro-Move" rel="noopener noreferrer">reMarkable : dimensions du Paper Pro Move</a></li>
        <li><a href="https://support.remarkable.com/s/article/About-reMarkable-2" rel="noopener noreferrer">reMarkable : dimensions du reMarkable 2</a></li>
        <li><a href="https://support.remarkable.com/s/article/About-reMarkable-Paper-Pro" rel="noopener noreferrer">reMarkable : dimensions du Paper Pro</a></li>
      </ul>
    """,
    "/guides/bloc-notes-numerique-couleur-ou-noir-et-blanc/": """
      <p class="article-answer"><strong>Choisissez la couleur si elle transporte une information que vous utilisez vraiment : légende, correction, priorité ou catégorie.</strong> Pour des notes textuelles, des romans et des documents conçus en noir et blanc, un écran monochrome reste souvent suffisant.</p>

      <h2 id="difference">La couleur E Ink n’est pas celle d’une tablette classique</h2>
      <p>Un écran E Ink couleur vise la lecture et l’annotation de contenus relativement statiques. Il ne faut pas attendre le même rendu qu’un écran LCD ou OLED destiné aux photos et à la vidéo. La technologie Kaleido 3 annoncée par E Ink affiche par exemple une définition différente en noir et blanc et en couleur : jusqu’à 300 ppp pour le premier, 150 ppp pour la seconde.</p>
      <p>D’autres technologies couleur existent. Le reMarkable Paper Pro emploie un écran couleur de 11,8 pouces, tandis que le reMarkable 2 reste monochrome. Il faut donc comparer le rendu du modèle précis, pas attribuer les mêmes propriétés à tous les écrans E Ink.</p>

      <h2 id="usages">Quand la couleur apporte quelque chose</h2>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Document</th><th>Couleur utile si…</th><th>Noir et blanc suffisant si…</th></tr></thead>
        <tbody>
          <tr><td>Cours ou rapport</td><td>les surlignages indiquent une priorité</td><td>la structure repose sur les titres et annotations</td></tr>
          <tr><td>Schéma ou carte</td><td>la légende distingue des catégories</td><td>formes et textures restent compréhensibles</td></tr>
          <tr><td>Agenda</td><td>chaque couleur correspond à un type d’activité</td><td>une seule hiérarchie visuelle suffit</td></tr>
          <tr><td>Photo ou création</td><td>la couleur sert seulement de repère</td><td>la fidélité du rendu est indispensable : préférez alors LCD/OLED</td></tr>
        </tbody>
      </table></div>

      <h2 id="test">Faites le test en niveaux de gris</h2>
      <p>Prenez trois documents habituels et convertissez-les en niveaux de gris. Si une légende disparaît, si deux courbes deviennent impossibles à distinguer ou si vos corrections perdent leur fonction, la couleur a une valeur concrète. Si le document reste parfaitement exploitable, elle constitue surtout une préférence.</p>
      <p>Vérifiez ensuite l’éclairage, la définition annoncée pour la couleur et les options d’export. Une annotation colorée peut rester utile dans le fichier exporté, même si son affichage sur l’appareil paraît plus discret.</p>

      <h2 id="decision">Choisir sans surpayer une fonction décorative</h2>
      <p>La couleur se justifie lorsque vous pouvez nommer le code visuel qu’elle préserve. Sinon, comparez d’abord le contraste, la taille, le logiciel et le prix total. Pour un besoin de vidéo, de photographie ou de création graphique fidèle, consultez plutôt la comparaison entre <a href="/guides/tablette-classique-ou-tablette-e-ink/">tablette classique et tablette E Ink</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://www.eink.com/brand/detail/Kaleido3" rel="noopener noreferrer">E Ink : caractéristiques de Kaleido 3</a></li>
        <li><a href="https://support.remarkable.com/s/article/About-reMarkable-Paper-Pro" rel="noopener noreferrer">reMarkable : écran couleur du Paper Pro</a></li>
        <li><a href="https://support.remarkable.com/s/article/About-reMarkable-2" rel="noopener noreferrer">reMarkable : écran monochrome du reMarkable 2</a></li>
      </ul>
    """,
    "/guides/bloc-notes-numerique-avec-ou-sans-abonnement/": """
      <p class="article-answer"><strong>Un abonnement n’est acceptable que s’il finance une fonction dont vous avez besoin chaque mois.</strong> Avant l’achat, vérifiez que l’écriture, l’accès local aux notes, l’export et la sauvegarde minimale restent possibles sans paiement récurrent.</p>

      <h2 id="types">De quel abonnement parle-t-on ?</h2>
      <p>Il faut distinguer le service lié à l’appareil d’un abonnement de livres ou d’un forfait mobile. Pour un bloc-notes numérique, le coût récurrent peut couvrir davantage de stockage cloud, des fonctions dans les applications, une conversion avancée ou une protection supplémentaire. Il ne devrait pas être confondu avec Kindle Unlimited, Audible ou une carte SIM.</p>

      <h2 id="verifier">Les fonctions à vérifier sans formule payante</h2>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Fonction</th><th>Question à poser</th><th>Risque si elle dépend du paiement</th></tr></thead>
        <tbody>
          <tr><td>Accès aux notes</td><td>restent-elles lisibles et modifiables sur l’appareil ?</td><td>dépendance pour un usage de base</td></tr>
          <tr><td>Export</td><td>peut-on récupérer PDF, image ou texte ?</td><td>données difficiles à déplacer</td></tr>
          <tr><td>Synchronisation</td><td>quels appareils, délais et quotas sont inclus ?</td><td>historique incomplet ou transfert manuel</td></tr>
          <tr><td>Conversion</td><td>l’écriture manuscrite vers le texte est-elle incluse ?</td><td>coût récurrent pour une fonction de travail</td></tr>
          <tr><td>Sauvegarde</td><td>existe-t-il une copie locale ou un export de secours ?</td><td>perte d’accès en cas de changement d’offre</td></tr>
        </tbody>
      </table></div>

      <h2 id="exemple">L’exemple de reMarkable Connect</h2>
      <p>reMarkable documente séparément les fonctions de Connect et celles disponibles sans abonnement. Sans Connect, l’appareil conserve notamment des intégrations avec Google Drive, Dropbox et OneDrive, tandis que l’offre payante ajoute des services tels que le stockage cloud illimité et des fonctions dans les applications reMarkable. Cette répartition peut évoluer ; consultez les deux pages officielles le jour de l’achat.</p>

      <h2 id="calcul">Calculez le coût sur votre durée d’usage</h2>
      <p>Multipliez le tarif mensuel par le nombre de mois pendant lesquels vous pensez garder l’appareil. Ajoutez ce montant au prix du matériel et des accessoires. Le tarif Connect affiché sur la boutique reMarkable lors de notre consultation était de 3,99 € par mois après la période d’essai, soit 143,64 € sur trois ans si le prix ne change pas.</p>
      <p>Ce calcul n’est pas une prévision : reMarkable a déjà annoncé une modification de tarif en mars 2026. Il montre seulement pourquoi un faible montant mensuel doit apparaître dans la comparaison initiale.</p>

      <h2 id="decision">La règle de décision</h2>
      <p>Simulez une semaine de travail sans abonnement. Si une tâche essentielle devient impossible, comparez le coût total ou choisissez un écosystème différent. Si seules des fonctions de confort disparaissent, vous pourrez décider après l’achat sans rendre vos notes dépendantes du paiement.</p>
      <p>Poursuivez avec les guides sur le <a href="/guides/prix-bloc-notes-numerique/">prix total</a>, l’<a href="/guides/exporter-notes/">export des notes</a> et la <a href="/guides/synchroniser-notes-cloud/">synchronisation cloud</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/s/article/About-Connect-Subscription" rel="noopener noreferrer">reMarkable : fonctions de Connect</a></li>
        <li><a href="https://support.remarkable.com/s/article/Using-reMarkable-without-a-subscription" rel="noopener noreferrer">reMarkable : utilisation sans abonnement</a></li>
        <li><a href="https://support.remarkable.com/s/article/Changes-to-Connect-subscription-pricing" rel="noopener noreferrer">reMarkable : modification du tarif Connect en 2026</a></li>
        <li><a href="https://remarkable.com/shop" rel="noopener noreferrer">reMarkable : tarif affiché lors de la consultation du 8 septembre 2026</a></li>
      </ul>
    """,
    "/guides/prix-bloc-notes-numerique/": """
      <p class="article-answer"><strong>Le prix d’un bloc-notes numérique se compare comme une configuration prête à l’emploi, pas comme un appareil nu.</strong> Comptez l’appareil, le stylet nécessaire, la protection si vous le transportez, les consommables et les services payants que votre usage exige. Deux modèles affichés au même prix peuvent donc représenter des budgets très différents.</p>

      <h2 id="combien">Combien coûte réellement un bloc-notes numérique ?</h2>
      <p>Il n’existe pas un prix unique qui résume le marché. Le format de l’écran, la couleur, les accessoires inclus et l’écosystème logiciel changent fortement le montant à prévoir. Pour cadrer le budget sans fabriquer une moyenne, le plus fiable consiste à partir de configurations officielles datées.</p>

      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Repère officiel au 8 septembre 2026</th><th>Prix affiché</th><th>Ce que ce prix permet de comprendre</th></tr></thead>
        <tbody>
          <tr><td>Kobo Elipsa 2E</td><td>399,99 €</td><td>un appareil 10,3 pouces peut démarrer autour de 400 €, avant d’ajouter les accessoires de transport non inclus dans le panier choisi</td></tr>
          <tr><td>reMarkable Paper Pure</td><td>à partir de 399 €</td><td>le Marker est inclus dans le prix de départ affiché par reMarkable</td></tr>
          <tr><td>reMarkable Paper Pro avec Marker Plus</td><td>699 €</td><td>un grand écran couleur et un stylet plus complet font monter nettement le budget</td></tr>
          <tr><td>reMarkable Paper Pro avec Book Folio</td><td>849 €</td><td>la protection officielle peut modifier fortement le prix d’une configuration prête à transporter</td></tr>
          <tr><td>reMarkable Paper Pro avec Type Folio</td><td>899 €</td><td>un clavier transforme le panier en outil de saisie plus polyvalent, avec un surcoût important</td></tr>
        </tbody>
      </table></div>

      <p>Ces montants sont des instantanés de boutiques officielles, pas une fourchette garantie. Ils montrent surtout pourquoi il faut comparer le contenu du panier. Le Kobo Elipsa 2E SleepCover était par exemple affiché séparément à 69,99 € lors de la même vérification. Un acheteur qui veut protéger l’appareil pendant les déplacements doit donc intégrer cette dépense au lieu de comparer uniquement les 399,99 € de l’appareil.</p>

      <h2 id="formule">Les postes à intégrer dans votre budget</h2>
      <p>Votre coût total correspond au prix du matériel réellement nécessaire, auquel s’ajoutent les coûts récurrents pendant la durée d’utilisation prévue. Un accessoire n’a pas à entrer dans le calcul s’il ne sert pas à votre scénario.</p>

      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Poste</th><th>À vérifier</th><th>Quand il change la décision</th></tr></thead>
        <tbody>
          <tr><td>Appareil</td><td>taille, version, stockage et génération exacte</td><td>toujours</td></tr>
          <tr><td>Stylet</td><td>inclus ou non, gomme, boutons, recharge</td><td>dès que l’écriture manuscrite est centrale</td></tr>
          <tr><td>Protection</td><td>étui officiel ou compatible, maintien du stylet</td><td>si l’appareil voyage régulièrement</td></tr>
          <tr><td>Pointes</td><td>nombre fourni, compatibilité et prix du remplacement</td><td>pour certains stylets en usage intensif</td></tr>
          <tr><td>Abonnement</td><td>fonction concernée, tarif mensuel ou annuel, période d’essai</td><td>si une fonction de travail dépend du service</td></tr>
          <tr><td>Clavier</td><td>compatibilité, disposition et protection intégrée</td><td>si vous tapez fréquemment de longs textes</td></tr>
        </tbody>
      </table></div>

      <p>La formule de comparaison reste simple : <strong>coût total = appareil + accessoires indispensables + consommables + abonnements sur la durée retenue.</strong> Cette méthode évite qu’un prix d’appel avantage artificiellement un modèle dont le stylet, l’étui ou une fonction logicielle essentielle sont facturés séparément.</p>

      <h2 id="paniers">Comparez des configurations équivalentes</h2>
      <p>Une comparaison utile part de la même tâche. Si vous cherchez un appareil pour les réunions, comparez par exemple chaque modèle avec le stylet nécessaire et une protection de transport. Si vous annotez de grands PDF au bureau, un étui peut être secondaire mais la taille d’écran devient prioritaire.</p>

      <ol>
        <li>Définissez les deux ou trois tâches que l’appareil doit remplacer.</li>
        <li>Choisissez la taille et les fonctions indispensables à ces tâches.</li>
        <li>Ajoutez uniquement les accessoires nécessaires pour obtenir cette configuration.</li>
        <li>Intégrez les services payants si une fonction importante en dépend.</li>
        <li>Comparez ensuite les totaux, pas les prix d’appel.</li>
      </ol>

      <p>Les bundles officiels illustrent bien l’écart possible à produit presque identique. Pour le Paper Pro, reMarkable affichait 699 € avec Marker Plus, 849 € avec Book Folio et 899 € avec Type Folio. Le bon panier dépend donc moins du nombre d’accessoires que de ceux que vous utiliserez vraiment.</p>

      <h2 id="duree">Prix d’achat ou coût sur plusieurs années ?</h2>
      <p>Un abonnement modeste peut devenir visible sur trois ou quatre ans. Sur la boutique reMarkable en zone euro consultée le 8 septembre 2026, Connect était affiché à 3,99 € par mois ou 39,90 € par an après la période d’essai. À tarif inchangé, cela représenterait 143,64 € sur trois ans en paiement mensuel, ou 119,70 € avec trois années facturées au tarif annuel.</p>
      <p>Ce calcul n’est pas une prévision de prix. Il sert à montrer l’effet d’un coût récurrent sur le panier initial. Avant d’ajouter un abonnement, vérifiez quelles fonctions restent disponibles gratuitement et lesquelles vous utiliserez réellement. Le guide <a href="/guides/bloc-notes-numerique-avec-ou-sans-abonnement/">bloc-notes numérique avec ou sans abonnement</a> détaille cette vérification.</p>

      <h2 id="payer-plus">Quand vaut-il la peine de payer plus cher ?</h2>
      <p>Un surcoût est défendable lorsqu’il supprime une contrainte concrète. Un grand écran peut éviter des zooms permanents sur des PDF, la couleur peut préserver des légendes indispensables, un clavier peut remplacer une partie de la saisie sur ordinateur et un logiciel plus ouvert peut être nécessaire pour une application métier.</p>
      <p>À l’inverse, payer davantage pour une fonction rarement utilisée ne rend pas l’appareil plus adapté. Si vos notes sont surtout textuelles et que vous exportez quelques PDF, un écran couleur ou un clavier coûteux peut rester sans effet sur votre travail quotidien.</p>

      <h2 id="economiser">Économiser sans déplacer le problème</h2>
      <p>Le prix le plus bas n’est intéressant que si l’appareil couvre déjà votre besoin. Une économie sur le matériel peut disparaître si vous devez acheter un stylet, une protection ou un service supplémentaire juste après la commande.</p>
      <p>Commencez donc par éliminer les fonctions inutiles, puis comparez les paniers restants. Une taille d’écran plus petite peut réduire le budget si elle affiche correctement vos documents. À l’inverse, acheter trop compact pour de grands PDF peut vous pousser à remplacer l’appareil plus tôt. Notre guide sur la <a href="/guides/taille-ecran-bloc-notes-numerique/">taille d’écran d’un bloc-notes numérique</a> aide à trancher ce point avant de regarder les promotions.</p>

      <h2 id="suite">Quel comparatif consulter selon votre budget ?</h2>
      <p>Une fois votre panier cible défini, passez au comparatif correspondant à votre contrainte. Les <a href="/comparatifs/bloc-notes-numerique-pas-cher/">bloc-notes numériques pas chers</a> servent à chercher une configuration accessible, tandis que le <a href="/comparatifs/meilleur-bloc-notes-numerique/">comparatif général des bloc-notes numériques</a> permet d’arbitrer entre plusieurs usages. Si vous refusez tout coût récurrent, consultez directement les <a href="/comparatifs/bloc-notes-numerique-sans-abonnement/">modèles sans abonnement</a>.</p>
      <p>Les réductions temporaires, elles, restent séparées de ce guide. Elles sont regroupées dans les <a href="/bons-plans/bloc-notes-numerique/">bons plans bloc-notes numériques</a> afin de ne pas confondre budget structurel et promotion du moment.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://ereader.kobo.com/fr-fr/products/kobo-elipsa-2e" rel="noopener noreferrer">Kobo France : Kobo Elipsa 2E, prix affiché le 8 septembre 2026</a></li>
        <li><a href="https://ereader.kobo.com/fr-fr/products/kobo-elipsa-2e-sleepcover-black" rel="noopener noreferrer">Kobo France : SleepCover Elipsa 2E, prix affiché le 8 septembre 2026</a></li>
        <li><a href="https://remarkable.com/fr-FR/shop/compare" rel="noopener noreferrer">reMarkable : comparaison des tablettes et prix de départ du Paper Pure</a></li>
        <li><a href="https://remarkable.com/fr-FR/products/remarkable-paper/pro?region_id=000250" rel="noopener noreferrer">reMarkable : configurations et prix du Paper Pro</a></li>
        <li><a href="https://remarkable.com/de-AT/shop/connect" rel="noopener noreferrer">reMarkable : tarif Connect en zone euro consulté le 8 septembre 2026</a></li>
      </ul>
    """,
    "/guides/choisir-bloc-notes-numerique/": """
      <p class="article-answer"><strong>Pour choisir un bloc-notes numérique, partez de votre flux de travail.</strong> Repérez les documents que vous utilisez, leur destination après annotation et les services cloud indispensables. Vous pourrez ensuite comparer la taille de l’écran, le stylet et l’autonomie sans vous laisser guider par une fiche technique trop longue.</p>

      <h2 id="questions">Les cinq questions à trancher avant l’achat</h2>
      <ol>
        <li><strong>Écrivez-vous surtout des notes libres ou annotez-vous des PDF ?</strong> Un carnet de réunion et un article scientifique au format A4 n’imposent pas la même surface d’écran.</li>
        <li><strong>Où les notes doivent-elles arriver ?</strong> Listez les formats et destinations nécessaires : PDF, image, texte converti, ordinateur, Google Drive, OneDrive ou Dropbox.</li>
        <li><strong>Avez-vous besoin d’applications tierces ?</strong> Un système volontairement limité réduit les distractions ; un appareil Android accepte davantage d’outils, avec plus de réglages et de complexité.</li>
        <li><strong>Lisez-vous autant que vous écrivez ?</strong> L’accès aux livres, les formats pris en charge et la gestion des annotations varient fortement selon l’écosystème.</li>
        <li><strong>Quel coût total acceptez-vous ?</strong> Ajoutez au prix de l’appareil le stylet, l’étui, les pointes et les éventuels services récurrents.</li>
      </ol>

      <h2 id="criteres">Les critères qui changent vraiment le choix</h2>
      <div class="table-wrapper">
        <table class="comp-table">
          <thead><tr><th>Critère</th><th>À privilégier si…</th><th>Point à vérifier</th></tr></thead>
          <tbody>
            <tr><td>Taille d’écran</td><td>vous consultez de grands PDF ou écrivez côte à côte</td><td>dimensions réelles de la zone d’écriture, poids et encombrement</td></tr>
            <tr><td>Éclairage</td><td>vous lisez souvent le soir ou dans une pièce sombre</td><td>présence d’un éclairage frontal et effet éventuel sur l’épaisseur</td></tr>
            <tr><td>Couleur</td><td>vos schémas ou documents reposent sur des codes couleur</td><td>rendu plus discret que sur un écran LCD/OLED</td></tr>
            <tr><td>Logiciel</td><td>vous avez un flux de travail précis</td><td>export, synchronisation, OCR, recherche et applications disponibles</td></tr>
            <tr><td>Stylet</td><td>vous écrivez plusieurs heures par jour</td><td>stylet inclus, gomme, boutons, pointes et coût de remplacement</td></tr>
          </tbody>
        </table>
      </div>

      <p>La fiche technique ne permet pas, à elle seule, de juger la sensation d’écriture. La latence perçue, le frottement de la pointe et le bruit dépendent du couple écran–stylet et des préférences de chacun. Sans essai direct, il est plus honnête de comparer les fonctions vérifiables que de promettre une sensation « identique au papier ».</p>

      <h2 id="ecosysteme">Écosystème fermé ou tablette E Ink ouverte ?</h2>
      <p>Un appareil spécialisé comme reMarkable concentre l’expérience sur les carnets, les documents et ses propres applications. Une tablette BOOX récente repose sur Android et peut intégrer Google Play, ce qui élargit le choix d’applications. Cette ouverture ne garantit toutefois pas que chaque application soit agréable sur un écran à rafraîchissement lent.</p>
      <p>La compatibilité avec votre manière de travailler doit décider. Avant d’acheter, suivez un document pendant tout son parcours : réception, annotation, classement, export, puis ouverture sur l’ordinateur d’un collègue. Un blocage à l’une de ces étapes suffit à écarter le modèle.</p>

      <h2 id="profils">Quel profil vous ressemble ?</h2>
      <ul>
        <li><strong>Réunions et concentration :</strong> recherchez une interface simple, une sortie PDF fiable et une organisation claire des carnets.</li>
        <li><strong>Études et recherche :</strong> privilégiez un écran assez grand, l’annotation de PDF, la recherche et une méthode d’export exploitable sur ordinateur.</li>
        <li><strong>Lecture dominante :</strong> vérifiez d’abord la librairie, les formats de livres et le confort de prise en main. Une liseuse avec stylet peut suffire.</li>
        <li><strong>Applications et polyvalence :</strong> une tablette E Ink Android est plus flexible, mais demande davantage de configuration.</li>
        <li><strong>Couleur et multimédia :</strong> si la fidélité des couleurs, la vidéo ou la navigation fluide sont prioritaires, une tablette classique reste généralement plus adaptée.</li>
      </ul>

      <h2 id="erreurs">Trois erreurs fréquentes</h2>
      <p>La première erreur consiste à choisir sur l’autonomie annoncée. Les fabricants l’expriment souvent en semaines, alors que le Wi-Fi, l’éclairage, la fréquence d’écriture et la synchronisation modifient le résultat réel.</p>
      <p>La deuxième consiste à confondre stockage et portabilité des notes. Beaucoup d’espace ne sert pas si les fichiers restent difficiles à sortir de l’écosystème.</p>
      <p>Enfin, un modèle très polyvalent n’est pas toujours le plus pratique. Plus d’applications peut aussi apporter davantage de réglages et de distractions. Une fonction compte seulement si elle améliore un usage régulier.</p>

      <h2 id="checklist">Checklist finale</h2>
      <p>Avant la commande, notez vos trois tâches principales et vérifiez-les dans la documentation du modèle. Confirmez ensuite le format d’export, le service cloud, les accessoires inclus, l’éclairage, le poids et les conditions de l’abonnement éventuel. Si un seul de ces points est bloquant, éliminez le modèle avant de comparer les détails secondaires.</p>
      <p>Pour poursuivre, consultez nos guides sur la <a href="/guides/taille-ecran-bloc-notes-numerique/">taille d’écran</a>, les <a href="/guides/formats-fichiers-compatibles/">formats compatibles</a> et le choix entre <a href="/guides/ecosysteme-ouvert-ou-ferme/">écosystème ouvert ou fermé</a>.</p>

      <h2 id="sources">Sources consultées</h2>
      <ul class="source-list">
        <li><a href="https://support.remarkable.com/s/article/About-reMarkable-2" rel="noopener noreferrer">reMarkable Support : caractéristiques du reMarkable 2</a></li>
        <li><a href="https://shop.boox.com/products/go103" rel="noopener noreferrer">BOOX : caractéristiques officielles du Go 10.3</a></li>
        <li><a href="https://help.kobo.com/hc/fr/articles/1500001927562-Annoter-votre-livre-avec-le-stylet-Kobo" rel="noopener noreferrer">Kobo : annotation avec le Kobo Stylus</a></li>
        <li><a href="https://www.amazon.com/gp/help/customer/display.html?nodeId=T4sq0EZZFwu9vvH3Fx" rel="noopener noreferrer">Amazon : fonctions du Kindle Scribe</a></li>
      </ul>
    """,
    "/guides/liseuse-ou-bloc-notes-numerique/": """
      <p class="article-answer"><strong>Choisissez une liseuse si votre priorité est de lire ; choisissez un bloc-notes numérique si vous devez écrire régulièrement, organiser des carnets ou annoter des documents.</strong> Certains appareils hybrides savent faire les deux, mais leur orientation principale reste déterminante pour le confort quotidien.</p>

      <h2 id="difference">La différence essentielle</h2>
      <p>Une liseuse est conçue autour du livre numérique : bibliothèque, lecture prolongée, navigation dans un ouvrage et prise en main légère. Un bloc-notes numérique est organisé autour de la page de travail : carnets, stylet, classement, annotation et export.</p>
      <p>Les deux familles peuvent utiliser un écran à encre électronique. Leur format physique, leur logiciel, leur stylet et la circulation des fichiers déterminent donc l’expérience quotidienne.</p>

      <h2 id="tableau">Liseuse ou bloc-notes : comparaison rapide</h2>
      <div class="table-wrapper">
        <table class="comp-table">
          <thead><tr><th>Besoin</th><th>Liseuse</th><th>Bloc-notes numérique</th></tr></thead>
          <tbody>
            <tr><td>Lire des romans</td><td>Usage central, format souvent plus léger</td><td>Possible, mais appareil plus grand</td></tr>
            <tr><td>Prendre des notes longues</td><td>Limité ou secondaire selon le modèle</td><td>Usage central avec carnets et outils d’écriture</td></tr>
            <tr><td>Annoter des PDF</td><td>Possible sur certains modèles</td><td>Généralement mieux adapté, surtout avec grand écran</td></tr>
            <tr><td>Transport quotidien</td><td>Souvent plus compact</td><td>Plus encombrant en 10 pouces et au-delà</td></tr>
            <tr><td>Exporter et partager</td><td>Dépend fortement de l’écosystème</td><td>Fonction importante, mais méthodes variables</td></tr>
          </tbody>
        </table>
      </div>

      <h2 id="hybrides">Les appareils hybrides changent-ils la réponse ?</h2>
      <p>Oui, partiellement. Le Kindle Scribe et le Kobo Elipsa associent lecture et stylet. Kobo permet par exemple d’annoter des EPUB, des Kobo EPUB et des PDF non protégés avec les modèles compatibles. Le Kindle Scribe propose des carnets en plus de l’environnement Kindle. Ces appareils conviennent lorsque la lecture reste importante mais que l’écriture n’est plus occasionnelle.</p>
      <p>Un hybride ne supprime pas les compromis. Vérifiez la taille, le poids, les formats acceptés, la manière d’écrire dans les livres et surtout l’export des annotations. La présence d’un stylet ne signifie pas que toutes les notes pourront être récupérées dans le format souhaité.</p>

      <h2 id="choisir-liseuse">Choisissez plutôt une liseuse si…</h2>
      <ul>
        <li>vous lisez principalement des romans et peu de grands PDF ;</li>
        <li>vous voulez tenir facilement l’appareil à une main ;</li>
        <li>vos annotations restent liées aux livres ;</li>
        <li>vous n’avez pas besoin de carnets complexes ou d’un flux de travail professionnel.</li>
      </ul>

      <h2 id="choisir-bloc-notes">Choisissez plutôt un bloc-notes numérique si…</h2>
      <ul>
        <li>l’écriture manuscrite est une activité quotidienne ;</li>
        <li>vous travaillez sur des supports de cours, contrats ou articles en PDF ;</li>
        <li>vous avez besoin de dossiers, modèles de pages, conversion en texte ou partage régulier ;</li>
        <li>vous acceptez un format plus grand pour obtenir une surface d’écriture confortable.</li>
      </ul>

      <h2 id="decision">La méthode la plus simple pour décider</h2>
      <p>Pendant une semaine, comptez les séances de lecture et d’écriture que remplacerait l’appareil. Si la lecture représente nettement la majorité et que vos notes sont brèves, commencez par une liseuse. Si vous remplissez plusieurs pages, annotez des documents ou devez envoyer vos notes à d’autres personnes, partez d’un bloc-notes numérique.</p>
      <p>Si les deux usages sont équilibrés, comparez les hybrides sur une tâche complète plutôt que sur leur liste de fonctions : ouvrir votre livre ou PDF, écrire, retrouver l’annotation et l’exporter.</p>

      <h2 id="sources">Sources consultées</h2>
      <ul class="source-list">
        <li><a href="https://help.kobo.com/hc/fr/articles/1500001927562-Annoter-votre-livre-avec-le-stylet-Kobo" rel="noopener noreferrer">Kobo : formats et modèles compatibles avec les annotations au stylet</a></li>
        <li><a href="https://help.kobo.com/hc/en-us/articles/360062226733-Use-your-Kobo-eReader-as-a-notebook" rel="noopener noreferrer">Kobo : utilisation des carnets intégrés</a></li>
        <li><a href="https://www.amazon.com/gp/help/customer/display.html?nodeId=T4sq0EZZFwu9vvH3Fx" rel="noopener noreferrer">Amazon : fonctions de lecture et de carnets du Kindle Scribe</a></li>
      </ul>
    """,
    "/guides/tablette-classique-ou-tablette-e-ink/": """
      <p class="article-answer"><strong>Une tablette E Ink convient mieux à la lecture et à l’écriture concentrées ; une tablette classique convient mieux aux applications, à la couleur, à la vidéo et aux interactions rapides.</strong> Commencez par les tâches indispensables : elles révèlent rapidement les compromis impossibles à accepter.</p>

      <h2 id="ecrans">Deux technologies, deux rythmes d’utilisation</h2>
      <p>Une tablette classique utilise un écran LCD ou OLED conçu pour afficher des animations, de la vidéo et des couleurs riches avec un rafraîchissement rapide. Un écran E Ink privilégie l’affichage de pages statiques ; ses changements d’écran sont plus lents et peuvent laisser des traces résiduelles jusqu’au rafraîchissement suivant.</p>
      <p>Cette différence explique l’essentiel des usages. L’E Ink est cohérente pour lire, écrire et consulter des documents relativement statiques. Une tablette classique est plus adaptée dès que l’activité exige défilement rapide, vidéo, visioconférence, retouche d’image ou applications non optimisées.</p>

      <h2 id="comparaison">Comparaison par usage</h2>
      <div class="table-wrapper">
        <table class="comp-table">
          <thead><tr><th>Usage</th><th>Tablette E Ink</th><th>Tablette classique</th></tr></thead>
          <tbody>
            <tr><td>Écriture manuscrite</td><td>Interface souvent centrée sur le stylet</td><td>Très bonnes applications, sensation d’écran différente</td></tr>
            <tr><td>Lecture longue</td><td>Page mate et usage spécialisé</td><td>Écran lumineux, très polyvalent</td></tr>
            <tr><td>Couleur</td><td>Disponible mais plus atténuée</td><td>Couleurs plus riches et fidèles</td></tr>
            <tr><td>Vidéo et animation</td><td>Peu adaptée</td><td>Usage normal</td></tr>
            <tr><td>Applications</td><td>Choix limité ou expérience variable</td><td>Écosystèmes applicatifs complets</td></tr>
            <tr><td>Autonomie</td><td>Souvent annoncée en semaines selon l’usage</td><td>Généralement pensée pour une recharge plus fréquente</td></tr>
          </tbody>
        </table>
      </div>

      <h2 id="eink">Quand une tablette E Ink est le meilleur outil</h2>
      <p>Choisissez l’E Ink lorsque votre journée numérique doit surtout remplacer des cahiers et des documents papier. Elle est particulièrement cohérente pour les réunions, les cours, les brouillons, la lecture attentive et l’annotation de PDF. Son intérêt vient aussi de ses limites : moins de notifications et d’usages multimédias peuvent favoriser un environnement de travail plus calme.</p>
      <p>Il faut cependant vérifier le logiciel. Certaines tablettes E Ink sont très spécialisées ; d’autres utilisent Android et donnent accès à Google Play. Même sur Android, une application conçue pour un écran classique peut présenter des animations, contrastes ou gestes peu adaptés à l’encre électronique.</p>

      <h2 id="classique">Quand une tablette classique reste préférable</h2>
      <p>Gardez une tablette LCD ou OLED si vous alternez fréquemment écriture, web, vidéo, présentations, messagerie et création visuelle. C’est également le choix le plus prudent lorsque votre travail dépend d’une application précise, d’une restitution fidèle des couleurs ou d’une navigation très fluide.</p>
      <p>Une tablette classique n’empêche pas la prise de notes au stylet. Elle offre souvent des outils plus riches, mais aussi davantage de sollicitations. Le choix oppose donc une machine polyvalente à un outil volontairement spécialisé, pas une « bonne » à une « mauvaise » technologie.</p>

      <h2 id="compromis">Les compromis à accepter avec l’E Ink</h2>
      <ul>
        <li>un rafraîchissement plus lent et parfois des traces résiduelles avant nettoyage de l’écran ;</li>
        <li>des couleurs moins saturées sur les modèles couleur ;</li>
        <li>une compatibilité applicative ou documentaire à vérifier modèle par modèle ;</li>
        <li>un rapport équipement-prix difficile à comparer directement à celui d’une tablette classique.</li>
      </ul>

      <h2 id="test-decision">Un test de décision en trois questions</h2>
      <ol>
        <li>La vidéo, la visioconférence ou une application métier sont-elles indispensables ? Si oui, privilégiez une tablette classique.</li>
        <li>La lecture et l’écriture représentent-elles l’essentiel de l’usage ? Si oui, examinez une tablette E Ink.</li>
        <li>Hésitez-vous encore ? Vérifiez l’export et l’application la plus importante. Le premier blocage concret doit décider avant l’autonomie ou le design.</li>
      </ol>
      <p>Pour affiner le choix, consultez notre guide sur <a href="/guides/choisir-bloc-notes-numerique/">les critères d’un bloc-notes numérique</a> et celui consacré à <a href="/guides/tablette-e-ink/">la technologie E Ink</a>.</p>

      <h2 id="sources">Sources consultées</h2>
      <ul class="source-list">
        <li><a href="https://shop.boox.com/products/go103" rel="noopener noreferrer">BOOX : exemple officiel de tablette E Ink Android avec Google Play</a></li>
        <li><a href="https://support.remarkable.com/s/article/About-reMarkable-2" rel="noopener noreferrer">reMarkable : caractéristiques et autonomie annoncée du reMarkable 2</a></li>
        <li><a href="https://help.kobo.com/hc/en-us/articles/360017763713-File-formats-your-Kobo-eReader-and-Kobo-Books-app-support" rel="noopener noreferrer">Kobo : formats pris en charge et limites liées aux DRM</a></li>
      </ul>
    """,
}

from guide_content_extra import GUIDE_CONTENT_EXTRA
GUIDE_CONTENT.update(GUIDE_CONTENT_EXTRA)


from guide_content_quality_choice import GUIDE_CONTENT_QUALITY_CHOICE
from guide_content_quality_tech import GUIDE_CONTENT_QUALITY_TECH
from guide_content_quality_cloud import GUIDE_CONTENT_QUALITY_CLOUD
from guide_content_quality_workflows import GUIDE_CONTENT_QUALITY_WORKFLOWS
GUIDE_CONTENT.update(GUIDE_CONTENT_QUALITY_CHOICE)
GUIDE_CONTENT.update(GUIDE_CONTENT_QUALITY_TECH)
GUIDE_CONTENT.update(GUIDE_CONTENT_QUALITY_CLOUD)
GUIDE_CONTENT.update(GUIDE_CONTENT_QUALITY_WORKFLOWS)

from guide_content_bespoke import GUIDE_CONTENT_BESPOKE
GUIDE_CONTENT.update(GUIDE_CONTENT_BESPOKE)

for path, title, desc in GUIDES:
    crumbs = breadcrumb(("Guides", "/guides/"), title)
    write(path + "index.html", content_page(title, desc, path, crumbs, "Guide", GUIDE_CONTENT.get(path, "")))

# ── BONS PLANS ────────────────────────────────────────────────────────────────
write("/bons-plans/index.html", hub_page(
    "Bons plans — Offres et prix des bloc-notes numériques",
    "Promotions, baisses de prix et repères d’achat vérifiés sur les tablettes E Ink et bloc-notes numériques.",
    "/bons-plans/",
    breadcrumb("Bons plans"),
    "Des offres vérifiées, des prix de référence datés et les promotions expirées clairement séparées des bons plans encore achetables.",
    [
        ("Tous les bons plans", "/bons-plans/bloc-notes-numerique/"),
        ("Offres reMarkable", "/bons-plans/remarkable/"),
        ("Offres Kindle Scribe", "/bons-plans/kindle-scribe/"),
        ("Offres Kobo Elipsa", "/bons-plans/kobo-elipsa/"),
        ("Offres Boox", "/bons-plans/boox/"),
        ("Occasion", "/bons-plans/bloc-notes-numerique-occasion/"),
        ("Black Friday", "/bons-plans/black-friday/"),
    ]
))

BONS_PLANS = [
    ("/bons-plans/bloc-notes-numerique/", "Bons plans bloc-notes numériques — Offres et prix vérifiés", "Promotions réellement vérifiées, prix à surveiller et offres expirées sur les tablettes E Ink."),
    ("/bons-plans/remarkable/", "Bons plans reMarkable — Offres et prix à surveiller", "Bundles, reconditionné et baisses de prix reMarkable vérifiés avec leur prix de référence."),
    ("/bons-plans/kindle-scribe/", "Bons plans Kindle Scribe — Offres et baisses de prix", "Promotions Kindle Scribe actives, prix à surveiller et historiques de baisse clairement séparés."),
    ("/bons-plans/kobo-elipsa/", "Bons plans Kobo Elipsa — Offres et prix", "Prix de référence et promotions vérifiées sur la Kobo Elipsa 2E."),
    ("/bons-plans/boox/", "Bons plans BOOX — Promotions et disponibilité", "Promotions BOOX vérifiées avec contrôle du stock, du bundle et du coût final."),
    ("/bons-plans/bloc-notes-numerique-occasion/", "Bloc-notes numérique d'occasion — Guide d'achat", "Acheter un bloc-notes numérique d'occasion ou reconditionné : prix, état, garantie et contrôles utiles."),
    ("/bons-plans/black-friday/", "Black Friday 2026 — Bloc-notes numériques", "Date, prix de référence et watchlist pour les offres Black Friday 2026 sur les tablettes E Ink."),
]

for path, title, desc in BONS_PLANS:
    crumbs = breadcrumb(("Bons plans", "/bons-plans/"), title.split("—")[0].strip())
    write(path + "index.html", content_page(title, desc, path, crumbs, "Offres", DEAL_CONTENT.get(path, ""), DEAL_STATUS_LABEL.get(path)))

# ── ACCESSOIRES ───────────────────────────────────────────────────────────────
write("/accessoires/index.html", hub_page(
    "Accessoires pour bloc-notes numériques",
    "Stylets, housses, étuis, protections d'écran et accessoires pour tablettes E Ink.",
    "/accessoires/",
    breadcrumb("Accessoires"),
    "Les meilleurs accessoires pour votre bloc-notes numérique : stylets, housses, protections et plus.",
    [
        ("Stylets", "/accessoires/stylets/"),
        ("Housses et étuis", "/accessoires/housses-etuis/"),
        ("Pointes de stylet", "/accessoires/pointes-stylet/"),
        ("Claviers", "/accessoires/claviers/"),
        ("Protections d'écran", "/accessoires/protections-ecran/"),
        ("Accessoires reMarkable", "/accessoires/remarkable/"),
        ("Accessoires Kindle Scribe", "/accessoires/kindle-scribe/"),
        ("Accessoires Boox", "/accessoires/boox/"),
    ]
))

ACCESSOIRES = [
    ("/accessoires/stylets/", "Meilleurs stylets pour tablettes E Ink", "Notre sélection des meilleurs stylets pour bloc-notes numériques."),
    ("/accessoires/housses-etuis/", "Meilleures housses et étuis pour tablettes E Ink", "Protégez votre investissement avec nos housses recommandées."),
    ("/accessoires/pointes-stylet/", "Pointes de stylet — Guide et sélection", "Quelles pointes de stylet choisir pour votre tablette E Ink ?"),
    ("/accessoires/claviers/", "Claviers compatibles avec les tablettes E Ink", "Ajoutez un clavier Bluetooth à votre bloc-notes numérique."),
    ("/accessoires/protections-ecran/", "Meilleures protections d'écran pour tablettes E Ink", "Protégez l'écran de votre tablette E Ink avec les bonnes protections."),
    ("/accessoires/remarkable/", "Accessoires reMarkable — Stylets, housses et plus", "Tous les accessoires officiels et compatibles pour reMarkable."),
    ("/accessoires/kindle-scribe/", "Accessoires Kindle Scribe — Sélection", "Stylets, housses et accessoires pour le Kindle Scribe."),
    ("/accessoires/boox/", "Accessoires Boox — Stylets et housses", "Les meilleurs accessoires pour vos tablettes Boox."),
]

for path, title, desc in ACCESSOIRES:
    crumbs = breadcrumb(("Accessoires", "/accessoires/"), title.split("—")[0].strip())
    write(path + "index.html", content_page(title, desc, path, crumbs))

# ── FOOTER PAGES ──────────────────────────────────────────────────────────────
FOOTER_PAGES = [
    ("/methode-de-test/", "Notre méthode de test — bloc-notes numériques.fr", "Comment testons-nous les bloc-notes numériques ? Notre protocole complet."),
    ("/comment-nous-comparons/", "Comment nous comparons les produits", "Notre méthodologie de comparaison des tablettes E Ink et bloc-notes numériques."),
    ("/a-propos/", "À propos — bloc-notes numériques.fr", "Qui sommes-nous ? Notre équipe et notre engagement pour des tests indépendants."),
    ("/contact/", "Contact — bloc-notes numériques.fr", "Contactez l'équipe de bloc-notes numériques.fr."),
    ("/transparence-affiliation/", "Transparence sur l'affiliation — bloc-notes numériques.fr", "Comment fonctionne notre modèle d'affiliation et comment préservons-nous notre indépendance."),
    ("/mentions-legales/", "Mentions légales — bloc-notes numériques.fr", "Mentions légales, politique de confidentialité et conditions d'utilisation."),
]

for path, title, desc in FOOTER_PAGES:
    slug = path.strip("/").replace("-", " ").title()
    crumbs = breadcrumb(slug)
    write(path + "index.html", content_page(title, desc, path, crumbs))

print("\n✅ Toutes les pages ont été générées.")
