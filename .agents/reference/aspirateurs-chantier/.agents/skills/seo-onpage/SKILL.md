---
name: seo-onpage
description: "Run a single-page on-page SEO audit or optimization covering title, meta, headings, content quality, internal links, URL hygiene and honest schema. Adapted from Rampstack."
category: seo-foundation
metadata:
  upstream: https://github.com/rampstackco/claude-skills/tree/main/skills/seo-onpage
  source_repo: MarcW88/bloc-notes-numerique
  source_sha: 7df9f0c63c5b6433ff808157667e71b56ccd2dd5
  vendored_for: aspirateurs-chantier.fr
---

# On-Page SEO

Use this skill after the page's target query and role are known. Optimize for relevance, click-through and crawler comprehension without keyword quotas or template-driven headings.

## Eight dimensions

1. **Title** — unique, aligned with the query and the real promise.
2. **Meta description** — accurate, useful for CTR, not a keyword list.
3. **Heading structure** — one H1; H2/H3 represent real reader questions or decision stages. No arbitrary counts.
4. **Body content** — answer intent early; use specifics, entities and real trade-offs.
5. **Internal links** — descriptive anchors to logical next questions; no fixed quota.
6. **Images/media** — useful media with appropriate alt text and stable dimensions.
7. **URL** — preserve clean existing conventions; do not change a valid URL merely to insert a keyword.
8. **Schema** — only when it matches visible content and the evidence basis. Do not use Review schema to imply hands-on testing that did not happen.

## Workflow

1. Confirm target query/cluster and page role.
2. Review the actual page/rendered HTML.
3. Assess each dimension as `PASS`, `NEEDS_WORK`, or `FAIL`.
4. Prioritize by user/search impact.
5. Draft changes only when requested by the calling workflow.

## Failure patterns

- optimizing unresolved intent;
- keyword-density targets;
- arbitrary word/title/heading rules as hard quality signals;
- forcing the same architecture across sibling pages;
- misleading schema;
- links added only to satisfy a quota.

## Attribution

Vendored and adapted from `rampstackco/claude-skills/skills/seo-onpage`, MIT licensed.