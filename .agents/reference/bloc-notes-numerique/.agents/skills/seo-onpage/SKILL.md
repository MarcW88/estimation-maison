---
name: seo-onpage
description: "Run a single-page on-page SEO audit or optimization covering title, meta, headings, content quality, internal links, URL hygiene and honest schema. Adapted from Rampstack's seo-onpage skill."
category: seo-foundation
metadata:
  upstream: https://github.com/rampstackco/claude-skills/tree/main/skills/seo-onpage
  vendored_for: bloc-notes-numeriques.fr
---

# On-Page SEO

Use this skill after the page's target query and role are known. Optimize for relevance, click-through and crawler comprehension without keyword quotas or template-driven headings.

## Eight dimensions

### 1. Title
Unique, aligned with the target query and the page's real promise. Avoid stuffing and unnecessary duplication with H1.

### 2. Meta description
Unique, useful for CTR, accurate to the page and not a keyword list.

### 3. Heading structure
One H1. H2/H3 should describe genuine reader questions or decision stages. No arbitrary heading count and no headings created solely for keywords.

### 4. Body content
Answer the dominant intent early. Cover the decision with the depth the topic requires. Prefer specifics, entities and real trade-offs over generic completeness.

### 5. Internal links
Use descriptive anchors and link only where the destination answers a logical next question. No fixed link quota.

### 6. Images/media
Meaningful images need appropriate alt text and stable dimensions. Decorative images do not need descriptive alt text.

### 7. URL
Respect the site's existing clean URL conventions. Do not change a valid URL merely to insert a keyword.

### 8. Schema
Use structured data only when it matches visible content and the evidence basis. For comparison/buying-guide content without genuine hands-on review evidence, prefer honest Article/ItemList-style markup over misleading Review markup.

## Workflow

1. Confirm target query/cluster and page role.
2. Review the actual page and rendered HTML.
3. Assess the eight dimensions as `PASS`, `NEEDS_WORK`, or `FAIL`.
4. Prioritize fixes by user/search impact, not by checklist count.
5. Draft changes only when requested by the calling workflow.

## Failure patterns

- optimizing a page whose intent is unresolved;
- keyword-density targets;
- arbitrary title/meta/word-count rules treated as hard quality signals;
- forcing the same heading architecture across sibling pages;
- misleading schema;
- adding internal links to satisfy a quota.

## Output

Return target query, page role, findings by dimension, critical fixes, important fixes and optional polish.

## Attribution

Vendored and adapted from `rampstackco/claude-skills/skills/seo-onpage`, MIT licensed. The upstream skill remains the methodological reference.