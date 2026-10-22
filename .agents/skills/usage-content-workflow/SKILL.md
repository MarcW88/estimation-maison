---
name: usage-content-workflow
description: Workflow unique de production et correction des pages SEO/GEO sous /usages/ de bloc-notes-numeriques.fr. Utiliser après usage-analysis-workflow lorsqu'une page nécessite LIGHT_UPDATE ou DEEP_REWRITE, ou pour produire une nouvelle page centrée sur un job-to-be-done. Ne pas utiliser pour classer des produits, expliquer principalement une technologie ou rédiger une page de marque.
metadata:
  adapted_for: bloc-notes-numeriques.fr
  orchestration_target: ">=80% existing skills"
---

# Usage Content Workflow

## Rôle

C'est le **seul workflow de production/correction** à utiliser pour les URLs sous `/usages/`.

Il ne décide plus seul si une page existante doit être réécrite. Pour une URL existante, la séquence normale est :

`usage-analysis-workflow / AUDIT` → décision → correction si nécessaire → `usage-analysis-workflow / PUBLISH_REVIEW`.

Décisions consommées :

- `KEEP` → ne pas rédiger ;
- `LIGHT_UPDATE` → corriger uniquement le scope identifié par l'audit ;
- `DEEP_REWRITE` → reconstruire la page en préservant les éléments valides ;
- `MERGE` / `NOINDEX` → ne pas produire une nouvelle version sans décision humaine sur le rôle de l'URL.

Pour une **nouvelle URL**, réaliser directement le cadrage intention + JTBD + recherche avant la rédaction ; il n'existe évidemment pas de contenu historique à auditer.

Principe de séparation :

- `/usages/` = comprendre le besoin, les circonstances, le workflow, les frictions et les critères ;
- `/comparatifs/` = choisir entre des produits ;
- `/guides/` = expliquer une technologie, un critère ou une procédure ;
- `/marques/` = documenter un écosystème, une gamme ou un produit.

Une page usage doit rester utile même si aucun produit précis ni lien affilié n'est cité.

---

# 1. Entrées

Lire avant toute production :

- `AGENTS.md` et `DESIGN.md` ;
- `usage-workflow.config.yaml` ;
- `.agents/skills/usage-analysis-workflow/SKILL.md` ;
- l'audit de la page lorsqu'elle existe ;
- la page cible et son fichier `.content/usages/<slug>.json` ;
- les autres pages `/usages/` pertinentes ;
- les guides, comparatifs et pages marques susceptibles de répondre à une sous-question ;
- les données sémantiques, GSC ou autres signaux disponibles ;
- les sources nécessaires aux faits actuels.

Créer ou mettre à jour `.content/usages/<slug>.json` **avant la rédaction**.

Ne pas utiliser la mémoire du modèle pour combler un manque factuel.

---

# 2. Chaîne de production fondée sur les skills réutilisés

La majorité de la méthode doit provenir des skills existants. Le présent workflow orchestre ; il ne doit pas recréer leurs méthodes sous forme de règles custom.

## Étape 1 — intention et rôle

Utiliser `search-intent` pour confirmer :

- requête/topic principal ;
- intention ;
- situation ou problème central ;
- niveau de maturité ;
- résultat attendu ;
- pages internes proches ;
- risque de cannibalisation.

Pour une page existante, respecter le diagnostic de `usage-analysis-workflow / AUDIT` et préserver la valeur déjà identifiée.

### Gate de frontière

Une page usage ne doit pas devenir :

- un classement de produits ;
- un guide technique autonome ;
- une page de marque ;
- un pseudo-persona générique.

Si la production révèle que le rôle de l'URL est mauvais malgré l'audit, arrêter la rédaction et renvoyer vers `usage-analysis-workflow` plutôt que forcer le contenu dans le slug.

## Étape 2 — `jobs-to-be-done`

Utiliser le skill `jobs-to-be-done` avant toute recommandation de solution.

Documenter uniquement les dimensions utiles au sujet :

- circumstances ;
- progress/outcome ;
- functional jobs ;
- emotional/social jobs lorsqu'ils sont réellement utiles ;
- Push / Pull / Anxiety / Habit ;
- current hires ;
- Big Hire / Little Hire.

Ne pas remplir mécaniquement toutes les cases.

### Gate de preuve JTBD

Sans interview utilisateur ou donnée comportementale :

- les motivations émotionnelles/sociales restent `INFERRED` ou `HYPOTHESIS` ;
- ne jamais écrire « les étudiants veulent… », « les professionnels préfèrent… » ou équivalent comme un fait universel ;
- les circonstances et tâches observables doivent primer sur les attributs démographiques.

