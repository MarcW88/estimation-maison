---
name: comparison-content-workflow
description: Workflow unique de création et de réécriture des pages /comparatifs/ de bloc-notes-numeriques.fr. Orchestre principalement des skills GitHub externes pour l'intention, l'audit, la preuve, le brief, la rédaction, l'on-page et l'édition. La logique custom est limitée à la décision comparative et au contrôle du cluster.
metadata:
  adapted_for: bloc-notes-numeriques.fr
  orchestration_target: ">=80% existing GitHub skills"
  custom_scope: "orchestration + comparison decision logic"
---

# Comparison Content Workflow

## Rôle

C'est le **seul workflow de production** à utiliser pour créer ou réécrire une URL `/comparatifs/`.

Comme le `brand-content-workflow`, il doit orchestrer des skills spécialisés plutôt que fabriquer une méthode maison parallèle.

Principe central :

> **Intention → preuves → décision → brief → rédaction → review.**

Un comparatif peut être excellent sans score numérique. Un score, une pondération, un tableau ou un Total Solution Cost ne sont utilisés que s'ils rendent la décision plus claire.

---

# 1. Entrées

Pour une page existante, lire d'abord le rapport le plus récent du `comparison-analysis-workflow / AUDIT` et le traiter comme le handoff de départ.

Lire également selon pertinence :

- page actuelle ;
- comparatifs voisins ;
- `comparison-workflow.config.yaml` ;
- données `.content/comparisons/` existantes ;
- GSC / sémantique / historique ;
- pages marques, usages et guides utiles ;
- sources actuelles nécessaires.

Ne pas refaire un audit complet si un rapport récent existe, sauf si les données ou la gamme ont changé de façon significative.

---

# 2. Chaîne principale de production — skills existants

## 2.1 `seo-keyword` — Rampstack

Confirmer :

- target query / cluster ;
- intent dominant ;
- format accepté dans la SERP ;
- rôle unique de l'URL ;
- risque de chevauchement avec un autre comparatif.

Le SERP et les données disponibles priment sur une intuition de template.

## 2.2 `jobs-to-be-done` — Wondel.ai, lorsque pertinent

Pour les pages liées à un contexte réel (`étudiant`, `professionnel`, PDF, mobilité, etc.), traduire le besoin en contraintes et critères de décision.

Ne pas inventer de motivations utilisateur non documentées.

## 2.3 `seo-content-audit` — Rampstack

Pour une page existante : préserver ce qui fonctionne. Le workflow ne réécrit pas un bon passage uniquement pour créer de la nouveauté.

Si l'audit a conclu `LIGHT_UPDATE`, respecter ce niveau de changement sauf découverte factuelle majeure.

## 2.4 `evidence-based-reviews` — Rampstack

Construire la base de preuve de la recommandation :

- specs officielles ;
- synthèse propriétaires/utilisateurs lorsque nécessaire ;
- tests indépendants nommés lorsque le jugement le nécessite ;
- hands-on uniquement lorsqu'il existe réellement.

Ne pas sur-documenter des faits simples. Concentrer les preuves fortes sur les éléments qui changent le choix.

## 2.5 `fact-check`

Vérifier les claims importants et les données susceptibles d'évoluer : génération, fonctions, compatibilités, prix, abonnement, disponibilité et comparaison factuelle.

Une appréciation éditoriale reste une appréciation éditoriale ; ne pas la déguiser en mesure.

## 2.6 `affiliate-value`

Avant la rédaction, identifier la valeur originale :

- différences réellement décisionnelles ;
- limites ;
- cas où un produit n'est pas le bon choix ;
- alternatives ;
- coûts ou contraintes cachés réellement pertinents ;
- information difficile à obtenir depuis une seule fiche fabricant.

La page doit rester utile si tous les liens affiliés disparaissent.

## 2.7 `content-brief-authoring` — Rampstack

Construire le brief **avant** le draft.

Le brief doit au minimum préciser :

- query/cluster ;
- décision du lecteur ;
- scope de la comparaison ;
- principaux critères ;
- faits/preuves obligatoires ;
- arbitrages importants ;
- angle éditorial ;
- anti-patterns ;
- outline proposé et rôle de chaque section.

Le plan est spécifique à l'URL. Le workflow n'impose aucun squelette de comparatif.

## 2.8 `content-and-copy` — Rampstack

Rédiger depuis le brief et les preuves.

Priorités :

1. décision claire ;
2. substance ;
3. trade-offs ;
4. structure adaptée ;
5. voix éditoriale naturelle.

Ne pas produire six fiches produits mécaniquement symétriques si la décision peut être mieux expliquée autrement.

---

# 3. Couche custom minimale — décision comparative

Cette couche existe uniquement parce qu'un comparatif doit recommander ou arbitrer entre plusieurs options.

## 3.1 Scope / candidats

Identifier un ensemble **raisonnable** de choix plausibles pour la requête.

Il n'est pas nécessaire de documenter tout le marché. En revanche :

- ne pas omettre silencieusement un candidat évident susceptible de changer la conclusion ;
- expliquer les exclusions majeures lorsque cela aide le lecteur ;
- ne jamais inclure un produit uniquement parce qu'il est monétisable.

## 3.2 Critères

Définir les critères avant la recommandation. Ils viennent de l'intention, du JTBD et des différences réelles entre produits.

