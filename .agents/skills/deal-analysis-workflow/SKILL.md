---
name: deal-analysis-workflow
description: Workflow unique d'analyse des pages /bons-plans/ de bloc-notes-numeriques.fr. Audite une URL ou le cluster, contrôle intention, fraîcheur, preuve de prix, validité des offres, valeur affiliée, frontières éditoriales, industrialisation et SEO, puis décide KEEP, LIGHT_UPDATE, DEEP_REWRITE, MERGE ou NOINDEX. En PUBLISH_REVIEW, sert de gate final avant validation humaine et peut générer un handoff de correction vers deal-content-workflow.
metadata:
  adapted_for: bloc-notes-numeriques.fr
  orchestration_target: ">=80% existing GitHub skills"
  custom_scope: "orchestration + deal integrity + freshness + cluster similarity"
---

# Deal Analysis Workflow

## Rôle

C'est le **seul workflow d'analyse** à utiliser pour les URLs sous `/bons-plans/`.

Il ne rédige pas la page. Il orchestre en priorité les skills spécialisés déjà présents dans le dépôt et ajoute uniquement les contrôles propres à un contenu de promotion : existence réelle de l'offre, fraîcheur, prix de référence, économie défendable et cohérence entre l'offre et le produit.

Séparation des responsabilités :

- `deal-analysis-workflow` = diagnostiquer, comparer le cluster, décider et effectuer le publish review ;
- `deal-content-workflow` = créer ou corriger la page uniquement lorsqu'un audit ou une demande de création le justifie.

Principe central :

> **Une page Bons plans doit prouver l'offre avant de la promouvoir. Le workflow juge d'abord la fiabilité et l'utilité de l'information commerciale, pas la quantité de remises affichées.**

---

# 1. Modes

## `AUDIT`

Mode par défaut pour une URL existante.

Retourne un diagnostic, une décision et, uniquement si une correction est nécessaire, un `CONTENT_HANDOFF` destiné au `deal-content-workflow`. Il ne modifie pas le texte.

L'audit individuel doit également regarder les pages sœurs pertinentes lorsque le risque de chevauchement, de deal périmé ou de structure clonée existe.

## `CLUSTER_AUDIT`

Analyse plusieurs URLs `/bons-plans/` ensemble afin de détecter :

- intentions identiques ou trop proches ;
- mêmes offres répétées sans rôle distinct ;
- pages événementielles périmées qui concurrencent une page evergreen ;
- pages marque qui doublonnent un hub général ;
- contenus d'occasion/reconditionné qui devraient avoir un rôle séparé ;
- offres actives incohérentes entre plusieurs pages ;
- différences de prix ou de statut non expliquées pour un même produit ;
- architecture éditoriale industrialisée ;
- pages sans offre active qui n'apportent plus de valeur autonome.

Le mode cluster ne déclenche aucune réécriture automatiquement.

## `PUBLISH_REVIEW`

Gate final après création ou correction via `deal-content-workflow`.

Il exécute le validateur machine, rejoue les contrôles substantiels et retourne exactement :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Un PASS n'autorise jamais à retirer `noindex,follow` sans validation humaine et instruction explicite.

---

# 2. Entrées

Lire selon disponibilité :

- `AGENTS.md` ;
- `deal-workflow.config.yaml` ;
- la page cible et les pages Bons plans voisines ;
- `.content/deals/<slug>.json` et les autres registres de deals pertinents ;
- `references/promo-evidence.md` du `deal-content-workflow` ;
- pages marques, produits, comparatifs, guides et usages nécessaires pour vérifier le contexte produit ;
- données GSC, sémantiques ou historiques lorsqu'elles existent ;
- SERP actuelle si l'intention ou la saisonnalité est incertaine ;
- sources actuelles pour prix, disponibilité, événements, bundles et conditions commerciales.

Ne jamais compléter un prix, une remise, une disponibilité ou un statut avec la mémoire du modèle. Une donnée non vérifiée reste inconnue ou change de statut.

---

# 3. Chaîne de skills réutilisés — source principale de l'analyse

Le workflow doit d'abord exécuter les skills existants. Ne pas recopier leurs méthodologies dans ce fichier.

## 3.1 `seo-content-audit`

