"""Bespoke editorial output for priority comparison rewrites, 9 Sep 2026.

Each entry has its own decision logic and structure. This module intentionally
contains no shared page renderer or page-type template.
"""

META = {
    "bloc-notes-numerique-a4": {
        "title": "Bloc-notes numérique A4 : les meilleurs grands écrans E Ink en 2026",
        "h1": "Bloc-notes numérique A4 : quel grand écran choisir en 2026 ?",
        "description": "Comparatif des bloc-notes numériques proches du format A4 : BOOX Note Max, Tab X C, Fujitsu Quaderno A4 et alternatives plus compactes.",
        "lead": "Pour les PDF, plans et documents A4, la diagonale réelle et la surface utile comptent davantage qu'un score généraliste.",
        "status_label": "Vérifié le 9 septembre 2026",
    },
    "bloc-notes-numerique-sans-abonnement": {
        "title": "Bloc-notes numérique sans abonnement : que choisir en 2026 ?",
        "h1": "Quel bloc-notes numérique choisir sans abonnement ?",
        "description": "Comparatif des bloc-notes numériques utilisables sans paiement mensuel : Supernote, BOOX, Kindle, Kobo et reMarkable avec les limites réelles de chaque écosystème.",
        "lead": "Le bon critère n'est pas seulement l'existence d'un abonnement, mais ce qui continue réellement de fonctionner lorsqu'on ne paie rien chaque mois.",
        "status_label": "Vérifié le 9 septembre 2026",
    },
    "bloc-notes-numerique-pas-cher": {
        "title": "Bloc-notes numérique pas cher : les choix réellement utilisables en 2026",
        "h1": "Quel bloc-notes numérique pas cher choisir en 2026 ?",
        "description": "Comparatif budget 2026 : PocketBook InkPad One, reMarkable Paper Pure et autres options avec stylet, en comparant la configuration réellement utilisable.",
        "lead": "Le prix de la tablette seule est trompeur : nous comparons d'abord ce qu'il faut réellement acheter pour lire, écrire et exporter ses notes.",
        "status_label": "Vérifié le 9 septembre 2026",
    },
    "remarkable-vs-boox": {
        "title": "reMarkable vs BOOX en 2026 : simplicité ou Android ouvert ?",
        "h1": "reMarkable ou BOOX : quelle marque choisir en 2026 ?",
        "description": "Comparaison reMarkable vs BOOX : Paper Pure, Paper Pro, Go 10.3 Gen II, Note Air5 C et grands formats selon vos notes, PDF, applications et cloud.",
        "lead": "Ce duel oppose moins deux tablettes que deux philosophies : reMarkable réduit les possibilités pour protéger le focus, BOOX ouvre l'appareil à Android et aux applications.",
        "status_label": "Vérifié le 9 septembre 2026",
    },
    "remarkable-vs-supernote": {
        "title": "reMarkable vs Supernote en 2026 : quel carnet E Ink choisir ?",
        "h1": "reMarkable ou Supernote : lequel choisir pour prendre des notes ?",
        "description": "Comparatif reMarkable vs Supernote : Paper Pure, Paper Pro, Manta et Nomad selon simplicité, organisation des notes, couleur, éclairage et abonnement.",
        "lead": "Les deux marques privilégient l'écriture et le calme, mais reMarkable mise sur la simplicité tandis que Supernote pousse beaucoup plus loin l'organisation manuscrite.",
        "status_label": "Vérifié le 9 septembre 2026",
    },
    "boox-vs-supernote": {
        "title": "BOOX vs Supernote en 2026 : Android ou carnet spécialisé ?",
        "h1": "BOOX ou Supernote : quelle approche choisir en 2026 ?",
        "description": "Comparatif BOOX vs Supernote : Go 10.3, Note Air5 C, Note Max, Manta et Nomad selon apps Android, notes, PDF, organisation et simplicité.",
        "lead": "BOOX cherche à faire beaucoup de choses sur E Ink ; Supernote cherche surtout à rendre l'écriture et l'organisation manuscrite meilleures.",
        "status_label": "Vérifié le 9 septembre 2026",
    },
}

