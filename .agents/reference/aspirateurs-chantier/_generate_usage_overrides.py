#!/usr/bin/env python3
"""Replace placeholder usage pages with intent-led content.

Usage pages own the non-brand job-to-be-done. Brand pages explain an ecosystem;
model pages explain a reference; comparison pages rank alternatives.
"""
from pathlib import Path
from html import escape
import re

BASE = Path(__file__).resolve().parent
UPDATED = '09/09/2026'

PAGES = {
'aspirateur-platre': {
 'title':'Quel aspirateur choisir pour le plâtre ?',
 'desc':'Poussière fine, colmatage et captage : choisir l’aspiration selon le travail réellement réalisé sur plâtre et supports minéraux.',
 'answer':'Pour le plâtre, le premier problème est la poussière fine et colmatante. Choisissez la classe de l’appareil à partir du risque réel et du support travaillé, puis regardez le maintien du débit, le décolmatage et le captage à la source. Une puissance moteur élevée ne remplace ni une classe de sécurité ni un bon raccordement à l’outil.',
 'sections':[
  ('risque','Commencer par la poussière réellement produite','Poncer un enduit, découper une plaque et nettoyer des morceaux au sol ne sollicitent pas l’aspirateur de la même manière. Le nettoyage de déchets déposés demande surtout une machine robuste ; le ponçage ou la découpe génèrent une poussière beaucoup plus fine qui doit être captée au plus près de l’outil. Si le support ou le chantier peut contenir d’autres poussières minérales, l’évaluation du risque doit intégrer ces matériaux au lieu de raisonner sur le seul mot « plâtre ».','/guides/classes-l-m-h/','classes L/M/H'),
  ('decolmatage','Le décolmatage devient important quand le filtre se charge vite','Une poussière très fine réduit progressivement le passage de l’air. Un système automatique de type AFC, Tact, AUTOCLEAN ou InfiniClean peut limiter les interruptions, mais ces technologies ne sont pas identiques et ne disent rien, à elles seules, sur la classe de poussière. Pour un usage occasionnel, un nettoyage manuel peut suffire ; pour une ponceuse utilisée longtemps, le maintien du débit devient beaucoup plus important.','/guides/decolmatage-automatique/','décolmatage automatique'),
  ('outil','Avec une ponceuse, penser système complet','Le flexible, le diamètre du raccord, la prise asservie ou la télécommande et l’étanchéité du raccord comptent autant que la cuve. L’objectif est de capter la poussière avant qu’elle se disperse. Un aspirateur puissant mais mal raccordé peut être moins efficace qu’un ensemble mieux dimensionné.','/usages/aspirateur-ponceuse/','aspirateur pour ponceuse'),
  ('choix','Comment arbitrer entre les familles de machines','Pour une rénovation domestique sans poussière dangereuse identifiée, un appareil eau/poussière peut suffire au nettoyage final. Dès que le travail génère durablement une poussière fine, comparez les machines certifiées pour le niveau de risque requis, leur décolmatage et leur comportement avec l’outil. La page comparatif classe M ne doit être utilisée que si M est réellement la classe adaptée.','/comparatifs/aspirateur-classe-m/','comparatif classe M')],
 'sources':[('INRS — prévention des poussières','https://www.inrs.fr/risques/poussieres/ce-qu-il-faut-retenir.html'),('INRS — silice cristalline et captage à la source','https://www.inrs.fr/risques/silice-cristalline/ce-qu-il-faut-retenir')]
},
'aspirateur-ponceuse': {
 'title':'Quel aspirateur choisir pour une ponceuse ?',
 'desc':'Captage à la source, raccord, décolmatage, classe de poussière et démarrage automatique : les critères qui changent vraiment le choix.',
 'answer':'Avec une ponceuse, choisissez d’abord en fonction de la poussière produite et de la qualité du captage à la source. Ensuite viennent le raccord, le maintien du débit, le décolmatage et le démarrage automatique. Festool et Mirka peuvent simplifier le workflow dans leur propre écosystème, mais ils ne remplacent pas l’évaluation du risque.',
 'sections':[
  ('captage','Le captage à la source passe avant la taille de la cuve','Une ponceuse génère la poussière en continu. Le flexible et l’orifice de la machine doivent donc former un circuit stable : raccord qui ne se décroche pas, diamètre cohérent et flexible assez souple pour ne pas gêner le geste. Pour le bois, l’INRS rappelle que la ventilation générale ne suffit pas et que les poussières doivent être captées au plus près de leur source.','/accessoires/adaptateur-outil-electroportatif/','adaptateurs outil'),
  ('classe','La classe dépend du matériau, pas de la ponceuse','Poncer du bois, un enduit, une peinture ou un support minéral ne produit pas le même risque. Ne choisissez pas une classe L/M/H parce que le fabricant de la ponceuse recommande une marque d’aspirateur. Identifiez la poussière, puis vérifiez la certification de la référence exacte. Un filtre HEPA n’est pas une classe d’aspirateur.','/guides/classes-l-m-h/','guide des classes L/M/H'),
  ('debit','Débit maintenu et décolmatage : le vrai enjeu sur une longue session','Le débit maximal à vide est moins utile que la capacité à continuer d’aspirer quand le filtre se charge. Sur des poussières colmatantes, le décolmatage automatique réduit les pauses. Les chiffres annoncés par deux fabricants ne sont comparables que si le point de mesure est le même.','/guides/debit-air-aspirateur/','débit d’air'),
  ('declenchement','Prise asservie, Bluetooth ou télécommande','Une prise asservie démarre l’aspirateur avec un outil filaire. Sur batterie, certaines marques utilisent Bluetooth ou télécommande. Ce confort n’améliore pas la filtration, mais il évite de poncer quelques secondes sans aspiration à chaque reprise.','/guides/prise-asservie/','prise asservie'),
  ('ecosystemes','Festool et Mirka : utiles comme écosystèmes, pas comme réponse universelle','Festool mise sur CLEANTEC, Bluetooth et Systainer ; Mirka construit son système autour de DEROS/DEOS, DEXOS et de ses abrasifs. Ces intégrations peuvent réduire les frictions si vous possédez déjà les outils. Pour comparer objectivement les critères indépendamment de la marque, cette page reste l’URL principale ; les hubs Festool et Mirka expliquent seulement ce que leur écosystème ajoute.','/marques/mirka/','écosystème Mirka')],
 'sources':[('INRS — ventilation et aspiration des poussières de bois','https://www.inrs.fr/metiers/metiers-du-bois/transformation-du-bois/poussiere/ventilation-aspiration.html'),('INRS — silice cristalline','https://www.inrs.fr/risques/silice-cristalline/ce-qu-il-faut-retenir')]
},
'aspirateur-atelier': {
 'title':'Quel aspirateur choisir pour un atelier ?',
 'desc':'Nettoyage, machines raccordées, poussières fines, liquides et mobilité : construire un choix d’atelier sans surdimensionner.',
 'answer':'Dans un atelier, séparez deux besoins : nettoyer le sol et aspirer directement sur les machines. Un grand eau/poussière est excellent pour le premier ; le second demande surtout un bon captage, le raccord adapté, la classe nécessaire et un filtre qui ne se colmate pas trop vite.',
 'sections':[
  ('deux-besoins','Nettoyage général et extraction machine ne sont pas le même travail','Une cuve de 25 à 35 L est confortable pour le nettoyage, mais sa taille ne garantit pas une bonne extraction sur une ponceuse ou une scie. Si l’aspirateur reste raccordé à une machine, regardez d’abord flexible, prise asservie et maintien du débit.','/guides/capacite-cuve/','capacité de cuve'),
  ('poussieres','Adapter la classe aux matériaux travaillés','Bois, enduits, béton, métal et poussières ordinaires n’ont pas le même profil de risque. Une fiche modèle doit documenter explicitement sa classe ; un modèle grand public non classé peut rester pertinent pour les liquides ou déchets ordinaires mais ne doit pas être promu comme aspirateur de sécurité.','/guides/classes-l-m-h/','classes L/M/H'),
  ('mobilite','La meilleure cuve est celle que vous acceptez de déplacer','Au-delà du volume, comparez encombrement, roulettes, rangement du flexible et fréquence de vidage. Un gros 42 L convient mieux à un poste quasi fixe qu’à des déplacements entre étages.','/modeles/makita-vc4210mx/','Makita VC4210MX'),
  ('workflow','Choisir l’écosystème seulement s’il réduit réellement les frictions','Makpac, L-BOXX, Systainer, AIRLOCK ou Click & Clean ont de la valeur si vos outils les utilisent déjà. Sinon, comparez le coût du système complet et la disponibilité des consommables plutôt que le logo.','/comparatifs/aspirateur-professionnel/','comparatif professionnel')],
 'sources':[('INRS — prévenir les risques liés aux poussières','https://www.inrs.fr/risques/poussieres/ce-qu-il-faut-retenir.html')]
},
'aspirateur-bois-sciure-copeaux': {
 'title':'Aspirateur pour bois, sciure et copeaux : que choisir ?',
 'desc':'Captage à la source, poussières de bois, copeaux, débit et filtration : distinguer aspiration mobile et réseau d’atelier.',
 'answer':'Pour le bois, ne mettez pas sciure fine et gros copeaux dans la même catégorie. Les copeaux demandent surtout du débit et un conduit adapté ; les poussières fines imposent une démarche de prévention, du captage à la source et une filtration choisie selon le risque.',
 'sections':[
  ('captage','Les poussières de bois doivent être captées au plus près de la machine','L’INRS considère les travaux exposant aux poussières de bois comme des procédés cancérogènes et donne la priorité au captage à la source. Un aspirateur mobile peut convenir à une ponceuse ou une scie portative ; les grosses machines fixes peuvent demander un réseau d’aspiration conçu pour leur débit.','/usages/aspirateur-scie/','aspiration sur scie'),
  ('copeaux','Gros copeaux : débit, diamètre et volume','Pour rabotage, sciage ou déchets volumineux, un flexible trop étroit se bouche facilement. Le diamètre de raccord et le débit réel peuvent compter davantage que la dépression maximale. Une cuve plus grande réduit les vidages, sans améliorer la filtration.','/guides/debit-air-aspirateur/','débit d’air'),
  ('classe','Poussière fine : ne pas déduire la classe du filtre','La classe de l’aspirateur doit être documentée par le fabricant et choisie selon l’évaluation du risque. Ne transformez pas la présence d’un HEPA en classe M ou H.','/guides/classes-l-m-h/','classes L/M/H'),
  ('nettoyage','Éviter de remettre les poussières en suspension','Pour l’entretien d’un atelier bois, l’INRS recommande le nettoyage par aspiration plutôt que balai ou soufflette. Le vidage et le changement de filtre font aussi partie de l’exposition à considérer.','/guides/entretien-aspirateur-chantier/','entretien')],
 'sources':[('INRS — poussières de bois','https://www.inrs.fr/risques/poussieres-bois/ce-qu-il-faut-retenir'),('INRS — aspiration des poussières de bois','https://www.inrs.fr/metiers/metiers-du-bois/transformation-du-bois/poussiere/ventilation-aspiration.html')]
},
'aspirateur-gravats': {
 'title':'Aspirateur pour gravats : lequel choisir ?',
 'desc':'Débris lourds, poussières minérales et eau résiduelle : distinguer le nettoyage des gravats du captage des poussières fines.',
 'answer':'Pour des gravats déjà déposés, privilégiez robustesse, diamètre du flexible, cuve et aspiration eau/poussière. Mais découper, percer ou meuler des matériaux minéraux génère une autre problématique : la poussière fine doit être captée à la source et peut contenir de la silice. Un gros aspirateur de nettoyage n’est pas automatiquement adapté à ce risque.',
 'sections':[
  ('debris','Gros débris : protéger le flexible et limiter les bouchons','Pour morceaux de plâtre, petits éclats et déchets humides, regardez le diamètre du flexible, la résistance de la cuve et la facilité de vidage. Une cuve de 30 L est confortable, mais un pré-séparateur peut être plus utile qu’un volume encore supérieur dans certains ateliers.','/guides/capacite-cuve/','capacité de cuve'),
  ('poussiere','Découpe et meulage : le sujet devient la poussière minérale','L’INRS recommande de réduire les émissions, de travailler à l’humide lorsque c’est possible et de capter les poussières à la source. Pour la silice cristalline, le raccordement des outils à un système d’aspiration haute dépression fait partie des mesures de prévention.','/guides/classes-l-m-h/','classes L/M/H'),
  ('eau','Eau résiduelle : vérifier la capacité liquide réelle','La capacité brute d’une cuve n’est pas toujours sa capacité utile en liquide. Comparez les valeurs nettes lorsqu’elles sont publiées et vérifiez la procédure de passage eau/poussière du fabricant.','/comparatifs/aspirateur-eau-poussiere/','comparatif eau/poussière'),
  ('modeles','Ne pas confondre WD grand public et NT de sécurité','Un Kärcher WD 6 peut être très pertinent pour nettoyer un chantier, alors qu’un NT M répond à une logique de poussière différente. Les performances de nettoyage ne permettent pas de déduire une certification.','/marques/karcher/','gamme Kärcher')],
 'sources':[('INRS — silice cristalline','https://www.inrs.fr/risques/silice-cristalline/ce-qu-il-faut-retenir'),('INRS — prévention des poussières','https://www.inrs.fr/risques/poussieres/ce-qu-il-faut-retenir.html')]
},
'aspirateur-scie': {
 'title':'Aspirateur pour scie de chantier : comment choisir ?',
 'desc':'Scie circulaire, onglet ou table : raccord, débit, captage à la source, prise asservie et nature des poussières.',
 'answer':'Pour une scie, le meilleur aspirateur est d’abord celui qui se raccorde correctement au carter de captage et maintient assez de débit. Ensuite viennent la prise asservie, la classe nécessaire selon le matériau et le diamètre du flexible. La puissance moteur seule est un mauvais raccourci.',
 'sections':[
  ('raccord','Le carter et le raccord déterminent une grande partie du résultat','Une scie mal carénée laisse échapper de la poussière même avec un aspirateur puissant. Vérifiez le diamètre réel de sortie, la présence éventuelle de deux points de captage et les adaptateurs avant l’achat.','/accessoires/adaptateur-outil-electroportatif/','adaptateurs'),
  ('debit','Les copeaux demandent du débit et un conduit qui ne se bouche pas','Pour le bois, un diamètre trop faible peut limiter le transport des copeaux. Sur une scie portative, un aspirateur haute dépression est souvent plus pratique ; sur une machine fixe très productive, un réseau dédié peut être plus adapté.','/guides/debit-air-aspirateur/','débit d’air'),
  ('demarrage','La prise asservie évite les démarrages oubliés','Avec une scie filaire, l’aspirateur peut démarrer automatiquement avec l’outil. Sur batterie, regardez les systèmes sans fil ou télécommandes. Cette fonction améliore le workflow, pas la classe de filtration.','/guides/prise-asservie/','prise asservie'),
  ('materiau','Bois et matériaux minéraux ne posent pas le même risque','Pour le bois, l’INRS donne priorité au captage à la source. Pour des matériaux contenant de la silice, les opérations de découpe demandent aussi des mesures spécifiques. La classe doit donc suivre le matériau travaillé, pas le type de scie.','/usages/aspirateur-bois-sciure-copeaux/','bois et sciure')],
 'sources':[('INRS — poussières de bois','https://www.inrs.fr/risques/poussieres-bois/ce-qu-il-faut-retenir'),('INRS — silice cristalline','https://www.inrs.fr/risques/silice-cristalline/ce-qu-il-faut-retenir')]
},
'aspirateur-bricolage-renovation': {
 'title':'Aspirateur de chantier pour bricolage et rénovation',
 'desc':'Nettoyage, eau, ponçage, perçage et découpe : choisir une machine en fonction des tâches plutôt qu’un niveau de gamme générique.',
 'answer':'Pour le bricolage, ne partez pas d’une classe L par défaut. Un aspirateur eau/poussière grand public peut être excellent pour nettoyer liquides et débris ordinaires sans être certifié L/M/H. Dès que vous poncez, percez ou découpez des matériaux générant des poussières dangereuses, le choix doit suivre le risque et le captage à la source.',
 'sections':[
  ('taches','Commencez par lister les travaux réels','Nettoyage de garage, aspiration d’eau, gravats, ponçage, perçage et sciage imposent des critères différents. Un seul appareil peut couvrir plusieurs tâches, mais il faut identifier la contrainte la plus exigeante avant de choisir.','/guides/comment-choisir-aspirateur-de-chantier/','guide de choix'),
  ('grand-public','Un WD, AdvancedVac ou Multi peut être pertinent sans être classe L','Les gammes grand public eau/poussière privilégient polyvalence, prix et facilité d’entretien. Ne les dévalorisez pas parce qu’elles ne sont pas certifiées M ; ne les transformez pas non plus en aspirateurs de sécurité sur la base d’un filtre ou d’une forte aspiration.','/comparatifs/aspirateur-eau-poussiere/','eau et poussière'),
  ('poussiere','Les travaux générant de la poussière changent le cahier des charges','Pour ponçage, sciage ou découpe, le captage à la source, la nature du matériau et la classe documentée deviennent prioritaires. Le même chantier peut donc justifier un appareil différent pour le nettoyage final et pour le travail raccordé à l’outil.','/guides/classes-l-m-h/','classes L/M/H'),
  ('budget','Comparer le coût du système complet','Ajoutez sacs, filtres, raccords, batteries éventuelles et disponibilité des consommables. Une machine moins chère peut être le meilleur choix si elle répond vraiment au besoin ; une plateforme professionnelle n’a de valeur que si ses fonctions sont utilisées.','/marques/parkside/','Parkside')],
 'sources':[('INRS — prévention des poussières','https://www.inrs.fr/risques/poussieres/ce-qu-il-faut-retenir.html')]
}
}


