---
name: deal-content-workflow
description: Workflow unique de création, correction et réécriture des pages /bons-plans/ de bloc-notes-numeriques.fr. Orchestre principalement des skills GitHub existants pour l'intention, la preuve de prix, la factualité, la valeur affiliée, le brief, la rédaction, l'on-page et l'édition. Il consomme les handoffs du deal-analysis-workflow et renvoie la page vers PUBLISH_REVIEW.
metadata:
  adapted_for: bloc-notes-numeriques.fr
  orchestration_target: ">=80% existing GitHub skills"
  custom_scope: "orchestration + deal evidence + freshness"
---

# Deal Content Workflow

## Rôle

C'est le **seul workflow de production** à utiliser pour créer, actualiser ou réécrire une URL sous `/bons-plans/`.

Il travaille en binôme avec `deal-analysis-workflow` :

- `deal-analysis-workflow` diagnostique, décide et produit le handoff de correction ;
- `deal-content-workflow` applique uniquement les changements nécessaires, construit les preuves de l'offre, rédige, puis renvoie la page vers `PUBLISH_REVIEW`.

Principe central :

> **Intention → preuve de l'offre → prix de référence → valeur du deal → brief → rédaction → review.**

Un bon plan n'est pas un prix barré. Une page `/bons-plans/` doit permettre au lecteur de comprendre si l'offre existe réellement, si l'économie est défendable, si le produit reste pertinent et si acheter maintenant est rationnel.

---

# 1. Entrées et niveau de changement

Lire :

- `AGENTS.md` ;
- `deal-workflow.config.yaml` ;
- `references/promo-evidence.md` ;
- page cible et pages sœurs pertinentes ;
- `.content/deals/<slug>.json` ;
- pages marques, produits, comparatifs, guides et usages nécessaires ;
- sources actuelles de prix, disponibilité et caractéristiques produit.

## Page existante

Commencer obligatoirement par :

`.agents/skills/deal-analysis-workflow/SKILL.md` en mode `AUDIT`.

Consommer le `CONTENT_HANDOFF` produit par l'audit lorsqu'il existe.

Règles :

- `KEEP` → ne pas réécrire ;
- `LIGHT_UPDATE` → modifier uniquement le scope du handoff ;
- `DEEP_REWRITE` → reconstruire ce qui est nécessaire tout en préservant explicitement la valeur identifiée ;
- `MERGE` ou `NOINDEX` → ne pas déclencher une production structurelle sans décision humaine.

Ne pas transformer un `LIGHT_UPDATE` en refonte complète pour homogénéiser le style.

## Nouvelle page

Il n'y a pas d'audit préalable obligatoire, mais toutes les étapes de preuve, d'intention, de valeur et de QA restent obligatoires.

---

# 2. Types de pages — grilles de risque, jamais templates

Types définis dans `deal-workflow.config.yaml` :

- `LIVE_DEALS` : offres réellement intéressantes disponibles maintenant ;
- `BRAND_DEALS` : promotions et baisses de prix d'une marque ou gamme ;
- `EVENT_DEALS` : Black Friday, Prime Day ou autre événement commercial ;
- `SECOND_HAND` : occasion, reconditionné, refurbished ou open-box.

Le type détermine surtout les risques de fraîcheur et de preuve. Il ne doit jamais imposer un nombre de H2/H3, un ordre de sections, un tableau, une FAQ, une conclusion ou un nombre minimum d'offres.

---

# 3. Chaîne de production fondée sur les skills existants

## 3.1 Intention — `seo-keyword` + `search-intent`

Confirmer :

- target query / cluster ;
- intention dominante ;
- besoin immédiat du lecteur : acheter, surveiller, préparer un événement ou chercher de l'occasion ;
- rôle unique de l'URL ;
- frontières avec comparatifs, marques, guides et usages ;
- risque de cannibalisation avec une autre page Bons plans.

Utiliser les données disponibles avant d'inférer la cible.

## 3.2 Préservation / refresh — `seo-content-audit` + `content-refresh`

Pour une page existante :

