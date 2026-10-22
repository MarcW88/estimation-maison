# Deal Content Workflow

Workflow éditorial pour pages de promotions, bons plans, événements commerciaux et occasion/reconditionné.

## Contenu du package

- `SKILL.md` : orchestration complète.
- `references/promo-evidence.md` : standard de preuve d'une promotion.
- `THIRD_PARTY_NOTICES.md` : attribution des briques méthodologiques MIT.
- `.content/deals/_template.json` : modèle de registre de preuve.
- `deal-workflow.config.yaml` : types de pages, statuts et TTL.
- `validate_deal_workflow.py` : garde-fous structurels et de fraîcheur.

## Philosophie

Une page de deal ne classe pas les produits : elle juge la qualité et la fraîcheur d'une offre. La recommandation produit doit rester indépendante du niveau de commission et être traitée par un comparatif ou une page produit dédiée.

## Intégration minimale dans un autre repo

1. Copier le skill dans `.agents/skills/deal-content-workflow/`.
2. Copier le template et créer `.content/deals/<slug>.json`.
3. Adapter `deal-workflow.config.yaml` aux URLs et TTL du site.
4. Adapter le validateur à la liste de pages du projet.
5. Brancher le générateur HTML sur les registres de preuve.
6. Exécuter la QA avant toute publication ou indexation.

Le package n'impose aucun fournisseur de prix ni API : les sources peuvent être officielles, marchands, price trackers ou recherches manuelles, à condition que leur niveau de preuve soit enregistré.