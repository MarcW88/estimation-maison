#!/usr/bin/env python3
"""Generate all HTML pages for aspirateurs-chantier site."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

# ── LOGO SVG ──────────────────────────────────────────────────────────────────
LOGO_ICON = """<svg class="logo-icon" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="18" width="12" height="10" rx="3" fill="#1B4FD8" opacity="0.15" stroke="#1B4FD8" stroke-width="1.5"/>
  <circle cx="8" cy="28" r="2" fill="#1B4FD8"/>
  <circle cx="14" cy="28" r="2" fill="#1B4FD8"/>
  <path d="M14 22 Q20 16 26 10" stroke="#1B4FD8" stroke-width="2" stroke-linecap="round"/>
  <circle cx="27" cy="9" r="3" fill="#E05E1A"/>
</svg>"""

# ── NAV ───────────────────────────────────────────────────────────────────────
NAV_HTML = """<nav class="site-nav">
  <div class="nav-item">
    <a href="/comparatifs/" class="nav-link">Comparatifs<svg class="chev" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg></a>
    <div class="dropdown">
      <a href="/comparatifs/meilleur-aspirateur-de-chantier/">Meilleur aspirateur de chantier</a>
      <a href="/comparatifs/aspirateur-eau-poussiere/">Eau et poussière</a>
      <a href="/comparatifs/aspirateur-chantier-sans-fil/">Sans fil</a>
      <a href="/comparatifs/aspirateur-chantier-sans-sac/">Sans sac</a>
      <a href="/comparatifs/aspirateur-chantier-puissant/">Les plus puissants</a>
      <div class="dd-sep"></div>
      <a href="/comparatifs/aspirateur-professionnel/">Professionnel</a>
      <a href="/comparatifs/aspirateur-industriel/">Industriel</a>
      <a href="/comparatifs/aspirateur-classe-m/">Classe M</a>
      <a href="/comparatifs/petit-aspirateur-de-chantier/">Petit format</a>
    </div>
  </div>
  <div class="nav-item">
    <a href="/usages/" class="nav-link">Par usage<svg class="chev" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg></a>
    <div class="dropdown">
      <a href="/usages/aspirateur-platre/">Plâtre</a>
      <a href="/usages/aspirateur-ponceuse/">Ponceuse</a>
      <a href="/usages/aspirateur-atelier/">Atelier</a>
      <a href="/usages/aspirateur-bois-sciure-copeaux/">Bois &amp; sciure</a>
      <a href="/usages/aspirateur-gravats/">Gravats</a>
      <a href="/usages/aspirateur-scie/">Scie</a>
      <a href="/usages/aspirateur-bricolage-renovation/">Bricolage &amp; rénovation</a>
    </div>
  </div>
  <div class="nav-item">
    <a href="/marques/" class="nav-link">Marques<svg class="chev" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg></a>
    <div class="dropdown">
      <a href="/marques/karcher/">Kärcher</a>
      <a href="/marques/bosch/">Bosch</a>
      <a href="/marques/makita/">Makita</a>
      <a href="/marques/festool/">Festool</a>
      <a href="/marques/dewalt/">DeWalt</a>
      <a href="/marques/parkside/">Parkside</a>
      <a href="/marques/nilfisk/">Nilfisk</a>
      <a href="/marques/mirka/">Mirka</a>
    </div>
  </div>
  <div class="nav-item">
    <a href="/modeles/" class="nav-link">Modèles<svg class="chev" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg></a>
    <div class="dropdown">
      <span class="dd-label">Kärcher</span>
      <a href="/modeles/karcher-wd2/">Kärcher WD2</a>
      <a href="/modeles/karcher-wd5/">Kärcher WD5</a>
      <a href="/modeles/karcher-wd6/">Kärcher WD6</a>
      <a href="/modeles/karcher-nt-30-1-tact/">Kärcher NT 30/1 Tact</a>
      <div class="dd-sep"></div>
      <span class="dd-label">Bosch</span>
      <a href="/modeles/bosch-advancedvac-20/">AdvancedVac 20</a>
      <a href="/modeles/bosch-gas-35-m-afc/">GAS 35 M AFC</a>
      <a href="/modeles/bosch-gas-35-l-afc/">GAS 35 L AFC</a>
    </div>
  </div>
  <div class="nav-item">
    <a href="/guides/" class="nav-link">Guides<svg class="chev" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg></a>
    <div class="dropdown">
      <a href="/guides/comment-choisir-aspirateur-de-chantier/">Comment choisir ?</a>
      <a href="/guides/classes-l-m-h/">Classes L, M et H</a>
      <a href="/guides/decolmatage-automatique/">Décolmatage automatique</a>
      <a href="/guides/prise-asservie/">Prise asservie</a>
      <div class="dd-sep"></div>
      <a href="/guides/depression-kpa-mbar-air-watt/">kPa, mbar, Air Watts</a>
      <a href="/guides/debit-air-aspirateur/">Débit d'air</a>
      <a href="/guides/puissance-aspiration/">Puissance moteur</a>
      <a href="/guides/filtre-hepa-aspirateur/">Filtre HEPA</a>
    </div>
  </div>
</nav>"""

HEADER_HTML = f"""<header class="site-header">
  <div class="header-inner">
    <a href="/" class="site-logo">
      {LOGO_ICON}
      <div class="logo-text">
        <span class="logo-line1">Aspirateurs</span>
        <span class="logo-line2">Chantier</span>
      </div>
    </a>
    {NAV_HTML}
    <a href="/guides/comment-choisir-aspirateur-de-chantier/" class="header-cta">Choisir mon aspirateur</a>
    <button class="burger" aria-label="Menu"><span></span><span></span><span></span></button>
  </div>
</header>"""

FOOTER_HTML = """<footer class="site-footer">
  <div class="container">
    <div class="footer-main">
      <div class="footer-brand">
        <div class="site-logo" style="display:flex;align-items:center;gap:10px;">
          <div class="logo-text">
            <span class="logo-line1">Aspirateurs</span>
            <span class="logo-line2">Chantier</span>
          </div>
        </div>
        <p class="footer-tagline">Base de données spécialisée sur les aspirateurs de chantier. Comparatifs indépendants, fiches techniques et guides d'achat.</p>
      </div>
      <div class="footer-col">
        <h4>Comparatifs</h4>
        <a href="/comparatifs/meilleur-aspirateur-de-chantier/">Meilleur aspirateur</a>
        <a href="/comparatifs/aspirateur-eau-poussiere/">Eau et poussière</a>
        <a href="/comparatifs/aspirateur-chantier-sans-fil/">Sans fil</a>
        <a href="/comparatifs/aspirateur-classe-m/">Classe M</a>
        <a href="/comparatifs/aspirateur-professionnel/">Professionnel</a>
      </div>
      <div class="footer-col">
        <h4>Marques</h4>
        <a href="/marques/karcher/">Kärcher</a>
        <a href="/marques/bosch/">Bosch</a>
        <a href="/marques/makita/">Makita</a>
        <a href="/marques/festool/">Festool</a>
        <a href="/marques/nilfisk/">Nilfisk</a>
      </div>
      <div class="footer-col">
        <h4>Le site</h4>
        <a href="/methode-de-test/">Méthode de test</a>
        <a href="/a-propos/">À propos</a>
        <a href="/contact/">Contact</a>
        <a href="/transparence-affiliation/">Affiliation</a>
        <a href="/mentions-legales/">Mentions légales</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© aspirateurs-chantier.fr — Base de données indépendante</span>
      <span>Liens affiliés présents. <a href="/transparence-affiliation/">Transparence.</a></span>
    </div>
  </div>
</footer>"""


def css_path_for(canonical):
    # The site is served from its own domain, so an absolute root path works
    # consistently for the homepage and for pages at every directory depth.
    return "/style.css"


def html_doc(title, desc, canonical, body_html):
    cp = css_path_for(canonical)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://aspirateurs-chantier.fr{canonical}">
  <link rel="stylesheet" href="{cp}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
</head>
<body>
{HEADER_HTML}
<main>
{body_html}
</main>
{FOOTER_HTML}
</body>
</html>"""


def breadcrumb(*items):
    parts = ['<a href="/">Accueil</a><span class="sep">/</span>']
    for i, item in enumerate(items):
        if isinstance(item, tuple):
            parts.append(f'<a href="{item[1]}">{item[0]}</a>')
        else:
            parts.append(f'<span>{item}</span>')
        if i < len(items) - 1:
            parts.append('<span class="sep">/</span>')
    return f'<div class="container"><nav class="breadcrumb">{" ".join(parts)}</nav></div>'


def hub_page(title, desc, canonical, bc, intro, links):
    link_items = ""
    for label, url, meta in links:
        link_items += f"""<a href="{url}" class="hub-link">
  <div><div>{label}</div><div class="hub-link-meta">{meta}</div></div>
  <span class="hub-link-right">→</span>
</a>\n"""
    body = f"""{bc}
<section class="page-hero">
  <div class="container">
    <h1>{title}</h1>
    <p class="lead">{intro}</p>
    <div class="page-meta">
      <span class="meta-tag">Mis à jour régulièrement</span>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="hub-grid">{link_items}</div>
  </div>
</section>"""
    return html_doc(title, desc, canonical, body)