Utiliser `.agents/skills/seo-content-audit/SKILL.md` pour déterminer si l'URL mérite d'être conservée, mise à jour, consolidée ou retirée du cluster.

Ce skill porte la logique amont `KEEP / UPDATE / MERGE / REDIRECT / DELETE`. Les actions destructives restent des recommandations tant que l'utilisateur ne les demande pas explicitement.

## 3.2 `seo-keyword` + `search-intent`

Confirmer lorsque les données le permettent :

- requête ou cluster principal ;
- intention dominante ;
- besoin immédiat : acheter maintenant, surveiller un prix, préparer un événement, chercher de l'occasion/reconditionné ;
- rôle unique de l'URL ;
- chevauchement avec une autre page Bons plans ou un comparatif.

Les données GSC/sémantiques et la SERP actuelle priment sur le slug.

## 3.3 `content-refresh`

Uniquement lorsqu'une mise à jour est nécessaire. Diagnostiquer notamment : obsolescence, intent drift, thin value, merchant duplication, faiblesse structurelle, cannibalisation, prose générique et trust gap.

Le présent workflow mappe ensuite le besoin vers `LIGHT_UPDATE` ou `DEEP_REWRITE`.

## 3.4 `fact-check`

Vérifier les claims importants :

- produit et variante exacts ;
- vendeur ;
- prix actuel ;
- disponibilité ;
- frais ou conditions connus ;
- bundle ;
- prix de référence ;
- dates de début/fin lorsqu'elles existent ;
- état d'une offre, d'un événement ou d'une annonce ;
- compatibilités et caractéristiques produit utilisées pour justifier la pertinence du deal.

Une affirmation plausible mais non sourcée reste non vérifiée.

## 3.5 `affiliate-value`

Vérifier que la page reste utile sans liens affiliés. Une bonne page Bons plans doit apporter une lecture éditoriale : remise réellement intéressante ou non, limites, seuil de prix, contexte, alternatives, situations où attendre est préférable et risques liés à l'occasion/reconditionné lorsque pertinent.

## 3.6 `evidence-based-reviews`

Conditionnel. L'utiliser uniquement lorsqu'un jugement sur qualité, ergonomie, autonomie observée, fiabilité ou expérience produit dépasse ce que les specs officielles permettent d'établir.

Une promotion ne justifie jamais un faux test ou un jugement produit sans niveau de preuve adapté.

## 3.7 `internal-linking-audit`

Vérifier que la page renvoie vers la prochaine question logique : page produit/marque, comparatif, guide, usage, alternative ou autre deal réellement complémentaire. Aucun quota.

## 3.8 `anti-ai-slop`

Utiliser en review/detection pour rechercher : formulations promotionnelles génériques, faux sentiment d'urgence, répétition de blocs, pages marque clonées, événements recyclés et structure interchangeable.

## 3.9 SEO

- `seo-onpage` : title, meta, H1, structure, maillage, canonical, URL et schema honnête ;
- `seo-technical` : robots, crawlabilité, canonical, HTML et données structurées réellement applicables ;
- `seo-drift` : uniquement si un baseline avant/après existe et apporte une information utile.

Aucun quota de mots, headings, offres, liens ou sources ne sert de proxy de qualité.

## 3.10 `editorial-qa`

Dernière QA générique : intention, valeur originale, factualité, naturel, SEO, utilité et indépendance vis-à-vis de l'affiliation.

---

# 4. Couche custom n°1 — intégrité de l'offre

Les statuts autorisés restent ceux de `deal-workflow.config.yaml` :

- `ACTIVE_VERIFIED`
- `ACTIVE_STOCK_SENSITIVE`
- `PRICE_WATCH`
- `EXPIRED`
- `SOLD_OUT`
- `UNVERIFIED`
- `NOT_STARTED`

Pour chaque offre mentionnée dans le HTML, vérifier qu'elle existe dans `.content/deals/<slug>.json` et que son statut permet la formulation utilisée.

## Offre active

Une offre `ACTIVE_VERIFIED` doit au minimum avoir :

- produit/variante identifiables ;
- `merchant` ;
- `price` ;
- `currency` ;
- `checked_at` ;
- `source` ;
- disponibilité suffisamment confirmée pour le niveau d'affirmation publié.

