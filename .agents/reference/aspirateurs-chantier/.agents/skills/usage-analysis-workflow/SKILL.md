---
name: usage-analysis-workflow
description: Workflow unique d'analyse des pages /usages/ d'aspirateurs-chantier.fr. Adapté de MarcW88/bloc-notes-numerique. Audite une page ou le cluster, vérifie intention, JTBD, frontières avec comparatifs/guides, preuves, valeur affiliée, sécurité des claims aspirateurs, AI-slop et SEO, puis décide KEEP, LIGHT_UPDATE, DEEP_REWRITE, MERGE ou NOINDEX. En PUBLISH_REVIEW, sert de gate final avant validation humaine.
metadata:
  source_repo: MarcW88/bloc-notes-numerique
  source_skill: .agents/skills/usage-analysis-workflow/SKILL.md
  adapted_for: aspirateurs-chantier.fr
  orchestration_target: ">=80% existing skills"
---

# Usage Analysis Workflow — aspirateurs-chantier.fr

## Rôle

C'est le **seul workflow d'analyse** à utiliser pour les URLs sous `/usages/`.

Il ne réécrit pas la page par défaut. Il orchestre d'abord les skills partagés déjà présents dans le dépôt et limite la couche custom aux contrôles propres à l'univers des aspirateurs de chantier.

Séparation stricte :

- `usage-analysis-workflow` = diagnostiquer, comparer le cluster, décider et faire le publish review ;
- `usage-content-workflow` = produire/corriger uniquement lorsque l'analyse le demande ;
- `/comparatifs/` = choisir entre produits ou familles de produits ;
- `/guides/` = expliquer une technologie, un risque, un critère ou une procédure ;
- `/marques/` = documenter marque, gamme ou écosystème.

Le workflow ne doit pas devenir un second système de fact-check, de rédaction, de SEO ou d'affiliation : ces responsabilités restent dans les skills partagés.

---

# 1. Modes

## `AUDIT`

Mode par défaut pour une URL existante. Retourne une décision et un plan de correction **sans réécrire la page**.

Comparer la page avec :

- les usages voisins ;
- les comparatifs qui pourraient absorber l'intention d'achat ;
- les guides qui couvrent une sous-question technique ;
- les pages marques citées ou susceptibles de prendre le dessus sur le job.

## `CLUSTER_AUDIT`

Analyse l'ensemble de `/usages/` pour détecter :

- jobs trop proches ;
- pages matière/outillage dont le rôle est mal défini ;
- cannibalisation avec guides/comparatifs ;
- duplication de valeur ;
- structures industrialisées ;
- trous de couverture dans le parcours de choix et d'utilisation.

Aucune réécriture, redirection ou fusion automatique.

## `PUBLISH_REVIEW`

Gate final après `usage-content-workflow`.

Retourner exactement :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Un PASS n'autorise jamais l'indexation ou un merge automatique.

---

# 2. Entrées

Lire avant l'analyse :

- `AGENTS.md` et `DESIGN.md` si pertinent ;
- `usage-workflow.config.yaml` ;
- `.agents/skills/usage-skill-stack.json` ;
- la page cible ;
- `.content/usages/<slug>.json` si présent ;
- les pages `/usages/` proches ;
- les guides, comparatifs et pages marques voisines ;
- les données historiques disponibles : analyse sémantique, GSC, logs, backlinks ou autres signaux ;
- les sources actuelles pour tout fait susceptible d'avoir évolué.

Ne jamais combler une donnée absente par mémoire du modèle.

---

# 3. Chaîne de skills partagés obligatoire

Exécuter les skills existants avant les contrôles custom. Ne recopier ni leurs méthodes ni leurs checklists dans ce workflow.

## Audit, intention et job

- `content-audit` : valeur existante, obsolescence, duplication, cannibalisation, potentiel de récupération ;
- `search-intent` : requête/topic, intention dominante, problème concret, rôle de l'URL ;
- `jobs-to-be-done` : circonstances, progrès recherché, tâches, frictions, Push/Pull/Anxiety/Habit lorsque pertinent ;
- `content-refresh` : uniquement lorsque l'audit conclut qu'une mise à jour est nécessaire.

