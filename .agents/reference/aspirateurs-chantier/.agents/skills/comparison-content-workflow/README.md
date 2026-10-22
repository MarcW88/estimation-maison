# Comparison Content Workflow

Workflow de production des pages `/comparatifs/` d'aspirateurs-chantier.fr, adapté du workflow récent de `MarcW88/bloc-notes-numerique`.

## Principe

Le workflow est un **orchestrateur** : l'essentiel de la méthode vient de skills réutilisables/vendored et la couche custom reste limitée aux décisions propres aux aspirateurs de chantier.

Chaîne principale :

1. intention et cluster (`seo-keyword`) ;
2. JTBD lorsque le contexte change la décision ;
3. conservation de la valeur existante (`seo-content-audit`) ;
4. preuves + fact-check ;
5. valeur affiliée originale ;
6. couche custom légère : scope, critères et gates métier ;
7. brief ;
8. rédaction ;
9. humanizer / anti-slop / SEO / maillage / QA ;
10. `comparison-analysis-workflow / PUBLISH_REVIEW` ;
11. validation humaine.

## Ce qui n'est plus obligatoire

Le workflow **n'impose pas** :

- scoring numérique ;
- pondérations dont la somme vaut 100 ;
- hard gates formels dans un JSON ;
- exhaustive product universe ;
- equivalence engine formel ;
- Total Solution Cost sur chaque page ;
- nombre minimum de mots, H2, liens ou sources ;
- structure éditoriale identique entre comparatifs.

Ces outils restent utilisables lorsqu'ils améliorent réellement la décision.

## Données de comparaison

`.content/comparisons/<slug>.json` est un support méthodologique. Les champs doivent refléter la méthode effectivement utilisée, et non l'inverse.

Champs courants : intention, candidats, exclusions importantes, critères, preuves, logique de recommandation, contexte de mesure, coûts pertinents et statut. `scores`, `weights` et `ranking` sont facultatifs.

## Scripts

- `scripts/validate_comparison_data.py` vérifie l'intégrité des données présentes sans imposer de scoring.
- `scripts/score_comparison.py` est un **outil optionnel** pour les pages dont le brief justifie explicitement une méthode chiffrée. Il ne doit pas être exécuté automatiquement sur tous les comparatifs.

## Gates métier Aspirateurs Chantier

Vérifier notamment :

- classe L/M/H explicitement sourcée ;
- filtre HEPA ≠ classe appareil ;
- débit/dépression comparés avec contexte de mesure ;
- décolmatage ≠ certification ;
- wet/dry ≠ aptitude aux poussières dangereuses ;
- compatibilité exacte des plateformes batterie ;
- capacité brute/nette/eau distinguée si nécessaire ;
- aucun faux test ni autonomie réelle inventée.

## Gouvernance 80/20

Voir `.agents/skills/comparison-skill-stack.json` et `validate_comparison_skill_stack.py`.

Le ratio est calculé sur les composants d'orchestration : les skills génériques doivent représenter au moins 80 % du stack, les workflows custom restant minoritaires.

## Publication

`noindex, follow` est conservé jusqu'à :

1. validation machine ;
2. `PUBLISH_REVIEW` PASS ;
3. validation humaine explicite ;
4. instruction explicite d'indexer.
