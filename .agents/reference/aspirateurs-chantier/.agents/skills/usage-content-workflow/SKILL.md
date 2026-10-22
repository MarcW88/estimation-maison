---
name: usage-content-workflow
description: Workflow unique de production et correction des pages SEO/GEO sous /usages/ d'aspirateurs-chantier.fr. Adapté de MarcW88/bloc-notes-numerique. Utiliser après usage-analysis-workflow lorsqu'une page nécessite LIGHT_UPDATE ou DEEP_REWRITE, ou pour produire une nouvelle page centrée sur un job de chantier. Ne pas utiliser pour classer des produits, expliquer principalement une technologie ou rédiger une page de marque.
metadata:
  source_repo: MarcW88/bloc-notes-numerique
  source_skill: .agents/skills/usage-content-workflow/SKILL.md
  adapted_for: aspirateurs-chantier.fr
  orchestration_target: ">=80% existing skills"
---

# Usage Content Workflow — aspirateurs-chantier.fr

## Rôle

C'est le **seul workflow de production/correction** à utiliser pour les URLs sous `/usages/`.

Pour une URL existante :

`usage-analysis-workflow / AUDIT` → décision → correction si nécessaire → `usage-analysis-workflow / PUBLISH_REVIEW`.

Décisions consommées :

- `KEEP` → ne pas rédiger ;
- `LIGHT_UPDATE` → corriger uniquement le scope audité ;
- `DEEP_REWRITE` → reconstruire en préservant les éléments valides ;
- `MERGE` / `NOINDEX` → ne pas produire une nouvelle version sans décision humaine sur le rôle de l'URL.

Principe de séparation :

- `/usages/` = circonstances, job, workflow, frictions et critères ;
- `/comparatifs/` = choix entre modèles ;
- `/guides/` = technologie, critère, sécurité ou procédure ;
- `/marques/` = marque, gamme ou écosystème.

Une page usage doit rester utile même si aucun produit précis ni lien affilié n'est cité.

---

# 1. Entrées

Lire avant toute production :

- `AGENTS.md` / `DESIGN.md` lorsque pertinent ;
- `usage-workflow.config.yaml` ;
- `.agents/skills/usage-skill-stack.json` ;
- `.agents/skills/usage-analysis-workflow/SKILL.md` ;
- l'audit de la page lorsqu'il existe ;
- la page cible ;
- `.content/usages/<slug>.json` ;
- les pages usage proches ;
- guides/comparatifs/marques voisins ;
- données sémantiques, GSC, logs ou autres signaux disponibles ;
- sources nécessaires aux faits actuels.

Créer ou mettre à jour `.content/usages/<slug>.json` **avant la rédaction**.

Ne jamais utiliser la mémoire du modèle pour combler un manque factuel.

---

# 2. Chaîne de production fondée sur les skills partagés

La majorité de la méthode doit provenir des skills existants. Le présent workflow orchestre ; il ne recrée pas leurs méthodes.

## Étape 1 — intention et rôle

Utiliser `search-intent` pour confirmer : requête/topic, intention, situation centrale, résultat attendu, pages internes proches et cannibalisation potentielle.

Pour une page existante, respecter `usage-analysis-workflow / AUDIT` et préserver la valeur identifiée.

### Gate de frontière

Une page usage ne doit pas devenir :

- un classement de produits ;
- un guide technique autonome ;
- une page marque ;
- une simple page mot-clé « aspirateur + X » sans job distinct.

Si le rôle de l'URL est mauvais, arrêter et renvoyer vers `usage-analysis-workflow`.

## Étape 2 — `jobs-to-be-done`

Documenter seulement les dimensions utiles :

- circumstances ;
- progress/outcome ;
- functional jobs ;
- emotional/social jobs seulement s'ils apportent une vraie décision ;
- Push / Pull / Anxiety / Habit ;
- current hires ;
- Big Hire / Little Hire si pertinent.

