"""High-depth overrides for technical /guides/ pages."""

GUIDE_CONTENT_QUALITY_TECH = {
    "/guides/tablette-e-ink/": """
      <p class="article-answer"><strong>Une tablette E Ink est une tablette dont l’écran utilise de l’encre électronique plutôt qu’un LCD ou OLED.</strong> Elle est particulièrement adaptée à la lecture, à la prise de notes et aux documents statiques, car l’image reste affichée avec très peu d’énergie. En contrepartie, les rafraîchissements sont plus lents et les interfaces animées, la vidéo ou le scroll intensif restent moins naturels que sur une tablette classique.</p>

      <h2 id="definition">Ce qui définit réellement une tablette E Ink</h2>
      <p>Le terme « tablette E Ink » couvre plusieurs familles de produits : liseuses avec stylet, blocs-notes spécialisés, tablettes Android ouvertes et grands écrans destinés aux PDF. Leur point commun est la technologie d’affichage électrophorétique. Des particules chargées se déplacent dans de minuscules capsules sous l’effet d’un champ électrique afin de former l’image.</p>
      <p>Cette image peut ensuite rester visible sans être rafraîchie en permanence. C’est ce comportement qui différencie l’E Ink d’un écran classique et explique à la fois sa sobriété sur des pages statiques et sa difficulté avec les contenus qui changent plusieurs dizaines de fois par seconde.</p>
      <p>Pour le mécanisme physique détaillé, le guide <a href="/guides/encre-electronique-fonctionnement/">comment fonctionne l’encre électronique</a> va plus loin sans mélanger technologie et choix de produit.</p>

      <h2 id="familles">Toutes les tablettes E Ink n’ont pas la même philosophie</h2>
      <p>Une erreur fréquente consiste à considérer que deux appareils E Ink de même taille sont interchangeables. En pratique, le logiciel compte autant que l’écran. reMarkable privilégie un environnement centré sur les documents et carnets. Supernote développe des fonctions de structuration et de reconnaissance manuscrite. Kindle Scribe et Kobo restent liés à l’univers de la lecture. BOOX combine E Ink et Android avec Google Play sur plusieurs modèles.</p>
      <div class="table-wrapper"><table class="comp-table"><thead><tr><th>Famille</th><th>Logique dominante</th><th>À vérifier avant achat</th></tr></thead><tbody>
        <tr><td>Liseuse + stylet</td><td>lecture enrichie par l’écriture</td><td>export des annotations, carnets, formats</td></tr>
        <tr><td>Bloc-notes spécialisé</td><td>écriture, classement, PDF et export</td><td>cloud, OCR, organisation, applications compagnon</td></tr>
        <tr><td>Tablette E Ink Android</td><td>applications tierces et polyvalence</td><td>fluidité des apps, autonomie, complexité</td></tr>
        <tr><td>Grand format</td><td>PDF, plans, partitions et documents proches de l’A4</td><td>poids, transport, prix</td></tr>
      </tbody></table></div>
      <p>Le tableau montre pourquoi il est dangereux de chercher « la meilleure tablette E Ink » sans préciser l’usage. Une tablette Android peut être plus ouverte mais moins simple. Une liseuse avec stylet peut être excellente pour lire sans devenir l’outil idéal pour gérer cent carnets professionnels.</p>

      <h2 id="avantages">Pourquoi l’E Ink est cohérent pour lire et écrire longtemps</h2>
      <p>L’écran est réfléchissant : il utilise la lumière ambiante plutôt que d’émettre lui-même toute la lumière nécessaire à l’image. Cette propriété donne une bonne lisibilité en extérieur et permet de maintenir une page avec peu d’énergie. Certains appareils ajoutent un éclairage frontal pour la lecture dans l’obscurité ; d’autres l’omettent pour conserver une dalle plus simple ou plus proche de la surface.</p>
      <p>Pour les notes, l’intérêt vient aussi de la spécialisation du logiciel. Les fabricants peuvent optimiser la zone de dessin et le rafraîchissement pour faire apparaître rapidement le trait du stylet, puis nettoyer l’écran ensuite. Ce comportement explique pourquoi la sensation d’écriture ne se résume pas au temps de rafraîchissement théorique de l’encre.</p>
      <p>Le guide sur la <a href="/guides/latence-ecriture/">latence d’écriture</a> détaille cette chaîne et évite de comparer des chiffres sans protocole commun.</p>

      <h2 id="limites">Les limites apparaissent dès que l’image doit changer constamment</h2>
      <p>Défilement rapide, vidéo, animations et interfaces complexes demandent de nombreuses mises à jour. Les fabricants utilisent des modes accélérés et, chez BOOX notamment, des technologies de rafraîchissement destinées à améliorer la fluidité. Mais ces modes peuvent augmenter le ghosting, la consommation ou la nécessité de rafraîchissements complets.</p>
      <p>Il faut donc distinguer « possible » et « adapté ». Ouvrir un site web, une application Android ou une vidéo ne signifie pas que l’expérience sera comparable à un iPad. Si vos tâches principales reposent sur ces contenus, une tablette classique reste souvent plus logique.</p>
      <p>Pour cette frontière, consultez <a href="/guides/tablette-classique-ou-tablette-e-ink/">tablette classique ou tablette E Ink</a> avant de choisir un modèle.</p>

      <h2 id="couleur">Monochrome et couleur répondent à des usages différents</h2>
      <p>La couleur E Ink existe, notamment avec Kaleido 3. E Ink annonce 4 096 couleurs, avec 300 ppp en noir et blanc et 150 ppp en couleur sur cette technologie. Le résultat convient aux graphiques, cartes, surligneurs et documents où la couleur sert d’information, mais il ne vise pas la fidélité photo d’un LCD ou OLED.</p>
      <p>Le monochrome conserve donc tout son intérêt pour le texte, les notes et les PDF principalement noirs. La couleur doit être justifiée par votre contenu, pas par l’idée qu’un écran couleur serait automatiquement plus avancé.</p>
      <p>Le test en niveaux de gris proposé dans <a href="/guides/bloc-notes-numerique-couleur-ou-noir-et-blanc/">couleur ou noir et blanc</a> permet de transformer cette préférence en critère concret.</p>

      <h2 id="achat">Les critères techniques à vérifier sur une fiche produit</h2>
      <p>Une fiche technique utile ne se limite pas à la diagonale et au stockage. Regardez la résolution, la présence d’un front light, le type de stylet, les formats documentaires, la connectivité, le système d’exploitation et les méthodes d’export. Sur une tablette Android, vérifiez aussi la version du système et l’accès effectif au Google Play Store.</p>
      <div class="table-wrapper"><table class="comp-table"><thead><tr><th>Critère</th><th>Impact concret</th><th>Question à poser</th></tr></thead><tbody>
        <tr><td>Taille</td><td>surface de PDF et mobilité</td><td>mon document reste-t-il lisible sans zoom ?</td></tr>
        <tr><td>Résolution</td><td>finesse du texte et du trait</td><td>quelle résolution en N&B et, si besoin, en couleur ?</td></tr>
        <tr><td>Front light</td><td>lecture dans l’obscurité</td><td>est-il indispensable à mon contexte ?</td></tr>
        <tr><td>OS / apps</td><td>ouverture logicielle</td><td>mes applications critiques sont-elles utilisables ?</td></tr>
        <tr><td>Export</td><td>sortie des données</td><td>quels formats puis-je récupérer ?</td></tr>
      </tbody></table></div>
      <p>Ces critères doivent être reliés à des tâches. Une résolution élevée n’aide pas si l’appareil bloque votre format de fichier ; Android n’aide pas si votre application principale est pénible sur E Ink. Le guide <a href="/guides/choisir-bloc-notes-numerique/">comment choisir son bloc-notes numérique</a> remet ces spécifications dans l’ordre de décision.</p>

      <h2 id="decision">Quand une tablette E Ink est-elle un bon choix ?</h2>
      <p>Elle est cohérente si l’essentiel de votre temps passe sur des pages relativement stables : carnets, livres, PDF, articles, documents à corriger. Plus votre journée dépend de la vidéo, du scroll, de la collaboration temps réel et d’applications animées, plus l’avantage de l’E Ink diminue.</p>
      <p>Une fois ce périmètre validé, le <a href="/comparatifs/tablette-e-ink/">comparatif des tablettes E Ink</a> peut servir à choisir une famille et un modèle sans confondre technologie et usage.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://www.eink.com/tech/detail/How_it_works" rel="noopener noreferrer">E Ink : fonctionnement de l’encre électronique</a></li>
        <li><a href="https://www.eink.com/brand/detail/Kaleido3" rel="noopener noreferrer">E Ink : Kaleido 3</a></li>
        <li><a href="https://shop.boox.com/products/go103gen2" rel="noopener noreferrer">BOOX : tablette E Ink Android actuelle</a></li>
        <li><a href="https://support.remarkable.com/articles/Knowledge/About-reMarkable-2" rel="noopener noreferrer">reMarkable : exemple de bloc-notes E Ink monochrome</a></li>
      </ul>
    """,

    "/guides/encre-electronique-fonctionnement/": """
      <p class="article-answer"><strong>L’encre électronique forme une image en déplaçant des particules chargées à l’intérieur de microcapsules ou structures comparables.</strong> Une fois les particules positionnées, l’image peut rester visible sans être redessinée en continu. C’est ce fonctionnement bistable qui explique la très faible consommation sur une page statique, la lisibilité en lumière ambiante et, en même temps, les rafraîchissements plus lents qu’un écran LCD ou OLED.</p>

      <h2 id="capsules">Des particules chargées forment les pixels visibles</h2>
      <p>Dans le système monochrome décrit par E Ink, des microcapsules contiennent notamment des particules blanches et noires portant des charges opposées. Lorsqu’un champ électrique est appliqué, certaines particules migrent vers la surface et deviennent visibles. En contrôlant cette migration pixel par pixel, l’écran produit du texte, des images et différents niveaux de gris.</p>
      <p>Le terme « encre » peut induire en erreur : rien n’est imprimé définitivement. La couche d’encre fait partie d’un module électronique commandé par une matrice et un contrôleur. La différence avec un écran lumineux vient de la manière dont l’état optique est créé et maintenu.</p>
      <p>Cette base physique permet de comprendre les choix pratiques décrits dans le guide <a href="/guides/tablette-e-ink/">qu’est-ce qu’une tablette E Ink</a>.</p>

      <h2 id="bistable">Pourquoi une page statique consomme si peu</h2>
      <p>L’un des intérêts majeurs de l’ePaper est son caractère bistable : une fois l’image formée, elle peut rester visible sans alimentation continue de chaque pixel. L’énergie est surtout nécessaire lorsque l’état de l’écran change. Un livre affichant la même page pendant trente secondes n’a donc pas le même profil de consommation qu’un navigateur qui défile continuellement.</p>
      <p>Cette propriété explique pourquoi les fabricants annoncent souvent des autonomies en semaines sur des usages de lecture ou de notes. Elle ne signifie pas que toute la tablette consomme presque zéro : processeur, Wi-Fi, éclairage frontal, stockage, stylet actif et applications continuent à demander de l’énergie.</p>
      <p>Le guide sur <a href="/guides/autonomie-tablette-e-ink/">l’autonomie des tablettes E Ink</a> aide à interpréter les chiffres fabricants sans attribuer toute la consommation à la dalle.</p>

      <h2 id="refresh">Pourquoi le rafraîchissement est plus lent et produit du ghosting</h2>
      <p>Déplacer physiquement des particules n’est pas instantané comme modifier l’intensité d’un sous-pixel LCD. Les contrôleurs appliquent donc des formes d’onde et différents modes de mise à jour selon le compromis recherché. Un rafraîchissement complet peut nettoyer davantage l’image, tandis qu’un mode rapide privilégie la vitesse.</p>
      <p>Le ghosting correspond à des traces résiduelles d’un état précédent. Il n’indique pas nécessairement un défaut : il peut être le résultat volontaire d’un mode qui évite de nettoyer entièrement chaque pixel à chaque mouvement. Les appareils déclenchent alors périodiquement un rafraîchissement plus complet.</p>
      <p>Cette logique est directement liée à la <a href="/guides/latence-ecriture/">latence d’écriture</a> : le trait peut être affiché rapidement avec une stratégie optimisée, puis l’image finalisée ensuite.</p>

      <h2 id="couleur">Comment la couleur est-elle ajoutée à l’E Ink ?</h2>
      <p>Il existe plusieurs approches. Kaleido 3 utilise une couche de filtres couleur au-dessus de l’encre monochrome. E Ink annonce 4 096 couleurs et une résolution de 300 ppp en noir et blanc contre 150 ppp en couleur. D’autres technologies E Ink gèrent la couleur différemment et ne doivent pas être assimilées automatiquement à Kaleido.</p>
      <p>La couche couleur modifie le compromis optique : la lecture de texte, les couleurs, l’éclairage frontal et le contraste doivent être évalués ensemble. C’est pourquoi une tablette couleur n’est pas simplement une tablette monochrome à laquelle on aurait ajouté des pixels rouges, verts et bleus comme sur un LCD.</p>
      <p>Pour décider si ce compromis a une valeur pour vos documents, consultez <a href="/guides/bloc-notes-numerique-couleur-ou-noir-et-blanc/">couleur ou noir et blanc</a>.</p>

      <h2 id="lumiere">Écran réfléchissant et front light ne sont pas contradictoires</h2>
      <p>L’ePaper est lisible grâce à la lumière réfléchie par sa surface, ce qui le rapproche visuellement d’un support imprimé. Certains appareils ajoutent toutefois un front light : des LED diffusent de la lumière au-dessus ou à travers une couche optique pour éclairer la surface. La lumière ne provient donc pas du même mécanisme que sur un écran LCD rétroéclairé.</p>
      <p>Un appareil sans front light peut être excellent en plein jour mais nécessiter une lampe dans une pièce sombre. Un modèle avec éclairage offre plus de souplesse, au prix d’une consommation supplémentaire et d’une structure d’écran différente. Ce critère doit être relié à votre environnement d’utilisation.</p>
      <p>Le <a href="/guides/choisir-bloc-notes-numerique/">guide général de choix</a> permet de placer l’éclairage après les critères de fichiers et de workflow.</p>

      <h2 id="ecriture">Pourquoi l’écriture peut sembler rapide malgré l’E Ink</h2>
      <p>La chaîne d’écriture comprend le stylet, le numériseur, le processeur, le logiciel de dessin, le contrôleur d’écran et la dalle. Les fabricants peuvent optimiser le rendu du trait pour n’actualiser qu’une zone ou utiliser une forme d’onde rapide. Le chiffre de rafraîchissement général de l’écran ne suffit donc pas à prédire la sensation du stylet.</p>
      <p>reMarkable, BOOX, Supernote et d’autres fabricants appliquent leurs propres stratégies. Deux appareils utilisant de l’E Ink peuvent ainsi réagir différemment, notamment selon l’application et le mode sélectionné. Une mesure de latence n’est comparable que si le protocole est identique.</p>
      <p>Cette distinction est développée dans <a href="/guides/latence-ecriture/">le guide dédié à la latence</a>.</p>

      <h2 id="decision">Ce que ce fonctionnement change lors d’un achat</h2>
      <p>Vous pouvez déduire trois règles. Premièrement, l’E Ink est particulièrement cohérent pour des contenus statiques. Deuxièmement, les performances de scroll ou vidéo ne doivent pas être extrapolées à partir de la seule puissance du processeur. Troisièmement, autonomie, latence et couleur sont des propriétés du système complet, pas de la couche d’encre isolée.</p>
      <p>Pour passer de la technologie aux modèles, utilisez le <a href="/comparatifs/tablette-e-ink/">comparatif des tablettes E Ink</a> en gardant ces mécanismes comme grille de lecture.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://www.eink.com/tech/detail/How_it_works" rel="noopener noreferrer">E Ink : fonctionnement des particules chargées</a></li>
        <li><a href="https://www.eink.com/brand/detail/Kaleido" rel="noopener noreferrer">E Ink : structure Kaleido et filtres couleur</a></li>
        <li><a href="https://www.eink.com/brand/detail/Kaleido3" rel="noopener noreferrer">E Ink : Kaleido 3</a></li>
      </ul>
    """,

    "/guides/latence-ecriture/": """
      <p class="article-answer"><strong>La latence d’écriture est le délai entre le mouvement du stylet et l’apparition visible du trait, mais elle ne dépend pas d’un seul composant.</strong> Numériseur, traitement du stylet, application, contrôleur d’écran, mode de rafraîchissement et dalle participent tous au résultat. C’est pourquoi un chiffre annoncé en millisecondes ne doit être comparé entre appareils que si le protocole de mesure est identique.</p>

      <h2 id="chaine">Du stylet à l’encre : la latence est une chaîne complète</h2>
      <p>Lorsque vous déplacez le stylet, le numériseur détecte sa position et éventuellement la pression ou l’inclinaison. Le logiciel transforme ces données en trait, puis le contrôleur décide quelles zones de l’écran doivent être mises à jour. Enfin, la dalle E Ink change d’état. Chaque étape peut ajouter un délai ou être optimisée.</p>
      <p>Cette chaîne explique pourquoi deux appareils utilisant une dalle proche peuvent avoir des sensations différentes. Le fabricant peut réduire le délai logiciel, prédire une partie du mouvement, limiter la zone rafraîchie ou utiliser une forme d’onde rapide. À l’inverse, une application tierce mal optimisée peut ralentir la sensation même sur un appareil puissant.</p>
      <p>Le mécanisme physique du dernier maillon est détaillé dans <a href="/guides/encre-electronique-fonctionnement/">le fonctionnement de l’encre électronique</a>.</p>

      <h2 id="mesures">Pourquoi les chiffres de millisecondes sont difficiles à comparer</h2>
      <p>Une mesure de latence dépend du point de départ et du point d’arrivée. Mesure-t-on le contact du stylet, le mouvement initial, le premier pixel visible ou le trait final nettoyé ? Une caméra à 60 images/s ne donne pas la même résolution temporelle qu’une caméra à haute vitesse. La version logicielle, le stylet et l’application modifient aussi le résultat.</p>
      <p>reMarkable publie par exemple une valeur de latence pour certains modèles, mais cette donnée décrit son propre système et son protocole. Elle ne doit pas être placée dans un classement face à une mesure indépendante d’un autre appareil comme s’il s’agissait de la même expérience.</p>
      <p>Une bonne comparaison distingue donc les valeurs officielles, les tests tiers avec protocole publié et l’expérience subjective. Sans protocole commun, quelques millisecondes d’écart donnent une précision trompeuse.</p>

      <h2 id="refresh">Le rafraîchissement de l’écran n’est qu’un maillon</h2>
      <p>E Ink utilise différents modes de mise à jour. Un mode rapide peut faire apparaître plus vite une modification locale, tandis qu’un rafraîchissement complet nettoie davantage les résidus visuels. Pour l’écriture, les fabricants cherchent souvent à faire apparaître le trait rapidement puis à finaliser la page ensuite.</p>
      <p>Le ghosting que vous observez après un trait ou un déplacement peut donc provenir du compromis choisi pour privilégier la vitesse. Un appareil qui nettoie systématiquement chaque zone pourrait être plus propre mais moins réactif. La sensation d’écriture résulte de cet équilibre, pas d’une course vers un chiffre unique.</p>
      <p>Les tablettes Android E Ink ajoutent parfois plusieurs modes de rafraîchissement selon l’application. Le même appareil peut alors sembler différent dans l’app Notes intégrée et dans une application tierce.</p>

      <h2 id="sensation">La latence ressentie n’est pas la seule dimension du confort d’écriture</h2>
      <p>Deux appareils ayant une latence proche peuvent donner des sensations différentes à cause de l’épaisseur entre la pointe et l’image, du frottement de surface, de la précision du numériseur, du poids du stylet ou du comportement de la gomme. Il faut donc éviter de faire de la latence un synonyme de « sensation papier ».</p>
      <div class="table-wrapper"><table class="comp-table"><thead><tr><th>Facteur</th><th>Ce que vous ressentez</th><th>Comment le tester</th></tr></thead><tbody>
        <tr><td>Latence</td><td>trait qui suit plus ou moins vite la main</td><td>écriture rapide et hachures</td></tr>
        <tr><td>Distance pointe/image</td><td>impression d’écrire au-dessus du trait</td><td>petits caractères et précision</td></tr>
        <tr><td>Friction</td><td>glisse ou résistance</td><td>long paragraphe</td></tr>
        <tr><td>Précision</td><td>écart entre pointe et trait</td><td>bords, diagonales, signatures</td></tr>
        <tr><td>Rafraîchissement</td><td>ghosting ou clignotement</td><td>effacer, déplacer et tourner des pages</td></tr>
      </tbody></table></div>
      <p>Ce tableau explique pourquoi un test en magasin doit reproduire votre écriture. Tracer trois lignes lentes ne révèle pas les mêmes limites qu’un cours pris à grande vitesse ou un croquis avec nombreuses corrections.</p>

      <h2 id="usages">Quand la latence devient-elle vraiment prioritaire ?</h2>
      <p>Elle compte davantage pour l’écriture rapide, le dessin, les schémas fins et les signatures. Dans ces usages, un retard visible peut perturber le contrôle du geste. Pour de la lecture et quelques annotations marginales, une différence modeste de latence pèse souvent moins que la taille d’écran, le format de fichier ou la qualité de l’export.</p>
      <p>Un étudiant qui écrit tout un cours à la main doit donc donner davantage de poids à la réactivité qu’un lecteur qui surligne quelques passages. Un professionnel qui signe des documents doit vérifier la précision aux bords autant que la vitesse du trait.</p>
      <p>Pour remettre ce critère parmi les autres, consultez <a href="/guides/choisir-bloc-notes-numerique/">comment choisir son bloc-notes numérique</a> et <a href="/usages/prise-de-notes-etudiant/">la prise de notes pour les études</a>.</p>

      <h2 id="protocole">Un protocole simple pour tester la latence vous-même</h2>
      <p>Si vous pouvez essayer un appareil, ne cherchez pas à produire une mesure scientifique sans équipement. Cherchez plutôt des situations où le délai vous gênerait. Utilisez la même application et le même mode de rafraîchissement pendant tout le test, puis observez le comportement à plusieurs vitesses.</p>
      <ol><li>Écrivez une phrase à votre vitesse normale.</li><li>Écrivez plus vite que d’habitude pour faire apparaître une limite éventuelle.</li><li>Tracez de petites lettres et des diagonales près des bords.</li><li>Faites des hachures et des corrections successives.</li><li>Effacez et déplacez des éléments pour observer le rafraîchissement.</li></ol>
      <p>Si vous comparez deux appareils, répétez exactement la même séquence. Cette méthode ne produit pas un nombre universel, mais elle répond à la question qui compte : le système suit-il suffisamment votre geste pour votre usage ?</p>

      <h2 id="decision">La règle de décision</h2>
      <p>Traitez la latence comme un critère d’usage, pas comme un score absolu. Plus vous écrivez vite et dessinez, plus elle doit peser. Pour des annotations occasionnelles, donnez davantage de poids aux fichiers, à la taille et à l’export. Et si un fabricant annonce un chiffre, vérifiez le protocole avant de le comparer.</p>
      <p>Pour passer aux appareils après ce diagnostic, le <a href="/comparatifs/meilleur-bloc-notes-numerique/">comparatif des bloc-notes numériques</a> peut être lu avec cette grille plutôt qu’avec une simple colonne « ms ».</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://www.eink.com/tech/detail/How_it_works" rel="noopener noreferrer">E Ink : fonctionnement de l’affichage</a></li>
        <li><a href="https://support.remarkable.com/articles/Knowledge/About-reMarkable-2" rel="noopener noreferrer">reMarkable : exemple de latence annoncée sur reMarkable 2</a></li>
        <li><a href="https://help.boox.com/hc/en-us/articles/8569373888788-Handwritten-Notes" rel="noopener noreferrer">BOOX : outils d’écriture et rafraîchissement</a></li>
      </ul>
    """,

    "/guides/ocr-manuscrit/": """
      <p class="article-answer"><strong>Sur un bloc-notes numérique, « OCR manuscrit » peut désigner au moins trois fonctions différentes : convertir l’écriture en texte éditable, rendre l’écriture recherchable ou créer un PDF avec une couche de texte.</strong> Avant de comparer des appareils, vérifiez laquelle de ces sorties vous utilisez réellement, car les fabricants ne proposent pas tous les mêmes fonctions ni les mêmes formats.</p>

      <h2 id="fonctions">Conversion, recherche et PDF recherchable ne sont pas la même chose</h2>
      <p>La conversion remplace ou copie votre écriture sous forme de texte que vous pouvez éditer. La recherche manuscrite garde l’écriture visuelle mais crée un index permettant de retrouver un mot. Le PDF recherchable conserve l’apparence de la page tout en ajoutant une couche textuelle exploitable sur ordinateur. Ces fonctions peuvent coexister ou être proposées séparément.</p>
      <div class="table-wrapper"><table class="comp-table"><thead><tr><th>Fonction</th><th>Résultat</th><th>Usage principal</th></tr></thead><tbody>
        <tr><td>Conversion</td><td>texte éditable</td><td>compte rendu, email, Word</td></tr>
        <tr><td>Recherche manuscrite</td><td>index des mots reconnus</td><td>retrouver une note dans des carnets</td></tr>
        <tr><td>PDF recherchable</td><td>écriture visible + couche texte</td><td>archive et recherche sur ordinateur</td></tr>
      </tbody></table></div>
      <p>Une fiche produit qui indique simplement « OCR » ne suffit donc pas. Demandez quel contenu est reconnu, où le traitement a lieu et dans quel format vous récupérez le résultat. C’est particulièrement important si votre objectif est de sortir les notes de l’écosystème.</p>

      <h2 id="remarkable">reMarkable : conversion vers une nouvelle page texte</h2>
      <p>reMarkable documente la conversion de notes manuscrites en texte. La conversion peut créer une nouvelle page typée tout en conservant l’original manuscrit ; la sélection d’une zone peut aussi remplacer directement l’écriture par du texte. La documentation précise qu’une connexion Wi-Fi et un compte cloud sont nécessaires pour cette fonction.</p>
      <p>Le texte converti peut ensuite être édité et envoyé par email ou vers des services cloud. reMarkable indique aussi que certains contenus, comme les symboles mathématiques et diagrammes, ne sont pas convertis comme du texte normal. Cette limite rappelle qu’un OCR de notes n’est pas un système universel de reconnaissance scientifique.</p>
      <p>Si votre priorité est de produire un document final, le guide <a href="/guides/convertir-notes-manuscrites-en-texte/">convertir ses notes manuscrites en texte</a> décrit le workflow complet.</p>

      <h2 id="supernote-boox">Supernote et BOOX : reconnaissance intégrée à l’organisation des notes</h2>
      <p>Supernote propose des notes à reconnaissance en temps réel. Le système reconnaît l’écriture en arrière-plan et permet notamment de rechercher du texte manuscrit reconnu. Les résultats peuvent être exportés en TXT ou DOCX. Les notes standard peuvent également être reconnues lors de l’export, ce qui crée un choix entre écriture visuelle et texte transformé.</p>
      <p>BOOX permet la reconnaissance de texte dans ses notes manuscrites et propose des fonctions de recherche, d’édition et de partage. Les langues peuvent nécessiter le téléchargement de paquets. Comme les appareils BOOX sont Android, le workflow peut aussi combiner l’application Notes intégrée et des outils tiers, mais ces derniers ne profitent pas forcément de toutes les optimisations du système.</p>
      <p>Pour comparer l’ouverture de ces environnements, le guide <a href="/guides/ecosysteme-ouvert-ou-ferme/">écosystème ouvert ou fermé</a> apporte le contexte logiciel.</p>

      <h2 id="kindle-kobo">Kindle Scribe et Kobo ont leurs propres formes de conversion</h2>
      <p>Kindle Scribe peut convertir des carnets et, sur les modèles récents, créer des PDF recherchables lors du partage. Amazon précise que certains contenus comme dessins, diagrammes et équations ne sont pas pris en charge comme texte manuscrit normal. Sur les modèles 2025+, le résultat peut être envoyé vers des services cloud compatibles.</p>
      <p>Kobo distingue les carnets de base et avancés. Les carnets avancés prennent en charge la conversion de l’écriture et peuvent être exportés dans des formats comme DOCX, TXT ou HTML. Les gestes de mise en forme et de correction sont liés à ce type de carnet, tandis qu’un carnet de base reste plus proche d’une page dessinée.</p>
      <p>Cette diversité explique pourquoi l’intention « je veux de l’OCR » doit être reformulée en « je veux obtenir tel fichier à partir de telle note ».</p>

      <h2 id="precision">La précision dépend du contenu et pas seulement du moteur</h2>
      <p>Langue, cursive, taille des caractères, abréviations, mise en page et vocabulaire spécialisé influencent le résultat. Les équations, schémas, flèches ou tableaux manuscrits peuvent être mal interprétés ou volontairement exclus de la conversion. Un taux de reconnaissance global ne prédit donc pas la qualité sur vos propres notes.</p>
      <p>La bonne méthode consiste à tester une page représentative contenant vos titres, abréviations, mots techniques, ratures et symboles. Comparez ensuite le temps de correction du texte obtenu au temps que vous auriez passé à le retaper. Un OCR légèrement imparfait peut être très utile si la correction est rapide ; un OCR apparemment performant peut être mauvais s’il casse la structure de votre document.</p>
      <p>Pour l’organisation de grands volumes, consultez aussi <a href="/guides/organiser-notes-numeriques/">organiser ses notes numériques</a>, car la recherche manuscrite peut parfois être plus utile que la conversion intégrale.</p>

      <h2 id="connexion">En ligne ou hors ligne : vérifiez où se fait le traitement</h2>
      <p>Les conditions varient. reMarkable demande le Wi-Fi pour sa conversion documentée. BOOX peut demander une connexion pour certaines opérations ou le téléchargement de langues. Supernote propose de la reconnaissance en arrière-plan et documente des conditions propres à ses notes de reconnaissance. Il est donc risqué d’écrire « l’OCR fonctionne hors ligne » pour une marque entière sans préciser la fonction et la version logicielle.</p>
      <p>Cette question compte dans les environnements sensibles ou sans connexion. Si vos notes ne doivent pas quitter l’appareil, vérifiez explicitement le traitement local, les comptes nécessaires et les formats de sortie avant de sélectionner un modèle.</p>
      <p>Le guide <a href="/guides/bloc-notes-numerique-avec-ou-sans-abonnement/">avec ou sans abonnement</a> complète ce point pour les services cloud et fonctions premium.</p>

      <h2 id="decision">Choisissez l’OCR à partir du résultat final attendu</h2>
      <p>Si vous voulez rédiger un document Word, privilégiez une conversion exportable en DOCX ou texte. Si vous voulez retrouver rapidement une note, la recherche manuscrite peut suffire et préserver la page originale. Si vous archivez des carnets visuels, un PDF recherchable peut être le meilleur compromis.</p>
      <p>Avant l’achat, écrivez une page réelle, convertissez-la et regardez le fichier final plutôt que l’animation de démonstration. Ensuite, le <a href="/comparatifs/meilleur-bloc-notes-numerique/">comparatif des bloc-notes numériques</a> peut intégrer l’OCR comme critère réellement défini.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/articles/Knowledge/Convert-handwritten-notes-into-text" rel="noopener noreferrer">reMarkable : conversion manuscrite</a></li>
        <li><a href="https://support.supernote.com/en_US/Tools-Features/handwriting-recognition" rel="noopener noreferrer">Supernote : reconnaissance et export</a></li>
        <li><a href="https://help.boox.com/hc/en-us/articles/8569373888788-Handwritten-Notes" rel="noopener noreferrer">BOOX : reconnaissance dans les notes</a></li>
        <li><a href="https://help.kobo.com/hc/en-us/articles/360062226733-Use-your-Kobo-eReader-as-a-notebook" rel="noopener noreferrer">Kobo : carnets et formats d’export</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/TJE2UYmdw0ppUuR3Rs" rel="noopener noreferrer">Amazon : conversion et PDF recherchable</a></li>
      </ul>
    """,

    "/guides/autonomie-tablette-e-ink/": """
      <p class="article-answer"><strong>L’autonomie d’une tablette E Ink ne se résume pas à « plusieurs semaines ».</strong> L’écran consomme très peu lorsqu’une image reste fixe, mais le Wi-Fi, l’éclairage frontal, le processeur, les applications, la synchronisation et les rafraîchissements rapides peuvent changer fortement le résultat. Comparez donc les autonomies avec un scénario d’usage, pas uniquement avec la capacité de batterie ou une promesse fabricant.</p>

      <h2 id="ecran">Pourquoi l’écran E Ink peut économiser beaucoup d’énergie</h2>
      <p>Une image ePaper peut rester affichée sans être redessinée en continu. L’énergie est surtout consommée lorsqu’un changement d’état est nécessaire. Lire une page pendant une minute est donc très différent d’utiliser une interface qui défile constamment. Cette propriété permet à de nombreux appareils E Ink de viser des durées entre charges plus longues que les tablettes classiques.</p>
      <p>Mais l’écran n’est qu’un composant. Une tablette moderne contient un processeur, du stockage, du Wi-Fi, parfois Bluetooth, un front light et des services de synchronisation. Sur un modèle Android, les applications en arrière-plan peuvent également augmenter la consommation.</p>
      <p>Pour comprendre le rôle spécifique de la dalle, consultez <a href="/guides/encre-electronique-fonctionnement/">le fonctionnement de l’encre électronique</a>.</p>

      <h2 id="facteurs">Les facteurs qui font varier l’autonomie au quotidien</h2>
      <p>Deux personnes utilisant le même appareil peuvent obtenir des résultats très différents. Un lecteur hors ligne avec front light éteint change peu souvent d’écran. Un utilisateur qui synchronise des PDF, utilise une application Android, navigue sur le web et choisit un rafraîchissement rapide sollicite beaucoup plus le système.</p>
      <div class="table-wrapper"><table class="comp-table"><thead><tr><th>Facteur</th><th>Pourquoi il consomme</th><th>Comment le contrôler</th></tr></thead><tbody>
        <tr><td>Wi-Fi / cloud</td><td>transferts et synchronisations</td><td>désactiver lorsque inutile</td></tr>
        <tr><td>Front light</td><td>LED d’éclairage</td><td>réduire l’intensité</td></tr>
        <tr><td>Rafraîchissement rapide</td><td>plus de mises à jour</td><td>réserver aux apps qui en ont besoin</td></tr>
        <tr><td>Applications Android</td><td>CPU, réseau et tâches de fond</td><td>limiter les apps actives</td></tr>
        <tr><td>Écriture intensive</td><td>numériseur + rafraîchissements fréquents</td><td>normal, à intégrer au scénario</td></tr>
      </tbody></table></div>
      <p>Il ne s’agit pas de désactiver toutes les fonctions pour atteindre un record. Le but est de savoir lesquelles vous utiliserez réellement afin d’interpréter une autonomie annoncée dans un contexte comparable au vôtre.</p>

      <h2 id="fabricants">Pourquoi les annonces fabricants ne sont pas directement comparables</h2>
      <p>Les fabricants n’emploient pas nécessairement les mêmes protocoles. reMarkable annonce par exemple jusqu’à deux semaines pour le reMarkable 2, mais cette valeur appartient à ses conditions d’utilisation. Une autre marque peut annoncer une durée avec un autre mélange de lecture, écriture, Wi-Fi ou éclairage.</p>
      <p>La capacité en mAh ne résout pas le problème. Une batterie plus grande alimente parfois un processeur plus puissant, un écran couleur, un front light ou des modes rapides. Comparer 3 700 mAh à 3 000 mAh ne permet donc pas de déduire directement laquelle durera plus longtemps.</p>
      <p>Traitez les annonces comme des repères propres à chaque produit, puis cherchez des tests indépendants utilisant un protocole explicite si l’autonomie est un critère critique.</p>

      <h2 id="couleur-android">Couleur, Android et rafraîchissement rapide changent le profil énergétique</h2>
      <p>Une tablette E Ink couleur ou Android peut offrir davantage de fonctions, mais ces fonctions rendent le scénario plus proche d’une tablette polyvalente. Les modèles BOOX avec Android, Google Play et modes de rafraîchissement avancés peuvent utiliser plus souvent le processeur et le réseau qu’un e-note spécialisé restant sur un carnet statique.</p>
      <p>Cela ne signifie pas qu’Android « a une mauvaise autonomie ». Cela signifie qu’il permet des usages qui consomment davantage. Si vous installez email, navigateur et outils collaboratifs, l’appareil n’est plus utilisé comme une liseuse traditionnelle.</p>
      <p>Le guide <a href="/guides/ecosysteme-ouvert-ou-ferme/">écosystème ouvert ou fermé</a> aide à déterminer si cette polyvalence justifie le compromis pour votre travail.</p>

      <h2 id="scenario">Construisez votre propre scénario de comparaison</h2>
      <p>Définissez une journée type : nombre d’heures d’écriture, de lecture, usage du front light, synchronisations et applications. Demandez ensuite si l’appareil doit tenir une journée, une semaine de travail ou un voyage sans chargeur. Ce seuil est plus utile qu’une recherche du maximum absolu.</p>
      <ol><li>Notez le nombre d’heures d’écran actif par jour.</li><li>Indiquez si le Wi-Fi reste connecté en permanence.</li><li>Ajoutez l’éclairage frontal et son niveau habituel.</li><li>Listez les applications tierces éventuelles.</li><li>Fixez la fréquence de recharge que vous acceptez.</li></ol>
      <p>Une personne qui peut charger au bureau chaque vendredi n’a pas besoin du même compromis qu’un voyageur qui part dix jours sans prise disponible. L’autonomie doit donc être évaluée comme une contrainte logistique.</p>

      <h2 id="preserver">Comment préserver l’autonomie sans dégrader l’usage</h2>
      <p>Désactivez surtout ce qui ne sert pas. Couper le Wi-Fi pendant plusieurs heures de lecture, réduire l’éclairage dans une pièce déjà lumineuse et éviter un mode de rafraîchissement ultra-rapide dans une application statique sont des optimisations logiques. Fermer des applications Android inutiles peut également réduire les tâches en arrière-plan.</p>
      <p>En revanche, ne sacrifiez pas une fonction essentielle uniquement pour atteindre une durée théorique. Si la synchronisation est au cœur de votre travail, gardez-la et intégrez sa consommation dans votre décision. Une autonomie réaliste avec vos fonctions actives vaut plus qu’un record obtenu en mode minimal.</p>
      <p>Pour replacer l’autonomie parmi les autres critères, revenez au <a href="/guides/choisir-bloc-notes-numerique/">guide général de choix</a>.</p>

      <h2 id="decision">La règle de décision</h2>
      <p>Ne comparez ni les semaines annoncées ni les mAh isolément. Comparez la capacité de l’appareil à tenir votre intervalle de recharge habituel avec les fonctions que vous utiliserez réellement. Si deux modèles dépassent déjà largement ce seuil, donnez davantage de poids aux fichiers, à l’écran et au logiciel.</p>
      <p>Si l’autonomie devient un critère éliminatoire, utilisez le <a href="/comparatifs/tablette-e-ink/">comparatif des tablettes E Ink</a> uniquement avec des données dont le protocole ou les conditions sont clairement indiqués.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://www.eink.com/tech/detail/How_it_works" rel="noopener noreferrer">E Ink : principe bistable</a></li>
        <li><a href="https://support.remarkable.com/articles/Knowledge/About-reMarkable-2" rel="noopener noreferrer">reMarkable : batterie et autonomie annoncée</a></li>
        <li><a href="https://shop.boox.com/products/go103gen2" rel="noopener noreferrer">BOOX : batterie, Android et caractéristiques du Go 10.3 Gen II</a></li>
        <li><a href="https://support.supernote.com/en_US/faq" rel="noopener noreferrer">Supernote : ressources d’autonomie et batterie</a></li>
      </ul>
    """,

    "/guides/formats-fichiers-compatibles/": """
      <p class="article-answer"><strong>La compatibilité d’un bloc-notes numérique ne se résume pas à une liste d’extensions.</strong> Un appareil peut ouvrir un PDF ou EPUB sans pour autant conserver toutes les annotations, gérer les DRM, réexporter le fichier dans le format voulu ou offrir la même expérience avec un DOCX. Pour choisir, vérifiez séparément l’import, l’annotation, l’export et les protections du document.</p>

      <h2 id="quatre-niveaux">Un format peut être « compatible » à quatre niveaux différents</h2>
      <p>La première question est l’ouverture : le fichier est-il accepté ? La deuxième est l’édition ou l’annotation : peut-on écrire dessus ou seulement le lire ? La troisième est la restitution : peut-on réexporter le document avec les modifications ? La quatrième concerne la structure : le texte reste-t-il éditable ou le document devient-il une image/PDF aplati ?</p>
      <div class="table-wrapper"><table class="comp-table"><thead><tr><th>Niveau</th><th>Question</th><th>Exemple de piège</th></tr></thead><tbody>
        <tr><td>Import</td><td>le fichier entre-t-il sur l’appareil ?</td><td>format absent ou limite de taille</td></tr>
        <tr><td>Lecture</td><td>la mise en page reste-t-elle exploitable ?</td><td>DOCX rendu différemment</td></tr>
        <tr><td>Annotation</td><td>où sont stockés les traits et surlignages ?</td><td>note liée mais pas incorporée au fichier</td></tr>
        <tr><td>Export</td><td>que récupère-t-on ?</td><td>PDF/image au lieu de texte éditable</td></tr>
      </tbody></table></div>
      <p>Cette grille explique pourquoi une simple colonne « PDF : oui » dans un comparatif est insuffisante. Pour un workflow professionnel, la sortie est souvent plus importante que l’ouverture initiale.</p>

      <h2 id="pdf">PDF : le format le plus courant, mais pas toujours le plus simple</h2>
      <p>Le PDF préserve la mise en page et convient bien aux contrats, articles, cours et documents à annoter. reMarkable, Kobo, Kindle Scribe, BOOX et Supernote le prennent en charge sous différentes formes. La différence se situe dans la navigation, l’annotation, la gestion des liens et la manière dont les notes sont exportées.</p>
      <p>Un PDF protégé par mot de passe ou DRM peut limiter l’écriture. Amazon indique par exemple que certains PDF protégés importés sur Kindle Scribe deviennent lecture seule. BOOX peut demander d’incorporer les annotations au PDF avant de le synchroniser ailleurs pour que les traits apparaissent dans un autre lecteur.</p>
      <p>Si les PDF représentent votre usage principal, consultez <a href="/guides/annoter-pdf-tablette-e-ink/">le guide d’annotation PDF</a> plutôt que de vous arrêter au support du format.</p>

      <h2 id="epub">EPUB et DRM : le fichier n’est pas toujours librement transférable</h2>
      <p>EPUB est un format de livre reflowable : le texte peut s’adapter à la taille et à la police choisies. Mais les livres achetés peuvent être protégés par DRM. Kobo explique par exemple que les EPUB ou PDF protégés par Adobe DRM nécessitent Adobe Digital Editions pour certains transferts. Un EPUB non protégé suit un parcours plus simple.</p>
      <p>Les annotations d’un ebook ne fonctionnent pas nécessairement comme celles d’un PDF. Elles peuvent rester liées à la bibliothèque et au moteur de lecture plutôt qu’être incorporées dans un fichier portable. Si vous devez partager vos annotations, vérifiez donc la méthode spécifique au fabricant.</p>
      <p>Cette différence est centrale dans <a href="/guides/liseuse-ou-bloc-notes-numerique/">liseuse ou bloc-notes numérique</a>.</p>

      <h2 id="bureautique">DOCX, PPTX et fichiers bureautiques : ouverture ne veut pas dire édition complète</h2>
      <p>Les tablettes Android E Ink comme BOOX prennent en charge de nombreux formats dans leurs lecteurs et peuvent installer des applications tierces. Supernote documente également la création et l’édition de documents Word dans certaines fonctions. Mais une mise en page complexe, des macros, commentaires avancés ou polices spécifiques peuvent ne pas se comporter comme sur un ordinateur.</p>
      <p>Si vous devez réellement éditer un DOCX, testez la fonction précise : correction de texte, insertion, suivi des modifications, tableaux et export final. Pour un simple document à lire et annoter, convertir en PDF peut parfois produire un workflow plus stable.</p>
      <p>Ne choisissez donc pas un appareil parce qu’une extension apparaît dans une liste. Décrivez l’action nécessaire sur ce fichier et vérifiez-la dans la documentation ou une démonstration.</p>

      <h2 id="notes">Les formats de notes propriétaires nécessitent un plan de sortie</h2>
      <p>Les carnets internes utilisent souvent un format propre au fabricant afin de conserver les traits, objets, liens et métadonnées. Ce format est utile dans l’écosystème mais ne sera pas toujours lisible ailleurs. L’important est de savoir quels exports standard sont proposés : PDF, PNG, SVG, TXT, DOCX ou autre.</p>
      <p>Une exportation standard peut perdre certaines fonctions. Les liens internes entre pages, tags ou structure de calques peuvent disparaître dans un PDF. Avant de créer plusieurs années d’archives, décidez quelles informations doivent survivre à un changement de marque.</p>
      <p>Le guide <a href="/guides/exporter-notes/">exporter ses notes</a> et celui sur <a href="/guides/bloc-notes-numerique-avec-ou-sans-abonnement/">les dépendances d’écosystème</a> permettent de construire ce plan.</p>

      <h2 id="comparatif">Repères documentés selon les écosystèmes</h2>
      <p>Les formats évoluent avec les mises à jour, mais les documentations officielles montrent des philosophies différentes. reMarkable concentre l’import sur PDF/EPUB et certains médias selon la méthode, avec export en PDF, PNG, SVG ou texte pour certains contenus. Kobo liste EPUB, PDF, images et plusieurs formats texte. BOOX annonce un éventail très large incluant PDF, EPUB, DOC/DOCX, PPT/PPTX et de nombreux formats de lecture.</p>
      <div class="table-wrapper"><table class="comp-table"><thead><tr><th>Écosystème</th><th>Force</th><th>Point de vigilance</th></tr></thead><tbody>
        <tr><td>reMarkable</td><td>workflow document/notes simple</td><td>formats d’import volontairement resserrés</td></tr>
        <tr><td>Kobo</td><td>large bibliothèque de formats lecture</td><td>DRM et types de carnets</td></tr>
        <tr><td>BOOX</td><td>grand nombre de formats + Android</td><td>comportement variable selon application</td></tr>
        <tr><td>Supernote</td><td>notes, PDF/EPUB et Word</td><td>vérifier l’export de chaque type de contenu</td></tr>
        <tr><td>Kindle Scribe</td><td>Kindle + documents compatibles</td><td>génération et méthode d’envoi/import</td></tr>
      </tbody></table></div>
      <p>Ces repères ne remplacent pas la vérification du fichier réel. La meilleure pratique reste d’essayer un document représentatif avant l’achat ou de consulter le manuel de la version logicielle actuelle.</p>

      <h2 id="decision">La checklist compatibilité avant achat</h2>
      <p>Choisissez trois fichiers réels : le plus fréquent, le plus complexe et celui que vous devez partager. Pour chacun, vérifiez import, lecture, annotation et export. Ajoutez la question des DRM et de la taille maximale si elle est pertinente. Si le workflow fonctionne sur ces trois cas, la compatibilité est probablement suffisante.</p>
      <p>Ensuite, replacez ce critère dans le <a href="/guides/choisir-bloc-notes-numerique/">guide général de choix</a> et, si le cloud intervient, dans <a href="/guides/synchroniser-notes-cloud/">la synchronisation des notes</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files" rel="noopener noreferrer">reMarkable : formats d’import et d’export</a></li>
        <li><a href="https://help.kobo.com/hc/en-us/articles/360017763713-File-formats-your-Kobo-eReader-and-Kobo-Books-app-support" rel="noopener noreferrer">Kobo : formats et DRM</a></li>
        <li><a href="https://shop.boox.com/products/go103gen2" rel="noopener noreferrer">BOOX : formats documentaires du Go 10.3 Gen II</a></li>
        <li><a href="https://support.supernote.com/en_US/Tools-Features/word-documents" rel="noopener noreferrer">Supernote : documents Word</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/TIh9JOMGAKr7bY4zqu" rel="noopener noreferrer">Amazon : limites de fichiers Kindle Scribe</a></li>
      </ul>
    """,
}
