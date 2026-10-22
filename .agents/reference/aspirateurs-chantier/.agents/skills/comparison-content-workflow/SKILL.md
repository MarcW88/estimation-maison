---
name: comparison-content-workflow
description: Workflow unique de création et de réécriture des pages /comparatifs/ d'aspirateurs-chantier.fr. Clone/adaptation du workflow de bloc-notes-numerique, orchestrant majoritairement des skills GitHub existants. La logique custom reste limitée à la décision comparative et aux contraintes propres aux aspirateurs de chantier.
metadata:
  adapted_for: aspirateurs-chantier.fr
  source_workflow: MarcW88/bloc-notes-numerique/comparison-content-workflow
  orchestration_target: ">=80% existing/vendored skills"
  custom_scope: "orchestration + vacuum comparison decision logic only"
---

# Comparison Content Workflow — Aspirateurs Chantier

## Rôle

C'est le **seul workflow de production** à utiliser pour créer ou réécrire une URL `/comparatifs/`.

Il est cloné/adapté depuis `MarcW88/bloc-notes-numerique` et doit rester un orchestrateur. Il ne doit jamais devenir une méthodologie custom parallèle.

Principe central :

> **Intention → preuves → décision → brief → rédaction → review.**

Scoring, pondération, tableau, hard gate formel ou coût total détaillé sont optionnels. Ils ne sont utilisés que s'ils rendent la décision plus claire.

## Gouvernance 80/20 non négociable

La méthode doit rester à **>=80 % shared / <=20 % custom**.

Les responsabilités génériques appartiennent aux skills importés/vendored depuis `bloc-notes-numerique` et leurs upstreams. Le custom Aspirateurs Chantier est limité à :

1. scope/candidats/critères spécifiques à la décision sur un aspirateur ;
2. sécurité et comparabilité des claims métier ;
3. cohérence du cluster et gate final.

Interdit de recréer un `fact-check-aspirateurs`, un `humanizer-aspirateurs`, un moteur de brief custom ou un moteur de rédaction custom pour contourner les skills partagés.

---

# 1. Entrées

Pour une page existante, lire d'abord le rapport récent du `comparison-analysis-workflow / AUDIT` et respecter son niveau de changement.

Lire selon pertinence :

- page cible et comparatifs voisins ;
- `comparison-workflow.config.yaml` ;
- `.content/comparisons/<slug>.json` ;
- GSC / analyse sémantique / historique ;
- SERP actuelle ;
- `/usages/`, `/marques/`, `/modeles/`, `/guides/` ;
- `.content/models/model-evidence.json` ;
- sources actuelles fabricants, manuels et sources secondaires utiles.

Ne pas refaire un audit complet si un handoff récent existe, sauf changement significatif de gamme, SERP ou données.

---

# 2. Chaîne principale — skills partagés obligatoires

## `seo-keyword`
Confirmer query/cluster, intention, format SERP, rôle unique de l'URL et risque de chevauchement.

## `jobs-to-be-done`
Utiliser lorsque le contexte change réellement la décision : professionnel, mobilité, petit format, budget, usage outil, etc. Si non pertinent, le run peut enregistrer `N/A` avec justification.

## `seo-content-audit`
Préserver ce qui fonctionne. Un `LIGHT_UPDATE` ne devient pas un deep rewrite sans découverte majeure documentée.

## `evidence-based-reviews`
Construire la base de preuve : specs officielles, expérience utilisateurs si nécessaire, tests indépendants nommés lorsque le jugement l'exige, hands-on seulement s'il existe réellement.

## `fact-check` — pré-draft
Vérifier classe, génération, fonctions, compatibilités, débit/dépression, capacité, poids, prix/disponibilité lorsqu'ils sont utilisés.

## `affiliate-value`
Identifier la valeur originale : différences décisionnelles, limites, cas d'inadéquation, alternatives, coûts ou contraintes cachés pertinents. La page doit rester utile sans affiliation.

## `content-brief-authoring`
Construire le brief **avant** le draft : query, décision, scope, critères, preuves, arbitrages, angle, anti-patterns et outline spécifique.

## `content-and-copy`
Rédiger depuis le brief et les preuves : décision claire, substance, trade-offs, structure adaptée et voix naturelle.

Le générateur Python ne remplace aucune de ces étapes.

---

# 3. Couche custom minimale — décision Aspirateurs Chantier

## 3.1 Scope / candidats
Identifier un ensemble raisonnable de produits réellement plausibles. Ne pas documenter tout le marché par principe ; ne pas omettre silencieusement un candidat évident susceptible de changer la conclusion.

## 3.2 Critères
Définir les critères **avant** la recommandation. Selon l'intention : classe L/M/H, maintien du débit, débit/dépression contextualisés, prise/raccord outil, antistatique, capacité, mobilité, plateforme batterie, consommables, eau/poussière, coût de configuration.

## 3.3 Gates métier non négociables
- classe L/M/H jamais déduite depuis HEPA, puissance ou débit ;
- AFC/Tact/InfiniClean/AUTOCLEAN ≠ certification ;
- mesures de débit/dépression non équivalentes sans contexte de mesure ;
- capacité brute/net/eau distinguée lorsque nécessaire ;
- compatibilité batterie vérifiée au niveau de la plateforme ;
- wet/dry ≠ aptitude aux poussières dangereuses ;
- autonomie ou sensation d'usage uniquement avec preuve appropriée.

## 3.4 Verdict
Le verdict doit être traçable aux critères et preuves. Un verdict conditionnel est préférable à un faux gagnant universel.

