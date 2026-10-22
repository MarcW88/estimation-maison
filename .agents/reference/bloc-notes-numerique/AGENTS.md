# Instructions du dépôt

Ce dépôt contient le site éditorial et d’affiliation bloc-notes-numeriques.fr.

## Design

Pour toute création, modification ou revue de l’interface :

1. Lire `DESIGN.md` avant de modifier le frontend.
2. Utiliser le skill `.agents/skills/site-design-review/SKILL.md` pour toute demande d’audit, de critique, de polish ou de validation visuelle.
3. Préserver une esthétique de média éditorial spécialisé. Ne pas transformer le site en landing page SaaS, en catalogue e-commerce ou en comparateur affilié agressif.
4. Réutiliser les composants et tokens existants avant d’en créer de nouveaux.
5. Vérifier au minimum les rendus mobile et desktop lorsque l’environnement permet de lancer le site.
6. Lors d’un audit, ne pas corriger automatiquement les problèmes sauf si la demande inclut explicitement l’implémentation.

## Qualité et confiance

- Distinguer clairement le contenu éditorial des liens affiliés.
- Ne pas inventer de tests, mesures, prix, avis utilisateurs ou expériences produit.
- Afficher les limites et le niveau de preuve aussi clairement que les avantages.
- Conserver une hiérarchie HTML sémantique et une navigation accessible.
- Respecter les commandes de build, lint et test définies par le projet lorsqu’elles seront disponibles.

## Production éditoriale — Guides

Pour toute URL sous `/guides/`, il n’existe que deux workflows Guide à choisir :

1. **Analyser / auditer** : `.agents/skills/guide-analysis-workflow/SKILL.md`.
2. **Créer / réécrire** : `.agents/skills/guide-content-workflow/SKILL.md`.

Ces deux fichiers sont des **orchestrateurs**. La méthodologie doit venir majoritairement des skills GitHub spécialisés déjà présents dans le dépôt, notamment `seo-content-audit`, `seo-keyword`, `search-intent`, `content-refresh`, `fact-check`, `evidence-based-reviews` lorsque nécessaire, `affiliate-value`, `content-brief-authoring`, `content-and-copy`, `internal-linking-audit`, `humanizer`, `general-writing`, `anti-ai-slop`, `seo-onpage`, `seo-technical` et `editorial-qa`. Ne pas recopier leurs méthodes dans un workflow Guide custom.

### Règles obligatoires

1. Une page existante passe d’abord par `guide-analysis-workflow` en mode `AUDIT` avant une réécriture substantielle.
2. `guide-analysis-workflow` possède les trois modes `AUDIT`, `CLUSTER_AUDIT` et `PUBLISH_REVIEW`.
3. Les types `CHOICE`, `EXPLAINER` et `HOW_TO` sont des grilles de risques, jamais des templates éditoriaux. Un guide peut être hybride.
4. Le plan final est construit après l’intention, les preuves et le périmètre. Aucun type de guide n’impose un ordre de sections, un nombre de H2/H3, un tableau, une FAQ, une checklist ou un nombre d’étapes.
5. Respecter les frontières : `/guides/` explique ou rend une tâche faisable ; `/usages/` traite un job et ses circonstances ; `/comparatifs/` choisit entre des produits ; `/marques/` documente un écosystème, une gamme ou un produit.
6. Pour un `CHOICE`, aider à arbitrer sans fabriquer un podium produit. Pour un `EXPLAINER`, relier mécanisme et conséquence pratique. Pour un `HOW_TO`, publier uniquement des étapes vérifiables et distinguer les versions/plateformes lorsque nécessaire.
7. Adapter la fraîcheur au risque : logiciel, cloud, abonnement, compatibilité, prix, génération produit et procédures doivent être vérifiés actuellement ; un mécanisme stable n’a pas besoin d’une récence artificielle mais doit rester exact.
8. Ne jamais remplir un trou de preuve avec la connaissance du modèle. Une information inconnue reste inconnue, est qualifiée ou est retirée.
9. Utiliser `evidence-based-reviews` seulement lorsqu’un jugement expérientiel produit le nécessite. Ne pas transformer un guide documentaire en faux test.
10. La page doit rester utile si tous les liens affiliés disparaissent et ne doit pas se réduire à une reformulation marchande.
11. Comparer la structure aux guides voisins : mêmes fonctions de H2, mêmes tableaux, mêmes procédures, mêmes CTA ou mêmes conclusions sans justification constituent un signal d’industrialisation et peuvent imposer `DEEP_REWRITE`.
12. Pour une page existante, `guide-content-workflow` doit préserver la valeur identifiée par l’audit et limiter les changements au scope nécessaire pour `LIGHT_UPDATE`.
13. Après rédaction, exécuter la chaîne définie dans `guide-content-workflow`, puis `guide-analysis-workflow` en mode `PUBLISH_REVIEW`.
14. `validate_guide_quality.py` ne contrôle que les blockers détectables automatiquement. Il ne peut imposer ni minimum de mots, ni nombre de H2/H3, ni quota de liens ou de sources.
15. Le `PUBLISH_REVIEW` doit se terminer par `PASS — READY_FOR_HUMAN_VALIDATION` avant validation humaine.
16. Ne retirer `noindex` qu’après validation humaine explicite **et** instruction explicite de rendre la page indexable.
17. Aucun quota de mots, H2/H3, tableaux, étapes, FAQ, liens internes ou sources ne peut servir de proxy de qualité.

