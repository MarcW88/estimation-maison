---
name: usage-analysis-workflow
description: Workflow unique d'analyse des pages /usages/ de bloc-notes-numeriques.fr. Audite une page ou le cluster, vérifie JTBD, rôle éditorial, cannibalisation avec comparatifs/guides, preuves, valeur affiliée, AI-slop et SEO, puis décide KEEP, LIGHT_UPDATE, DEEP_REWRITE, MERGE ou NOINDEX. En mode PUBLISH_REVIEW, sert de gate final avant validation humaine.
metadata:
  adapted_for: bloc-notes-numeriques.fr
  orchestration_target: ">=80% existing skills"
---

# Usage Analysis Workflow

## Rôle

C'est le **seul workflow d'analyse** à utiliser pour les URLs sous `/usages/`.

Il ne réécrit pas la page par défaut. Il orchestre les skills spécialisés déjà présents dans le dépôt et ajoute uniquement les contrôles spécifiques aux pages centrées sur un **job, des circonstances et un workflow d'usage**.

Séparation des responsabilités :

- `usage-analysis-workflow` = diagnostiquer, comparer le cluster, décider et faire le publish review ;
- `usage-content-workflow` = produire ou corriger uniquement lorsqu'une décision d'analyse le demande.

Les autres catégories gardent leurs workflows propres :

- `/comparatifs/` = décision entre produits ;
- `/guides/` = explication d'une technologie, d'un critère ou d'une procédure ;
- `/marques/` = marque, écosystème, gamme ou produit.

---

# 1. Modes

## `AUDIT`

Mode par défaut pour une URL existante.

Retourne une décision et un plan de correction **sans réécrire la page**.

L'audit est individuel mais pas isolé : comparer la page cible avec les pages `/usages/` les plus proches et avec les pages `/comparatifs/` ou `/guides/` susceptibles de couvrir la même intention.

## `CLUSTER_AUDIT`

Analyse le cluster `/usages/` dans son ensemble afin de détecter :

- jobs ou intentions trop proches ;
- pages dont le rôle devrait être déplacé vers un guide ou un comparatif ;
- cannibalisation inter-catégories ;
- duplication de valeur ;
- industrialisation de structure ;
- trous de couverture importants dans le parcours utilisateur.

Le mode cluster **ne déclenche aucune réécriture automatiquement**.

## `PUBLISH_REVIEW`

Gate final après correction ou production via `usage-content-workflow`.

Il réexécute les contrôles substantiels et le validateur machine, puis retourne exactement :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Un PASS n'autorise jamais l'indexation ou le merge automatiquement.

---

# 2. Entrées

Lire avant l'analyse :

- `AGENTS.md` et, si nécessaire, `DESIGN.md` ;
- `usage-workflow.config.yaml` ;
- la page cible et son fichier `.content/usages/<slug>.json` lorsqu'il existe ;
- les pages `/usages/` proches ;
- les comparatifs, guides et pages marques qui répondent à des sous-questions voisines ;
- les données historiques disponibles : analyse sémantique, GSC, logs ou autres signaux pertinents ;
- les sources actuelles lorsque les faits peuvent avoir évolué.

Ne jamais compléter une donnée absente à partir de la mémoire du modèle.

---

# 3. Chaîne de skills réutilisés

Le workflow doit d'abord **exécuter les skills existants**. Ne pas recopier leurs checklists dans ce fichier ni créer un sous-agent custom lorsqu'un skill local couvre déjà le besoin.

## 3.1 `content-audit`

Vérifier si l'URL possède encore une fonction autonome et identifier :

- valeur existante à préserver ;
- faiblesse de contenu ;
- obsolescence ;
- duplication ;
- cannibalisation ;
- problème de structure ;
- potentiel de récupération.

Utiliser les décisions internes du skill (`KEEP`, `UPDATE`, `MERGE`, `REDIRECT`, `REMOVE`) comme diagnostic, puis les mapper vers les décisions finales de ce workflow.

## 3.2 `search-intent`

Déterminer :

