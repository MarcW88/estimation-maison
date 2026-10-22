---
name: brand-content-workflow
description: Workflow unique de rédaction et de refonte des pages /marques/ de bloc-notes-numeriques.fr. Orchestre majoritairement des skills GitHub existants pour produire un contenu d'affiliation e-commerce utile, sourcé, fact-checké, non templatisé et sans faux test. La structure éditoriale doit découler de l'intention et des preuves, jamais du seul type de page.
metadata:
  adapted_for: bloc-notes-numeriques.fr
  orchestration_target: ">=80% existing skills"
---

# Brand Content Workflow

## Rôle

C'est le **seul workflow de production** à utiliser pour créer ou réécrire une URL sous `/marques/`.

Il orchestre des skills existants plutôt que de réimplémenter leur méthode. Le custom doit rester limité au contexte du site, au choix d'une architecture propre à l'URL et au handoff vers le workflow d'analyse.

Principe central :

> **Pas de plan avant l'intention et les preuves. Pas de claim important sans source. Pas de template éditorial par type de page.**

Le but n'est pas de produire un texte « SEO complet », mais une page d'affiliation e-commerce qui aide réellement le lecteur à comprendre, vérifier et décider.

---

# 1. Entrées obligatoires

Lire :

- `AGENTS.md` ;
- `brand-workflow.config.yaml` ;
- URL cible et contenu existant le cas échéant ;
- pages sœurs pertinentes ;
- `.content/brands/` et `.content/reviews/` ;
- données GSC, sémantiques ou historiques disponibles ;
- sources actuelles nécessaires à la vérification.

Pour une page existante, commencer obligatoirement par :

`.agents/skills/brand-analysis-workflow/SKILL.md` en mode `AUDIT`.

Ne pas lancer une réécriture profonde si l'audit conclut `KEEP`, `LIGHT_UPDATE`, `MERGE` ou `NOINDEX` sans raison documentée de changer cette décision.

---

# 2. Chaîne de production fondée sur les skills existants

## 2.1 Intention — `search-intent`

Avant toute recherche de plan, établir :

- requête/topic principal ;
- intention ;
- décision ou problème concret du lecteur ;
- rôle de l'URL par rapport aux autres pages ;
- prochaine question logique ;
- risque de cannibalisation.

Lorsque des données historiques existent, les utiliser avant d'inférer la cible.

## 2.2 Audit/récupération — `content-audit` + `content-refresh`

Pour une page existante :

- utiliser `content-audit` pour décider ce qui mérite d'être conservé ;
- si `UPDATE`, utiliser `content-refresh` afin de distinguer correction légère, révision majeure et réécriture complète ;
- préserver les passages concrets, les liens utiles, les tableaux décisionnels et les faits encore valides ;
- ne pas remplacer automatiquement une bonne information par une prose plus fluide mais plus vague.

Pour une nouvelle page, cette étape est `N/A`.

## 2.3 Recherche et evidence brief — `fact-check`

La recherche précède le plan et la rédaction.

Construire un registre des affirmations nécessaires avec au minimum :

| Question / claim | Source | Date | Status | Utilité pour la décision |
|---|---|---|---|---|

Hiérarchie de sources par défaut :

1. fabricant, support ou manuel officiel ;
2. distributeur officiel ;
3. retailer fiable pour disponibilité ou information commerciale complémentaire ;
4. tests et médias spécialisés indépendants nommés ;
5. plusieurs sources utilisateurs lorsqu'un pattern d'expérience est réellement étudié.

Statuts : `VERIFIED`, `SUPPORTED`, `INFERRED`, `UNKNOWN`, `OUTDATED`, `CONTRADICTED`.

Règles :

- ne jamais utiliser la mémoire du modèle pour combler `UNKNOWN` ;
- ne pas utiliser une autre page affiliée comme source primaire d'une spécification lorsqu'une source officielle existe ;
- dater les informations susceptibles d'évoluer ;
- conserver les contradictions entre sources au lieu de les lisser.

## 2.4 Reviews et jugements — `evidence-based-reviews`

Obligatoire pour `REVIEW` et dès qu'une page formule un jugement important sur qualité, ergonomie, autonomie observée, fiabilité ou expérience.

Utiliser les quatre tiers :

- Tier 1 : specs fabricant vérifiées ;
- Tier 2 : synthèse utilisateurs à échelle suffisante ;
- Tier 3 : triangulation de sources expertes ;
- Tier 4 : hands-on uniquement si un vrai test documenté existe.

Une sensation ou observation issue d'un autre test ne devient jamais une expérience propre au site.

