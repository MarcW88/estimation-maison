---
name: guide-content-workflow
description: Workflow unique de production et correction des guides SEO/GEO sous /guides/ d'aspirateurs-chantier.fr. Adapté de MarcW88/bloc-notes-numerique. Utiliser après guide-analysis-workflow lorsqu'une page existante nécessite LIGHT_UPDATE ou DEEP_REWRITE, ou pour créer un nouveau guide. Orchestre majoritairement des skills existants pour intention, recherche, preuves, brief, rédaction et QA.
metadata:
  source_repo: MarcW88/bloc-notes-numerique
  source_skill: .agents/skills/guide-content-workflow/SKILL.md
  source_sha: 7562fb6c569ef18d4ec0bccecd6584d559f90291
  adapted_for: aspirateurs-chantier.fr
  orchestration_target: ">=80% existing skills"
  custom_scope: "guide routing + vacuum-domain integrity + category boundaries + source-of-truth integration"
---

# Guide Content Workflow — aspirateurs-chantier.fr

## Rôle

C'est le seul workflow de production/correction pour `/guides/`.

Séquence :

`guide-analysis-workflow / AUDIT` → décision → production si nécessaire → `guide-analysis-workflow / PUBLISH_REVIEW`.

- `KEEP` : ne pas réécrire ;
- `LIGHT_UPDATE` : ne corriger que le scope audité ;
- `DEEP_REWRITE` : reconstruire la page en préservant les éléments valides ;
- `MERGE` / `NOINDEX` : aucune nouvelle version ou redirection sans décision humaine.

Le workflow ne retire jamais `noindex, follow`.

## Entrées

Lire :

- `guide-workflow.config.yaml` ;
- `.agents/skills/guide-analysis-workflow/SKILL.md` ;
- `.agents/skills/guide-skill-stack.json` ;
- le cluster audit et la page cible ;
- `.content/guides/<slug>.json` si présent ;
- `.content/guides/v2/<slug>.html` et `render-map.json` pour un guide déjà migré ;
- les guides voisins et pages `/usages/`, `/comparatifs/`, `/marques/` proches ;
- les données sémantiques, GSC ou autres signaux disponibles ;
- les sources nécessaires aux faits actuels.

`_generate_guides.py` reste la baseline historique du shell/contenu Guide. Pour les pages travaillées avec le workflow v2, **la source éditoriale finale est le fragment authored sous `.content/guides/v2/`**, matérialisé par `_materialize_guides_v2.py`. `_guide_quality_supplements.py` est déprécié et ne doit plus être exécuté : aucun seuil de longueur ne peut décider qu'une section est nécessaire.

## Router sans créer de template

Le type dominant sert uniquement à sélectionner les risques à vérifier :

- `CHOICE` : arbitrer entre options/contraintes ;
- `EXPLAINER` : expliquer une mesure, classe, technologie ou mécanisme ;
- `HOW_TO` : permettre une tâche vérifiable ;
- `HYBRID` : uniquement lorsque plusieurs fonctions sont réellement nécessaires.

Les références `choice-guide`, `explainer-guide` et `how-to-guide` sont des questions de contrôle, jamais des plans obligatoires. Aucun quota de mots, H2, tableaux, FAQ, liens ou sources.

## Chaîne partagée obligatoire

### 1. Intention, cluster et rôle

Utiliser `seo-keyword`, `search-intent`, `seo-content-audit` et `content-refresh` selon la décision. Confirmer requête/topic, tâche du lecteur, périmètre, exclusions, prochaine étape et chevauchements internes.

Gate de frontière :

- `/guides/` = critère, risque, technologie, arbitrage ou procédure autonome ;
- `/usages/` = job complet et contraintes de travail ;
- `/comparatifs/` = choix entre modèles/familles ;
- `/marques/` = gamme ou écosystème.

### 2. Recherche et preuve