- requête ou topic principal ;
- intention dominante ;
- problème concret du lecteur ;
- niveau de maturité ;
- rôle attendu de l'URL ;
- pages concurrentes internes ;
- sections qui ne servent plus l'intention.

L'intention doit être observée ou documentée lorsque des données existent ; ne pas la déduire uniquement du slug.

## 3.3 `jobs-to-be-done`

Skill central pour `/usages/`.

Identifier les **circumstances**, le progrès recherché, l'outcome, les functional/emotional/social jobs utiles, les forces `Push / Pull / Anxiety / Habit`, les solutions actuellement "embauchées" et les différences entre achat initial et usage répété.

Règle de preuve : sans interview ou donnée comportementale, ne pas transformer une hypothèse JTBD en fait sur un groupe d'utilisateurs.

## 3.4 `content-refresh`

Uniquement si `content-audit` conclut qu'une mise à jour est nécessaire.

Diagnostiquer notamment : intent drift, thin value, outdated facts, weak structure, generic prose, cannibalization ou trust gap. Le skill propose l'ampleur de correction ; le présent workflow prend la décision finale.

## 3.5 `affiliate-value`

Utiliser lorsque la page influence directement ou indirectement une décision d'achat.

Vérifier que la page reste utile sans liens affiliés et qu'elle apporte : compromis, limites, alternatives, critères et prochaines étapes — pas une reformulation de fiches produits.

## 3.6 `fact-check`

Contrôler les affirmations vérifiables : capacités produit/logiciel, compatibilités, abonnements, prix lorsqu'ils sont mentionnés, limitations et données techniques.

Une affirmation plausible mais non sourcée reste non vérifiée.

## 3.7 `evidence-based-reviews`

Conditionnel, pas automatique.

L'utiliser lorsque la page contient un **jugement expérientiel** ou une conclusion importante sur le comportement d'un produit dans l'usage réel. Ne pas l'imposer pour chaque fait ou chaque critère éditorial.

## 3.8 `internal-linking-audit`

Vérifier que le maillage fait progresser le lecteur vers la prochaine question logique : guide, comparatif, marque ou autre usage. Aucun quota de liens.

## 3.9 `anti-ai-slop`

Utiliser en mode review/detection. Rechercher : prose générique, répétition, symétrie artificielle, plans interchangeables, transitions stéréotypées et pages qui pourraient être permutées en remplaçant uniquement le nom du contexte.

## 3.10 SEO

- `seo-technical` : canonical, robots, crawlabilité, schema réellement applicable, structure technique ;
- `seo-best-practices` : uniquement les règles pertinentes au site statique ;
- `seo-drift` : seulement lorsqu'un baseline avant/après existe et apporte une information utile.

## 3.11 `editorial-qa`

Dernière QA générique : intention, valeur originale, factualité, naturel, utilité, SEO et cohérence de la page sans dépendance aux liens affiliés.

---

# 4. Contrôle custom n°1 — le job possède-t-il une URL autonome ?

C'est le premier contrôle réellement spécifique à `/usages/`.

Une page usage doit aider le lecteur à comprendre **comment un contexte change les contraintes et le workflow**, pas seulement reformuler une catégorie de personne.

Vérifier :

- circonstances spécifiques ;
- progrès recherché ;
- frictions qui changent réellement selon le job ;
- critères dérivés de ces frictions ;
- alternatives raisonnables au bloc-notes E Ink ;
- contre-indications ;
- prochaine décision logique.

Une page n'est pas justifiée uniquement parce qu'un mot-clé combine `bloc-notes numérique + étudiant/professionnel/dessin/etc.`.

### Signaux d'échec

- pseudo-persona générique sans circonstances ;
- même raisonnement applicable à toutes les pages usage ;
- critères dérivés des specs disponibles plutôt que du job ;
- page utile uniquement comme liste de produits ;
- absence de cas où le bloc-notes numérique est un mauvais choix.

---

# 5. Contrôle custom n°2 — frontière avec Comparatifs et Guides

C'est le risque de cannibalisation principal du cluster.

## `/usages/` vs `/comparatifs/`

La page usage doit répondre à :

