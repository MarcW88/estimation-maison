# Direction visuelle — aspirateurs-chantier.fr

## Positionnement

Le site doit ressembler à un média technique spécialisé dans les aspirateurs de chantier : précis, robuste, sobre, crédible et orienté décision.

Il ne doit pas ressembler à :

- un catalogue Amazon ou une grille d'affiliation ;
- une landing page SaaS générique ;
- un faux laboratoire industriel ;
- un site bricolage grand public surchargé d'icônes ;
- une interface manifestement assemblée à partir de cartes standards.

L'identité doit évoquer l'atelier et le chantier par la précision des données, la hiérarchie et les détails fonctionnels, pas par des textures industrielles décoratives.

## Public et objectif

Le lecteur peut être un bricoleur avancé, un artisan ou un professionnel qui cherche à comprendre une gamme, une classe de poussière, un système de décolmatage, une compatibilité outil ou un compromis mobilité/capacité.

Sur une page éditoriale, l'interface doit l'aider à :

1. comprendre rapidement l'angle de décision ;
2. distinguer les familles, profils ou technologies qui changent réellement le choix ;
3. lire les preuves, limites et données techniques sans fausse précision ;
4. poursuivre vers une fiche modèle, un comparatif spécialisé, un usage ou un guide lorsque la question devient plus précise.

## Principes visuels

- Direction éditoriale technique plutôt qu'e-commerce.
- Information dense mais hiérarchisée ; éviter les grands vides artificiels.
- Les tableaux, classes L/M/H et valeurs techniques doivent être lisibles avant d'être décoratifs.
- Les composants doivent soutenir la lecture : answer box, tableaux, sommaire, sources et liens associés.
- Les pages d'un même cluster peuvent partager un système visuel, mais ne doivent pas paraître être le même template avec un titre différent.
- Les appels commerciaux restent secondaires par rapport au raisonnement éditorial.
- Responsive conçu pour la lecture de données : reflow des blocs et scroll contrôlé des tableaux.

## Système existant à préserver

Le design actuel repose sur les tokens de `style.css` :

- fond principal `#F8FAFB` ;
- surface `#FFFFFF` ;
- texte `#0F1923` ;
- bleu principal `#1B4FD8` ;
- accent orange `#E05E1A` ;
- bordure `#D1D9E0` ;
- Space Grotesk pour la hiérarchie ;
- Inter pour le corps ;
- JetBrains Mono pour les données et métadonnées.

Les classes de poussière utilisent un code couleur fonctionnel distinct pour L, M et H. Toute évolution doit conserver un contraste WCAG AA et ne jamais reposer uniquement sur la couleur pour transmettre le niveau de risque.

## Pages marques : composants attendus

Une page marque peut utiliser, lorsque le contenu le justifie :

- un hero éditorial compact avec type de contenu, H1, lead et date de vérification ;
- une `answer-box` qui donne l'angle de décision principal ;
- des tableaux dans `table-wrap` pour synthétiser une gamme ou comparer des références ;
- un sommaire latéral `toc-list` reflétant les vrais H2 ;
- un encadré d'affiliation discret et explicite ;
- des liens vers modèles, usages, comparatifs et guides réellement pertinents ;
- un bloc sources/méthode visible lorsque des données techniques sont utilisées.

L'absence d'une carte ou d'un tableau n'est pas un défaut si la structure éditoriale fonctionne mieux sans.

## Pages comparatifs : composants attendus

Une page comparatif doit aider à arbitrer, pas seulement empiler des fiches produits. Elle peut utiliser :

- un hero éditorial compact avec l'intention et la date de vérification ;
- une `answer-box` qui pose immédiatement la règle de décision ;
- un module de décision propre à l'intention lorsque plusieurs axes doivent être compris avant le tableau ;
- un tableau comparatif dans un wrapper scrollable lorsque les colonnes sont réellement utiles ;
- une indication de scroll sur mobile lorsque le tableau dépasse le viewport ;
- un sommaire latéral sticky sur desktop et repliable avant l'article sur tablette/mobile ;
- un handoff mobile avant la lecture longue, éditorial si aucun CTA existant n'est pertinent ;
- des sources et limites aussi visibles que les recommandations.

Un comparatif ne doit pas transformer un score arbitraire en élément visuel dominant. Les modules de décision doivent refléter l'intention de la page : classe, mobilité, mesure, process, collecte ou encombrement selon le cas.

## Règles anti-design générique / IA

Éviter notamment :

- la succession systématique de cartes identiques pour chaque idée ;
- les énormes H1 centrés sans information concrète ;
- les glows, glassmorphism et ombres lourdes ;
- les dégradés bleus/violets génériques ;
- les pills décoratives répétées ;
- les icônes sans fonction ;
- la symétrie parfaite de toutes les sections ;
- les barres de score ou notes pseudo-scientifiques sans méthode ;
- les faux badges de confiance ou d'urgence ;
- la répétition agressive de boutons d'achat ;
- des blocs « avantages / inconvénients » identiques sur toutes les pages lorsqu'ils ne servent pas l'intention ;
- une interface qui mime un tableau de bord alors que la page est éditoriale.

Ne jamais affirmer qu'un design a été généré par IA. On peut signaler une accumulation de conventions génériques fréquemment observées dans des interfaces générées ou assemblées automatiquement.

## Confiance éditoriale et affiliation

- La date de vérification doit être visible lorsqu'elle est pertinente.
- Une analyse documentaire ne doit pas être mise en scène comme un test physique.
- Les limites et incompatibilités doivent être aussi visibles que les avantages.
- Les liens affiliés sont identifiables et ne doivent pas dominer la page.
- Les sources et la méthode doivent pouvoir être trouvées sans chercher dans le footer.
- Les chiffres techniques ne doivent pas être présentés comme comparables lorsqu'ils ne partagent pas le même protocole ou point de mesure.

## Accessibilité et interaction

- Tous les contrôles doivent fonctionner au clavier.
- Le focus doit être visible sur liens, boutons, navigation et contrôles.
- Le menu mobile doit être réellement ouvrable, navigable et refermable.
- Un bouton burger sans menu fonctionnel est un défaut bloquant de navigation mobile.
- Les tableaux larges doivent rester utilisables sans créer de débordement horizontal de toute la page.
- Les ancres du sommaire doivent pointer vers des IDs existants.
- Sur les pages longues, le sommaire mobile doit apparaître avant l'article et rester repliable.
- Aucun contenu essentiel ne doit disparaître à un breakpoint.

## Critères de validation d'une page éditoriale

Une page est visuellement validée si :

1. son angle de décision est compris rapidement ;
2. la hiérarchie éditoriale reste claire sur desktop et mobile ;
3. les tableaux et données techniques restent lisibles sans overflow global ;
4. le sommaire aide réellement à naviguer ;
5. le niveau de preuve et l'affiliation sont visibles sans écraser le contenu ;
6. la page appartient clairement à aspirateurs-chantier.fr tout en gardant une architecture adaptée à son intention ;
7. la navigation et les états clavier sont fonctionnels ;
8. aucun pattern générique important ne domine la composition.