Utiliser `fact-check` sur les claims vérifiables. Adapter la profondeur à la stabilité du fait : norme/réglementation/compatibilité/gamme actuelle → vérification actuelle ; mécanisme stable → source technique solide ; jugement expérientiel → `evidence-based-reviews` uniquement si nécessaire.

Conserver claim, source, date, portée et incertitude. Une inconnue reste `UNKNOWN` ou est exclue.

### 3. Intégrité métier aspirateurs

Avant le brief :

- L/M/H ne se déduisent jamais de HEPA, puissance, débit, dépression ou décolmatage ;
- filtre H13/H14 ≠ aspirateur classe H ;
- débit, dépression et puissance électrique sont trois métriques distinctes ;
- une comparaison cross-brand exige un contexte de mesure suffisamment homogène ;
- distinguer capacités brute/nette/eau ;
- distinguer nettoyage manuel, semi-auto et automatique ;
- distinguer prise asservie, télécommande, Bluetooth et Wireless Tool Control ;
- vérifier compatibilités outil/flexible/batterie/sac/filtre lorsqu'elles changent la décision ;
- traiter amiante, silice et poussières réglementées avec prudence et renvoi aux prescriptions applicables.

### 4. Valeur et brief

Utiliser `affiliate-value` lorsque le guide influence l'achat. La page doit rester utile sans lien affilié.

Utiliser `content-brief-authoring` avec : tâche, angle, valeur propre, preuves, unknowns, valeur à préserver, maillage et structure issue de la recherche. Chaque grande section doit être justifiée par une question, étape, distinction, preuve, arbitrage ou limite.

### 5. Rédaction

Utiliser `content-and-copy`. Répondre tôt, écrire en français naturel et précis, distinguer faits/interprétations/inconnues, ne jamais inventer de test ou de mesure, et préserver en `LIGHT_UPDATE` ce que l'audit a jugé valide.

Pour une page v2 :

- corps authored : `.content/guides/v2/<slug>.html` ;
- title/meta/H1/lead/answer/TOC : `.content/guides/v2/render-map.json` ;
- preuve d'exécution : `.content/guides/<slug>.json` ;
- rendu : `_materialize_guides_v2.py`.

Le renderer ne peut jamais rédiger la méthode, fabriquer les preuves ou attribuer un PASS.

## Contrôles post-rédaction

Exécuter séparément :

1. `fact-check` final ;
2. `internal-linking-audit` ;
3. `humanizer` ;
4. `general-writing` ;
5. `anti-ai-slop` ;
6. `seo-drift` seulement avec baseline utile ;
7. `seo-onpage` ;
8. `seo-technical` ;
9. `seo-best-practices` lorsque pertinent ;
10. `editorial-qa` ;
11. lecture complète dans l'ordre rendu et QA visuelle lorsque disponible.

Aucun PASS ne peut être déduit d'une simple validation machine.

## Traçabilité

Pour chaque guide audité, persister `.content/guides/<slug>.json` avec :

- slug, URL, type et décision ;
- reader task ;
- valeur à préserver ;
- registre de preuves ;
- outline evidence-led ;
- exécution des skills partagés et des deux orchestrateurs ;
- risques résiduels ;
- `editorial.publish_review` ;
- `human_validation: false` tant que Marc n'a pas validé ;
- `robots: "noindex, follow"` tant que l'indexation n'a pas été explicitement demandée.

Un `KEEP` peut avoir un record et un PASS sans fragment v2 s'il n'a nécessité aucune réécriture.

## PUBLISH_REVIEW

Exécuter :

- `python3 validate_guide_workflow.py` ;
- `python3 validate_guide_quality.py` ;
- fact-check, affiliate-value, anti-ai-slop, internal linking, SEO et editorial QA ;
- comparaison finale au cluster.

Verdicts exacts :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Même avec PASS, aucune indexation automatique.

## Interdictions

Ne pas réintroduire : quota de mots, minimum de H2/H3, quota de liens/sources, nombre obligatoire d'étapes, tableau/FAQ obligatoire, score artificiel, architecture fixe par type ou duplication des règles déjà couvertes par les skills partagés.