## 3.5 Scoring et coût
Optionnels et proportionnés. Pas de fausse précision ni de modèle de coût forcé.

---

# 4. Architecture éditoriale

Aucun template obligatoire par type de comparatif.

Interdit d'imposer :
- nombre fixe de H2/H3 ;
- nombre fixe de mots ou liens ;
- `answer box → repères de décision → tableau → quelques H2 → sources` comme cadence par défaut ;
- `méthode → critères → ranking → produit 1 → produit 2 → FAQ → conclusion` ;
- même longueur par produit ;
- tableau, module de décision, FAQ ou conclusion obligatoires ;
- sections symétriques « avantages / limites / pour qui » pour chaque machine.

Le composant `comparison-decision-module` est **optionnel**. Il n'est utilisé que s'il clarifie réellement la décision.

Chaque section doit justifier sa présence par une question, décision, preuve ou arbitrage propre à l'URL.

---

# 5. Post-draft — skills partagés

1. `fact-check` — réextraire et corriger les claims.
2. `humanizer` — corriger structure/prose trop générique sans altérer les faits.
3. `general-writing` — clarté, précision, voix ; éditer le minimum nécessaire.
4. `anti-ai-slop` — détecter blocs interchangeables, transitions recyclées, symétries mécaniques et structure fonctionnellement clonée.
5. `seo-onpage` — title, meta, H1, headings, contenu, liens et schema honnête.
6. `seo-technical` — canonical, robots, crawlabilité, structured data et intégrité HTML.
7. `internal-linking-audit` — router vers guides/usages/marques/modèles utiles.
8. `editorial-qa` — gate générique final.

---

# 6. Persistance méthodologique

`.content/comparisons/<slug>.json` reste un support méthodologique, pas un formulaire obligatoire.

Conserver uniquement les champs réellement utiles : intention/JTBD, scope/candidats, exclusions, critères, preuves, recommendation logic, comparabilité, prix/configuration, scores si utilisés, research date et statut.

## Run evidence v2

Après un **vrai** passage du workflow, persister :

`.content/comparisons/runs/<slug>.json`

Ce fichier doit documenter :

- la décision du lecteur ;
- le scope comparatif ;
- la valeur sans affiliation ;
- les candidats considérés et exclusions majeures ;
- l'outline dérivé des preuves ;
- les outputs des 16 étapes shared ;
- les 2 contrôles custom ;
- le `PUBLISH_REVIEW` final.

Le générateur Python **n'a pas le droit de fabriquer son propre run-evidence**.

Sans run v2 valide, la page doit rester `REQUIRES_WORKFLOW_RERUN`.

---

# 7. Rôle du générateur

Les scripts Python peuvent :

- produire/maintenir le shell HTML ;
- injecter les composants visuels ;
- matérialiser un contenu éditorial déjà produit par le workflow ;
- normaliser les assets ;
- appliquer robots/canonical ;
- vérifier l'idempotence.

Ils ne peuvent pas, à eux seuls :

- déclarer qu'une recherche a été faite ;
- choisir la structure éditoriale finale à partir d'un template ;
- produire le brief au nom de `content-brief-authoring` ;
- créer des preuves au nom d'`evidence-based-reviews` ;
- simuler `humanizer`, `anti-ai-slop` ou `editorial-qa` ;
- accorder `READY_FOR_HUMAN_VALIDATION`.

---

# 8. Frontières éditoriales du cluster

- `/modeles/` = référence précise ;
- `/marques/` = gamme/écosystème ;
- `/usages/` = besoin/tâche ;
- `/guides/` = critère technique ;
- `/comparatifs/` = arbitrage entre options pour une décision donnée.

Le même modèle peut apparaître dans plusieurs comparatifs si la logique de décision change réellement. Réutiliser les mêmes arguments, la même cadence ou le même verdict sous une autre requête est un blocker.

---

# 9. Gate final

Une fois le draft stable :

1. persister le run-evidence v2 ;
2. exécuter `validate_comparison_run_evidence.py --slug <slug> --require-run` ;
3. appeler `comparison-analysis-workflow` en `PUBLISH_REVIEW` ;
4. enregistrer `PASS — READY_FOR_HUMAN_VALIDATION` dans le run ;
5. laisser `enforce_comparison_review_state.py` dériver l'état du ledger.

Le générateur ne peut pas accorder le PASS.

---

# 10. Indexation

Conserver `noindex, follow` par défaut. Indexation seulement après validation machine, run v2 valide, PUBLISH_REVIEW PASS, validation humaine explicite et instruction explicite d'indexer.

---

# 11. Orchestration 80/20

```text
PAGE EXISTANTE
  comparison-analysis-workflow / AUDIT
        ↓
seo-keyword
        ↓
jobs-to-be-done si pertinent
        ↓
seo-content-audit
        ↓
evidence-based-reviews + fact-check
        ↓
affiliate-value
        ↓
CUSTOM LÉGER : scope + critères + gates métier + logique de recommandation
        ↓
content-brief-authoring
        ↓
content-and-copy
        ↓
fact-check
        ↓
humanizer → general-writing → anti-ai-slop
        ↓
seo-onpage + seo-technical + internal-linking-audit
        ↓
editorial-qa
        ↓
persist run-evidence v2
        ↓
comparison-analysis-workflow / PUBLISH_REVIEW
        ↓
validation humaine
```

Le custom doit rester minoritaire et ne jamais réimplémenter les skills partagés.