- préserver ce que l'audit a identifié comme utile et encore valide ;
- corriger uniquement les problèmes documentés ;
- utiliser `content-refresh` lorsqu'il faut traiter obsolescence, merchant duplication, thin value, structure faible, cannibalisation ou prose générique.

Un changement de prix ou de statut n'exige pas automatiquement une réécriture éditoriale complète.

## 3.3 Preuve de l'offre — `fact-check` + registre deals

Avant le plan et avant toute formulation promotionnelle, créer ou mettre à jour `.content/deals/<slug>.json`.

Le registre est la source de vérité pour :

- `page_type` ;
- `status` ;
- `checked_at` ;
- `freshness_policy` ;
- `intent` ;
- `reference_prices` ;
- `offers` ;
- `watchlist` ;
- `evidence_ledger` ;
- `editorial` ;
- `qa`.

Ne jamais publier une offre qui n'existe que dans le HTML.

Pour chaque offre collecter selon disponibilité :

- produit exact et variante ;
- vendeur ;
- prix ;
- devise ;
- disponibilité ;
- frais ou contraintes connus ;
- bundle ;
- pays ;
- date/heure de vérification ;
- source ;
- prix de référence et base du prix de référence lorsqu'une remise est revendiquée.

## 3.4 Classification des offres

Utiliser uniquement :

- `ACTIVE_VERIFIED` : prix et disponibilité suffisamment vérifiés ;
- `ACTIVE_STOCK_SENSITIVE` : prix visible mais stock, pays, frais ou checkout peuvent changer l'offre ;
- `PRICE_WATCH` : prix observé sans preuve suffisante qu'il s'agit d'une promotion ;
- `EXPIRED` : promotion terminée ;
- `SOLD_OUT` : prix promotionnel visible mais stock épuisé ;
- `UNVERIFIED` : signal trouvé mais non confirmé ;
- `NOT_STARTED` : événement futur.

Une offre `ACTIVE_VERIFIED` doit au minimum avoir `merchant`, `price`, `currency`, `checked_at` et `source`.

Le texte final ne peut jamais être plus affirmatif que le statut du registre.

## 3.5 Prix de référence

Appliquer `references/promo-evidence.md`.

Ordre de préférence :

1. prix constructeur actuel hors promotion ;
2. prix constructeur précédent clairement daté ;
3. somme documentée des éléments d'un bundle ;
4. historique de prix fourni par une source spécialisée ;
5. prix barré marchand uniquement comme signal secondaire.

Ne jamais calculer une remise depuis un prix de référence dont l'origine n'est pas documentée.

Lorsque `price` et `reference_price` sont présents :

`discount_pct = (reference_price - price) / reference_price * 100`

Conserver les valeurs brutes dans le JSON et arrondir uniquement l'affichage si nécessaire.

Ne pas reprendre mécaniquement le pourcentage marketing du marchand.

## 3.6 Contexte produit — `fact-check` + `evidence-based-reviews` si nécessaire

Une réduction ne transforme pas un mauvais choix en bon choix.

Réutiliser les faits validés depuis les pages marques/produits ou les sources officielles. Vérifier uniquement les éléments nécessaires pour expliquer pourquoi l'offre peut être intéressante ou non.

Utiliser `evidence-based-reviews` seulement lorsqu'un jugement expérientiel produit l'exige. Ne jamais simuler de hands-on.

## 3.7 Valeur originale — `affiliate-value`

Avant le plan, identifier ce que la page apporte au-delà du marchand :

- remise réellement défendable ;
- prix à surveiller plutôt que fausse promotion ;
- seuil à partir duquel l'offre devient intéressante ;
- limites du produit ou du bundle ;
- alternative moins chère ou plus rationnelle ;
- situation où attendre est préférable ;
- risque de stock ou de variation au checkout ;
- pour l'occasion/reconditionné : état, garantie, canal, génération ou accessoires manquants lorsqu'ils changent la décision.

Test obligatoire : **la page reste-t-elle utile si tous les liens affiliés disparaissent ?**

---

# 4. Fraîcheur

Appliquer `deal-workflow.config.yaml`.

Repères du dépôt :

