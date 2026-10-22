---
name: comparison-analysis-workflow
description: Workflow unique d'analyse des pages /comparatifs/ d'aspirateurs-chantier.fr. Clone/adaptation du workflow bloc-notes-numerique, orchestrant majoritairement des skills GitHub existants, avec custom limité aux contrôles propres aux comparaisons d'aspirateurs de chantier. Décisions: KEEP, LIGHT_UPDATE, DEEP_REWRITE, MERGE ou NOINDEX.
metadata:
  adapted_for: aspirateurs-chantier.fr
  source_workflow: MarcW88/bloc-notes-numerique/comparison-analysis-workflow
  orchestration_target: ">=80% existing/vendored skills"
  custom_scope: "orchestration + vacuum comparison sanity + cluster boundaries only"
---

# Comparison Analysis Workflow — Aspirateurs Chantier

## Rôle

C'est le **seul workflow d'analyse** à utiliser pour `/comparatifs/`.

Il reste un orchestrateur. Les méthodologies génériques vivent dans les skills partagés importés depuis `bloc-notes-numerique` et leurs upstreams. La couche custom couvre uniquement ce qui est réellement propre à la décision sur un aspirateur de chantier.

Principe :

> **Évaluer la qualité de la décision offerte au lecteur, pas la sophistication apparente de la méthodologie.**

## Gouvernance 80/20

Le workflow doit conserver **>=80 % de responsabilités shared et <=20 % custom**.

Le custom est limité à :

1. périmètre comparatif aspirateurs ;
2. sécurité/comparabilité des claims métier ;
3. frontières du cluster ;
4. décision finale KEEP/LIGHT/DEEP/MERGE/NOINDEX et PUBLISH_REVIEW.

Il ne doit jamais réimplémenter `seo-keyword`, `seo-content-audit`, `evidence-based-reviews`, `fact-check`, `affiliate-value`, `anti-ai-slop`, `seo-onpage`, `internal-linking-audit` ou `editorial-qa`.

---

# 1. Modes

## `AUDIT`
Analyse une URL existante et produit un diagnostic + décision, sans réécriture.

## `CLUSTER_AUDIT`
Compare les URLs `/comparatifs/` pour détecter :

- chevauchement d'intention ;
- recommandations recyclées ;
- mêmes produits et arguments sous plusieurs promesses ;
- architectures fonctionnellement clonées ;
- profondeur insuffisante ;
- preuves trop faibles ;
- manque de valeur originale.

## `PUBLISH_REVIEW`
Gate final :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Un PASS doit être persisté dans `.content/comparisons/runs/<slug>.json`. Le générateur ne peut pas accorder ce statut.

---

# 2. Entrées

Lire selon disponibilité :

- page cible ;
- comparatifs voisins ;
- `comparison-workflow.config.yaml` ;
- `.content/comparisons/<slug>.json` ;
- `.content/comparisons/runs/<slug>.json` si existant ;
- GSC / sémantique / historique ;
- SERP actuelle si l'intention est incertaine ou mouvante ;
- `/usages/`, `/marques/`, `/modeles/`, `/guides/` ;
- `.content/models/model-evidence.json` ;
- sources actuelles.

L'absence de données doit être signalée, jamais compensée par une précision inventée.

---

# 3. Chaîne principale — skills partagés obligatoires

## `seo-content-audit`
Décider quoi conserver, mettre à jour ou consolider. Examiner la cannibalisation sans réécrire par réflexe.

## `seo-keyword`
Confirmer requête/cluster, intention dominante, SERP, rôle de l'URL et différences avec les comparatifs proches.

## `jobs-to-be-done`
Utiliser lorsque le contexte change réellement la décision. Un `N/A` doit être justifié dans le run-evidence.

## `evidence-based-reviews`
Distinguer specs officielles, synthèse d'expérience, preuves expertes et hands-on réel. Une fiche constructeur soutient un fait, pas une sensation d'usage inventée.

## `fact-check`
Vérifier modèles/générations, classe de poussière, fonctions, compatibilités, mesures, disponibilité et prix lorsqu'utilisés.

## `affiliate-value`
Vérifier que la page reste utile sans lien affilié : arbitrages, limites, incompatibilités, alternatives et conséquences pratiques.

## `seo-onpage`
Title, meta, H1, structure, contenu, liens, canonical, URL et schema honnête. Aucun quota de mots/H2/liens.

## `internal-linking-audit`
Vérifier les handoffs vers guides, usages, marques et modèles.

## `anti-ai-slop`
Détecter non seulement des H2 identiques, mais aussi :

