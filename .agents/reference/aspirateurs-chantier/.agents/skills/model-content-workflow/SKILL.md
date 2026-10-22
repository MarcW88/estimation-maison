---
name: model-content-workflow
description: Orchestration 80/20 de création et refonte des pages /modeles/ d'aspirateurs-chantier.fr. La méthode éditoriale reste portée par les skills partagés ; le custom est limité aux contraintes métier d'une référence précise et au handoff inter-modèles.
metadata:
  adapted_for: aspirateurs-chantier.fr
  source_workflow: aspirateurs-chantier.fr/brand-content-workflow
  reference_pattern: bloc-notes-numeriques.fr PRODUCT/REVIEW
  orchestration_target: ">=80% shared responsibilities; <=20% custom"
---

# Model Content Workflow — aspirateurs-chantier.fr

## Contrat 80/20

Ce workflow est un orchestrateur, pas un générateur éditorial custom.

- **>=80% shared** : intention, audit, refresh, recherche, fact-check, preuves de jugement, valeur affiliée, brief, rédaction, finition, maillage, SEO et QA.
- **<=20% custom** : identité exacte de la référence, contraintes métier aspirateurs et handoff vers la revue inter-modèles.

Interdit : recréer ici un moteur de fact-check, rédaction, style, maillage, SEO ou QA.

Avant toute production :

```bash
python3 validate_model_skill_stack.py
```

Un FAIL bloque le travail.

## 1. Entrées obligatoires

Lire :

- `model-workflow.config.yaml` ;
- `.content/models/model-evidence.json` ;
- la page cible `/modeles/<slug>/` ;
- les pages modèles sœurs pertinentes ;
- la page marque et les comparatifs/usages/guides adjacents ;
- les données sémantiques/GSC disponibles ;
- les sources actuelles ;
- `.content/models/runs/<slug>.json` s'il existe.

Pour une page existante, commencer par `model-analysis-workflow / AUDIT`.

`model-evidence.json` est un seed factuel Tier 1 : ce n'est ni un plan, ni un verdict, ni une preuve suffisante pour tous les jugements.

## 2. Chaîne shared obligatoire

Exécuter et persister un résumé d'output pour chaque étape :

1. `search-intent`
2. `content-audit`
3. `content-refresh` si UPDATE, sinon `N/A` motivé
4. `fact-check` pré-draft
5. `evidence-based-reviews` si un jugement dépasse une spec, sinon `N/A` motivé
6. `affiliate-value`
7. `content-brief-authoring`
8. `content-and-copy`
9. `fact-check` post-draft
10. `humanizer`
11. `general-writing`
12. `anti-ai-slop`
13. `internal-linking-audit`
14. `seo-technical`
15. `seo-best-practices`
16. `editorial-qa`

`content-recovery-and-production-workflow` reste la couche de récupération générale. Ne pas recopier sa méthode ici.

Une simple mention « skill exécuté » n'est pas une preuve suffisante.

## 3. Rôle d'une page MODEL

Une page `/modeles/` aide à décider sur **une référence précise**.

Elle ne doit pas devenir :

- un comparatif miniature ;
- une page marque raccourcie ;
- un guide générique ;
- une page usage générique ;
- une review hands-on fictive.

Frontières :

- `MODEL` : référence, statut, caractéristiques décisionnelles, compatibilités, limites et fit ;
- `COMPARISON` : choix entre plusieurs références ;
- `BRAND_HUB` : gamme et écosystème ;
- `USAGE` : problème/contexte de travail ;
- `GUIDE` : concept ou méthode.

## 4. Custom — vacuum model domain review

Selon la référence, vérifier :

- référence, suffixe, variante, génération et statut ;
- classe L/M/H documentée ;
- filtre/HEPA vs classe ;
- débit/dépression et contexte de mesure ;
- capacité brute/net/eau ;
- décolmatage ;
- prise outil/Auto-Start ;
- antistatique ;
- eau/poussière ;
- alimentation et plateforme batterie ;
- autonomie si utilisée ;
- flexibles, raccords et consommables ;
- poids, mobilité et encombrement ;
- compatibilités dépendantes de la génération.

