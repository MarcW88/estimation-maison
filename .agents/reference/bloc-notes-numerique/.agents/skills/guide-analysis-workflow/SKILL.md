---
name: guide-analysis-workflow
description: Workflow unique d'analyse des pages /guides/ de bloc-notes-numeriques.fr. Audite une URL ou le cluster, contrôle intention, rôle pédagogique, frontières avec usages/comparatifs/marques, preuves, fraîcheur, valeur affiliée, industrialisation éditoriale et SEO, puis décide KEEP, LIGHT_UPDATE, DEEP_REWRITE, MERGE ou NOINDEX. En mode PUBLISH_REVIEW, sert de gate final avant validation humaine.
metadata:
  adapted_for: bloc-notes-numeriques.fr
  orchestration_target: ">=80% existing GitHub skills"
  custom_scope: "orchestration + guide integrity + category boundaries + cluster similarity"
---

# Guide Analysis Workflow

## Rôle

C'est le **seul workflow d'analyse** à utiliser pour les URLs sous `/guides/`.

Il ne rédige pas la page. Il orchestre en priorité les skills spécialisés déjà présents dans le dépôt et ajoute uniquement les contrôles propres à un contenu qui doit **faire comprendre, faire décider ou permettre d'accomplir une tâche**.

Séparation des responsabilités :

- `guide-analysis-workflow` = diagnostiquer, comparer le cluster, décider et effectuer le publish review ;
- `guide-content-workflow` = produire ou corriger uniquement lorsqu'une décision d'analyse le demande.

Frontières générales :

- `/guides/` = comprendre une technologie, un critère, un arbitrage ou une procédure ;
- `/usages/` = comprendre un job, des circonstances, des frictions et le workflow complet ;
- `/comparatifs/` = choisir entre des produits ;
- `/marques/` = comprendre une marque, un écosystème, une gamme ou un produit.

Un guide peut soutenir une décision d'achat sans devenir un classement produit.

---

# 1. Modes

## `AUDIT`

Mode par défaut pour une URL existante.

Retourne une décision et un plan de correction **sans réécrire la page**. L'audit est individuel mais compare aussi les URLs voisines lorsque le risque de chevauchement ou de structure clonée existe.

## `CLUSTER_AUDIT`

Analyse plusieurs URLs `/guides/` ensemble afin de détecter :

- intentions ou tâches qui se chevauchent ;
- guides qui devraient être fusionnés ;
- sous-questions qui appartiennent plutôt à `/usages/`, `/comparatifs/` ou `/marques/` ;
- couverture fragmentée d'un même sujet ;
- trous utiles dans le parcours ;
- architectures éditoriales industrialisées ;
- répétitions de conclusions, tableaux, procédures ou CTA sans justification.

Le mode cluster ne déclenche aucune réécriture automatiquement.

## `PUBLISH_REVIEW`

Gate final après correction ou production via `guide-content-workflow`.

Il réexécute le validateur machine et les contrôles substantiels, puis retourne exactement :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Un PASS n'autorise jamais à retirer `noindex,follow`, à merger ou à déployer sans instruction explicite.

---

# 2. Entrées

Lire selon disponibilité :

- `AGENTS.md` et `DESIGN.md` si le rendu est concerné ;
- la page cible ;
- son brief `.content/briefs/<slug>.md` et son review `.content/reviews/<slug>.md` lorsqu'ils existent ;
- les guides voisins ;
- les pages usages, comparatifs ou marques qui couvrent des sous-questions proches ;
- l'analyse sémantique, GSC, historique ou autres signaux disponibles ;
- la SERP actuelle lorsque l'intention est incertaine ou susceptible d'avoir évolué ;
- les sources actuelles pour les faits instables.

Ne jamais combler une donnée absente avec la mémoire du modèle. Signaler les inconnues qui peuvent changer la décision.

---

# 3. Chaîne de skills réutilisés — source principale de l'analyse

Le workflow doit d'abord **exécuter les skills existants**. Ne pas recopier leurs checklists dans ce fichier et ne pas créer un sous-agent custom lorsqu'une brique existante couvre le besoin.

## 3.1 `seo-content-audit` — Rampstack

Utiliser `.agents/skills/seo-content-audit/SKILL.md` pour déterminer si l'URL mérite d'être conservée, mise à jour, consolidée ou retirée du cluster.