## Production éditoriale — Pages Par usage

Pour toute création ou réécriture sous `/usages/` :

1. Utiliser `.agents/skills/usage-content-workflow/SKILL.md`.
2. Utiliser `.agents/skills/jobs-to-be-done/SKILL.md` pendant la pré-analyse afin de partir des circonstances, du progrès recherché et du workflow réel plutôt que d’un persona générique ou d’une liste de fonctionnalités.
3. Créer ou mettre à jour `.content/usages/<slug>.json` avant la rédaction ; ce fichier est la source de vérité du cadrage usage.
4. Respecter la frontière éditoriale : `/usages/` explique le besoin et les critères ; `/comparatifs/` classe les produits ; `/guides/` explique une technologie, un critère ou une procédure ; `/marques/` documente un écosystème ou un produit.
5. Ne pas faire de scoring ou de ranking produit dans une page usage. Si un classement devient nécessaire, passer la main à `comparison-content-workflow`.
6. Distinguer `OBSERVED`, `SUPPORTED`, `INFERRED`, `HYPOTHESIS` et `UNKNOWN`. Ne jamais présenter une motivation supposée comme un comportement utilisateur observé.
7. Considérer les alternatives hors E Ink et les situations où le bloc-notes numérique n’est pas le bon outil.
8. Conserver `noindex,follow` jusqu’à validation humaine explicite.
9. Après rédaction, exécuter la chaîne de QA définie dans `usage-content-workflow`, y compris le contrôle anti-cannibalisation avec les comparatifs et guides proches.

## Production éditoriale — Comparatifs

Pour toute URL sous `/comparatifs/`, il n’existe que deux workflows comparison à choisir :

1. **Analyser / auditer** : `.agents/skills/comparison-analysis-workflow/SKILL.md`.
2. **Créer / réécrire** : `.agents/skills/comparison-content-workflow/SKILL.md`.

Ces deux fichiers sont des **orchestrateurs**. La méthodologie doit venir majoritairement des skills GitHub spécialisés déjà présents dans le dépôt, notamment `seo-content-audit`, `seo-keyword`, `jobs-to-be-done`, `evidence-based-reviews`, `content-brief-authoring`, `content-and-copy`, `seo-onpage`, `humanizer`, `general-writing` et `anti-ai-slop`. Ne pas recopier leurs méthodes dans un nouveau workflow custom.

### Règles obligatoires