CONTENT = {
"bloc-notes-numerique-a4": r'''
<p class="article-answer"><strong>Pour travailler régulièrement sur des PDF A4 sans zoomer en permanence, notre choix noir et blanc est le BOOX Note Max.</strong> Son écran E Ink de 13,3 pouces et 300 ppp est réellement dans la catégorie « proche de l'A4 ». Si la couleur et l'éclairage frontal sont prioritaires, le BOOX Tab X C est plus adapté. Le Fujitsu Quaderno A4 Gen.3C mérite aussi d'être considéré pour un workflow très centré sur le PDF, mais sa distribution est beaucoup plus orientée vers le Japon.</p>

<h2 id="a4-signifie">Un écran « A4 » n'est pas simplement un grand 10 pouces</h2>
<p>Une feuille A4 mesure 210 × 297 mm. Sur une tablette E Ink, le terme A4 est souvent utilisé de façon approximative pour désigner un appareil confortable avec de grands documents. La différence est pourtant importante : 10,2 ou 10,3 pouces restent pratiques à transporter, mais demandent plus souvent du zoom ou du recadrage sur des articles scientifiques, contrats, partitions ou plans conçus pour une page A4.</p>
<p>Les appareils 13,3 pouces comme le Note Max, le Tab X C ou le Fujitsu Quaderno A4 offrent une surface beaucoup plus proche du document original. La contrepartie est immédiate : ils pèsent autour de 600 g pour les BOOX et occupent nettement plus de place dans un sac.</p>

<h2 id="choix">Trois choix selon votre façon de travailler</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Besoin</th><th>Choix</th><th>Atout déterminant</th><th>Limite</th></tr></thead><tbody>
<tr><td>PDF A4 en noir et blanc</td><td><a href="/marques/boox/">BOOX Note Max</a></td><td>13,3", 300 ppp, Android 13, stylet inclus</td><td>Pas d'éclairage frontal, environ 615 g</td></tr>
<tr><td>A4 + couleur + usage le soir</td><td><a href="/marques/boox/">BOOX Tab X C</a></td><td>13,3" Kaleido 3, éclairage frontal, apps Android</td><td>Plus cher, environ 625 g, couleur 150 ppp</td></tr>
<tr><td>PDF et annotation avant tout</td><td>Fujitsu Quaderno A4 Gen.3C</td><td>13,3" explicitement décliné en format A4, stylet, interface documentaire</td><td>Écosystème et disponibilité européenne à vérifier avant achat</td></tr>
<tr><td>Compromis plus mobile</td><td><a href="/marques/remarkable/remarkable-paper-pro/">reMarkable Paper Pro</a></td><td>11,8", couleur, éclairage, environnement focalisé</td><td>Moins proche de l'A4 qu'un 13,3"</td></tr>
</tbody></table></div>

<h2 id="note-max">Pourquoi le Note Max est le meilleur point de départ pour les PDF A4</h2>
<p>BOOX présente explicitement le Note Max comme un appareil « A4-sized ». Son écran monochrome Carta 1300 de 13,3 pouces affiche 3200 × 2400 pixels à 300 ppp. Cette densité est un avantage réel pour des textes fins, des tableaux et des documents techniques. Android 13 et Google Play permettent aussi d'utiliser des applications de lecture, de cloud ou de gestion documentaire qui ne sont pas disponibles sur des systèmes plus fermés.</p>
<p>Il faut toutefois accepter l'absence d'éclairage frontal. Pour un bureau bien éclairé, cela peut même rapprocher l'écran de l'apparence d'une feuille. Pour un usage nocturne ou dans un avion sombre, c'est une vraie contrainte et le Tab X C devient plus logique.</p>

<h2 id="tab-x-c">Tab X C : la couleur change le document, pas seulement le marketing</h2>
<p>Le Tab X C garde le même format 13,3 pouces mais ajoute la couleur Kaleido 3 et un éclairage frontal réglable. Les documents contenant des légendes, corrections, diagrammes ou codes couleur deviennent plus faciles à interpréter qu'en niveaux de gris. En revanche, la définition couleur tombe à 150 ppp, contre 300 ppp en noir et blanc, et la facture augmente nettement.</p>
<p>Nous le privilégierions donc seulement si la couleur apporte de l'information au document. Pour du texte juridique, des articles scientifiques monochromes ou des partitions, le Note Max reste plus rationnel.</p>

<h2 id="quaderno">Le Fujitsu Quaderno A4 est le spécialiste à ne pas oublier</h2>
<p>Le Quaderno A4 Gen.3C utilise lui aussi un écran flexible de 13,3 pouces, avec 4096 couleurs et un stylet à 4096 niveaux de pression. Sa documentation reste très centrée sur le PDF, ce qui peut être un avantage pour un utilisateur qui ne veut ni Android ni une multitude d'applications.</p>
<p>Nous ne le plaçons pas comme recommandation principale pour la France : la gamme est avant tout commercialisée et documentée par Fujitsu au Japon, et il faut vérifier le canal d'achat, la garantie et les applications nécessaires avant import. C'est un excellent exemple de produit techniquement pertinent mais commercialement moins simple.</p>

<h2 id="10-pouces">Quand un 10,3 pouces reste préférable</h2>
<p>Un écran 13,3 pouces n'est pas automatiquement meilleur. Si vos PDF sont occasionnels et que vous portez l'appareil tous les jours, un <a href="/marques/boox/">BOOX Go 10.3</a>, un <a href="/marques/supernote/">Supernote Manta</a> ou un Kindle Scribe peuvent être plus agréables au quotidien. Dans ce cas, vous acceptez davantage de zoom en échange d'un appareil plus facile à tenir.</p>
<p>Le guide sur la <a href="/guides/taille-ecran-bloc-notes-numerique/">taille d'écran</a> explique ce compromis. Cette page, elle, privilégie volontairement les appareils qui réduisent le plus le besoin de zoom sur de vrais documents A4.</p>

<h2 id="sources">Sources consultées</h2><ul class="source-list">
<li><a href="https://shop.boox.com/products/notemax" rel="noopener noreferrer">BOOX — Note Max, spécifications officielles</a></li>
<li><a href="https://shop.boox.com/products/tabxc" rel="noopener noreferrer">BOOX — Tab X C, spécifications officielles</a></li>
<li><a href="https://sdmgr.fmworld.net/digital-paper/product.html" rel="noopener noreferrer">Fujitsu — Quaderno A4 Gen.3C</a></li>
<li><a href="https://remarkable.com/products/remarkable-paper/pro" rel="noopener noreferrer">reMarkable — Paper Pro</a></li>
</ul>
''',

"bloc-notes-numerique-sans-abonnement": r'''
<p class="article-answer"><strong>Si votre priorité est de garder un système de notes complet sans paiement mensuel, Supernote est le choix le plus simple à expliquer en 2026.</strong> La marque annonce explicitement des mises à jour logicielles gratuites et « No subscription ». BOOX est également très solide : ses appareils fonctionnent sans abonnement BOOX et incluent 10 Go de stockage Onyx gratuit, mais les applications Android que vous installez peuvent évidemment avoir leurs propres abonnements.</p>

<h2 id="definition">« Sans abonnement » peut vouloir dire trois choses différentes</h2>
<p>Il faut distinguer l'appareil utilisable sans paiement récurrent, le cloud gratuit et les services premium facultatifs. Un bloc-notes peut continuer à écrire parfaitement sans abonnement tout en réservant la recherche avancée, le stockage illimité ou l'édition depuis un ordinateur à une formule payante.</p>
<p>C'est précisément le cas de reMarkable : Connect est facultatif, mais il donne accès notamment à la recherche dans l'écriture manuscrite, au stockage et à la synchronisation cloud illimités, aux intégrations et à des outils supplémentaires. Sans Connect, la tablette reste utilisable, mais les fichiers inactifs depuis plus de 50 jours ne continuent pas tous à se synchroniser dans le cloud.</p>

<h2 id="comparaison">Ce qui reste sans paiement mensuel</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Écosystème</th><th>Notre lecture</th><th>Point à vérifier</th></tr></thead><tbody>
<tr><td><a href="/marques/supernote/">Supernote</a></td><td>Positionnement officiel sans abonnement, fonctions de notes avancées et mises à jour gratuites</td><td>Cloud choisi et éventuels services tiers</td></tr>
<tr><td><a href="/marques/boox/">BOOX</a></td><td>Pas d'abonnement BOOX nécessaire pour l'appareil ; 10 Go Onyx Cloud gratuits</td><td>Abonnements éventuels des apps Android installées</td></tr>
<tr><td><a href="/marques/kindle-scribe/">Kindle Scribe</a></td><td>Les fonctions de lecture et de notebook du Scribe ne sont pas présentées comme dépendantes d'un abonnement appareil</td><td>Services de contenu Amazon séparés du fonctionnement du carnet</td></tr>
<tr><td><a href="/marques/kobo-elipsa/">Kobo Elipsa 2E</a></td><td>Notes, lecture et intégrations Google Drive/Dropbox sont des fonctions de l'appareil</td><td>Livres et services de contenu restent un sujet distinct</td></tr>
<tr><td><a href="/marques/remarkable/">reMarkable</a></td><td>Utilisable gratuitement, mais Connect améliore fortement le cloud et le travail entre appareils</td><td>Décider si ces fonctions sont indispensables à votre workflow</td></tr>
</tbody></table></div>

<h2 id="supernote">Supernote : le choix le plus net si vous refusez un abonnement</h2>
<p>Supernote ne se contente pas de dire que l'appareil « fonctionne » sans abonnement : la marque présente explicitement l'absence de souscription comme un élément de son produit. Les fonctions de liens entre notes, titres, mots-clés, reconnaissance manuscrite et export peuvent donc être évaluées sans devoir intégrer un coût mensuel à la décision.</p>
<p>Le Manta convient mieux à une grande surface de notes et de PDF ; le Nomad privilégie la mobilité. Les deux restent monochromes et sans éclairage frontal. Si cette dernière contrainte est rédhibitoire, BOOX devient souvent le meilleur compromis.</p>

<h2 id="boox">BOOX : pas d'abonnement imposé, mais un écosystème plus ouvert</h2>
<p>BOOX fournit 10 Go de stockage Onyx gratuit et annonce plus de trois ans de mises à jour firmware pour ses modèles récents. Les Go 10.3 Gen II, Note Air5 C et Note Max peuvent donc être utilisés sans souscrire à un service BOOX récurrent.</p>
<p>Android change toutefois la logique : installer Microsoft 365, Notion, Dropbox ou une autre application peut introduire des coûts qui ne viennent pas de BOOX. Pour un comparatif « sans abonnement », il faut donc séparer le coût de la tablette de celui de votre stack logicielle.</p>

<h2 id="remarkable">reMarkable n'est pas à exclure, mais Connect doit être compris avant l'achat</h2>
<p>Le Paper Pure à 399 € avec Marker inclus reste pleinement capable de prendre des notes sans Connect. En revanche, reMarkable facture actuellement Connect 3,99 $ par mois ou 39,90 $ par an après un essai de 50 jours. La recherche manuscrite, le stockage cloud illimité, des intégrations et plusieurs fonctions de travail entre appareils font partie des avantages annoncés de Connect.</p>
<p>Autrement dit : si vous voulez seulement écrire, annoter et gérer vos fichiers principalement sur la tablette, reMarkable reste défendable sans abonnement. Si votre décision repose justement sur la synchronisation poussée entre tablette, ordinateur et mobile, il faut intégrer Connect au coût réel.</p>

<h2 id="regle">Notre règle de décision</h2>
<p>Choisissez Supernote si l'absence de paiement récurrent est une contrainte absolue et que l'organisation manuscrite est prioritaire. Choisissez BOOX si vous voulez rester sans abonnement constructeur mais avez besoin d'applications et de clouds multiples. Kindle ou Kobo sont plus logiques si la lecture est centrale. Choisissez reMarkable seulement après avoir vérifié que les fonctions Connect qui vous intéressent ne sont pas indispensables.</p>
<p>Le guide <a href="/guides/bloc-notes-numerique-avec-ou-sans-abonnement/">avec ou sans abonnement</a> détaille le principe ; ce comparatif applique ce critère aux appareils actuels.</p>

<h2 id="sources">Sources consultées</h2><ul class="source-list">
<li><a href="https://supernote.com/" rel="noopener noreferrer">Supernote — No subscription et mises à jour gratuites</a></li>
<li><a href="https://shop.boox.com/products/go103gen2" rel="noopener noreferrer">BOOX — 10 Go Onyx Cloud gratuits et politique de mises à jour</a></li>
<li><a href="https://remarkable.com/shop/connect/pricing" rel="noopener noreferrer">reMarkable — prix et fonctions de Connect</a></li>
<li><a href="https://remarkable.com/products/remarkable-paper/pure" rel="noopener noreferrer">reMarkable — fonctionnement du Paper Pure sans Connect</a></li>
<li><a href="https://digprjsurvey.amazon.com/csad/help/node/G7N7RPHV2SW8CKBW" rel="noopener noreferrer">Amazon — guides Kindle Scribe actuels</a></li>
<li><a href="https://ereader.kobo.com/fr-fr/products/kobo-elipsa-2e" rel="noopener noreferrer">Kobo — Elipsa 2E</a></li>
</ul>
''',

"bloc-notes-numerique-pas-cher": r'''
<p class="article-answer"><strong>Le prix le plus bas que nous avons trouvé en Europe pour un grand E Ink avec stylet inclus est actuellement le PocketBook InkPad One à 329 €.</strong> C'est un excellent achat si vous lisez beaucoup et prenez des notes simples. Pour un usage vraiment centré sur l'écriture, le reMarkable Paper Pure à partir de 399 € avec Marker inclus reste plus convaincant malgré son prix supérieur.</p>

<h2 id="deux-gagnants">Il y a deux « bons plans » différents : lire avec un stylet ou remplacer un carnet</h2>
<p>Un comparatif budget devient trompeur dès qu'il mélange le prix d'entrée et la qualité du workflow. Le PocketBook InkPad One coûte moins cher, offre un écran 10,3 pouces, un éclairage et un stylet dans la boîte. Les tests indépendants récents confirment cependant que ses fonctions de notes restent plus simples que celles de reMarkable, Supernote ou BOOX.</p>
<p>Le Paper Pure coûte 399 € sur la boutique française de reMarkable, Marker inclus. Il n'a pas d'éclairage frontal, mais son logiciel et son ergonomie sont beaucoup plus directement construits autour de la prise de notes. Pour quelqu'un qui remplace plusieurs cahiers, ces 70 € supplémentaires peuvent avoir plus de valeur qu'une longue liste de fonctions de lecture.</p>

<h2 id="budget">Les configurations à regarder en priorité</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Option</th><th>Prix repéré</th><th>Stylet</th><th>À choisir si…</th><th>Limite</th></tr></thead><tbody>
<tr><td>PocketBook InkPad One</td><td>329 € depuis le 1er août 2026</td><td>Inclus</td><td>Vous lisez beaucoup de PDF/ebooks et notez occasionnellement</td><td>Outils de notes moins avancés</td></tr>
<tr><td><a href="/marques/remarkable/">reMarkable Paper Pure</a></td><td>À partir de 399 €</td><td>Marker inclus</td><td>L'écriture et le focus sont prioritaires</td><td>Pas d'éclairage frontal</td></tr>
<tr><td><a href="/marques/kobo-elipsa/">Kobo Elipsa 2E</a></td><td>399,99 €</td><td>Vérifier le bundle au panier</td><td>Vous êtes déjà dans Kobo et voulez un grand écran</td><td>Moins fort comme carnet spécialisé</td></tr>
<tr><td><a href="/marques/boox/">BOOX Go 10.3 Gen II</a></td><td>399,99 $ sur la boutique BOOX consultée</td><td>Inclus selon bundle officiel</td><td>Vous voulez Android 15 et les apps</td><td>Prix européen/taxes à vérifier</td></tr>
</tbody></table></div>

<h2 id="pocketbook">PocketBook InkPad One : le moins cher n'est pas un faux choix</h2>
<p>Le firmware publié en août 2026 ajoute la conversion de l'écriture en texte et l'envoi direct de notes par e-mail. Le stylet actif est inclus. Pour un étudiant qui lit des cours, un lecteur de documents ou quelqu'un qui veut surligner et griffonner sans construire une base de connaissances complexe, l'offre à 329 € est sérieuse.</p>
<p>Les essais de Connect et Galaxus convergent toutefois sur une limite : les outils de notes et d'annotation sont moins aboutis que chez les spécialistes. Nous ne le choisirions donc pas seulement parce qu'il est 70 € moins cher si votre activité quotidienne consiste surtout à écrire.</p>

<h2 id="paper-pure">Paper Pure : notre meilleur rapport valeur/prix pour écrire</h2>
<p>À 399 € Marker inclus, le Paper Pure évite un piège fréquent des comparatifs budget : annoncer une tablette à un prix puis ajouter le stylet indispensable. Le système reste volontairement fermé et sans front light, mais le produit est pensé pour écrire, classer et annoter plutôt que pour être une liseuse à laquelle on a ajouté un stylet.</p>
<p>Si votre budget maximum est autour de 400 €, c'est donc notre choix par défaut pour la prise de notes. Si 329 € est déjà votre plafond, le PocketBook devient plus rationnel.</p>

<h2 id="kobo">Attention aux bundles et aux prix qui ne racontent pas toute l'histoire</h2>
<p>La boutique Kobo affiche l'Elipsa 2E à 399,99 €. Selon les pages de la boutique consultées, le texte sur l'inclusion du Stylet Kobo 2 n'est pas parfaitement cohérent : certaines pages le présentent inclus, la fiche produit mentionne aussi le stylet comme vendu séparément. Nous préférons donc vous demander de vérifier le panier réel plutôt que de publier un coût total artificiellement précis.</p>
<p>La même prudence vaut pour BOOX ou Supernote lorsqu'un prix est affiché en dollars ou via un revendeur hors France. Pour une décision budget, taxes, stylet, folio et livraison comptent plus qu'un prix catalogue isolé.</p>

<h2 id="occasion">Et l'occasion ?</h2>
<p>reMarkable a arrêté le reMarkable 2 mais continue son support logiciel et vend des appareils reconditionnés certifiés selon disponibilité. Le marché d'occasion peut donc faire descendre le coût, mais nous ne mélangeons pas ces prix variables avec les produits neufs. Consultez plutôt la page <a href="/bons-plans/bloc-notes-numerique-occasion/">bloc-notes numérique d'occasion</a> lorsque vous êtes prêt à accepter une disponibilité fluctuante.</p>

<h2 id="sources">Sources consultées</h2><ul class="source-list">
<li><a href="https://pocketbook.de/en/news/more-ways-to-take-notes-new-firmware-update-for-the-pocketbook-inkpad-one" rel="noopener noreferrer">PocketBook — InkPad One, prix et firmware août 2026</a></li>
<li><a href="https://www.connect.de/testbericht/pocketbook-inkpad-one-test-ereader-review-3213274.html" rel="noopener noreferrer">Connect — test InkPad One, septembre 2026</a></li>
<li><a href="https://www.galaxus.be/fr/page/pocketbook-inkpad-one-tablette-e-ink-basee-sur-linux-a-lessai-42544" rel="noopener noreferrer">Galaxus — test InkPad One</a></li>
<li><a href="https://remarkable.com/fr-FR/shop/compare" rel="noopener noreferrer">reMarkable France — Paper Pure à partir de 399 €, Marker inclus</a></li>
<li><a href="https://ereader.kobo.com/fr-fr/products/kobo-elipsa-2e" rel="noopener noreferrer">Kobo France — Elipsa 2E</a></li>
<li><a href="https://shop.boox.com/products/go103gen2" rel="noopener noreferrer">BOOX — Go 10.3 Gen II</a></li>
</ul>
''',

"remarkable-vs-boox": r'''
<p class="article-answer"><strong>Choisissez reMarkable si vous voulez que votre tablette disparaisse derrière votre travail ; choisissez BOOX si vous voulez que votre tablette E Ink s'intègre à vos applications.</strong> En 2026, réduire ce duel à Paper Pure contre Go 10.3 serait trop étroit : reMarkable propose aussi Paper Pro et Paper Pro Move, tandis que BOOX couvre du Go 10.3 Gen II au Note Air5 C et aux grands Note Max/Tab X C.</p>

<h2 id="philosophie">Le vrai choix : protéger le focus ou ouvrir le workflow</h2>
<p>ZDNET résume bien le contraste en comparant directement Paper Pure et Go 10.3 Lumi : les deux ont un format proche et un prix voisin, mais le BOOX est un appareil ouvert et polyvalent alors que le reMarkable est construit comme un outil de travail sans distractions.</p>
<p>Cette différence traverse toute la gamme. Sur reMarkable, vous ne choisissez pas des apps : vous choisissez une taille, la couleur, l'éclairage et le niveau de mobilité dans le même environnement logiciel. Sur BOOX, Android, Google Play, les clouds et les apps tierces deviennent des éléments centraux de la décision.</p>

<h2 id="choisir">Quel écosystème selon votre priorité ?</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Priorité</th><th>reMarkable</th><th>BOOX</th></tr></thead><tbody>
<tr><td>Prendre des notes sans distractions</td><td><strong>Avantage net</strong></td><td>Possible, mais l'ouverture demande plus de configuration</td></tr>
<tr><td>Apps Android / Kindle / Kobo / Notion</td><td>Non</td><td><strong>Avantage net</strong></td></tr>
<tr><td>Écran couleur focalisé</td><td>Paper Pro / Move</td><td>Note Air5 C / Tab X C</td></tr>
<tr><td>Grand format 13,3"</td><td>Pas de 13,3" actuel</td><td><strong>Note Max / Tab X C</strong></td></tr>
<tr><td>Éclairage sur un 10,3" monochrome</td><td>Paper Pure : non</td><td><strong>Go 10.3 Gen II Lumi : oui</strong></td></tr>
<tr><td>Interface simple</td><td><strong>Avantage</strong></td><td>Plus dense et réglable</td></tr>
</tbody></table></div>

<h2 id="equivalents">Les modèles qui se répondent réellement</h2>
<p><strong>Paper Pure vs Go 10.3 Gen II/Lumi :</strong> c'est le duel le plus propre pour l'écriture monochrome autour de 10 pouces. Le Pure privilégie la simplicité. Le Go ajoute Android 15 ; la version Lumi ajoute l'éclairage frontal.</p>
<p><strong>Paper Pro vs Note Air5 C :</strong> les deux introduisent la couleur, mais BOOX reste plus « tablette » avec Android 15, Google Play et un clavier optionnel. Paper Pro garde un environnement focalisé et un écran plus grand de 11,8 pouces.</p>
<p><strong>Paper Pro Move :</strong> reMarkable possède ici un produit compact 7,3 pouces sans équivalent direct dans la gamme de notes BOOX que nous recommandons. À l'inverse, BOOX possède des 13,3 pouces sans équivalent reMarkable.</p>

<h2 id="ecriture">Pour l'écriture, les tests ne racontent pas une victoire simple</h2>
<p>Les comparaisons hands-on d'eWritable et ZDNET montrent surtout des préférences de philosophie et de sensation. BOOX a énormément progressé sur ses logiciels et ses écrans ; reMarkable reste plus immédiat à prendre en main. Le Go 10.3 Gen II utilise désormais un stylet actif InkSense, qu'eWritable juge bon mais moins convaincant que certains anciens systèmes EMR.</p>
<p>Nous ne transformons donc pas une préférence de stylet en score universel. Si le geste d'écriture est votre critère numéro un, essayez idéalement l'appareil ou consultez plusieurs tests hands-on.</p>

<h2 id="cloud">Le cloud et les abonnements peuvent renverser la décision</h2>
<p>BOOX offre 10 Go de cloud Onyx mais laisse aussi installer les services de votre choix. reMarkable Connect est facultatif, mais certaines fonctions avancées de synchronisation et de recherche sont liées à l'abonnement. Un utilisateur déjà dépendant de plusieurs apps professionnelles peut trouver BOOX beaucoup plus naturel ; quelqu'un qui veut précisément sortir de cette complexité préférera reMarkable.</p>

<h2 id="verdict">Notre verdict</h2>
<p><strong>reMarkable gagne pour le focus.</strong> Paper Pure est le choix le plus simple pour écrire ; Paper Pro ajoute couleur et éclairage ; Move ajoute la mobilité.</p>
<p><strong>BOOX gagne pour l'ouverture.</strong> Go 10.3 Gen II/Lumi convient à l'écriture monochrome, Note Air5 C à la couleur et aux apps, Note Max/Tab X C aux grands documents.</p>
<p>Si votre question est « lequel est meilleur ? », remplacez-la par « est-ce que je veux moins de possibilités ou davantage ? ». C'est ce qui fait réellement basculer ce duel.</p>

<h2 id="sources">Sources consultées</h2><ul class="source-list">
<li><a href="https://www.zdnet.fr/guide-achat/remarkable-paper-pure-vs-boox-go-10-3-lumi-2e-generation-quelle-tablette-choisir-pour-le-travail-496047.htm" rel="noopener noreferrer">ZDNET France — Paper Pure vs BOOX Go 10.3 Lumi, mise à jour septembre 2026</a></li>
<li><a href="https://ewritable.net/remarkable-vs-boox-which-are-the-best-e-ink-tablets/" rel="noopener noreferrer">eWritable — reMarkable vs BOOX, mars 2026</a></li>
<li><a href="https://remarkable.com/fr-FR/shop/compare" rel="noopener noreferrer">reMarkable — gamme actuelle</a></li>
<li><a href="https://shop.boox.com/products/go103gen2" rel="noopener noreferrer">BOOX — Go 10.3 Gen II / Lumi</a></li>
<li><a href="https://shop.boox.com/products/noteair5c" rel="noopener noreferrer">BOOX — Note Air5 C</a></li>
<li><a href="https://shop.boox.com/products/notemax" rel="noopener noreferrer">BOOX — Note Max</a></li>
</ul>
''',

"remarkable-vs-supernote": r'''
<p class="article-answer"><strong>Supernote est notre choix pour construire un système de notes manuscrites ; reMarkable est notre choix pour écrire avec le moins de friction.</strong> Les deux marques sont beaucoup plus proches l'une de l'autre que BOOX : elles assument un appareil spécialisé plutôt qu'une tablette généraliste. La différence se joue donc dans la profondeur de l'organisation, la simplicité, la couleur, l'éclairage et la politique d'abonnement.</p>

<h2 id="meme-but">Deux marques focalisées, deux définitions du « carnet numérique »</h2>
<p>eWritable décrit Supernote et reMarkable comme deux des interprétations les plus concentrées du carnet E Ink. reMarkable travaille l'immédiateté : ouvrir, écrire, classer, partager. Supernote ajoute une logique plus proche d'un système de connaissances avec titres manuscrits, mots-clés, étoiles et liens entre notes, PDF, ebooks et pages web.</p>
<p>Ce n'est pas une différence de « puissance ». Une personne qui prend des notes linéaires peut trouver les fonctions Supernote inutiles ; une personne qui construit des dossiers sur plusieurs mois peut trouver reMarkable trop simple.</p>

<h2 id="decision">Choisissez selon la manière dont vos notes vieillissent</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Vous voulez…</th><th>Choix</th><th>Pourquoi</th></tr></thead><tbody>
<tr><td>Écrire immédiatement et rester focalisé</td><td><a href="/marques/remarkable/">reMarkable</a></td><td>Interface plus simple et gamme cohérente</td></tr>
<tr><td>Relier, indexer et retrouver beaucoup de notes</td><td><a href="/marques/supernote/">Supernote</a></td><td>Liens, titres, mots-clés, étoiles, reconnaissance hors ligne</td></tr>
<tr><td>Écrire en couleur ou avec éclairage frontal</td><td><a href="/marques/remarkable/">reMarkable Paper Pro / Move</a></td><td>Supernote reste monochrome et sans front light</td></tr>
<tr><td>Éviter tout abonnement constructeur</td><td><a href="/marques/supernote/">Supernote</a></td><td>La marque annonce explicitement « No subscription »</td></tr>
<tr><td>Un grand carnet léger et réparable</td><td><a href="/marques/supernote/">Manta</a></td><td>Conception modulaire et approche long terme</td></tr>
</tbody></table></div>

<h2 id="pure-manta">Paper Pure vs Manta : le duel le plus pertinent</h2>
<p>Le Paper Pure et le Manta sont les deux appareils à regarder si vous cherchez surtout un grand carnet monochrome. Le Pure démarre à 399 € avec Marker inclus et pèse 360 g. Le Manta mise sur un écran de taille proche A5, la modularité et un système de notes plus profond.</p>
<p>Les comparatifs hands-on récents ne donnent pas un vainqueur universel. Kit Betts-Masters continue de préférer le Manta pour ses headings, links et digest, tout en trouvant le Paper Pure beaucoup plus compétitif qu'attendu sur la simplicité et le dessin. C'est exactement la raison pour laquelle nous préférons une recommandation conditionnelle à un score global.</p>

<h2 id="gammes">La gamme reMarkable couvre des besoins que Supernote ne couvre pas</h2>
<p>Paper Pro apporte un écran couleur 11,8 pouces et un éclairage frontal. Paper Pro Move apporte la couleur et l'éclairage dans 7,3 pouces. Supernote ne propose actuellement ni couleur ni front light. Si ces deux critères sont importants, la comparaison s'arrête rapidement.</p>
<p>À l'inverse, Supernote Nomad est un petit carnet 7,8 pouces très mobile avec la même philosophie logicielle que Manta. Il n'est pas un équivalent exact du Move : le Nomad privilégie l'organisation et le monochrome, le Move privilégie couleur, éclairage et compacité.</p>

<h2 id="abonnement">La politique logicielle peut compter autant que le matériel</h2>
<p>Supernote annonce des mises à jour gratuites sans abonnement. reMarkable Connect reste optionnel, mais réserve des fonctions comme la recherche manuscrite, le cloud illimité et plusieurs intégrations. Cela ne rend pas reMarkable inutilisable sans Connect ; cela signifie simplement que le coût à long terme doit être examiné si ces fonctions sont au cœur de votre workflow.</p>

<h2 id="verdict">Verdict : simplicité reMarkable, profondeur Supernote</h2>
<p>Nous recommandons reMarkable à quelqu'un qui veut un carnet numérique simple et cohérent, ou qui a besoin de couleur/éclairage. Nous recommandons Supernote à quelqu'un dont la difficulté principale est de structurer, relier et retrouver des années de notes sans abonnement constructeur.</p>
<p>Pour une comparaison plus générale, consultez aussi <a href="/comparatifs/meilleur-bloc-notes-numerique/">notre sélection des meilleurs bloc-notes numériques</a>.</p>

<h2 id="sources">Sources consultées</h2><ul class="source-list">
<li><a href="https://ewritable.net/remarkable-vs-supernote-which-is-the-best-e-ink-tablet/" rel="noopener noreferrer">eWritable — reMarkable vs Supernote, mars 2026</a></li>
<li><a href="https://supernote.com/pages/note-system-everything-you-need-to-stay-organized" rel="noopener noreferrer">Supernote — système de notes</a></li>
<li><a href="https://supernote.com/pages/supernote-manta" rel="noopener noreferrer">Supernote — Manta et politique sans abonnement</a></li>
<li><a href="https://remarkable.com/fr-FR/shop/compare" rel="noopener noreferrer">reMarkable — comparaison de la gamme</a></li>
<li><a href="https://remarkable.com/shop/connect/pricing" rel="noopener noreferrer">reMarkable — Connect</a></li>
</ul>
''',

"boox-vs-supernote": r'''
<p class="article-answer"><strong>Choisissez BOOX si votre bloc-notes doit exécuter des applications et ouvrir presque n'importe quel type de document ; choisissez Supernote si votre priorité est de construire un système de notes manuscrites durable.</strong> Le duel oppose un ordinateur E Ink flexible à un carnet E Ink spécialisé.</p>

<h2 id="pas-un-duel">BOOX et Supernote ne cherchent pas à résoudre le même problème</h2>
<p>BOOX équipe ses modèles récents d'Android et de Google Play. Le Go 10.3 Gen II fonctionne sous Android 15, le Note Air5 C ajoute la couleur et le Note Max monte à 13,3 pouces. Supernote reste volontairement plus limité : écriture, lecture, organisation, reconnaissance et quelques fonctions intégrées, sans ambition de remplacer une tablette Android.</p>
<p>Cette limite est souvent l'avantage principal de Supernote. Moins d'apps signifie aussi moins de réglages et moins de tentations de transformer le carnet en deuxième ordinateur.</p>

<h2 id="choix">Le bon choix dépend de ce qui doit se passer après l'écriture</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Après avoir écrit, vous devez…</th><th>Choix</th></tr></thead><tbody>
<tr><td>Relier des notes, créer des titres manuscrits, indexer par mots-clés</td><td><strong>Supernote</strong></td></tr>
<tr><td>Ouvrir une app Android, un service métier ou plusieurs lecteurs</td><td><strong>BOOX</strong></td></tr>
<tr><td>Travailler en couleur</td><td><strong>BOOX Note Air5 C / Tab X C</strong></td></tr>
<tr><td>Lire des PDF A4 sur 13,3 pouces</td><td><strong>BOOX Note Max / Tab X C</strong></td></tr>
<tr><td>Éviter un abonnement constructeur et rester focalisé</td><td><strong>Supernote</strong></td></tr>
<tr><td>Avoir un éclairage frontal sur un 10 pouces monochrome</td><td><strong>BOOX Go 10.3 Lumi</strong></td></tr>
</tbody></table></div>

<h2 id="manta-go">Manta vs Go 10.3 Gen II : le face-à-face le plus proche</h2>
<p>Ces deux appareils sont les plus comparables pour un utilisateur qui veut écrire en noir et blanc sur un format autour de 10 pouces. Le Manta pousse beaucoup plus loin les liens et l'organisation des carnets. Le Go 10.3 Gen II apporte Android 15 et Google Play ; la version Lumi ajoute l'éclairage frontal.</p>
<p>eWritable a longtemps utilisé Supernote comme appareil principal mais a aussi salué le Go 10.3 comme l'un des premiers BOOX capables de se faire oublier comme « ordinateur ». Sur la génération II, le site apprécie les progrès mais regrette le passage à un stylet actif par rapport à l'ancien EMR. Là encore, cela montre pourquoi un score unique simplifierait trop le choix.</p>

<h2 id="air5c">Note Air5 C : BOOX sort complètement du terrain de Supernote</h2>
<p>Le Note Air5 C fonctionne sous Android 15, utilise un écran Kaleido 3 couleur, possède un éclairage frontal et accepte un clavier optionnel. TechRadar juge son expérience d'écriture excellente et sa polyvalence très forte, tout en soulignant une interface complexe, le poids et une autonomie plus courte qu'un appareil spécialisé.</p>
<p>Si vous avez besoin de couleur, Gmail, Kindle, Kobo, Libby ou d'autres apps sur l'appareil, Supernote n'est tout simplement pas le produit équivalent. Si vous n'en avez pas besoin, cette polyvalence peut devenir du bruit.</p>

<h2 id="long-terme">Supernote répond mieux à la question « que deviennent mes notes dans deux ans ? »</h2>
<p>Les titres, liens, mots-clés, étoiles et la recherche manuscrite hors ligne sont conçus pour retrouver de l'information dans une base de notes qui grandit. La marque met aussi en avant la modularité matérielle et l'absence d'abonnement.</p>
<p>BOOX peut évidemment stocker, chercher et synchroniser beaucoup de contenu, mais sa force vient surtout de l'ouverture : vous choisissez plus librement les apps et services qui feront ce travail.</p>

<h2 id="verdict">Verdict</h2>
<p><strong>BOOX gagne dès qu'une application, la couleur, un écran 13,3 pouces ou l'éclairage frontal est non négociable.</strong></p>
<p><strong>Supernote gagne lorsqu'un carnet manuscrit structuré, simple et sans abonnement est le cœur du besoin.</strong></p>
<p>Si vous ne savez pas encore dans quelle catégorie vous êtes, le guide <a href="/guides/ecosysteme-ouvert-ou-ferme/">écosystème ouvert ou fermé</a> permet de trancher avant de comparer les modèles.</p>

<h2 id="sources">Sources consultées</h2><ul class="source-list">
<li><a href="https://shop.boox.com/products/go103gen2" rel="noopener noreferrer">BOOX — Go 10.3 Gen II / Lumi</a></li>
<li><a href="https://shop.boox.com/products/noteair5c" rel="noopener noreferrer">BOOX — Note Air5 C</a></li>
<li><a href="https://shop.boox.com/products/notemax" rel="noopener noreferrer">BOOX — Note Max</a></li>
<li><a href="https://supernote.com/pages/supernote-manta" rel="noopener noreferrer">Supernote — Manta</a></li>
<li><a href="https://supernote.com/pages/note-system-everything-you-need-to-stay-organized" rel="noopener noreferrer">Supernote — organisation des notes</a></li>
<li><a href="https://ewritable.net/brands/boox/tablets/boox-go-10-3-gen-2/" rel="noopener noreferrer">eWritable — BOOX Go 10.3 Gen II</a></li>
<li><a href="https://www.techradar.com/tablets/ereaders/onyx-boox-note-air5-c-review" rel="noopener noreferrer">TechRadar — Note Air5 C</a></li>
</ul>
'''
}