Ce skill porte la logique amont `KEEP / UPDATE / MERGE / REDIRECT / DELETE`. Les actions destructives restent des recommandations tant que l'utilisateur ne les demande pas explicitement.

## 3.2 `seo-keyword` — Rampstack

Utiliser `.agents/skills/seo-keyword/SKILL.md` pour confirmer, lorsque les données le permettent :

- requête ou cluster principal ;
- intention ;
- forme attendue de la réponse ;
- proximité avec d'autres URLs ;
- périmètre trop large ou trop étroit.

Les données GSC ou sémantiques disponibles priment sur une supposition tirée du slug.

## 3.3 `search-intent`

Utiliser en complément lorsque la page doit être examinée finement comme une réponse à une tâche ou une décision : résultat attendu, maturité, sous-questions et sections qui ne servent plus l'intention.

## 3.4 `content-refresh`

Uniquement si une mise à jour est nécessaire. Utiliser le skill pour identifier intent drift, obsolescence, thin value, faiblesse structurelle, cannibalisation, prose générique ou trust gap. Le présent workflow décide ensuite si la correction reste légère ou devient une reconstruction.

## 3.5 `fact-check`

Contrôler les affirmations vérifiables avec une exigence proportionnée à leur stabilité : technologie, formats, compatibilité, procédure, abonnement, prix, fonctionnalités logicielles, génération produit ou conditions d'utilisation.

Une affirmation plausible mais non sourcée reste non vérifiée.

## 3.6 `evidence-based-reviews`

Conditionnel, jamais automatique.

L'utiliser uniquement si le guide contient un **jugement expérientiel produit** ou une conclusion sur un comportement réel qui dépasse ce qu'une documentation officielle permet d'établir. Un guide purement explicatif ou procédural n'a pas besoin de simuler une méthodologie de test produit.

## 3.7 `affiliate-value`

Utiliser lorsque le guide influence l'achat. La page doit rester utile sans liens affiliés et apporter un raisonnement propre : arbitrages, limites, contre-indications, dépendances, coût ou prochaine étape pertinente.

## 3.8 `internal-linking-audit`

Vérifier que les liens répondent à la prochaine question logique du lecteur. Aucun quota de liens ; l'absence d'un lien n'est un problème que lorsqu'une vraie étape du parcours est manquante.

## 3.9 `anti-ai-slop`

Utiliser en review/detection pour rechercher prose générique, symétrie artificielle, sections interchangeables, procédures trop lisses, répétitions et architectures répliquées d'un guide à l'autre.

Ce skill ne sert pas à détecter l'origine du texte.

## 3.10 SEO

- `seo-onpage` : title, meta, H1, couverture utile, structure, maillage, canonical et schema honnête ;
- `seo-technical` : robots, crawlabilité, canonical, HTML et données structurées réellement applicables ;
- `seo-drift` : uniquement lorsqu'un baseline avant/après existe et apporte une information utile.

Aucun quota de mots, headings, tableaux, FAQ, liens ou sources ne sert de proxy de qualité.

## 3.11 `editorial-qa`

Dernière QA générique : intention, valeur originale, factualité, naturel, utilité, SEO et cohérence de la page sans dépendance à l'affiliation.

---

# 4. Couche custom n°1 — quel travail ce guide doit-il accomplir ?

Le type dominant sert de **grille de risque**, jamais de template éditorial.

Trois familles sont utiles pour diagnostiquer le travail principal :

- `CHOICE` : aider à arbitrer entre options, contraintes ou approches sans construire un ranking produit ;
- `EXPLAINER` : rendre compréhensible un mécanisme, une mesure, un format ou une technologie ;
- `HOW_TO` : permettre d'accomplir une tâche, une intégration, un transfert ou une procédure vérifiable.

Un guide peut être hybride. Le type ne doit jamais imposer un nombre de H2, leur ordre, un tableau, une FAQ ou une conclusion standard.

## Pour `CHOICE`

Vérifier surtout :

- la décision exacte à prendre ;
- les critères qui changent réellement cette décision ;
- les compromis et critères éliminatoires ;
- les situations où chaque option cesse d'être adaptée ;
- l'absence de podium produit déguisé.

## Pour `EXPLAINER`

Vérifier surtout :

- concept et termes voisins distingués ;
- mécanisme expliqué sans fausse causalité ;
- lien entre mécanisme et conséquence pratique ;
- limites, exceptions ou simplifications importantes ;
- absence de pseudo-précision technique.

## Pour `HOW_TO`

