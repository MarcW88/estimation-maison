# Comparison Content Workflow

Workflow portable pour créer des comparatifs produits SEO/GEO orientés affiliation.

## Ce qu'il ajoute par rapport au workflow Guides

Le cœur n'est plus uniquement éditorial. Il impose : intention, univers produit, équivalence, evidence ledger, critères avant gagnant, pondération, hard gates, scoring, justification du ranking, couche affiliation, rédaction et QA.

## Fichier obligatoire par comparatif

Créer `.content/comparisons/<slug>.json` à partir de la méthode du projet.

## Utilisation recommandée

> Applique `comparison-content-workflow` à `/comparatifs/meilleur-bloc-notes-numerique/`.
> Définis les critères et poids avant de scorer.
> Utilise uniquement des sources vérifiées.
> Ne tiens jamais compte des commissions dans le classement.
> Garde la page noindex jusqu'à validation.

## Scripts

- `scripts/validate_comparison_data.py` vérifie la structure méthodologique.
- `scripts/score_comparison.py` calcule les scores brut et ajusté par confiance.

## Important

Un score n'est pas une vérité scientifique. Il sert à expliciter les arbitrages, rendre le ranking traçable, empêcher les critères de changer après le résultat et documenter l'incertitude. Il ne remplace jamais le jugement éditorial.
