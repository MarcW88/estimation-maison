---
name: brand-analysis-workflow
description: Workflow unique d'analyse des pages /marques/ de bloc-notes-numeriques.fr. Audite une page ou le cluster, compare les architectures, contrôle intention, valeur affiliée, preuves, factualité, AI-slop et SEO, puis décide KEEP, LIGHT_UPDATE, DEEP_REWRITE, MERGE ou NOINDEX. En mode PUBLISH_REVIEW, remplace l'ancien brand-editorial-publish-gate.
metadata:
  adapted_for: bloc-notes-numeriques.fr
  orchestration_target: ">=80% existing skills"
---

# Brand Analysis Workflow

## Rôle

C'est le **seul workflow d'analyse** à utiliser pour les URLs sous `/marques/`.

Il ne réécrit pas la page par défaut. Il orchestre des skills spécialisés déjà présents dans le dépôt et ajoute uniquement les contrôles qui sont propres au cluster marques de bloc-notes-numeriques.fr.

Les autres workflows du site restent autonomes : comparatifs, guides, usages, bons plans et pages de confiance ne passent pas par ce workflow.

## Modes

### `AUDIT`

Mode par défaut pour une URL existante. Retourne une décision et un plan de correction sans produire la nouvelle page.

### `CLUSTER_AUDIT`

Analyse plusieurs URLs `/marques/` ensemble afin de détecter cannibalisation, duplication de rôle et industrialisation de structure.

### `PUBLISH_REVIEW`

Gate final après rédaction. Il vérifie la page individuellement et dans son cluster, exécute le validateur machine et retourne soit :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Un PASS ne retire jamais `noindex,follow` automatiquement.

---

# 1. Entrées

Lire avant l'audit :

- `AGENTS.md` ;
- `brand-workflow.config.yaml` ;
- page cible et pages sœurs pertinentes ;
- données persistées dans `.content/brands/` et `.content/reviews/` ;
- requêtes, GSC ou autres données historiques lorsqu'elles existent ;
- sources actuelles lorsque les faits peuvent avoir évolué.

Ne jamais inventer une donnée absente pour compléter l'audit.

---

# 2. Chaîne de skills obligatoire

L'analyse repose d'abord sur des skills existants. Ne pas recopier leurs checklists dans ce workflow ; les exécuter selon leur rôle.

## 2.1 `content-audit`

Décider si l'URL a encore une fonction autonome et identifier : valeur historique, contenu marchand, obsolescence, faiblesse structurelle, duplication et potentiel de récupération.

Décisions internes possibles : `KEEP`, `UPDATE`, `MERGE`, `REDIRECT`, `REMOVE`.

## 2.2 `search-intent`

Déterminer :

- requête ou topic principal ;
- intention ;
- problème ou décision du lecteur ;
- rôle de l'URL ;
- chevauchements avec les autres URLs ;
- sections qui ne servent pas l'intention.

Utiliser les données disponibles avant d'inférer la cible.

## 2.3 `content-refresh`

Uniquement lorsque `content-audit` conclut `UPDATE`. Diagnostiquer `Intent drift`, `Thin value`, `Merchant duplication`, `Outdated`, `Weak structure`, `Cannibalization`, `Generic prose` ou `Trust gap`, puis recommander correction légère, révision majeure ou réécriture complète.

## 2.4 `affiliate-value`

Vérifier que la page conserve une vraie valeur si tous les liens affiliés sont supprimés. Contrôler notamment : limites, alternatives, compatibilités, coût réel, critères d'achat et absence de faux test.

## 2.5 `fact-check`

Extraire les claims vérifiables, appliquer la hiérarchie de sources et classer chaque claim important. Une affirmation plausible mais non sourcée reste non vérifiée.

## 2.6 `evidence-based-reviews`

Obligatoire pour les pages `REVIEW` et pour toute page contenant un jugement produit important. Vérifier l'adéquation entre verdict et niveaux de preuve, les sources expertes, les patterns utilisateurs et l'absence de hands-on fictif.