def content_page(title, desc, canonical, bc, ctype="guide", answer="", related=None):
    related_html = ""
    if related:
        links = "\n".join(f'<a href="{u}">{l}</a>' for l, u in related)
        related_html = f"""<div class="related-box">
  <h4>À lire aussi</h4>
  <div class="related-links">{links}</div>
</div>"""
    answer_html = f'<div class="answer-box"><p>{answer}</p></div>' if answer else ""
    body = f"""{bc}
<section class="page-hero">
  <div class="container">
    <span class="ctype ctype-{ctype}">{ctype.title()}</span>
    <h1 style="margin-top:10px;">{title}</h1>
    <p class="lead">{desc}</p>
    <div class="page-meta">
      <span class="meta-tag">Vérifié : MM/AAAA</span>
    </div>
  </div>
</section>
<div class="container">
  <div class="content-layout">
    <article class="content-main">
      {answer_html}
      <!-- Contenu à rédiger -->
      {related_html}
    </article>
    <aside class="content-sidebar">
      <div class="sidebar-box">
        <div class="sidebar-box-head">Sommaire</div>
        <div class="sidebar-box-body">
          <nav class="toc-list">
            <!-- TOC générée -->
          </nav>
        </div>
      </div>
      <div class="sidebar-box">
        <div class="sidebar-box-head">Affiliation</div>
        <div class="sidebar-box-body">
          <p class="affil-note">Ce site contient des liens affiliés. Nos recommandations restent indépendantes. <a href="/transparence-affiliation/">En savoir plus.</a></p>
        </div>
      </div>
      <a href="/guides/comment-choisir-aspirateur-de-chantier/" class="btn btn-primary" style="width:100%;justify-content:center;text-align:center;">Choisir mon aspirateur</a>
    </aside>
  </div>
</div>"""
    return html_doc(title, desc, canonical, body)


def model_page(title, desc, canonical, bc, model_name, brand, dust_class,
               specs: dict, pros: list, cons: list, related=None):
    class_badge = {"L": "badge-l", "M": "badge-m", "H": "badge-h"}.get(dust_class, "badge-gray")
    spec_rows = ""
    for k, v in specs.items():
        spec_rows += f'<tr><td class="sk">{k}</td><td class="sv">{v}</td></tr>\n'
    pro_items = "\n".join(f"<li>{p}</li>" for p in pros)
    con_items = "\n".join(f"<li>{c}</li>" for c in cons)
    related_html = ""
    if related:
        links = "\n".join(f'<a href="{u}">{l}</a>' for l, u in related)
        related_html = f'<div class="related-box"><h4>À lire aussi</h4><div class="related-links">{links}</div></div>'
    body = f"""{bc}
<section class="model-hero">
  <div class="container">
    <div class="model-hero-inner">
      <div>
        <div class="model-badges">
          <span class="badge {class_badge}">Classe {dust_class}</span>
          <span class="badge badge-blue">{brand}</span>
          <span class="ctype ctype-modele">Fiche modèle</span>
        </div>
        <h1 class="model-title">{model_name}</h1>
        <p class="model-tagline lead">{desc}</p>
        <div class="model-actions">
          <a href="#specs" class="btn btn-outline btn-sm">Voir les specs</a>
          <a href="#verdict" class="btn btn-primary btn-sm">Verdict</a>
          <a href="#prix" class="btn btn-accent btn-sm">Voir le prix</a>
        </div>
      </div>
      <div class="spec-sheet">
        <div class="spec-sheet-header">
          <span>Fiche technique</span>
          <span class="verified">Données vérifiées MM/AAAA</span>
        </div>
        <table class="spec-table">
          {spec_rows}
        </table>
      </div>
    </div>
  </div>
</section>
<div class="container">
  <div class="content-layout">
    <article class="content-main">
      <div class="pro-con-grid">
        <div class="pro-box"><h4>Idéal pour</h4><ul>{pro_items}</ul></div>
        <div class="con-box"><h4>Moins adapté si</h4><ul>{con_items}</ul></div>
      </div>
      <!-- Contenu test à rédiger -->
      {related_html}
    </article>
    <aside class="content-sidebar">
      <div class="sidebar-box">
        <div class="sidebar-box-head">Classe filtration</div>
        <div class="sidebar-box-body">
          <span class="badge {class_badge}" style="font-size:0.82rem;padding:6px 14px;">Classe {dust_class}</span>
        </div>
      </div>
      <div class="sidebar-box">
        <div class="sidebar-box-head">Sommaire</div>
        <div class="sidebar-box-body"><nav class="toc-list"></nav></div>
      </div>
      <div class="sidebar-box">
        <div class="sidebar-box-head">Affiliation</div>
        <div class="sidebar-box-body">
          <p class="affil-note">Ce site contient des liens affiliés. <a href="/transparence-affiliation/">En savoir plus.</a></p>
        </div>
      </div>
    </aside>
  </div>
</div>"""
    return html_doc(title, desc, canonical, body)