- `LIVE_DEALS` : offre active 48 h ; revue de page 7 jours ;
- `BRAND_DEALS` : offre active 72 h ; revue de page 7 jours ;
- `EVENT_DEALS` : offre active 24 h ; revue de page 14 jours ;
- `SECOND_HAND` : offre active 72 h ; revue de page 14 jours.

Une offre qui dépasse son TTL ne doit plus être présentée comme active sans nouvelle vérification.

Lors d'une mise à jour, si l'offre n'est plus confirmée, la reclasser en `UNVERIFIED`, `SOLD_OUT` ou `EXPIRED` et supprimer les formulations d'urgence/CTA promotionnels devenus faux.

Pour un événement commercial, distinguer explicitement les phases `avant`, `pendant` et `après` lorsque cela change le contenu.

---

# 5. Construction du brief avant rédaction

Utiliser `content-brief-authoring` avant le draft.

Le brief doit être spécifique à l'URL et préciser au minimum :

- query / intention ;
- rôle unique de la page ;
- offres réellement publiables et leur statut ;
- faits et prix de référence nécessaires ;
- valeur éditoriale originale ;
- ce que l'audit demande de préserver ;
- corrections obligatoires du `CONTENT_HANDOFF` ;
- frontières avec comparatifs/marques/guides/usages ;
- outline proposé et rôle de chaque section ;
- formulations ou claims interdits faute de preuve.

Aucun plan standard `intro → tableau → offres → pourquoi acheter → FAQ → conclusion` n'est imposé.

Chaque section doit pouvoir être justifiée par l'intention, une preuve ou une décision réelle du lecteur.

---

# 6. Rédaction — `content-and-copy`

Rédiger depuis le brief et le registre de preuve.

Priorités :

1. dire clairement ce qui est vérifié ;
2. distinguer remise réelle, prix observé et offre incertaine ;
3. indiquer la date de contrôle lorsque la fraîcheur est décisionnelle ;
4. expliquer pour qui l'offre a du sens ;
5. exposer limites et compromis ;
6. dire quand attendre ou choisir une autre option est préférable ;
7. préserver une voix éditoriale naturelle, non promotionnelle.

Interdictions :

- prix inventé ou extrapolé ;
- faux compte à rebours ;
- faux sentiment d'urgence ;
- « meilleur prix », « prix historique » ou « record » sans preuve suffisante ;
- ranking dépendant d'une commission ;
- promotion construite uniquement depuis un prix barré marchand ;
- deal périmé présenté comme actif ;
- transformation de la page en comparatif produit ;
- faux test ou expérience simulée ;
- métadiscours SEO/GEO/éditeur dans le texte utilisateur.

---

# 7. Fact-check post-draft

Après rédaction :

1. réextraire les claims vérifiables ;
2. comparer chaque offre avec `.content/deals/<slug>.json` ;
3. revalider prix, vendeur, disponibilité, prix de référence, date et statut ;
4. recalculer les remises affichées ;
5. vérifier que les formulations correspondent au niveau de preuve ;
6. retirer ou qualifier tout claim `UNVERIFIED`, périmé ou contradictoire ;
7. vérifier qu'aucune appréciation éditoriale n'est devenue une fausse mesure ou expérience propre.

Le fact-check est séparé de la rédaction afin d'éviter qu'une phrase commerciale plausible soit acceptée parce qu'elle « sonne juste ».

---

# 8. Finition éditoriale

Utiliser dans cet ordre :

1. `humanizer` en mode embedded ;
2. `general-writing` pour clarté, précision et voix ;
3. `anti-ai-slop` pour le contrôle final du caractère purpose-built.

Ne pas utiliser `natural-writing` comme étape obligatoire pour ces pages françaises.

La finition peut modifier structure et prose, mais ne peut jamais ajouter un fait, une disponibilité, un prix ou une réduction absents des preuves.

Contrôler particulièrement :

- intro qui reformule le H1 ;
- blocs d'offres mécaniquement symétriques ;
- répétition « pourquoi c'est un bon plan / pour qui / verdict » ;
- urgence artificielle ;
- transitions génériques ;
- même structure que les pages marque ou événement voisines ;
- conclusion qui répète seulement les prix ;
- vocabulaire publicitaire excessif.

---

