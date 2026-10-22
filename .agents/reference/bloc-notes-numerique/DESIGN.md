# Direction visuelle — bloc-notes-numeriques.fr

## Positionnement

Le site doit ressembler à un média éditorial spécialisé dans le papier numérique : calme, précis, utile et légèrement premium.

Il ne doit pas ressembler à :

- une landing page SaaS ;
- un catalogue Amazon ;
- un faux laboratoire de test ;
- un blog technologique générique ;
- une interface manifestement générée par IA.

## Public et objectif

Le lecteur cherche à choisir un bloc-notes numérique adapté à un usage concret : travail, études, réunions, annotation de PDF, lecture ou dessin.

L’interface doit l’aider à comprendre les compromis entre les produits avant de l’envoyer vers un marchand.

## Principes visuels

- Direction éditoriale inspirée du papier, de l’écriture et de l’encre électronique.
- Mise en page lisible, avec une densité d’information maîtrisée.
- Hiérarchie typographique nette et rythme moins mécanique qu’une succession de cartes.
- Espaces blancs généreux, sans vider artificiellement les pages.
- Photographies de produits crédibles et légalement utilisables.
- Illustrations linéaires ou annotations manuscrites utilisées avec parcimonie.
- Tableaux comparatifs sobres, lisibles et cohérents entre les pages.
- États interactifs visibles au clavier comme à la souris.
- Responsive pensé pour le contenu, pas seulement obtenu par empilement automatique.

## Palette initiale

Ces couleurs servent de direction de départ et doivent être implémentées comme tokens, pas répétées en valeurs brutes dans les composants.

| Rôle | Couleur |
|---|---|
| Fond principal | `#F7F6F1` |
| Surface | `#FFFFFF` |
| Texte principal | `#202321` |
| Texte secondaire | `#5F655F` |
| Vert principal | `#52675A` |
| Accent terracotta | `#C66A4A` |
| Fond secondaire | `#ECECE7` |
| Bordure | `#D8D9D3` |

Vérifier les contrastes avant validation. Ajuster les couleurs si nécessaire pour respecter WCAG AA.

## Typographie

Direction recommandée :

- une serif éditoriale pour les grands titres, par exemple Newsreader ou Source Serif 4 ;
- une sans-serif très lisible pour le corps, les menus et les données, par exemple Manrope.

Ne pas multiplier les familles ni utiliser une police manuscrite pour du contenu essentiel. Les annotations manuscrites éventuelles restent décoratives et rares.

## Composants distinctifs

- Verdict rapide : « idéal pour », « à éviter si », avantage principal et limite principale.
- Fiche produit avec critères standardisés.
- Tableau comparatif stable entre tous les modèles.
- Encadré méthodologique et niveau de preuve.
- Comparaison directe « modèle A / modèle B ».
- Note éditoriale courte pouvant évoquer une annotation au stylet.
- Date de test ou de vérification clairement visible.
- Double action distincte : « Lire le test » et « Voir le prix ».

## Règles anti-design IA

Éviter notamment :

- les énormes titres centrés suivis de deux boutons sans information concrète ;
- les dégradés violets ou bleus génériques ;
- les glows, glassmorphism et ombres épaisses ;
- les coins très arrondis sur tous les éléments ;
- les pills et badges décoratifs répétés ;
- les grilles systématiques de trois cartes identiques ;
- les icônes placées uniquement pour remplir l’espace ;
- les illustrations abstraites sans lien avec le produit ;
- les animations dispersées et sans fonction ;
- les formulations vagues telles que « révolutionnez votre productivité » ;
- les faux témoignages, fausses statistiques ou faux signaux d’urgence ;
- les notes globales sans méthode explicite ;
- les boutons d’achat répétés après chaque paragraphe ;
- une symétrie parfaite et répétitive sur toute la page.

Une carte doit regrouper une information réellement autonome. Une section n’a pas besoin d’une carte par défaut.

## Affiliation et confiance

- Identifier sans ambiguïté les liens affiliés.
- Ne pas masquer une publicité sous l’apparence d’un verdict éditorial.
- Présenter au moins une limite réelle pour chaque produit recommandé.
- Expliquer la méthodologie et les critères de classement.
- Ne pas prétendre avoir testé un appareil sans preuve documentée.
- Distinguer : testé, pris en main, analysé à partir de documentation, ou simplement comparé.
- Présenter les prix comme datés et susceptibles d’évoluer.

## Critères de validation

Une page est visuellement validée si :

1. son objectif et son action principale sont compris rapidement ;
2. elle paraît appartenir à un média spécialisé identifiable ;
3. la hiérarchie reste claire sur mobile et desktop ;
4. les informations commerciales ne dominent pas l’éditorial ;
5. les composants sont cohérents sans rendre toutes les sections identiques ;
6. le contraste, le focus clavier et la structure sémantique sont corrects ;
7. aucun pattern anti-design IA important n’est présent.
