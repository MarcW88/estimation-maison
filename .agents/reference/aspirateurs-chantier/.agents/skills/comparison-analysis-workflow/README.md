# Comparison Analysis Workflow

Workflow d'analyse des pages `/comparatifs/` d'aspirateurs-chantier.fr.

## Modes

- `AUDIT` — diagnostic d'une page existante sans réécriture.
- `CLUSTER_AUDIT` — audit des frontières d'intention et de la similarité entre comparatifs.
- `PUBLISH_REVIEW` — gate final après production.

## Décisions

- `KEEP`
- `LIGHT_UPDATE`
- `DEEP_REWRITE`
- `MERGE`
- `NOINDEX`

## Gouvernance

Ce workflow est custom uniquement pour l'orchestration, les risques métier liés aux aspirateurs de chantier et les frontières du cluster. Les audits SEO, intention, preuve, fact-check, affiliation, anti-slop, maillage et QA sont délégués aux skills partagés définis dans `.agents/skills/comparison-skill-stack.json`.

Le ratio shared doit rester >=80 %.

## Publication

Un `PUBLISH_REVIEW` peut retourner :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Il ne retire jamais `noindex, follow` automatiquement.