Aucune obligation de pondération numérique.

## 3.3 Verdict

Le verdict doit être traçable aux critères et aux preuves.

Favoriser une formulation utile :

- « meilleur choix général pour X » ;
- « choisissez Y si votre priorité est… » ;
- « évitez Z si… » ;
- ou verdict conditionnel dans un head-to-head.

Un gagnant absolu n'est pas obligatoire.

## 3.4 Scoring — optionnel

N'utiliser un score que s'il rend les arbitrages plus compréhensibles.

S'il est utilisé :

- l'échelle doit être stable ;
- les critères doivent être explicités ;
- les notes sont clairement des jugements éditoriaux sauf mesure réelle ;
- éviter les décimales qui simulent une précision inexistante ;
- le classement doit rester intelligible sans le score.

Ne pas inventer des notes pour remplir un JSON.

## 3.5 Coût — proportionné

Pour `pas cher`, `sans abonnement` ou une intention fortement budgétaire, comparer la configuration réellement nécessaire.

Pour une page où le prix est secondaire, un repère de prix/configuration suffit. Ne pas imposer un modèle de coût complexe si cela ne change pas la décision.

---

# 4. Architecture éditoriale

Aucun template par type de comparatif.

Interdit d'imposer :

- nombre fixe de H2/H3 ;
- `méthode → critères → ranking → produit 1 → produit 2 → FAQ → conclusion` ;
- même longueur par produit ;
- tableau obligatoire ;
- FAQ obligatoire ;
- conclusion obligatoire ;
- quotas de mots ou de liens.

Chaque section doit justifier sa présence par une question, une décision, une preuve ou un arbitrage propre à cette URL.

Deux pages comparatives proches doivent pouvoir avoir des structures radicalement différentes si leurs décisions diffèrent.

---

# 5. Post-draft — skills spécialisés

## 5.1 `fact-check`

Réextraire les claims et corriger les faits, comparatifs, prix, générations et disponibilités.

## 5.2 `humanizer`

Modifier structure et prose lorsque le texte paraît générique, répétitif ou trop lisse. Préserver les faits.

## 5.3 `general-writing` — msimchowitz/writing-skills

Passage final de clarté, précision et voix. Éditer le minimum nécessaire plutôt que tout réécrire.

## 5.4 `anti-ai-slop`

Vérifier notamment :

- blocs produits interchangeables ;
- transitions répétées ;
- « avantages / limites / pour qui » cloné ;
- conclusion qui répète le classement ;
- structure identique à un autre comparatif ;
- généralités applicables à n'importe quelle tablette E Ink.

## 5.5 `seo-onpage` — Rampstack

Title, meta, H1, headings, contenu, liens internes, URL et schema honnête.

## 5.6 `seo-technical`

Uniquement pour les points techniques réellement applicables : canonical, robots, crawlabilité, structured data et intégrité HTML.

## 5.7 `editorial-qa`

Dernière QA générique : intention, valeur, factualité, naturel et utilité sans affiliation.

---

# 6. Persistance

`.content/comparisons/<slug>.json` est un support méthodologique, **pas un formulaire obligatoire**.

Conserver seulement les champs réellement utilisés, par exemple :

- intent/JTBD ;
- scope/candidats ;
- exclusions importantes ;
- criteria ;
- evidence / sources ;
- recommendation logic ;
- price/configuration notes ;
- scores/weights **si utilisés** ;
- ranking **si la page utilise un ranking** ;
- date de recherche ;
- status.

Ne jamais ajouter un champ méthodologique uniquement pour satisfaire le workflow.

---

# 7. Gate final

Une fois le draft stable, appeler :

`.agents/skills/comparison-analysis-workflow/SKILL.md` en mode `PUBLISH_REVIEW`.

Résultat requis avant validation humaine :

`PASS — READY_FOR_HUMAN_VALIDATION`

Sinon :

`FAIL — KEEP_NOINDEX`

Le gate final vérifie surtout : intention, décision, preuves, valeur, différenciation éditoriale, SEO et absence de faux hands-on — pas la présence d'une méthodologie chiffrée imposée.

---

# 8. Indexation

Conserver `noindex,follow` par défaut.

Le workflow ne retire jamais `noindex` automatiquement.

Indexation seulement après validation machine, PUBLISH_REVIEW PASS, validation humaine explicite et instruction explicite d'indexer.

---

# 9. Orchestration 80/20

```text
PAGE EXISTANTE
  comparison-analysis-workflow / AUDIT
        ↓
seo-keyword (Rampstack)
        ↓
jobs-to-be-done (Wondel.ai) si pertinent
        ↓
seo-content-audit (Rampstack)
        ↓
evidence-based-reviews (Rampstack) + fact-check
        ↓
affiliate-value
        ↓
CUSTOM LÉGER : scope + critères + logique de recommandation
        ↓
content-brief-authoring (Rampstack)
        ↓
content-and-copy (Rampstack)
        ↓
fact-check
        ↓
humanizer → general-writing → anti-ai-slop
        ↓
seo-onpage (Rampstack) + seo-technical
        ↓
editorial-qa
        ↓
comparison-analysis-workflow / PUBLISH_REVIEW
        ↓
validation humaine
```

Le custom doit rester minoritaire et ne jamais réimplémenter les skills externes.