## 2.5 Valeur originale — `affiliate-value`

Avant le plan, identifier la valeur que la page peut apporter au-delà du fabricant et des marchands.

Selon l'intention, cela peut être :

- conséquence réelle d'une compatibilité ;
- distinction entre générations ;
- coût complet ;
- accessoire obligatoire ou inutile ;
- dépendance à un service ou abonnement ;
- contrainte logicielle ;
- alternative plus rationnelle ;
- situation dans laquelle il vaut mieux ne pas acheter ;
- synthèse de preuves contradictoires ;
- critère qui change réellement la décision.

Test obligatoire : **la page reste-t-elle utile si tous les liens affiliés disparaissent ?**

---

# 3. Construction libre mais justifiée du plan

C'est la seule étape éditoriale substantielle propre à ce workflow.

Le plan est construit **après** `search-intent`, l'evidence brief et `affiliate-value`.

Pour chaque section proposée, pouvoir répondre :

1. quelle question du lecteur cette section résout-elle ?
2. quelles preuves permettent de l'écrire ?
3. quelle décision ou compréhension améliore-t-elle ?
4. pourquoi cette information mérite-t-elle sa propre section plutôt qu'une phrase ailleurs ?

Si ces réponses sont faibles, supprimer ou fusionner la section.

## Interdiction de template par page type

Le type de page indique des risques factuels et des frontières, pas une architecture.

Il est interdit de définir :

- un nombre fixe de H2/H3 ;
- un ordre standard « gamme → forces → limites → pour qui → verdict » ;
- un tableau obligatoire ;
- une FAQ automatique ;
- une conclusion automatique ;
- un minimum de mots ou de liens.

Deux `BRAND_HUB` peuvent et doivent avoir des architectures différentes si leurs écosystèmes, leurs produits et les questions des utilisateurs diffèrent.

---

# 4. Le type de page comme garde-fou, pas comme squelette

## `DIRECTORY`

Éviter de refaire le comparatif général. Aider à comprendre les différences de logique entre marques et à choisir la prochaine page pertinente.

## `BRAND_HUB`

Vérifier la gamme actuelle, les générations et l'écosystème lorsque ces éléments changent réellement le choix. Ne pas imposer une section pour chacun.

## `PRODUCT`

Se concentrer sur le modèle : statut, génération, caractéristiques décisionnelles, compatibilités, coût ou contraintes. Ne pas dupliquer une review séparée.

## `REVIEW`

Produire un jugement traçable aux preuves. Distinguer clairement desk research, synthèse indépendante et éventuel hands-on réel.

## `SERVICE`

Traiter ce qui change l'usage : fonctions, coût, gratuit/payant, dépendance, données, fonctionnement sans le service, lock-in éventuel.

## `ACCESSORY_HUB`

Privilégier compatibilités exactes, génération, utilité réelle et coût. Une matrice est utile seulement si elle réduit une vraie ambiguïté.

## `ALTERNATIVES`

Partir de la raison de quitter la marque ou le produit. Les alternatives doivent résoudre cette limite précise, pas former un classement générique.

---

# 5. Rédaction à partir des preuves

Le draft doit utiliser le research/evidence brief comme frontière factuelle.

Règles :

- chaque claim important doit pouvoir être relié à une source ou être clairement présenté comme déduction ;
- aucune donnée, prix, génération, compatibilité, date, garantie, performance ou expérience ne peut être inventée pour « compléter » la page ;
- éviter la paraphrase fabricant lorsque la conséquence pour le lecteur n'est pas expliquée ;
- afficher les limites aussi clairement que les avantages ;
- ne pas écrire une section uniquement pour placer un mot-clé ou un lien ;
- ne pas simuler d'expérience utilisateur ;
- ne pas faire varier le verdict selon la commission.

La prose finale ne doit pas parler de SEO, GEO, hub, maillage, intention, page type ou stratégie éditoriale.

---

# 6. Fact-check post-draft — `fact-check`

Après rédaction :

1. réextraire les claims vérifiables du draft ;
2. comparer avec l'evidence brief ;
3. recontrôler les affirmations ajoutées ou reformulées ;
4. corriger les claims `OUTDATED` ou `CONTRADICTED` ;
5. qualifier ou supprimer `UNKNOWN` ;
6. s'assurer qu'aucune synthèse utilisateur ou experte n'est devenue une expérience propre.

Le fact-check est séparé de la rédaction précisément pour éviter qu'une phrase plausible soit acceptée parce qu'elle « sonne juste ».

---

# 7. Finition éditoriale — stack externe

Utiliser dans cet ordre :

