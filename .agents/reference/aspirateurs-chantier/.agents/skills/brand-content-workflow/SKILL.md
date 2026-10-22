---
name: brand-content-workflow
description: Orchestration 80/20 des pages /marques/ d'aspirateurs-chantier.fr. La méthode éditoriale reste portée par les skills partagés vendored depuis bloc-notes-numerique et leurs repos upstream ; le custom est limité aux contraintes métier aspirateurs et au routage du cluster.
metadata:
  adapted_for: aspirateurs-chantier.fr
  source_workflow: bloc-notes-numeriques.fr/brand-content-workflow
  orchestration_target: ">=80% shared responsibilities; <=20% custom"
---

# Brand Content Workflow — aspirateurs-chantier.fr

## Contrat 80/20

Ce workflow est un **orchestrateur**, pas un générateur éditorial custom.

- **>=80% shared** : intention, audit, refresh, recherche/fact-check, preuves de jugement, valeur affiliée, brief, rédaction, finition, maillage, SEO et QA sont délégués aux skills partagés du dépôt, eux-mêmes vendored depuis `MarcW88/bloc-notes-numerique` avec leur provenance conservée.
- **<=20% custom** : uniquement les contraintes métier aspirateurs de chantier, la logique distinctive propre à la marque et le handoff vers le gate inter-marques.

Interdit : créer un nouveau skill custom qui duplique `fact-check`, `affiliate-value`, `humanizer`, `content-and-copy`, `internal-linking-audit`, SEO ou QA.

Avant toute production :

```bash
python3 validate_brand_skill_stack.py
```

Un FAIL bloque le travail.

---

# 1. Entrées obligatoires

Lire :

- `AGENTS.md` ;
- `brand-workflow.config.yaml` ;
- page cible et pages sœurs ;
- `.content/brands/<slug>.yaml` ;
- `.content/brands/audits/` ;
- pages `/modeles/`, `/comparatifs/`, `/guides/`, `/usages/` utiles ;
- données sémantiques/GSC disponibles ;
- sources actuelles nécessaires.

Pour une page existante, commencer par `brand-analysis-workflow / AUDIT`.

Le HTML généré n'est jamais la source de vérité éditoriale. `_generate_brands.py` fournit seulement un shell/seed ; il ne peut ni définir le plan final ni accorder un PASS de publication.

---

# 2. Chaîne shared obligatoire

Exécuter les responsabilités dans cet ordre et conserver un résumé d'output pour le run-evidence final.

1. `search-intent`
2. `content-audit`
3. `content-refresh` si l'audit conclut UPDATE ; sinon marquer `N/A` avec raison
4. `fact-check` — evidence brief **avant** le plan
5. `evidence-based-reviews` dès qu'un jugement dépasse une spec ; sinon `N/A` motivé
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

Le workflow partagé `content-recovery-and-production-workflow` reste la couche de récupération générale. Ne pas recopier sa méthode ici.

## Ce que chaque étape doit laisser

Le run doit permettre de retrouver au minimum :

- la décision/problème réel du lecteur ;
- ce qui est conservé ou supprimé de l'ancien contenu ;
- les claims et sources ;
- les contradictions/unknowns ;
- la valeur de la page sans aucun lien affilié ;
- un brief/plan où chaque section répond à une question et cite ses preuves ;
- les changements issus des passes de style et QA ;
- les risques résiduels.

Une simple mention « skill exécuté » n'est pas une preuve suffisante.

---

# 3. Le plan vient des preuves, jamais du type BRAND_HUB

Après `search-intent`, `fact-check`, `affiliate-value` et `content-brief-authoring`, construire une architecture **propre à l'URL**.

Pour chaque section, documenter :

- `question` : question réelle du lecteur ;
- `evidence_refs` : faits/sources qui permettent de répondre ;
- `decision_value` : ce que cette réponse change dans le choix.

Supprimer une section qui n'a pas ces trois éléments.

Interdictions :

- ordre fixe « gamme → écosystème → forces → limites → pour qui → éviter » ;
- nombre fixe de H2/H3 ;
- FAQ automatique ;
- tableau obligatoire ;
- conclusion automatique ;
- quota de mots ;
- paragraphe passe-partout partagé entre marques.