Règles absolues :

- ne jamais déduire une classe depuis puissance, filtre ou marketing ;
- ne pas comparer des métriques non comparables sans qualification ;
- ne jamais transformer une donnée constructeur ou un test tiers en observation maison ;
- ne pas attribuer à une variante les specs d'une autre.

Ce contrôle ne remplace pas `fact-check`.

## 5. Recherche avant architecture

Construire un evidence brief avant le plan.

Pour chaque claim/question important :

- source ;
- date si nécessaire ;
- statut `VERIFIED`, `SUPPORTED`, `INFERRED`, `UNKNOWN`, `OUTDATED` ou `CONTRADICTED` ;
- valeur pour la décision.

Hiérarchie : fabricant/documentation officielle → distributeur officiel → retailer fiable si nécessaire → tests indépendants → patterns utilisateurs crédibles.

## 6. Plan bespoke dérivé des preuves

Pour chaque section :

- `question` ;
- `evidence_refs` ;
- `decision_value`.

Supprimer ou fusionner une section qui ne justifie pas ces trois éléments.

Interdictions :

- squelette fixe « specs → pour qui → limites → source » ;
- nombre fixe de H2/H3 ;
- tableau obligatoire ;
- FAQ ou conclusion automatiques ;
- quotas de mots/liens ;
- même ordre pour tous les modèles.

Une GAS 18V-10 L, une GAS 35 M AFC et une Kärcher WD 2 n'ont aucune raison de partager le même raisonnement si leurs décisions diffèrent.

## 7. Valeur originale

`affiliate-value` doit répondre à :

> Si tous les liens affiliés disparaissent, la page aide-t-elle encore mieux à décider qu'une fiche fabricant ?

Valeur possible : conséquence pratique d'une spec, distinction de génération, compatibilité, consommables, compromis mobilité/capacité, limite qui rend une autre référence plus rationnelle, contradiction entre sources, clarification de classe/statut.

Réarranger les puces constructeur n'est pas une valeur originale.

## 8. Evidence-based review

`evidence-based-reviews` devient obligatoire dès qu'une phrase porte un jugement de qualité, fiabilité, ergonomie, performance observée ou expérience.

- Tier 1 : faits constructeur vérifiés
- Tier 2 : synthèse utilisateurs
- Tier 3 : triangulation experte
- Tier 4 : hands-on réel uniquement

Une fiche modèle peut être entièrement documentaire.

## 9. Finition et QA

Après le draft : `fact-check` → `humanizer` → `general-writing` → `anti-ai-slop` → maillage → SEO → `editorial-qa`.

Contrôler en particulier : headings interchangeables, intro qui reformule le H1, blocs « pour qui/limites » clonés, transitions génériques, paragraphes communs, langage de faux test.

## 10. Run-evidence v2

Créer :

`.content/models/runs/<slug>.json`

avec :

- `contract_version: 2`
- `slug`
- `status`
- `shared_steps` pour les 16 étapes
- `custom_steps` : `vacuum-model-domain-review` et `model-analysis-publish-review`
- `reader_decision`
- `value_without_affiliate_links`
- `outline` avec `question`, `evidence_refs`, `decision_value`
- `publish_review`

Validation :

```bash
python3 validate_model_run_evidence.py --slug <slug> --require-run
```

Le générateur ne peut jamais fabriquer ce fichier à la place du workflow éditorial.

## 11. Renderer actuel — phase 1

`_generate_model_overrides.py` reste inchangé pendant cette phase.

- ne pas modifier automatiquement les pages modèles ;
- ne pas prendre son squelette comme méthode éditoriale ;
- ne pas lui permettre d'accorder un statut READY ;
- ne pas faire dériver le plan de ses H2 actuels.

La migration du renderer vers un body bespoke sera une phase séparée.

## 12. Gate final

Appeler `model-analysis-workflow / PUBLISH_REVIEW`.

Résultats exacts :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Même avec PASS, conserver `noindex, follow` jusqu'à validation humaine et instruction explicite d'indexer.