Sans interview ou donnée comportementale, les motivations restent `INFERRED` ou `HYPOTHESIS`.

Dans cet univers, privilégier les circonstances observables : matériau, outil, fréquence, durée, localisation du captage, quantité de déchets, mobilité, contraintes de sécurité et de vidage.

## Étape 3 — cartographier le workflow utile

Décomposer uniquement les étapes qui changent le choix :

- émission de poussière/matière ;
- captage à la source ou nettoyage après émission ;
- transfert dans flexible/raccord ;
- maintien des performances lorsque le filtre se charge ;
- collecte/ensachage ;
- vidage et exposition secondaire ;
- déplacements entre postes ;
- gestion des liquides lorsque pertinente.

Pour chaque étape réellement utile, relier : tâche → friction → conséquence → capacité qui réduit la friction → niveau de preuve.

Aucun nombre d'étapes n'est obligatoire.

## Étape 4 — transformer les frictions en critères

Hiérarchiser seulement lorsque cela clarifie la décision :

- `MUST_HAVE` ;
- `HIGH` ;
- `CONDITIONAL` ;
- `LOW` ;
- `CONTRAINDICATION`.

Chaque critère doit répondre à :

> Qu'est-ce que ce critère change dans ce job précis ?

Exemples possibles, jamais automatiques : classe de poussière, décolmatage, antistatique, diamètre/longueur de flexible, prise asservie, collecte par sac, volume utile, vidange, mobilité, plateforme batterie, captage continu, compatibilité avec l'outil.

Ne pas attribuer de score produit ici.

## Étape 5 — recherche et preuves

Utiliser `fact-check` pour les claims vérifiables.

Utiliser `evidence-based-reviews` uniquement lorsqu'une conclusion sur le comportement réel dépasse la fiche technique.

Pour les claims importants, conserver : claim, source, date, stabilité, evidence class.

Classes : `OBSERVED`, `SUPPORTED`, `INFERRED`, `HYPOTHESIS`, `UNKNOWN`.

Règles métier incontournables :

- classe L/M/H explicitement sourcée ;
- ne pas inférer une classe depuis HEPA, puissance, débit ou décolmatage ;
- filtre et certification machine distincts ;
- ACD distinct d'ATEX/Zone 22 ;
- débit/dépression cross-brand seulement si contexte de mesure comparable ;
- compatibilités outil/flexible/batterie/consommables vérifiées lorsqu'elles changent la décision ;
- aucun faux hands-on.

## Étape 6 — familles et alternatives de solutions

Déterminer les familles **après** le JTBD et les critères.

Selon le job, les alternatives peuvent inclure :

- aspirateur de chantier généraliste ;
- extracteur classe M/H ;
- extracteur compact lié à un outil ;
- aspirateur sans fil ;
- système eau/poussière ;
- collecteur/aspirateur à copeaux dédié ;
- captage fixe d'atelier ;
- solution industrielle continue ;
- méthode de travail qui réduit l'émission à la source.

Ne jamais imposer les mêmes familles à toutes les pages.

Pour chaque famille utile : quand elle convient, friction résolue, compromis principal, contre-indication.

Si la question devient « quel modèle acheter ? », faire le handoff vers `comparison-content-workflow`.

## Étape 7 — `affiliate-value`

Si la page influence l'achat, utiliser `affiliate-value` avant la rédaction finale.

La valeur indépendante des liens affiliés doit inclure au minimum des arbitrages, limites, alternatives, critères ou contre-indications réellement utiles.

## Étape 8 — brief et architecture bespoke

Utiliser `content-brief-authoring` pour transformer intention, JTBD, frictions, critères, preuves, valeur existante et handoffs en **plan propre à la page**.

Il n'existe aucune architecture obligatoire pour les pages usages.

Ne pas imposer mécaniquement : situation → workflow → critères → produits → limites → conclusion.

