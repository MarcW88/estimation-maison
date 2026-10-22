---
name: trust-content-workflow
description: Produit et maintient les pages de confiance du site (méthode d'évaluation, politique de comparaison, à propos, contact, transparence affiliation) sans inventer de tests, d'équipe, d'indépendance ou d'informations juridiques.
---

# Trust Content Workflow

## Objectif

Les pages de confiance ne servent pas à fabriquer une image de crédibilité. Elles doivent expliquer, de façon vérifiable, **qui publie le site, comment les conclusions sont produites, quelles sont les limites des analyses et comment le site gagne de l'argent**.

Le workflow couvre :

- `METHODOLOGY` → `/methode-de-test/` ;
- `COMPARISON_POLICY` → `/comment-nous-comparons/` ;
- `ABOUT` → `/a-propos/` ;
- `CONTACT` → `/contact/` ;
- `AFFILIATE_DISCLOSURE` → `/transparence-affiliation/` ;
- `LEGAL_PENDING` → `/mentions-legales/`, uniquement pour enregistrer les informations manquantes jusqu'à fourniture par le propriétaire du site.

## Principe central

> Une page de confiance doit réduire l'asymétrie d'information entre le site et le lecteur.

Ne jamais utiliser une formulation plus forte que le niveau de preuve disponible.

## Source de vérité

Avant rédaction, créer ou mettre à jour `.content/trust/<slug>.json`.

Le registre doit contenir au minimum :

- `page_type` ;
- `status` ;
- `claims` ;
- `required_disclosures` ;
- `unknowns` ;
- `editorial_rules` ;
- `qa`.

Toute affirmation institutionnelle importante présente dans le HTML doit pouvoir être reliée à un claim du registre.

## Niveaux de preuve

Utiliser uniquement :

- `DIRECT_OBSERVATION` : action ou test réellement effectué et documenté ;
- `REPO_EVIDENCE` : processus ou règle effectivement présent dans le dépôt ;
- `OFFICIAL_SOURCE` : information issue d'une source officielle identifiable ;
- `OWNER_CONFIRMED` : information explicitement confirmée par le propriétaire/éditeur du site ;
- `EDITORIAL_INFERENCE` : conclusion éditoriale clairement présentée comme telle ;
- `UNKNOWN` : information manquante ou non vérifiée.

`UNKNOWN` n'est pas une faiblesse à masquer : il doit bloquer la formulation correspondante.

## Règles transversales

### Tests et expérience produit

- Ne jamais écrire « nous avons testé », « lors de nos tests » ou équivalent sans `DIRECT_OBSERVATION` et trace correspondante.
- Une analyse documentaire doit être nommée comme telle.
- Si certains produits sont testés physiquement et d'autres non, l'indiquer produit par produit ou via un badge/niveau de preuve.
- Tant qu'aucun protocole de test physique généralisé n'existe, préférer « méthode d'évaluation » à « méthode de test » dans le H1 et l'introduction.

### Équipe et identité

- Ne jamais écrire « notre équipe » si le site est géré par une seule personne ou si les contributeurs ne sont pas documentés.
- Ne pas inventer d'expertise, de diplômes, de volume de tests, d'ancienneté ou de relation avec une marque.
- Une biographie ne doit contenir que des éléments `OWNER_CONFIRMED` ou publiquement vérifiables.

### Indépendance éditoriale

Le mot « indépendant » ne doit pas rester un slogan. Si utilisé, expliquer au minimum :

- si les commissions influencent ou non le scoring ;
- si une marque peut payer pour être incluse ;
- comment sont traités les produits prêtés/offerts ;
- si les contenus sponsorisés sont acceptés ;
- comment sont signalés les liens affiliés.

Si l'une de ces règles n'est pas définie, ne pas sur-promettre l'indépendance.

### Affiliation

- Expliquer simplement qu'un achat via certains liens peut générer une commission.
- Ne jamais affirmer automatiquement que l'affiliation « ne coûte rien au lecteur » : le prix final est fixé par le marchand et peut varier.
- Les commissions ne doivent pas modifier un score ou un classement.
- Les liens commerciaux doivent respecter la politique du site (`rel="sponsored"` lorsque nécessaire).
- Expliquer le traitement des produits sans programme d'affiliation : ils ne doivent pas être exclus pour cette seule raison.

### Marques, prêts et cadeaux

Documenter explicitement le traitement de :

- produits achetés par le site ;
- produits prêtés ;
- produits offerts ;
- accès presse ;
- partenariats sponsorisés ;
- absence de relation commerciale.

Ne pas prétendre qu'aucun produit n'a jamais été fourni si cette information n'est pas confirmée.

## Workflow par type de page

### METHODOLOGY

Objectif : expliquer comment une conclusion est produite.

Inclure :

1. ce qui est réellement testé physiquement ;
2. ce qui relève d'une analyse documentaire ;
3. sources prioritaires ;
4. niveaux de preuve ;
5. fact-check et mise à jour ;
6. limites de la méthode ;
7. corrections d'erreurs.

Le texte doit permettre au lecteur de distinguer **observation**, **source** et **jugement éditorial**.

### COMPARISON_POLICY

Objectif : rendre le classement reproductible et intelligible.

Inclure :

1. définition de l'intention / du use case ;
2. critères avant sélection des gagnants ;
3. preuves utilisées ;
4. scoring et pondération ;
5. traitement des données manquantes ;
6. égalités / ex aequo ;
7. influence nulle des commissions sur les notes ;
8. fréquence et motif de mise à jour ;
9. limites du classement.

Se synchroniser avec `comparison-content-workflow` plutôt que créer une méthodologie parallèle.

### ABOUT

Objectif : répondre honnêtement à « qui publie ce site et pourquoi ? ».

Inclure uniquement des faits confirmés sur :

- l'éditeur ou l'auteur ;
- le but du site ;
- l'expérience pertinente ;
- la manière dont le contenu est produit ;
- les limites ;
- le modèle économique ;
- la politique de corrections.

Pas de persona d'entreprise fictif, pas de fausse rédaction, pas de faux laboratoire.

### CONTACT

Objectif : offrir une voie de correction et de dialogue.

Prévoir des motifs explicites :

- signaler une erreur factuelle ;
- demander une correction ;
- exercer un droit de réponse ;
- proposer une source ou un produit ;
- question liée à l'affiliation ;
- problème technique ;
- contact professionnel.

Ne publier aucune adresse, téléphone ou identité de contact non confirmés.

### AFFILIATE_DISCLOSURE

Objectif : permettre au lecteur de comprendre le modèle économique avant de cliquer.

Inclure :

1. définition d'un lien affilié ;
2. moment où une commission peut être perçue ;
3. influence sur le classement ;
4. traitement des marchands/programmes ;
5. produits sans affiliation ;
6. prix et disponibilité ;
7. liens sponsorisés ;
8. produits prêtés/offerts si applicable ;
9. contenus sponsorisés si applicable ;
10. politique de mise à jour.

### LEGAL_PENDING

Le workflow **ne rédige pas de mentions légales à partir d'hypothèses**.

Il peut uniquement enregistrer les informations nécessaires et leur statut :

- identité ou raison sociale de l'éditeur ;
- statut juridique ;
- adresse ;
- email de contact légal ;
- directeur de publication ;
- hébergeur ;
- outils de mesure / cookies ;
- traitements de données ;
- éventuel numéro d'entreprise / TVA selon le cadre applicable.

Tant que ces éléments ne sont pas confirmés, conserver la page en `LEGAL_PENDING` et `noindex,follow`.

## Chaîne de production

1. Audit des claims existants dans la page et le footer.
2. Création/mise à jour du registre `.content/trust/<slug>.json`.
3. Classification des claims par niveau de preuve.
4. Suppression ou affaiblissement des formulations non prouvées.
5. Vérification de cohérence avec les workflows `comparison-content-workflow`, `deal-content-workflow`, `guide-content-workflow` et `brand-content-workflow`.
6. Rédaction.
7. QA dans cet ordre :
   - `fact-check` ;
   - `affiliate-value` pour les claims économiques/affiliés ;
   - `natural-writing` ;
   - `humanizer` ;
   - `general-writing` ;
   - `anti-ai-slop` ;
   - `internal-linking-audit` ;
   - `editorial-qa` ;
   - `validate_trust_workflow.py`.

## Garde-fous bloquants

La page ne peut pas obtenir `PASS` si elle contient :

- un test physique non documenté ;
- une équipe fictive ;
- une expertise personnelle inventée ;
- une promesse d'indépendance non définie ;
- une affirmation de prix/commission non vérifiée ;
- un faux historique de marque ou du site ;
- une coordonnée de contact inventée ;
- une information juridique supposée ;
- un placeholder présenté comme un fait.

## Indexation

Conserver `noindex,follow` jusqu'à validation humaine explicite. La validation éditoriale et la décision d'indexation restent deux décisions séparées.