Vérifier surtout :

- prérequis et contexte nécessaires ;
- étapes vérifiables uniquement lorsque l'ordre compte réellement ;
- différences de version, plateforme ou écosystème ;
- résultat attendu et moyen de vérifier qu'il est obtenu ;
- échecs probables, limites ou alternatives utiles ;
- absence d'étape inventée à partir de la mémoire du modèle.

---

# 5. Couche custom n°2 — frontières éditoriales

## Guide vs Usage

Un guide traite une **sous-question autonome**. Une page usage traite le job complet et les frictions propres à une situation.

Exemple : annotation PDF comme procédure → Guide ; manière dont les PDF changent le workflow étudiant → Usage.

## Guide vs Comparatif

Un guide peut expliquer les critères et arbitrages. Dès qu'il faut sélectionner des candidats, scorer, classer ou recommander des produits entre eux, la décision appartient au comparatif.

## Guide vs Marque

Un guide peut citer plusieurs écosystèmes pour expliquer une différence. Si la question porte principalement sur le fonctionnement, la gamme ou le service d'une marque, la page marque doit posséder ce rôle.

### Test pratique

Si deux URLs peuvent garder le même H1, la même réponse centrale et le même bloc décisionnel en ne changeant que quelques termes, leur séparation est probablement insuffisante.

---

# 6. Couche custom n°3 — intégrité pédagogique et fraîcheur

Un guide n'est pas jugé à sa longueur mais à sa capacité à rendre une chose **plus claire, plus faisable ou plus décidable**.

Vérifier :

- la réponse principale arrive assez tôt pour l'intention ;
- les sections ajoutent une information ou un raisonnement distinct ;
- un tableau est utilisé seulement s'il rend une comparaison plus lisible ;
- une procédure est détaillée seulement autant que nécessaire pour être exécutable ;
- une définition ne remplace pas l'explication de l'impact ;
- une liste ne remplace pas une règle de décision lorsque le lecteur doit arbitrer ;
- les cas limites ou contre-indications importantes ne sont pas masqués.

## Fraîcheur proportionnée

Adapter le niveau de recherche au risque d'obsolescence :

- mécanique physique ou concept stable → vérifier l'exactitude, sans exiger artificiellement une source récente ;
- logiciel, cloud, abonnement, compatibilité, prix, génération produit ou procédure → vérifier actuellement ;
- une date de vérification ne compense jamais une source faible.

---

# 7. Couche custom n°4 — similarité structurelle du cluster

En `AUDIT`, comparer la cible aux guides les plus proches. En `CLUSTER_AUDIT` et `PUBLISH_REVIEW`, regarder le sous-cluster pertinent dans son ensemble.

Chercher notamment :

- mêmes fonctions de H2/H3 dans le même ordre ;
- intro et conclusion identiques avec substitution du sujet ;
- tableau placé systématiquement au même endroit ;
- blocs « avantages / inconvénients / comment choisir / FAQ » répliqués sans besoin ;
- procédures qui gardent artificiellement le même nombre d'étapes ;
- mêmes CTA et mêmes liens comme fin obligatoire ;
- mêmes transitions et rythme de paragraphes ;
- références `choice / explainer / how-to` transformées en squelettes de production.

Les composants visuels communs sont normaux. Le problème apparaît lorsque **la pensée éditoriale est déterminée avant l'intention et les preuves**.

Une industrialisation substantielle peut déclencher `DEEP_REWRITE`.

---

# 8. Décisions `AUDIT` / `CLUSTER_AUDIT`

## `KEEP`

La page possède une tâche claire, distincte, actuelle et utile. Aucun changement substantiel n'est nécessaire.

## `LIGHT_UPDATE`

Corrections ciblées : faits, sources, procédure locale, exemple, title/meta, maillage, frontière avec une autre URL ou quelques passages. L'architecture fondamentale reste pertinente.

## `DEEP_REWRITE`

Réserver ce statut aux problèmes structurants :

- intention ou rôle mal cadré ;
- procédure non fiable ou substantiellement obsolète ;
- explication incapable de relier mécanisme et conséquence ;
- guide de choix qui ne permet pas réellement d'arbitrer ;
- valeur originale faible ;
- preuves insuffisantes sur les claims centraux ;
- cannibalisation forte ;
- architecture fortement industrialisée.

`DEEP_REWRITE` ne signifie pas « tout jeter ». Préserver faits, sources, exemples, passages et raisonnements valides identifiés par l'audit.