def render(slug, d):
    sections = []
    toc = []
    for sid, title, text, url, anchor in d['sections']:
        sections.append(f'<h2 id="{sid}">{escape(title)}</h2><p>{escape(text)}</p><p><a href="{url}">Approfondir : {escape(anchor)}</a></p>')
        toc.append(f'<a href="#{sid}">{escape(title)}</a>')
    sources = ''.join(f'<li><a href="{url}" rel="nofollow noopener">{escape(label)}</a></li>' for label, url in d['sources'])
    return f'''<main>
<div class="container"><nav class="breadcrumb"><a href="/">Accueil</a><span class="sep">/</span> <a href="/usages/">Par usage</a> <span class="sep">/</span> <span>{escape(d['title'])}</span></nav></div>
<section class="page-hero"><div class="container"><span class="ctype ctype-usage">Usage</span><h1 style="margin-top:10px;">{escape(d['title'])}</h1><p class="lead">{escape(d['desc'])}</p><div class="page-meta"><span class="meta-tag">Vérifié : {UPDATED}</span><span class="meta-tag">Recherche documentaire</span></div></div></section>
<div class="container"><div class="content-layout"><article class="content-main">
<div class="answer-box"><p>{escape(d['answer'])}</p></div>
{''.join(sections)}
<h2 id="sources">Sources et méthode</h2><p>Cette page synthétise des recommandations de prévention et les critères techniques utiles au choix. Elle ne remplace pas l’évaluation du risque ni les prescriptions applicables au chantier.</p><ul>{sources}</ul>
</article><aside class="content-sidebar"><div class="sidebar-box"><div class="sidebar-box-head">Sommaire</div><div class="sidebar-box-body"><nav class="toc-list">{''.join(toc)}<a href="#sources">Sources</a></nav></div></div><div class="sidebar-box"><div class="sidebar-box-head">Affiliation</div><div class="sidebar-box-body"><p class="affil-note">Ce site contient des liens affiliés. Nos recommandations restent indépendantes. <a href="/transparence-affiliation/">En savoir plus.</a></p></div></div></aside></div></div>
</main>'''


def main():
    for slug, d in PAGES.items():
        path = BASE / 'usages' / slug / 'index.html'
        html = path.read_text(encoding='utf-8')
        html = re.sub(r'<title>.*?</title>', f'<title>{escape(d["title"])}</title>', html, count=1, flags=re.S)
        html = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{escape(d["desc"], quote=True)}">', html, count=1)
        html = re.sub(r'<main>.*?</main>', render(slug, d), html, count=1, flags=re.S)
        path.write_text('\n'.join(line.rstrip() for line in html.splitlines()) + '\n', encoding='utf-8')
        print(f'✓ usage {slug}')


if __name__ == '__main__':
    main()
