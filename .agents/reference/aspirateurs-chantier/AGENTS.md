# Instructions du dépôt

Ce dépôt contient aspirateurs-chantier.fr.

## Maintenance éditoriale

Suivre `docs/content-maintenance.md` et `maintenance.config.json`. Préparer avec `python scripts/maintenance_orchestrator.py prepare --max-pages 10`. La préparation n’est pas un audit IA.

Réutiliser exclusivement les paires analysis/content-workflow existantes sous `.agents/skills/` : guides → guide, comparatifs → comparison, marques → brand, usages → usage, modeles → model. Lire intégralement le workflow pertinent et les skills spécialisés appelés. AUDIT avant correction, puis content-workflow seulement pour LIGHT_UPDATE/DEEP_REWRITE, et PUBLISH_REVIEW avant validation humaine. KEEP ne déclenche aucune modification éditoriale.

**Modèles : audit uniquement.** Respecter la phase 1 de model-content-workflow : pas de modification automatique des pages ni de `_generate_model_overrides.py`. Les corrections et la migration du renderer nécessitent une tâche séparée.

Persister les vrais rapports, preuves et run-evidence ; ne pas inventer de recherche, de test produit, de certification, de prix ou de PASS. Vérifier les claims de sécurité avec des sources adaptées. Préserver les sources de génération existantes et les plans propres aux pages ; aucun nouveau template éditorial.

Conserver URLs, canonical et état robots. MERGE/NOINDEX, suppression, redirection et indexation nécessitent une décision humaine. Ouvrir une PR avec rapports, registre, historique et corrections ; aucun merge automatique.

## Design

Lire DESIGN.md et `.agents/skills/site-design-review/SKILL.md` avant toute intervention sur l’interface. Préserver les composants et tokens existants.