Sans interview ou donnée comportementale, une motivation supposée reste `INFERRED` ou `HYPOTHESIS`, jamais un fait utilisateur universel.

## Preuves et valeur

- `fact-check` : claims vérifiables ;
- `evidence-based-reviews` : seulement si un jugement expérientiel ou de comportement réel dépasse les specs ;
- `affiliate-value` : la page doit rester utile sans liens affiliés.

## Qualité, maillage et SEO

- `internal-linking-audit` ;
- `anti-ai-slop` ;
- `seo-technical` ;
- `seo-best-practices` et `seo-onpage` lorsque applicables ;
- `seo-drift` seulement si un baseline exploitable existe ;
- `editorial-qa` en dernière QA générique.

La provenance et le ratio des skills sont contrôlés par `.agents/skills/usage-skill-stack.json`.

---

# 4. Contrôle custom n°1 — le job possède-t-il une URL autonome ?

Une page usage doit expliquer **comment une situation de chantier modifie réellement le système d'aspiration à prévoir**.

Le job doit être défini par des circonstances et contraintes observables, par exemple :

- matière produite : sciure, copeaux, plâtre, poussière minérale, gravats, eau ;
- mode de production : ponçage continu, coupe intermittente, nettoyage de fin de chantier, captage à la source ;
- granulométrie et quantité ;
- fréquence et durée ;
- outil raccordé ou aspiration libre ;
- besoin de mobilité ;
- contraintes de collecte/vidage ;
- risque poussière et classe requise lorsqu'elle est réellement applicable.

Une URL n'est pas justifiée uniquement parce qu'un mot-clé combine `aspirateur + matière/outillage`.

### Signaux d'échec

- même raisonnement applicable à toutes les pages en changeant seulement `plâtre` par `sciure` ;
- critères hérités d'un catalogue produit plutôt que du travail réel ;
- page transformée en liste de modèles ;
- aucune contre-indication ou alternative ;
- aucune différence de workflow par rapport à une page sœur.

---

# 5. Contrôle custom n°2 — frontières avec Comparatifs et Guides

## `/usages/` vs `/comparatifs/`

La page usage répond à :

> Dans ce travail précis, quelles poussières/matières apparaissent, quelles frictions cela crée et quelles caractéristiques deviennent décisives ?

Le comparatif répond à :

> Quels modèles choisir entre eux une fois ces contraintes connues ?

Une page usage peut citer une famille ou un exemple pour illustrer une contrainte. Elle ne crée pas de podium, de ranking ni de pseudo-« meilleur aspirateur pour X » si la décision est réellement comparative.

## `/usages/` vs `/guides/`

La page usage reste centrée sur le **job complet**.

Les sous-questions autonomes doivent être renvoyées vers les guides, par exemple :

- classes L/M/H ;
- décolmatage du filtre ;
- aspiration eau/poussière ;
- débit vs dépression ;
- sac vs sans sac ;
- entretien des filtres ;
- règles de sécurité ou procédés spécifiques.

### Test pratique

Si une page usage et un guide/comparatif pourraient conserver le même H1, le même tableau principal et la même conclusion en modifiant seulement quelques mots, la frontière n'est pas assez nette.

---

# 6. Contrôle custom n°3 — workflow réel de captage et critères

Ne pas imposer un nombre fixe d'étapes.

Selon le job, vérifier seulement les étapes qui changent la décision, par exemple :

- production de poussière/matière ;
- captage à la source ou nettoyage après émission ;
- transfert via flexible/raccord ;
- maintien du débit lorsque le filtre se charge ;
- collecte dans sac/cuve ;
- vidage et exposition secondaire ;
- déplacement entre postes ;
- gestion des liquides si pertinente.

Chaque critère doit répondre à :

> Qu'est-ce que ce critère change dans cet usage précis ?

Un critère générique sans conséquence sur le job doit être retiré ou rétrogradé.

---

# 7. Contrôle custom n°4 — sécurité et comparabilité des claims aspirateurs

Ces règles ne remplacent pas `fact-check` ; elles définissent uniquement les erreurs métier à interdire.

