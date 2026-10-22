---
name: guide-content-workflow
description: Workflow unique de production et correction des guides SEO/GEO sous /guides/ de bloc-notes-numeriques.fr. Utiliser après guide-analysis-workflow lorsqu'une page existante nécessite LIGHT_UPDATE ou DEEP_REWRITE, ou pour créer un nouveau guide. Orchestre majoritairement des skills GitHub existants pour intention, recherche, preuves, brief, rédaction et QA.
metadata:
  adapted_for: bloc-notes-numeriques.fr
  orchestration_target: ">=80% existing GitHub skills"
  custom_scope: "guide routing + category boundaries + source-of-truth integration"
---

# Guide Content Workflow

## Rôle

C'est le **seul workflow de production/correction** à utiliser pour les URLs sous `/guides/`.

Pour une page existante, la séquence normale est :

`guide-analysis-workflow / AUDIT` → décision → correction si nécessaire → `guide-analysis-workflow / PUBLISH_REVIEW`.

Décisions consommées :

- `KEEP` → ne pas réécrire ;
- `LIGHT_UPDATE` → corriger uniquement le scope identifié ;
- `DEEP_REWRITE` → reconstruire la page tout en préservant les éléments valides ;
- `MERGE` / `NOINDEX` → ne pas produire une nouvelle version sans décision humaine sur le rôle de l'URL.

Pour une **nouvelle URL**, effectuer directement intention, recherche, preuves et brief avant la rédaction.

Le workflow ne retire jamais `noindex,follow` de lui-même.

---

# 1. Entrées

Lire avant toute production :

- `AGENTS.md` et `DESIGN.md` si le rendu est concerné ;
- `.agents/skills/guide-analysis-workflow/SKILL.md` ;
- l'audit de la page lorsqu'elle existe ;
- la page cible et sa source de vérité dans le générateur ;
- `.content/briefs/<slug>.md` et `.content/reviews/<slug>.md` lorsqu'ils existent ;
- les guides voisins ;
- les pages usages, comparatifs et marques qui répondent à des sous-questions proches ;
- les données sémantiques, GSC ou autres signaux disponibles ;
- les sources nécessaires aux faits actuels.

Ne pas utiliser la mémoire du modèle pour combler un manque factuel.

Pour une page existante, préserver explicitement la valeur identifiée par `guide-analysis-workflow / AUDIT`.

---

# 2. Router le travail sans créer un template

Identifier le travail dominant uniquement pour choisir les risques à vérifier :

- `CHOICE` — aider à arbitrer entre options, contraintes ou approches ;
- `EXPLAINER` — expliquer une technologie, une mesure, un format ou un mécanisme ;
- `HOW_TO` — permettre une tâche, un transfert, une intégration ou une procédure.

Un guide peut être hybride.

Lire si utile :

- `references/choice-guide.md` ;
- `references/explainer-guide.md` ;
- `references/how-to-guide.md`.

Ces références sont des **questions de contrôle**, pas des architectures à reproduire. Elles ne doivent jamais imposer l'ordre ou le nombre de sections, un tableau, une FAQ, une checklist ou un nombre d'étapes.

---

# 3. Chaîne de production fondée sur les skills réutilisés

La majorité de la méthode doit provenir des skills existants. Le présent fichier orchestre ; il ne duplique pas leurs méthodologies.

## Étape 1 — intention, cluster et rôle

Utiliser :

- `seo-keyword` lorsque recherche, clustering ou validation du topic est nécessaire ;
- `search-intent` pour la tâche exacte, les sous-questions et le résultat attendu ;
- `seo-content-audit` et `content-refresh` pour une page existante lorsque l'audit l'a demandé.

Confirmer :

- requête/topic principal ;
- intention ;
- tâche ou décision du lecteur ;
- périmètre ;
- prochaine étape logique ;
- chevauchements internes.

### Gate de frontière

Un guide ne doit pas devenir :

- une page Usage qui traite un job complet et ses circonstances ;
- un comparatif qui sélectionne ou classe des produits ;
- une page Marque centrée sur un écosystème ou une gamme.