## 2.7 `internal-linking-audit`

Vérifier que les liens internes servent une étape logique du parcours : produit, review, comparatif, usage, guide, service, accessoire ou alternative. Aucun quota.

## 2.8 `anti-ai-slop`

Utiliser en mode review/detection. Rechercher les sorties génériques, sur-lissées, répétitives, trop symétriques ou applicables à n'importe quelle marque. Toute critique doit pointer vers un élément visible.

## 2.9 SEO

Utiliser `seo-technical` pour les points techniques réellement applicables : indexability, canonical, robots, structured data, crawlabilité et architecture.

Utiliser `seo-best-practices` uniquement pour les règles pertinentes au HTML statique du site ; ignorer les prescriptions propres à React/Laravel qui ne s'appliquent pas.

Utiliser `seo-drift` seulement si un baseline ou une comparaison avant/après est disponible et utile. Ce n'est pas un gate obligatoire.

## 2.10 `editorial-qa`

Dernière QA générique : intention, valeur originale, factualité, naturel, SEO et utilité réelle sans affiliation.

---

# 3. Contrôle custom n°1 — adéquation au rôle de page

Le type de page sert de **grille de risque**, jamais de template éditorial.

Types : `DIRECTORY`, `BRAND_HUB`, `PRODUCT`, `REVIEW`, `SERVICE`, `ACCESSORY_HUB`, `ALTERNATIVES`.

Vérifier seulement les questions qui changent la décision :

- `DIRECTORY` : distingue réellement les univers sans refaire le comparatif général ;
- `BRAND_HUB` : permet de comprendre la gamme et l'écosystème lorsque ces éléments sont nécessaires ;
- `PRODUCT` : statut/génération, caractéristiques décisionnelles et compatibilités ;
- `REVIEW` : verdict proportionnel aux preuves, distinct de la fiche produit ;
- `SERVICE` : fonctions, coût, dépendance, données et fonctionnement sans service ;
- `ACCESSORY_HUB` : compatibilités exactes et utilité réelle ;
- `ALTERNATIVES` : raisons concrètes de changer et alternatives adaptées à ces raisons.

Ne jamais exiger les mêmes headings, le même ordre ou le même nombre de sections entre deux pages du même type.

---

# 4. Contrôle custom n°2 — similarité structurelle du cluster

Ce contrôle répond au risque principal de production industrialisée.

En `AUDIT`, comparer au minimum la page cible avec les pages sœurs les plus proches. En `CLUSTER_AUDIT` et `PUBLISH_REVIEW`, regarder le cluster pertinent dans son ensemble.

Comparer :

- intitulés et fonctions sémantiques des H2/H3 ;
- ordre des questions traitées ;
- forme des introductions ;
- répétition de blocs « forces / limites / pour qui / verdict » ;
- emplacement systématique des tableaux, listes ou CTA ;
- rythme des paragraphes et conclusions ;
- phrases ou transitions recyclées ;
- mêmes critères appliqués à des marques dont les vrais enjeux sont différents.

## Règle

Une similarité visuelle ou quelques composants partagés ne sont pas un problème en soi. Le FAIL intervient lorsque **l'architecture éditoriale semble dictée par un squelette réutilisé plutôt que par l'intention et les preuves de la page**.

Signaux forts :

- plusieurs pages gardent les mêmes rôles de sections dans le même ordre alors que les questions utilisateurs diffèrent ;
- une section existe uniquement parce qu'elle existe chez les autres marques ;
- les détails spécifiques pourraient être permutés entre pages sans modifier l'argument ;
- les mêmes recommandations « pour qui / moins adapté » sont répétées avec changement de marque ;
- le plan ne peut pas être justifié par le research/evidence brief de la page.

Si ce problème est substantiel : `DEEP_REWRITE`.

---

# 5. Contrôle de preuves

La hiérarchie par défaut est :