- Ne jamais déduire une classe L/M/H depuis HEPA, puissance, débit, dépression ou décolmatage.
- Filtration, nettoyage du filtre et classe de poussière sont des notions distinctes.
- `wet/dry` ne signifie pas aptitude aux poussières dangereuses.
- ACD ne doit pas être présenté comme équivalent à une certification ATEX/Zone 22.
- Une classe de filtre ne transforme pas automatiquement la certification de la machine complète.
- Débit et dépression cross-brand ne sont pas comparables sans contexte de mesure suffisamment homogène.
- Les capacités brut/net/eau ne doivent pas être mélangées.
- Les compatibilités de flexible, raccord outil, batterie et consommables doivent être vérifiées au niveau pertinent si elles influencent la recommandation.
- Les cas à risque élevé (amiante, silice ou poussières réglementées) doivent rester prudents et renvoyer vers les prescriptions applicables ; ne pas simplifier la sécurité en « acheter une classe plus élevée ».

---

# 8. Similarité structurelle du cluster

En `AUDIT`, comparer la page aux sœurs les plus proches. En `CLUSTER_AUDIT` et `PUBLISH_REVIEW`, regarder tout le cluster pertinent.

Comparer :

- fonction sémantique des H2/H3 ;
- ordre des questions ;
- mêmes critères dans le même ordre ;
- même cadence « problème → tableau → produits → conclusion » ;
- emplacement mécanique des tableaux, listes, CTA et blocs limites ;
- mêmes familles de solutions répétées sans nécessité ;
- formulations et transitions recyclées.

Les composants visuels communs sont acceptables. Une architecture éditoriale décidée avant l'analyse du job ne l'est pas.

---

# 9. Niveaux de preuve

Utiliser :

- `OBSERVED` ;
- `SUPPORTED` ;
- `INFERRED` ;
- `HYPOTHESIS` ;
- `UNKNOWN`.

Principes :

- une motivation utilisateur non observée reste une hypothèse ;
- une capacité machine actuelle doit être vérifiée ;
- un comportement en poussière fine ne devient pas prouvé par une puissance moteur ;
- `UNKNOWN` ne devient jamais une certitude rédactionnelle ;
- aucun hands-on n'est inventé.

---

# 10. Décisions

## `KEEP`

Job distinct, intention servie, page actuelle, suffisamment utile et différenciée.

## `LIGHT_UPDATE`

Corrections ciblées : faits, preuves, frontière, maillage, quelques critères ou passages. Architecture fondamentale pertinente.

## `DEEP_REWRITE`

Job mal cadré, contenu devenu comparatif déguisé, preuve insuffisante sur des points structurants, architecture industrialisée ou valeur trop faible.

Préserver les éléments valides plutôt que repartir mécaniquement de zéro.

## `MERGE`

Une autre URL couvre pratiquement le même job/intention. Recommander une cible, sans merger/rediriger automatiquement.

## `NOINDEX`

Valeur/preuve/justification insuffisante. Aucune action destructive automatique.

Pour chaque décision : confiance, preuves, unknowns, blockers, valeur à préserver, corrections, prochaine étape.

### Handoff

- `KEEP` → aucune rédaction ;
- `LIGHT_UPDATE` → `usage-content-workflow` scope limité ;
- `DEEP_REWRITE` → `usage-content-workflow` reconstruction guidée par job + preuves ;
- `MERGE` / `NOINDEX` → décision humaine avant action structurelle.

---

# 11. `PUBLISH_REVIEW`

Sur une version considérée terminée :

1. exécuter `python3 validate_usage_workflow.py` ;
2. réexécuter au minimum intention, JTBD, fact-check, affiliate-value, anti-ai-slop, internal linking, SEO technique et editorial QA ;
3. vérifier les frontières avec guides/comparatifs ;
4. vérifier les claims de sécurité aspirateurs ;
5. vérifier l'absence de ranking produit déguisé et de structure clonée ;
6. confirmer `noindex, follow` tant que l'indexation n'a pas été explicitement demandée.

Sortie exacte :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Le PASS machine n'est qu'un plancher structurel. La validation humaine reste obligatoire.
