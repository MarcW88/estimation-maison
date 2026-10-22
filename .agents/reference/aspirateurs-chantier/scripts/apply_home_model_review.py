#!/usr/bin/env python3
"""Apply the reviewed homepage structure and small comparison-label cleanup.

The homepage is treated as an orientation page: start from risk/workflow, then
usage, then documented reference profiles, brands and methodology. Model-page
polish is CSS-only so verified editorial bodies remain untouched.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"

HOME_MAIN = r'''<main>

<section class="hero home-hero">
  <div class="container">
    <div class="hero-inner home-hero-grid">
      <div class="home-hero-copy">
        <div class="hero-eyebrow">Guide technique indépendant — données, usages et comparatifs</div>
        <h1 class="hero-title">Aspirateurs de chantier :<br>choisir selon le risque et le travail réel.</h1>
        <p class="hero-desc lead">Poussière à capter, outil raccordé, durée des sessions, mobilité et collecte : nous remettons les caractéristiques constructeur dans leur contexte avant de comparer les modèles.</p>
        <div class="hero-actions">
          <a href="/comparatifs/meilleur-aspirateur-de-chantier/" class="btn btn-primary btn-lg">Comparer par profil</a>
          <a href="/guides/comment-choisir-aspirateur-de-chantier/" class="btn btn-outline btn-lg">Construire mon cahier des charges</a>
        </div>
      </div>
      <aside class="home-decision-panel" aria-label="Commencer selon votre besoin">
        <p class="eyebrow">Commencer ici</p>
        <h2>Quel problème devez-vous résoudre ?</h2>
        <div class="home-decision-list">
          <a class="home-decision-link" href="/guides/classes-l-m-h/"><span class="home-decision-index">01</span><span><strong>Poussière à risque</strong>Commencez par la classe réellement requise, pas par la puissance.</span><span class="home-decision-arrow">→</span></a>
          <a class="home-decision-link" href="/usages/aspirateur-ponceuse/"><span class="home-decision-index">02</span><span><strong>Captage avec un outil</strong>Raccord, prise asservie et maintien du débit deviennent centraux.</span><span class="home-decision-arrow">→</span></a>
          <a class="home-decision-link" href="/comparatifs/aspirateur-eau-poussiere/"><span class="home-decision-index">03</span><span><strong>Eau, gravats et nettoyage</strong>La robustesse, la vidange et la polyvalence passent avant la classe.</span><span class="home-decision-arrow">→</span></a>
          <a class="home-decision-link" href="/comparatifs/aspirateur-chantier-sans-fil/"><span class="home-decision-index">04</span><span><strong>Mobilité</strong>Poids, capacité utile et parc batteries définissent le compromis.</span><span class="home-decision-arrow">→</span></a>
        </div>
        <p class="home-decision-note">Une classe, un filtre HEPA, un chiffre de débit et un système de décolmatage ne répondent pas à la même question.</p>
      </aside>
    </div>
  </div>
</section>

<section class="home-orientation">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Avant le modèle</p>
      <h2>Trois questions qui évitent de comparer les mauvais appareils</h2>
    </div>
    <div class="home-orientation-grid">
      <div class="home-orientation-item"><span class="home-orientation-number">01 / RISQUE</span><h3>Qu’aspirez-vous exactement ?</h3><p>Le matériau et le procédé déterminent d’abord les exigences de collecte et, lorsqu’elle est nécessaire, la classe de l’appareil.</p><a href="/guides/classes-l-m-h/">Comprendre les classes L, M et H →</a></div>
      <div class="home-orientation-item"><span class="home-orientation-number">02 / WORKFLOW</span><h3>L’aspirateur travaille-t-il avec un outil ?</h3><p>Ponceuse, scie et rainureuse déplacent la décision vers le raccordement, le déclenchement et le comportement du filtre pendant la session.</p><a href="/guides/prise-asservie/">Voir la prise asservie →</a></div>
      <div class="home-orientation-item"><span class="home-orientation-number">03 / CONTRAINTE</span><h3>Qu’est-ce qui vous ralentit aujourd’hui ?</h3><p>Transport, vidages, câble, filtre qui se charge ou gros débris : la meilleure référence dépend souvent de cette friction concrète.</p><a href="/guides/comment-choisir-aspirateur-de-chantier/">Passer par le guide de choix →</a></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Par usage</p>
      <h2>Partez du chantier, pas d’un modèle</h2>
      <p>Les mêmes litres et les mêmes watts ne prennent pas le même sens selon ce que vous captez et la manière dont vous travaillez.</p>
    </div>
    <div class="usage-grid">
      <a href="/usages/aspirateur-platre/" class="usage-card"><h3>Plâtre</h3><p>Poussière fine, sessions de ponçage et filtre qui se charge : commencez par le risque et le maintien du débit.</p></a>
      <a href="/usages/aspirateur-ponceuse/" class="usage-card"><h3>Ponceuse</h3><p>Captage à la source, raccord, démarrage avec l’outil et nettoyage du filtre pendant le travail.</p></a>
      <a href="/usages/aspirateur-atelier/" class="usage-card"><h3>Atelier</h3><p>Un aspirateur mobile, un captage dédié ou les deux : organisez les postes avant de dimensionner la cuve.</p></a>
      <a href="/usages/aspirateur-bois-sciure-copeaux/" class="usage-card"><h3>Bois &amp; sciure</h3><p>Distinguez poussières fines, gros copeaux, outils portatifs et machines fixes avant de choisir l’architecture.</p></a>
      <a href="/usages/aspirateur-gravats/" class="usage-card"><h3>Gravats</h3><p>Débris grossiers, robustesse, capacité utile et facilité de vidage priment sur un classement abstrait de puissance.</p></a>
      <a href="/usages/aspirateur-scie/" class="usage-card"><h3>Scie</h3><p>Le raccordement au capot et le volume de matière changent fortement entre scie portative, onglet et machine fixe.</p></a>
      <a href="/usages/aspirateur-bricolage-renovation/" class="usage-card"><h3>Bricolage &amp; rénovation</h3><p>Un profil polyvalent doit couvrir nettoyage, outil électroportatif et déchets variés sans suracheter une certification inutile.</p></a>
    </div>
  </div>
</section>

<section class="section section--white">
  <div class="container">
    <div class="section-head home-reference-intro">
      <p class="eyebrow">Repères documentés</p>
      <h2>Cinq références pour comprendre les principaux compromis</h2>
      <p>Ce tableau n’est pas un podium. Il situe des profils très différents à partir des fiches constructeur vérifiées ; la bonne référence dépend ensuite de votre risque et de votre usage.</p>
    </div>
    <div class="data-table-wrap">
      <table class="data-table home-reference-table">
        <thead><tr><th>Profil</th><th>Référence</th><th>Classe</th><th>Point utile documenté</th><th>Contrepartie</th><th>Analyse</th></tr></thead>
        <tbody>
          <tr><td>Bricolage / atelier</td><td class="home-reference-model">Bosch AdvancedVac 20</td><td><span class="badge badge-gray">Non documentée</span></td><td>20 L, eau/poussière et démarrage synchronisé avec l’outil.</td><td class="home-reference-limit">Aucune classe L/M/H documentée sur la référence analysée.</td><td><a href="/modeles/bosch-advancedvac-20/">Voir la fiche →</a></td></tr>
          <tr><td>Nettoyage + outil</td><td class="home-reference-model">Kärcher WD 6 P S</td><td><span class="badge badge-gray">Non documentée</span></td><td>30 L, prise outil 100–2 100 W, 75 L/s et 280 mbar publiés.</td><td class="home-reference-limit">Nettoyage du filtre manuel par bouton.</td><td><a href="/modeles/karcher-wd6/">Voir la fiche →</a></td></tr>
          <tr><td>Mobile classe L</td><td class="home-reference-model">Bosch GAS 18V-10 L</td><td><span class="badge badge-l">L</span></td><td>4,7 kg sans batterie, 6 L nets et plateforme 18 V / AMPShare.</td><td class="home-reference-limit">Petite capacité et autonomie dépendante du parc batteries.</td><td><a href="/modeles/bosch-gas-18v-10-l/">Voir la fiche →</a></td></tr>
          <tr><td>Classe M / format 35 L</td><td class="home-reference-model">Bosch GAS 35 M AFC</td><td><span class="badge badge-m">M</span></td><td>AFC automatique, 35 L brut / 23 L net, 74 L/s et 254 mbar à la turbine.</td><td class="home-reference-limit">12,4 kg et alimentation filaire.</td><td><a href="/modeles/bosch-gas-35-m-afc/">Voir la fiche →</a></td></tr>
          <tr><td>Classe M / grande capacité</td><td class="home-reference-model">Makita VC4210MX</td><td><span class="badge badge-m">M</span></td><td>InfiniClean automatique, 34 L poussière et prise outil jusqu’à 2 400 W.</td><td class="home-reference-limit">16 kg sans câble : la mobilité devient une vraie contrepartie.</td><td><a href="/modeles/makita-vc4210mx/">Voir la fiche →</a></td></tr>
        </tbody>
      </table>
    </div>
    <p style="margin-top:18px;font-size:.8rem;"><a href="/comparatifs/meilleur-aspirateur-de-chantier/">Comparer les profils plus en détail →</a></p>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Marques</p><h2>Repérer les gammes avant de comparer les références</h2><p>Une marque couvre souvent plusieurs logiques de produit. Le niveau pertinent est la gamme et la référence exacte, surtout pour les classes et le nettoyage du filtre.</p></div>
    <div class="brand-grid">
      <a href="/marques/karcher/" class="brand-card"><div class="brand-name">Kärcher</div><div class="brand-tier">WD / NT</div><div class="brand-desc">WD pour le nettoyage eau/poussière et les travaux courants ; NT pour les usages professionnels et références de sécurité.</div></a>
      <a href="/marques/bosch/" class="brand-card"><div class="brand-name">Bosch</div><div class="brand-tier">AdvancedVac / GAS</div><div class="brand-desc">AdvancedVac côté bricolage ; GAS côté Professional, avec des références L et M à distinguer modèle par modèle.</div></a>
      <a href="/marques/makita/" class="brand-card"><div class="brand-name">Makita</div><div class="brand-tier">VC</div><div class="brand-desc">Des références L et M avec des écarts importants de capacité, poids et mode de nettoyage du filtre.</div></a>
      <a href="/marques/festool/" class="brand-card"><div class="brand-name">Festool</div><div class="brand-tier">CT</div><div class="brand-desc">Écosystème fortement orienté travail avec l’outil ; vérifiez précisément classe, variante et présence éventuelle d’AUTOCLEAN.</div></a>
      <a href="/marques/dewalt/" class="brand-card"><div class="brand-name">DeWalt</div><div class="brand-tier">Chantier / batterie</div><div class="brand-desc">À comparer surtout lorsque l’écosystème d’outils et de batteries influence déjà le chantier.</div></a>
      <a href="/marques/nilfisk/" class="brand-card"><div class="brand-name">Nilfisk</div><div class="brand-tier">Multi / Professional</div><div class="brand-desc">La gamme Multi couvre l’eau/poussière ; les références professionnelles répondent à d’autres niveaux d’exigence.</div></a>
      <a href="/marques/parkside/" class="brand-card"><div class="brand-name">Parkside</div><div class="brand-tier">Bricolage</div><div class="brand-desc">Positionnement budget et disponibilité variable : comparez la référence exacte plutôt qu’une réputation de gamme.</div></a>
      <a href="/marques/mirka/" class="brand-card"><div class="brand-name">Mirka</div><div class="brand-tier">Ponçage</div><div class="brand-desc">Écosystème spécialisé autour du ponçage ; raccords, commande et compatibilités se vérifient au niveau du modèle.</div></a>
    </div>
  </div>
</section>

<section class="home-method">
  <div class="container home-method-inner">
    <div class="home-method-lead"><p class="eyebrow">Notre méthode</p><h2>Ce que nous vérifions avant de rapprocher deux modèles</h2><p>Le site repose sur une recherche documentaire. Nous séparons les faits constructeur, les certifications et notre lecture du compromis ; nous ne transformons pas une fiche technique en faux test terrain.</p><div class="home-method-links"><a href="/methode-de-test/">Méthode &amp; sources →</a><a href="/transparence-affiliation/">Transparence affiliation →</a></div></div>
    <div class="home-method-points">
      <div class="home-method-point"><span>01</span><div><strong>Référence exacte et source primaire</strong><p>Les chiffres et fonctions sont rattachés au modèle vérifié, avec date de contrôle lorsque le contenu a été retravaillé.</p></div></div>
      <div class="home-method-point"><span>02</span><div><strong>Classe de l’appareil ≠ filtre</strong><p>HEPA, décolmatage et puissance ne permettent jamais d’inventer une classe L, M ou H absente de la documentation.</p></div></div>
      <div class="home-method-point"><span>03</span><div><strong>Valeur constructeur ≠ mesure indépendante</strong><p>Débit et dépression restent étiquetés selon leur point de mesure ; ils servent de repères, pas de podium automatique.</p></div></div>
      <div class="home-method-point"><span>04</span><div><strong>Le compromis passe avant le “meilleur”</strong><p>Poids, cuve, câble, batterie, prise outil et nettoyage du filtre sont reliés au workflow réel plutôt qu’additionnés dans un score.</p></div></div>
    </div>
  </div>
</section>

<section class="section section--white">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Guides techniques</p><h2>Comprendre avant de choisir</h2><p>Classes, débit, dépression, filtration et connexion à l’outil : les notions qui changent réellement la lecture d’une fiche produit.</p></div>
    <div class="guide-grid">
      <a href="/guides/classes-l-m-h/" class="guide-card"><span class="ctype ctype-guide">Guide</span><div class="guide-q">Classe L, M ou H : laquelle me faut-il ?</div><div class="guide-hint">Risque, certification et cas d’usage.</div><div class="guide-arrow">Lire le guide →</div></a>
      <a href="/guides/decolmatage-automatique/" class="guide-card"><span class="ctype ctype-guide">Guide</span><div class="guide-q">À quoi sert le décolmatage automatique ?</div><div class="guide-hint">Maintien du filtre et continuité de travail.</div><div class="guide-arrow">Lire le guide →</div></a>
      <a href="/guides/depression-kpa-mbar-air-watt/" class="guide-card"><span class="ctype ctype-guide">Guide</span><div class="guide-q">kPa, mbar, Air Watts : que comparer vraiment ?</div><div class="guide-hint">Unités, points de mesure et limites des chiffres.</div><div class="guide-arrow">Lire le guide →</div></a>
      <a href="/guides/prise-asservie/" class="guide-card"><span class="ctype ctype-guide">Guide</span><div class="guide-q">Qu’est-ce qu’une prise asservie ?</div><div class="guide-hint">Démarrage avec l’outil et compatibilité.</div><div class="guide-arrow">Lire le guide →</div></a>
      <a href="/guides/filtre-hepa-aspirateur/" class="guide-card"><span class="ctype ctype-guide">Guide</span><div class="guide-q">Le filtre HEPA H13/H14 est-il utile sur chantier ?</div><div class="guide-hint">Média filtrant, appareil complet et confusion à éviter.</div><div class="guide-arrow">Lire le guide →</div></a>
      <a href="/guides/sac-ou-sans-sac/" class="guide-card"><span class="ctype ctype-guide">Guide</span><div class="guide-q">Sac ou sans sac sur chantier ?</div><div class="guide-hint">Collecte, vidage, consommables et filtration.</div><div class="guide-arrow">Lire le guide →</div></a>
    </div>
  </div>
</section>

</main>'''


def apply_home() -> None:
    html = HOME.read_text(encoding="utf-8")
    html = re.sub(r"<title>.*?</title>", "<title>Aspirateurs de chantier : comparatifs documentés et guides de choix</title>", html, count=1, flags=re.S)
    html = re.sub(
        r'<meta name="description" content="[^"]*">',
        '<meta name="description" content="Choisir un aspirateur de chantier selon la poussière, l’outil et le chantier : comparatifs documentés, fiches modèles vérifiées et guides classes L/M/H.">',
        html,
        count=1,
    )
    html, count = re.subn(r"<main>.*?</main>", HOME_MAIN, html, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError("homepage: impossible de remplacer <main>")
    html = html.replace(
        "Base de données spécialisée sur les aspirateurs de chantier. Comparatifs indépendants, fiches techniques et guides d'achat.",
        "Base spécialisée sur les aspirateurs de chantier : comparatifs documentés, fiches modèles vérifiées et guides de choix.",
    )
    html = html.replace('>Méthode de test</a>', '>Méthode &amp; sources</a>')
    HOME.write_text(html, encoding="utf-8")


def fix_comparison_labels() -> int:
    changed = 0
    for page in sorted((ROOT / "comparatifs").glob("*/index.html")):
        if page.parent.name == "comparatifs":
            continue
        text = page.read_text(encoding="utf-8")
        updated = text.replace('<span class="ctype ctype-comp">Comp</span>', '<span class="ctype ctype-comp">Comparatif</span>')
        if updated != text:
            page.write_text(updated, encoding="utf-8")
            changed += 1
    return changed


def main() -> None:
    apply_home()
    comp = fix_comparison_labels()
    print(f"Homepage rebuilt; comparison labels corrected on {comp} page(s).")


if __name__ == "__main__":
    main()