`ACTIVE_STOCK_SENSITIVE` impose une formulation prudente lorsque le stock, le pays, les frais ou le checkout peuvent modifier l'offre.

## Offre non active

- `PRICE_WATCH` = prix observé, mais promotion non prouvée ;
- `EXPIRED` = ne doit pas conserver de CTA ou formulation d'urgence comme si l'offre était active ;
- `SOLD_OUT` = ne doit pas être présenté comme achetable ;
- `UNVERIFIED` = ne doit pas devenir une affirmation commerciale ;
- `NOT_STARTED` = l'événement futur doit être clairement présenté comme futur.

Le HTML ne peut jamais être plus affirmatif que le registre de preuve.

---

# 5. Couche custom n°2 — prix de référence et économie réelle

Une remise n'est publiable comme telle que si le prix de référence est documenté.

Ordre de préférence :

1. prix constructeur actuel hors promotion ;
2. prix constructeur précédent clairement daté ;
3. somme documentée des éléments d'un bundle ;
4. historique de prix fourni par une source spécialisée ;
5. prix barré marchand uniquement comme signal secondaire.

Vérifier :

- même produit, même variante et configuration comparable ;
- prix de référence encore pertinent ;
- frais ou éléments obligatoires qui changent le coût réel ;
- pourcentage recalculé depuis les valeurs documentées lorsqu'il est affiché ;
- absence de termes comme « prix historique », « meilleur prix », « record » sans historique suffisant.

Un prix inférieur n'est pas automatiquement une bonne affaire si la référence est artificielle, le bundle incomplet ou le produit peu pertinent.

---

# 6. Couche custom n°3 — fraîcheur

Appliquer `deal-workflow.config.yaml`.

Repères actuels du dépôt :

- `LIVE_DEALS` : offre active 48 h ; revue de page 7 jours ;
- `BRAND_DEALS` : offre active 72 h ; revue de page 7 jours ;
- `EVENT_DEALS` : offre active 24 h ; revue de page 14 jours ;
- `SECOND_HAND` : offre active 72 h ; revue de page 14 jours.

Une offre qui dépasse son TTL ne doit plus être présentée comme active sans nouvelle vérification.

La récence seule ne suffit pas : un `checked_at` récent associé à une source faible ne transforme pas un signal en preuve.

En cas d'événement commercial, vérifier aussi que la page distingue clairement : avant l'événement, pendant l'événement et après l'événement.

---

# 7. Couche custom n°4 — rôle de page et frontières éditoriales

Les types de page servent de grilles de risque, pas de templates :

- `LIVE_DEALS` : répondre à « quelles offres sont réellement intéressantes maintenant ? » ;
- `BRAND_DEALS` : suivre les offres d'une marque/gamme sans refaire la page marque ;
- `EVENT_DEALS` : couvrir une période commerciale avec une logique temporelle explicite ;
- `SECOND_HAND` : aider à acheter d'occasion/reconditionné avec contrôle de l'état, du canal, de la garantie et du risque lorsque ces données sont disponibles.

Frontières :

- si la question devient « quel produit choisir ? » → `/comparatifs/` ;
- si elle devient « que vaut ce produit ou cette marque ? » → `/marques/` ;
- si elle devient « comment choisir ou utiliser ? » → `/guides/` ;
- si elle porte sur un contexte de travail précis → `/usages/`.

Une page Bons plans peut rappeler brièvement pourquoi une offre est pertinente, mais ne doit pas reconstruire un comparatif complet pour justifier le CTA.

---

# 8. Couche custom n°5 — cluster et industrialisation

En `AUDIT`, comparer la cible aux pages Bons plans les plus proches. En `CLUSTER_AUDIT` et `PUBLISH_REVIEW`, regarder le sous-cluster pertinent dans son ensemble.

Chercher notamment :

- mêmes offres copiées dans plusieurs pages sans rôle distinct ;
- mêmes H2 fonctionnels dans le même ordre pour toutes les marques ;
- mêmes phrases « pourquoi c'est une bonne affaire / faut-il craquer / notre verdict » ;
- mêmes blocs promotionnels avec simple substitution de marque/prix ;
- même conclusion d'urgence ;
- événements annuels recyclés sans mise à jour substantielle ;
- une page sans offre active qui conserve artificiellement une structure de deal live ;
- contradictions de prix/statut entre pages sœurs ;
- cannibalisation entre hub général, pages marque et pages événement.

