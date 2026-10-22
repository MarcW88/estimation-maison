---
name: guide-analysis-workflow
description: Workflow unique d'analyse des pages /guides/ d'aspirateurs-chantier.fr. Adapté de MarcW88/bloc-notes-numerique. Audite une URL ou le cluster, contrôle intention, rôle pédagogique, frontières avec usages/comparatifs/marques, preuves, fraîcheur, sécurité des claims aspirateurs, valeur affiliée, similarité structurelle et SEO, puis décide KEEP, LIGHT_UPDATE, DEEP_REWRITE, MERGE ou NOINDEX. En PUBLISH_REVIEW, sert de gate final avant validation humaine.
metadata:
  source_repo: MarcW88/bloc-notes-numerique
  source_skill: .agents/skills/guide-analysis-workflow/SKILL.md
  source_sha: 02476e597d6f3e878d43d641606fe936921d1c47
  adapted_for: aspirateurs-chantier.fr
  orchestration_target: ">=80% existing skills"
  custom_scope: "guide routing + vacuum-domain integrity + category boundaries + publish gate"
---

# Guide Analysis Workflow — aspirateurs-chantier.fr

## Rôle

C'est le **seul workflow d'analyse** à utiliser pour les URLs sous `/guides/`.

Il ne rédige pas la page. Il orchestre d'abord les skills partagés déjà présents dans le dépôt et limite la couche custom aux contrôles qui sont réellement propres aux aspirateurs de chantier.

Séparation stricte :

- `guide-analysis-workflow` = diagnostiquer, comparer le cluster, décider et effectuer le publish review ;
- `guide-content-workflow` = produire ou corriger lorsqu'une décision d'analyse le demande ;
- `/usages/` = expliquer comment un job réel modifie le système d'aspiration à prévoir ;
- `/comparatifs/` = choisir entre produits ou familles de produits ;
- `/marques/` = documenter marque, gamme ou écosystème ;
- `/guides/` = comprendre un critère, un risque, une technologie, un arbitrage ou une procédure autonome.

Un guide peut soutenir une décision d'achat sans devenir un classement produit.

---

# 1. Modes

## `AUDIT`

Mode par défaut pour une URL existante. Retourne une décision et un plan de correction **sans réécrire la page**.

Comparer la cible aux guides voisins et aux pages usages/comparatifs/marques proches lorsque le risque de chevauchement existe.

## `CLUSTER_AUDIT`

Analyse le cluster `/guides/` pour détecter :

- intentions ou sous-questions qui se chevauchent ;
- guides qui devraient être fusionnés ;
- sous-questions qui appartiennent plutôt à `/usages/`, `/comparatifs/` ou `/marques/` ;
- couverture fragmentée d'un même sujet ;
- trous utiles dans le parcours ;
- architectures éditoriales industrialisées ;
- répétitions de conclusions, tableaux, procédures ou CTA sans justification ;
- contradictions techniques entre guides.

Aucune réécriture, fusion ou redirection automatique.

## `PUBLISH_REVIEW`

Gate final après correction ou production via `guide-content-workflow`.

Retourner exactement :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Un PASS n'autorise jamais à retirer `noindex, follow`, à merger ou à indexer sans validation humaine et instruction explicite.

---

# 2. Entrées

Lire selon disponibilité :

- `AGENTS.md` et `DESIGN.md` si le rendu est concerné ;
- `guide-workflow.config.yaml` ;
- `.agents/skills/guide-skill-stack.json` ;
- la page cible ;
- `.content/guides/<slug>.json` si présent ;
- `.content/briefs/<slug>.md` et `.content/reviews/<slug>.md` s'ils existent ;
- les guides voisins ;
- les pages usages, comparatifs ou marques qui couvrent des sous-questions proches ;
- les données sémantiques, GSC, logs ou historiques disponibles ;
- la SERP actuelle lorsque l'intention est incertaine ;
- les sources actuelles pour les faits instables.

Ne jamais combler une donnée absente avec la mémoire du modèle. Une inconnue qui peut changer la décision reste `UNKNOWN`.

---

# 3. Chaîne de skills partagés obligatoire

Exécuter les skills existants avant les contrôles custom. Ne pas recopier leurs checklists dans ce workflow.