1. fabricant / documentation / manuel officiel ;
2. distributeur officiel ;
3. retailer fiable pour disponibilité ou information commerciale complémentaire ;
4. tests et publications indépendantes nommées ;
5. plusieurs sources utilisateurs pour des patterns d'expérience.

Une autre page affiliée ne sert pas de source primaire de spécification lorsqu'une source officielle est disponible.

Pour les informations importantes utiliser : `VERIFIED`, `SUPPORTED`, `INFERRED`, `UNKNOWN`, `OUTDATED`, `CONTRADICTED`.

`UNKNOWN` et `CONTRADICTED` ne peuvent pas être transformés en certitude rédactionnelle.

---

# 6. Décision finale AUDIT / CLUSTER_AUDIT

Mapper les résultats vers cinq statuts simples :

### `KEEP`

Page forte, actuelle, distincte et utile. Pas de modification substantielle requise.

### `LIGHT_UPDATE`

Corrections ciblées : facts, sources, quelques passages, liens ou faiblesse éditoriale locale. La structure fondamentale reste pertinente.

### `DEEP_REWRITE`

Intent mal servi, valeur faible, architecture générique, contenu marchand, preuves insuffisantes, structure industrialisée ou besoin de reconstruction importante.

### `MERGE`

Une autre URL couvre pratiquement la même intention et la distinction ne justifie pas deux pages.

### `NOINDEX`

La page ne possède pas encore assez de valeur ou de justification pour être indexée. Les recommandations `REDIRECT`/`REMOVE` du skill `content-audit` peuvent être consignées ici, mais aucune suppression ou redirection n'est appliquée automatiquement.

Pour chaque décision donner :

- confiance ;
- preuves utilisées ;
- unknowns ;
- blockers ;
- valeur déjà présente ;
- actions nécessaires ;
- prochaine étape.

Pour `DEEP_REWRITE`, passer la main à `brand-content-workflow`.

---

# 7. Mode PUBLISH_REVIEW

Exécuter uniquement sur un draft considéré terminé.

## Étape A — validation machine

Exécuter :

```bash
python3 validate_brands.py
```

Un PASS machine n'est qu'un plancher structurel.

## Étape B — réexécuter les gates substantiels

Vérifier au minimum :

- intention satisfaite ;
- valeur affiliée originale ;
- claims importants sourcés ;
- niveau de preuve honnête ;
- pas de faux test ;
- pas de métadiscours SEO/éditeur dans la prose ;
- pas de merchant rewrite ;
- pas de cannibalisation non résolue ;
- pas de signal `HIGH` d'AI-slop ;
- architecture propre à la page et justifiée par son research brief ;
- absence de clonage structurel substantiel avec les pages sœurs ;
- title/H1/canonical/robots cohérents ;
- liens et schema honnêtes ;
- page utile même sans liens affiliés.

## Étape C — résultat

### PASS

Retourner exactement le statut :

`PASS — READY_FOR_HUMAN_VALIDATION`

Lister les éventuels risques mineurs restants.

### FAIL

Retourner :

`FAIL — KEEP_NOINDEX`

Lister les gates en échec et router vers le skill ou le workflow qui doit corriger le problème. Un FAIL n'entraîne pas automatiquement une réécriture complète.

---

# 8. Indexation

Par défaut, toutes les pages travaillées restent `noindex,follow`.

Le workflow n'est jamais autorisé à retirer `noindex` seul. Conditions cumulatives avant une future indexation :

1. aucun blocker dans `validate_brands.py` ;
2. `PUBLISH_REVIEW` = `PASS — READY_FOR_HUMAN_VALIDATION` ;
3. validation humaine explicite ;
4. instruction explicite de rendre la page indexable.

---

# 9. Ce que ce workflow ne doit pas devenir

Ne pas ajouter :

- quotas de mots ;
- quotas de headings ;
- quotas de liens ;
- score artificiel de qualité ;
- template fixe par type de page ;
- générateur de texte ;
- deuxième copie des règles déjà maintenues dans les skills appelés.

Sa valeur est l'orchestration, la décision et le contrôle inter-pages propre au cluster marques.