# 9. Maillage — `internal-linking-audit`

Ajouter uniquement les liens qui répondent à une prochaine question logique :

- produit ou marque pour comprendre l'écosystème ;
- comparatif pour choisir entre plusieurs produits ;
- guide pour un critère/procédure ;
- usage pour un contexte précis ;
- autre page Bons plans seulement si son rôle est réellement complémentaire.

Aucun quota de liens.

---

# 10. SEO

Utiliser :

- `seo-onpage` pour title, meta, H1, contenu, maillage, URL, canonical et schema honnête ;
- `seo-technical` pour robots, crawlabilité, canonical, HTML et structured data ;
- `seo-drift` uniquement lorsqu'un baseline ou une régression utile existe.

Éviter qu'une page d'événement périmée cannibalise une page evergreen sans justification éditoriale.

Aucun nombre de mots, headings, offres, tableaux ou liens n'est un KPI de qualité.

---

# 11. QA générique — `editorial-qa`

La page doit passer les contrôles d'intention, valeur originale, factualité, naturel, SEO, utilité réelle et indépendance vis-à-vis de l'affiliation.

Un contenu avec des prix exacts peut encore échouer s'il est purement marchand, trop promotionnel ou sans valeur décisionnelle.

---

# 12. Gate final — `deal-analysis-workflow` / `PUBLISH_REVIEW`

Une fois le draft stable, appeler :

`.agents/skills/deal-analysis-workflow/SKILL.md` en mode `PUBLISH_REVIEW`.

Cette étape :

- exécute `python3 validate_deal_workflow.py` ;
- recontrôle les offres, statuts, prix de référence et TTL ;
- vérifie les preuves et l'intention ;
- compare la structure aux pages sœurs ;
- cherche les contradictions et l'industrialisation éditoriale ;
- vérifie les blockers propres aux pages Bons plans.

Résultat attendu avant validation humaine :

`PASS — READY_FOR_HUMAN_VALIDATION`

Sinon :

`FAIL — KEEP_NOINDEX`

En cas de FAIL éditorial, utiliser le nouveau `CONTENT_HANDOFF` produit par l'analyse pour corriger uniquement les gates en échec.

---

# 13. Persistance

Conserver dans `.content/deals/<slug>.json` au minimum les éléments réellement utilisés :

- intention et rôle ;
- type de page ;
- `checked_at` ;
- fraîcheur ;
- offres et statuts ;
- prix de référence et leur base ;
- evidence ledger ;
- watchlist ;
- décisions éditoriales importantes ;
- résultat d'audit ;
- résultat du `PUBLISH_REVIEW`.

Le HTML final ne doit jamais être l'unique endroit où prix et preuves sont documentés.

---

# 14. Indexation

Conserver `noindex,follow` par défaut.

Le workflow ne retire jamais `noindex` automatiquement.

Indexation uniquement après :

1. `validate_deal_workflow.py` sans blocker ;
2. `deal-analysis-workflow / PUBLISH_REVIEW` = `PASS — READY_FOR_HUMAN_VALIDATION` ;
3. validation humaine explicite ;
4. instruction explicite de rendre la page indexable.

---

# 15. Résumé de l'orchestration

```text
PAGE EXISTANTE
  deal-analysis-workflow / AUDIT
        ↓
CONTENT_HANDOFF si LIGHT_UPDATE ou DEEP_REWRITE
        ↓
seo-keyword + search-intent
        ↓
seo-content-audit + content-refresh si nécessaire
        ↓
fact-check + registre .content/deals
        ↓
preuve de prix / statut / fraîcheur
        ↓
evidence-based-reviews si jugement expérientiel
        ↓
affiliate-value
        ↓
content-brief-authoring
        ↓
content-and-copy
        ↓
fact-check post-draft
        ↓
humanizer → general-writing → anti-ai-slop
        ↓
internal-linking-audit
        ↓
seo-onpage + seo-technical
        ↓
editorial-qa
        ↓
deal-analysis-workflow / PUBLISH_REVIEW
        ↓
validation humaine
```

Le workflow orchestre ; il ne remplace pas les skills spécialisés et ne contourne jamais la preuve de l'offre.
