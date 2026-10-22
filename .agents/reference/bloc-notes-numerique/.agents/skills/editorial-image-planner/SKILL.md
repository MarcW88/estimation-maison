---
name: editorial-image-planner
description: Décide si une page de bloc-notes-numeriques.fr a réellement besoin d'une image éditoriale générée, puis crée une requête compatible avec l'automatisation BFL. À utiliser après la rédaction et avant la publication.
license: MIT
metadata:
  adapted_for: bloc-notes-numeriques.fr
  generator: Black Forest Labs FLUX API
  default_model: FLUX.2 Pro Preview
---

# Editorial Image Planner

## Objectif

Ajouter des images uniquement lorsqu'elles améliorent réellement la page. Une image générée n'est jamais un quota SEO, un remplissage décoratif ou une preuve produit.

Le workflow de génération est piloté par les fichiers `.content/image-requests/*.json`. Le moteur ne génère que les requêtes explicitement marquées `required: true`, `allow_ai_generation: true` et `status: PENDING` ou `REGENERATE`.

## 1. Décision : image nécessaire ou non

Créer une image uniquement si au moins une de ces conditions est satisfaite :

- elle rend un contexte d'usage concret plus immédiatement compréhensible ;
- elle permet de visualiser une situation, un environnement ou un geste difficile à saisir par le texte seul ;
- elle améliore nettement la compréhension d'une section sans prétendre représenter une preuve factuelle ;
- elle apporte une vraie respiration éditoriale à une page longue lorsque cette respiration a aussi une fonction sémantique claire.

Ne pas générer d'image si :

- elle serait seulement décorative ;
- la page est déjà suffisamment illustrée ;
- une vraie capture, photo officielle ou illustration factuelle serait plus appropriée ;
- l'image risque d'être interprétée comme une preuve d'un test ou d'une expérience réelle ;
- le texte suffit parfaitement à accomplir la tâche du lecteur.

Par défaut, **0 ou 1 image générée par page**. Une deuxième image exige un rôle éditorial distinct et explicite.

## 2. Interdictions de génération IA

Mettre `allow_ai_generation: false` lorsque l'image devrait représenter fidèlement :

- un produit identifiable précis ;
- un logo ou une identité de marque ;
- une interface logicielle, une capture d'écran ou un menu ;
- une caractéristique technique dont l'exactitude visuelle compte ;
- un tableau, graphique, benchmark ou résultat de test ;
- un emballage, accessoire ou connectique censé correspondre exactement à un produit réel ;
- une personne réelle identifiable ;
- une scène présentée comme un test hands-on du site.

Dans ces cas, conserver éventuellement la requête avec `status: BLOCKED` afin de documenter qu'une vraie image est nécessaire, mais ne pas déclencher BFL.

## 3. Types d'images autorisés

Privilégier les scènes génériques, plausibles et éditoriales :

- prise de notes pendant une réunion ;
- étudiant utilisant un appareil E Ink générique dans un contexte de cours ;
- lecture et annotation de documents sans interface ou marque identifiable ;
- bureau, bibliothèque, déplacement, travail nomade ;
- geste d'écriture ou contexte d'organisation documentaire.

Le rendu doit être photoréaliste et sobre : lumière naturelle, matériaux plausibles, imperfections réalistes, photographie éditoriale. Éviter les compositions publicitaires, les appareils futuristes, les logos inventés et le texte généré dans l'image.

## 4. Créer la requête

Copier `.content/image-requests/_template.json` vers :

`.content/image-requests/<slug>-<slot>.json`

Renseigner au minimum :

- `page` : chemin du fichier HTML généré ;
- `required` : décision éditoriale ;
- `reason` : pourquoi l'image est utile ;
- `allow_ai_generation` : garde-fou de vérité ;
- `status` : `PENDING`, `BLOCKED`, `NOT_NEEDED`, `GENERATED` ou `REGENERATE` ;
- `marker` : commentaire HTML unique ;
- `output_path` : toujours sous `assets/generated/` ;
- `prompt` : brief photographique complet ;
- `alt` : description utile et concise ;
- dimensions, `prompt_upsampling` et éventuellement `seed`.

Pour BFL FLUX.2 [pro], utiliser par défaut :

- `width: 1024` ;
- `height: 672` ;
- `prompt_upsampling: true` ;
- `seed: null` sauf besoin explicite de reproductibilité.

FLUX.2 n'utilise pas de negative prompt. Décrire positivement le rendu souhaité et intégrer les contraintes utiles dans le prompt.

## 5. Placer le marqueur dans la source de vérité

Le `marker` doit être présent **dans la source qui génère la page**, pas uniquement dans le HTML final.

Exemple :

```html
<!-- EDITORIAL_IMAGE:prise-notes-reunion -->
```

Le placer à l'endroit exact où l'image apporte le plus de valeur. Éviter de mettre automatiquement toutes les images juste sous le H1.

Lors de l'exécution GitHub Actions, le script remplace ce marqueur dans le HTML généré par la balise `<figure>` correspondante. Si le site est régénéré plus tard et que le marqueur réapparaît, l'automatisation réinsère l'image existante sans la régénérer.

## 6. Prompt photographique

Le prompt doit décrire :

- sujet et action ;
- environnement ;
- lumière ;
- cadrage ;
- matériau et détails physiques utiles ;
- esthétique photographique ;
- contraintes de vérité.

Terminer généralement par des contraintes du type :

`photorealistic editorial photography, natural light, realistic proportions and materials, generic unbranded device, blank or non-readable screen content, no visible logo or watermark, candid documentary framing`

Ne pas demander au modèle d'inventer une marque, un écran lisible ou une référence produit précise.

## 7. Vérification avant commit

Avant de créer une requête `PENDING`, confirmer :

- l'image a un rôle explicite ;
- aucune vraie image n'est nécessaire à la place ;
- la scène peut être générique sans induire le lecteur en erreur ;
- le prompt n'invente pas une preuve ;
- le marqueur est présent dans la source de vérité ;
- l'alt décrit l'image et non une intention SEO ;
- le chemin de sortie est unique.

Si un doute subsiste sur la fidélité nécessaire, choisir `BLOCKED` plutôt que générer.