## `MERGE`

Une autre URL couvre essentiellement la même tâche ou intention. Indiquer la cible recommandée, sans merger/rediriger automatiquement.

## `NOINDEX`

La page n'a pas encore assez de valeur, de preuve ou de justification pour être indexée. Aucune suppression automatique.

Pour chaque décision fournir :

- confiance ;
- valeur existante à préserver ;
- preuves utilisées ;
- unknowns importants ;
- blockers ;
- améliorations secondaires ;
- risques de cannibalisation ;
- prochaine étape.

### Handoff

- `KEEP` → aucune rédaction ;
- `LIGHT_UPDATE` → `guide-content-workflow` avec scope limité ;
- `DEEP_REWRITE` → `guide-content-workflow` avec reconstruction guidée par l'intention et les preuves ;
- `MERGE` / `NOINDEX` → décision humaine avant action structurelle.

---

# 9. Mode `PUBLISH_REVIEW`

Exécuter uniquement sur une version considérée terminée.

## Étape A — validation machine

Exécuter :

```bash
python3 validate_guide_quality.py
```

Le validateur contrôle uniquement des blockers détectables automatiquement. Il ne valide ni profondeur, ni style, ni exactitude factuelle avec des quotas structurels.

## Étape B — gates substantiels

Réexécuter les skills pertinents et vérifier au minimum :

- intention ou tâche réellement satisfaite ;
- frontière nette avec usages/comparatifs/marques ;
- faits et procédures importants correctement sourcés ;
- fraîcheur adaptée au risque d'obsolescence ;
- aucun faux test ni faux hands-on ;
- aucun classement produit déguisé lorsque la page est un guide ;
- explication, décision ou procédure réellement exploitable ;
- cas limites et restrictions significatives présents ;
- valeur réelle sans affiliation ;
- absence de merchant rewrite ;
- pas de cannibalisation non résolue ;
- pas de signal `HIGH` d'AI-slop ;
- architecture justifiée par la page et non par une référence réutilisée ;
- absence de clonage structurel substantiel avec les guides voisins ;
- title/H1/canonical/robots/liens/schema cohérents ;
- lecture complète de la version rendue si le rendu est disponible.

## Étape C — résultat

### PASS

Retourner exactement :

`PASS — READY_FOR_HUMAN_VALIDATION`

### FAIL

Retourner exactement :

`FAIL — KEEP_NOINDEX`

Lister les gates en échec et router vers le skill ou la passe qui doit corriger le problème. Un FAIL n'entraîne pas automatiquement une réécriture totale.

---

# 10. Indexation

Conserver `noindex,follow` par défaut.

Indexation uniquement après :

1. aucun blocker machine ;
2. `PUBLISH_REVIEW` = `PASS — READY_FOR_HUMAN_VALIDATION` ;
3. validation humaine explicite ;
4. instruction explicite de rendre la page indexable.

---

# 11. Répartition 80/20

La méthodologie doit venir majoritairement des skills existants :

- Rampstack : `seo-content-audit`, `seo-keyword`, `content-brief-authoring`, `content-and-copy`, `seo-onpage` ;
- stack preuve/confiance : `fact-check`, `evidence-based-reviews`, `affiliate-value` ;
- stack éditoriale : `internal-linking-audit`, `humanizer`, `general-writing`, `anti-ai-slop`, `editorial-qa` ;
- contrôles techniques : `seo-technical` et, seulement si utile, `seo-drift`.

La couche custom de ce workflow se limite à :

1. orchestration et mapping des décisions ;
2. intégrité propre aux trois familles de guides ;
3. frontières avec les autres catégories ;
4. fraîcheur proportionnée et similarité structurelle du cluster.

Ne pas ajouter de deuxième méthode SEO, fact-check, rédaction ou qualité à l'intérieur du workflow.

---

# 12. Ce que ce workflow ne doit pas devenir

Ne pas ajouter :

- quota de mots ;
- nombre minimum de H2/H3 ;
- quota de liens ou de sources ;
- nombre obligatoire d'étapes ;
- tableau ou FAQ obligatoire ;
- score artificiel de qualité ;
- template fixe `CHOICE`, `EXPLAINER` ou `HOW_TO` ;
- générateur de texte ;
- duplication des méthodes déjà maintenues dans les skills spécialisés.

Sa valeur est l'orchestration, la décision et le contrôle inter-pages propre au cluster Guides.