> Qu'est-ce qui compte dans cette situation, quelles frictions apparaissent et quel type de solution convient ?

Le comparatif répond à :

> Quels produits choisir entre eux pour cette décision ?

Une page usage peut citer des familles ou des exemples, mais elle ne doit pas créer un podium, un ranking ou un faux "meilleur produit".

Exemples à contrôler explicitement :

- `/usages/prise-de-notes-etudiant/` vs `/comparatifs/bloc-notes-numerique-etudiant/` ;
- `/usages/prise-de-notes-professionnelle/` vs `/comparatifs/bloc-notes-numerique-professionnel/`.

## `/usages/` vs `/guides/`

La page usage doit rester centrée sur le **job complet**. Une sous-question technique ou procédurale suffisamment autonome doit être expliquée dans un guide puis reliée depuis l'usage.

Exemple à contrôler explicitement :

- `/usages/annotation-pdf/` vs `/guides/annoter-pdf-tablette-e-ink/`.

### Test pratique

Si deux URLs pourraient garder le même H1, le même tableau central et la même conclusion en changeant seulement quelques mots, leur séparation n'est pas suffisamment nette.

---

# 6. Contrôle custom n°3 — workflow réel et critères

Ne pas imposer un diagramme ou un nombre fixe d'étapes.

Vérifier seulement que les recommandations de la page peuvent être reliées à des tâches ou frictions réelles du job, par exemple :

- entrée/import ;
- travail principal ;
- organisation/retrouvabilité ;
- sortie/export/partage ;
- continuité dans le temps ou entre appareils.

Toutes ces étapes ne sont pas obligatoires sur toutes les pages.

Un critère important doit pouvoir répondre à :

> Qu'est-ce que ce critère change dans ce job précis ?

Si la réponse est faible ou générique, le critère est probablement hérité d'un template ou d'une fiche produit.

---

# 7. Contrôle custom n°4 — similarité structurelle du cluster

En `AUDIT`, comparer la page cible aux pages sœurs les plus proches. En `CLUSTER_AUDIT` et `PUBLISH_REVIEW`, regarder le cluster pertinent dans son ensemble.

Comparer :

- fonction sémantique des H2/H3 ;
- ordre des questions ;
- formes d'introduction et de conclusion ;
- emplacement répétitif des tableaux, listes, CTA et blocs "pour qui / limites" ;
- mêmes familles de solutions utilisées mécaniquement ;
- mêmes critères dans le même ordre ;
- formulations et transitions recyclées.

Les composants visuels communs ne sont pas un problème. Le problème apparaît lorsque **l'architecture éditoriale semble déterminée avant l'analyse du job**.

Une similarité substantielle non justifiée peut déclencher `DEEP_REWRITE`.

---

# 8. Preuves et niveaux d'incertitude

Pour les affirmations importantes, utiliser les classes adaptées au registre usage :

- `OBSERVED` ;
- `SUPPORTED` ;
- `INFERRED` ;
- `HYPOTHESIS` ;
- `UNKNOWN`.

Principes :

- une motivation utilisateur non observée reste `INFERRED` ou `HYPOTHESIS` ;
- une capacité produit actuelle doit être vérifiée par une source fiable ;
- une sensation d'usage ne devient pas un fait parce qu'une spec officielle existe ;
- `UNKNOWN` ne peut pas devenir une certitude rédactionnelle ;
- aucune expérience personnelle n'est inventée.

---

# 9. Décisions `AUDIT` / `CLUSTER_AUDIT`

Mapper l'ensemble des résultats vers cinq décisions simples.

## `KEEP`

La page possède un job distinct, sert l'intention, est actuelle, utile et suffisamment différenciée des comparatifs/guides et des autres usages.

## `LIGHT_UPDATE`

Corrections ciblées : facts, sources, formulation d'un critère, quelques passages, maillage ou séparation locale avec une autre page. L'architecture fondamentale reste pertinente.

## `DEEP_REWRITE`

Le job est mal cadré, la page sert une autre intention, la valeur est trop faible, les preuves sont insuffisantes sur des points structurants, le contenu est devenu un comparatif déguisé, ou l'architecture est substantiellement industrialisée.

