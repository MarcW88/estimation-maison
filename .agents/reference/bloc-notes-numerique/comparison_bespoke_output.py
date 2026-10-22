"""Per-URL editorial overrides for comparison pages.

This module is deliberately small. `comparison_content.py` contains a legacy
renderer for comparison pages that have not yet been reviewed with the new
workflow. Once a page is produced or deeply rewritten through
`comparison-content-workflow`, its final article body belongs here so CI cannot
re-impose the legacy scoring/template structure.

Do not add a page-type template to this file. Each override must be specific to
one URL and come from that page's brief/evidence/recommendation logic.
"""

BESPOKE_COMPARISON_META: dict[str, dict[str, str]] = {
    "meilleur-bloc-notes-numerique": {
        "title": "Meilleur bloc-notes numérique 2026 : lequel choisir ?",
        "h1": "Meilleur bloc-notes numérique 2026 : lequel choisir selon votre usage ?",
        "description": "Comparatif 2026 des meilleurs bloc-notes numériques E Ink : reMarkable, Supernote, BOOX, Kindle et Kobo, avec le meilleur choix selon votre usage.",
        "lead": "Notre sélection des bloc-notes numériques E Ink à stylet, avec un choix par défaut et les alternatives à privilégier selon votre manière de travailler.",
        "status_label": "Vérifié le 9 septembre 2026",
    }
}