1. Une page existante passe d’abord par `comparison-analysis-workflow` en mode `AUDIT` avant une réécriture substantielle.
2. L’analyse juge d’abord **la qualité de la décision offerte au lecteur**, pas la sophistication apparente de la méthodologie.
3. Le scope doit contenir les choix plausibles pour la requête. Il n’est pas nécessaire de documenter tout le marché ; une exclusion importante est expliquée seulement lorsqu’elle peut changer la conclusion.
4. Les critères sont définis avant la recommandation et découlent de l’intention, du JTBD lorsque pertinent et des différences réelles entre produits.
5. Le scoring, la pondération, les hard gates, l’Equivalence Engine et le Total Solution Cost sont **optionnels**. Les utiliser uniquement lorsqu’ils rendent la décision plus claire.
6. Si un score existe, le présenter comme un jugement éditorial sauf mesure réelle. Une spec vérifie un fait ; elle ne prouve pas automatiquement une sensation d’usage. Éviter la fausse précision.
7. Utiliser `evidence-based-reviews` pour adapter le niveau de preuve au claim : specs officielles pour les faits, sources propriétaires/utilisateurs ou tests experts pour les jugements qui en ont besoin, hands-on uniquement lorsqu’il existe réellement.
8. Ne jamais remplir un trou de preuve avec la connaissance du modèle. Une donnée absente reste inconnue ou est qualifiée.
9. Aucun produit n’est inclus ou favorisé parce qu’il possède un meilleur lien ou une meilleure commission d’affiliation.
10. Le verdict doit être traçable aux critères et aux preuves et préciser quand un autre choix devient meilleur. Un `HEAD_TO_HEAD` peut parfaitement conclure « X si…, Y si… » sans gagnant universel.
11. Pour une intention fortement budgétaire, comparer une configuration réellement utilisable. Pour les autres pages, ne pas imposer un calcul de coût complexe s’il ne change pas la décision.
12. Le plan final est construit **après** l’intention, les preuves et la logique de recommandation. Aucun type de comparatif n’impose un ordre de sections, un nombre de H2/H3, un tableau, une FAQ ou des fiches produits symétriques.
13. Comparer la structure aux comparatifs voisins : mêmes H2 fonctionnels, mêmes blocs produit, mêmes arguments et mêmes conclusions sous des intentions différentes constituent un signal de production industrialisée.
14. `DEEP_REWRITE` est réservé aux problèmes réellement structurants : intention/role mal cadré, sélection inadéquate, recommandation injustifiable, faible valeur originale, obsolescence majeure ou architecture fortement industrialisée. L’absence de scoring complexe n’est jamais à elle seule un motif de `DEEP_REWRITE`.
15. La page doit rester utile si tous les liens affiliés disparaissent et doit montrer les limites significatives des recommandations.
16. Après rédaction, exécuter la chaîne définie dans `comparison-content-workflow`, puis `comparison-analysis-workflow` en mode `PUBLISH_REVIEW`.
17. `validate_comparisons.py` contrôle uniquement les blockers détectables automatiquement. Scoring, poids et ranking sont optionnels ; lorsqu’ils existent, le validateur contrôle leur cohérence.
18. Le `PUBLISH_REVIEW` doit se terminer par `PASS — READY_FOR_HUMAN_VALIDATION` avant validation humaine.
19. Ne retirer `noindex` qu’après validation humaine explicite **et** instruction explicite de rendre la page indexable.
20. Aucun quota de mots, H2/H3, tableaux ou liens internes ne peut servir de proxy de qualité.

## Production éditoriale — Pages marques

Pour toute URL sous `/marques/`, il n’existe que deux workflows brand à choisir :

1. **Analyser / auditer** : `.agents/skills/brand-analysis-workflow/SKILL.md`.
2. **Créer / réécrire** : `.agents/skills/brand-content-workflow/SKILL.md`.

Les skills transversaux appelés par ces workflows (`content-audit`, `search-intent`, `affiliate-value`, `fact-check`, `evidence-based-reviews`, `humanizer`, `general-writing`, `anti-ai-slop`, etc.) sont des briques internes. Ne pas créer un nouveau workflow brand lorsqu’un de ces skills couvre déjà l’étape.

### Règles obligatoires