## Étape 3 — cartographier le workflow utile

Décomposer le job uniquement autant que nécessaire pour comprendre les frictions qui changent la décision.

Des étapes possibles sont : entrée/import, travail principal, organisation/retrouvabilité, sortie/export/partage, continuité dans le temps ou entre appareils.

Pour chaque étape réellement pertinente, relier :

- tâche ;
- friction ;
- conséquence si elle échoue ;
- capacité ou caractéristique qui réduit la friction ;
- niveau de preuve.

Aucun nombre d'étapes n'est obligatoire.

## Étape 4 — transformer les frictions en critères

Hiérarchiser les critères seulement lorsque cette hiérarchie apporte une décision plus claire :

- `MUST_HAVE` ;
- `HIGH` ;
- `CONDITIONAL` ;
- `LOW` ;
- `CONTRAINDICATION`.

Chaque critère doit pouvoir répondre à :

> Qu'est-ce que ce critère change dans ce job précis ?

Ne pas attribuer de scores produit ici. Les critères proviennent du workflow réel, pas du catalogue de fonctionnalités disponibles.

## Étape 5 — recherche et preuves

Utiliser `fact-check` pour les claims vérifiables.

Lorsque la page contient un jugement expérientiel important sur un appareil, utiliser également `evidence-based-reviews` avec un niveau de preuve proportionné au claim. Ne pas l'appeler mécaniquement pour chaque spec.

Conserver dans le record usage, pour les claims importants :

- claim ;
- source ;
- date ;
- stabilité ;
- evidence class.

Classes usage : `OBSERVED`, `SUPPORTED`, `INFERRED`, `HYPOTHESIS`, `UNKNOWN`.

Pour les capacités produit ou logiciel susceptibles d'évoluer, privilégier des sources primaires et dater la vérification.

## Étape 6 — familles et alternatives de solutions

Déterminer les familles de solutions **après** le JTBD et les critères.

Une famille peut être, lorsque le sujet le justifie : appareil minimaliste, plateforme ouverte, grand écran PDF, couleur, liseuse avec stylet, tablette LCD, papier ou workflow hybride.

Ne jamais imposer les mêmes familles à toutes les pages.

Pour chaque famille réellement utile, expliquer :

- quand elle convient ;
- quelle friction elle résout ;
- son compromis principal ;
- dans quelles circonstances elle devient un mauvais choix.

Si le lecteur a désormais besoin de savoir **quel produit acheter**, créer un handoff vers `comparison-content-workflow` plutôt que construire un podium ici.

## Étape 7 — `affiliate-value`

Si la page influence l'achat, utiliser `affiliate-value` avant la rédaction finale.

La page doit apporter de la valeur même sans liens affiliés : compromis, limites, alternatives, critères, contre-indications et parcours de décision.

## Étape 8 — brief et architecture bespoke

Utiliser `content-brief-authoring` pour transformer :

- intention ;
- JTBD ;
- frictions ;
- critères ;
- preuves ;
- valeur existante à préserver ;
- handoffs vers guides/comparatifs ;

en un **plan propre à cette page**.

### Règle centrale

Il n'existe **aucune architecture éditoriale obligatoire par type d'usage**.

Ne pas partir d'un plan fixe du genre : situation → workflow → critères → familles → contre-indications → conclusion si ce plan n'est pas celui que le research justifie.

Deux pages usage peuvent partager des composants visuels, mais leurs sections, leur ordre, leur nombre de H2/H3, leur usage des tableaux et leur conclusion doivent découler de la décision propre au job.

Le brief doit justifier les grandes sections par :

- une question utilisateur ;
- une friction ;
- une preuve ;
- un arbitrage ;
- ou une prochaine étape nécessaire.

## Étape 9 — rédaction

Utiliser `content-and-copy` pour produire la page à partir du brief et du registre de preuves.

Règles :

- répondre au job principal rapidement ;
- employer un français naturel, précis et sobre ;
- expliquer les compromis plutôt que promettre une solution idéale ;
- distinguer faits, déductions et hypothèses ;
- rendre les contre-indications aussi honnêtes que les bénéfices ;
- ne jamais inventer test, expérience personnelle, autonomie mesurée, prix ou avis utilisateur ;
- ne pas transformer la page en comparatif produit ;
- conserver l'état robots de brouillon défini par la politique du site ;
- intégrer le contenu dans la vraie source de vérité (`usage_content.py` ou module explicitement relié à la génération), pas seulement dans le HTML généré.

