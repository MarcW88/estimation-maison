---
name: model-analysis-workflow
description: Workflow 80/20 d'audit, cluster audit et publish review des pages /modeles/ d'aspirateurs-chantier.fr. Les contrôles génériques sont délégués aux skills partagés ; le custom se limite aux contraintes d'une référence, à la distinctivité inter-modèles et à la décision finale.
metadata:
  adapted_for: aspirateurs-chantier.fr
  source_workflow: aspirateurs-chantier.fr/brand-analysis-workflow
  reference_pattern: bloc-notes-numeriques.fr PRODUCT/REVIEW
  orchestration_target: ">=80% shared responsibilities; <=20% custom"
---

# Model Analysis Workflow — aspirateurs-chantier.fr

## Contrat 80/20

Ce workflow décide ; il ne remplace pas les skills spécialisés.

- **>=80% shared** : audit, intention, refresh, valeur affiliée, fact-check, evidence-based reviews, maillage, anti-AI, SEO et QA.
- **<=20% custom** : contrôle métier d'une référence + distinctivité/cannibalisation inter-modèles + décision de publication.

Avant toute analyse :

```bash
python3 validate_model_skill_stack.py
```

## 1. Modes

### `AUDIT`
Analyse une URL existante et retourne une décision et un plan de correction sans réécrire.

### `CLUSTER_AUDIT`
Compare plusieurs pages `/modeles/` pour détecter duplication de rôle, cannibalisation, architectures clonées et références qui ne justifient plus une URL autonome.

### `PUBLISH_REVIEW`
Gate final d'un draft produit par `model-content-workflow`.

Résultats exacts :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Un PASS n'indexe jamais automatiquement la page.

## 2. Entrées

Lire :

- `model-workflow.config.yaml` ;
- `.content/models/model-evidence.json` ;
- page cible et pages sœurs pertinentes ;
- `.content/models/runs/<slug>.json` s'il existe ;
- page marque ;
- comparatifs, usages et guides adjacents ;
- données historiques ;
- sources actuelles.

`model-evidence.json` est une base de faits primaires, pas une garantie d'intention, de profondeur, de valeur originale ou de distinctivité.

## 3. Shared skills obligatoires

Utiliser selon leur rôle, sans recopier leurs checklists :

- `content-audit`
- `search-intent`
- `content-refresh` si UPDATE
- `affiliate-value`
- `fact-check`
- `evidence-based-reviews` pour tout jugement important
- `internal-linking-audit`
- `anti-ai-slop`
- `seo-technical`
- `seo-best-practices`
- `editorial-qa`

En `PUBLISH_REVIEW`, vérifier aussi la trace de `content-brief-authoring`, `content-and-copy`, `humanizer` et `general-writing` dans le run-evidence v2.

## 4. AUDIT — rôle et intention

Déterminer :

- requête/topic principal ;
- problème ou décision du lecteur ;
- rôle autonome de la référence ;
- valeur existante à préserver ;
- faits obsolètes ou non prouvés ;
- dépendance aux descriptions fabricant ;
- valeur sans affiliation ;
- chevauchement avec d'autres `/modeles/` ;
- chevauchement avec `/marques/`, `/comparatifs/`, `/usages/`, `/guides/`.

Frontière centrale :

- MODEL = décider sur une référence ;
- COMPARISON = choisir entre plusieurs références ;
- BRAND_HUB = comprendre une gamme ;
- USAGE = partir d'un contexte de travail ;
- GUIDE = expliquer un concept.

## 5. Custom n°1 — vacuum model domain review

Contrôler quand pertinent :

- identité exacte, suffixe, variante, génération ;
- statut actuel/discontinué ;
- classe L/M/H et source de certification ;
- filtre vs classe ;
- débit/dépression et point/protocole de mesure ;
- capacité brute/net/eau ;
- décolmatage ;
- prise outil/Auto-Start ;
- antistatique ;
- eau/poussière ;
- batterie/plateforme ;
- flexibles/raccords/consommables ;
- poids, mobilité, encombrement ;
- compatibilités de génération.

FAIL si :

