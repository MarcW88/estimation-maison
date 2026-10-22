# Content Recovery & Production Workflow

Workflow générique pour réutiliser le même process SEO/GEO sur plusieurs sites.

## Installation

Copier ce dossier dans :

`.agents/skills/content-recovery-and-production-workflow/`

Puis copier :

`content-workflow.config.example.yaml`

à la racine du projet sous le nom :

`content-workflow.config.yaml`

## À adapter par site

- `content_scope`
- `content_type`
- `source_of_truth`
- `quality_reference`
- chemins commerciaux
- dossiers briefs/reviews
- seuils du quality gate
- stratégie noindex

## Exemple d'instruction

> Applique content-recovery-and-production-workflow à toutes les pages /guides/.  
> Pour les contenus existants : recovery.  
> Pour les pages vides : création.  
> Prends /guides/prix-produit/ comme quality_reference.  
> Ne retire aucun noindex.

## Important

Le validator est un garde-fou structurel. Il ne remplace jamais le fact-check, le GEO, le Humanizer ou l'editorial QA.
