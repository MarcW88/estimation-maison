# Promo evidence standard

Adapté pour un site éditorial affilié à partir des principes de `promo-discount-impact-review-ecommerce` de mardab96/ecommerce-claude-skills.

## Ce que l'on cherche à prouver

Une page de bons plans n'a pas à prouver que la promotion est rentable pour le marchand. Elle doit prouver que le lecteur voit bien :

1. un prix réellement observable ;
2. une comparaison défendable ;
3. une disponibilité compatible avec l'achat ;
4. un avantage qui ne masque pas un compromis important.

## Niveaux de preuve

- `OFFICIAL_CURRENT`: prix ou disponibilité sur le site constructeur/marchand.
- `OFFICIAL_HISTORICAL`: prix constructeur daté dans une annonce officielle.
- `SPECIALIST_PRICE_TRACKER`: historique ou prix marché provenant d'un comparateur spécialisé.
- `RETAILER_CURRENT`: offre visible chez un revendeur identifiable.
- `EDITORIAL_REPORT`: article tiers daté décrivant une promotion passée ou présente.
- `HYPOTHESIS`: interprétation à ne jamais présenter comme fait.

## Règles de décision

### ACTIVE_VERIFIED

Possible seulement si la source permet de confirmer le prix et si rien n'indique que l'offre est terminée ou indisponible.

### ACTIVE_STOCK_SENSITIVE

Utiliser si :

- le stock varie ;
- la TVA/frais finaux dépendent du checkout ;
- le prix dépend d'un entrepôt, d'une variante ou d'un bundle ;
- la page promotionnelle et la fiche produit se contredisent sur la disponibilité.

### PRICE_WATCH

Utiliser lorsqu'un prix est intéressant ou inférieur à un ancien prix connu, mais qu'aucun mécanisme promotionnel actuel n'est démontré.

### EXPIRED / SOLD_OUT

Ces offres peuvent rester dans l'historique pour donner un repère, mais ne doivent pas être mises en avant comme achetables.

## Réduction calculée

Toujours conserver :

- `price`
- `reference_price`
- `reference_price_basis`

Puis calculer la remise. Si la base n'est pas fiable, ne pas afficher de pourcentage.

## Pièges à éviter

- reprendre un prix barré sans comprendre sa base ;
- comparer deux bundles différents ;
- oublier le stylet, l'étui ou un abonnement nécessaire ;
- comparer un ancien modèle bradé avec le prix d'un nouveau modèle ;
- dire « meilleur prix » sur la base d'un seul marchand ;
- utiliser un article de deal ancien comme preuve d'une offre actuelle ;
- confondre disponibilité produit et disponibilité dans le pays ciblé.

## Exemple

Si un pack est affiché 849 € et que les éléments séparés documentés valent 898 €, on peut dire :

> Le pack économise 49 € par rapport à l'achat séparé des éléments observés le même jour.

On ne doit pas dire :

> C'est le prix le plus bas jamais vu.

sans historique démontrable.