## Audit, intention et périmètre

- `seo-content-audit` : KEEP / UPDATE / MERGE / REDIRECT / DELETE comme diagnostic amont ; les actions destructives restent des recommandations ;
- `seo-keyword` : requête/topic, intention, clustering et proximité avec d'autres URLs quand les données le permettent ;
- `search-intent` : tâche exacte, maturité, sous-questions, forme attendue de la réponse ;
- `content-refresh` : uniquement si une mise à jour est nécessaire.

## Preuves et valeur

- `fact-check` : claims vérifiables ;
- `evidence-based-reviews` : seulement si un jugement expérientiel dépasse ce que les specs/documentations permettent d'établir ;
- `affiliate-value` : la page doit rester utile sans lien affilié.

## Maillage, style et SEO

- `internal-linking-audit` ;
- `anti-ai-slop` ;
- `seo-onpage` ;
- `seo-technical` ;
- `seo-best-practices` lorsque pertinent ;
- `seo-drift` seulement avec baseline exploitable ;
- `editorial-qa` en dernière QA générique.

La provenance et le ratio 80/20 sont contrôlés par `.agents/skills/guide-skill-stack.json`.

---

# 4. Couche custom n°1 — quel travail ce guide doit-il accomplir ?

Le type dominant sert de **grille de risque**, jamais de template.

- `CHOICE` : aider à arbitrer entre options, contraintes ou approches sans ranking produit ;
- `EXPLAINER` : rendre compréhensible un mécanisme, une unité, une classe ou une technologie ;
- `HOW_TO` : permettre d'accomplir une tâche ou une procédure vérifiable ;
- `HYBRID` : uniquement lorsqu'une page combine réellement plusieurs fonctions.

### CHOICE

Vérifier surtout : décision exacte, critères qui changent la décision, critères éliminatoires, compromis, situations où chaque option devient inadaptée et absence de podium produit déguisé.

### EXPLAINER

Vérifier surtout : concept et termes voisins, mécanisme sans fausse causalité, conséquence pratique, limites/exceptions et absence de pseudo-précision.

### HOW_TO

Vérifier surtout : prérequis, ordre des étapes lorsqu'il compte réellement, variantes machine/accessoire, résultat attendu, moyen de vérification, échecs probables et alternatives. Aucune étape ne peut être inventée parce qu'elle paraît logique.

---

# 5. Couche custom n°2 — frontières éditoriales

## Guide vs Usage

Un guide traite une **sous-question autonome** : classe L/M/H, décolmatage, débit, dépression, cuve, HEPA, sac, entretien, prise asservie, etc.

Une page Usage traite le **job complet** : ponçage, plâtre, sciure, gravats, scie, atelier, rénovation.

## Guide vs Comparatif

Un guide peut expliquer les critères et arbitrages. Dès qu'il faut sélectionner, scorer, classer ou recommander des modèles entre eux, le workflow Comparatif possède la décision.

## Guide vs Marque

Un guide peut citer plusieurs constructeurs pour illustrer une différence. Si la question porte principalement sur la gamme, le système ou une fonction propriétaire d'une marque, la page Marque doit posséder ce rôle.

### Test pratique

Si deux URLs peuvent garder le même H1, la même réponse centrale et le même bloc décisionnel en changeant seulement quelques termes, leur séparation est probablement insuffisante.

---

# 6. Couche custom n°3 — intégrité technique aspirateurs

Ces règles ne remplacent pas `fact-check`. Elles interdisent les erreurs métier qui peuvent rendre un guide trompeur.