- classe déduite de la puissance, du filtre ou du marketing ;
- mesures non comparables mises au même niveau sans qualification ;
- donnée fabricant/test tiers transformée en observation maison ;
- variante décrite avec les specs d'une autre ;
- recommandation sécurité personnalisée au-delà des preuves.

Ce contrôle ne remplace pas `fact-check`.

## 6. Custom n°2 — distinctivité et cannibalisation

Comparer la page aux modèles les plus proches sur :

- question résolue par chaque section ;
- rôle et ordre des H2/H3 ;
- intro/answer-box ;
- placement systématique tableaux/CTA ;
- répétition « specs / pour qui / limites / source » ;
- transitions recyclées ;
- recommandations interchangeables ;
- paragraphes longs communs ;
- critères d'achat ;
- frontière avec le comparatif correspondant.

Une cohérence visuelle est normale. Une architecture éditoriale clonée ne l'est pas.

Signaux de `DEEP_REWRITE` :

- même signature de sections malgré des décisions différentes ;
- section sans question lecteur identifiable ;
- paragraphe réutilisable en changeant seulement le nom du modèle ;
- `best_for`/`limits` réduits à des champs catalogue reformulés ;
- répétition du comparatif sans analyse propre ;
- plan non justifiable par l'evidence brief.

## 7. Contrôle des preuves

Statuts :

`VERIFIED`, `SUPPORTED`, `INFERRED`, `UNKNOWN`, `OUTDATED`, `CONTRADICTED`.

`UNKNOWN` ne peut pas être comblé par mémoire modèle.

Pour un jugement important :

- Tier 1 : fabricant/documentation
- Tier 2 : patterns utilisateurs
- Tier 3 : triangulation experte
- Tier 4 : test hands-on réel uniquement

Une page modèle n'a pas besoin de Tier 4 pour être utile.

## 8. Décision AUDIT / CLUSTER_AUDIT

- `KEEP` : forte, actuelle, distincte, utile.
- `LIGHT_UPDATE` : corrections ciblées.
- `DEEP_REWRITE` : intention mal servie, valeur faible, recherche superficielle, merchant rewrite, preuve insuffisante ou clonage.
- `MERGE` : autre URL couvre presque la même intention ou référence sans rôle autonome suffisant.
- `NOINDEX` : valeur/justification encore insuffisante.

Retourner : confiance, preuves, unknowns, blockers, valeur existante, actions nécessaires et prochaine étape.

`DEEP_REWRITE` route vers `model-content-workflow`.

## 9. PUBLISH_REVIEW

Avant un PASS :

```bash
python3 validate_model_skill_stack.py
python3 validate_model_run_evidence.py --slug <slug> --require-run
```

Puis vérifier :

- intention satisfaite ;
- rôle MODEL respecté ;
- valeur utile sans affiliation ;
- claims reliés aux preuves ;
- contradictions/unknowns qualifiés ;
- identité/variante/génération exactes ;
- niveau de preuve honnête ;
- aucun faux test ;
- aucune inférence abusive de classe L/M/H ;
- plan issu du brief propre à l'URL ;
- pas de clonage structurel avec les modèles voisins ;
- cannibalisation avec comparatif/marque/usage résolue ;
- résultats `humanizer`, `general-writing`, `anti-ai-slop` pris en compte ;
- maillage logique ;
- SEO technique cohérent ;
- limites visibles lorsqu'elles changent la décision.

Un JSON valide n'est qu'un plancher : le jugement éditorial reste obligatoire.

## 10. Phase 1 — gouvernance avant migration du renderer

`_generate_model_overrides.py` reste inchangé.

- son squelette actuel ne constitue pas un PASS ;
- aucune page existante n'est considérée conforme parce qu'elle est générée ;
- le workflow peut auditer sans réécrire ;
- la migration vers un body bespoke viendra dans une phase séparée.

## 11. Indexation

Conserver `noindex, follow` par défaut.

Avant indexation :

1. stack shared/custom valide ;
2. run-evidence v2 valide ;
3. `PUBLISH_REVIEW = PASS — READY_FOR_HUMAN_VALIDATION` ;
4. validation humaine explicite ;
5. instruction explicite d'indexer.

Aucun workflow ne retire `noindex` automatiquement.