- même fonction éditoriale dans le même ordre ;
- answer box systématique ;
- module de décision systématique ;
- tableau systématique ;
- cadence `repères → tableau → limites → sources` recyclée ;
- blocs produits mécaniquement symétriques ;
- transitions et verdicts substituables entre URLs.

## `editorial-qa`
QA finale sur intention, valeur originale, factualité, naturel, SEO et utilité réelle.

---

# 4. Couche custom minimale — sanity check Aspirateurs Chantier

## A. Périmètre crédible
Produits réellement plausibles ; candidats évidents considérés ou exclusion expliquée ; pas d'inclusion guidée par la monétisation ; pas de catalogue exhaustif sans valeur.

## B. Critères avant recommandation
Selon la page : classe L/M/H, type de poussière, maintien du débit, décolmatage, raccord outil, antistatique, mobilité, volume, alimentation, plateforme batterie, consommables, eau/poussière, coût de configuration.

## C. Sécurité et comparabilité honnête
1. Classe appareil ≠ filtre.
2. Puissance ≠ classe de sécurité.
3. Débit/dépression : contexte de mesure obligatoire.
4. Décolmatage ≠ certification.
5. Wet/dry ≠ aptitude aux poussières dangereuses.
6. Compatibilité batterie vérifiée au niveau plateforme.
7. Cuve brute/net/eau distinguée si nécessaire.

## D. Verdict traçable
La page doit expliquer pourquoi un choix est recommandé, quand un autre devient meilleur et quelle limite peut inverser la décision.

## E. Scoring/coût proportionnés
Optionnels ; jamais imposés pour donner l'apparence d'une méthodologie.

---

# 5. CLUSTER_AUDIT — standard renforcé

Le cluster audit ne peut plus conclure PASS uniquement parce que les signatures H2 diffèrent.

Il doit comparer au minimum :

- intention et rôle de chaque URL ;
- overlap de candidats ;
- overlap d'arguments ;
- fonction réelle de chaque section ;
- profondeur de l'analyse ;
- qualité/diversité des preuves ;
- présence de preuves indépendantes lorsqu'un jugement le nécessite ;
- valeur originale par URL ;
- utilité si les liens affiliés disparaissent ;
- existence ou non d'un run-evidence v2 ;
- similarité de cadence éditoriale au niveau cluster.

Partager CSS, composants ou tableaux n'est pas un problème. Partager la même pensée éditoriale l'est.

---

# 6. Décisions

## `KEEP`
Page distincte, actuelle, utile et convaincante, avec run-evidence valide si elle prétend être prête.

## `LIGHT_UPDATE`
Corrections locales : faits, sources, sélection secondaire, formulation, maillage ou quelques arbitrages. Ne pas gonfler artificiellement la page.

## `DEEP_REWRITE`
Problème structurel : rôle/intention mal cadré, sélection inadéquate, recommandation non justifiable, faible valeur affiliée, architecture industrialisée, profondeur insuffisante, obsolescence substantielle ou preuves trop faibles.

## `MERGE`
Une autre URL sert essentiellement la même décision.

## `NOINDEX`
Valeur ou justification insuffisante. Aucune suppression/redirection automatique.

Pour chaque décision fournir : confiance, valeur à préserver, blockers, améliorations secondaires, données manquantes et prochaine étape.

---

# 7. PUBLISH_REVIEW

1. exécuter `python3 _validate_comparatifs.py` ;
2. exécuter `python3 validate_comparison_run_evidence.py --slug <slug> --require-run` ;
3. rejouer les skills pertinents ;
4. comparer la fonction des sections aux pages sœurs ;
5. vérifier verdict, preuves, limites et faux hands-on ;
6. vérifier title/H1/canonical/robots/schema ;
7. vérifier utilité sans affiliation ;
8. vérifier gates métier ;
9. enregistrer le résultat dans le run-evidence.

PASS : `PASS — READY_FOR_HUMAN_VALIDATION`

FAIL : `FAIL — KEEP_NOINDEX`

`enforce_comparison_review_state.py` est ensuite la seule couche autorisée à refléter ce PASS dans le ledger.

---

# 8. Indexation

Conserver `noindex, follow` par défaut. Indexation uniquement après validateur machine sans blocker, run-evidence v2 valide, PUBLISH_REVIEW PASS, validation humaine explicite et instruction explicite d'indexer.

---

# 9. Gouvernance finale

La méthode vient majoritairement des skills partagés/vendored. Le custom de ce workflow se limite aux contrôles propres aux aspirateurs de chantier et à la décision de cluster. Aucun nouveau skill custom ne doit être ajouté pour compenser un mauvais output d'un skill partagé : il faut mieux exécuter le skill partagé concerné.