Les composants visuels partagés sont normaux. Le problème apparaît lorsque **la pensée éditoriale et la qualification du deal semblent produites par un squelette réutilisé plutôt que par les preuves de l'offre et l'intention**.

Une industrialisation substantielle peut déclencher `DEEP_REWRITE`.

---

# 9. Décisions `AUDIT` / `CLUSTER_AUDIT`

## `KEEP`

Page distincte, utile, actuelle et correctement documentée. Les offres et formulations sont cohérentes avec les preuves. Aucun changement substantiel.

## `LIGHT_UPDATE`

Corrections ciblées : revalidation d'offres, changement de statut, prix ou date, retrait d'un CTA périmé, correction de source, title/meta, maillage, formulation trop promotionnelle ou quelques passages. L'architecture fondamentale reste pertinente.

## `DEEP_REWRITE`

Réserver aux problèmes structurants :

- intention ou rôle mal cadré ;
- majorité des offres obsolètes ou non défendables ;
- prix de référence central non fiable ;
- page devenue essentiellement une copie de marchand ;
- valeur éditoriale trop faible sans affiliation ;
- cannibalisation forte ;
- architecture fortement industrialisée ;
- événement périmé dont la page doit être repensée pour conserver une utilité ;
- distinction insuffisante entre deal, comparatif et page marque.

`DEEP_REWRITE` ne signifie pas tout jeter : préserver les faits, sources, seuils, explications, liens et passages encore valides identifiés par l'audit.

## `MERGE`

Une autre URL sert essentiellement la même intention ou les mêmes offres. Indiquer la cible recommandée, sans merger ni rediriger automatiquement.

## `NOINDEX`

La page n'a pas encore assez de valeur, de preuve ou de fraîcheur pour être indexée. Une page peut rester utile comme brouillon/veille interne sans être publiable.

Pour chaque décision fournir :

- confiance ;
- valeur existante à préserver ;
- preuves utilisées ;
- offres et statuts concernés ;
- unknowns importants ;
- blockers ;
- améliorations secondaires ;
- risques de cannibalisation ;
- prochaine étape.

---

# 10. Handoff vers la rédaction/correction

Le handoff est **obligatoire uniquement pour `LIGHT_UPDATE` et `DEEP_REWRITE`**.

- `KEEP` → aucune rédaction ;
- `LIGHT_UPDATE` → `deal-content-workflow` avec scope strictement limité ;
- `DEEP_REWRITE` → `deal-content-workflow` avec reconstruction guidée par l'intention et les preuves ;
- `MERGE` / `NOINDEX` → décision humaine avant action structurelle.

Produire le bloc suivant :

```text
CONTENT_HANDOFF
workflow: deal-content-workflow
decision: LIGHT_UPDATE | DEEP_REWRITE
target_url: <url>
intent_to_preserve_or_fix: <...>
value_to_preserve:
- <...>
mandatory_fixes:
- <...>
offers_to_revalidate_or_reclassify:
- <offer> -> <required check/status>
claims_or_prices_to_recheck:
- <...>
required_sources_or_evidence:
- <...>
cluster_conflicts_to_resolve:
- <...>
seo_or_internal_linking_changes:
- <...>
do_not_change_unless_new_evidence:
- <...>
expected_end_state: <...>
```

Puis fournir ce prompt de production :

```text
Utilise `.agents/skills/deal-content-workflow/SKILL.md` pour corriger ou réécrire la page cible à partir du `CONTENT_HANDOFF` ci-dessus.
Respecte le niveau de changement décidé par l'audit : ne transforme pas un `LIGHT_UPDATE` en réécriture complète.
Préserve explicitement les éléments listés dans `value_to_preserve` et `do_not_change_unless_new_evidence`.
Revalide toute offre, tout prix et toute disponibilité demandés avant de les publier.
Ne transforme jamais un prix observé en promotion sans prix de référence documenté.
Après la correction, exécute le fact-check, les passes éditoriales/SEO prévues par le workflow puis `deal-analysis-workflow` en mode `PUBLISH_REVIEW`.
Conserve `noindex,follow` jusqu'à validation humaine explicite.
```

