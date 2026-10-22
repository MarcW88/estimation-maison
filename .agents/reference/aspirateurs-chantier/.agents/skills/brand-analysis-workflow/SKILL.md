---
name: brand-analysis-workflow
description: Orchestration 80/20 d'audit et de publish review des pages /marques/ d'aspirateurs-chantier.fr. Les contrôles génériques restent délégués aux skills partagés vendored depuis bloc-notes-numerique ; le custom se limite aux risques métier aspirateurs et à la distinctivité inter-marques.
metadata:
  adapted_for: aspirateurs-chantier.fr
  source_workflow: bloc-notes-numeriques.fr/brand-analysis-workflow
  orchestration_target: ">=80% shared responsibilities; <=20% custom"
---

# Brand Analysis Workflow — aspirateurs-chantier.fr

## Contrat 80/20

Ce workflow décide ; il ne remplace pas les skills spécialisés.

- **>=80% shared** : audit, intention, refresh, affiliate value, fact-check, evidence-based reviews, maillage, anti-AI, SEO et editorial QA restent propriétaires de leurs skills partagés.
- **<=20% custom** : contrôle des risques métier aspirateurs + comparaison structurelle/inter-pages + décision finale.

Avant toute analyse :

```bash
python3 validate_brand_skill_stack.py
```

## Modes

- `AUDIT` : une page existante ;
- `CLUSTER_AUDIT` : plusieurs marques ensemble ;
- `PUBLISH_REVIEW` : gate final d'un draft déjà produit par `brand-content-workflow`.

---

# 1. Shared skills à orchestrer

Ne pas recopier leurs checklists. Utiliser selon leur rôle :

- `content-audit` ;
- `search-intent` ;
- `content-refresh` si UPDATE ;
- `affiliate-value` ;
- `fact-check` ;
- `evidence-based-reviews` pour tout jugement important ;
- `internal-linking-audit` ;
- `anti-ai-slop` en review ;
- `seo-technical` ;
- `seo-best-practices` ;
- `editorial-qa`.

En `PUBLISH_REVIEW`, vérifier également la trace des étapes de production `content-brief-authoring`, `content-and-copy`, `humanizer` et `general-writing` dans le run-evidence v2.

---

# 2. AUDIT — rôle et valeur de l'URL

Déterminer d'abord avec les shared skills :

- intention réelle ;
- décision ou problème du lecteur ;
- rôle autonome dans le cluster ;
- valeur existante à préserver ;
- faits obsolètes ou non prouvés ;
- dépendance excessive aux fiches fabricant ;
- valeur qui subsiste sans affiliation ;
- chevauchement avec `/modeles/`, `/comparatifs/`, `/guides/`, `/usages/`.

Ne pas produire un plan avant d'avoir ces éléments.

---

# 3. Custom n°1 — contrôle métier aspirateurs

Seulement lorsqu'ils sont pertinents pour la marque, contrôler : classes L/M/H, filtre vs classe, débit/dépression et protocole, capacité, décolmatage, prise outil, antistatique, raccords, plateformes batteries, consommables, eau/poussière, poids/mobilité et statut de génération.

FAIL si :

- une classe est déduite de la puissance ou de la filtration ;
- deux métriques non comparables sont mises sur le même plan sans qualification ;
- une donnée fabricant ou tierce devient une observation maison ;
- une recommandation sécurité personnalisée dépasse les preuves disponibles.

Ce contrôle ne doit jamais devenir un deuxième `fact-check` custom.

---

# 4. Custom n°2 — distinctivité inter-marques

Comparer la page aux marques sœurs sur :

- rôle des H2/H3 et leur ordre ;
- question réellement résolue par chaque section ;
- intro / answer-box ;
- emplacement systématique de tableaux et CTA ;
- répétition de blocs « gamme / forces / limites / pour qui / éviter » ;
- paragraphes de transition ;
- recommandations interchangeables ;
- architecture dictée par un générateur plutôt que par les preuves.

Une cohérence visuelle est normale. Une architecture éditoriale clonée ne l'est pas.

Signaux de `DEEP_REWRITE` :

- plusieurs marques suivent la même signature de sections malgré des décisions différentes ;
- une section n'a pas de question lecteur identifiable ;
- son existence n'est pas justifiable par le brief/evidence ledger ;
- des paragraphes longs peuvent être copiés d'une marque à l'autre en changeant seulement le nom ;
- l'output est plus proche d'une fiche catalogue que d'une aide à la décision.

---

# 5. Décision AUDIT / CLUSTER_AUDIT

- `KEEP` : forte, actuelle, distincte et utile ;
- `LIGHT_UPDATE` : corrections ciblées sans reconstruction ;
- `DEEP_REWRITE` : intention mal servie, valeur faible, recherche trop superficielle ou architecture générique ;
- `MERGE` : intention pratiquement identique à une autre URL ;
- `NOINDEX` : valeur/justification encore insuffisante.

Retourner : confiance, preuves, unknowns, blockers, valeur existante, actions nécessaires et prochaine étape.

`DEEP_REWRITE` route vers `brand-content-workflow`.

---

# 6. PUBLISH_REVIEW — preuve d'exécution obligatoire

Avant de pouvoir retourner un PASS :

```bash
python3 validate_brand_skill_stack.py
python3 _validate_brands.py
python3 validate_brand_run_evidence.py --slug <slug> --require-run
```

Puis vérifier substantiellement :

- intention satisfaite ;
- valeur utile même sans affiliation ;
- claims importants reliés aux preuves ;
- contradictions/unknowns correctement qualifiés ;
- niveau de preuve honnête ;
- aucun faux test ;
- architecture issue du brief propre à l'URL ;
- aucune industrialisation structurelle substantielle ;
- résultats des passes `humanizer`, `general-writing`, `anti-ai-slop` pris en compte ;
- liens internes répondant à la prochaine question ;
- SEO technique cohérent ;
- limitations aussi visibles que les avantages lorsque décisionnelles.

Un fichier d'audit de quelques lignes ou un flag généré par Python ne constitue pas un PUBLISH_REVIEW.

## Résultat

PASS exact :

`PASS — READY_FOR_HUMAN_VALIDATION`

Sinon :

`FAIL — KEEP_NOINDEX`

Le run-evidence v2 doit enregistrer le résultat sous `brand-analysis-publish-review`.

---

# 7. Indexation

Le workflow conserve `noindex, follow` par défaut.

Conditions cumulatives avant indexation :

1. stack shared/custom valide ;
2. run-evidence v2 valide ;
3. `_validate_brands.py` sans blocker ;
4. `PUBLISH_REVIEW = PASS — READY_FOR_HUMAN_VALIDATION` ;
5. validation humaine explicite ;
6. instruction explicite d'indexer.

---

# 8. Limites du custom

Ne pas ajouter de quotas de mots, headings ou liens. Ne pas créer de score artificiel. Ne pas transformer le type `BRAND_HUB` en squelette. Ne pas coder un nouveau moteur de recherche, de fact-check, de rédaction ou de style dans ce workflow.

La gouvernance reste **>=80% shared / <=20% custom**. Le custom sert à adapter le domaine et à prendre la décision inter-pages, pas à remplacer les skills provenant des repos existants.
