"""Contenus guides produits par le workflow guide-content-workflow.

Ce module complète et remplace les entrées de GUIDE_CONTENT de _generate.py.
Toutes les pages restent noindex jusqu'à validation humaine du lot.
"""

GUIDE_CONTENT_EXTRA = {
    "/guides/choisir-bloc-notes-numerique/": """
      <p class="article-answer"><strong>Pour choisir un bloc-notes numérique, commencez par les tâches qui doivent absolument fonctionner.</strong> Vérifiez d'abord vos fichiers, vos exports, le cloud et les applications nécessaires. La taille d'écran, la couleur, le stylet et l'autonomie viennent ensuite. Un seul blocage dans votre flux de travail peut suffire à éliminer un modèle.</p>

      <h2 id="eliminatoires">Les critères éliminatoires avant les fiches techniques</h2>
      <p>Une longue liste de caractéristiques aide peu si l'appareil ne peut pas récupérer, annoter ou restituer vos documents comme prévu. Avant de comparer les écrans, notez le parcours complet d'un fichier : arrivée sur l'appareil, annotation, classement, export puis ouverture sur votre ordinateur ou celui d'un collègue.</p>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Question</th><th>Pourquoi elle passe en premier</th><th>Exemple de blocage</th></tr></thead>
        <tbody>
          <tr><td>Quels fichiers utilisez-vous ?</td><td>PDF, EPUB et documents bureautiques ne sont pas gérés de la même manière selon l'écosystème.</td><td>un PDF protégé ou un format non pris en charge</td></tr>
          <tr><td>Où doivent finir vos notes ?</td><td>L'export conditionne le partage et l'archivage.</td><td>notes visibles sur l'appareil mais difficiles à récupérer ailleurs</td></tr>
          <tr><td>Quel cloud est indispensable ?</td><td>Google Drive, OneDrive et Dropbox ne sont pas intégrés partout de la même façon.</td><td>copie manuelle à chaque échange</td></tr>
          <tr><td>Avez-vous besoin d'une application précise ?</td><td>Un système spécialisé n'offre pas la même liberté qu'Android.</td><td>application métier absente ou peu adaptée à l'E Ink</td></tr>
        </tbody>
      </table></div>

      <h2 id="profils">Quel type d'écosystème correspond à votre usage ?</h2>
      <p>Les familles de produits n'ont pas toutes le même objectif. Les exemples ci-dessous servent à comprendre leur orientation, pas à établir un classement.</p>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Priorité</th><th>À vérifier en premier</th><th>Familles à examiner</th></tr></thead>
        <tbody>
          <tr><td>Réunions et écriture</td><td>organisation des carnets, export PDF, simplicité</td><td>reMarkable, Supernote et autres appareils spécialisés</td></tr>
          <tr><td>Lecture et prise de notes</td><td>bibliothèque, annotation des livres et PDF</td><td>Kindle Scribe, Kobo Elipsa et autres hybrides lecture-écriture</td></tr>
          <tr><td>Applications tierces</td><td>Android, Google Play, comportement des apps sur E Ink</td><td>BOOX et tablettes E Ink ouvertes</td></tr>
          <tr><td>PDF grands formats</td><td>surface utile, poids, zoom</td><td>tablettes proches de 11 à 13 pouces</td></tr>
          <tr><td>Documents en couleur</td><td>valeur réelle de la couleur, contraste, export</td><td>modèles E Ink couleur</td></tr>
        </tbody>
      </table></div>

      <h2 id="questions">Cinq questions à trancher avant l'achat</h2>
      <ol>
        <li><strong>Écrivez-vous surtout des notes libres ou annotez-vous des PDF ?</strong> Un carnet de réunion et un article scientifique proche de l'A4 n'imposent pas la même surface.</li>
        <li><strong>Vos notes doivent-elles devenir du texte ?</strong> Vérifiez la reconnaissance manuscrite, les langues prises en charge et les formats d'export.</li>
        <li><strong>Lisez-vous autant que vous écrivez ?</strong> Une liseuse avec stylet peut suffire si la bibliothèque reste l'usage principal.</li>
        <li><strong>La couleur transporte-t-elle une information ?</strong> Si elle ne sert qu'à décorer, elle ne doit pas décider seule.</li>
        <li><strong>Quel coût total acceptez-vous ?</strong> Comptez le stylet, la protection et les services récurrents réellement nécessaires.</li>
      </ol>

      <h2 id="ouvert-ferme">Écosystème spécialisé ou tablette E Ink ouverte ?</h2>
      <p>reMarkable concentre son logiciel sur les carnets, documents et applications compagnon. BOOX propose au contraire des appareils Android avec davantage d'applications et de réglages. Cette ouverture donne plus de possibilités, mais une application conçue pour LCD ou OLED peut rester peu agréable sur un écran à rafraîchissement plus lent.</p>
      <p>Le bon choix dépend donc moins du nombre de fonctions que du nombre de vos tâches indispensables que l'appareil exécute correctement.</p>

      <h2 id="materiel">Les critères matériels viennent ensuite</h2>
      <p>Une fois le flux de travail validé, comparez la taille d'écran, l'éclairage frontal éventuel, la couleur, le poids, le stylet et les accessoires. La sensation d'écriture ne peut pas être déduite honnêtement d'une fiche technique : latence perçue, frottement et bruit dépendent du couple écran-stylet et de préférences personnelles.</p>
      <p>Pour approfondir, consultez les guides sur la <a href="/guides/taille-ecran-bloc-notes-numerique/">taille d'écran</a>, la <a href="/guides/bloc-notes-numerique-couleur-ou-noir-et-blanc/">couleur</a>, les <a href="/guides/bloc-notes-numerique-avec-ou-sans-abonnement/">abonnements</a> et le <a href="/guides/prix-bloc-notes-numerique/">budget total</a>. Une fois vos critères éliminatoires fixés, passez au <a href="/comparatifs/meilleur-bloc-notes-numerique/">comparatif des bloc-notes numériques</a>.</p>

      <h2 id="sources">Sources consultées</h2>
      <ul class="source-list">
        <li><a href="https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files" rel="noopener noreferrer">reMarkable : import, export, cloud et USB</a></li>
        <li><a href="https://help.boox.com/hc/en-us/articles/8569457124628-Integrated-Third-Party-Cloud-Storage" rel="noopener noreferrer">BOOX : stockage cloud tiers intégré</a></li>
        <li><a href="https://help.kobo.com/hc/fr/articles/360062226733-Utiliser-votre-liseuse-Kobo-comme-un-carnet" rel="noopener noreferrer">Kobo : carnets et conversion manuscrite</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/TP8wuaQilIlwlITVTL" rel="noopener noreferrer">Amazon : partage Kindle Scribe vers Google Drive et OneDrive</a></li>
      </ul>
    """,

    "/guides/liseuse-ou-bloc-notes-numerique/": """
      <p class="article-answer"><strong>Choisissez une liseuse si la lecture reste votre activité dominante ; choisissez un bloc-notes numérique si l'écriture, les PDF et la circulation des notes structurent votre travail.</strong> Les appareils hybrides comme Kindle Scribe ou Kobo Elipsa rapprochent les deux univers, mais ils ne rendent pas les flux d'export et d'annotation identiques.</p>

      <h2 id="difference">La différence se joue dans le logiciel, pas seulement dans l'écran</h2>
      <p>Une liseuse est organisée autour des livres : bibliothèque, lecture, surlignage et annotations liées aux ouvrages. Un bloc-notes numérique est organisé autour de pages de travail : carnets, modèles, classement, stylet, export et partage. Les deux peuvent utiliser de l'encre électronique ; c'est donc le parcours de vos contenus qui les distingue vraiment.</p>

      <h2 id="tableau">Liseuse, hybride ou bloc-notes : comparaison pratique</h2>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Besoin</th><th>Liseuse</th><th>Hybride lecture + stylet</th><th>Bloc-notes spécialisé</th></tr></thead>
        <tbody>
          <tr><td>Romans et ebooks</td><td>usage central</td><td>usage central</td><td>variable selon l'écosystème</td></tr>
          <tr><td>Carnets manuscrits</td><td>absents ou secondaires</td><td>présents</td><td>usage central</td></tr>
          <tr><td>PDF</td><td>lecture possible mais format parfois petit</td><td>annotation prévue sur certains modèles</td><td>souvent prioritaire</td></tr>
          <tr><td>Export des notes</td><td>souvent lié au livre</td><td>dépend du type de contenu</td><td>fonction à vérifier avant achat</td></tr>
          <tr><td>Mobilité</td><td>souvent compacte</td><td>souvent autour de 10 pouces</td><td>du compact au grand format</td></tr>
        </tbody>
      </table></div>

      <h2 id="hybrides">Ce que changent Kindle Scribe et Kobo Elipsa</h2>
      <p>Kindle Scribe permet d'écrire dans des carnets et d'ajouter des annotations à différents documents. Les modèles sortis en 2025 ou après peuvent aussi importer depuis Google Drive ou OneDrive et y renvoyer des copies annotées. Amazon précise toutefois que les annotations ajoutées à un fichier importé ne se synchronisent pas automatiquement vers le fichier d'origine : il faut exporter une nouvelle copie.</p>
      <p>Kobo Elipsa et les autres Kobo compatibles avec le stylet proposent des carnets de base et avancés. Les carnets avancés peuvent convertir l'écriture en texte. Pour les livres, les annotations manuscrites restent cependant contraintes par le format : Kobo indique par exemple que les annotations d'EPUB ne s'exportent pas comme les annotations d'un PDF non protégé.</p>

      <h2 id="test">Testez un cycle complet plutôt qu'une liste de fonctions</h2>
      <ol>
        <li>Importez ou imaginez votre document le plus fréquent : livre, PDF de cours, contrat ou article.</li>
        <li>Vérifiez où vous pouvez écrire : directement sur la page, dans une note liée ou dans un carnet séparé.</li>
        <li>Vérifiez comment retrouver l'annotation plusieurs semaines plus tard.</li>
        <li>Contrôlez ce qui sort réellement de l'appareil : PDF annoté, texte converti, image ou lien.</li>
      </ol>
      <p>Si le cycle se termine dans l'écosystème de lecture, une liseuse hybride peut être suffisante. Si vos notes doivent devenir des documents de travail partagés, un bloc-notes spécialisé ou une tablette E Ink plus ouverte mérite davantage d'attention.</p>

      <h2 id="decision">La règle de décision</h2>
      <p>Lecture très majoritaire et notes brèves : partez d'une liseuse. Lecture et écriture réellement équilibrées : examinez les hybrides. Écriture quotidienne, PDF, classement et export : partez d'un bloc-notes numérique. Pour aller plus loin, comparez <a href="/comparatifs/kindle-scribe-vs-kobo-elipsa/">Kindle Scribe et Kobo Elipsa</a> ou consultez le guide <a href="/usages/lecture-et-prise-de-notes/">lecture et prise de notes</a>.</p>

      <h2 id="sources">Sources consultées</h2>
      <ul class="source-list">
        <li><a href="https://help.kobo.com/hc/fr/articles/1500001927562-Annoter-votre-livre-avec-le-stylet-Kobo" rel="noopener noreferrer">Kobo : annotation des livres et export des PDF</a></li>
        <li><a href="https://help.kobo.com/hc/fr/articles/360062226733-Utiliser-votre-liseuse-Kobo-comme-un-carnet" rel="noopener noreferrer">Kobo : carnets de base et avancés</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/TjrMJmg3DZpAQLwVuN" rel="noopener noreferrer">Amazon : import Google Drive et OneDrive sur Kindle Scribe</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/TJE2UYmdw0ppUuR3Rs" rel="noopener noreferrer">Amazon : partage des notes et carnets Kindle Scribe</a></li>
      </ul>
    """,

    "/guides/tablette-classique-ou-tablette-e-ink/": """
      <p class="article-answer"><strong>Une tablette E Ink est pertinente si votre journée est surtout composée de lecture, d'écriture et de documents statiques. Une tablette classique reste préférable dès que vidéo, visioconférence, applications interactives, navigation rapide ou restitution fidèle des couleurs deviennent indispensables.</strong></p>

      <h2 id="ecrans">Deux technologies, deux rythmes d'utilisation</h2>
      <p>Un écran LCD ou OLED émet de la lumière et actualise rapidement son image. Un écran E Ink est réfléchissant : il utilise la lumière ambiante et conserve une image sans devoir l'alimenter en continu. E Ink précise toutefois que les mises à jour d'écran prennent du temps et que les modes rapides réduisent une partie de l'avantage énergétique. Cela explique pourquoi l'E Ink excelle sur les pages statiques mais reste moins naturel pour les interfaces animées.</p>

      <h2 id="comparaison">Comparaison par tâche</h2>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Tâche</th><th>Tablette E Ink</th><th>Tablette classique</th></tr></thead>
        <tbody>
          <tr><td>Notes manuscrites longues</td><td>usage cohérent, interfaces souvent centrées sur le stylet</td><td>très bonnes applications, expérience plus polyvalente</td></tr>
          <tr><td>Lecture de PDF</td><td>adaptée si la taille d'écran convient</td><td>adaptée, zoom et défilement plus fluides</td></tr>
          <tr><td>Vidéo et visioconférence</td><td>mauvais critère d'achat</td><td>usage normal</td></tr>
          <tr><td>Applications métier</td><td>à tester modèle par modèle</td><td>écosystèmes complets</td></tr>
          <tr><td>Couleurs fidèles</td><td>pas l'objectif principal</td><td>plus adaptée</td></tr>
          <tr><td>Autonomie sur contenu statique</td><td>avantage structurel de l'affichage bistable</td><td>écran alimenté en continu</td></tr>
        </tbody>
      </table></div>

      <h2 id="deconseille">Les situations où je déconseille une tablette E Ink</h2>
      <p>Une tablette E Ink ne devrait pas être votre appareil principal si votre journée dépend de Teams ou Zoom, de vidéos, de Canva ou d'outils graphiques, de dashboards très interactifs, de défilements rapides ou d'une application dont l'interface n'a pas été pensée pour l'encre électronique. Android sur BOOX élargit le choix d'applications, mais l'accès à une app ne garantit pas que ses animations et ses contrastes soient agréables sur E Ink.</p>

      <h2 id="surdimensionnee">Quand une tablette classique est inutilement polyvalente</h2>
      <p>Si votre besoin se limite à écrire des comptes rendus, lire des documents, surligner des articles, corriger des PDF et retrouver vos carnets, une tablette classique peut fournir beaucoup de fonctions dont vous ne vous servez jamais. Dans ce cas, l'intérêt d'une tablette E Ink vient autant de sa spécialisation que de sa technologie d'écran.</p>

      <h2 id="couleur">La couleur ne transforme pas l'E Ink en écran LCD</h2>
      <p>Les technologies E Ink couleur existent, mais elles conservent les contraintes d'un écran destiné à des contenus relativement statiques. Pour des schémas, légendes ou surlignages, la couleur peut suffire. Pour la photo, la vidéo ou la création graphique fidèle, une tablette classique reste le choix le plus cohérent.</p>

      <h2 id="decision">Décidez avec votre tâche la plus exigeante</h2>
      <p>Commencez par la tâche qui tolère le moins de compromis. Si elle exige un écran rapide ou une application précise, partez d'une tablette classique. Si elle consiste surtout à lire et écrire, examinez l'E Ink. Ensuite seulement, comparez le <a href="/guides/ecosysteme-ouvert-ou-ferme/">niveau d'ouverture de l'écosystème</a>, la <a href="/guides/bloc-notes-numerique-couleur-ou-noir-et-blanc/">couleur</a> et la <a href="/guides/taille-ecran-bloc-notes-numerique/">taille d'écran</a>.</p>

      <h2 id="sources">Sources consultées</h2>
      <ul class="source-list">
        <li><a href="https://www.eink.com/tech/detail/How_it_works" rel="noopener noreferrer">E Ink : fonctionnement, modes de mise à jour et vidéo</a></li>
        <li><a href="https://www.eink.com/tech/detail/Benefits" rel="noopener noreferrer">E Ink : bistabilité et affichage réfléchissant</a></li>
        <li><a href="https://help.boox.com/hc/en-us/articles/8569457124628-Integrated-Third-Party-Cloud-Storage" rel="noopener noreferrer">BOOX : intégration de services tiers</a></li>
      </ul>
    """,

    "/guides/taille-ecran-bloc-notes-numerique/": """
      <p class="article-answer"><strong>Un écran d'environ 10 pouces reste un point de départ polyvalent pour écrire et annoter des PDF, mais la diagonale seule ne suffit pas.</strong> Un format compact privilégie le transport ; un écran de 11 à 13 pouces facilite les grands documents. Choisissez le plus petit écran qui affiche correctement votre document principal.</p>

      <h2 id="mesure">La diagonale ne décrit pas la surface utile</h2>
      <p>Les pouces mesurent la diagonale. Ils ne disent rien du ratio de l'écran, des bordures ni de l'espace occupé par l'interface. Deux appareils proches sur la fiche technique peuvent donc afficher une page de façon différente. Pour un PDF, la largeur de texte réellement lisible est souvent plus utile que la diagonale annoncée.</p>

      <h2 id="formats">Quel format pour quel usage ?</h2>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Taille indicative</th><th>Usage cohérent</th><th>Compromis à accepter</th></tr></thead>
        <tbody>
          <tr><td>7 à 8 pouces</td><td>listes, journal, notes brèves, mobilité</td><td>peu d'espace pour les PDF complexes</td></tr>
          <tr><td>Autour de 10 pouces</td><td>réunions, cours, carnets, PDF courants</td><td>documents proches de l'A4 souvent zoomés</td></tr>
          <tr><td>11 à 13 pouces</td><td>articles scientifiques, partitions, plans, grands PDF</td><td>poids, transport et prix plus contraignants</td></tr>
        </tbody>
      </table></div>

      <h2 id="documents">Partez du document, pas du produit</h2>
      <p>Un contrat A4 avec de petites notes de bas de page, une partition ou un article scientifique n'imposent pas les mêmes contraintes qu'un carnet de réunion. Un grand écran évite certains zooms, mais il devient inutile s'il reste sur un bureau alors que vous aviez besoin de mobilité.</p>
      <p>Les gammes actuelles illustrent l'amplitude disponible : reMarkable documente par exemple des formats allant de 7,3 pouces sur Paper Pro Move à 11,8 pouces sur Paper Pro. Ces chiffres servent de repères de taille, pas de recommandation de modèle.</p>

      <h2 id="test">Un test simple avant l'achat</h2>
      <ol>
        <li>Choisissez le PDF ou le modèle de page que vous utilisez le plus.</li>
        <li>Regardez ses proportions et la taille du texte.</li>
        <li>Vérifiez sur une démonstration, une capture à l'échelle ou le manuel si la page impose un zoom fréquent.</li>
        <li>Ajoutez l'étui et le stylet lorsque vous comparez le poids transporté.</li>
      </ol>

      <h2 id="decision">La règle de décision</h2>
      <p>Choisissez le plus petit écran qui laisse votre document principal réellement exploitable. Si vous travaillez régulièrement sur des pages proches de l'A4, consultez ensuite le <a href="/comparatifs/bloc-notes-numerique-a4/">comparatif des grands formats</a>. Pour des carnets, cours et réunions, un format autour de 10 pouces reste le compromis à examiner en premier. Vérifiez enfin le <a href="/guides/prix-bloc-notes-numerique/">budget total</a>, car la taille influence aussi le prix et l'encombrement.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/s/article/About-reMarkable-Paper-Pro-Move" rel="noopener noreferrer">reMarkable : Paper Pro Move</a></li>
        <li><a href="https://support.remarkable.com/s/article/About-reMarkable-2" rel="noopener noreferrer">reMarkable : reMarkable 2</a></li>
        <li><a href="https://support.remarkable.com/s/article/About-reMarkable-Paper-Pro" rel="noopener noreferrer">reMarkable : Paper Pro</a></li>
      </ul>
    """,

    "/guides/bloc-notes-numerique-couleur-ou-noir-et-blanc/": """
      <p class="article-answer"><strong>Choisissez la couleur uniquement si elle transporte une information dont vous avez besoin : légende, correction, priorité, schéma ou catégorie.</strong> Pour du texte, des notes simples et des documents conçus en noir et blanc, un écran monochrome reste souvent suffisant.</p>

      <h2 id="difference">La couleur E Ink n'est pas celle d'une tablette classique</h2>
      <p>Les écrans E Ink sont pensés pour des contenus relativement statiques. E Ink indique par exemple que Kaleido 3 affiche jusqu'à 300 ppp en noir et blanc et 150 ppp en couleur, avec 4 096 couleurs. D'autres technologies couleur existent, comme Gallery. Il faut donc comparer la technologie et le modèle précis plutôt que parler de "l'E Ink couleur" comme d'un seul écran.</p>

      <h2 id="usages">Quand la couleur change réellement le travail</h2>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Document</th><th>Couleur utile si…</th><th>Noir et blanc suffisant si…</th></tr></thead>
        <tbody>
          <tr><td>Cours</td><td>les surlignages correspondent à des catégories</td><td>titres et annotations suffisent</td></tr>
          <tr><td>Graphiques</td><td>plusieurs séries se distinguent uniquement par leur couleur</td><td>formes, labels et textures restent explicites</td></tr>
          <tr><td>Agenda</td><td>chaque couleur encode un type d'activité</td><td>une seule hiérarchie visuelle suffit</td></tr>
          <tr><td>Photo ou création</td><td>la couleur sert de repère</td><td>si la fidélité est essentielle, préférez LCD/OLED</td></tr>
        </tbody>
      </table></div>

      <h2 id="test">Faites le test en niveaux de gris</h2>
      <p>Prenez trois documents représentatifs et affichez-les en niveaux de gris. Si deux courbes deviennent impossibles à distinguer, si une légende perd son sens ou si vos corrections ne se repèrent plus, la couleur a une fonction. Si tout reste lisible, elle est probablement secondaire dans votre décision.</p>

      <h2 id="compromis">Les compromis à vérifier sur le modèle précis</h2>
      <p>Ne déduisez pas le contraste, la définition, la saturation ou l'éclairage d'un seul mot comme "couleur". Sur Kaleido, la définition couleur diffère de la définition noir et blanc. D'autres écrans couleur utilisent une architecture différente. Vérifiez aussi ce qui arrive à la couleur après export : une annotation peut conserver sa couleur dans le fichier partagé même si son rendu à l'écran paraît plus discret.</p>

      <h2 id="decision">N'achetez pas la couleur comme une fonction décorative</h2>
      <p>Si vous pouvez nommer précisément l'information que la couleur préserve, elle mérite d'entrer dans vos critères. Sinon, comparez d'abord le contraste, la taille, le logiciel et le coût total. Si vous avez confirmé le besoin, poursuivez vers le <a href="/comparatifs/bloc-notes-numerique-couleur/">comparatif des bloc-notes numériques couleur</a>. Pour la vidéo et la création graphique fidèle, lisez plutôt <a href="/guides/tablette-classique-ou-tablette-e-ink/">tablette classique ou E Ink</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://www.eink.com/brand/detail/Kaleido3" rel="noopener noreferrer">E Ink : Kaleido 3</a></li>
        <li><a href="https://www.eink.com/tech/detail/FAQ" rel="noopener noreferrer">E Ink : familles d'encres couleur</a></li>
        <li><a href="https://support.remarkable.com/s/article/About-reMarkable-Paper-Pro" rel="noopener noreferrer">reMarkable : écran couleur Paper Pro</a></li>
      </ul>
    """,

    "/guides/bloc-notes-numerique-avec-ou-sans-abonnement/": """
      <p class="article-answer"><strong>Un bloc-notes numérique peut fonctionner sans abonnement, mais "sans abonnement" ne signifie pas la même chose selon l'écosystème.</strong> Vérifiez séparément l'écriture locale, l'accès aux notes, l'export, la synchronisation, les intégrations cloud et la reconnaissance manuscrite. Une fonction de confort payante n'a pas le même impact qu'un export essentiel.</p>

      <h2 id="questions">Les cinq fonctions à tester sans paiement récurrent</h2>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Fonction</th><th>Question à poser</th><th>Risque</th></tr></thead>
        <tbody>
          <tr><td>Notes locales</td><td>restent-elles lisibles et modifiables ?</td><td>dépendance pour l'usage de base</td></tr>
          <tr><td>Export</td><td>peut-on récupérer un PDF, une image ou du texte ?</td><td>données enfermées</td></tr>
          <tr><td>Synchronisation</td><td>quelle durée, quels appareils, quel quota ?</td><td>historique incomplet</td></tr>
          <tr><td>Cloud tiers</td><td>Google Drive, OneDrive ou Dropbox sont-ils accessibles ?</td><td>étapes manuelles</td></tr>
          <tr><td>OCR / recherche</td><td>la fonction est-elle incluse ou payante ?</td><td>coût récurrent pour une fonction de travail</td></tr>
        </tbody>
      </table></div>

      <h2 id="ecosystemes">Ce que documentent les principaux écosystèmes</h2>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Écosystème</th><th>Sans abonnement spécifique documenté</th><th>Point d'attention</th></tr></thead>
        <tbody>
          <tr><td>reMarkable</td><td>écriture locale, cloud limité et consultation/export dans les apps</td><td>Connect ajoute notamment stockage illimité, intégrations, recherche manuscrite et édition dans les apps</td></tr>
          <tr><td>Kindle Scribe 2025+</td><td>connexions Google Drive et OneDrive avec compte Amazon et compte cloud</td><td>certaines fonctions dépendent de la génération du Scribe, pas d'un abonnement Kindle dédié</td></tr>
          <tr><td>Kobo compatibles stylet</td><td>carnets locaux, sauvegarde Kobo, Google Drive/Dropbox sur certains modèles</td><td>fonctions différentes selon modèles et types de carnets</td></tr>
          <tr><td>BOOX</td><td>stockage tiers intégré et export local</td><td>la synchronisation des notes BOOX utilise le compte ONYX ; les services tiers ont leur propre fonctionnement</td></tr>
          <tr><td>Supernote</td><td>Supernote Cloud, Dropbox, Google Drive et OneDrive documentés</td><td>il faut choisir et configurer le service de synchronisation</td></tr>
        </tbody>
      </table></div>

      <h2 id="remarkable">Pourquoi reMarkable demande une analyse séparée</h2>
      <p>Connect est un abonnement explicite. reMarkable indique qu'il ajoute notamment le stockage cloud illimité, les intégrations, la recherche dans l'écriture et l'édition dans les applications. Sans Connect, les documents peuvent encore se synchroniser, mais les fichiers qui n'ont pas été ouverts et synchronisés depuis plus de 50 jours cessent d'être disponibles dans les applications compagnon. L'appareil conserve ses notes localement.</p>
      <p>Le bon raisonnement n'est donc pas "abonnement = appareil inutilisable", mais "quelles fonctions de mon flux dépendent réellement de Connect ?".</p>

      <h2 id="sortie">Préparez un plan de sortie des données</h2>
      <p>Avant l'achat, exportez mentalement un carnet important : dans quel format le récupérez-vous, où le sauvegardez-vous et pouvez-vous encore le lire sans le service du fabricant ? Cette question protège mieux contre la dépendance qu'une simple case "sans abonnement".</p>

      <h2 id="decision">La règle de décision</h2>
      <p>Simulez une semaine sans formule payante. Si une tâche essentielle disparaît, ajoutez son coût au <a href="/guides/prix-bloc-notes-numerique/">budget total</a> ou choisissez un autre écosystème. Si seules des fonctions de confort sont concernées, l'abonnement peut rester optionnel. Pour passer au choix de modèles, consultez le <a href="/comparatifs/bloc-notes-numerique-sans-abonnement/">comparatif des bloc-notes sans abonnement</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/articles/Knowledge/About-Connect-Subscription" rel="noopener noreferrer">reMarkable : Connect</a></li>
        <li><a href="https://support.remarkable.com/articles/Knowledge/Pair-your-reMarkable-with-the-cloud" rel="noopener noreferrer">reMarkable : cloud sans Connect</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/Tuar1obhcxaS8hVUKd" rel="noopener noreferrer">Amazon : connexions cloud Kindle Scribe</a></li>
        <li><a href="https://help.kobo.com/hc/en-us/articles/360062226733-Use-your-Kobo-eReader-as-a-notebook" rel="noopener noreferrer">Kobo : carnets et sauvegarde</a></li>
        <li><a href="https://help.boox.com/hc/en-us/articles/8569457124628-Integrated-Third-Party-Cloud-Storage" rel="noopener noreferrer">BOOX : cloud tiers</a></li>
        <li><a href="https://support.supernote.com/en_US/transfer-files" rel="noopener noreferrer">Supernote : cloud et transfert</a></li>
      </ul>
    """,

    "/guides/tablette-e-ink/": """
      <p class="article-answer"><strong>Une tablette E Ink est un appareil à écran d'encre électronique conçu avant tout pour afficher des contenus statiques avec une consommation faible entre les rafraîchissements.</strong> Elle devient intéressante pour lire, écrire et annoter des documents ; elle est moins adaptée aux usages qui exigent vidéo, animations ou interactions très rapides.</p>

      <h2 id="definition">Qu'est-ce qu'une tablette E Ink ?</h2>
      <p>E Ink désigne une technologie d'affichage électrophorétique. Contrairement à un écran LCD ou OLED, l'image est réfléchie par la lumière ambiante au lieu d'être produite par un rétroéclairage. La dalle conserve aussi son image sans alimentation continue : cette propriété est appelée bistabilité.</p>

      <h2 id="familles">Toutes les tablettes E Ink ne se ressemblent pas</h2>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Famille</th><th>Orientation</th><th>Exemples d'écosystèmes</th></tr></thead>
        <tbody>
          <tr><td>Liseuse avec stylet</td><td>lecture d'abord, écriture ensuite</td><td>Kindle Scribe, Kobo Elipsa</td></tr>
          <tr><td>Bloc-notes spécialisé</td><td>carnets, PDF, concentration</td><td>reMarkable, Supernote</td></tr>
          <tr><td>Tablette E Ink Android</td><td>applications et fichiers plus ouverts</td><td>BOOX</td></tr>
          <tr><td>Modèle couleur</td><td>schémas, surlignage, documents colorés</td><td>plusieurs technologies E Ink couleur</td></tr>
        </tbody>
      </table></div>

      <h2 id="avantages">Pourquoi l'E Ink est efficace sur des pages statiques</h2>
      <p>E Ink indique que ses écrans sont bistables : l'énergie est surtout utilisée lorsque l'image change. Le texte ou le dessin peut rester affiché sans rafraîchissement permanent. Cette propriété explique une partie de l'autonomie des liseuses et tablettes E Ink, mais elle ne permet pas de comparer directement deux appareils : processeur, Wi-Fi, éclairage et logiciel consomment également de l'énergie.</p>

      <h2 id="limites">Les limites à accepter</h2>
      <p>Le rafraîchissement est plus lent qu'un écran classique et peut laisser des traces résiduelles jusqu'à un rafraîchissement complet. La vidéo n'est donc pas l'usage naturel de la technologie. Sur les modèles couleur, le rendu et la définition peuvent aussi différer du noir et blanc. Enfin, le logiciel compte autant que la dalle : une tablette spécialisée et une tablette Android peuvent utiliser de l'E Ink tout en offrant des expériences très différentes.</p>

      <h2 id="choisir">Quand choisir une tablette E Ink ?</h2>
      <p>Examinez l'E Ink si vous remplacez surtout des cahiers, des articles, des contrats ou des livres. Si votre appareil doit aussi gérer visioconférence, vidéo, création visuelle ou applications très animées, lisez la comparaison <a href="/guides/tablette-classique-ou-tablette-e-ink/">tablette classique ou E Ink</a>. Pour comprendre le mécanisme physique, poursuivez avec <a href="/guides/encre-electronique-fonctionnement/">le fonctionnement de l'encre électronique</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://www.eink.com/tech/detail/FAQ" rel="noopener noreferrer">E Ink : définition et familles de technologies</a></li>
        <li><a href="https://www.eink.com/tech/detail/Benefits" rel="noopener noreferrer">E Ink : bistabilité et affichage réfléchissant</a></li>
        <li><a href="https://www.eink.com/tech/detail/How_it_works" rel="noopener noreferrer">E Ink : modes de mise à jour</a></li>
      </ul>
    """,

    "/guides/encre-electronique-fonctionnement/": """
      <p class="article-answer"><strong>L'encre électronique E Ink fonctionne en déplaçant des particules chargées dans de minuscules capsules ou cellules sous l'effet d'un champ électrique.</strong> Une fois les particules positionnées, l'image reste visible sans alimentation continue. C'est ce mécanisme qui permet un affichage réfléchissant et bistable.</p>

      <h2 id="capsules">Des particules noires et blanches qui se déplacent</h2>
      <p>Dans les systèmes noir et blanc décrits par E Ink, chaque microcapsule ou Microcup contient des particules blanches et noires portant des charges opposées. Une tension attire l'une ou l'autre couleur vers la surface. Le lecteur voit alors un point clair ou sombre. Des millions de zones commandées forment le texte et les images.</p>

      <h2 id="couches">L'encre n'est qu'une couche de l'écran</h2>
      <p>Le film d'encre est laminé sur une couche de circuits qui crée les champs électriques nécessaires. Un module complet comprend aussi le TFT, des couches de protection, l'électronique de pilotage et les connecteurs. Une tablette E Ink ne se résume donc pas à "de l'encre" : la couche tactile, le stylet et le logiciel participent aussi à l'expérience.</p>

      <h2 id="bistabilite">Pourquoi l'image reste sans consommer en continu</h2>
      <p>La technologie est bistable. Une fois les particules en place, elles peuvent maintenir l'image sans que l'écran soit constamment alimenté. La consommation intervient principalement lors des changements d'image. Cela ne signifie pas que l'appareil entier ne consomme rien : processeur, réseau, stockage et éclairage frontal restent alimentés selon l'usage.</p>

      <h2 id="rafraichissement">Pourquoi les rafraîchissements sont visibles</h2>
      <p>Déplacer les particules prend plus de temps que modifier les pixels d'un LCD ou d'un OLED. E Ink propose plusieurs modes de mise à jour ; certains sont plus rapides au prix d'un rendu ou d'une efficacité énergétique différents. Les traces résiduelles observées avant un rafraîchissement complet viennent de ce compromis de pilotage, pas d'une image "gravée" définitivement.</p>

      <h2 id="couleur">Comment obtient-on de la couleur ?</h2>
      <p>E Ink commercialise plusieurs familles couleur. Kaleido utilise une approche différente de Gallery, et leurs caractéristiques ne doivent pas être mélangées. Dans les systèmes couleur à particules multiples, différentes particules chargées peuvent être positionnées pour produire les teintes visibles. Pour choisir un appareil, consultez les spécifications du modèle plutôt que de généraliser à partir du terme "E Ink couleur".</p>

      <h2 id="suite">Ce que ce fonctionnement change pour l'utilisateur</h2>
      <p>Il explique trois propriétés concrètes : une page reste visible sans rafraîchissement permanent, l'écran utilise la lumière ambiante, et les changements d'image sont moins immédiats que sur une tablette classique. Pour l'impact sur l'écriture, consultez <a href="/guides/latence-ecriture/">le guide sur la latence</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://www.eink.com/tech/detail/FAQ" rel="noopener noreferrer">E Ink : microcapsules, Microcups et charges</a></li>
        <li><a href="https://www.eink.com/tech/detail/Electronic_Ink_Film" rel="noopener noreferrer">E Ink : film d'encre et couches du module</a></li>
        <li><a href="https://www.eink.com/tech/detail/Benefits" rel="noopener noreferrer">E Ink : bistabilité</a></li>
      </ul>
    """,

    "/guides/latence-ecriture/": """
      <p class="article-answer"><strong>La latence d'écriture est le délai entre le mouvement du stylet et l'apparition du trait à l'écran.</strong> Elle ne dépend pas d'un seul chiffre : numériseur, traitement du stylet, logiciel de dessin, mode de rafraîchissement et écran participent tous à la sensation finale.</p>

      <h2 id="chaine">La latence est une chaîne complète</h2>
      <p>Le stylet doit d'abord être détecté, sa position interprétée, le trait calculé puis affiché. Un fabricant peut optimiser une partie de cette chaîne sans modifier la technologie d'encre elle-même. C'est pourquoi deux appareils utilisant de l'E Ink peuvent donner une sensation d'écriture différente.</p>

      <h2 id="eink">Le rafraîchissement E Ink n'est qu'un maillon</h2>
      <p>E Ink indique que ses écrans disposent de plusieurs modes de mise à jour, avec des temps et compromis différents. Les modes rapides servent aux interactions plus fréquentes ; les rafraîchissements complets réduisent les résidus visuels. Pour l'écriture, les fabricants utilisent donc des stratégies de rendu qui privilégient la réactivité du trait avant le nettoyage complet de la page.</p>

      <h2 id="mesures">Pourquoi un chiffre de latence ne suffit pas</h2>
      <p>Un nombre annoncé par un fabricant ou mesuré par un test n'est comparable que si la méthode est identique : point de départ du chronométrage, stylet, application, fréquence d'échantillonnage, caméra et version logicielle. Sans protocole commun, classer des appareils sur quelques millisecondes donne une précision trompeuse.</p>

      <h2 id="verifier">Ce qu'il faut vérifier en pratique</h2>
      <ul>
        <li>le trait suit-il suffisamment votre main pour votre vitesse d'écriture ?</li>
        <li>les hachures, petits caractères et signatures restent-ils contrôlables ?</li>
        <li>les rafraîchissements complets interrompent-ils votre rythme ?</li>
        <li>l'expérience reste-t-elle correcte dans l'application que vous utiliserez réellement ?</li>
      </ul>
      <p>Ces questions nécessitent idéalement un essai direct. Sans test contrôlé, il est plus rigoureux de documenter le fonctionnement et les modes disponibles que de promettre une sensation "papier".</p>

      <h2 id="decision">Quand la latence doit-elle devenir un critère prioritaire ?</h2>
      <p>Elle compte surtout si vous écrivez vite, dessinez, faites des schémas détaillés ou signez fréquemment. Pour de la lecture et des annotations ponctuelles, les contraintes de fichiers et d'export peuvent être plus importantes. Retrouvez ces critères dans le guide <a href="/guides/choisir-bloc-notes-numerique/">comment choisir son bloc-notes numérique</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://www.eink.com/tech/detail/How_it_works" rel="noopener noreferrer">E Ink : modes et temps de mise à jour</a></li>
        <li><a href="https://www.eink.com/tech/detail/FAQ" rel="noopener noreferrer">E Ink : fonctionnement des modules</a></li>
      </ul>
    """,

    "/guides/ocr-manuscrit/": """
      <p class="article-answer"><strong>L'OCR manuscrit transforme une écriture en texte exploitable, mais trois fonctions différentes sont souvent confondues : convertir une page en texte, rendre l'écriture recherchable et extraire du texte vers un fichier.</strong> Vérifiez laquelle vous utilisez réellement avant de comparer les appareils.</p>

      <h2 id="types">Trois fonctions derrière le mot OCR</h2>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Fonction</th><th>Résultat</th><th>Usage</th></tr></thead>
        <tbody>
          <tr><td>Conversion</td><td>l'écriture devient du texte éditable</td><td>compte rendu, document Word, email</td></tr>
          <tr><td>Recherche manuscrite</td><td>l'appareil indexe l'écriture reconnue</td><td>retrouver un mot dans des carnets</td></tr>
          <tr><td>PDF recherchable</td><td>l'écriture reste visuelle mais reçoit une couche texte</td><td>archivage et recherche sur ordinateur</td></tr>
        </tbody>
      </table></div>

      <h2 id="ecosystemes">Les approches diffèrent selon les fabricants</h2>
      <p>reMarkable peut convertir plusieurs pages manuscrites en texte et exporter le résultat par email ou vers des services cloud. Supernote propose des notes à reconnaissance en temps réel et exporte les résultats en TXT ou DOCX. BOOX permet de convertir une sélection manuscrite en texte et de l'éditer ou la partager. Kobo réserve la conversion aux carnets avancés. Kindle Scribe peut convertir les carnets en texte et produire, sur les modèles récents, des PDF recherchables.</p>

      <h2 id="precision">La précision dépend aussi de votre écriture</h2>
      <p>Langue, taille des caractères, écriture cursive, mise en page, symboles et équations influencent le résultat. Amazon précise par exemple que certains contenus comme dessins, diagrammes et équations ne sont pas pris en charge par sa conversion manuscrite. Kobo demande d'écrire dans les lignes d'un carnet avancé pour faciliter la reconnaissance.</p>

      <h2 id="connexion">En ligne ou hors ligne ?</h2>
      <p>Le besoin de connexion varie selon l'écosystème et la fonction. BOOX indique qu'une connexion Wi-Fi est nécessaire pour certaines opérations de reconnaissance et pour télécharger des langues. Supernote précise qu'une activation initiale en ligne peut être nécessaire avant l'usage hors ligne de certaines fonctions. Il faut donc vérifier les conditions du modèle et de la version logicielle plutôt que supposer que tout OCR fonctionne localement.</p>

      <h2 id="test">Le bon test avant achat</h2>
      <p>Écrivez une page typique avec titres, abréviations, mots techniques et corrections. Vérifiez ensuite ce que vous récupérez : texte éditable, PDF recherchable ou simple image. Si votre objectif principal est de transformer vos carnets en documents, consultez aussi <a href="/guides/convertir-notes-manuscrites-en-texte/">le guide de conversion des notes manuscrites</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/articles/Knowledge/Convert-handwritten-notes-into-text" rel="noopener noreferrer">reMarkable : conversion manuscrite</a></li>
        <li><a href="https://support.supernote.com/handwriting-recognition" rel="noopener noreferrer">Supernote : reconnaissance et export TXT/DOCX</a></li>
        <li><a href="https://help.boox.com/hc/en-us/articles/10701578837268-Handwritten-Notes" rel="noopener noreferrer">BOOX : reconnaissance manuscrite</a></li>
        <li><a href="https://help.kobo.com/hc/fr/articles/360062226733-Utiliser-votre-liseuse-Kobo-comme-un-carnet" rel="noopener noreferrer">Kobo : carnets avancés</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/TWTo0OyovlJ9jwOV0B" rel="noopener noreferrer">Amazon : limites de la reconnaissance Kindle Scribe</a></li>
      </ul>
    """,

    "/guides/autonomie-tablette-e-ink/": """
      <p class="article-answer"><strong>L'E Ink réduit la consommation de l'écran lorsque l'image reste statique, mais l'autonomie réelle d'une tablette dépend surtout de ce que vous faites entre deux pages.</strong> Wi-Fi, éclairage, synchronisation, processeur, fréquence d'écriture et applications rendent les promesses "en semaines" difficiles à comparer directement.</p>

      <h2 id="bistabilite">Pourquoi l'E Ink peut consommer peu à l'affichage</h2>
      <p>E Ink décrit ses écrans comme bistables : une image peut rester visible sans alimentation continue. L'énergie est principalement utilisée lors des changements d'image. Cette propriété favorise les usages de lecture statique, mais elle ne couvre qu'une partie de la consommation totale d'un appareil.</p>

      <h2 id="facteurs">Ce qui réduit l'autonomie</h2>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Facteur</th><th>Pourquoi il compte</th></tr></thead>
        <tbody>
          <tr><td>Éclairage frontal</td><td>les LED consomment tant qu'elles sont allumées</td></tr>
          <tr><td>Wi-Fi et cloud</td><td>synchronisation et transferts sollicitent réseau et processeur</td></tr>
          <tr><td>Écriture fréquente</td><td>le trait oblige l'écran et le système à actualiser souvent</td></tr>
          <tr><td>Applications Android</td><td>certaines tâches sollicitent davantage CPU, mémoire et réseau</td></tr>
          <tr><td>Rafraîchissements rapides</td><td>les interactions fréquentes réduisent l'avantage du contenu statique</td></tr>
        </tbody>
      </table></div>

      <h2 id="semaines">Pourquoi "plusieurs semaines" ne suffit pas</h2>
      <p>Une autonomie annoncée en semaines dépend d'un scénario : durée quotidienne d'utilisation, nombre de pages, éclairage, Wi-Fi et veille. Deux fabricants peuvent annoncer la même durée avec des hypothèses différentes. Sans protocole commun, convertir ces chiffres en classement est trompeur.</p>

      <h2 id="protocole">Comment comparer proprement deux modèles</h2>
      <ol>
        <li>Fixez une durée quotidienne d'écriture et de lecture.</li>
        <li>Utilisez le même niveau d'éclairage ou désactivez-le.</li>
        <li>Gardez le Wi-Fi dans le même état.</li>
        <li>Notez la fréquence de synchronisation.</li>
        <li>Comparez la baisse de batterie sur plusieurs jours plutôt qu'une seule session.</li>
      </ol>
      <p>Sans test direct, utilisez l'autonomie annoncée comme repère interne à une gamme et concentrez votre décision sur les fonctions vérifiables.</p>

      <h2 id="decision">Quand l'autonomie doit-elle décider ?</h2>
      <p>Elle devient prioritaire si vous travaillez loin d'une prise pendant plusieurs jours. Pour un usage de bureau, un mauvais flux de fichiers ou un écran inadapté pénalisera souvent davantage que quelques recharges supplémentaires. Replacez donc l'autonomie dans la méthode générale pour <a href="/guides/choisir-bloc-notes-numerique/">choisir un bloc-notes numérique</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://www.eink.com/tech/detail/Benefits" rel="noopener noreferrer">E Ink : bistabilité et consommation de l'affichage</a></li>
        <li><a href="https://www.eink.com/tech/detail/How_it_works" rel="noopener noreferrer">E Ink : modes de rafraîchissement</a></li>
      </ul>
    """,

    "/guides/formats-fichiers-compatibles/": """
      <p class="article-answer"><strong>PDF et EPUB sont les formats les plus largement partagés entre les grands écosystèmes E Ink, mais la compatibilité ne garantit pas les mêmes fonctions d'annotation, d'export ou de DRM.</strong> Pour choisir, vérifiez votre format principal et ce que l'appareil permet d'en faire après import.</p>

      <h2 id="tableau">Formats : les grandes différences par écosystème</h2>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Écosystème</th><th>Formats documentaires utiles à connaître</th><th>Attention</th></tr></thead>
        <tbody>
          <tr><td>reMarkable</td><td>PDF, EPUB ; import web JPG/PNG converti en PDF</td><td>les formats d'export diffèrent des formats d'import</td></tr>
          <tr><td>Kobo</td><td>EPUB, PDF, MOBI, TXT, HTML, RTF, CBZ/CBR et images</td><td>DRM et annotations limitent certaines opérations</td></tr>
          <tr><td>Kindle Scribe</td><td>PDF, DOC/DOCX, TXT, RTF, HTML, images, EPUB via services d'import</td><td>le traitement dépend de Send to Kindle ou du cloud</td></tr>
          <tr><td>BOOX</td><td>PDF et nombreux formats réajustables dont EPUB, DOC/DOCX, HTML, MOBI, RTF, TXT</td><td>lecture possible ne signifie pas édition complète</td></tr>
          <tr><td>Supernote</td><td>PDF, EPUB et documents Word parmi les formats de travail documentés</td><td>certaines fonctions varient selon le type de document</td></tr>
        </tbody>
      </table></div>

      <h2 id="pdf">PDF : format fixe, fonctions variables</h2>
      <p>Le PDF conserve sa mise en page. C'est utile pour contrats, articles et formulaires, mais la taille de l'écran compte davantage. Les annotations peuvent aussi être intégrées différemment lors de l'export. Kobo précise par exemple que les PDF non protégés peuvent être exportés avec les annotations manuscrites, alors que les restrictions sont différentes pour les EPUB.</p>

      <h2 id="epub">EPUB : plus souple pour la lecture</h2>
      <p>EPUB est un format de livre réajustable. Le texte peut changer de taille et se redistribuer, mais les fonctions d'écriture dépendent du fabricant. Une mention "EPUB compatible" ne vous dit donc pas si vos annotations seront exportables.</p>

      <h2 id="drm">Ne confondez pas format et droits numériques</h2>
      <p>Un fichier peut avoir une extension compatible tout en restant protégé par DRM. Kobo distingue par exemple Adobe DRM et Social DRM et impose Adobe Digital Editions dans certains cas. Les possibilités d'annotation et de transfert peuvent alors être différentes d'un PDF ou EPUB personnel non protégé.</p>

      <h2 id="test">Le test qui évite les mauvaises surprises</h2>
      <p>Prenez trois fichiers réels : votre PDF le plus complexe, un ebook et un document de travail. Vérifiez import, affichage, annotation et export. Si vous ne récupérez pas le résultat dans le format voulu, la simple compatibilité d'ouverture ne suffit pas. Poursuivez avec <a href="/guides/exporter-notes/">le guide d'export des notes</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files" rel="noopener noreferrer">reMarkable : formats d'import et d'export</a></li>
        <li><a href="https://help.kobo.com/hc/fr/articles/360017763713-Formats-de-fichiers-pris-en-charge-par-votre-application-Kobo-eReader-et-Kobo-Books" rel="noopener noreferrer">Kobo : formats pris en charge</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/TIh9JOMGAKr7bY4zqu" rel="noopener noreferrer">Amazon : formats compatibles via cloud drive</a></li>
        <li><a href="https://help.boox.com/hc/en-us/articles/25400769451540-Adjust-EPUB-and-Similar" rel="noopener noreferrer">BOOX : formats réajustables</a></li>
        <li><a href="https://support.supernote.com/en_US/epub-and-pdf-documents" rel="noopener noreferrer">Supernote : EPUB et PDF</a></li>
      </ul>
    """,

    "/guides/exporter-notes/": """
      <p class="article-answer"><strong>Pour exporter des notes, choisissez d'abord le résultat final dont vous avez besoin : PDF fidèle au manuscrit, image, texte éditable ou format natif de sauvegarde.</strong> Les fabricants proposent plusieurs sorties, mais elles ne servent pas au même objectif.</p>

      <h2 id="formats">Quel format d'export choisir ?</h2>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Format</th><th>À privilégier pour</th><th>Limite</th></tr></thead>
        <tbody>
          <tr><td>PDF</td><td>partage, impression, archivage visuel</td><td>édition du manuscrit limitée</td></tr>
          <tr><td>PNG/JPG</td><td>une page, une illustration, insertion rapide</td><td>pas de structure de document</td></tr>
          <tr><td>TXT/DOCX</td><td>texte reconnu et réutilisable</td><td>la mise en page manuscrite n'est pas conservée à l'identique</td></tr>
          <tr><td>Format natif</td><td>sauvegarde et restauration dans le même écosystème</td><td>dépendance au fabricant</td></tr>
        </tbody>
      </table></div>

      <h2 id="remarkable">reMarkable</h2>
      <p>reMarkable documente l'export en PDF, PNG et SVG depuis ses applications, ainsi que l'envoi de texte pour certains contenus. Les fichiers peuvent aussi être envoyés vers Google Drive, Dropbox ou OneDrive. Une interface USB permet d'importer et télécharger des documents sans passer uniquement par les applications cloud.</p>

      <h2 id="autres">Kindle Scribe, Kobo, BOOX et Supernote</h2>
      <p>Kindle Scribe peut partager carnets et documents par email ; les modèles récents peuvent aussi envoyer vers Google Drive et OneDrive, avec choix entre PDF manuscrit, texte ou PDF recherchable selon le contenu. Kobo exporte ses carnets, notamment vers Dropbox, avec des options différentes entre carnets de base et avancés. BOOX exporte les notes manuscrites en PNG, PDF ou format .note. Supernote exporte les pages de notes en PNG/PDF et peut produire TXT ou DOCX après reconnaissance.</p>

      <h2 id="durable">Préservez un format durable</h2>
      <p>Si vos notes ont une valeur professionnelle ou personnelle à long terme, gardez au moins une copie dans un format lisible en dehors de l'appareil. Un PDF est souvent adapté à l'archive visuelle ; un DOCX ou TXT convient mieux si le contenu doit être retravaillé. Le format natif reste utile pour restaurer l'édition complète, mais ne devrait pas être votre seule sauvegarde.</p>

      <h2 id="test">Testez l'export avant d'accumuler des centaines de pages</h2>
      <ol>
        <li>Créez deux pages avec écriture, surlignage et dessin.</li>
        <li>Exportez-les dans le format prévu.</li>
        <li>Ouvrez le fichier sur ordinateur et téléphone.</li>
        <li>Vérifiez couleurs, lisibilité, recherche et poids du fichier.</li>
      </ol>
      <p>Pour le transfert lui-même, consultez <a href="/guides/transfert-notes-vers-ordinateur/">transférer ses notes vers l'ordinateur</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files" rel="noopener noreferrer">reMarkable : import et export</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/TJE2UYmdw0ppUuR3Rs" rel="noopener noreferrer">Amazon : partage Kindle Scribe</a></li>
        <li><a href="https://help.kobo.com/hc/en-us/articles/360062226733-Use-your-Kobo-eReader-as-a-notebook" rel="noopener noreferrer">Kobo : export de carnets</a></li>
        <li><a href="https://help.boox.com/hc/en-us/articles/8569373888788-Handwritten-Notes" rel="noopener noreferrer">BOOX : export PNG/PDF/.note</a></li>
        <li><a href="https://support.supernote.com/en_US/introduction-to-the-toolbar" rel="noopener noreferrer">Supernote : formats d'export des notes</a></li>
      </ul>
    """,

    "/guides/synchroniser-notes-cloud/": """
      <p class="article-answer"><strong>Synchroniser des notes ne signifie pas simplement les copier dans le cloud.</strong> Une vraie synchronisation maintient plusieurs appareils ou applications au même état ; un export vers Google Drive, OneDrive ou Dropbox crée parfois seulement une copie. Vérifiez cette différence avant de construire votre flux de travail.</p>

      <h2 id="trois">Trois opérations souvent confondues</h2>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Opération</th><th>Ce qui se passe</th></tr></thead>
        <tbody>
          <tr><td>Synchronisation</td><td>les mêmes notes ou fichiers se mettent à jour entre appareils</td></tr>
          <tr><td>Import cloud</td><td>une copie d'un fichier distant est téléchargée sur la tablette</td></tr>
          <tr><td>Export cloud</td><td>une nouvelle copie est envoyée vers le service distant</td></tr>
        </tbody>
      </table></div>

      <h2 id="remarkable">reMarkable</h2>
      <p>Les fichiers reMarkable se synchronisent via le cloud du fabricant vers les applications compagnon. Sans Connect, la synchronisation est limitée pour les documents restés inactifs plus de 50 jours. Google Drive, Dropbox et OneDrive servent aussi d'intégrations pour parcourir, copier et envoyer des fichiers ; il ne faut pas confondre ces intégrations avec le cloud natif reMarkable.</p>

      <h2 id="boox-supernote">BOOX et Supernote</h2>
      <p>BOOX synchronise ses notes via le compte ONYX et propose en parallèle des stockages tiers intégrés comme Google Drive, OneDrive et Dropbox. Supernote permet de sélectionner un service de synchronisation parmi Supernote Cloud et plusieurs clouds tiers, puis de choisir les dossiers concernés.</p>

      <h2 id="kindle-kobo">Kindle Scribe et Kobo</h2>
      <p>Les Kindle Scribe récents peuvent importer des fichiers depuis Google Drive ou OneDrive et renvoyer des copies annotées. Amazon précise que les annotations d'un document importé ne se resynchronisent pas automatiquement vers le fichier d'origine. Kobo peut accéder à Google Drive ou Dropbox sur certains modèles et sauvegarde aussi les carnets dans son propre environnement. Là encore, import/export et synchronisation continue ne sont pas synonymes.</p>

      <h2 id="choisir">Choisissez selon votre source de vérité</h2>
      <p>Décidez quel emplacement contient la version de référence : la tablette, le cloud du fabricant ou votre Drive d'entreprise. Si deux services peuvent modifier le même document sans synchronisation bidirectionnelle, les doublons deviennent probables. Pour une intégration précise, consultez les guides <a href="/guides/bloc-notes-numerique-google-drive/">Google Drive</a>, <a href="/guides/bloc-notes-numerique-onedrive/">OneDrive</a> et <a href="/guides/bloc-notes-numerique-dropbox/">Dropbox</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files" rel="noopener noreferrer">reMarkable : sync et intégrations</a></li>
        <li><a href="https://help.boox.com/hc/en-us/articles/25401889318548-Note-Syncing" rel="noopener noreferrer">BOOX : synchronisation des notes</a></li>
        <li><a href="https://support.supernote.com/en_US/transfer-files" rel="noopener noreferrer">Supernote : services cloud</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/TjrMJmg3DZpAQLwVuN" rel="noopener noreferrer">Amazon : import cloud Kindle Scribe</a></li>
        <li><a href="https://help.kobo.com/hc/en-us/articles/15335985512983-Add-books-to-your-eReader-using-Google-Drive" rel="noopener noreferrer">Kobo : Google Drive</a></li>
      </ul>
    """,

    "/guides/bloc-notes-numerique-google-drive/": """
      <p class="article-answer"><strong>Google Drive est utilisable avec plusieurs familles de bloc-notes numériques, mais pas toujours comme une synchronisation bidirectionnelle.</strong> reMarkable, BOOX, certains Kobo, Supernote et les Kindle Scribe sortis en 2025 ou après proposent désormais des formes d'accès, d'import ou d'export vers Google Drive.</p>

      <h2 id="comparaison">Google Drive selon l'écosystème</h2>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Écosystème</th><th>Fonction documentée</th><th>À retenir</th></tr></thead>
        <tbody>
          <tr><td>reMarkable</td><td>parcourir, copier depuis Drive et envoyer des fichiers vers Drive</td><td>intégration distincte du cloud natif reMarkable</td></tr>
          <tr><td>BOOX</td><td>stockage tiers intégré, téléchargement et envoi de documents</td><td>plusieurs comptes et services peuvent coexister</td></tr>
          <tr><td>Kobo compatibles</td><td>ajout de PDF/EPUB non protégés depuis Drive</td><td>fonction limitée à certains modèles</td></tr>
          <tr><td>Supernote</td><td>synchronisation de dossiers sélectionnés</td><td>Google Drive peut être choisi comme service de sync</td></tr>
          <tr><td>Kindle Scribe 2025+</td><td>import de fichiers et partage de copies vers Drive</td><td>les annotations ne modifient pas automatiquement le fichier source</td></tr>
        </tbody>
      </table></div>

      <h2 id="attention">Le piège principal : croire que le PDF source se met à jour</h2>
      <p>Sur Kindle Scribe, Amazon précise explicitement qu'un fichier importé depuis Drive est copié sur l'appareil ; après annotation, il faut renvoyer une nouvelle copie vers le cloud. Cette distinction existe aussi dans d'autres écosystèmes selon le type de fichier. Avant l'achat, vérifiez si votre workflow exige une vraie synchronisation ou seulement un aller-retour de documents.</p>

      <h2 id="workflow">Un workflow simple et robuste</h2>
      <ol>
        <li>Conservez un dossier Drive dédié aux documents à annoter.</li>
        <li>Importez ou ouvrez une copie sur la tablette.</li>
        <li>Après annotation, exportez vers un dossier distinct "annotés".</li>
        <li>N'écrasez le fichier source que si vous êtes certain du comportement de l'écosystème.</li>
      </ol>

      <h2 id="choix">Google Drive est-il un critère éliminatoire ?</h2>
      <p>Oui si votre organisation centralise tous les documents dans Drive. Mais vérifiez le détail : accès aux fichiers, formats acceptés, comptes professionnels et sens de la synchronisation. Pour comparer avec d'autres services, consultez <a href="/guides/synchroniser-notes-cloud/">le guide de synchronisation cloud</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/articles/Knowledge/About-my-remarkable-com" rel="noopener noreferrer">reMarkable : intégration Google Drive</a></li>
        <li><a href="https://help.boox.com/hc/en-us/articles/8569457124628-Integrated-Third-Party-Cloud-Storage" rel="noopener noreferrer">BOOX : Google Drive intégré</a></li>
        <li><a href="https://help.kobo.com/hc/en-us/articles/15335985512983-Add-books-to-your-eReader-using-Google-Drive" rel="noopener noreferrer">Kobo : Google Drive</a></li>
        <li><a href="https://support.supernote.com/en_US/transfer-files" rel="noopener noreferrer">Supernote : Google Drive</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/TjrMJmg3DZpAQLwVuN" rel="noopener noreferrer">Amazon : import depuis Google Drive</a></li>
      </ul>
    """,

    "/guides/bloc-notes-numerique-onedrive/": """
      <p class="article-answer"><strong>OneDrive est aujourd'hui compatible avec plusieurs écosystèmes E Ink, notamment reMarkable, BOOX, Supernote et les Kindle Scribe sortis en 2025 ou après.</strong> La fonction peut toutefois être un import/export de fichiers plutôt qu'une édition synchronisée du document source.</p>

      <h2 id="comparaison">OneDrive selon l'écosystème</h2>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Écosystème</th><th>Fonction principale</th><th>Attention</th></tr></thead>
        <tbody>
          <tr><td>reMarkable</td><td>parcourir OneDrive, copier des fichiers, envoyer des notes et documents</td><td>certaines fonctions d'intégration sont associées à Connect</td></tr>
          <tr><td>BOOX</td><td>OneDrive fait partie des stockages tiers intégrés</td><td>l'usage des fichiers et la sync des notes restent deux mécanismes</td></tr>
          <tr><td>Supernote</td><td>OneDrive peut être choisi pour synchroniser des dossiers</td><td>configuration et sélection de dossiers nécessaires</td></tr>
          <tr><td>Kindle Scribe 2025+</td><td>import et partage vers Microsoft OneDrive</td><td>une copie annotée est envoyée, le fichier source n'est pas modifié en direct</td></tr>
        </tbody>
      </table></div>

      <h2 id="entreprise">Compte Microsoft 365 professionnel : vérifiez les politiques IT</h2>
      <p>Amazon indique que l'accès à un drive professionnel dépend des paramètres de sécurité de l'entreprise. Cette prudence vaut plus largement pour les appareils personnels connectés à Microsoft 365 : authentification, politiques de conformité et autorisations peuvent bloquer une intégration pourtant compatible en théorie.</p>

      <h2 id="workflow">Le bon test avant achat</h2>
      <p>Connectez un compte de test si possible, importez un PDF, annotez-le puis renvoyez-le vers OneDrive. Vérifiez le dossier de destination, le nom du fichier et le comportement en cas de nouvelle version. Si votre processus exige une édition bidirectionnelle instantanée, une simple fonction d'import/export ne suffit pas.</p>

      <h2 id="decision">Quand OneDrive doit-il guider le choix ?</h2>
      <p>Il devient prioritaire dans un environnement Microsoft centré sur SharePoint/OneDrive et Office. Dans ce cas, ajoutez aussi à vos critères l'export PDF, les comptes d'entreprise et les politiques IT. Pour la vue globale, consultez <a href="/guides/synchroniser-notes-cloud/">synchroniser ses notes dans le cloud</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/articles/Knowledge/About-my-remarkable-com" rel="noopener noreferrer">reMarkable : OneDrive</a></li>
        <li><a href="https://help.boox.com/hc/en-us/articles/8569457124628-Integrated-Third-Party-Cloud-Storage" rel="noopener noreferrer">BOOX : OneDrive intégré</a></li>
        <li><a href="https://support.supernote.com/en_US/Whats-New/utilize-onedrive-your-new-cloud-sync-option-for-file-backup" rel="noopener noreferrer">Supernote : synchronisation OneDrive</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/TP8wuaQilIlwlITVTL" rel="noopener noreferrer">Amazon : partage Kindle Scribe vers OneDrive</a></li>
      </ul>
    """,

    "/guides/bloc-notes-numerique-dropbox/": """
      <p class="article-answer"><strong>Dropbox est l'une des intégrations cloud les plus répandues sur les appareils de prise de notes E Ink.</strong> reMarkable, BOOX, Kobo et Supernote proposent tous des fonctions documentées autour de Dropbox, mais elles vont de l'import/export de fichiers à la synchronisation de dossiers.</p>

      <h2 id="comparaison">Dropbox selon l'écosystème</h2>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Écosystème</th><th>Fonction documentée</th></tr></thead>
        <tbody>
          <tr><td>reMarkable</td><td>parcourir Dropbox, copier des fichiers vers la tablette et envoyer notes/documents vers Dropbox</td></tr>
          <tr><td>BOOX</td><td>Dropbox est disponible dans le stockage tiers intégré</td></tr>
          <tr><td>Kobo compatibles</td><td>ajout d'EPUB/PDF non protégés et export de carnets vers un dossier Rakuten Kobo</td></tr>
          <tr><td>Supernote</td><td>Dropbox peut être utilisé comme service de synchronisation de dossiers</td></tr>
        </tbody>
      </table></div>

      <h2 id="kobo">Pourquoi Dropbox est particulièrement important chez Kobo</h2>
      <p>Kobo documente Dropbox à la fois pour ajouter des livres et pour exporter des carnets. Les notes exportées sont enregistrées dans un dossier Rakuten Kobo. Les possibilités varient toutefois selon le modèle et le type de contenu ; un EPUB annoté n'offre pas les mêmes possibilités qu'un PDF non protégé.</p>

      <h2 id="workflow">Évitez les doublons</h2>
      <p>Créez des dossiers séparés pour les fichiers à lire et les fichiers annotés. Un export cloud crée souvent une nouvelle copie plutôt qu'une mise à jour intelligente du fichier d'origine. Une convention de nommage simple, avec date ou suffixe "-annote", évite de confondre source et résultat.</p>

      <h2 id="decision">Dropbox suffit-il comme critère de choix ?</h2>
      <p>Pas seul. Vérifiez aussi la direction des transferts, les formats, la synchronisation des carnets natifs et le fonctionnement hors ligne. Pour comparer l'ensemble des solutions, consultez <a href="/guides/synchroniser-notes-cloud/">le guide cloud</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files" rel="noopener noreferrer">reMarkable : Dropbox</a></li>
        <li><a href="https://help.boox.com/hc/en-us/articles/8569457124628-Integrated-Third-Party-Cloud-Storage" rel="noopener noreferrer">BOOX : Dropbox intégré</a></li>
        <li><a href="https://help.kobo.com/hc/en-us/articles/360033830114-Add-books-to-your-eReader-using-Dropbox" rel="noopener noreferrer">Kobo : ajouter des livres avec Dropbox</a></li>
        <li><a href="https://help.kobo.com/hc/en-us/articles/360062226733-Use-your-Kobo-eReader-as-a-notebook" rel="noopener noreferrer">Kobo : exporter un carnet vers Dropbox</a></li>
        <li><a href="https://support.supernote.com/en_US/transfer-files" rel="noopener noreferrer">Supernote : Dropbox</a></li>
      </ul>
    """,

    "/guides/ecosysteme-ouvert-ou-ferme/": """
      <p class="article-answer"><strong>Un écosystème ouvert offre davantage d'applications et de chemins de fichiers ; un écosystème fermé ou spécialisé réduit les choix pour contrôler davantage l'expérience.</strong> Le meilleur modèle dépend de votre besoin d'applications tierces, pas d'une préférence abstraite pour "ouvert" ou "fermé".</p>

      <h2 id="definitions">Ouvert et fermé : de quoi parle-t-on ?</h2>
      <p>BOOX utilise Android sur plusieurs tablettes et donne accès à des applications ainsi qu'à des stockages tiers. reMarkable et Supernote construisent au contraire un environnement centré sur leurs propres fonctions de notes et de documents. Kindle Scribe et Kobo sont encore plus liés à leur univers de lecture. Ces positions forment un continuum : aucun appareil n'est totalement ouvert ou totalement fermé.</p>

      <h2 id="comparaison">Les compromis principaux</h2>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Critère</th><th>Écosystème plus ouvert</th><th>Écosystème spécialisé</th></tr></thead>
        <tbody>
          <tr><td>Applications</td><td>plus de choix</td><td>sélection limitée et contrôlée</td></tr>
          <tr><td>Réglages</td><td>plus nombreux</td><td>plus simples</td></tr>
          <tr><td>Compatibilité</td><td>plus de chemins possibles</td><td>flux officiels mieux délimités</td></tr>
          <tr><td>Distractions</td><td>plus proches d'une tablette classique</td><td>environnement volontairement restreint</td></tr>
          <tr><td>Maintenance</td><td>apps et services tiers à gérer</td><td>dépendance accrue aux choix du fabricant</td></tr>
        </tbody>
      </table></div>

      <h2 id="android">Android ne garantit pas une bonne application E Ink</h2>
      <p>Une app peut être installable mais mal adaptée à l'affichage : animations, défilement, couleurs ou gestes peuvent donner une expérience inférieure à celle d'un LCD. L'ouverture doit donc être testée avec votre application critique, pas mesurée au nombre d'apps disponibles.</p>

      <h2 id="specialise">L'avantage d'un système spécialisé</h2>
      <p>Un appareil comme reMarkable concentre l'interface sur les carnets, les PDF et les applications compagnon. Supernote développe également ses propres fonctions de titres, liens, mots-clés, digests et reconnaissance. Cette spécialisation peut réduire les réglages nécessaires, mais elle vous rend plus dépendant de la feuille de route du fabricant.</p>

      <h2 id="decision">Choisissez par dépendance logicielle</h2>
      <p>Si une application précise est indispensable, vérifiez-la d'abord sur un système ouvert. Si vos besoins se limitent à écrire, lire, classer et exporter, un environnement spécialisé peut être plus cohérent. Replacez ensuite ce choix dans le guide <a href="/guides/choisir-bloc-notes-numerique/">comment choisir son bloc-notes numérique</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://help.boox.com/hc/en-us/articles/8569457124628-Integrated-Third-Party-Cloud-Storage" rel="noopener noreferrer">BOOX : services tiers intégrés</a></li>
        <li><a href="https://support.remarkable.com/articles/Knowledge/Desktop-app" rel="noopener noreferrer">reMarkable : applications compagnon</a></li>
        <li><a href="https://support.supernote.com/en_US/introduction-to-the-toolbar" rel="noopener noreferrer">Supernote : outils de notes</a></li>
      </ul>
    """,

    "/guides/annoter-pdf-tablette-e-ink/": """
      <p class="article-answer"><strong>Pour bien annoter un PDF sur une tablette E Ink, vérifiez quatre choses : la taille d'écran, la possibilité d'écrire directement sur le document, l'export des annotations et la gestion des PDF protégés.</strong> La présence d'un stylet ne garantit pas que votre fichier final sera récupérable comme vous le souhaitez.</p>

      <h2 id="avant">Avant d'importer le PDF</h2>
      <p>Commencez par vérifier le format de page et les protections. Un PDF proche de l'A4 peut devenir pénible sur un petit écran. Un PDF protégé par DRM peut aussi limiter l'écriture ou l'export. Kobo indique par exemple que l'annotation au stylet n'est pas disponible sur certains PDF protégés.</p>

      <h2 id="modes">Les principaux modes d'annotation</h2>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Action</th><th>À vérifier</th></tr></thead>
        <tbody>
          <tr><td>Écriture libre</td><td>le trait est-il intégré à la page exportée ?</td></tr>
          <tr><td>Surlignage</td><td>le texte reste-t-il sélectionnable et la couleur conservée ?</td></tr>
          <tr><td>Note liée</td><td>apparaît-elle dans le PDF ou seulement dans l'écosystème ?</td></tr>
          <tr><td>Découpage / capture</td><td>la fonction crée-t-elle une image ou un nouvel objet de note ?</td></tr>
        </tbody>
      </table></div>

      <h2 id="ecosystemes">Quelques différences utiles</h2>
      <p>BOOX NeoReader permet l'écriture sur document et l'export d'annotations manuscrites en PNG ou PDF. Supernote permet d'annoter des PDF puis d'exporter les pages avec écriture ; ses surlignages peuvent également être conservés à l'export. Kobo peut exporter un PDF non protégé avec ses annotations manuscrites. Kindle Scribe permet l'annotation de documents importés, mais le comportement dépend du mode d'import et de la génération de l'appareil.</p>

      <h2 id="workflow">Un workflow d'annotation robuste</h2>
      <ol>
        <li>Gardez une copie intacte du PDF source.</li>
        <li>Annotez une copie sur la tablette.</li>
        <li>Exportez deux pages de test avant de traiter un document long.</li>
        <li>Vérifiez sur ordinateur que le manuscrit, les surlignages et les commentaires sont visibles.</li>
        <li>Archivez le résultat dans un dossier distinct.</li>
      </ol>

      <h2 id="decision">Le PDF doit décider de la taille et du logiciel</h2>
      <p>Si l'annotation de PDF est votre usage principal, donnez plus de poids à la <a href="/guides/taille-ecran-bloc-notes-numerique/">taille d'écran</a>, aux exports et au cloud qu'à la bibliothèque d'ebooks. Consultez aussi la page <a href="/usages/annotation-pdf/">bloc-notes numérique pour annoter des PDF</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://help.boox.com/hc/en-us/articles/8569296110100-Take-Notes-on-Books" rel="noopener noreferrer">BOOX : annotations et export dans NeoReader</a></li>
        <li><a href="https://support.supernote.com/en_US/organizing/contents-bookmarks-and-annotations" rel="noopener noreferrer">Supernote : annotations PDF</a></li>
        <li><a href="https://support.supernote.com/organizing/highlighting-text-in-pdfs" rel="noopener noreferrer">Supernote : surlignage PDF</a></li>
        <li><a href="https://help.kobo.com/hc/fr/articles/1500001927562-Annoter-votre-livre-avec-le-stylet-Kobo" rel="noopener noreferrer">Kobo : PDF et annotations</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/TNtSm13k3txFI4EvDV" rel="noopener noreferrer">Amazon : types de documents compatibles avec les notes Kindle Scribe</a></li>
      </ul>
    """,

    "/guides/convertir-notes-manuscrites-en-texte/": """
      <p class="article-answer"><strong>Pour convertir des notes manuscrites en texte, utilisez la fonction de reconnaissance de l'appareil puis exportez le résultat dans un format éditable comme TXT ou DOCX lorsqu'il est disponible.</strong> Avant de traiter un long carnet, vérifiez la langue, la mise en page et ce qui arrive aux dessins, équations et corrections.</p>

      <h2 id="etapes">La méthode en quatre étapes</h2>
      <ol>
        <li>Écrivez avec la langue de reconnaissance correcte.</li>
        <li>Lancez la conversion sur une page test.</li>
        <li>Relisez noms propres, nombres, abréviations et jargon.</li>
        <li>Exportez vers un format éditable ou copiez le texte dans votre outil final.</li>
      </ol>

      <h2 id="ecosystemes">Ce que proposent les principaux écosystèmes</h2>
      <p>reMarkable convertit des pages manuscrites en texte et permet d'exporter ou envoyer le résultat. Supernote propose une reconnaissance en temps réel et exporte en TXT ou DOCX. BOOX peut convertir le manuscrit en texte éditable dans ses notes. Kobo réalise la conversion dans les carnets avancés. Kindle Scribe propose la conversion en texte et, sur les modèles récents, des PDF recherchables.</p>

      <h2 id="limites">Ce qui se convertit mal</h2>
      <p>Les dessins, équations, flèches, tableaux manuscrits et mises en page libres posent davantage de problèmes qu'une phrase linéaire. Amazon exclut explicitement plusieurs de ces éléments de sa reconnaissance. Kobo demande aussi une écriture dans les lignes des carnets avancés. Si votre page mélange texte et schémas, conservez le PDF manuscrit en plus du texte reconnu.</p>

      <h2 id="qualite">Corrigez avant de diffuser</h2>
      <p>La reconnaissance ne remplace pas une relecture. Traitez les chiffres, noms de personnes, références et termes techniques comme des zones à risque. Pour des notes professionnelles, gardez l'original manuscrit afin de pouvoir vérifier une transcription ambiguë.</p>

      <h2 id="choix">Si la conversion est centrale dans votre workflow</h2>
      <p>Comparez les langues, le besoin de connexion, les formats d'export et la recherche manuscrite. Le guide <a href="/guides/ocr-manuscrit/">OCR manuscrit</a> détaille ces différences.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/articles/Knowledge/Convert-handwritten-notes-into-text" rel="noopener noreferrer">reMarkable : conversion</a></li>
        <li><a href="https://support.supernote.com/handwriting-recognition" rel="noopener noreferrer">Supernote : reconnaissance et export</a></li>
        <li><a href="https://help.boox.com/hc/en-us/articles/10701578837268-Handwritten-Notes" rel="noopener noreferrer">BOOX : Text Recognition</a></li>
        <li><a href="https://help.kobo.com/hc/en-us/articles/360062226733-Use-your-Kobo-eReader-as-a-notebook" rel="noopener noreferrer">Kobo : conversion en carnet avancé</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/TWTo0OyovlJ9jwOV0B" rel="noopener noreferrer">Amazon : reconnaissance Kindle Scribe</a></li>
      </ul>
    """,

    "/guides/organiser-notes-numeriques/": """
      <p class="article-answer"><strong>Organisez vos notes autour de la manière dont vous les retrouverez, pas autour du nombre de dossiers disponibles.</strong> Une structure simple combine quelques dossiers stables, des titres explicites, des liens ou mots-clés lorsque l'appareil les prend en charge, et une règle d'archivage.</p>

      <h2 id="structure">Commencez avec peu de dossiers</h2>
      <p>Créez d'abord les catégories qui correspondent à des contextes durables : travail, études, personnel ou projets majeurs. Évitez de reproduire une arborescence de serveur avec de nombreux niveaux ; sur une tablette, la recherche et les titres deviennent vite plus rapides que la navigation profonde.</p>

      <h2 id="nommage">Utilisez des titres qui se trient naturellement</h2>
      <p>Une convention comme "2026-09-08 - Client - Réunion" facilite le tri et évite les carnets appelés "Notes 3". Pour un projet long, gardez le nom du projet stable puis ajoutez le type de note ou la date.</p>

      <h2 id="fonctions">Exploitez les fonctions natives utiles</h2>
      <p>Les outils varient selon l'écosystème. BOOX propose des tags sur le contenu manuscrit. Supernote permet notamment titres, mots-clés, liens et digests. reMarkable propose des tags pour organiser les documents. Kindle Scribe récent peut rechercher dans l'écriture manuscrite de ses carnets dans plusieurs langues. La bonne méthode utilise ces fonctions uniquement si elles accélèrent réellement la récupération.</p>

      <h2 id="archive">Séparez travail actif et archive</h2>
      <p>Une fois un projet terminé, exportez les documents importants en PDF ou texte, placez-les dans votre stockage de référence, puis archivez ou supprimez les brouillons inutiles de l'appareil. Cela limite les résultats de recherche et réduit la dépendance au format natif du fabricant.</p>

      <h2 id="routine">Une routine de cinq minutes</h2>
      <ol>
        <li>Renommez les carnets créés dans la journée.</li>
        <li>Déplacez-les dans leur dossier principal.</li>
        <li>Ajoutez un tag ou mot-clé seulement si vous savez comment vous le rechercherez.</li>
        <li>Exportez les éléments qui doivent vivre ailleurs.</li>
        <li>Archivez les projets terminés une fois par mois.</li>
      </ol>
      <p>Pour sécuriser l'archive, consultez <a href="/guides/exporter-notes/">exporter ses notes</a> et <a href="/guides/synchroniser-notes-cloud/">synchroniser ses notes dans le cloud</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://help.boox.com/hc/en-us/articles/10991847539732-Tag-System" rel="noopener noreferrer">BOOX : système de tags</a></li>
        <li><a href="https://support.supernote.com/en_US/introduction-to-the-toolbar" rel="noopener noreferrer">Supernote : titres, mots-clés et liens</a></li>
        <li><a href="https://support.supernote.com/en_US/what-is-digest-and-what-does-it-do" rel="noopener noreferrer">Supernote : Digest</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/TXEroxFZdxObrcesZO" rel="noopener noreferrer">Amazon : recherche Kindle Scribe</a></li>
      </ul>
    """,

    "/guides/transfert-notes-vers-ordinateur/": """
      <p class="article-answer"><strong>Vous pouvez transférer des notes vers un ordinateur par application compagnon, cloud, navigateur local, câble USB ou export de fichier selon l'écosystème.</strong> Choisissez la méthode selon votre besoin : transfert ponctuel, synchronisation régulière ou sauvegarde indépendante du fabricant.</p>

      <h2 id="methodes">Les quatre grandes méthodes</h2>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Méthode</th><th>Avantage</th><th>Limite</th></tr></thead>
        <tbody>
          <tr><td>Application desktop</td><td>simple pour consulter et exporter</td><td>dépend du compte et du cloud du fabricant</td></tr>
          <tr><td>Cloud tiers</td><td>intègre Drive/OneDrive/Dropbox</td><td>souvent copie plutôt que sync du fichier source</td></tr>
          <tr><td>USB</td><td>transfert local sans cloud</td><td>fonctionnement différent selon les appareils</td></tr>
          <tr><td>Réseau local</td><td>sans câble et parfois sans cloud externe</td><td>configuration nécessaire</td></tr>
        </tbody>
      </table></div>

      <h2 id="remarkable">reMarkable</h2>
      <p>reMarkable propose ses applications desktop et web, mais aussi une interface USB accessible dans un navigateur local. Depuis cette interface, vous pouvez importer ou télécharger des documents. Les applications desktop exportent notamment en PDF, PNG ou SVG.</p>

      <h2 id="boox-supernote">BOOX et Supernote</h2>
      <p>BOOX prend en charge le câble USB, Send2BOOX, BooxDrop sur réseau local et les stockages tiers intégrés. Supernote documente les transferts par cloud, email, USB Type-C, Browse & Access et Supernote Linking. Ces deux écosystèmes offrent donc plusieurs chemins selon que vous privilégiez le local ou le cloud.</p>

      <h2 id="kindle-kobo">Kindle Scribe et Kobo</h2>
      <p>Kindle Scribe peut partager des carnets par email et, sur les modèles récents, vers Google Drive ou OneDrive. Kobo exporte ses carnets et peut utiliser Dropbox ou Google Drive sur certains modèles. Pour un transfert destiné à l'édition, vérifiez si vous récupérez du texte, un PDF ou seulement une image.</p>

      <h2 id="sauvegarde">Pour une vraie sauvegarde, gardez un format indépendant</h2>
      <p>Copier un format natif ne garantit pas qu'il sera lisible sans l'application du fabricant. Conservez régulièrement un PDF ou un format texte en plus de la synchronisation propriétaire. Consultez <a href="/guides/exporter-notes/">les formats d'export</a> pour choisir la bonne sortie.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files" rel="noopener noreferrer">reMarkable : applications, web et USB</a></li>
        <li><a href="https://help.boox.com/hc/en-us/articles/360043083892-How-to-transfer-files-between-your-BOOX-device-and-other-devices" rel="noopener noreferrer">BOOX : méthodes de transfert</a></li>
        <li><a href="https://support.supernote.com/en_US/transfer-files" rel="noopener noreferrer">Supernote : méthodes de transfert</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/TJE2UYmdw0ppUuR3Rs" rel="noopener noreferrer">Amazon : partage Kindle Scribe</a></li>
      </ul>
    """,

    "/guides/imprimer-notes-numeriques/": """
      <p class="article-answer"><strong>La méthode la plus fiable pour imprimer des notes numériques consiste à les exporter en PDF puis à imprimer ce PDF depuis un ordinateur ou un téléphone.</strong> Cela évite de dépendre d'une fonction d'impression propre à la tablette et permet de vérifier mise en page, orientation et pages avant d'utiliser du papier.</p>

      <h2 id="pdf">Pourquoi le PDF est le meilleur intermédiaire</h2>
      <p>Le PDF conserve la mise en page et est accepté par les systèmes d'impression courants. reMarkable, BOOX et Supernote proposent tous un export PDF de notes manuscrites. Kindle Scribe peut également partager des carnets sous forme de PDF, et Kobo permet d'exporter ses carnets selon leur type.</p>

      <h2 id="etapes">Imprimer en quatre étapes</h2>
      <ol>
        <li>Exportez les pages nécessaires en PDF.</li>
        <li>Ouvrez le fichier sur ordinateur ou téléphone.</li>
        <li>Vérifiez le format papier, l'orientation et l'échelle.</li>
        <li>Imprimez une page test si vos notes utilisent les bords ou une trame particulière.</li>
      </ol>

      <h2 id="mise-en-page">Attention aux proportions de l'écran</h2>
      <p>Une page de carnet numérique n'a pas toujours le ratio d'une feuille A4. Une impression "adapter à la page" peut réduire les marges ou redimensionner l'écriture. Si vous créez des documents destinés à l'impression, utilisez dès le départ un modèle proche du format final.</p>

      <h2 id="couleur">Couleur et niveaux de gris</h2>
      <p>Si vos annotations utilisent des couleurs, vérifiez l'export avant d'imprimer. Une imprimante noir et blanc peut rendre deux couleurs presque identiques. Pour un document où la couleur encode une information, faites un test en niveaux de gris ou imprimez en couleur.</p>

      <h2 id="texte">Et si vous voulez un document propre plutôt qu'une copie manuscrite ?</h2>
      <p>Convertissez d'abord l'écriture en texte, corrigez la reconnaissance puis mettez le document en page dans Word ou un autre éditeur. Cette méthode convient mieux aux comptes rendus et rapports. Consultez <a href="/guides/convertir-notes-manuscrites-en-texte/">convertir les notes manuscrites en texte</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files" rel="noopener noreferrer">reMarkable : export PDF</a></li>
        <li><a href="https://help.boox.com/hc/en-us/articles/8569373888788-Handwritten-Notes" rel="noopener noreferrer">BOOX : export PDF</a></li>
        <li><a href="https://support.supernote.com/en_US/introduction-to-the-toolbar" rel="noopener noreferrer">Supernote : export PDF</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/TJE2UYmdw0ppUuR3Rs" rel="noopener noreferrer">Amazon : partage PDF Kindle Scribe</a></li>
      </ul>
    """,
}