BESPOKE_COMPARISON_CONTENT: dict[str, str] = {
    "meilleur-bloc-notes-numerique": r'''
<p class="article-answer"><strong>Pour remplacer un carnet papier sans transformer l'appareil en tablette généraliste, notre choix par défaut est le reMarkable Paper Pure.</strong> Il n'est toutefois pas le meilleur dans tous les cas : Supernote Manta organise mieux les notes manuscrites, BOOX Note Air5 C est beaucoup plus ouvert grâce à Android, Kindle Scribe reste plus logique si vous lisez autant que vous écrivez, et les Paper Pro deviennent plus pertinents lorsque la couleur, le grand format ou la mobilité passent au premier plan.</p>

<p>Dans ce comparatif, « bloc-notes numérique » désigne une <strong>tablette E Ink avec stylet</strong>. Nous ne comparons pas les cahiers effaçables à scanner, les smartpens ni les tablettes LCD/OLED classiques. Ce périmètre est volontaire : l'objectif est de choisir un appareil pensé d'abord pour écrire, annoter et retrouver ses notes.</p>

<h2 id="selection">Notre sélection 2026 en une minute</h2>
<p>Plutôt qu'un podium où quelques dixièmes séparent artificiellement des appareils très différents, voici la décision que nous retenons après vérification des gammes actuelles et confrontation avec des tests indépendants.</p>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Si votre priorité est…</th><th>Notre choix</th><th>Pourquoi</th><th>La contrepartie</th></tr></thead><tbody>
<tr><td>Remplacer un carnet papier</td><td><a href="/marques/remarkable/">reMarkable Paper Pure</a></td><td>Écriture focalisée, interface volontairement simple, format 10,3 pouces, Marker inclus.</td><td>Pas d'éclairage frontal, pas de couleur, écosystème fermé.</td></tr>
<tr><td>Organiser beaucoup de notes manuscrites</td><td><a href="/marques/supernote/">Supernote Manta</a></td><td>Navigation et organisation avancées, approche centrée sur les notes, logiciel sans abonnement.</td><td>Pas d'éclairage frontal ni de couleur.</td></tr>
<tr><td>Utiliser des apps, plusieurs clouds et la couleur</td><td><a href="/marques/boox/boox-note-air/">BOOX Note Air5 C</a></td><td>Android 15, Google Play, écran couleur 10,3 pouces, clavier optionnel.</td><td>Plus de réglages et une expérience moins minimaliste.</td></tr>
<tr><td>Lire des livres et écrire sur le même appareil</td><td><a href="/marques/kindle-scribe/">Kindle Scribe 3e génération</a></td><td>Grand écran E Ink, éclairage frontal et intégration Kindle très cohérente.</td><td>Outils de notes moins profonds que chez Supernote ou BOOX.</td></tr>
<tr><td>Travailler en couleur sur un grand écran</td><td><a href="/marques/remarkable/remarkable-paper-pro/">reMarkable Paper Pro</a></td><td>Écran couleur 11,8 pouces, éclairage frontal, environnement reMarkable focalisé.</td><td>Prix élevé et format moins mobile.</td></tr>
<tr><td>Prendre des notes partout</td><td><a href="/marques/remarkable/">reMarkable Paper Pro Move</a></td><td>Format 7,3 pouces, 230 g, couleur et éclairage frontal.</td><td>Trop compact pour beaucoup de PDF et de pages denses.</td></tr>
<tr><td>Rester dans l'écosystème Kobo</td><td><a href="/marques/kobo-elipsa/">Kobo Elipsa 2E</a></td><td>Lecture Kobo, annotation, notebooks, ComfortLight PRO et intégrations cloud.</td><td>Moins différenciant comme pur outil de notes face aux modèles plus récents.</td></tr>
</tbody></table></div>

<h2 id="paper-pure">Pourquoi le reMarkable Paper Pure est notre choix par défaut</h2>
<p>Le Paper Pure n'est pas le modèle le plus riche de cette sélection, et c'est précisément ce qui le rend cohérent avec la requête « bloc-notes numérique ». Son écran monochrome de 10,3 pouces, son Marker inclus et son interface sans applications généralistes en font un outil qui se comporte d'abord comme un carnet de travail. reMarkable permet de classer les notes avec dossiers et tags, de rechercher dans l'écriture manuscrite et de travailler avec des documents importés depuis des services comme Google Drive, OneDrive ou Dropbox.</p>

<p>Les tests indépendants consultés vont dans le même sens sans en faire un appareil parfait. WIRED relève une meilleure réactivité et un meilleur contraste que l'ancienne génération, tandis que TechCrunch insiste sur l'efficacité du positionnement sans distractions et sur les progrès de la recherche et du partage des notes. En revanche, TechCrunch note aussi que la lecture de PDF n'est pas toujours idéale et que l'appareil n'a pas vocation à remplacer une liseuse complète.</p>

<p>Deux limites doivent donc être considérées avant achat. D'abord, <strong>il n'y a pas d'éclairage frontal</strong> : si vous écrivez souvent dans un environnement sombre, ce choix devient nettement moins évident. Ensuite, vous n'installez pas les applications de votre choix comme sur BOOX. Si votre workflow dépend de Notion, OneNote, Kindle, Kobo ou d'applications métier directement sur l'appareil, passez plutôt à la section suivante.</p>

<h2 id="autres-choix">Quand il faut choisir autre chose</h2>

<h3>Supernote Manta si votre problème est l'organisation, pas seulement l'écriture</h3>
<p>Supernote pousse plus loin la logique du cahier structuré. Le Manta vise les utilisateurs qui accumulent des carnets, relient des idées et ont besoin de retrouver rapidement une information dans un ensemble de notes. Le logiciel, les fonctions de navigation et l'approche sans abonnement en font un choix particulièrement solide pour un usage manuscrit intensif. eWritable le classe d'ailleurs parmi ses meilleurs appareils de prise de notes et souligne la qualité du logiciel dédié.</p>
<p>Ce choix demande d'accepter deux concessions simples : l'écran reste monochrome et il n'y a pas d'éclairage frontal. Pour une personne qui écrit surtout en journée et valorise davantage la structure de ses notes que la lecture d'ebooks, ces concessions peuvent être secondaires.</p>

<h3>BOOX Note Air5 C si vos notes doivent vivre au milieu de vos applications</h3>
<p>Le Note Air5 C est le choix le plus éloigné du carnet fermé. Il fonctionne sous Android 15 avec Google Play, propose un écran couleur Kaleido 3 de 10,3 pouces, un stylet et un clavier optionnel. C'est le modèle à considérer lorsque vos notes doivent cohabiter avec plusieurs applications, clouds, services de lecture ou outils de travail sans passer systématiquement par un ordinateur.</p>
<p>Cette ouverture a un prix éditorial et pratique : BOOX offre beaucoup plus de réglages, et toutes les applications Android ne sont pas optimisées pour l'E Ink. Les tests d'Android Central et de TechRadar le décrivent comme un appareil très polyvalent, tout en relevant les compromis propres à la couleur E Ink et à une interface plus dense qu'un reMarkable ou un Supernote.</p>

<h3>Kindle Scribe si la lecture compte autant que la prise de notes</h3>
<p>Le Kindle Scribe 3e génération devient plus logique dès que votre bibliothèque Kindle fait partie du problème à résoudre. Son grand écran monochrome, son éclairage frontal et son Premium Pen permettent de réunir lecture, annotation et carnets sur un même appareil. Le test TechRadar de la génération actuelle apprécie particulièrement l'écran et les progrès de performance.</p>
<p>Le Scribe reste cependant un Kindle enrichi d'outils d'écriture plutôt qu'un système de knowledge management manuscrit. Si votre priorité est de construire un réseau de notes ou d'utiliser des applications tierces, Supernote et BOOX restent plus adaptés.</p>

<h3>Paper Pro si la couleur et la surface de travail justifient le surcoût</h3>
<p>Le reMarkable Paper Pro reprend la logique focalisée de la marque avec un écran couleur de 11,8 pouces et un éclairage frontal. Sa grande surface devient utile pour des documents denses, des schémas et des annotations où la couleur sert réellement à hiérarchiser l'information.</p>
<p>Il n'est pas notre choix général parce que ces avantages se paient en prix, en poids et en encombrement. Si la couleur ne change pas votre manière de travailler, le Paper Pure reste plus simple à justifier.</p>

<h3>Paper Pro Move si votre carnet doit réellement tenir dans vos déplacements</h3>
<p>Le Paper Pro Move change davantage le format que la philosophie. Son écran couleur de 7,3 pouces, son poids de 230 g et son éclairage frontal en font un carnet numérique beaucoup plus facile à transporter. Pour des réunions, des notes rapides ou un appareil que l'on sort debout et en déplacement, ce compromis peut être excellent.</p>
<p>En revanche, sa compacité devient une limite dès qu'il faut lire des PDF complexes ou retrouver le confort d'une page proche du format A5. Pour ce type de documents, consultez aussi notre guide sur la <a href="/guides/taille-ecran-bloc-notes-numerique/">taille d'écran</a>.</p>

<h3>Kobo Elipsa 2E si vous vivez déjà dans la bibliothèque Kobo</h3>
<p>La Kobo Elipsa 2E reste une liseuse grand format cohérente avec la prise de notes : écran 10,3 pouces, ComfortLight PRO, annotation d'ebooks et de PDF, notebooks, Dropbox et Google Drive. Elle a donc du sens si vous cherchez d'abord une expérience de lecture Kobo capable de prendre des notes.</p>
<p>Pour un achat centré uniquement sur l'écriture et l'organisation, nous la plaçons derrière les spécialistes plus récents. Son avantage principal n'est pas d'avoir le système de notes le plus profond, mais de réunir correctement l'univers Kobo et l'écriture au stylet.</p>

<h2 id="reconsideres">Les modèles actuels que nous avons reconsidérés</h2>
<p>Deux appareils importants ne disparaissent pas du marché simplement parce qu'ils ne figurent pas comme choix principal dans le tableau.</p>

<p><strong>BOOX Go 10.3 Gen II et Go 10.3 Gen II Lumi.</strong> Les deux modèles utilisent Android 15 et un écran monochrome 300 ppp ; la variante Lumi ajoute un éclairage frontal. Ils sont plus légers que le Note Air5 C et constituent d'excellents candidats pour quelqu'un qui veut Android sans couleur. Nous ne les retenons pas comme choix « ouverture et polyvalence » principal parce que le Note Air5 C couvre davantage de scénarios avec couleur, éclairage et clavier optionnel. Les tests indépendants du Go Gen II sont par ailleurs moins unanimes sur la prise de notes : 9to5Google apprécie fortement l'ensemble, tandis que Tom's Guide juge l'écriture moins convaincante que la lecture.</p>

<p><strong>Kindle Scribe Colorsoft.</strong> La couleur apporte quelque chose aux livres illustrés, surlignages et contenus visuels, mais elle s'accompagne d'un tarif plus élevé et des compromis habituels de Kaleido 3. Pour un usage général lecture + notes, nous préférons conserver le Scribe monochrome comme recommandation par défaut. Si la couleur est votre critère principal, consultez plutôt le <a href="/comparatifs/bloc-notes-numerique-couleur/">comparatif des bloc-notes numériques couleur</a>.</p>

<h2 id="criteres">Les critères qui font réellement basculer le choix</h2>
<p><strong>Éclairage frontal :</strong> si vous écrivez régulièrement le soir ou dans les transports, éliminer Paper Pure et Manta peut être plus utile que comparer leurs fonctions une par une.</p>
<p><strong>Applications tierces :</strong> si une application doit fonctionner directement sur l'appareil, BOOX est dans une catégorie à part. Si vous recherchez au contraire moins de distractions, cette ouverture peut devenir un défaut.</p>
<p><strong>Organisation des notes :</strong> Supernote est à considérer en priorité lorsque les liens, la navigation et la structuration des carnets sont au cœur du workflow. reMarkable reste plus simple, ce qui peut être préférable pour une prise de notes linéaire.</p>
<p><strong>Lecture :</strong> Kindle Scribe et Kobo Elipsa 2E deviennent plus rationnels lorsque vous achetez aussi un grand écran pour lire des ebooks. Pour un appareil principalement destiné aux notes, cet avantage pèse moins.</p>
<p><strong>Couleur et taille :</strong> la couleur vaut surtout pour le code visuel, les documents et les schémas. Elle ne rend pas automatiquement l'écriture meilleure. De même, un écran 11,8 pouces aide sur les documents denses mais pénalise la mobilité. Notre guide <a href="/guides/bloc-notes-numerique-couleur-ou-noir-et-blanc/">couleur ou noir et blanc</a> détaille ce compromis.</p>
<p><strong>Circulation des fichiers :</strong> vérifiez enfin comment vos notes entrent et sortent de l'appareil. Le meilleur écran n'est pas très utile si votre workflow oblige ensuite à reconstruire les documents ailleurs. Le guide sur <a href="/guides/ecosysteme-ouvert-ou-ferme/">les écosystèmes ouverts et fermés</a> aide à vérifier ce point avant l'achat.</p>

<h2 id="methode">Ce que cette sélection ne prétend pas mesurer</h2>
<p>Cette page repose sur une analyse documentaire menée à partir des gammes fabricants et de tests indépendants récents. Nous n'avons pas réalisé de test physique propriétaire de ces sept appareils dans les mêmes conditions. Nous ne présentons donc pas de mesures maison de latence, d'autonomie ou de sensation du stylet.</p>
<p>Lorsqu'une caractéristique est publiée par un fabricant — taille, version Android, présence d'un éclairage, stockage — nous la traitons comme une spécification. Les jugements comme « plus simple », « mieux organisé » ou « plus polyvalent » sont des conclusions éditoriales fondées sur l'ensemble des fonctions et sur la confrontation avec des tests indépendants. Les prix et bundles peuvent évoluer ; ils doivent être revérifiés au moment de l'achat.</p>

<h2 id="sources">Sources consultées</h2>
<ul class="source-list">
<li><a href="https://remarkable.com/fr-FR/shop/compare" rel="noopener noreferrer">reMarkable — comparaison de la gamme actuelle</a></li>
<li><a href="https://remarkable.com/products/remarkable-paper/pro/details/compare" rel="noopener noreferrer">reMarkable — Paper Pro</a></li>
<li><a href="https://remarkable.com/products/remarkable-paper/pro-move" rel="noopener noreferrer">reMarkable — Paper Pro Move</a></li>
<li><a href="https://supernote.com/pages/supernote-manta" rel="noopener noreferrer">Supernote — Manta</a></li>
<li><a href="https://shop.boox.com/products/noteair5c" rel="noopener noreferrer">BOOX — Note Air5 C</a></li>
<li><a href="https://shop.boox.com/products/go103gen2" rel="noopener noreferrer">BOOX — Go 10.3 Gen II / Lumi</a></li>
<li><a href="https://digprjsurvey.amazon.com/csad/help/node/GK33S847NN4V6Y83" rel="noopener noreferrer">Amazon — générations Kindle Scribe</a></li>
<li><a href="https://ereader.kobo.com/fr-fr/products/kobo-elipsa-2e" rel="noopener noreferrer">Kobo — Elipsa 2E</a></li>
<li><a href="https://www.wired.com/gallery/best-smart-notebooks-and-smart-pens/" rel="noopener noreferrer">WIRED — Best Digital Notebooks, août 2026</a></li>
<li><a href="https://www.wired.com/review/remarkable-paper-pure/" rel="noopener noreferrer">WIRED — reMarkable Paper Pure, mai 2026</a></li>
<li><a href="https://techcrunch.com/2026/07/17/remarkables-new-paper-pure-is-good-thats-why-i-wrote-this-review-on-it/" rel="noopener noreferrer">TechCrunch — reMarkable Paper Pure, juillet 2026</a></li>
<li><a href="https://ewritable.net/brands/ratta-supernote/tablets/supernote-a5-x2/" rel="noopener noreferrer">eWritable — Supernote Manta, mise à jour avril 2026</a></li>
<li><a href="https://www.androidcentral.com/tablets/onyx-boox-note-air-5-c-review" rel="noopener noreferrer">Android Central — BOOX Note Air5 C, 2026</a></li>
<li><a href="https://www.techradar.com/tablets/ereaders/amazon-kindle-scribe-2025-with-frontlight-review" rel="noopener noreferrer">TechRadar — Kindle Scribe 3e génération, juillet 2026</a></li>
<li><a href="https://www.tomsguide.com/computing/e-readers/boox-go-10.3-gen-ii-review" rel="noopener noreferrer">Tom's Guide — BOOX Go 10.3 Gen II, juillet 2026</a></li>
<li><a href="https://9to5google.com/2026/07/28/boox-go-10-3-gen-ii-review/" rel="noopener noreferrer">9to5Google — BOOX Go 10.3 Gen II, juillet 2026</a></li>
</ul>
'''
}


def bespoke_body(slug: str, fallback: str) -> str:
    """Return bespoke editorial content when a reviewed override exists."""
    body = BESPOKE_COMPARISON_CONTENT.get(slug)
    if body is None:
        return fallback
    body = body.strip()
    if not body:
        raise ValueError(f"Empty bespoke comparison content: {slug}")
    return body


def bespoke_meta(slug: str, fallback: dict[str, str]) -> dict[str, str]:
    """Merge per-URL editorial metadata over technical fallback metadata."""
    return {**fallback, **BESPOKE_COMPARISON_META.get(slug, {})}