1. Une page existante doit passer par `brand-analysis-workflow` en mode `AUDIT` avant une réécriture substantielle.
2. Déterminer le type `DIRECTORY`, `BRAND_HUB`, `PRODUCT`, `REVIEW`, `SERVICE`, `ACCESSORY_HUB` ou `ALTERNATIVES`, mais utiliser ce type uniquement comme grille de risque et de frontière éditoriale. **Le type de page ne doit jamais imposer un plan, un ordre de sections, un nombre de H2/H3, un tableau ou une FAQ.**
3. Le plan final doit être construit après l’analyse d’intention et le research/evidence brief. Chaque section doit être justifiable par une question du lecteur et des preuves disponibles.
4. Utiliser des sources fiables et actuelles. Pour les facts produits : fabricant/documentation en priorité ; sources indépendantes pour les jugements ; plusieurs sources utilisateurs seulement pour des patterns suffisamment documentés.
5. Ne jamais remplir un trou de preuve avec la connaissance du modèle. Une information reste `UNKNOWN`, est qualifiée ou est supprimée.
6. Toute recommandation doit distinguer faits vérifiés, interprétation éditoriale, synthèse d’autres sources et expérience réelle. Sans test physique documenté, aucune review ne peut imiter un test hands-on.
7. La page doit conserver une vraie valeur si tous les liens affiliés sont supprimés. Ne pas recopier ou simplement reformuler le fabricant ou un retailer.
8. Comparer la structure avec les pages sœurs : une architecture éditoriale répétée sans justification par l’intention ou les preuves est un signal de production industrialisée et peut imposer `DEEP_REWRITE`.
9. Éviter tout métadiscours destiné à l’éditeur dans le texte utilisateur : SEO, GEO, hub, maillage, intention de recherche, architecture de page ou stratégie éditoriale.
10. Après rédaction, exécuter la chaîne définie dans `brand-content-workflow`, puis `brand-analysis-workflow` en mode `PUBLISH_REVIEW`.
11. `validate_brands.py` contrôle uniquement les blockers détectables automatiquement. Un PASS machine ne signifie jamais que la page est publiable.
12. Le `PUBLISH_REVIEW` doit se terminer par `PASS — READY_FOR_HUMAN_VALIDATION`. Un seul blocker maintient la page en `noindex,follow`.
13. Ne retirer `noindex` qu’après validation humaine explicite **et** instruction explicite de rendre la page indexable.
14. Aucun quota de mots, H2/H3, tableaux ou liens internes ne peut servir de proxy de qualité.

## Production éditoriale — Bons plans

Pour toute URL sous `/bons-plans/`, il n’existe que deux workflows Deal à choisir :

1. **Analyser / auditer** : `.agents/skills/deal-analysis-workflow/SKILL.md`.
2. **Créer / corriger / réécrire** : `.agents/skills/deal-content-workflow/SKILL.md`.

Ces deux fichiers sont des **orchestrateurs**. La méthodologie doit venir majoritairement des skills spécialisés déjà présents dans le dépôt. La couche custom doit rester limitée à l’intégrité de l’offre, la preuve de prix, la fraîcheur, les frontières éditoriales et la cohérence du cluster.

### Règles obligatoires