Deux pages peuvent partager un shell visuel, mais les sections et leur ordre doivent découler du job.

Chaque grande section doit être justifiée par au moins une question utilisateur, une friction, une preuve, un arbitrage ou une prochaine étape.

## Étape 9 — rédaction

Utiliser `content-and-copy` à partir du brief et des preuves.

Règles :

- répondre rapidement au problème principal ;
- français naturel, précis et sobre ;
- expliquer les compromis ;
- distinguer faits, déductions et hypothèses ;
- traiter les contre-indications sérieusement ;
- ne jamais inventer test, expérience personnelle, autonomie, débit mesuré, prix ou avis utilisateur ;
- ne pas transformer la page en comparatif produit ;
- conserver `noindex, follow` pendant la récupération ;
- intégrer le contenu dans la vraie source de vérité du repo, pas uniquement dans un HTML généré.

Pour `LIGHT_UPDATE`, préserver les passages explicitement validés par l'audit.

## Étape 10 — contrôles post-rédaction

Ordre recommandé :

1. `fact-check` post-draft ;
2. `internal-linking-audit` ;
3. `humanizer` ;
4. `general-writing` ;
5. `anti-ai-slop` ;
6. `seo-drift` si baseline utile ;
7. `seo-technical` ;
8. `seo-best-practices` / `seo-onpage` selon applicabilité ;
9. `editorial-qa` ;
10. lecture complète dans l'ordre rendu.

Tout fait nouveau introduit après humanisation doit repasser par `fact-check`.

Le contrôle final confirme :

- job toujours visible ;
- critères reliés aux frictions ;
- hypothèses non transformées en certitudes ;
- page non transformée en comparatif ;
- claims de sécurité correctement bornés ;
- structure non clonée mécaniquement ;
- valeur maintenue sans affiliation.

---

# 3. Handoffs vers les autres workflows

## Vers `guide-content-workflow`

Sous-question technique/procédurale autonome : classes L/M/H, décolmatage, entretien filtre, eau/poussière, débit/dépression, sac/sans sac, sécurité, etc.

## Vers `comparison-content-workflow`

Dès qu'il faut sélectionner des candidats, comparer des modèles, scorer, pondérer, classer ou désigner un choix.

Le record usage transmet les contraintes au comparatif mais ne stocke pas un ranking produit comme source de vérité.

## Vers `brand-content-workflow`

Quand la question porte principalement sur une marque, une gamme ou un écosystème.

---

# 4. `PUBLISH_REVIEW` obligatoire

Une fois la rédaction terminée, ne pas auto-valider la page ici.

Passer à :

`usage-analysis-workflow / PUBLISH_REVIEW`

Sorties :

- `PASS — READY_FOR_HUMAN_VALIDATION` ;
- `FAIL — KEEP_NOINDEX`.

Un PASS reste suivi d'une validation humaine explicite. L'indexation est une instruction séparée.

---

# 5. Échecs de production

Arrêter et renvoyer vers l'analyse si :

- le job se réduit à « meilleur aspirateur pour X » ;
- les critères viennent surtout des fiches produits ;
- un ranking produit apparaît ;
- le rôle devient identique à un guide/comparatif ;
- une classe de poussière est inférée ;
- un claim ACD/ATEX est simplifié ;
- les contre-indications disparaissent ;
- des claims instables restent non sourcés ;
- l'architecture copie une page sœur sans justification ;
- un faux hands-on est introduit.

---

# 6. Ce que ce workflow ne doit pas devenir

Ne pas ajouter :

- quota de mots ;
- nombre minimum de H2/H3 ;
- quota de liens ;
- score qualité artificiel ;
- template unique par usage ;
- matrice JTBD remplie mécaniquement ;
- ranking produit ;
- deuxième copie des méthodes déjà présentes dans les skills partagés.

La couche custom reste limitée à l'orchestration et aux contraintes propres à l'usage d'un aspirateur de chantier.