def write(path, content):
    full = os.path.join(BASE, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ {path}")


# ═══════════════════════════════════════════════════════════════════════════════
# HOMEPAGE
# ═══════════════════════════════════════════════════════════════════════════════
homepage_body = """
<section class="hero">
  <div class="container">
    <div class="hero-inner">
      <div>
        <div class="hero-eyebrow">
          <svg width="12" height="12" viewBox="0 0 12 12" fill="none"><circle cx="6" cy="6" r="5" stroke="currentColor" stroke-width="1.5"/><circle cx="6" cy="6" r="2" fill="currentColor"/></svg>
          Base de données spécialisée — Tests &amp; comparatifs indépendants
        </div>
        <h1 class="hero-title">Aspirateurs de chantier :<br>comparatifs, tests et guide de choix.</h1>
        <p class="hero-desc lead">Tests approfondis, fiches techniques normalisées et comparatifs indépendants. Pour choisir le bon aspirateur selon le chantier, pas selon la commission.</p>
        <div class="hero-actions">
          <a href="/comparatifs/meilleur-aspirateur-de-chantier/" class="btn btn-primary btn-lg">Voir le comparatif général</a>
          <a href="/guides/comment-choisir-aspirateur-de-chantier/" class="btn btn-outline btn-lg">Guide de choix</a>
        </div>
      </div>
      <div class="hero-stats">
        <div class="hero-stat-header"><span>Critères de comparaison</span></div>
        <div class="hero-stat-row">
          <span class="stat-label">Dépression (kPa)</span>
          <div class="stat-bar-wrap"><div class="stat-bar-track"><div class="stat-bar-fill" style="width:85%"></div></div></div>
          <span class="stat-value">≤ 33 kPa</span>
        </div>
        <div class="hero-stat-row">
          <span class="stat-label">Débit max (L/s)</span>
          <div class="stat-bar-wrap"><div class="stat-bar-track"><div class="stat-bar-fill" style="width:70%"></div></div></div>
          <span class="stat-value">≤ 56 L/s</span>
        </div>
        <div class="hero-stat-row">
          <span class="stat-label">Classe filtration</span>
          <div class="stat-bar-wrap"></div>
          <span class="stat-value"><span class="badge badge-l">L</span> <span class="badge badge-m">M</span> <span class="badge badge-h">H</span></span>
        </div>
        <div class="hero-stat-row">
          <span class="stat-label">Capacité cuve (L)</span>
          <div class="stat-bar-wrap"><div class="stat-bar-track"><div class="stat-bar-fill" style="width:60%"></div></div></div>
          <span class="stat-value">6 – 45 L</span>
        </div>
        <div class="hero-stat-row">
          <span class="stat-label">Décolmatage auto</span>
          <div class="stat-bar-wrap"></div>
          <span class="stat-value">Oui / Non</span>
        </div>
        <div class="hero-stat-row">
          <span class="stat-label">Prise asservie</span>
          <div class="stat-bar-wrap"></div>
          <span class="stat-value">Oui / Non</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Par usage</p>
      <h2>Quel est votre chantier ?</h2>
      <p>Chaque application a ses exigences de filtration, débit et décolmatage. Trouvez le bon modèle directement.</p>
    </div>
    <div class="usage-grid">
      <a href="/usages/aspirateur-platre/" class="usage-card">
        <div class="usage-card-icon"><svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M8 12h8M12 8v8"/></svg></div>
        <h3>Plâtre</h3>
        <p>Filtration fine indispensable. Décolmatage automatique recommandé.</p>
      </a>
      <a href="/usages/aspirateur-ponceuse/" class="usage-card">
        <div class="usage-card-icon"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 3v18M3 12h18"/></svg></div>
        <h3>Ponceuse</h3>
        <p>Prise asservie, débit maintenu, compatibilité Festool / Mirka.</p>
      </a>
      <a href="/usages/aspirateur-atelier/" class="usage-card">
        <div class="usage-card-icon"><svg viewBox="0 0 24 24"><path d="M2 20h20M4 20V10l8-7 8 7v10"/></svg></div>
        <h3>Atelier</h3>
        <p>Usage polyvalent, longue durée, grande cuve.</p>
      </a>
      <a href="/usages/aspirateur-bois-sciure-copeaux/" class="usage-card">
        <div class="usage-card-icon"><svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5M2 12l10 5 10-5"/></svg></div>
        <h3>Bois &amp; sciure</h3>
        <p>Gros volumes, copeaux, aspiration machine à bois.</p>
      </a>
      <a href="/usages/aspirateur-gravats/" class="usage-card">
        <div class="usage-card-icon"><svg viewBox="0 0 24 24"><polygon points="12 2 22 20 2 20"/></svg></div>
        <h3>Gravats</h3>
        <p>Débris lourds, cuve robuste, eau &amp; poussière.</p>
      </a>
      <a href="/usages/aspirateur-scie/" class="usage-card">
        <div class="usage-card-icon"><svg viewBox="0 0 24 24"><line x1="4" y1="12" x2="20" y2="12"/><polyline points="14 6 20 12 14 18"/></svg></div>
        <h3>Scie</h3>
        <p>Scie circulaire, onglet, table — connexion directe outil.</p>
      </a>
      <a href="/usages/aspirateur-bricolage-renovation/" class="usage-card">
        <div class="usage-card-icon"><svg viewBox="0 0 24 24"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg></div>
        <h3>Bricolage &amp; rénovation</h3>
        <p>Polyvalence, rapport qualité-prix, facilité d'entretien.</p>
      </a>
    </div>
  </div>
</section>

<section class="section section--white">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Comparatif général</p>
      <h2>Les meilleurs aspirateurs de chantier</h2>
      <p>Notre sélection principale, mise à jour régulièrement. <a href="/comparatifs/meilleur-aspirateur-de-chantier/" style="color:var(--color-primary);font-weight:600;">Voir le comparatif complet →</a></p>
    </div>
    <div class="data-table-wrap">
      <table class="data-table">
        <thead>
          <tr>
            <th>Modèle</th>
            <th>Classe</th>
            <th>Dépression</th>
            <th>Débit</th>
            <th>Cuve</th>
            <th>Décolm. auto</th>
            <th>Pr. asservie</th>
            <th>Prix</th>
            <th>Verdict</th>
          </tr>
        </thead>
        <tbody>
          <tr class="row-highlight">
            <td class="col-model"><a href="/modeles/bosch-gas-35-m-afc/" style="color:var(--color-primary)">Bosch GAS 35 M AFC</a></td>
            <td><span class="badge badge-m">M</span></td>
            <td class="col-num"><strong>27</strong> kPa</td>
            <td class="col-num"><strong>56</strong> L/s</td>
            <td class="col-num">35 L</td>
            <td><span class="badge badge-blue">Oui</span></td>
            <td><span class="badge badge-blue">Oui</span></td>
            <td class="col-num">— €</td>
            <td><span class="verdict-pill">Meilleur choix</span></td>
          </tr>
          <tr>
            <td class="col-model"><a href="/modeles/karcher-wd6/" style="color:var(--color-primary)">Kärcher WD6</a></td>
            <td><span class="badge badge-l">L</span></td>
            <td class="col-num"><strong>30</strong> kPa</td>
            <td class="col-num"><strong>—</strong> L/s</td>
            <td class="col-num">30 L</td>
            <td><span class="badge badge-gray">Non</span></td>
            <td><span class="badge badge-gray">Non</span></td>
            <td class="col-num">— €</td>
            <td>Meilleur rapport Q/P</td>
          </tr>
          <tr>
            <td class="col-model"><a href="/modeles/festool-ctl-midi/" style="color:var(--color-primary)">Festool CTL Midi</a></td>
            <td><span class="badge badge-m">M</span></td>
            <td class="col-num"><strong>—</strong> kPa</td>
            <td class="col-num"><strong>—</strong> L/s</td>
            <td class="col-num">17 L</td>
            <td><span class="badge badge-blue">Oui</span></td>
            <td><span class="badge badge-blue">Oui</span></td>
            <td class="col-num">— €</td>
            <td>Meilleur ponceuse</td>
          </tr>
          <tr>
            <td class="col-model"><a href="/modeles/bosch-gas-18v-10-l/" style="color:var(--color-primary)">Bosch GAS 18V-10 L</a></td>
            <td><span class="badge badge-l">L</span></td>
            <td class="col-num"><strong>—</strong> kPa</td>
            <td class="col-num"><strong>—</strong> L/s</td>
            <td class="col-num">10 L</td>
            <td><span class="badge badge-gray">Non</span></td>
            <td><span class="badge badge-blue">Oui</span></td>
            <td class="col-num">— €</td>
            <td>Meilleur sans fil</td>
          </tr>
          <tr>
            <td class="col-model"><a href="/modeles/makita-vc2512l/" style="color:var(--color-primary)">Makita VC2512L</a></td>
            <td><span class="badge badge-l">L</span></td>
            <td class="col-num"><strong>—</strong> kPa</td>
            <td class="col-num"><strong>—</strong> L/s</td>
            <td class="col-num">25 L</td>
            <td><span class="badge badge-gray">Non</span></td>
            <td><span class="badge badge-blue">Oui</span></td>
            <td class="col-num">— €</td>
            <td>Bon rapport Q/P</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Marques</p>
      <h2>Les fabricants du marché</h2>
    </div>
    <div class="brand-grid">
      <a href="/marques/karcher/" class="brand-card">
        <div class="brand-name">Kärcher</div>
        <div class="brand-tier">Gamme WD &amp; NT</div>
        <div class="brand-desc">Leader grand public. Série WD (eau+poussière) et NT (professionnelle). Excellent rapport qualité-prix.</div>
      </a>
      <a href="/marques/bosch/" class="brand-card">
        <div class="brand-name">Bosch</div>
        <div class="brand-tier">Gamme GAS &amp; AdvancedVac</div>
        <div class="brand-desc">Référence professionnelle. GAS 35 M AFC parmi les meilleures performances classe M du marché.</div>
      </a>
      <a href="/marques/makita/" class="brand-card">
        <div class="brand-name">Makita</div>
        <div class="brand-tier">Gamme VC</div>
        <div class="brand-desc">Excellente fiabilité, compatibilité batterie 18V et 40V avec l'écosystème outil Makita.</div>
      </a>
      <a href="/marques/festool/" class="brand-card">
        <div class="brand-name">Festool</div>
        <div class="brand-tier">Gamme CTL &amp; CT</div>
        <div class="brand-desc">La référence ponçage. Intégration parfaite avec les ponceuses Festool. Haut de gamme.</div>
      </a>
      <a href="/marques/dewalt/" class="brand-card">
        <div class="brand-name">DeWalt</div>
        <div class="brand-tier">Gamme DXV</div>
        <div class="brand-desc">Bonne qualité, écosystème batterie 18/54V très répandu dans les corps de métier.</div>
      </a>
      <a href="/marques/nilfisk/" class="brand-card">
        <div class="brand-name">Nilfisk</div>
        <div class="brand-tier">Gamme Multi</div>
        <div class="brand-desc">Fabricant professionnel historique. Bonne présence en classe H.</div>
      </a>
      <a href="/marques/parkside/" class="brand-card">
        <div class="brand-name">Parkside</div>
        <div class="brand-tier">Entrée de gamme</div>
        <div class="brand-desc">Rapport qualité-prix agressif (Lidl). Idéal bricolage occasionnel.</div>
      </a>
      <a href="/marques/mirka/" class="brand-card">
        <div class="brand-name">Mirka</div>
        <div class="brand-tier">Spécialiste ponçage</div>
        <div class="brand-desc">Concurrent direct de Festool sur le ponçage. Aspirateurs optimisés pour leurs ponceuses.</div>
      </a>
    </div>
  </div>
</section>

<section class="section section--white">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Guides techniques</p>
      <h2>Comprendre avant de choisir</h2>
      <p>Les questions que posent les utilisateurs aux moteurs de recherche et aux assistants IA.</p>
    </div>
    <div class="guide-grid">
      <a href="/guides/classes-l-m-h/" class="guide-card">
        <span class="ctype ctype-guide">Guide</span>
        <div class="guide-q">Classe L, M ou H : laquelle me faut-il ?</div>
        <div class="guide-hint">Réglementation, risques, cas d'usage concrets.</div>
        <div class="guide-arrow">Lire le guide →</div>
      </a>
      <a href="/guides/decolmatage-automatique/" class="guide-card">
        <span class="ctype ctype-guide">Guide</span>
        <div class="guide-q">À quoi sert le décolmatage automatique ?</div>
        <div class="guide-hint">Maintien du débit, durée de vie du filtre, utilisation ponceuse.</div>
        <div class="guide-arrow">Lire le guide →</div>
      </a>
      <a href="/guides/depression-kpa-mbar-air-watt/" class="guide-card">
        <span class="ctype ctype-guide">Guide</span>
        <div class="guide-q">kPa, mbar, Air Watts : que comparer vraiment ?</div>
        <div class="guide-hint">Les métriques qui comptent, celles qui sont du marketing.</div>
        <div class="guide-arrow">Lire le guide →</div>
      </a>
      <a href="/guides/prise-asservie/" class="guide-card">
        <span class="ctype ctype-guide">Guide</span>
        <div class="guide-q">Qu'est-ce qu'une prise asservie ?</div>
        <div class="guide-hint">Démarrage automatique avec l'outil, compatibilité, sécurité.</div>
        <div class="guide-arrow">Lire le guide →</div>
      </a>
      <a href="/guides/filtre-hepa-aspirateur/" class="guide-card">
        <span class="ctype ctype-guide">Guide</span>
        <div class="guide-q">Le filtre HEPA H13/H14 est-il utile sur chantier ?</div>
        <div class="guide-hint">Quand c'est nécessaire, quand c'est du sur-dimensionnement.</div>
        <div class="guide-arrow">Lire le guide →</div>
      </a>
      <a href="/guides/sac-ou-sans-sac/" class="guide-card">
        <span class="ctype ctype-guide">Guide</span>
        <div class="guide-q">Sac ou sans sac sur chantier ?</div>
        <div class="guide-hint">Coût récurrent, confort de vidage, filtration réelle.</div>
        <div class="guide-arrow">Lire le guide →</div>
      </a>
    </div>
  </div>
</section>
"""

write("/index.html", html_doc(
    "Aspirateurs de chantier — Comparatifs, tests et guide de choix",
    "Base de données spécialisée sur les aspirateurs de chantier. Comparatifs indépendants, fiches techniques normalisées et guides d'achat.",
    "/",
    homepage_body
))

# ═══════════════════════════════════════════════════════════════════════════════
# COMPARATIFS
# ═══════════════════════════════════════════════════════════════════════════════
write("/comparatifs/index.html", hub_page(
    "Comparatifs d'aspirateurs de chantier",
    "Tous nos comparatifs indépendants d'aspirateurs de chantier, classés par usage, type et budget.",
    "/comparatifs/",
    breadcrumb("Comparatifs"),
    "Comparatifs basés sur des données techniques vérifiées. Chaque tableau présente les métriques réelles : dépression, débit, classe de filtration.",
    [
        ("Meilleur aspirateur de chantier", "/comparatifs/meilleur-aspirateur-de-chantier/", "Hub · page principale"),
        ("Eau et poussière", "/comparatifs/aspirateur-eau-poussiere/", "Wet & dry"),
        ("Sans fil", "/comparatifs/aspirateur-chantier-sans-fil/", "18V / 36V / 54V"),
        ("Sans sac", "/comparatifs/aspirateur-chantier-sans-sac/", "Vidage direct"),
        ("Les plus puissants", "/comparatifs/aspirateur-chantier-puissant/", "Dépression &gt; 25 kPa"),
        ("Professionnel", "/comparatifs/aspirateur-professionnel/", "Usage intensif"),
        ("Industriel", "/comparatifs/aspirateur-industriel/", "Grande capacité"),
        ("Classe M", "/comparatifs/aspirateur-classe-m/", "Poussières dangereuses modérées"),
        ("Petit format", "/comparatifs/petit-aspirateur-de-chantier/", "&lt; 15 litres"),
    ]
))

COMPARATIFS = [
    ("/comparatifs/meilleur-aspirateur-de-chantier/",
     "Meilleur aspirateur de chantier — Comparatif",
     "Quel est le meilleur aspirateur de chantier ? Notre comparatif indépendant avec données techniques vérifiées.",
     "Pour la majorité des utilisateurs, le <strong>Bosch GAS 35 M AFC</strong> offre le meilleur équilibre performance/praticité en classe M. Pour un usage grand public avec budget limité, le <strong>Kärcher WD6</strong> reste la référence en classe L. Pour le ponçage intensif, privilégiez le <strong>Festool CTL Midi</strong>.",
     [("Guide classes L/M/H", "/guides/classes-l-m-h/"), ("Aspirateur plâtre", "/usages/aspirateur-platre/"), ("Aspirateur ponceuse", "/usages/aspirateur-ponceuse/")]),
    ("/comparatifs/aspirateur-eau-poussiere/",
     "Meilleur aspirateur eau et poussière de chantier",
     "Comparatif des meilleurs aspirateurs eau et poussière pour le chantier et l'atelier.",
     "Un aspirateur <strong>eau et poussière</strong> (wet &amp; dry) aspire aussi bien les liquides que les solides. Vérifiez que le modèle dispose d'un filtre adaptable à chaque mode et d'une cuve en acier ou plastique robuste résistant à l'humidité.",
     [("Kärcher WD6", "/modeles/karcher-wd6/"), ("Kärcher WD5", "/modeles/karcher-wd5/"), ("Gravats", "/usages/aspirateur-gravats/")]),
    ("/comparatifs/aspirateur-chantier-sans-fil/",
     "Meilleur aspirateur de chantier sans fil — Comparatif",
     "Comparatif des aspirateurs de chantier sans fil (18V, 36V, 54V) : autonomie, performances, compatibilité.",
     "Les aspirateurs sans fil de chantier atteignent désormais des performances proches du filaire sur des durées courtes. Le <strong>Bosch GAS 18V-10 L</strong> et le <strong>Makita VC001</strong> sont les références actuelles.",
     [("Bosch GAS 18V-10 L", "/modeles/bosch-gas-18v-10-l/"), ("Marque Bosch", "/marques/bosch/"), ("Marque Makita", "/marques/makita/")]),
    ("/comparatifs/aspirateur-chantier-sans-sac/",
     "Meilleur aspirateur de chantier sans sac",
     "Les meilleurs aspirateurs de chantier sans sac : économique, pratique, mais quels compromis filtration ?",
     "Le vidage sans sac simplifie le chantier mais nécessite un filtre de qualité pour éviter les remises en suspension. Évaluez le système de décolmatage avant d'acheter.",
     [("Sac ou sans sac ?", "/guides/sac-ou-sans-sac/"), ("Filtres aspirateur", "/accessoires/filtres-aspirateur-chantier/"), ("Décolmatage", "/guides/decolmatage-automatique/")]),
    ("/comparatifs/aspirateur-chantier-puissant/",
     "Aspirateur de chantier puissant — Les modèles les plus performants",
     "Quels sont les aspirateurs de chantier les plus puissants du marché ? Classement par dépression et débit réel.",
     "La puissance moteur (watts) est un indicateur marketing peu fiable. Les métriques pertinentes sont la <strong>dépression maximale</strong> (kPa ou mbar) et le <strong>débit d'air</strong> (L/s ou m³/h). Un bon aspirateur de chantier professionnel dépasse 25 kPa et 50 L/s.",
     [("kPa, mbar, Air Watts", "/guides/depression-kpa-mbar-air-watt/"), ("Débit d'air", "/guides/debit-air-aspirateur/"), ("Bosch GAS 35 M AFC", "/modeles/bosch-gas-35-m-afc/")]),
    ("/comparatifs/aspirateur-professionnel/",
     "Meilleur aspirateur professionnel de chantier",
     "Comparatif des aspirateurs professionnels pour usage intensif : classe M, décolmatage, durabilité.",
     "",
     [("Classe M", "/comparatifs/aspirateur-classe-m/"), ("Bosch GAS 35 M AFC", "/modeles/bosch-gas-35-m-afc/"), ("Festool CTL Midi", "/modeles/festool-ctl-midi/")]),
    ("/comparatifs/aspirateur-industriel/",
     "Meilleur aspirateur industriel — Comparatif",
     "Les meilleurs aspirateurs industriels pour une utilisation intensive en atelier ou sur gros chantiers.",
     "",
     [("Nilfisk Multi II", "/modeles/nilfisk-multi-ii-30-t/"), ("Kärcher NT 30/1", "/modeles/karcher-nt-30-1-tact/"), ("Capacité cuve", "/guides/capacite-cuve/")]),
    ("/comparatifs/aspirateur-classe-m/",
     "Meilleur aspirateur classe M — Comparatif",
     "Comparatif des meilleurs aspirateurs de chantier classe M pour poussières dangereuses modérées (plâtre, bois, béton).",
     "Un aspirateur <strong>classe M</strong> filtre les poussières dangereuses modérées (efficacité filtre ≥ 99,9 % à 0,1–1 µm). Il est obligatoire pour le ponçage du plâtre, le béton et de nombreuses essences de bois. La classe M n'est pas la même chose que simplement avoir un filtre HEPA.",
     [("Classes L, M et H", "/guides/classes-l-m-h/"), ("Plâtre", "/usages/aspirateur-platre/"), ("Bosch GAS 35 M AFC", "/modeles/bosch-gas-35-m-afc/")]),
    ("/comparatifs/petit-aspirateur-de-chantier/",
     "Meilleur petit aspirateur de chantier",
     "Les meilleurs aspirateurs de chantier compacts (moins de 15 litres) pour petits travaux et déplacements.",
     "",
     [("Bosch AdvancedVac 20", "/modeles/bosch-advancedvac-20/"), ("Bosch GAS 18V-10 L", "/modeles/bosch-gas-18v-10-l/"), ("Sans fil", "/comparatifs/aspirateur-chantier-sans-fil/")]),
]

for path, title, desc, answer, related in COMPARATIFS:
    bc = breadcrumb(("Comparatifs", "/comparatifs/"), title.split("—")[0].strip())
    write(path + "index.html", content_page(title, desc, path, bc, "comp", answer, related))

# ═══════════════════════════════════════════════════════════════════════════════
# USAGES
# ═══════════════════════════════════════════════════════════════════════════════
write("/usages/index.html", hub_page(
    "Aspirateur de chantier par usage",
    "Quel aspirateur de chantier choisir selon votre application ? Plâtre, ponceuse, atelier, bois, gravats, scie.",
    "/usages/",
    breadcrumb("Par usage"),
    "Chaque usage impose ses contraintes de filtration, débit et décolmatage. Nos pages usage répondent à la question concrète plutôt que de lister tous les modèles.",
    [
        ("Plâtre", "/usages/aspirateur-platre/", "Classe M · décolmatage"),
        ("Ponceuse", "/usages/aspirateur-ponceuse/", "Prise asservie · Festool · Mirka"),
        ("Atelier", "/usages/aspirateur-atelier/", "Usage polyvalent"),
        ("Bois &amp; sciure", "/usages/aspirateur-bois-sciure-copeaux/", "Gros volumes · copeaux"),
        ("Gravats", "/usages/aspirateur-gravats/", "Débris lourds · eau+poussière"),
        ("Scie", "/usages/aspirateur-scie/", "Circulaire · onglet · table"),
        ("Bricolage &amp; rénovation", "/usages/aspirateur-bricolage-renovation/", "Polyvalence · budget"),
    ]
))

USAGES = [
    ("/usages/aspirateur-platre/",
     "Quel aspirateur choisir pour le plâtre ?",
     "Filtration, décolmatage et débit : les critères spécifiques à l'aspiration de poussière de plâtre sur chantier.",
     "Pour aspirer régulièrement de la <strong>poussière de plâtre</strong>, privilégiez un aspirateur de chantier disposant d'une <strong>filtration classe M minimum</strong> et d'un <strong>décolmatage automatique du filtre</strong>. Pour un usage intensif avec une ponceuse girafe, la capacité à maintenir le débit d'air pendant le travail est généralement plus importante que la seule puissance électrique du moteur.",
     [("Classes L, M, H", "/guides/classes-l-m-h/"), ("Décolmatage automatique", "/guides/decolmatage-automatique/"), ("Aspirateur classe M", "/comparatifs/aspirateur-classe-m/"), ("Bosch GAS 35 M AFC", "/modeles/bosch-gas-35-m-afc/")]),
    ("/usages/aspirateur-ponceuse/",
     "Quel aspirateur choisir pour une ponceuse ?",
     "Prise asservie, décolmatage et compatibilité avec Festool, Mirka et ponceuses girafe : notre guide complet.",
     "Pour une ponceuse, trois critères dominent : la <strong>prise asservie</strong> (démarrage automatique avec l'outil), le <strong>décolmatage automatique</strong> pour maintenir le débit sous charge, et la <strong>compatibilité du raccord</strong> (Ø 27, 35 ou 36 mm selon la marque).",
     [("Festool CTL Midi", "/modeles/festool-ctl-midi/"), ("Prise asservie", "/guides/prise-asservie/"), ("Décolmatage automatique", "/guides/decolmatage-automatique/"), ("Marque Festool", "/marques/festool/"), ("Marque Mirka", "/marques/mirka/")]),
    ("/usages/aspirateur-atelier/",
     "Meilleur aspirateur d'atelier — Guide et sélection",
     "Aspirateur pour atelier : polyvalence, grande cuve, robustesse et entretien facile.",
     "",
     [("Kärcher WD6", "/modeles/karcher-wd6/"), ("Makita VC4210MX", "/modeles/makita-vc4210mx/"), ("Capacité cuve", "/guides/capacite-cuve/")]),
    ("/usages/aspirateur-bois-sciure-copeaux/",
     "Aspirateur pour bois, sciure et copeaux — Guide",
     "Aspiration de sciure, copeaux et poussières de bois : classe de filtration, débit et connexion machines.",
     "La sciure de bois dur (chêne, noyer, hêtre, frêne) est classée cancérigène de catégorie 1A au-dessus de 3 mg/m³ dans l'air. Une <strong>filtration classe M ou H</strong> est obligatoire pour le ponçage du bois dans un cadre professionnel.",
     [("Classes L, M, H", "/guides/classes-l-m-h/"), ("Filtre HEPA", "/guides/filtre-hepa-aspirateur/"), ("Makita VC4210MX", "/modeles/makita-vc4210mx/")]),
    ("/usages/aspirateur-gravats/",
     "Aspirateur pour gravats — Lequel choisir ?",
     "Gravats, débris lourds, eau résiduelle : les aspirateurs adaptés aux travaux de démolition et gros œuvre.",
     "Pour les gravats, privilégiez un aspirateur avec <strong>cuve acier ou plastique renforcé</strong>, une <strong>grande capacité (30 L+)</strong> et une fonction <strong>eau et poussière</strong>. La dépression est moins critique que la robustesse mécanique.",
     [("Eau et poussière", "/comparatifs/aspirateur-eau-poussiere/"), ("Kärcher NT 30/1 Tact", "/modeles/karcher-nt-30-1-tact/"), ("Nilfisk Multi II 30 T", "/modeles/nilfisk-multi-ii-30-t/")]),
    ("/usages/aspirateur-scie/",
     "Aspirateur pour scie de chantier — Guide",
     "Scie circulaire, scie à onglet, scie sur table : connexion directe et aspiration des sciures.",
     "Chaque type de scie impose un <strong>diamètre de raccord différent</strong>. Vérifiez la compatibilité avant l'achat ou prévoyez un adaptateur universel. La prise asservie est indispensable pour démarrer l'aspiration dès la mise en marche de la scie.",
     [("Prise asservie", "/guides/prise-asservie/"), ("Adaptateurs", "/accessoires/adaptateur-outil-electroportatif/"), ("Bois &amp; sciure", "/usages/aspirateur-bois-sciure-copeaux/")]),
    ("/usages/aspirateur-bricolage-renovation/",
     "Aspirateur de chantier pour bricolage et rénovation",
     "Quel aspirateur pour travaux de bricolage et rénovation à domicile ? Budget, polyvalence et facilité d'usage.",
     "Pour du bricolage et de la rénovation occasionnelle, un aspirateur <strong>classe L</strong> avec fonction eau+poussière suffit dans la majorité des cas. La classe M n'est obligatoire que si vous poncez régulièrement du plâtre, du béton ou du bois.",
     [("Kärcher WD5", "/modeles/karcher-wd5/"), ("Bosch AdvancedVac 20", "/modeles/bosch-advancedvac-20/"), ("Classes L, M, H", "/guides/classes-l-m-h/")]),
]

for path, title, desc, answer, related in USAGES:
    bc = breadcrumb(("Par usage", "/usages/"), title)
    write(path + "index.html", content_page(title, desc, path, bc, "usage", answer, related))

# ═══════════════════════════════════════════════════════════════════════════════
# MARQUES
# ═══════════════════════════════════════════════════════════════════════════════
write("/marques/index.html", hub_page(
    "Marques d'aspirateurs de chantier",
    "Présentation des marques d'aspirateurs de chantier : Kärcher, Bosch, Makita, Festool, DeWalt, Nilfisk, Parkside, Mirka.",
    "/marques/",
    breadcrumb("Marques"),
    "Kärcher, Bosch, Makita, Festool, DeWalt, Parkside, Nilfisk et Mirka : huit univers de gamme à comparer selon l’usage, les classes, les outils et l’écosystème.",
    [
        ("Kärcher", "/marques/karcher/", "WD2 / WD5 / WD6 / NT"),
        ("Bosch", "/marques/bosch/", "AdvancedVac / GAS"),
        ("Makita", "/marques/makita/", "VC serie"),
        ("Festool", "/marques/festool/", "CTL / CT"),
        ("DeWalt", "/marques/dewalt/", "DXV serie"),
        ("Parkside", "/marques/parkside/", "PNTS série"),
        ("Nilfisk", "/marques/nilfisk/", "Multi / Attix"),
        ("Mirka", "/marques/mirka/", "DE / DEROS"),
    ]
))

MARQUES = [
    ("/marques/karcher/", "Kärcher — Aspirateurs de chantier : gamme et avis",
     "Tout sur les aspirateurs de chantier Kärcher : WD2, WD5, WD6, NT 30/1. Gamme, comparatifs et conseils d'achat.",
     [("Kärcher WD2", "/modeles/karcher-wd2/"), ("Kärcher WD5", "/modeles/karcher-wd5/"), ("Kärcher WD6", "/modeles/karcher-wd6/"), ("Kärcher NT 30/1 Tact", "/modeles/karcher-nt-30-1-tact/"), ("Meilleur aspirateur chantier", "/comparatifs/meilleur-aspirateur-de-chantier/")]),
    ("/marques/bosch/", "Bosch — Aspirateurs de chantier GAS et AdvancedVac",
     "Gamme Bosch Professional : GAS 12-25 PL, GAS 18V-10 L, GAS 35 L/M AFC. Tests et comparatifs.",
     [("Bosch AdvancedVac 20", "/modeles/bosch-advancedvac-20/"), ("Bosch GAS 12-25 PL", "/modeles/bosch-gas-12-25-pl/"), ("Bosch GAS 18V-10 L", "/modeles/bosch-gas-18v-10-l/"), ("Bosch GAS 35 L AFC", "/modeles/bosch-gas-35-l-afc/"), ("Bosch GAS 35 M AFC", "/modeles/bosch-gas-35-m-afc/")]),
    ("/marques/makita/", "Makita — Aspirateurs de chantier VC",
     "Aspirateurs de chantier Makita : VC2512L, VC4210MX. Compatibilité batterie 18V et 40V.",
     [("Makita VC2512L", "/modeles/makita-vc2512l/"), ("Makita VC4210MX", "/modeles/makita-vc4210mx/"), ("Sans fil", "/comparatifs/aspirateur-chantier-sans-fil/")]),
    ("/marques/festool/", "Festool — Aspirateurs CT et CTL pour ponçage",
     "Les aspirateurs Festool CTL Midi et CT Series : la référence pour le ponçage professionnel.",
     [("Festool CTL Midi", "/modeles/festool-ctl-midi/"), ("Ponceuse", "/usages/aspirateur-ponceuse/"), ("Aspirateur classe M", "/comparatifs/aspirateur-classe-m/")]),
    ("/marques/dewalt/", "DeWalt — Aspirateurs de chantier DXV",
     "Gamme DeWalt DXV : aspirateurs professionnels compatibles batteries 18V et 54V FlexVolt.",
     [("Sans fil", "/comparatifs/aspirateur-chantier-sans-fil/"), ("Aspirateur professionnel", "/comparatifs/aspirateur-professionnel/")]),
    ("/marques/parkside/", "Parkside — Aspirateurs de chantier PNTS",
     "Aspirateurs de chantier Parkside (Lidl) : rapport qualité-prix, limites et alternatives.",
     [("Petit aspirateur", "/comparatifs/petit-aspirateur-de-chantier/"), ("Bricolage", "/usages/aspirateur-bricolage-renovation/")]),
    ("/marques/nilfisk/", "Nilfisk — Aspirateurs industriels et professionnels",
     "Gamme Nilfisk Multi et Attix : aspirateurs industriels pour usage professionnel intensif.",
     [("Nilfisk Multi II 30 T", "/modeles/nilfisk-multi-ii-30-t/"), ("Aspirateur industriel", "/comparatifs/aspirateur-industriel/")]),
    ("/marques/mirka/", "Mirka — Aspirateurs pour ponceuses",
     "Les aspirateurs Mirka, optimisés pour les ponceuses orbitales DEROS et DE. Compatibilité et performances.",
     [("Ponceuse", "/usages/aspirateur-ponceuse/"), ("Festool CTL Midi", "/modeles/festool-ctl-midi/"), ("Classe M", "/comparatifs/aspirateur-classe-m/")]),
]

for path, title, desc, related in MARQUES:
    brand = title.split("—")[0].strip()
    bc = breadcrumb(("Marques", "/marques/"), brand)
    write(path + "index.html", content_page(title, desc, path, bc, "marque", "", related))

# ═══════════════════════════════════════════════════════════════════════════════
# MODÈLES
# ═══════════════════════════════════════════════════════════════════════════════
write("/modeles/index.html", hub_page(
    "Fiches techniques — Aspirateurs de chantier",
    "Fiches techniques normalisées des principaux aspirateurs de chantier : données vérifiées, dépression, débit, classe, décolmatage.",
    "/modeles/",
    breadcrumb("Modèles"),
    "Chaque fiche modèle est une entité structurée avec des données normalisées : dépression (kPa), débit (L/s), classe de filtration, décolmatage, prise asservie. Données vérifiées régulièrement.",
    [
        ("Kärcher WD2", "/modeles/karcher-wd2/", "Classe L · entrée de gamme"),
        ("Kärcher WD5", "/modeles/karcher-wd5/", "Classe L · eau+poussière"),
        ("Kärcher WD6", "/modeles/karcher-wd6/", "Classe L · premium"),
        ("Kärcher NT 30/1 Tact", "/modeles/karcher-nt-30-1-tact/", "Classe M · professionnel"),
        ("Bosch AdvancedVac 20", "/modeles/bosch-advancedvac-20/", "Classe L · compact"),
        ("Bosch GAS 12-25 PL", "/modeles/bosch-gas-12-25-pl/", "Classe L · entrée gamme Pro"),
        ("Bosch GAS 18V-10 L", "/modeles/bosch-gas-18v-10-l/", "Classe L · sans fil 18V"),
        ("Bosch GAS 35 L AFC", "/modeles/bosch-gas-35-l-afc/", "Classe L · décolmatage auto"),
        ("Bosch GAS 35 M AFC", "/modeles/bosch-gas-35-m-afc/", "Classe M · référence pro"),
        ("Makita VC2512L", "/modeles/makita-vc2512l/", "Classe L · 25 litres"),
        ("Makita VC4210MX", "/modeles/makita-vc4210mx/", "Classe L · 42 litres"),
        ("Festool CTL Midi", "/modeles/festool-ctl-midi/", "Classe M · ponçage"),
        ("Nilfisk Multi II 30 T", "/modeles/nilfisk-multi-ii-30-t/", "Classe L · industriel"),
    ]
))

MODELES = [
    ("/modeles/karcher-wd2/", "Kärcher WD2", "Kärcher", "L",
     "Fiche technique Kärcher WD2 : aspirateur eau et poussière entrée de gamme.",
     {"Marque": "Kärcher", "Modèle": "WD2", "Classe filtration": "L", "Capacité cuve": "— L", "Puissance moteur": "1000 W", "Dépression max.": "— kPa", "Débit max.": "— L/s", "Eau + poussière": "Oui", "Décolmatage auto": "Non", "Prise asservie": "Non", "Poids": "— kg", "Données vérifiées": "MM/AAAA"},
     ["Nettoyage après bricolage", "Liquides renversés", "Budget limité"],
     ["Usage professionnel intensif", "Poussières fines (plâtre, ponçage)"],
     [("Kärcher WD5", "/modeles/karcher-wd5/"), ("Meilleur aspirateur chantier", "/comparatifs/meilleur-aspirateur-de-chantier/"), ("Marque Kärcher", "/marques/karcher/")]),
    ("/modeles/karcher-wd5/", "Kärcher WD5", "Kärcher", "L",
     "Fiche technique Kärcher WD5 : aspirateur eau et poussière polyvalent, bon rapport qualité-prix.",
     {"Marque": "Kärcher", "Modèle": "WD5", "Classe filtration": "L", "Capacité cuve": "— L", "Puissance moteur": "1100 W", "Dépression max.": "— kPa", "Débit max.": "— L/s", "Eau + poussière": "Oui", "Décolmatage auto": "Non", "Prise asservie": "Non", "Poids": "— kg", "Données vérifiées": "MM/AAAA"},
     ["Polyvalence eau + poussière", "Bricolage régulier", "Rapport qualité-prix"],
     ["Ponçage plâtre intensif", "Usage professionnel journalier"],
     [("Kärcher WD6", "/modeles/karcher-wd6/"), ("Kärcher WD2", "/modeles/karcher-wd2/"), ("Marque Kärcher", "/marques/karcher/")]),
    ("/modeles/karcher-wd6/", "Kärcher WD6", "Kärcher", "L",
     "Fiche technique Kärcher WD6 : le meilleur aspirateur eau et poussière de la gamme grand public Kärcher.",
     {"Marque": "Kärcher", "Modèle": "WD6", "Classe filtration": "L", "Capacité cuve": "30 L", "Puissance moteur": "1200 W", "Dépression max.": "30 kPa", "Débit max.": "— L/s", "Eau + poussière": "Oui", "Décolmatage auto": "Non", "Prise asservie": "Non", "Poids": "— kg", "Données vérifiées": "MM/AAAA"},
     ["Meilleur rapport Q/P classe L", "Grande cuve", "Eau + poussière"],
     ["Filtration classe M ou H requise", "Ponçage intensif"],
     [("Kärcher NT 30/1 Tact", "/modeles/karcher-nt-30-1-tact/"), ("Eau et poussière", "/comparatifs/aspirateur-eau-poussiere/"), ("Marque Kärcher", "/marques/karcher/")]),
    ("/modeles/karcher-nt-30-1-tact/", "Kärcher NT 30/1 Tact", "Kärcher", "M",
     "Fiche technique Kärcher NT 30/1 Tact : aspirateur professionnel classe M avec décolmatage Tact.",
     {"Marque": "Kärcher", "Modèle": "NT 30/1 Tact", "Classe filtration": "M", "Capacité cuve": "30 L", "Puissance moteur": "1380 W", "Dépression max.": "— kPa", "Débit max.": "— L/s", "Eau + poussière": "Oui", "Décolmatage": "Tact (semi-auto)", "Prise asservie": "Oui", "Poids": "— kg", "Données vérifiées": "MM/AAAA"},
     ["Usage professionnel classe M", "Semi-décolmatage Tact", "Grande cuve"],
     ["Prix plus élevé que concurrents directs", "Pas de décolmatage entièrement automatique"],
     [("Bosch GAS 35 M AFC", "/modeles/bosch-gas-35-m-afc/"), ("Aspirateur classe M", "/comparatifs/aspirateur-classe-m/"), ("Marque Kärcher", "/marques/karcher/")]),
    ("/modeles/bosch-advancedvac-20/", "Bosch AdvancedVac 20", "Bosch", "L",
     "Fiche technique Bosch AdvancedVac 20 : aspirateur compact et polyvalent pour bricolage.",
     {"Marque": "Bosch", "Modèle": "AdvancedVac 20", "Classe filtration": "L", "Capacité cuve": "20 L", "Puissance moteur": "600 W", "Dépression max.": "— kPa", "Débit max.": "— L/s", "Eau + poussière": "Non", "Décolmatage auto": "Non", "Prise asservie": "Oui", "Poids": "— kg", "Données vérifiées": "MM/AAAA"},
     ["Compact et maniable", "Prise asservie", "Bricolage régulier"],
     ["Capacité limitée", "Non eau + poussière", "Usage professionnel intensif"],
     [("Bosch GAS 12-25 PL", "/modeles/bosch-gas-12-25-pl/"), ("Petit aspirateur", "/comparatifs/petit-aspirateur-de-chantier/"), ("Marque Bosch", "/marques/bosch/")]),
    ("/modeles/bosch-gas-12-25-pl/", "Bosch GAS 12-25 PL", "Bosch", "L",
     "Fiche technique Bosch GAS 12-25 PL : aspirateur professionnel compact entrée de gamme.",
     {"Marque": "Bosch Professional", "Modèle": "GAS 12-25 PL", "Classe filtration": "L", "Capacité cuve": "25 L", "Puissance moteur": "1250 W", "Dépression max.": "— kPa", "Débit max.": "— L/s", "Eau + poussière": "Non", "Décolmatage auto": "Non", "Prise asservie": "Oui", "Poids": "— kg", "Données vérifiées": "MM/AAAA"},
     ["Usage professionnel classe L", "Prise asservie", "Rapport qualité-prix"],
     ["Pas de décolmatage automatique", "Classe L uniquement"],
     [("Bosch GAS 35 L AFC", "/modeles/bosch-gas-35-l-afc/"), ("Marque Bosch", "/marques/bosch/")]),
    ("/modeles/bosch-gas-18v-10-l/", "Bosch GAS 18V-10 L", "Bosch", "L",
     "Fiche technique Bosch GAS 18V-10 L : aspirateur de chantier sans fil 18V, compact.",
     {"Marque": "Bosch Professional", "Modèle": "GAS 18V-10 L", "Classe filtration": "L", "Capacité cuve": "10 L", "Alimentation": "18V (sans fil)", "Batterie incluse": "Non (vendu nu)", "Dépression max.": "— kPa", "Débit max.": "— L/s", "Eau + poussière": "Non", "Décolmatage auto": "Non", "Prise asservie": "Oui", "Poids (nu)": "— kg", "Données vérifiées": "MM/AAAA"},
     ["Mobilité sans câble", "Prise asservie", "Système batterie 18V Bosch"],
     ["Autonomie limitée", "Cuve 10 L seulement", "Incompatible usage eau"],
     [("Sans fil", "/comparatifs/aspirateur-chantier-sans-fil/"), ("Bosch GAS 35 L AFC", "/modeles/bosch-gas-35-l-afc/"), ("Marque Bosch", "/marques/bosch/")]),
    ("/modeles/bosch-gas-35-l-afc/", "Bosch GAS 35 L AFC", "Bosch", "L",
     "Fiche technique Bosch GAS 35 L AFC : aspirateur classe L avec décolmatage automatique.",
     {"Marque": "Bosch Professional", "Modèle": "GAS 35 L AFC", "Classe filtration": "L", "Capacité cuve": "35 L", "Puissance moteur": "1380 W", "Dépression max.": "27 kPa", "Débit max.": "56 L/s", "Eau + poussière": "Oui", "Décolmatage": "Automatique (AFC)", "Prise asservie": "Oui", "Poids": "— kg", "Données vérifiées": "MM/AAAA"},
     ["Décolmatage AFC automatique", "Grande cuve 35 L", "Eau + poussière", "Prise asservie"],
     ["Classe L uniquement (pas M)", "Encombrant"],
     [("Bosch GAS 35 M AFC", "/modeles/bosch-gas-35-m-afc/"), ("Décolmatage auto", "/guides/decolmatage-automatique/"), ("Marque Bosch", "/marques/bosch/")]),
    ("/modeles/bosch-gas-35-m-afc/", "Bosch GAS 35 M AFC", "Bosch", "M",
     "Fiche technique Bosch GAS 35 M AFC : la référence aspirateur de chantier classe M avec décolmatage automatique.",
     {"Marque": "Bosch Professional", "Modèle": "GAS 35 M AFC", "Classe filtration": "M", "Capacité cuve": "35 L", "Puissance moteur": "1380 W", "Dépression max.": "27 kPa", "Débit max.": "56 L/s", "Eau + poussière": "Oui", "Décolmatage": "Automatique (AFC)", "Prise asservie": "Oui", "Antistatic": "Oui", "Poids": "— kg", "Longueur câble": "5 m", "Usage recommandé": "Plâtre / ponçage / chantier intensif", "Données vérifiées": "MM/AAAA"},
     ["Filtration classe M validée", "Décolmatage AFC automatique", "Cuve 35 L", "Prise asservie", "Eau + poussière", "Antistatic"],
     ["Prix premium", "Encombrant (35 L)", "Pas de batterie"],
     [("Bosch GAS 35 L AFC", "/modeles/bosch-gas-35-l-afc/"), ("Aspirateur classe M", "/comparatifs/aspirateur-classe-m/"), ("Plâtre", "/usages/aspirateur-platre/"), ("Ponceuse", "/usages/aspirateur-ponceuse/"), ("Marque Bosch", "/marques/bosch/")]),
    ("/modeles/makita-vc2512l/", "Makita VC2512L", "Makita", "L",
     "Fiche technique Makita VC2512L : aspirateur de chantier classe L 25 litres.",
     {"Marque": "Makita", "Modèle": "VC2512L", "Classe filtration": "L", "Capacité cuve": "25 L", "Puissance moteur": "1000 W", "Dépression max.": "— kPa", "Débit max.": "— L/s", "Eau + poussière": "Non", "Décolmatage auto": "Non", "Prise asservie": "Oui", "Poids": "— kg", "Données vérifiées": "MM/AAAA"},
     ["Fiabilité Makita", "Prise asservie", "Bon rapport qualité-prix"],
     ["Pas de décolmatage automatique", "Classe L uniquement"],
     [("Makita VC4210MX", "/modeles/makita-vc4210mx/"), ("Marque Makita", "/marques/makita/")]),
    ("/modeles/makita-vc4210mx/", "Makita VC4210MX", "Makita", "L",
     "Fiche technique Makita VC4210MX : grand aspirateur de chantier classe L 42 litres.",
     {"Marque": "Makita", "Modèle": "VC4210MX", "Classe filtration": "L", "Capacité cuve": "42 L", "Puissance moteur": "1050 W", "Dépression max.": "— kPa", "Débit max.": "— L/s", "Eau + poussière": "Non", "Décolmatage auto": "Non", "Prise asservie": "Oui", "Poids": "— kg", "Données vérifiées": "MM/AAAA"},
     ["Grande capacité 42 L", "Idéal atelier", "Fiabilité Makita"],
     ["Volumineux", "Pas de décolmatage auto"],
     [("Makita VC2512L", "/modeles/makita-vc2512l/"), ("Atelier", "/usages/aspirateur-atelier/"), ("Marque Makita", "/marques/makita/")]),
    ("/modeles/festool-ctl-midi/", "Festool CTL Midi", "Festool", "M",
     "Fiche technique Festool CTL Midi : la référence aspirateur classe M pour le ponçage professionnel.",
     {"Marque": "Festool", "Modèle": "CTL Midi", "Classe filtration": "M", "Capacité cuve": "17 L", "Puissance moteur": "700 W", "Dépression max.": "— kPa", "Débit max.": "— L/s", "Eau + poussière": "Non", "Décolmatage": "Automatique", "Prise asservie": "Oui (Bluetooth)", "Connectivité": "Bluetooth Festool", "Poids": "— kg", "Usage recommandé": "Ponçage professionnel", "Données vérifiées": "MM/AAAA"},
     ["Intégration parfaite ponceuses Festool", "Décolmatage automatique", "Compact 17 L", "Prise asservie Bluetooth"],
     ["Prix très élevé", "Pas eau + poussière", "Écosystème Festool fermé"],
     [("Ponceuse", "/usages/aspirateur-ponceuse/"), ("Aspirateur classe M", "/comparatifs/aspirateur-classe-m/"), ("Marque Festool", "/marques/festool/"), ("Marque Mirka", "/marques/mirka/")]),
    ("/modeles/nilfisk-multi-ii-30-t/", "Nilfisk Multi II 30 T", "Nilfisk", "L",
     "Fiche technique Nilfisk Multi II 30 T : aspirateur industriel polyvalent 30 litres.",
     {"Marque": "Nilfisk", "Modèle": "Multi II 30 T", "Classe filtration": "L", "Capacité cuve": "30 L", "Puissance moteur": "1400 W", "Dépression max.": "— kPa", "Débit max.": "— L/s", "Eau + poussière": "Oui", "Décolmatage auto": "Non", "Prise asservie": "Non", "Poids": "— kg", "Données vérifiées": "MM/AAAA"},
     ["Construction robuste", "Grande cuve industrielle", "Eau + poussière"],
     ["Pas de décolmatage automatique", "Accessoires propriétaires"],
     [("Aspirateur industriel", "/comparatifs/aspirateur-industriel/"), ("Marque Nilfisk", "/marques/nilfisk/"), ("Eau et poussière", "/comparatifs/aspirateur-eau-poussiere/")]),
]

for (path, model_name, brand, dust_class, desc, specs, pros, cons, related) in MODELES:
    bc = breadcrumb(("Modèles", "/modeles/"), model_name)
    title = f"{model_name} — Fiche technique et avis"
    write(path + "index.html", model_page(title, desc, path, bc, model_name, brand, dust_class, specs, pros, cons, related))

# ═══════════════════════════════════════════════════════════════════════════════
# GUIDES
# ═══════════════════════════════════════════════════════════════════════════════
write("/guides/index.html", hub_page(
    "Guides techniques — Aspirateurs de chantier",
    "Guides pour comprendre et choisir un aspirateur de chantier : classes L/M/H, décolmatage, dépression, débit, filtres HEPA.",
    "/guides/",
    breadcrumb("Guides"),
    "La partie technique est souvent négligée par les sites d'affiliation. Ces guides répondent aux questions que posent les vrais utilisateurs aux moteurs de recherche et aux assistants IA.",
    [
        ("Comment choisir ?", "/guides/comment-choisir-aspirateur-de-chantier/", "Guide complet"),
        ("Classes L, M et H", "/guides/classes-l-m-h/", "Réglementation et usage"),
        ("Décolmatage automatique", "/guides/decolmatage-automatique/", "Fonctionnement et intérêt"),
        ("Prise asservie", "/guides/prise-asservie/", "Démarrage automatique"),
        ("Puissance moteur", "/guides/puissance-aspiration/", "Watts réels vs marketing"),
        ("kPa, mbar, Air Watts", "/guides/depression-kpa-mbar-air-watt/", "Décrypter les unités"),
        ("Débit d'air", "/guides/debit-air-aspirateur/", "L/s, m³/h : ce qui compte"),
        ("Capacité cuve", "/guides/capacite-cuve/", "20, 30 ou 40 litres ?"),
        ("Filtre HEPA", "/guides/filtre-hepa-aspirateur/", "H13/H14 sur chantier"),
        ("Sac ou sans sac", "/guides/sac-ou-sans-sac/", "Coût et filtration réelle"),
        ("Entretien", "/guides/entretien-aspirateur-chantier/", "Maintenance et durée de vie"),
    ]
))

GUIDES = [
    ("/guides/comment-choisir-aspirateur-de-chantier/",
     "Comment choisir un aspirateur de chantier ?",
     "Tous les critères pour bien choisir : classe de filtration, dépression, débit, décolmatage, prise asservie et budget.",
     "Le critère n°1 est la <strong>classe de filtration</strong> (L, M ou H), qui dépend du type de poussières aspirées. Ensuite viennent la <strong>dépression</strong> (capacité à soulever les débris), le <strong>débit d'air</strong> (maintenu sous charge), et les équipements pratiques : décolmatage automatique, prise asservie.",
     [("Classes L, M, H", "/guides/classes-l-m-h/"), ("kPa et mbar", "/guides/depression-kpa-mbar-air-watt/"), ("Débit d'air", "/guides/debit-air-aspirateur/"), ("Comparatif général", "/comparatifs/meilleur-aspirateur-de-chantier/")]),
    ("/guides/classes-l-m-h/",
     "Classes L, M et H — Quelle classe choisir ?",
     "Différence entre aspirateur de chantier classe L, M et H : réglementation européenne, efficacité de filtration et cas d'usage.",
     "La <strong>classe L</strong> filtre 99 % des poussières à partir de 1 µm. La <strong>classe M</strong> filtre 99,9 % à 0,1–1 µm (plâtre, béton, bois dur). La <strong>classe H</strong> filtre 99,995 % et est requise pour l'amiante et les poussières cancérigènes. Le choix dépend du matériau aspiré, pas de la durée d'usage.",
     [("Décolmatage automatique", "/guides/decolmatage-automatique/"), ("Plâtre", "/usages/aspirateur-platre/"), ("Bois et sciure", "/usages/aspirateur-bois-sciure-copeaux/"), ("Aspirateur classe M", "/comparatifs/aspirateur-classe-m/")]),
    ("/guides/decolmatage-automatique/",
     "Décolmatage automatique — À quoi ça sert vraiment ?",
     "Fonctionnement du décolmatage automatique (AFC), impact sur le débit d'air et durée de vie du filtre.",
     "Le décolmatage automatique consiste à envoyer une impulsion d'air inverse dans le filtre pour décoller les poussières accumulées. Il maintient le <strong>débit d'air constant</strong> pendant le travail, ce qui est particulièrement critique avec une ponceuse ou en aspirant du plâtre. Sans décolmatage, le débit chute progressivement à mesure que le filtre se charge.",
     [("Débit d'air", "/guides/debit-air-aspirateur/"), ("Ponceuse", "/usages/aspirateur-ponceuse/"), ("Plâtre", "/usages/aspirateur-platre/"), ("Bosch GAS 35 M AFC", "/modeles/bosch-gas-35-m-afc/")]),
    ("/guides/prise-asservie/",
     "Prise asservie — Fonctionnement et compatibilité",
     "La prise asservie démarre l'aspirateur automatiquement avec l'outil électroportatif. Fonctionnement, puissance maximale et compatibilité.",
     "La <strong>prise asservie</strong> (ou prise de courant commutée) alimente l'outil connecté et démarre l'aspirateur automatiquement dès la mise en marche de l'outil. Vérifiez la puissance maximale supportée (généralement 2 200 W) avant de brancher un outil puissant.",
     [("Ponceuse", "/usages/aspirateur-ponceuse/"), ("Scie", "/usages/aspirateur-scie/"), ("Adaptateur outil", "/accessoires/adaptateur-outil-electroportatif/")]),
    ("/guides/puissance-aspiration/",
     "Puissance d'un aspirateur de chantier — Watts réels vs marketing",
     "Quelle puissance faut-il pour un aspirateur de chantier ? Décryptage des watts moteur et métriques réelles.",
     "La puissance moteur en watts est le <strong>critère le moins fiable</strong> pour comparer des aspirateurs de chantier. Un aspirateur de 1 000 W bien conçu peut surpasser un modèle de 1 800 W mal optimisé. Les métriques pertinentes sont la dépression maximale (kPa) et le débit d'air (L/s).",
     [("kPa, mbar, Air Watts", "/guides/depression-kpa-mbar-air-watt/"), ("Débit d'air", "/guides/debit-air-aspirateur/"), ("Comparatif puissants", "/comparatifs/aspirateur-chantier-puissant/")]),
    ("/guides/depression-kpa-mbar-air-watt/",
     "kPa, mbar, Air Watts — Décrypter les unités de dépression",
     "Comprendre les unités de mesure des aspirateurs de chantier : kPa, mbar, mmH₂O, Air Watts. Lesquelles comparer.",
     "La <strong>dépression maximale</strong> mesure la capacité à soulever des débris lourds. 1 kPa = 10 mbar = 102 mmH₂O. Les <strong>Air Watts</strong> (ou Watts air) combinent dépression et débit : c'est la métrique la plus représentative de la performance réelle, mais rarement publiée par les fabricants.",
     [("Débit d'air", "/guides/debit-air-aspirateur/"), ("Puissance moteur", "/guides/puissance-aspiration/"), ("Comment choisir", "/guides/comment-choisir-aspirateur-de-chantier/")]),
    ("/guides/debit-air-aspirateur/",
     "Débit d'air d'un aspirateur de chantier — Ce qu'il faut savoir",
     "Quel débit d'air faut-il pour un aspirateur de chantier ? L/s, m³/h, débit sous charge vs débit à vide.",
     "Le débit d'air (exprimé en L/s ou m³/h) mesure la quantité d'air déplacée. C'est le critère clé pour l'aspiration de <strong>débris légers comme les copeaux et la sciure</strong>. Attention : le débit publié est souvent mesuré à vide. Avec un outil connecté et un filtre chargé, il peut chuter significativement — d'où l'importance du décolmatage automatique.",
     [("Décolmatage automatique", "/guides/decolmatage-automatique/"), ("kPa et mbar", "/guides/depression-kpa-mbar-air-watt/"), ("Bois et sciure", "/usages/aspirateur-bois-sciure-copeaux/")]),
    ("/guides/capacite-cuve/",
     "Capacité de cuve — 20, 30 ou 40 litres ?",
     "Quelle capacité de cuve choisir pour un aspirateur de chantier ? Impact sur l'autonomie et le transport.",
     "Une cuve de <strong>20 à 25 litres</strong> convient pour la plupart des travaux de bricolage. Pour un usage professionnel quotidien, <strong>30 à 35 litres</strong> réduit les arrêts pour vidage. Au-delà de 40 litres, l'aspirateur devient difficile à déplacer. Une cuve plus grande n'améliore pas les performances d'aspiration.",
     [("Atelier", "/usages/aspirateur-atelier/"), ("Gravats", "/usages/aspirateur-gravats/"), ("Makita VC4210MX", "/modeles/makita-vc4210mx/")]),
    ("/guides/filtre-hepa-aspirateur/",
     "Filtre HEPA H13/H14 sur un aspirateur de chantier — Utile ou superflu ?",
     "Le filtre HEPA est-il vraiment nécessaire sur un aspirateur de chantier ? Différence H13, H14 et filtres classe H.",
     "Un filtre <strong>HEPA H13</strong> filtre 99,95 % des particules à 0,3 µm. Il est requis pour les poussières classées cancérigènes (bois dur, silice cristalline, amiante). Pour du plâtre ou du béton ordinaire, la <strong>classe M</strong> suffit réglementairement. Ne confondez pas HEPA (norme filtre) et classe H (norme aspirateur).",
     [("Classes L, M, H", "/guides/classes-l-m-h/"), ("Bois et sciure", "/usages/aspirateur-bois-sciure-copeaux/"), ("Filtres accessoires", "/accessoires/filtres-aspirateur-chantier/")]),
    ("/guides/sac-ou-sans-sac/",
     "Sac ou sans sac pour un aspirateur de chantier ?",
     "Aspirateur de chantier avec ou sans sac : filtration réelle, coût d'utilisation et facilité de vidage.",
     "Le sac filtrant améliore souvent la <strong>filtration des poussières fines</strong> et facilite le vidage sans remise en suspension. Sans sac, l'entretien est moins coûteux mais la filtration dépend entièrement du filtre principal. En classe M et H, l'utilisation d'un sac est généralement recommandée.",
     [("Classes L, M, H", "/guides/classes-l-m-h/"), ("Sacs aspirateur", "/accessoires/sacs-aspirateur-chantier/"), ("Filtres", "/accessoires/filtres-aspirateur-chantier/")]),
    ("/guides/entretien-aspirateur-chantier/",
     "Entretien d'un aspirateur de chantier — Guide complet",
     "Comment entretenir un aspirateur de chantier pour prolonger sa durée de vie : filtre, cuve, tuyau, moteur.",
     "",
     [("Filtres", "/accessoires/filtres-aspirateur-chantier/"), ("Sacs", "/accessoires/sacs-aspirateur-chantier/"), ("Décolmatage automatique", "/guides/decolmatage-automatique/")]),
]

for path, title, desc, answer, related in GUIDES:
    bc = breadcrumb(("Guides", "/guides/"), title)
    write(path + "index.html", content_page(title, desc, path, bc, "guide", answer, related))

# ═══════════════════════════════════════════════════════════════════════════════
# ACCESSOIRES
# ═══════════════════════════════════════════════════════════════════════════════
write("/accessoires/index.html", hub_page(
    "Accessoires pour aspirateurs de chantier",
    "Sacs, filtres, flexibles, tuyaux et adaptateurs pour aspirateurs de chantier.",
    "/accessoires/",
    breadcrumb("Accessoires"),
    "Les accessoires déterminent souvent l'efficacité réelle d'un aspirateur. Un bon sac ou filtre peut transformer un modèle ordinaire.",
    [
        ("Sacs aspirateur de chantier", "/accessoires/sacs-aspirateur-chantier/", "Filtrés, non-tissés"),
        ("Filtres aspirateur de chantier", "/accessoires/filtres-aspirateur-chantier/", "HEPA, plissés, classe M/H"),
        ("Flexible et tuyaux", "/accessoires/flexible-tuyau-aspirateur/", "Longueur, diamètre, antistatic"),
        ("Adaptateurs outil électroportatif", "/accessoires/adaptateur-outil-electroportatif/", "Ø 27/35/36 mm"),
    ]
))

ACCESSOIRES = [
    ("/accessoires/sacs-aspirateur-chantier/", "Sacs pour aspirateur de chantier — Guide et sélection",
     "Quels sacs choisir pour votre aspirateur de chantier ? Compatibilité, matière filtrante et fréquence de remplacement.",
     "",
     [("Sac ou sans sac ?", "/guides/sac-ou-sans-sac/"), ("Filtres", "/accessoires/filtres-aspirateur-chantier/")]),
    ("/accessoires/filtres-aspirateur-chantier/", "Filtres pour aspirateur de chantier — Sélection",
     "Filtres plissés, HEPA H13/H14, classe M et H pour aspirateurs de chantier. Compatibilité et remplacement.",
     "",
     [("Filtre HEPA", "/guides/filtre-hepa-aspirateur/"), ("Classes L, M, H", "/guides/classes-l-m-h/"), ("Sacs", "/accessoires/sacs-aspirateur-chantier/")]),
    ("/accessoires/flexible-tuyau-aspirateur/", "Flexible et tuyaux pour aspirateur de chantier",
     "Extension de longueur, diamètres standards (27, 35, 36 mm), flexibles antistatiques pour aspiration de copeaux.",
     "",
     [("Adaptateurs", "/accessoires/adaptateur-outil-electroportatif/"), ("Bois et sciure", "/usages/aspirateur-bois-sciure-copeaux/")]),
    ("/accessoires/adaptateur-outil-electroportatif/", "Adaptateurs outil électroportatif — Raccords et compatibilité",
     "Adaptateurs pour connecter votre outil électroportatif (ponceuse, scie) à votre aspirateur. Diamètres et marques.",
     "",
     [("Prise asservie", "/guides/prise-asservie/"), ("Ponceuse", "/usages/aspirateur-ponceuse/"), ("Scie", "/usages/aspirateur-scie/")]),
]

for path, title, desc, answer, related in ACCESSOIRES:
    bc = breadcrumb(("Accessoires", "/accessoires/"), title.split("—")[0].strip())
    write(path + "index.html", content_page(title, desc, path, bc, "guide", answer, related))

# ═══════════════════════════════════════════════════════════════════════════════
# FOOTER PAGES
# ═══════════════════════════════════════════════════════════════════════════════
FOOTER_PAGES = [
    ("/methode-de-test/", "Méthode de test — aspirateurs-chantier.fr",
     "Notre protocole de test des aspirateurs de chantier : dépression, débit, filtration, bruit, durée de vie."),
    ("/a-propos/", "À propos — aspirateurs-chantier.fr",
     "Qui sommes-nous ? Notre engagement pour des données techniques vérifiées et des recommandations indépendantes."),
    ("/contact/", "Contact — aspirateurs-chantier.fr",
     "Contactez l'équipe d'aspirateurs-chantier.fr."),
    ("/transparence-affiliation/", "Transparence sur l'affiliation — aspirateurs-chantier.fr",
     "Comment fonctionnent nos liens affiliés et comment préservons-nous l'indépendance de nos recommandations."),
    ("/mentions-legales/", "Mentions légales — aspirateurs-chantier.fr",
     "Mentions légales, politique de confidentialité et conditions d'utilisation du site."),
]

for path, title, desc in FOOTER_PAGES:
    slug = path.strip("/").replace("-", " ").title()
    bc = breadcrumb(slug)
    write(path + "index.html", content_page(title, desc, path, bc))

print("\n✅ Toutes les pages ont été générées.")