- Ne jamais déduire une classe L/M/H depuis HEPA, puissance, débit, dépression ou décolmatage.
- Une classe de filtre ne transforme pas automatiquement la certification de la machine complète.
- `HEPA`, `H13/H14`, `classe H` et `classe M` ne sont pas des synonymes.
- `wet/dry` ne signifie pas aptitude aux poussières dangereuses.
- ACD ne doit pas être présenté comme équivalent à ATEX/Zone 22.
- Débit et dépression ne mesurent pas la même chose ; une comparaison cross-brand exige un contexte de mesure suffisamment homogène.
- Ne pas convertir kPa, mbar, mmH2O ou Air Watts en promesse de performance réelle sans expliquer ce que la métrique permet — et ne permet pas — de conclure.
- Capacité brute, nette, poussière et eau doivent être distinguées lorsqu'elles influencent le conseil.
- Puissance électrique moteur ≠ puissance d'aspiration.
- Décolmatage manuel, semi-automatique et automatique doivent être distingués selon les termes/documentations réellement disponibles.
- Prise asservie, démarrage sans fil/Bluetooth et Wireless Tool Control ne sont pas interchangeables ; vérifier au niveau modèle/système.
- Compatibilités de flexible, adaptateur, batterie, filtre, sac et consommables doivent être vérifiées lorsqu'elles changent la décision.
- Les cas à risque élevé (amiante, silice, poussières réglementées) exigent un langage prudent et ne se réduisent jamais à « acheter une classe plus élevée ».

---

# 7. Couche custom n°4 — intégrité pédagogique et similarité du cluster

Un guide n'est pas jugé à sa longueur mais à sa capacité à rendre une chose **plus claire, plus faisable ou plus décidable**.

Vérifier :

- réponse principale suffisamment tôt ;
- chaque section ajoute une information ou un raisonnement distinct ;
- tableau seulement s'il clarifie une comparaison ;
- procédure seulement aussi détaillée que nécessaire ;
- définition reliée à une conséquence pratique ;
- cas limites et contre-indications importantes visibles ;
- sources proportionnées à la stabilité du claim.

Comparer aussi les guides entre eux : fonctions des H2/H3, ordre des questions, tableaux au même endroit, blocs « avantages/inconvénients/comment choisir/FAQ », nombre artificiellement identique d'étapes, transitions et CTA clonés.

Les composants visuels partagés sont normaux. La pensée éditoriale ne doit pas être déterminée avant l'intention et les preuves.

---

# 8. Niveaux de preuve

Utiliser : `OBSERVED`, `SUPPORTED`, `INFERRED`, `HYPOTHESIS`, `UNKNOWN`.

Principes :

- une capacité actuelle doit être vérifiée ;
- une valeur constructeur reste une valeur constructeur ;
- une conclusion sur le comportement réel ne naît pas d'une fiche technique seule ;
- `UNKNOWN` ne devient jamais une certitude rédactionnelle ;
- aucun hands-on n'est inventé.

---

# 9. Décisions

## `KEEP`
Page distincte, actuelle, utile et correctement cadrée.

## `LIGHT_UPDATE`
Corrections ciblées : faits, sources, exemple, title/meta, maillage, frontière, quelques passages ou procédure locale.

## `DEEP_REWRITE`
Intention/rôle mal cadré, procédure non fiable, explication sans mécanisme/conséquence, guide de choix incapable d'arbitrer, preuves centrales insuffisantes, cannibalisation forte ou architecture industrialisée.

Préserver les faits, sources, passages et raisonnements valides identifiés par l'audit.

## `MERGE`
Une autre URL couvre essentiellement la même tâche. Indiquer la cible recommandée sans merger/rediriger automatiquement.

## `NOINDEX`
Valeur, preuve ou justification insuffisante. Aucune suppression automatique.

Pour chaque décision : confiance, valeur à préserver, preuves, unknowns, blockers, corrections, cannibalisation et prochaine étape.

### Handoff

- `KEEP` → aucune rédaction ;
- `LIGHT_UPDATE` → `guide-content-workflow` scope limité ;
- `DEEP_REWRITE` → `guide-content-workflow` reconstruction guidée par intention + preuves ;
- `MERGE` / `NOINDEX` → décision humaine avant action structurelle.

---

# 10. `PUBLISH_REVIEW`

Sur une version considérée terminée :

1. exécuter `python3 validate_guide_workflow.py` ;
2. exécuter `python3 validate_guide_quality.py` ;
3. réexécuter intention, fact-check, affiliate-value, anti-ai-slop, internal linking, SEO et editorial QA ;
4. vérifier les frontières avec usages/comparatifs/marques ;
5. vérifier les claims métier ci-dessus ;
6. vérifier l'absence de ranking produit déguisé et de structure clonée ;
7. confirmer `noindex, follow` tant que l'indexation n'a pas été explicitement demandée.

Sortie exacte :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Le PASS machine est un plancher structurel. La validation humaine reste obligatoire.
