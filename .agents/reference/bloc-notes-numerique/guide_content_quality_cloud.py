"""High-depth overrides for export, cloud and ecosystem guides."""

GUIDE_CONTENT_QUALITY_CLOUD = {
    "/guides/exporter-notes/": """
      <p class="article-answer"><strong>Exporter ses notes signifie transformer ou copier un contenu créé dans l’écosystème du bloc-notes vers un format utilisable ailleurs.</strong> Avant l’achat, ne vérifiez pas seulement si un bouton « Export » existe : contrôlez le format obtenu, ce qui est conservé — écriture, couleur, texte reconnu, liens — et la destination disponible : ordinateur, email, Google Drive, OneDrive, Dropbox ou application compagnon.</p>

      <h2 id="objectif">Commencez par le destinataire, pas par le format proposé</h2>
      <p>Un export n’est utile que si le fichier final fonctionne dans votre chaîne de travail. Pour transmettre une correction à un collègue, un PDF annoté peut suffire. Pour retravailler un compte rendu, vous aurez plutôt besoin de texte éditable ou de DOCX. Pour archiver un carnet visuel, un PDF ou une image peut être préférable à une conversion qui détruit la mise en page.</p>
      <p>Décrivez donc le résultat attendu : « je veux joindre mes annotations à un email », « je veux continuer le texte dans Word », « je veux retrouver le carnet dans Drive » ou « je veux sauvegarder une copie indépendante du fabricant ». Ces objectifs ne demandent pas la même fonction d’export.</p>
      <p>Si les extensions elles-mêmes ne sont pas claires, le guide <a href="/guides/formats-fichiers-compatibles/">formats de fichiers compatibles</a> distingue import, annotation et restitution.</p>

      <h2 id="formats">PDF, image, texte et DOCX ne préservent pas la même chose</h2>
      <p>Le PDF est généralement le format le plus pratique pour préserver l’apparence d’une page annotée. PNG ou JPEG produisent une image simple mais perdent la structure textuelle. SVG peut préserver des tracés vectoriels dans certains écosystèmes. TXT et DOCX deviennent intéressants lorsque l’écriture manuscrite a été reconnue et que le contenu doit rester éditable.</p>
      <div class="table-wrapper"><table class="comp-table"><thead><tr><th>Format de sortie</th><th>Ce qu’il préserve bien</th><th>Limite fréquente</th></tr></thead><tbody>
        <tr><td>PDF</td><td>mise en page et annotations visuelles</td><td>texte manuscrit pas toujours éditable</td></tr>
        <tr><td>PNG/JPEG</td><td>apparence d’une page</td><td>recherche et édition limitées</td></tr>
        <tr><td>SVG</td><td>tracés vectoriels</td><td>moins universel pour le partage quotidien</td></tr>
        <tr><td>TXT</td><td>texte simple</td><td>mise en page perdue</td></tr>
        <tr><td>DOCX</td><td>texte reconnu et édition bureautique</td><td>structure visuelle manuscrite transformée</td></tr>
      </tbody></table></div>
      <p>Le bon format dépend donc de ce que vous voulez préserver. Une note peut avoir deux exports utiles : un PDF qui garde la page originale et un DOCX qui récupère uniquement le texte reconnu. Il n’y a pas toujours un format unique « meilleur ».</p>

      <h2 id="ecosystemes">Les principaux écosystèmes n’exportent pas de la même manière</h2>
      <p>reMarkable documente l’export en PDF, PNG et SVG depuis son application, ainsi que l’envoi par email et l’upload vers Google Drive, Dropbox ou OneDrive. Supernote propose plusieurs sorties selon le type de note, dont PDF/image et TXT/DOCX après reconnaissance. BOOX permet notamment d’exporter ses notes en PNG, PDF ou format propriétaire et peut copier des documents vers des stockages cloud tiers.</p>
      <p>Kobo distingue les carnets de base et avancés : les premiers peuvent sortir en PDF ou image, les seconds en DOCX, TXT, HTML ou ZIP. Kindle Scribe propose l’envoi de carnets et documents par email ; sur les modèles 2025+, Amazon ajoute des sorties vers Drive, OneDrive et OneNote, avec PDF, texte ou PDF recherchable selon le cas.</p>
      <p>Cette diversité est une raison de vérifier le <a href="/guides/ocr-manuscrit/">type d’OCR manuscrit</a> avant de considérer qu’une tablette « exporte en texte ».</p>

      <h2 id="copie">Export, synchronisation et sauvegarde sont trois opérations différentes</h2>
      <p>Exporter crée généralement une copie dans un format ou un emplacement déterminé. Synchroniser maintient une relation entre plusieurs emplacements ou appareils. Sauvegarder vise à pouvoir récupérer les données après une perte ou une panne. Un export vers Google Drive peut donc être une copie ponctuelle sans devenir une synchronisation bidirectionnelle.</p>
      <p>Amazon l’explique clairement pour les fichiers importés sur les Kindle Scribe récents : les annotations ajoutées sur l’appareil ne modifient pas automatiquement le fichier source dans Drive ou OneDrive ; l’utilisateur renvoie une nouvelle copie annotée. De la même manière, un PDF exporté d’un carnet propriétaire est une bonne archive visuelle mais ne remplace pas nécessairement le fichier natif pour continuer à éditer sur la tablette.</p>
      <p>Le guide <a href="/guides/synchroniser-notes-cloud/">synchroniser ses notes dans le cloud</a> développe cette différence, essentielle pour éviter de croire qu’une copie est « toujours à jour ».</p>

      <h2 id="test">Le test d’export à faire avant de remplir des centaines de pages</h2>
      <p>Créez une page contenant plusieurs éléments : écriture manuscrite, surlignage, couleur si disponible, image ou forme, puis quelques lignes converties en texte. Exportez-la dans les formats que vous comptez utiliser et ouvrez les fichiers sur un ordinateur qui n’a pas le logiciel du fabricant.</p>
      <ol><li>Vérifiez que toute l’écriture est visible.</li><li>Contrôlez les couleurs et la position des annotations.</li><li>Testez la recherche dans le PDF si elle est annoncée.</li><li>Ouvrez le DOCX ou TXT et regardez la qualité du texte reconnu.</li><li>Conservez un exemplaire hors du cloud du fabricant.</li></ol>
      <p>Ce petit test permet de repérer immédiatement les pertes de structure. Il est beaucoup moins coûteux de découvrir une limite sur trois pages que lorsque votre archive contient deux années de notes.</p>

      <h2 id="plan-sortie">Construisez un plan de sortie indépendant de la marque</h2>
      <p>Décidez quelles données doivent être lisibles dans dix ans sans appareil de la marque. Pour beaucoup d’utilisateurs, une archive PDF périodique suffit pour les carnets terminés, tandis que les documents actifs restent dans le format natif. Pour d’autres, le texte doit pouvoir être réutilisé dans Word ou un gestionnaire de connaissances.</p>
      <p>Le plan de sortie doit aussi couvrir la structure : nom des dossiers, dates, projets et conventions de fichiers. Un export techniquement parfait reste difficile à utiliser si cent documents sortent sous des noms génériques. L’organisation est donc liée à la portabilité.</p>
      <p>Le guide <a href="/guides/organiser-notes-numeriques/">organiser ses notes numériques</a> propose une structure qui survit mieux aux changements d’outil.</p>

      <h2 id="decision">La checklist d’export avant achat</h2>
      <p>Vérifiez quatre choses : le format final, la destination, la fidélité du contenu et l’indépendance vis-à-vis du fabricant. Si vous devez continuer l’édition sur ordinateur, ajoutez le texte reconnu ou DOCX à vos critères. Si vous partagez surtout des annotations, privilégiez la qualité du PDF final.</p>
      <p>Une fois ce besoin défini, replacez-le dans le <a href="/guides/choisir-bloc-notes-numerique/">guide de choix d’un bloc-notes numérique</a>. Un excellent écran ne compense pas un export qui bloque votre dernière étape.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files" rel="noopener noreferrer">reMarkable : import, export, email et cloud</a></li>
        <li><a href="https://support.supernote.com/en_US/Tools-Features/handwriting-recognition" rel="noopener noreferrer">Supernote : export TXT/DOCX après reconnaissance</a></li>
        <li><a href="https://help.boox.com/hc/en-us/articles/8569373888788-Handwritten-Notes" rel="noopener noreferrer">BOOX : partage et export de notes</a></li>
        <li><a href="https://help.kobo.com/hc/en-us/articles/360062226733-Use-your-Kobo-eReader-as-a-notebook" rel="noopener noreferrer">Kobo : formats d’export des carnets</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/TP8wuaQilIlwlITVTL" rel="noopener noreferrer">Amazon : partage Kindle Scribe vers services cloud</a></li>
      </ul>
    """,

    "/guides/synchroniser-notes-cloud/": """
      <p class="article-answer"><strong>Synchroniser des notes dans le cloud signifie maintenir une version accessible depuis plusieurs appareils ou services, mais tous les systèmes ne font pas de synchronisation bidirectionnelle.</strong> Certains répliquent les fichiers natifs dans le cloud du fabricant, d’autres copient des PDF vers Drive, Dropbox ou OneDrive. Avant l’achat, vérifiez ce qui se synchronise, dans quel sens, à quel moment et comment sont gérés les conflits.</p>

      <h2 id="sync-export">Ne confondez pas synchronisation et export vers le cloud</h2>
      <p>Une synchronisation véritable cherche à conserver le même contenu à jour sur plusieurs emplacements. Un export crée une nouvelle copie. Cette différence est capitale : si vous annotez un PDF importé depuis Drive et que l’appareil vous permet seulement de renvoyer une copie, le document original ne change pas automatiquement.</p>
      <p>Les fabricants utilisent parfois le mot « cloud » pour des fonctions très différentes. Le cloud reMarkable sert notamment à relier la tablette à ses applications. BOOX peut synchroniser certaines données via le compte ONYX et accéder parallèlement à des stockages tiers. Supernote propose plusieurs services de synchronisation. Kindle Scribe 2025+ traite Drive et OneDrive comme des connexions d’import/export de copies pour plusieurs scénarios.</p>
      <p>Si votre besoin est seulement de récupérer un fichier terminé, le guide <a href="/guides/exporter-notes/">exporter ses notes</a> peut être plus pertinent qu’une synchronisation permanente.</p>

      <h2 id="questions">Les cinq questions à poser à n’importe quel cloud</h2>
      <p>Le nom du service ne suffit pas. Une intégration Google Drive peut signifier navigation dans les dossiers, import manuel, export d’une copie ou synchronisation d’un répertoire. Pour éviter les mauvaises surprises, utilisez toujours la même grille.</p>
      <div class="table-wrapper"><table class="comp-table"><thead><tr><th>Question</th><th>Pourquoi elle compte</th><th>Risque</th></tr></thead><tbody>
        <tr><td>Qu’est-ce qui est synchronisé ?</td><td>fichiers, notes natives, annotations, métadonnées</td><td>archive incomplète</td></tr>
        <tr><td>Dans quel sens ?</td><td>tablette → cloud, cloud → tablette ou les deux</td><td>croire qu’un original est mis à jour</td></tr>
        <tr><td>Quand ?</td><td>automatique, à l’ouverture, bouton manuel</td><td>version obsolète</td></tr>
        <tr><td>Comment sont gérés les conflits ?</td><td>édition sur plusieurs appareils</td><td>doublons ou écrasement</td></tr>
        <tr><td>Que reste-t-il sans abonnement ?</td><td>continuité à long terme</td><td>dépendance au service</td></tr>
      </tbody></table></div>
      <p>Cette grille est plus utile qu’une liste de logos cloud. Elle permet de comparer deux intégrations qui portent le même nom mais n’offrent pas le même workflow.</p>

      <h2 id="remarkable">reMarkable : cloud maison et intégrations tierces ont des rôles différents</h2>
      <p>reMarkable synchronise ses fichiers avec les applications compagnon lorsque la tablette est connectée au Wi-Fi. La documentation précise qu’un utilisateur sans Connect conserve la synchronisation, mais que les documents non ouverts et synchronisés depuis plus de 50 jours cessent d’être disponibles dans les apps. L’appareil garde néanmoins ses fichiers localement.</p>
      <p>Les intégrations Google Drive, Dropbox et OneDrive servent aussi à importer et exporter des documents. Il faut donc distinguer le cloud reMarkable, qui maintient l’écosystème tablette/apps, et les stockages tiers, utilisés comme sources ou destinations de fichiers.</p>
      <p>Pour comprendre le rôle de Connect dans ce dispositif, consultez <a href="/guides/bloc-notes-numerique-avec-ou-sans-abonnement/">bloc-notes avec ou sans abonnement</a>.</p>

      <h2 id="boox-supernote">BOOX et Supernote offrent plus d’une méthode de transfert</h2>
      <p>BOOX documente l’intégration de Dropbox, Google Drive, OneDrive et d’autres services WebDAV dans sa bibliothèque. Le système peut télécharger des fichiers vers la bibliothèque et copier certains documents vers le stockage cloud. Parallèlement, les données de lecture et notes BOOX peuvent utiliser le compte ONYX pour une synchronisation propre à l’écosystème.</p>
      <p>Supernote propose Supernote Cloud, Dropbox et Google Drive dans sa documentation de transfert, et OneDrive comme option de synchronisation ajoutée à son système. La marque propose également USB, Browse & Access sur le réseau local et des applications partenaires. Cela permet de construire un workflow qui ne repose pas obligatoirement sur un seul cloud.</p>
      <p>Cette différence illustre le thème <a href="/guides/ecosysteme-ouvert-ou-ferme/">écosystème ouvert ou fermé</a> : davantage d’options donnent de la flexibilité mais demandent aussi de comprendre quelle méthode fait quoi.</p>

      <h2 id="conflits">La synchronisation crée aussi un risque de conflits</h2>
      <p>Lorsque deux appareils modifient un même fichier avant que la synchronisation soit terminée, le système doit choisir entre écraser, dupliquer ou signaler le conflit. Supernote conseille par exemple d’éviter l’édition simultanée du même fichier sur deux appareils et d’attendre la fin du sync avant de poursuivre ailleurs.</p>
      <p>Dans un environnement professionnel, cette règle devient importante : une tablette E Ink n’est pas forcément un outil de coédition temps réel. Si plusieurs personnes travaillent sur une source unique, un workflow de copie annotée peut être préférable à une pseudo-synchronisation ambiguë, ou il faut conserver l’outil collaboratif principal sur ordinateur.</p>
      <p>Testez donc le cas problématique avant de l’ignorer : modifiez un fichier sur la tablette et sur l’ordinateur, puis observez exactement ce que le système conserve.</p>

      <h2 id="securite">Cloud et sauvegarde ne sont pas synonymes</h2>
      <p>Une synchronisation réplique parfois aussi une suppression ou une erreur. Pour les carnets importants, conservez périodiquement une copie indépendante dans un format standard. Un PDF exporté n’offre pas toutes les fonctions du carnet natif, mais constitue une archive lisible si le compte cloud rencontre un problème.</p>
      <p>Pour les données sensibles, vérifiez aussi les politiques de l’organisation : un compte OneDrive professionnel peut bloquer une connexion tierce, Amazon rappelle par exemple que l’accès à un drive d’entreprise dépend des paramètres de sécurité de l’organisation. Les droits et l’authentification font donc partie de la compatibilité.</p>
      <p>Le guide <a href="/guides/transfert-notes-vers-ordinateur/">transférer ses notes vers l’ordinateur</a> présente les alternatives locales lorsque le cloud n’est pas souhaité.</p>

      <h2 id="decision">La checklist avant de choisir une intégration cloud</h2>
      <p>Choisissez un document réel, faites-le entrer depuis votre cloud, annotez-le, renvoyez-le puis modifiez-le sur ordinateur. Vérifiez si vous manipulez une seule version ou plusieurs copies, comment les noms de fichiers évoluent et ce qui arrive aux annotations. Faites ensuite le même test avec un carnet natif.</p>
      <p>Une fois le mécanisme compris, les guides dédiés à <a href="/guides/bloc-notes-numerique-google-drive/">Google Drive</a>, <a href="/guides/bloc-notes-numerique-onedrive/">OneDrive</a> et <a href="/guides/bloc-notes-numerique-dropbox/">Dropbox</a> permettent de vérifier les différences propres à chaque service.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/articles/Knowledge/Help-with-sync-and-the-reMarkable-cloud" rel="noopener noreferrer">reMarkable : synchronisation cloud</a></li>
        <li><a href="https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files" rel="noopener noreferrer">reMarkable : intégrations tierces</a></li>
        <li><a href="https://help.boox.com/hc/en-us/articles/8569457124628-Integrated-Third-Party-Cloud-Storage" rel="noopener noreferrer">BOOX : stockages cloud intégrés</a></li>
        <li><a href="https://support.supernote.com/en_US/transfer-files" rel="noopener noreferrer">Supernote : services cloud et transferts</a></li>
        <li><a href="https://support.supernote.com/en_US/how-to-sync-files-between-two-devices" rel="noopener noreferrer">Supernote : gestion des conflits entre appareils</a></li>
      </ul>
    """,

    "/guides/bloc-notes-numerique-google-drive/": """
      <p class="article-answer"><strong>Google Drive peut être intégré à plusieurs bloc-notes numériques, mais l’expression « compatible Google Drive » couvre des fonctions très différentes.</strong> Selon l’appareil, vous pouvez importer un fichier, exporter une copie, synchroniser certains dossiers ou utiliser une application Android. Vérifiez surtout si vos annotations reviennent automatiquement dans le fichier d’origine — ce n’est pas toujours le cas.</p>

      <h2 id="compatibilite">Quatre niveaux de compatibilité avec Google Drive</h2>
      <p>Une intégration peut se limiter à choisir un fichier dans Drive, tandis qu’une autre expose des dossiers dans la bibliothèque de la tablette. Les modèles Android peuvent aussi installer l’application Drive elle-même. Pour comparer, séparez accès, import, export et synchronisation.</p>
      <div class="table-wrapper"><table class="comp-table"><thead><tr><th>Niveau</th><th>Ce que cela permet</th><th>Question à poser</th></tr></thead><tbody>
        <tr><td>Accès</td><td>voir les dossiers/fichiers</td><td>tous les formats sont-ils visibles ?</td></tr>
        <tr><td>Import</td><td>copier un document sur la tablette</td><td>le fichier reste-t-il lié à l’original ?</td></tr>
        <tr><td>Export</td><td>envoyer une copie vers Drive</td><td>annotations et nom sont-ils conservés ?</td></tr>
        <tr><td>Synchronisation</td><td>maintenir des dossiers à jour</td><td>est-elle bidirectionnelle et automatique ?</td></tr>
      </tbody></table></div>
      <p>Cette grille évite un raccourci fréquent : la présence du logo Drive ne prouve pas qu’un document est coédité entre tablette et ordinateur. Dans de nombreux workflows, la tablette télécharge une copie puis en renvoie une autre.</p>

      <h2 id="remarkable">reMarkable : Drive comme intégration de fichiers</h2>
      <p>reMarkable permet de connecter Google Drive puis d’importer et d’exporter des fichiers depuis la tablette. Sa documentation actuelle décrit aussi l’upload vers Drive depuis « My files ». Cette intégration est utile pour faire entrer un PDF de travail et renvoyer ensuite une version annotée.</p>
      <p>Il faut toutefois distinguer cette intégration du cloud reMarkable, qui synchronise les fichiers entre la tablette et les applications compagnon. Drive n’est pas simplement le stockage natif de la tablette : c’est un service tiers utilisé comme source et destination.</p>
      <p>Si vous utilisez aussi Connect, consultez <a href="/guides/bloc-notes-numerique-avec-ou-sans-abonnement/">avec ou sans abonnement</a> pour séparer clairement les deux rôles.</p>

      <h2 id="kindle">Kindle Scribe 2025+ : import et retour d’une copie</h2>
      <p>Amazon a ajouté une connexion Google Drive aux Kindle Scribe sortis en 2025 ou après. L’utilisateur peut importer certains fichiers compatibles depuis Drive, les annoter puis envoyer une copie vers son cloud. Amazon précise que les annotations réalisées sur le Scribe ne se synchronisent pas automatiquement dans le fichier original : il faut uploader une nouvelle copie.</p>
      <p>Pour les carnets, les modèles compatibles peuvent partager vers Drive sous plusieurs formes, dont PDF manuscrit, texte converti ou PDF recherchable selon les options. Le workflow est donc plus riche qu’un simple import, mais il reste fondé sur des copies explicites.</p>
      <p>Si Kindle est au cœur de votre choix, le <a href="/comparatifs/kindle-scribe-vs-remarkable/">comparatif Kindle Scribe vs reMarkable</a> aide à comparer deux philosophies d’intégration.</p>

      <h2 id="kobo">Kobo : Drive pour les fichiers non protégés sur certains modèles</h2>
      <p>Kobo documente Google Drive sur plusieurs liseuses, dont Kobo Elipsa et Elipsa 2E. Le service permet notamment d’ajouter des EPUB ou PDF non protégés depuis Drive. Kobo précise qu’un contenu protégé par DRM suit un autre parcours, généralement via Adobe Digital Editions.</p>
      <p>Cette nuance est importante pour une bibliothèque professionnelle ou académique : « le PDF est dans Drive » ne signifie pas qu’il sera forcément importable et annotable de la même manière. Vérifiez la protection du fichier et la version logicielle de la liseuse.</p>
      <p>Le guide <a href="/guides/formats-fichiers-compatibles/">formats compatibles</a> explique pourquoi DRM, format et méthode de transfert doivent être vérifiés ensemble.</p>

      <h2 id="boox-supernote">BOOX et Supernote : Drive peut s’intégrer à une logique de dossiers</h2>
      <p>BOOX permet de lier Google Drive dans son stockage cloud tiers. Les documents peuvent être téléchargés vers la bibliothèque et certains fichiers copiés vers le cloud. Sur les modèles Android, l’application Google Drive peut également être installée, ce qui ajoute une autre méthode avec un comportement différent de l’intégration système.</p>
      <p>Supernote documente Google Drive comme option de synchronisation de dossiers, aux côtés de Supernote Cloud et Dropbox. La logique de sélection des dossiers à synchroniser est donc plus proche d’une organisation persistante que d’un simple bouton d’export.</p>
      <p>Plus il existe de méthodes, plus il est important de choisir une méthode principale afin d’éviter les doublons. Le guide <a href="/guides/synchroniser-notes-cloud/">synchronisation cloud</a> propose une grille commune.</p>

      <h2 id="workflow">Le workflow Google Drive à tester avant achat</h2>
      <p>Créez un dossier de test dans Drive avec un PDF simple, un PDF lourd et un fichier protégé si vous en utilisez. Importez le premier, annotez-le, exportez-le puis ouvrez la copie sur ordinateur. Vérifiez le nom, l’emplacement, la présence des annotations et la différence avec le fichier source.</p>
      <ol><li>Connectez le compte exact que vous utiliserez.</li><li>Importez un fichier représentatif.</li><li>Ajoutez écriture et surlignage.</li><li>Renvoyez le document vers Drive.</li><li>Contrôlez s’il s’agit d’une copie ou d’un sync.</li></ol>
      <p>Si votre organisation impose Microsoft plutôt que Google, comparez ensuite avec <a href="/guides/bloc-notes-numerique-onedrive/">OneDrive</a>. Si vous cherchez une solution plus neutre entre systèmes, examinez aussi <a href="/guides/bloc-notes-numerique-dropbox/">Dropbox</a>.</p>

      <h2 id="decision">Quand Google Drive doit-il devenir un critère éliminatoire ?</h2>
      <p>Drive est éliminatoire si tous vos documents arrivent par ce service et que vous refusez les transferts manuels. Mais ne cochez pas seulement « oui/non » : exigez le niveau de compatibilité qui correspond à votre flux. Un import/export de copie peut être parfait pour de la correction ; une équipe qui attend une source synchronisée aura besoin d’un autre fonctionnement.</p>
      <p>Replacez ensuite l’intégration dans le <a href="/guides/choisir-bloc-notes-numerique/">guide général de choix</a>, car un cloud compatible ne compense pas une mauvaise taille d’écran ou un export inadapté.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files" rel="noopener noreferrer">reMarkable : Google Drive et export</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/TjrMJmg3DZpAQLwVuN" rel="noopener noreferrer">Amazon : import depuis Google Drive</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/TP8wuaQilIlwlITVTL" rel="noopener noreferrer">Amazon : partage vers Google Drive</a></li>
        <li><a href="https://help.kobo.com/hc/en-us/articles/15335985512983-Add-books-to-your-eReader-using-Google-Drive" rel="noopener noreferrer">Kobo : Google Drive et fichiers non protégés</a></li>
        <li><a href="https://help.boox.com/hc/en-us/articles/8569457124628-Integrated-Third-Party-Cloud-Storage" rel="noopener noreferrer">BOOX : Google Drive intégré</a></li>
        <li><a href="https://support.supernote.com/en_US/transfer-files" rel="noopener noreferrer">Supernote : synchronisation Google Drive</a></li>
      </ul>
    """,

    "/guides/bloc-notes-numerique-onedrive/": """
      <p class="article-answer"><strong>OneDrive est particulièrement important si vos notes doivent rejoindre un environnement Microsoft, mais les intégrations varient fortement.</strong> reMarkable, BOOX, Supernote et les Kindle Scribe récents proposent des formes de connexion à OneDrive. Selon le système, il s’agit d’import/export, de synchronisation de dossiers ou d’accès via Android. Vérifiez aussi les restrictions de votre compte Microsoft 365 professionnel.</p>

      <h2 id="besoin">Définissez ce que « travailler avec OneDrive » veut dire</h2>
      <p>Pour certains utilisateurs, OneDrive sert simplement à recevoir des PDF et y déposer des versions annotées. Pour d’autres, il est le stockage central d’une entreprise avec règles d’accès, dossiers partagés et politiques de sécurité. Ces deux scénarios demandent des intégrations différentes.</p>
      <p>Une tablette peut être techniquement compatible avec OneDrive tout en échouant sur un compte d’entreprise si l’administrateur bloque l’autorisation de l’application. Amazon rappelle explicitement que l’accès aux drives professionnels dépend des paramètres de sécurité de l’organisation. Il faut donc tester le compte réel, pas seulement un compte personnel.</p>
      <p>Si votre besoin se limite à sortir un fichier final, le guide <a href="/guides/exporter-notes/">exporter ses notes</a> peut suffire à définir le workflow.</p>

      <h2 id="modeles">Quatre types d’intégration OneDrive à reconnaître</h2>
      <p>Comme avec Drive, le logo du service ne dit pas le niveau de connexion. Les approches vont du transfert ponctuel à la synchronisation de dossiers. Une tablette Android peut aussi installer l’application officielle, avec des avantages et limites différents de l’intégration du fabricant.</p>
      <div class="table-wrapper"><table class="comp-table"><thead><tr><th>Approche</th><th>Exemple de fonctionnement</th><th>À surveiller</th></tr></thead><tbody>
        <tr><td>Import/export</td><td>ouvrir un PDF puis renvoyer une copie</td><td>pas de mise à jour de l’original</td></tr>
        <tr><td>Sync de dossiers</td><td>sélectionner des dossiers à synchroniser</td><td>conflits et rythme du sync</td></tr>
        <tr><td>Cloud intégré</td><td>naviguer dans OneDrive depuis la bibliothèque</td><td>formats copiables</td></tr>
        <tr><td>Application Android</td><td>utiliser l’app OneDrive</td><td>ergonomie et rafraîchissement E Ink</td></tr>
      </tbody></table></div>
      <p>Pour un environnement Microsoft lourd, la possibilité d’installer des apps peut sembler séduisante, mais elle doit être testée sur E Ink. Pour un flux simple de PDF, une intégration native plus limitée peut être plus efficace.</p>

      <h2 id="remarkable">reMarkable : OneDrive comme source et destination de documents</h2>
      <p>reMarkable prend en charge OneDrive parmi ses intégrations cloud et permet l’upload de fichiers depuis la tablette. L’usage typique consiste à récupérer un document, l’annoter puis exporter le résultat. Le cloud reMarkable et OneDrive jouent des rôles différents : le premier relie l’écosystème reMarkable, le second sert de stockage tiers.</p>
      <p>Dans un contexte professionnel, vérifiez l’autorisation OAuth et les politiques de l’entreprise. Une intégration qui fonctionne sur un compte Microsoft personnel ne garantit pas que votre tenant professionnel l’acceptera.</p>
      <p>Si le coût de Connect intervient dans votre comparaison, consultez <a href="/guides/bloc-notes-numerique-avec-ou-sans-abonnement/">le guide sur les abonnements</a>.</p>

      <h2 id="kindle">Kindle Scribe 2025+ : OneDrive est une connexion d’import et de partage</h2>
      <p>Amazon permet aux Kindle Scribe sortis en 2025 ou après de se connecter à Microsoft OneDrive. Des fichiers compatibles peuvent être importés, annotés puis partagés vers OneDrive. Amazon précise que les annotations ne se synchronisent pas automatiquement dans la source : une nouvelle copie du document est envoyée.</p>
      <p>Les carnets peuvent aussi être partagés vers OneDrive avec plusieurs options de format, dont PDF manuscrit, conversion en texte et PDF recherchable selon le cas. Cette logique est efficace pour déposer un livrable dans OneDrive, mais elle ne transforme pas le Scribe en coéditeur d’un fichier Office.</p>
      <p>Le guide <a href="/guides/liseuse-ou-bloc-notes-numerique/">liseuse ou bloc-notes</a> aide à décider si cette logique orientée lecture reste suffisante pour votre travail.</p>

      <h2 id="boox-supernote">BOOX et Supernote proposent des approches plus proches du système de fichiers</h2>
      <p>BOOX intègre OneDrive à sa bibliothèque cloud et permet de télécharger ou copier certains documents. Sur les modèles Android, l’application OneDrive elle-même peut être installée. Cela offre davantage de chemins possibles, mais augmente aussi le risque d’utiliser plusieurs copies ou dossiers sans convention claire.</p>
      <p>Supernote a ajouté OneDrive comme option de synchronisation. L’utilisateur autorise le service, sélectionne les dossiers à synchroniser puis déclenche le sync. Les notes et fichiers doivent toutefois être gérés avec prudence sur plusieurs appareils pour éviter les conflits.</p>
      <p>Le guide <a href="/guides/synchroniser-notes-cloud/">synchroniser ses notes cloud</a> explique pourquoi une synchronisation de dossiers demande davantage de discipline qu’un export ponctuel.</p>

      <h2 id="entreprise">Le vrai test : votre compte Microsoft 365 professionnel</h2>
      <p>Si OneDrive est un critère professionnel, effectuez le test avec le compte d’entreprise avant la fin de la période de retour. Vérifiez l’autorisation de connexion, les dossiers partagés, la taille des fichiers, le MFA et les restrictions éventuelles de l’administrateur. N’utilisez pas un compte personnel comme preuve de compatibilité.</p>
      <p>Testez aussi un fichier réel : import, annotation, export, ouverture dans OneDrive sur PC et éventuel partage à un collègue. Si votre workflow exige Word ou OneNote plutôt qu’un PDF final, vérifiez ces applications séparément ; « compatible OneDrive » ne garantit pas une édition Office complète.</p>
      <p>Si vous avez besoin d’applications métier Microsoft, comparez aussi <a href="/guides/ecosysteme-ouvert-ou-ferme/">écosystème ouvert ou fermé</a>.</p>

      <h2 id="decision">Quand OneDrive doit-il éliminer un modèle ?</h2>
      <p>Si votre entreprise centralise tous les documents dans OneDrive et interdit d’autres clouds, l’intégration devient un critère éliminatoire. Exigez alors le niveau exact dont vous avez besoin : dépôt de PDF, import de fichiers, synchronisation de dossiers ou usage d’une application. Si OneDrive sert seulement d’archive finale, une simple exportation fiable peut suffire.</p>
      <p>Pour comparer avec d’autres services, consultez <a href="/guides/bloc-notes-numerique-google-drive/">Google Drive</a> et <a href="/guides/bloc-notes-numerique-dropbox/">Dropbox</a>, puis revenez au <a href="/guides/choisir-bloc-notes-numerique/">guide de choix</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files" rel="noopener noreferrer">reMarkable : OneDrive comme intégration</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/Tuar1obhcxaS8hVUKd" rel="noopener noreferrer">Amazon : connexion OneDrive</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/TIh9JOMGAKr7bY4zqu" rel="noopener noreferrer">Amazon : limites et cloud professionnel</a></li>
        <li><a href="https://help.boox.com/hc/en-us/articles/8569457124628-Integrated-Third-Party-Cloud-Storage" rel="noopener noreferrer">BOOX : OneDrive intégré</a></li>
        <li><a href="https://support.supernote.com/en_US/Whats-New/utilize-onedrive-your-new-cloud-sync-option-for-file-backup" rel="noopener noreferrer">Supernote : synchronisation OneDrive</a></li>
      </ul>
    """,

    "/guides/bloc-notes-numerique-dropbox/": """
      <p class="article-answer"><strong>Dropbox est l’un des services cloud les plus largement intégrés aux bloc-notes numériques, mais chaque marque l’utilise différemment.</strong> reMarkable s’en sert pour importer et exporter des fichiers, BOOX l’intègre à sa bibliothèque cloud, Supernote peut synchroniser des dossiers et certains Kobo permettent de charger des fichiers depuis Dropbox. Vérifiez toujours si vous manipulez une copie ou un contenu réellement synchronisé.</p>

      <h2 id="interet">Pourquoi Dropbox peut être plus simple qu’un cloud lié à une suite bureautique</h2>
      <p>Dropbox sert principalement à stocker et partager des fichiers, sans imposer le même ensemble d’applications bureautiques que Microsoft 365 ou Google Workspace. Pour un workflow basé sur des PDF, EPUB et exports de notes, cette neutralité peut simplifier les échanges entre plusieurs appareils et systèmes.</p>
      <p>Elle ne garantit toutefois pas une meilleure intégration. Le fabricant décide si Dropbox apparaît comme un explorateur de fichiers, un service d’import/export ou une destination de synchronisation. Un même compte Dropbox peut donc se comporter différemment sur reMarkable, BOOX, Supernote ou Kobo.</p>
      <p>Le guide <a href="/guides/synchroniser-notes-cloud/">synchronisation cloud</a> fournit la grille pour distinguer ces mécanismes.</p>

      <h2 id="comparaison">Les principaux modes d’intégration Dropbox</h2>
      <p>Avant de comparer des marques, traduisez la compatibilité en action concrète. Cette étape est particulièrement utile si vous souhaitez garder une architecture de dossiers commune entre ordinateur et tablette.</p>
      <div class="table-wrapper"><table class="comp-table"><thead><tr><th>Mode</th><th>Usage</th><th>Limite possible</th></tr></thead><tbody>
        <tr><td>Import</td><td>prendre un PDF dans Dropbox</td><td>copie locale indépendante</td></tr>
        <tr><td>Export</td><td>déposer une version annotée</td><td>nouveau fichier à gérer</td></tr>
        <tr><td>Sync de dossiers</td><td>maintenir une arborescence choisie</td><td>conflits et délais</td></tr>
        <tr><td>App Android</td><td>accès complet à l’app Dropbox</td><td>ergonomie variable sur E Ink</td></tr>
      </tbody></table></div>
      <p>Si votre besoin est seulement « récupérer un PDF le matin et le renvoyer le soir », l’import/export suffit. Si vous voulez retrouver automatiquement une arborescence de projet entière, la synchronisation de dossiers devient plus importante.</p>

      <h2 id="remarkable">reMarkable : Dropbox comme intégration de documents</h2>
      <p>reMarkable permet d’importer des fichiers depuis Dropbox et d’y uploader des documents depuis la tablette. Le fonctionnement s’intègre à son système « My files », mais reste distinct de la synchronisation reMarkable vers les applications compagnon.</p>
      <p>Cette séparation a un avantage : vous pouvez garder Dropbox comme dépôt de projets tout en utilisant le cloud reMarkable pour la continuité entre tablette et desktop app. Elle demande toutefois de comprendre quelle copie est la version de référence.</p>
      <p>Pour éviter les doublons, définissez une convention : par exemple « source dans Dropbox, copie annotée suffixée -reviewed ». Le guide <a href="/guides/organiser-notes-numeriques/">organiser ses notes numériques</a> aide à construire ces règles.</p>

      <h2 id="boox-supernote">BOOX et Supernote : deux approches plus proches du dossier</h2>
      <p>BOOX permet de lier Dropbox dans la bibliothèque cloud et de télécharger les fichiers dans une étagère liée au compte. Certains documents peuvent ensuite être copiés vers le stockage cloud. Sur Android, l’application Dropbox peut aussi être installée, ce qui crée une seconde méthode qu’il vaut mieux ne pas mélanger sans raison.</p>
      <p>Supernote permet d’autoriser Dropbox puis de sélectionner les dossiers à synchroniser. Le système peut donc correspondre à quelqu’un qui souhaite retrouver une arborescence précise sur son appareil. Comme pour toute sync, évitez d’éditer simultanément la même ressource sur plusieurs appareils avant la fin de l’opération.</p>
      <p>Si vous hésitez entre flexibilité et simplicité, le guide <a href="/guides/ecosysteme-ouvert-ou-ferme/">écosystème ouvert ou fermé</a> complète cette comparaison.</p>

      <h2 id="kobo">Kobo : Dropbox sert surtout au transfert de livres et documents compatibles</h2>
      <p>Certains modèles Kobo permettent de charger des fichiers non protégés via Dropbox, en complément d’autres méthodes. Comme avec Google Drive, les DRM peuvent imposer un parcours différent et le fichier importé sur une liseuse ne devient pas automatiquement une ressource synchronisée partout dans l’écosystème Kobo.</p>
      <p>Cette intégration convient à un utilisateur qui stocke ses PDF ou EPUB personnels dans Dropbox et souhaite les récupérer facilement sur la liseuse. Elle ne doit pas être confondue avec une synchronisation collaborative d’un document annoté.</p>
      <p>Pour les contraintes de format, reportez-vous à <a href="/guides/formats-fichiers-compatibles/">formats de fichiers compatibles</a>.</p>

      <h2 id="test">Un dossier de test révèle rapidement les limites</h2>
      <p>Créez un dossier Dropbox dédié avec un PDF, un EPUB non protégé et, si besoin, un document bureautique. Connectez le bloc-notes, importez le fichier, annotez-le puis exportez le résultat dans un sous-dossier différent. Regardez ensuite le comportement sur votre ordinateur et votre téléphone.</p>
      <ol><li>Vérifiez si la structure des dossiers est visible.</li><li>Contrôlez la direction des transferts.</li><li>Observez le nom du fichier exporté.</li><li>Testez une modification sur ordinateur.</li><li>Vérifiez s’il existe un conflit ou simplement deux copies.</li></ol>
      <p>Ce test vous indique si Dropbox fonctionne comme un vrai espace de travail pour l’appareil ou simplement comme une boîte d’entrée/sortie. Les deux peuvent être utiles, mais pour des besoins différents.</p>

      <h2 id="decision">Dropbox comme critère de choix</h2>
      <p>Rendez Dropbox éliminatoire uniquement si votre organisation ou vos habitudes reposent réellement dessus. Ensuite, définissez le niveau requis : transfert ponctuel, synchronisation de dossiers ou application complète. Si plusieurs clouds vous conviennent, donnez davantage de poids au logiciel de notes et à l’export final.</p>
      <p>Pour comparer les alternatives, consultez <a href="/guides/bloc-notes-numerique-google-drive/">Google Drive</a> et <a href="/guides/bloc-notes-numerique-onedrive/">OneDrive</a>, puis replacez le cloud dans le <a href="/guides/choisir-bloc-notes-numerique/">guide général de choix</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files" rel="noopener noreferrer">reMarkable : Dropbox et export</a></li>
        <li><a href="https://help.boox.com/hc/en-us/articles/8569457124628-Integrated-Third-Party-Cloud-Storage" rel="noopener noreferrer">BOOX : Dropbox intégré</a></li>
        <li><a href="https://support.supernote.com/en_US/transfer-files" rel="noopener noreferrer">Supernote : synchronisation Dropbox</a></li>
        <li><a href="https://help.kobo.com/hc/en-us/articles/360024775093-Add-non-protected-PDF-and-ePub-files-to-your-Kobo-eReader-using-your-computer" rel="noopener noreferrer">Kobo : ajout de fichiers via cloud et USB</a></li>
      </ul>
    """,

    "/guides/ecosysteme-ouvert-ou-ferme/": """
      <p class="article-answer"><strong>Un écosystème fermé ou spécialisé privilégie la cohérence d’un nombre limité de fonctions ; un écosystème ouvert privilégie la possibilité d’ajouter des applications et services.</strong> Pour un bloc-notes numérique, le bon choix dépend du nombre de tâches externes que vous devez intégrer. Si vos notes peuvent rester dans un workflow simple de carnets, PDF et export, la spécialisation peut être un avantage. Si une application métier est indispensable, l’ouverture peut devenir éliminatoire.</p>

      <h2 id="definition">« Fermé » ne veut pas dire « données prisonnières » et « ouvert » ne veut pas dire « tout fonctionne bien »</h2>
      <p>Ces mots sont souvent utilisés de manière trop absolue. Un appareil spécialisé peut offrir de bons exports PDF, cloud et USB tout en refusant l’installation d’applications. À l’inverse, une tablette Android peut installer de nombreuses apps mais conserver des formats natifs propres au fabricant pour certaines notes.</p>
      <p>Il est donc préférable de séparer deux questions : peut-on installer ce que l’on veut, et peut-on récupérer facilement ses données ? L’ouverture applicative et la portabilité documentaire ne sont pas la même chose.</p>
      <p>Le guide <a href="/guides/exporter-notes/">exporter ses notes</a> permet d’évaluer la seconde dimension indépendamment du système d’exploitation.</p>

      <h2 id="comparaison">Les compromis principaux entre système spécialisé et système ouvert</h2>
      <p>Un environnement spécialisé peut réduire le nombre de réglages et concentrer les optimisations sur l’écriture. Un environnement ouvert peut intégrer des applications de calendrier, stockage ou collaboration déjà utilisées ailleurs. Le coût de cette liberté est souvent plus de complexité et des expériences variables selon l’app.</p>
      <div class="table-wrapper"><table class="comp-table"><thead><tr><th>Critère</th><th>Système spécialisé</th><th>Système ouvert / Android</th></tr></thead><tbody>
        <tr><td>Simplicité</td><td>flux cohérent et limité</td><td>plus de choix et de réglages</td></tr>
        <tr><td>Applications tierces</td><td>absentes ou sélectionnées</td><td>large choix via store</td></tr>
        <tr><td>Optimisation E Ink</td><td>logiciel souvent pensé pour la dalle</td><td>variable selon l’application</td></tr>
        <tr><td>Cloud</td><td>intégrations choisies</td><td>intégrations + apps tierces</td></tr>
        <tr><td>Maintenance</td><td>moins de décisions utilisateur</td><td>plus de comptes, apps et mises à jour</td></tr>
      </tbody></table></div>
      <p>Le tableau ne désigne pas de vainqueur. Il montre plutôt le type de friction que vous acceptez : limitation choisie ou complexité choisie.</p>

      <h2 id="specialises">reMarkable et Supernote : spécialisation avec des sorties vers l’extérieur</h2>
      <p>reMarkable ne se présente pas comme une tablette Android générale. Son logiciel est centré sur les fichiers et carnets, avec applications compagnon, email, USB et intégrations Google Drive, Dropbox et OneDrive. L’absence de store d’applications limite les usages, mais réduit aussi les distractions et les incompatibilités d’apps.</p>
      <p>Supernote suit également une logique de prise de notes spécialisée tout en développant ses propres outils : reconnaissance manuscrite, liens entre notes, cloud, Dropbox, Google Drive, OneDrive, USB et transferts locaux. Le système peut être riche sans être un Android généraliste.</p>
      <p>Pour un utilisateur qui veut surtout écrire et organiser, ces environnements doivent être jugés sur leurs fonctions natives plutôt que pénalisés pour l’absence d’un store.</p>

      <h2 id="android">BOOX : l’ouverture Android apporte des applications, avec une couche E Ink à gérer</h2>
      <p>Les BOOX récents comme le Go 10.3 Gen II utilisent Android et donnent accès au Google Play Store. Cela permet d’installer OneNote, Libby, Drive ou d’autres applications. L’avantage est évident lorsqu’une app précise fait partie du workflow et n’existe pas dans un système spécialisé.</p>
      <p>Mais l’application a été conçue d’abord pour des écrans classiques. Scroll, animations et rafraîchissements peuvent donc nécessiter des réglages spécifiques. BOOX fournit des outils et modes pour adapter l’affichage, mais cette flexibilité demande plus d’intervention de l’utilisateur.</p>
      <p>Le guide <a href="/guides/tablette-classique-ou-tablette-e-ink/">tablette classique ou E Ink</a> aide à décider si l’application est suffisamment centrale pour accepter ce compromis.</p>

      <h2 id="lecture">Kindle et Kobo : des écosystèmes fermés autour de la lecture, mais de plus en plus connectés</h2>
      <p>Kindle Scribe reste lié à l’écosystème Amazon, mais les modèles 2025+ ont élargi les connexions à Google Drive, OneDrive et OneNote pour plusieurs workflows. Kobo conserve sa bibliothèque et ses règles de DRM, tout en proposant Google Drive ou Dropbox sur certains modèles et des carnets avec plusieurs formats d’export.</p>
      <p>Ces appareils montrent que « fermé » évolue dans le temps. Une plateforme peut ajouter des portes vers l’extérieur sans devenir Android. Lors de l’achat, utilisez donc la documentation actuelle et non la réputation d’une marque acquise plusieurs années plus tôt.</p>
      <p>Si votre usage combine livres et notes, consultez <a href="/guides/liseuse-ou-bloc-notes-numerique/">liseuse ou bloc-notes numérique</a>.</p>

      <h2 id="securite">L’ouverture modifie aussi la surface de gestion et de sécurité</h2>
      <p>Installer davantage d’applications signifie gérer davantage de comptes, permissions, mises à jour et données en arrière-plan. Dans un contexte d’entreprise, une app peut être interdite ou un tenant cloud peut refuser une autorisation. Un appareil spécialisé réduit parfois cette surface, mais peut dépendre plus fortement de son propre service cloud.</p>
      <p>Il n’existe donc pas de réponse universelle sur la sécurité. Vérifiez le chiffrement, le verrouillage, les politiques de comptes et surtout les exigences de votre organisation. Pour des données sensibles, conservez une méthode d’export local ou une archive indépendante lorsque c’est autorisé.</p>
      <p>Le guide <a href="/guides/transfert-notes-vers-ordinateur/">transfert vers ordinateur</a> présente les options qui évitent de faire du cloud la seule voie de sortie.</p>

      <h2 id="decision">Le test pour savoir combien d’ouverture vous avez vraiment besoin</h2>
      <p>Listez toutes les applications et services que vous utilisez dans une semaine. Marquez ceux qui sont indispensables sur la tablette elle-même et ceux qui peuvent rester sur l’ordinateur ou le téléphone. Si aucun outil tiers n’est réellement indispensable, l’ouverture Android peut être une complexité sans bénéfice. Si OneNote ou une app métier doit fonctionner directement sur l’appareil, elle peut devenir un critère éliminatoire.</p>
      <p>Après ce tri, utilisez le <a href="/comparatifs/remarkable-vs-boox/">comparatif reMarkable vs BOOX</a> ou le <a href="/guides/choisir-bloc-notes-numerique/">guide de choix global</a> pour comparer des produits qui répondent déjà au niveau d’ouverture requis.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files" rel="noopener noreferrer">reMarkable : sorties et intégrations</a></li>
        <li><a href="https://shop.boox.com/products/go103gen2" rel="noopener noreferrer">BOOX : Android 15 et Google Play</a></li>
        <li><a href="https://support.supernote.com/en_US/transfer-files" rel="noopener noreferrer">Supernote : cloud, USB et transferts</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/Tuar1obhcxaS8hVUKd" rel="noopener noreferrer">Amazon : connexions Kindle Scribe</a></li>
        <li><a href="https://help.kobo.com/hc/en-us/articles/15335985512983-Add-books-to-your-eReader-using-Google-Drive" rel="noopener noreferrer">Kobo : Google Drive sur modèles compatibles</a></li>
      </ul>
    """,
}
