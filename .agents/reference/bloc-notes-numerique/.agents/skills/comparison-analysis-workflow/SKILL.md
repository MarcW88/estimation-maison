---
name: comparison-analysis-workflow
description: Workflow unique d'analyse des pages /comparatifs/ de bloc-notes-numeriques.fr. Orchestre principalement des skills GitHub externes pour l'intention, l'audit, les preuves, l'on-page et la qualité éditoriale, puis ajoute seulement les contrôles spécifiques à une comparaison. Décisions: KEEP, LIGHT_UPDATE, DEEP_REWRITE, MERGE ou NOINDEX. En PUBLISH_REVIEW, sert de gate final avant validation humaine.
metadata:
  adapted_for: bloc-notes-numeriques.fr
  orchestration_target: ">=80% existing GitHub skills"
  custom_scope: "orchestration + comparison sanity + cluster similarity"
---

# Comparison Analysis Workflow

## Rôle

C'est le **seul workflow d'analyse** à utiliser pour `/comparatifs/`.

Comme le `brand-analysis-workflow`, il doit rester un **orchestrateur**. Il ne doit pas reconstruire en interne les méthodologies déjà couvertes par les skills spécialisés.

Principe :

> **Évaluer la qualité de la décision offerte au lecteur, pas la sophistication apparente de la méthodologie.**

Un comparatif n'a pas besoin d'un scoring, de poids, d'un univers exhaustif ou d'un Total Solution Cost pour être bon. Ces outils ne sont utilisés que lorsqu'ils améliorent réellement la décision.

---

# 1. Modes

## `AUDIT`
Analyse une URL existante. Produit un diagnostic et une décision, sans réécriture.

## `CLUSTER_AUDIT`
Compare plusieurs URLs `/comparatifs/` afin de détecter chevauchements d'intention, recommandations recyclées et architectures industrialisées.

## `PUBLISH_REVIEW`
Gate final après rédaction. Retourne :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Un PASS ne retire jamais `noindex,follow`.

---

# 2. Entrées

Lire selon disponibilité :

- page cible ;
- pages comparatives voisines ;
- `comparison-workflow.config.yaml` ;
- données `.content/comparisons/` associées ;
- GSC / analyse sémantique / historique si disponibles ;
- SERP actuelle quand l'intention est incertaine ou susceptible d'avoir changé ;
- pages marques, usages et guides nécessaires au contexte ;
- sources actuelles pour les faits qui peuvent évoluer.

L'absence de données doit être signalée, jamais compensée par une précision inventée.

---

# 3. Chaîne de skills — source principale de l'analyse

## 3.1 `seo-content-audit` — Rampstack

Utiliser `.agents/skills/seo-content-audit/SKILL.md` pour déterminer si la page mérite d'être conservée, mise à jour ou consolidée et pour examiner la cannibalisation.

Ce skill porte la logique `KEEP / UPDATE / MERGE / REDIRECT / DELETE`. Le workflow ne la réécrit pas.

## 3.2 `seo-keyword` — Rampstack

Utiliser `.agents/skills/seo-keyword/SKILL.md` pour :

- confirmer la requête ou le cluster ;
- classifier l'intention ;
- vérifier la forme dominante de SERP ;
- distinguer deux URLs proches ;
- détecter un périmètre trop large ou trop étroit.

Si GSC ou données sémantiques existent, elles priment sur une supposition.

## 3.3 `jobs-to-be-done` — Wondel.ai

Utiliser pour les comparatifs où le contexte change réellement la décision : étudiant, professionnel, PDF, mobilité, budget d'usage, etc.

Ne pas l'utiliser pour inventer un persona. Il sert à comprendre le travail à accomplir et les contraintes qui peuvent faire préférer un produit à un autre.

## 3.4 `evidence-based-reviews` — Rampstack

C'est le skill principal pour l'intégrité des recommandations et des jugements produit.

Il distingue :

- specs constructeur vérifiées ;
- synthèse d'expérience utilisateurs ;
- triangulation de sources expertes ;
- hands-on uniquement lorsqu'il existe réellement.

Règle importante : une spec officielle peut soutenir un **fait**. Elle ne devient pas automatiquement une preuve d'une **sensation d'usage**. Inversement, un score éditorial n'a pas besoin d'être traité comme une mesure scientifique : il doit simplement être présenté comme un jugement éditorial et être explicable.

## 3.5 `fact-check`

Vérifier les claims importants : génération, fonctions, compatibilités, prix, abonnement, disponibilité et comparatifs factuels.

Le fact-check ne doit pas transformer une appréciation éditoriale en donnée scientifique.

## 3.6 `affiliate-value`

Vérifier que la page reste utile sans les liens affiliés et apporte plus qu'une réécriture de fiches constructeurs : arbitrages, limites, incompatibilités, alternatives et conséquences pratiques.

## 3.7 `seo-onpage` — Rampstack

Pour l'URL individuelle : title, meta, H1, structure, contenu, maillage, canonical, URL et schema honnête.

Aucun quota de headings, mots ou liens.

## 3.8 `anti-ai-slop`

Analyser la page comme un artefact éditorial : structure interchangeable, blocs trop symétriques, répétitions, verdicts génériques et sur-lissage.

Ce skill ne sert pas à détecter qui a écrit le contenu.

## 3.9 `editorial-qa`

QA générique finale sur intention, valeur originale, factualité, naturel, SEO et utilité réelle.

---

# 4. Couche custom minimale — sanity check comparatif

Cette couche est volontairement courte. Elle ne remplace aucun skill ci-dessus.

Vérifier seulement les points propres à une recommandation comparative :