1. `humanizer` en mode embedded ;
2. `general-writing` comme house-style pass ;
3. `anti-ai-slop` pour le contrôle final du caractère purpose-built.

`humanizer` orchestre déjà les passes associées `better-usage`, `academic-voice`, `writing-cadence` et `non-autoregressive-writing-pass` lorsque nécessaire. Ne pas les exécuter une deuxième fois par réflexe.

Pour les pages marques françaises, ne pas utiliser `natural-writing` comme étape obligatoire : ce skill est spécifique au néerlandais et reste présent pour les workflows qui en dépendent encore.

La finition doit pouvoir modifier la structure si elle apparaît mécanique, mais **elle ne peut ajouter aucun fait qui n'existe pas dans les preuves**.

À contrôler particulièrement :

- même rythme sur toutes les sections ;
- rule of three artificielle ;
- intro qui reformule le H1 ;
- conclusion qui résume sans apporter d'information ;
- transitions génériques ;
- headings interchangeables avec une autre marque ;
- structure trop parfaite ou symétrique ;
- listes utilisées à la place d'un raisonnement ;
- surpromesse commerciale.

---

# 8. Maillage — `internal-linking-audit`

Ajouter uniquement les liens qui répondent à une prochaine question logique.

Exemples possibles selon la page : produit, review, comparatif, alternative, service, accessoire, usage, guide ou bon plan.

Aucun quota de liens ni de destinations.

---

# 9. SEO

Utiliser :

- `seo-technical` pour canonical, robots, indexability, schema, crawlabilité et architecture technique pertinente ;
- `seo-best-practices` uniquement pour les règles applicables au site statique ;
- `seo-drift` seulement si un baseline ou une régression doit être comparé.

Vérifier title, H1, intention, canonical, breadcrumbs, structured data honnête, liens et cannibalisation.

Aucun nombre de mots, headings, tableaux ou liens n'est un KPI de qualité.

---

# 10. QA générique — `editorial-qa`

La page doit passer l'intention, la valeur originale, la factualité, le naturel, le SEO et l'utilité sans affiliation.

Un contenu factuellement correct peut encore échouer s'il est générique, marchand ou insuffisamment décisionnel.

---

# 11. Gate final — `brand-analysis-workflow` / `PUBLISH_REVIEW`

Une fois le draft stable, appeler :

`.agents/skills/brand-analysis-workflow/SKILL.md` en mode `PUBLISH_REVIEW`.

Cette étape :

- exécute `python3 validate_brands.py` ;
- recontrôle les preuves et l'intention ;
- compare la structure aux pages sœurs ;
- cherche l'industrialisation éditoriale ;
- vérifie les blockers propres aux pages marques.

Résultat attendu avant validation humaine :

`PASS — READY_FOR_HUMAN_VALIDATION`

Sinon :

`FAIL — KEEP_NOINDEX`

---

# 12. Persistance

Conserver dans `.content/brands/` ou `.content/reviews/` selon le cas :

- cadrage de l'intention ;
- research/evidence brief ;
- statut des claims ;
- sources et date de vérification ;
- valeur originale recherchée ;
- justification du plan ;
- résultat de l'audit et du `PUBLISH_REVIEW`.

Le HTML final ne doit jamais être l'unique endroit où les preuves sont documentées.

---

# 13. Indexation

Par défaut, conserver `noindex,follow`.

Le workflow n'est jamais autorisé à retirer le `noindex` automatiquement.

Conditions cumulatives avant une future indexation :

1. `validate_brands.py` sans blocker ;
2. `brand-analysis-workflow` / `PUBLISH_REVIEW` = `PASS — READY_FOR_HUMAN_VALIDATION` ;
3. validation humaine explicite ;
4. instruction explicite de rendre la page indexable.

---

# 14. Résumé de l'orchestration

```text
PAGE EXISTANTE
  brand-analysis-workflow / AUDIT
        ↓
search-intent
        ↓
content-audit + content-refresh si nécessaire
        ↓
fact-check → evidence brief
        ↓
evidence-based-reviews si jugement/review
        ↓
affiliate-value
        ↓
PLAN SPÉCIFIQUE À L'URL
        ↓
rédaction depuis les preuves
        ↓
fact-check post-draft
        ↓
humanizer → general-writing → anti-ai-slop
        ↓
internal-linking-audit
        ↓
SEO pertinent
        ↓
editorial-qa
        ↓
brand-analysis-workflow / PUBLISH_REVIEW
        ↓
validation humaine
```

Le workflow orchestre ; il ne remplace pas ses skills spécialisés.
