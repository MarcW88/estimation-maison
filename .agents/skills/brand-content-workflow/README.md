# Brand Content Workflow

Workflow portable pour créer et maintenir des pages marque SEO/GEO à forte valeur commerciale.

## Ce qu'il gère

Le workflow route automatiquement les pages vers :

- `BRAND_HUB`
- `PRODUCT`
- `REVIEW`
- `SERVICE`
- `ACCESSORY_HUB`
- `ALTERNATIVES`

## Différence avec les autres workflows

### Guide workflow
Part d'une question ou d'un besoin informationnel.

### Comparison workflow
Part d'un univers produit, de critères, de poids et d'un scoring.

### Brand workflow
Part d'une **entité**, de sa **gamme actuelle**, de son **écosystème** et de son **maillage**.

## Installation

Copier dans :

`.agents/skills/brand-content-workflow/`

Puis copier :

`brand-workflow.config.example.yaml`

à la racine sous :

`brand-workflow.config.yaml`

## Fichier de données par marque

Créer :

`.content/brands/<brand>.yaml`

à partir de :

`references/brand-data-template.yaml`

## Utilisation

Exemple :

> Applique `brand-content-workflow` à toutes les pages `/marques/remarkable/`.
> Route automatiquement chaque URL selon son type.
> Vérifie la gamme actuelle avant rédaction.
> Distingue analyse documentaire et test réel.
> Garde les pages noindex jusqu'à validation.

## Important

Le validator structurel ne prouve jamais :
- que les faits sont corrects ;
- qu'un produit a été réellement testé ;
- que le GEO est bon ;
- que le positionnement est juste.

Ces points restent des passes éditoriales séparées.
