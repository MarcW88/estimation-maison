---
name: evidence-based-reviews
description: Encadrer les reviews, avis et recommandations produit par des niveaux de preuve explicites sans inventer de test hands-on. Adapté du skill evidence-based-reviews de rampstackco/claude-skills et de sa réutilisation dans MarcW88/italiaanse-percolator.
metadata:
  upstream: https://github.com/rampstackco/claude-skills/tree/main/skills/evidence-based-reviews
  adapted_via: https://github.com/MarcW88/italiaanse-percolator/tree/main/.agents/skills/evidence-based-reviews
  adapted_for: bloc-notes-numeriques.fr
---

# Evidence-Based Reviews — adaptation bloc-notes-numeriques.fr

Utiliser pour toute page `REVIEW`, tout avis sur une marque ou un produit et toute recommandation dont le jugement dépasse de simples spécifications.

## Règle centrale

Ne jamais revendiquer une expérience pratique qui n'a pas eu lieu.

Une synthèse documentaire honnête peut produire une forte valeur éditoriale si elle vérifie les faits, confronte plusieurs sources et explique les conséquences pratiques. Elle ne doit jamais être déguisée en test maison.

## Les quatre niveaux de preuve

### Tier 1 — spécifications fabricant vérifiées

Sources : fabricant, documentation officielle, manuel, support officiel.

Utiliser pour : dimensions, écran, OS, stockage, formats, compatibilités, accessoires, fonctions, garantie annoncée, statut d'un modèle.

Une fiche fabricant peut établir un fait. Elle ne suffit pas à démontrer qu'un produit est agréable, fiable ou meilleur qu'un autre.

### Tier 2 — synthèse d'expérience utilisateurs

Sources : corpus d'avis marchands crédibles, forums, communautés, retours propriétaires ou support public.

Règles :

- chercher des motifs récurrents, pas une anecdote isolée ;
- nommer les corpus ou communautés consultés ;
- indiquer la taille du corpus lorsque celle-ci est connue ;
- conserver les désaccords lorsqu'ils existent ;
- ne jamais convertir « des utilisateurs rapportent » en « nous avons constaté ».

Quelques témoignages isolés ne permettent pas de parler de tendance.

### Tier 3 — triangulation de sources expertes

Comparer plusieurs tests ou analyses indépendantes nommées.

La triangulation doit faire apparaître les convergences et divergences. Ne pas transformer des avis contradictoires en consensus artificiel.

Utiliser notamment pour : ressenti d'écriture, latence, qualité d'écran, autonomie observée, ergonomie, expérience logicielle ou comparaison avec des concurrents lorsque le site n'a pas lui-même mesuré ces éléments.

### Tier 4 — test hands-on réel

Seulement si des données de première main existent réellement et sont traçables : appareil testé, durée, conditions, mesures, photos, notes ou protocole.

Préciser l'étendue réelle du test. Une prise en main courte n'est pas un test longue durée.

## Registre de preuve par page

Avant la rédaction d'une review, produire au minimum :

| Claim / question | Evidence tier | Source | Status | Action |
|---|---|---|---|---|

Statuts recommandés : `VERIFIED`, `SUPPORTED`, `INFERRED`, `UNKNOWN`, `OUTDATED`, `CONTRADICTED`.

`INFERRED` reste une déduction éditoriale et doit être formulée comme telle. `UNKNOWN` ne doit pas être rempli par connaissance modèle.

## Valeur originale sans faux test

Une review documentaire doit créer une synthèse qu'aucune source individuelle ne fournit à elle seule. Les formes de valeur utiles incluent :

- confrontation de spécifications et de conséquences pratiques ;
- comparaison de générations ;
- compatibilités difficiles à comprendre ;
- coût complet avec accessoires ou services ;
- critères permettant de dire pour qui le produit est pertinent ou non ;
- contradictions entre sources indépendantes ;
- patterns utilisateurs suffisamment documentés ;
- alternative plus rationnelle dans certaines situations.

Réarranger les puces du fabricant n'est pas une analyse originale.

## Méthodologie visible

Une review doit permettre au lecteur de comprendre sobrement sur quoi repose l'avis. La formulation dépend de la page et ne doit pas devenir un bloc standard cloné partout.

Exemples acceptables :

- « Cette analyse croise la documentation officielle et plusieurs essais indépendants ; nous n'avons pas réalisé de test physique. »
- « Nous avons vérifié les compatibilités dans la documentation du fabricant et confronté les observations de deux tests indépendants. »

Ne pas répéter cette précaution dans chaque section.

## Recommandations et désavantages

Un verdict doit être traçable à des critères et à des preuves. Montrer au moins la limite réellement décisive lorsqu'une recommandation est faite. Ne jamais masquer un désavantage parce qu'il réduit la conversion affiliée.

## Données structurées

Le markup est lui aussi une affirmation. Ne pas utiliser un schéma ou une propriété qui laisse entendre un test, une note ou une expérience inexistante. Les données structurées doivent refléter exactement le niveau de preuve du contenu visible.

## Transparence affiliée

La présence de liens affiliés doit être expliquée clairement selon les règles du site. La commission ne peut pas influencer le classement, le verdict ni l'ordre des recommandations.

## Workflow

1. Inventorier les preuves réellement disponibles.
2. Fixer les critères avant le verdict.
3. Vérifier les faits Tier 1 à la source primaire.
4. Utiliser Tier 2 uniquement avec un corpus suffisamment crédible.
5. Trianguler les sources Tier 3 et conserver leurs désaccords.
6. N'utiliser Tier 4 que si un test réel est documenté.
7. Synthétiser les conséquences pour la décision d'achat.
8. Déclarer sobrement le niveau de preuve.
9. Passer ensuite par `fact-check`, la finition éditoriale et la QA du workflow appelant.

## Échecs bloquants

FAIL si :

- « nous avons testé » sans Tier 4 réel ;
- expérience utilisateur issue de Tier 2/3 transformée en expérience propre ;
- affirmation de performance importante basée uniquement sur une fiche fabricant ;
- anecdote isolée présentée comme tendance ;
- source experte anonyme ou vague ;
- spécification provenant d'un agrégateur alors qu'une source officielle existe et contredit ou permet de vérifier l'information ;
- recommandation sans critère identifiable ;
- trou de preuve rempli par supposition.

Une lacune explicitement déclarée est préférable à une donnée inventée.
