---
name: editorial-image-planner
description: Décide si une page d'aspirateurs-chantier.fr a réellement besoin d'une image éditoriale générée, puis crée une requête compatible avec l'automatisation BFL. À utiliser après la rédaction et avant la publication.
license: MIT
metadata:
  adapted_for: aspirateurs-chantier.fr
  generator: Black Forest Labs FLUX API
  default_model: FLUX.2 Pro Preview
---

# Editorial Image Planner

## Objectif

Ajouter des images uniquement lorsqu'elles améliorent réellement la compréhension d'un usage, d'un environnement de chantier ou d'un geste de travail. Une image générée n'est jamais un quota SEO, un remplissage décoratif, une photo produit officielle ni une preuve de test.

Le workflow est piloté par `.content/image-requests/*.json`. Le moteur ne génère que les requêtes explicitement marquées `required: true`, `allow_ai_generation: true`, `truth_risk: LOW` et `status: PENDING` ou `REGENERATE`.

## 1. Décider si une image est utile

Créer une image uniquement si elle remplit un rôle éditorial clair, par exemple :

- montrer la relation entre un outil portatif, son flexible et un aspirateur générique ;
- rendre concret un environnement d'atelier ou de rénovation ;
- visualiser un geste de captage à la source difficile à comprendre par le texte seul ;
- distinguer visuellement nettoyage de sol, captage sur outil et collecte de débris ;
- apporter une respiration éditoriale à une page longue lorsque la scène reste sémantiquement utile.

Ne pas générer d'image si elle serait seulement décorative, si une photo réelle est nécessaire, ou si le texte suffit parfaitement.

Par défaut : **0 ou 1 image générée par page**.

## 2. Interdictions de génération IA

Mettre `allow_ai_generation: false` lorsque l'image devrait représenter fidèlement :

- un Bosch, Kärcher, Makita, Festool, Nilfisk, DeWalt, Mirka ou autre produit identifiable précis ;
- une référence, génération, accessoire ou système propriétaire exact ;
- un logo, emballage ou identité de marque ;
- un filtre, raccord, classe L/M/H ou dispositif de sécurité dont l'exactitude visuelle est importante ;
- une interface, tableau, graphique, benchmark ou résultat de mesure ;
- une scène présentée comme un test hands-on réellement effectué par le site ;
- une comparaison visuelle qui pourrait être interprétée comme une preuve de performance.

Dans ces cas, utiliser `BLOCKED` si une vraie photo ou source officielle serait utile.

## 3. Images autorisées

Privilégier des scènes génériques et plausibles :

- aspirateur eau/poussière non marqué dans un atelier réel ;
- ponceuse générique raccordée à un flexible d'aspiration ;
- nettoyage de poussières ou de débris dans une rénovation ;
- captage à la source sur outil électroportatif ;
- organisation d'un atelier avec plusieurs postes ;
- tuyau, établi, sol de chantier et consommables génériques sans référence identifiable.

Le rendu doit rester photoréaliste et documentaire : lumière naturelle ou d'atelier crédible, proportions réalistes, matériaux plausibles, légère imperfection, aucun look publicitaire. Éviter texte généré, logos inventés, machines futuristes et compositions catalogue.

## 4. Créer la requête

Copier `.content/image-requests/_template.json` vers `.content/image-requests/<slug>-<slot>.json`.

Renseigner au minimum : `page`, `required`, `reason`, `allow_ai_generation`, `truth_risk`, `status`, `marker`, `placement`, `output_path`, `prompt`, `alt`, dimensions et éventuellement `caption` / `seed`.

Valeurs par défaut :

- 1024 × 672 px ;
- `prompt_upsampling: true` ;
- `seed: null` ;
- sortie sous `assets/generated/`.

## 5. Marker et régénération

Le `marker` doit être une chaîne stable présente dans la source de vérité de la page et dans le HTML généré. Un commentaire HTML dédié est idéal, mais un H2 stable peut aussi servir de marker avec `placement: before` ou `after` : le H2 est alors conservé et sert d'ancre de réinsertion.

Ce mécanisme est particulièrement utile sur ce dépôt : si les pages usages/guides sont régénérées, l'image déjà générée est réinsérée au prochain passage sans nouvel appel BFL.

## 6. Prompt photographique

Le prompt doit préciser : sujet, action, environnement, lumière, cadrage, matériaux, niveau de poussière réaliste, rôle du flexible, esthétique photographique et contraintes de vérité.

Pour les scènes de chantier, terminer généralement par une contrainte de ce type :

`photorealistic editorial documentary photography, realistic workshop or renovation environment, natural practical lighting, realistic proportions and materials, generic unbranded wet/dry dust extractor and tools, no visible brand logo, no watermark, no readable labels, no advertising composition, no implication of a specific tested product, candid framing`

Ne jamais demander au modèle d'inventer un Bosch/Kärcher/Makita précis, une certification de poussière ou un résultat de test.

## 7. Vérification avant PENDING

Confirmer que :

- l'image répond à une question visuelle réelle ;
- une image générique ne trompe pas le lecteur ;
- aucune photo produit officielle n'est nécessaire ;
- le prompt ne revendique aucun test ou résultat ;
- le marker est stable ;
- l'alt décrit simplement la scène ;
- le chemin de sortie est unique.

En cas de doute sur la fidélité requise, choisir `BLOCKED`.
