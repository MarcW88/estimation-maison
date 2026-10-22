---
name: content-recovery-and-production-workflow
description: Workflow générique de récupération, enrichissement, création et validation de contenus SEO/GEO. À utiliser pour auditer des contenus existants, conserver ce qui fonctionne, enrichir sémantiquement, créer les pages manquantes et appliquer une chaîne QA complète avant publication.
---

# Content Recovery & Production Workflow

## Objectif

Produire ou améliorer des contenus utiles, différenciés, vérifiables et suffisamment riches pour le SEO, le GEO et le business, sans réécrire inutilement ce qui fonctionne déjà.

Le workflow distingue deux situations :

1. **Contenu existant** → `RECOVERY`
2. **Page vide ou contenu non exploitable** → `NEW_CONTENT`

Principe central :

> Conserver ce qui apporte déjà de la valeur, réparer ce qui est faible, enrichir ce qui manque, et ne réécrire totalement qu'en dernier recours.

Le workflow doit être paramétré pour chaque site via `content-workflow.config.yaml`.

## 1. Entrées obligatoires

Avant toute analyse, lire :

- les instructions du repo (`AGENTS.md`, `README`, etc.) ;
- `content-workflow.config.yaml` ;
- la ou les pages cibles ;
- la source de vérité éditoriale (`_generate.py`, Markdown, CMS, composants, HTML source, etc.) ;
- l'analyse sémantique si disponible ;
- les données SEO utiles si disponibles ;
- les pages voisines du cluster ;
- la page de référence qualitative définie par `quality_reference`.

Ne jamais modifier uniquement un HTML généré si le projet possède une source de vérité distincte.

## 2. Routing : RECOVERY ou NEW_CONTENT

### RECOVERY

Diagnostiquer :

- intent drift ;
- thin value ;
- contenu générique ;
- duplication marchande ;
- structure faible ;
- manque d'entités ;
- manque de preuves ;
- manque de contexte ;
- manque de maillage ;
- contenu obsolète ;
- cannibalisation ;
- faiblesse transactionnelle/business ;
- tableaux ou listes non interprétés ;
- sections trop courtes.

Attribuer un niveau :

- `LIGHT`: conserver environ 70 % ou plus du contenu utile ;
- `MAJOR`: enrichissement important en conservant les bons passages ;
- `FULL`: seulement si le contenu est majoritairement inexploitable.

### NEW_CONTENT

Utiliser si la page est vide, placeholder, inexistante ou inexploitable.

## 3. Pré-analyse obligatoire

Avant rédaction, produire un brief persistant.

Le brief couvre :

- mot-clé principal ;
- variantes utiles ;
- sous-thèmes ;
- questions ;
- intention ;
- rôle dans le funnel ;
- SERP ;
- entités ;
- registre de preuves ;
- différenciation ;
- architecture ;
- risques ;
- maillage ;
- niveau de refresh.

Enregistrer dans `briefs_dir`.

## 4. Plan de refresh obligatoire

Pour `RECOVERY`, produire :

1. ce qui reste ;
2. ce qui est supprimé ;
3. ce qui est réécrit ;
4. ce qui est ajouté ;
5. informations nécessaires ;
6. claims à vérifier ;
7. maillage à renforcer ;
8. valeur business/affiliate ;
9. niveau de refresh.

## 5. Rédaction

### Réponse initiale
Répondre à la question principale dès les premières phrases.

### Richesse sémantique
Chaque H2 important doit être une unité de valeur complète.

Un H2 ne doit pas simplement contenir :
- un petit paragraphe ;
- un tableau non expliqué ;
- une liste sans contexte.

Selon le besoin, développer :
- contexte ;
- mécanisme ;
- conséquence ;
- exemple ;
- limite ;
- interprétation ;
- prochaine étape.

### Tableaux
Tout tableau important doit :
1. être introduit ;
2. répondre à une question claire ;
3. être interprété après.

### Exemples
Ne jamais inventer :
- tests ;
- mesures ;
- prix ;
- avis ;
- expérience personnelle ;
- compatibilités.

### Entités
Nommer explicitement les technologies, marques, formats, services et concepts pertinents.

### Liens internes
Ajouter des liens lorsqu'ils servent une décision ou un approfondissement.

### Business / affiliation
Si la page influence un achat :
- rester utile sans liens affiliés ;
- aider à éliminer des options ;
- expliquer les compromis ;
- créer une transition naturelle vers une page transactionnelle.

## 6. Standard qualitatif

Le projet doit définir une `quality_reference`.

Cette page sert de **plancher qualitatif**, pas de modèle à copier.

Comparer :
- profondeur ;
- contexte ;
- densité d'information utile ;
- exemples ;
- maillage ;
- interprétation des tableaux ;
- valeur décisionnelle ;
- précision des entités ;
- niveau de preuve.

Une page plus courte peut être valide si son intention est plus étroite.

Ne jamais gonfler artificiellement le texte pour atteindre un volume.

## 7. Chaîne QA obligatoire

Exécuter distinctement :

1. `content-refresh`
2. `search-intent`
3. `affiliate-value` si pertinent
4. `fact-check`
5. `natural-writing`
6. `internal-linking-audit`
7. `humanizer`
8. `general-writing`
9. `anti-ai-slop`
10. `seo-drift`
11. `seo-technical`
12. `seo-best-practices`
13. contrôle GEO
14. `editorial-qa`
15. lecture complète en ordre rendu

### Fact-check
Classer les claims :
- `CONFIRMED`
- `PARTIAL`
- `UNVERIFIED`
- `CONTRADICTED`
- `OUTDATED`

## 8. Quality gate automatique

Le script peut vérifier des signaux observables :

- réponse initiale ;
- H2 substantiels ;
- sections trop maigres ;
- tableaux sans contexte ;
- tableaux sans interprétation ;
- maillage trop faible ;
- faible diversité des cibles ;
- sources insuffisantes ;
- placeholder ;
- robots ;
- contenu manifestement trop court.

Le script **ne doit jamais** déclarer automatiquement :

- Fact-check PASS ;
- GEO PASS ;
- Humanizer PASS ;
- Natural writing PASS ;
- Anti-AI-slop PASS.

## 9. Échecs automatiques

FAIL si subsiste :

- expérience directe inventée ;
- test inventé ;
- mesure inventée ;
- prix non vérifié présenté comme actuel ;
- claim important non sourcé ;
- contenu principalement générique ;
- H2 importants trop faibles ;
- tableau sans interprétation ;
- maillage quasi absent ;
- cannibalisation ;
- lien cassé ;
- robots/canonical incorrect ;
- placeholder ;
- source de vérité non mise à jour ;
- réécriture totale sans justification.

## 10. Statuts

- `BRIEF_READY`
- `DRAFT_READY`
- `QA_IN_PROGRESS`
- `REVISION_REQUIRED`
- `HUMAN_APPROVED`
- `PUBLISHABLE`

Un CI vert ne suffit jamais pour `PUBLISHABLE`.

## 11. Publication

Par défaut :
- conserver `noindex` si utilisé ;
- ne pas merger ;
- ne pas publier ;
- ne pas déployer.

Une autorisation explicite est nécessaire.

## 12. Traçabilité

Conserver :
- brief ;
- sources ;
- refresh plan ;
- décisions ;
- exclusions ;
- QA ;
- blockers ;
- statut final.