### A. Périmètre crédible

- les options comparées sont plausibles pour la requête ;
- les candidats majeurs manifestement pertinents ont été considérés **ou** le périmètre est expliqué ;
- aucune exhaustivité artificielle n'est exigée ;
- une exclusion importante mérite une raison, pas un registre de dizaines de produits sans intérêt.

### B. Critères avant recommandation

- les critères découlent de l'intention/JTBD ;
- ils expliquent réellement les différences entre les choix ;
- le gagnant n'a pas été choisi puis rationalisé après coup.

### C. Verdict traçable

La recommandation doit permettre de répondre :

- pourquoi ce choix est recommandé ;
- dans quelle situation un autre choix devient meilleur ;
- quelle limite peut faire changer de décision.

Un verdict conditionnel est souvent préférable à un gagnant universel.

### D. Comparabilité honnête

Lorsque les produits ou configurations diffèrent fortement, le texte l'explique. La comparaison n'a pas besoin d'une « equivalence engine » formelle si le lecteur comprend clairement ce qui est comparable et ce qui ne l'est pas.

### E. Coût proportionné à l'intention

Comparer le coût de façon équitable **lorsqu'il est décisionnel**. Pour une page budget ou sans abonnement, approfondir. Pour une page où le coût est secondaire, ne pas imposer un TSC complexe.

### F. Scoring optionnel

Le scoring est autorisé mais jamais obligatoire.

S'il existe :

- ses critères doivent être compréhensibles ;
- les notes sont des jugements éditoriaux, sauf mesure réellement observée ;
- éviter la fausse précision ;
- le texte doit rester utile même sans le score.

L'absence de scoring n'est jamais un blocker.

---

# 5. Contrôle custom — cluster et industrialisation

Comparer la page aux comparatifs voisins.

Chercher notamment :

- même fonction de H2 dans le même ordre ;
- même intro avec substitution de requête ;
- mêmes fiches produit symétriques ;
- mêmes produits et mêmes arguments sous plusieurs intentions ;
- même verdict simplement repondéré ;
- transitions ou conclusions recyclées ;
- différence éditoriale trop faible entre `meilleur`, `étudiant`, `professionnel`, `tablette E Ink`, etc.

Les composants visuels partagés sont normaux. Le problème apparaît lorsque **la pensée éditoriale** est clonée.

Une similarité substantielle peut déclencher `DEEP_REWRITE` même si les facts sont corrects.

---

# 6. Décision

## `KEEP`
Page distincte, actuelle, utile et convaincante. Aucun changement substantiel.

## `LIGHT_UPDATE`
Corrections locales : faits, sources, sélection secondaire, formulation, title/meta, maillage ou quelques arbitrages. La logique fondamentale reste bonne.

## `DEEP_REWRITE`
Réserver ce statut aux cas où il faut réellement reconstruire :

- intention ou rôle mal cadré ;
- sélection manifestement inadéquate ;
- recommandation impossible à justifier ;
- valeur affiliée faible ;
- architecture fortement industrialisée ;
- contenu substantiellement obsolète ;
- preuves trop faibles pour les principaux jugements publiés.

**Ne pas** classer automatiquement `DEEP_REWRITE` parce qu'une note éditoriale n'a pas de test indépendant ou parce qu'un registre méthodologique sophistiqué est absent.

## `MERGE`
Une autre URL sert essentiellement la même décision et la différenciation ne justifie pas deux pages.

## `NOINDEX`
La page n'a pas encore assez de valeur ou de justification pour être indexée. Aucune suppression/redirection automatique.

Pour chaque décision fournir :

- confiance ;
- valeur existante à préserver ;
- problèmes réellement bloquants ;
- améliorations secondaires ;
- données manquantes importantes ;
- prochaine étape.

Un `DEEP_REWRITE` passe au `comparison-content-workflow`.

---

# 7. PUBLISH_REVIEW

Après rédaction :

1. exécuter `python3 validate_comparisons.py` ;
2. rejouer les skills pertinents ci-dessus sur la version finale ;
3. comparer la structure aux pages sœurs ;
4. vérifier que le verdict est cohérent avec les preuves et les limites ;
5. vérifier qu'aucun faux hands-on ou contenu marchand faible n'a été introduit ;
6. vérifier title/H1/canonical/robots/schema ;
7. vérifier que la page reste utile sans liens affiliés.

### PASS

`PASS — READY_FOR_HUMAN_VALIDATION`

### FAIL

`FAIL — KEEP_NOINDEX`

Lister précisément le ou les gates en échec et router vers le skill concerné. Un FAIL ne déclenche pas automatiquement une réécriture totale.

---

# 8. Indexation

Conserver `noindex,follow` par défaut.

Indexation uniquement après :

1. validateur machine sans blocker ;
2. PUBLISH_REVIEW PASS ;
3. validation humaine explicite ;
4. instruction explicite de rendre la page indexable.

---

# 9. Répartition 80/20

La méthode doit venir majoritairement des skills GitHub existants :

- Rampstack : `seo-content-audit`, `seo-keyword`, `evidence-based-reviews`, `seo-onpage` ;
- Wondel.ai : `jobs-to-be-done` ;
- stack externe éditoriale : `anti-ai-slop`, puis `editorial-qa`/skills de contrôle existants.

La couche custom de ce workflow se limite à :

1. orchestration ;
2. sanity check de la comparaison ;
3. similarité structurelle/cannibalisation spécifique au cluster ;
4. mapping vers les cinq décisions du site.

Ne jamais transformer ce workflow en deuxième copie des skills qu'il orchestre.