Une page Kärcher, Festool, Parkside ou Mirka n'a aucune raison de partager le même squelette si les vraies décisions diffèrent.

---

# 4. Custom autorisé — seulement le métier aspirateurs

Le custom sert à éviter les erreurs propres au domaine. Selon la marque et la page, vérifier :

- classes L / M / H et rôle d'un aspirateur de sécurité ;
- filtre/HEPA vs classe de sécurité ;
- débit et dépression avec contexte de mesure ;
- capacité brute/net/eau ;
- décolmatage ;
- prise asservie / démarrage outil ;
- antistatique ;
- flexibles, raccords et outils ;
- LXT/XGT, XR/FLEXVOLT, Bosch DIY/Professional ou autres plateformes ;
- sacs, filtres et consommables ;
- eau/poussière vs poussières potentiellement dangereuses ;
- poids, mobilité et volume ;
- génération/statut exact du produit.

Règles absolues : ne jamais déduire une classe depuis la puissance ou un filtre ; ne pas comparer des métriques fabricants comme équivalentes si leurs protocoles diffèrent ; ne jamais transformer une donnée fabricant ou un test tiers en observation maison.

Le custom peut identifier l'angle spécifique d'une marque — par exemple WD/NT chez Kärcher ou CLEANTEC/CT chez Festool — mais **la rédaction et la recherche restent gérées par les shared skills**.

---

# 5. Profondeur et valeur ajoutée

Ne pas confondre « pas de quota de mots » avec « contenu court par défaut ».

Le draft doit aller aussi loin que nécessaire pour résoudre la décision : générations pertinentes, compatibilités, conséquences pratiques, limites, coût d'écosystème, alternatives rationnelles, contradictions de sources et cas où il vaut mieux ne pas acheter cette marque.

Test `affiliate-value` obligatoire : si tous les liens commerciaux disparaissent, la page doit encore permettre une décision mieux informée qu'une lecture des fiches constructeur.

---

# 6. Persistance : run-evidence v2

À la fin de la production, créer ou mettre à jour :

`.content/brands/runs/<slug>.json`

avec `contract_version: 2` et :

- `shared_steps` : les 16 étapes ci-dessus, `PASS` ou `N/A` motivé ;
- `custom_steps` : `vacuum-domain-review` et, après gate final, `brand-analysis-publish-review` ;
- `reader_decision` ;
- `value_without_affiliate_links` ;
- `outline` avec `question`, `evidence_refs`, `decision_value` ;
- `publish_review`.

Chaque step `PASS` doit avoir un `output` concret. Le générateur Python n'est jamais autorisé à fabriquer ce fichier à la place du workflow éditorial.

Validation :

```bash
python3 validate_brand_run_evidence.py --slug <slug> --require-run
```

---

# 7. Génération et QA

Après stabilisation du contenu :

```bash
python3 _generate_brand_content.py
python3 _validate_brands.py
python3 validate_brand_run_evidence.py --slug <slug> --require-run
```

Le générateur doit préserver le plan bespoke. `_validate_brands.py` bloque notamment :

- le vieux squelette générique réintroduit ;
- une signature H2 clonée sur plusieurs marques ;
- de longs paragraphes identiques réutilisés sur plusieurs marques ;
- un faux langage de test ;
- un statut READY sans run-evidence valide.

---

# 8. Gate final et indexation

Appeler `brand-analysis-workflow / PUBLISH_REVIEW` après les shared skills.

Seul résultat acceptable pour une page prête :

`PASS — READY_FOR_HUMAN_VALIDATION`

Sinon :

`FAIL — KEEP_NOINDEX`

Même avec PASS : conserver `noindex, follow` jusqu'à validation humaine explicite et instruction explicite d'indexer.

---

# Résumé

```text
brand-analysis-workflow / AUDIT
      ↓
16 responsabilités SHARED (intention → preuves → brief → rédaction → QA)
      ↓
custom vacuum-domain review (étroit)
      ↓
run-evidence v2
      ↓
génération shell + body bespoke
      ↓
anti-template machine QA
      ↓
brand-analysis-workflow / PUBLISH_REVIEW (custom étroit)
      ↓
validation humaine
```

La cible de gouvernance reste **>=80% shared / <=20% custom** ; augmenter le custom pour « améliorer » une page est un échec d'architecture, pas une solution.