Si le rôle apparaît incorrect malgré l'audit, arrêter et renvoyer vers `guide-analysis-workflow` plutôt que forcer un texte dans le slug.

## Étape 2 — recherche et registre de preuves

Utiliser `fact-check` pour les claims vérifiables.

Adapter la recherche à la stabilité du sujet :

- mécanisme stable → exactitude et source solide ;
- logiciel, cloud, abonnement, compatibilité, prix, génération produit ou procédure → vérification actuelle ;
- claim expérientiel produit important → `evidence-based-reviews` si nécessaire.

Pour les claims importants, conserver :

- affirmation ;
- source ;
- date de consultation ;
- portée/conditions ;
- stabilité ;
- niveau d'incertitude.

Une inconnue reste inconnue, qualifiée ou exclue.

## Étape 3 — questions propres au type dominant

### `CHOICE`

Documenter seulement ce qui change l'arbitrage : critères, compromis, critères éliminatoires, dépendances, coût lorsque pertinent, situations où chaque option cesse d'être adaptée.

Ne pas créer de podium produit. Si la tâche devient « quel modèle acheter ? », passer au workflow Comparatif.

### `EXPLAINER`

Documenter seulement ce qui permet de comprendre correctement : concept, termes voisins, mécanisme, causalité, conséquence pratique, limites et exceptions.

Une définition seule n'est pas une explication.

### `HOW_TO`

Documenter seulement ce qui permet d'exécuter la tâche : contexte, prérequis, méthode vérifiée, variantes de plateforme/version, résultat attendu, vérification, échecs probables et alternatives utiles.

Ne jamais inventer une étape parce qu'elle semble probable.

## Étape 4 — `affiliate-value` lorsque pertinent

Si le guide influence l'achat, utiliser `affiliate-value` avant la rédaction finale.

La page doit rester utile sans lien affilié. Les critères, limites, alternatives et conséquences pratiques doivent exister indépendamment d'un marchand.

## Étape 5 — brief propre à la page

Utiliser `content-brief-authoring` comme skill principal de brief et persister le résultat dans `.content/briefs/<slug>.md`, en conservant les champs utiles de `references/brief-template.md`.

Le brief doit contenir uniquement ce qui change réellement la page :

- intention/tâche ;
- valeur propre ;
- périmètre et exclusions ;
- faits et entités nécessaires ;
- preuves ;
- risques ;
- valeur existante à préserver pour une mise à jour ;
- liens vers les prochaines questions ;
- angle/thèse ;
- structure proposée **issue de cette recherche**.

### Règle centrale

Il n'existe **aucune architecture éditoriale obligatoire par type de guide**.

Le plan final est construit après l'intention et les preuves. Chaque grande section doit être justifiable par une question, une étape nécessaire, une distinction, une preuve, un arbitrage ou une limite.

Deux guides de même type peuvent avoir des structures très différentes.

## Étape 6 — rédaction

Utiliser `content-and-copy` pour produire la prose à partir du brief et du registre de preuves.

Règles :

- répondre suffisamment tôt à la question principale ;
- employer un français naturel, précis et sobre ;
- expliquer ce que les faits changent pour le lecteur ;
- distinguer faits, interprétations et inconnues ;
- ne jamais inventer test, mesure, expérience personnelle, prix, compatibilité ou procédure ;
- utiliser tableaux, listes et étapes uniquement lorsqu'ils améliorent la compréhension ;
- éviter les FAQ répétitives ;
- ne pas transformer le guide en classement produit ;
- pour `LIGHT_UPDATE`, ne pas réécrire par réflexe les passages que l'audit a demandé de préserver.

Intégrer le contenu dans la **source de vérité du générateur** (`_generate.py` ou module explicitement chargé), puis régénérer. Ne pas éditer uniquement le HTML généré.

---

# 4. Contrôles post-rédaction

Exécuter les passes pertinentes séparément ; ne pas déclarer plusieurs contrôles effectués après une relecture générique.

## Étape 7 — factualité après rédaction