1. Une page existante passe d’abord par `deal-analysis-workflow` en mode `AUDIT` avant toute correction substantielle.
2. `deal-analysis-workflow` possède les trois modes `AUDIT`, `CLUSTER_AUDIT` et `PUBLISH_REVIEW`.
3. L’audit décide `KEEP`, `LIGHT_UPDATE`, `DEEP_REWRITE`, `MERGE` ou `NOINDEX`.
4. Un `CONTENT_HANDOFF` vers `deal-content-workflow` n’est généré que pour `LIGHT_UPDATE` ou `DEEP_REWRITE`. `KEEP` ne déclenche aucune rédaction ; `MERGE` et `NOINDEX` nécessitent une décision humaine avant action structurelle.
5. Créer ou mettre à jour `.content/deals/<slug>.json` avant de modifier le texte : prix, disponibilité, statut, source et date de contrôle doivent être documentés.
6. Distinguer strictement `ACTIVE_VERIFIED`, `ACTIVE_STOCK_SENSITIVE`, `PRICE_WATCH`, `EXPIRED`, `SOLD_OUT`, `UNVERIFIED` et `NOT_STARTED`. Le HTML ne peut jamais être plus affirmatif que le registre.
7. Un prix barré marchand ne suffit jamais à prouver une remise. Documenter le prix de référence et sa base avant d’afficher une économie ou un pourcentage.
8. Une offre qui dépasse son TTL ne peut plus être présentée comme active sans nouvelle vérification.
9. Les types `LIVE_DEALS`, `BRAND_DEALS`, `EVENT_DEALS` et `SECOND_HAND` sont des grilles de risque, jamais des templates. Aucun type n’impose un ordre de sections, un tableau, une FAQ ou un nombre minimum d’offres.
10. Les pages Bons plans jugent l’offre, pas le classement absolu des produits. Si la question devient « quel produit choisir ? », passer au `comparison-content-workflow`.
11. Aucun produit ou deal ne peut être favorisé selon la commission. Les liens affiliés restent transparents et utilisent `rel="sponsored"` lorsque nécessaire.
12. Ne jamais inventer prix, disponibilité, réduction, durée, stock, compte à rebours ou notion de « meilleur prix ». Une donnée absente reste inconnue ou change de statut.
13. Pour une page existante, `deal-content-workflow` doit respecter le niveau de changement décidé par l’audit et préserver la valeur listée dans le `CONTENT_HANDOFF`.
14. Après rédaction/correction, exécuter la chaîne définie dans `deal-content-workflow`, puis `deal-analysis-workflow` en mode `PUBLISH_REVIEW`.
15. `validate_deal_workflow.py` contrôle uniquement les blockers détectables automatiquement. Un PASS machine ne signifie jamais que la page est publiable.
16. Le `PUBLISH_REVIEW` doit se terminer par `PASS — READY_FOR_HUMAN_VALIDATION` avant validation humaine.
17. En cas de FAIL éditorial, générer un nouveau `CONTENT_HANDOFF` limité aux gates en échec plutôt que de relancer automatiquement une réécriture complète.
18. Conserver `noindex,follow` jusqu’à validation humaine explicite **et** instruction explicite de rendre la page indexable.
19. Aucun quota de mots, H2/H3, offres, tableaux, liens ou sources ne peut servir de proxy de qualité.

## Production éditoriale — Pages de confiance du site

Pour toute création ou réécriture de `/methode-de-test/`, `/comment-nous-comparons/`, `/a-propos/`, `/contact/`, `/transparence-affiliation/` ou `/mentions-legales/` :

1. Utiliser `.agents/skills/trust-content-workflow/SKILL.md`.
2. Mettre à jour `.content/trust/<slug>.json` avant la rédaction ; ce registre est la source de vérité des claims institutionnels.
3. Ne jamais affirmer un test physique sans `DIRECT_OBSERVATION`, ni utiliser « notre équipe », « nos experts » ou équivalent sans preuve `OWNER_CONFIRMED`.
4. Définir concrètement l’indépendance éditoriale au lieu d’utiliser un slogan absolu ; les commissions ne doivent jamais modifier un score ou un classement.
5. Pour l’affiliation, expliquer qu’une transaction éligible peut générer une commission sans promettre un « même prix » ou une absence de coût non vérifiable.
6. Les informations inconnues doivent rester `UNKNOWN` ou `NEEDS_OWNER_INPUT`, jamais être complétées par supposition.
7. `/mentions-legales/` reste `LEGAL_PENDING` tant que les informations de l’éditeur, de l’hébergeur, des traitements de données et autres données légales n’ont pas été confirmées.
8. Exécuter `fact-check`, `affiliate-value` lorsque pertinent, `natural-writing`, `humanizer`, `general-writing`, `anti-ai-slop`, `internal-linking-audit`, `editorial-qa`, puis `validate_trust_workflow.py`.
9. Conserver `noindex,follow` jusqu’à validation humaine explicite ; une validation éditoriale n’entraîne jamais automatiquement l’indexation.
## Maintenance mensuelle à la demande

Pour « lance la maintenance mensuelle », suivre `docs/content-maintenance.md` et préparer le lot avec `scripts/maintenance_orchestrator.py prepare` (ou l'Action manuelle correspondante). Lire le workflow d'analyse sélectionné pour chaque page. La préparation n'est pas un audit. Exécuter les skills existants ici, enregistrer les vrais rapports avec `record`, puis n'appeler le content-workflow que pour LIGHT_UPDATE/DEEP_REWRITE. Conserver la validation humaine, l'état d'indexation et la chaîne de génération existante. Aucun appel API modèle ou service IA externe n'est requis par cette orchestration.