`DEEP_REWRITE` ne signifie pas "tout jeter" : préserver les faits, exemples, passages, sources et raisonnements qui restent utiles.

## `MERGE`

Une autre URL couvre pratiquement le même job ou la même intention et la distinction ne justifie pas deux pages autonomes.

Indiquer l'URL cible recommandée, mais ne pas merger/rediriger automatiquement.

## `NOINDEX`

L'URL ne possède pas encore assez de valeur, de preuve ou de justification pour être indexée. Les recommandations `REDIRECT` ou `REMOVE` issues de `content-audit` peuvent être consignées, mais aucune action destructive n'est automatique.

Pour chaque décision fournir :

- confiance ;
- preuves utilisées ;
- unknowns ;
- blockers ;
- valeur existante à préserver ;
- corrections nécessaires ;
- prochaine étape.

### Handoff

- `KEEP` → aucune rédaction ;
- `LIGHT_UPDATE` → `usage-content-workflow` avec scope de correction limité ;
- `DEEP_REWRITE` → `usage-content-workflow` avec reconstruction guidée par le job et les preuves ;
- `MERGE` / `NOINDEX` → décision humaine avant action structurelle.

---

# 10. Mode `PUBLISH_REVIEW`

Exécuter uniquement sur une version considérée terminée.

## Étape A — validation machine

Exécuter :

```bash
python3 validate_usage_workflow.py
```

Le PASS machine est un plancher structurel, jamais une validation JTBD ou éditoriale.

## Étape B — gates substantiels

Réexécuter au minimum :

- intention satisfaite ;
- job et circonstances réellement visibles ;
- critères reliés aux frictions du job ;
- hypothèses utilisateur signalées comme telles ;
- alternatives hors E Ink considérées lorsqu'elles sont pertinentes ;
- contre-indications honnêtes ;
- absence de ranking produit déguisé ;
- séparation claire avec comparatifs et guides ;
- claims importants sourcés ;
- pas de faux hands-on ;
- valeur réelle sans affiliation ;
- pas de merchant rewrite ;
- pas de cannibalisation non résolue ;
- pas de signal `HIGH` d'AI-slop ;
- architecture justifiée par le job et les preuves, pas par un squelette du cluster ;
- title/H1/canonical/robots cohérents ;
- maillage vers les prochaines étapes réellement utiles.

## Étape C — résultat

### PASS

Retourner exactement :

`PASS — READY_FOR_HUMAN_VALIDATION`

Lister les risques mineurs ou éléments de fraîcheur à surveiller.

### FAIL

Retourner exactement :

`FAIL — KEEP_NOINDEX`

Lister les gates en échec et router chaque correction vers le skill ou workflow approprié. Un FAIL n'entraîne pas automatiquement une réécriture complète.

---

# 11. Indexation et actions irréversibles

Par défaut, conserver l'état robots existant pendant l'analyse et la correction. Pour les pages actuellement en brouillon, maintenir `noindex,follow`.

Ce workflow n'est jamais autorisé à indexer, merger, rediriger ou supprimer automatiquement une URL.

Conditions cumulatives avant indexation d'une page actuellement noindex :

1. validateur machine sans blocker ;
2. `PUBLISH_REVIEW` = `PASS — READY_FOR_HUMAN_VALIDATION` ;
3. validation humaine explicite ;
4. instruction explicite de rendre la route indexable.

---

# 12. Ce que ce workflow ne doit pas devenir

Ne pas ajouter :

- quota de mots ;
- quota de headings ;
- quota de liens ;
- score artificiel de qualité ;
- template fixe par type d'usage ;
- nombre obligatoire d'étapes JTBD ;
- matrice produit obligatoire ;
- générateur de prose ;
- copie locale des règles déjà maintenues dans les skills spécialisés.

La couche custom doit rester limitée à :

1. orchestration ;
2. séparation des rôles entre usages, comparatifs et guides ;
3. adéquation job → page ;
4. cohérence workflow → critères ;
5. comparaison structurelle du cluster.