Relancer `fact-check` sur les claims réellement écrits. Si une modification ultérieure introduit un nouveau fait, repasser ce fait par ce gate.

Utiliser `evidence-based-reviews` seulement pour les jugements expérientiels qui le nécessitent.

## Étape 8 — maillage

Utiliser `internal-linking-audit`.

Un lien existe parce qu'il répond à la prochaine question logique, pas pour atteindre un quota. Vérifier les cibles et les ancres.

## Étape 9 — finition éditoriale

Dans cet ordre logique :

1. `humanizer` sur l'intégralité du contenu visible ;
2. `general-writing` avec le minimum de changements nécessaires ;
3. `anti-ai-slop` en mode review/detection ;
4. `seo-drift` uniquement si un baseline utile existe.

Après ces passes, vérifier qu'aucun fait, prérequis, limite ou nuance n'a été perdu ou inventé.

## Étape 10 — SEO et QA

Utiliser :

1. `seo-onpage` ;
2. `seo-technical` ;
3. `seo-best-practices` seulement pour les règles réellement applicables ;
4. `editorial-qa` ;
5. lecture complète dans l'ordre rendu, desktop/mobile lorsque le rendu est disponible.

Le contrôle final doit notamment confirmer :

- tâche satisfaite ;
- architecture propre à la page ;
- pas de clonage mécanique des références de type ;
- faits/procédures actuels lorsque nécessaire ;
- limites importantes préservées ;
- frontière claire avec usages/comparatifs/marques ;
- valeur sans affiliation ;
- aucun faux hands-on.

---

# 5. PUBLISH_REVIEW obligatoire

Une fois la correction/rédaction terminée, **ne pas auto-valider dans ce workflow**.

Passer la main à :

`guide-analysis-workflow / PUBLISH_REVIEW`

Ce mode exécute :

- `python3 validate_guide_quality.py` pour les blockers machine ;
- les gates substantiels ;
- la comparaison au cluster.

Résultats possibles :

- `PASS — READY_FOR_HUMAN_VALIDATION` ;
- `FAIL — KEEP_NOINDEX`.

Un PASS reste suivi d'une validation humaine explicite avant toute instruction d'indexation.

---

# 6. Statuts et traçabilité

Le brief peut conserver :

- `BRIEF_READY` ;
- `DRAFT_READY` ;
- `QA_IN_PROGRESS` ;
- `REVISION_REQUIRED` ;
- `HUMAN_APPROVED` ;
- `PUBLISHABLE`.

Ils ne remplacent pas la décision de `guide-analysis-workflow`.

Dans `.content/reviews/<slug>.md`, consigner au minimum les passes réellement effectuées, les blockers, les corrections importantes et les risques résiduels. Ne pas marquer un skill `PASS` sur la seule base du validateur machine.

`PUBLISHABLE` exige : PUBLISH_REVIEW PASS + validation humaine + contrôles techniques. L'indexation reste une instruction séparée.

---

# 7. Handoffs vers les autres workflows

## Vers `usage-content-workflow`

Lorsque la vraie question porte sur un contexte complet : étudiant, professionnel, réunion, dessin, remplacement du papier, lecture + notes, etc.

## Vers `comparison-content-workflow`

Lorsque la réponse nécessite de sélectionner, comparer, scorer, classer ou recommander des produits entre eux.

## Vers `brand-content-workflow`

Lorsque la question porte principalement sur une marque, une gamme, un produit ou un service de marque.

---

# 8. Ce que ce workflow ne doit pas devenir

Ne pas ajouter :

- quota de mots ;
- nombre minimum de H2/H3 ;
- quota de liens ou de sources ;
- nombre obligatoire d'étapes ;
- tableau ou FAQ obligatoire ;
- score qualité artificiel ;
- architecture fixe `CHOICE`, `EXPLAINER` ou `HOW_TO` ;
- deuxième copie des règles de `fact-check`, SEO, rédaction, humanisation ou QA déjà présentes dans les skills spécialisés.

La couche custom doit rester limitée au routing Guide, aux frontières de catégorie et à l'intégration dans la source de vérité du site.