Ce prompt est un **handoff**, pas un second workflow de rédaction.

---

# 11. Mode `PUBLISH_REVIEW`

Exécuter uniquement sur une version considérée terminée.

## Étape A — validation machine

Exécuter :

```bash
python3 validate_deal_workflow.py
```

Le validateur machine vérifie uniquement les blockers détectables automatiquement : registres attendus, statuts, champs obligatoires, dates, preuves minimales, présence du HTML et conservation du `noindex`.

Un PASS machine n'est qu'un plancher structurel.

## Étape B — gates substantiels

Réexécuter les skills pertinents et vérifier au minimum :

- intention réellement satisfaite ;
- offre active réellement vérifiée lorsqu'elle est présentée comme active ;
- statut du registre cohérent avec le HTML ;
- prix de référence défendable pour tout claim de remise ;
- pourcentage ou économie calculés depuis des valeurs documentées ;
- fraîcheur conforme au TTL ;
- aucune offre périmée ou sold-out présentée comme achetable ;
- aucune fausse urgence, faux compte à rebours ou faux « meilleur prix » ;
- produit/variante exacts et contexte produit suffisant ;
- aucune recommandation dictée par la commission ;
- valeur réelle même sans liens affiliés ;
- aucune transformation en comparatif produit ;
- aucun faux test ni faux hands-on ;
- pas de cannibalisation non résolue ;
- pas de signal `HIGH` d'AI-slop ;
- architecture spécifique à l'intention et aux offres ;
- absence de clonage structurel substantiel avec les pages sœurs ;
- title/H1/canonical/robots/liens/schema cohérents ;
- transparence affiliée et `rel="sponsored"` lorsque nécessaire.

## Étape C — résultat

### PASS

Retourner exactement :

`PASS — READY_FOR_HUMAN_VALIDATION`

Lister uniquement les risques mineurs restants, s'il y en a.

### FAIL

Retourner exactement :

`FAIL — KEEP_NOINDEX`

Lister les gates en échec et router vers le skill ou la passe qui doit corriger le problème. Si les corrections sont éditoriales, générer un nouveau `CONTENT_HANDOFF` limité aux échecs constatés.

Un FAIL ne déclenche jamais automatiquement une réécriture totale.

---

# 12. Indexation

Conserver `noindex,follow` par défaut.

Indexation uniquement après :

1. aucun blocker dans `validate_deal_workflow.py` ;
2. `PUBLISH_REVIEW` = `PASS — READY_FOR_HUMAN_VALIDATION` ;
3. validation humaine explicite ;
4. instruction explicite de rendre la page indexable.

---

# 13. Répartition 80/20

La méthodologie doit venir majoritairement des skills existants :

- Rampstack : `seo-content-audit`, `seo-keyword`, `seo-onpage` ;
- intention/refresh : `search-intent`, `content-refresh` ;
- preuve/confiance : `fact-check`, `evidence-based-reviews` si nécessaire, `affiliate-value` ;
- stack éditoriale : `internal-linking-audit`, `humanizer`, `general-writing`, `anti-ai-slop`, `editorial-qa` ;
- contrôle technique : `seo-technical` et, seulement si utile, `seo-drift`.

La couche custom se limite à :

1. orchestration et mapping des décisions ;
2. intégrité offre/prix/fraîcheur ;
3. frontières avec comparatifs, marques, guides et usages ;
4. contrôle de cohérence et de similarité du cluster ;
5. handoff de correction vers `deal-content-workflow`.

---

# 14. Ce que ce workflow ne doit pas devenir

Ne pas ajouter :

- quota de mots ;
- nombre minimum de H2/H3 ;
- nombre minimum d'offres ;
- quota de liens ou de sources ;
- FAQ obligatoire ;
- score artificiel de qualité ;
- template fixe par type de deal ;
- générateur de texte ;
- détection d'auteur IA ;
- duplication des méthodes déjà maintenues dans les skills spécialisés.

Sa valeur est l'orchestration, la décision, le contrôle temporel et le contrôle inter-pages propres au cluster Bons plans.