Pour `LIGHT_UPDATE`, ne pas réécrire par réflexe les passages que l'audit a demandé de préserver.

## Étape 10 — contrôles post-rédaction

Exécuter dans cet ordre logique, sans refaire inutilement les étapes déjà validées :

1. `fact-check` post-draft sur les claims réellement écrits ;
2. `internal-linking-audit` ;
3. `humanizer` ;
4. `general-writing` ;
5. `anti-ai-slop` ;
6. `seo-drift` seulement si un baseline utile existe ;
7. `seo-technical` ;
8. `seo-best-practices` / `seo-onpage` selon les éléments réellement applicables ;
9. `editorial-qa` ;
10. lecture complète dans l'ordre rendu.

Après `humanizer` et `general-writing`, ne jamais accepter une modification qui introduit un nouveau fait sans le repasser par `fact-check`.

Le contrôle final doit notamment confirmer :

- que le job n'a pas été remplacé par une liste de specs ;
- que les circonstances ou frictions nécessaires sont encore visibles ;
- que les critères restent reliés au job ;
- que les contre-indications n'ont pas disparu ;
- que les hypothèses ne sont pas devenues des certitudes ;
- que la page ne s'est pas transformée en comparatif ;
- que la structure ne copie pas mécaniquement les pages sœurs.

---

# 3. Handoffs vers les autres workflows

## Vers `guide-content-workflow`

Utiliser lorsqu'une sous-question mérite une explication autonome : fonctionnement E Ink, OCR, export, synchronisation, taille d'écran, prix, latence, annotation PDF procédurale, etc.

## Vers `comparison-content-workflow`

Utiliser dès qu'il faut réellement :

- sélectionner des candidats produits ;
- comparer plusieurs modèles ;
- scorer ou pondérer ;
- classer ;
- désigner un choix ou un meilleur modèle.

Le record usage peut transmettre les contraintes/critères au comparatif mais ne doit pas stocker un ranking produit comme source de vérité.

## Vers `brand-content-workflow`

Utiliser lorsque la question porte principalement sur une marque, une gamme, un produit ou un service de marque.

---

# 4. PUBLISH_REVIEW obligatoire

Une fois la correction/rédaction terminée, **ne pas auto-valider la page dans ce workflow**.

Passer la main à :

`usage-analysis-workflow / PUBLISH_REVIEW`

Ce mode réexécute le validateur machine et les gates substantiels, puis retourne :

- `PASS — READY_FOR_HUMAN_VALIDATION` ;
- ou `FAIL — KEEP_NOINDEX`.

Un PASS reste suivi d'une validation humaine explicite avant toute instruction d'indexation.

---

# 5. Échecs de production

Arrêter ou renvoyer vers l'analyse si :

- le job se réduit à « trouver le meilleur produit pour X » ;
- la page repose surtout sur une catégorie démographique ;
- des motivations hypothétiques sont traitées comme des faits ;
- les critères viennent des produits plutôt que des frictions ;
- aucune alternative hors E Ink n'est considérée alors qu'elle est plausible ;
- un ranking produit apparaît ;
- les contre-indications disparaissent sans justification ;
- la page devient substantiellement identique à un guide ou comparatif proche ;
- des claims instables sont non sourcés ;
- l'architecture a été copiée d'une autre page sans justification ;
- un faux hands-on est introduit.

---

# 6. Statuts du record usage

Les statuts de production internes peuvent rester :

- `JTBD_READY` ;
- `EVIDENCE_READY` ;
- `DRAFT_READY` ;
- `QA_IN_PROGRESS` ;
- `REVISION_REQUIRED` ;
- `HUMAN_APPROVED` ;
- `PUBLISHABLE`.

Ils ne remplacent pas la décision de `usage-analysis-workflow`.

`PUBLISHABLE` exige : PUBLISH_REVIEW PASS + validation humaine + contrôles techniques. L'indexation reste une instruction explicite séparée.

---

# 7. Ce que ce workflow ne doit pas devenir

Ne pas ajouter :

- quota de mots ;
- nombre minimum de H2/H3 ;
- quota de liens ;
- score qualité artificiel ;
- architecture fixe "par usage" ;
- matrice JTBD remplie mécaniquement ;
- ranking produit ;
- deuxième copie des méthodes déjà présentes dans les skills spécialisés.

La couche custom reste limitée à l'orchestration et aux frontières propres à `/usages/`.
