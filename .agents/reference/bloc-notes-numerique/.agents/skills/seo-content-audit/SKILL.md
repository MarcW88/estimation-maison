---
name: seo-content-audit
description: "Audit existing content to decide what to keep, update, merge, redirect, or delete; diagnose content decay and cannibalization. Adapted from Rampstack's SEO content audit skill."
category: seo-foundation
metadata:
  upstream: https://github.com/rampstackco/claude-skills/tree/main/skills/seo-content-audit
  vendored_for: bloc-notes-numeriques.fr
---

# SEO Content Audit

Use this skill to evaluate existing content before deciding to rewrite it. The goal is not to maximize changes; it is to preserve value and choose the smallest action that solves the problem.

## Core actions

Every audited page maps first to one of these upstream actions:

- `KEEP` — role and content are still strong.
- `UPDATE` — useful page with fixable decay, gaps or stale facts.
- `MERGE` — overlapping pages would be stronger as one.
- `REDIRECT` — page has no future as a standalone URL but equity/intent should move elsewhere.
- `DELETE` — no meaningful demand, value or assets worth preserving.

For bloc-notes-numeriques.fr, destructive actions are recommendations only unless the user explicitly asks to implement them.

## Evidence to consider

When available, use:

- Search Console queries, clicks, impressions, CTR and positions;
- analytics/conversions;
- backlinks/referring domains;
- crawl/internal-link context;
- last meaningful update;
- current SERP and competing pages;
- overlap with other URLs in the same cluster.

Do not fabricate missing metrics. If no performance data is available, audit editorial role, intent and overlap and mark the data gap.

## Cannibalization

When two pages plausibly serve the same query/decision, determine:

1. whether the intents are actually identical;
2. which URL has the stronger role/signals;
3. whether differentiation is meaningful;
4. whether merge is preferable to maintaining two weak variants.

Do not call two pages cannibalizing merely because they share products or vocabulary.

## Single-page use

For one URL, this skill answers:

- does the page still deserve to exist independently?
- what value should be preserved?
- is the problem local or structural?
- is a light update sufficient?
- is a deeper rebuild justified?

## Failure patterns

- deleting or rewriting solely because traffic is low;
- treating age alone as obsolescence;
- updating two pages that should be merged;
- rewriting a page without preserving its strong sections/signals;
- inventing performance evidence that was not supplied.

## Output

Return:

1. current role;
2. evidence available / missing;
3. strongest existing value;
4. overlap/cannibalization findings;
5. upstream action (`KEEP`, `UPDATE`, `MERGE`, `REDIRECT`, `DELETE`);
6. confidence and rationale.

## Attribution

Vendored and adapted from `rampstackco/claude-skills/skills/seo-content-audit`, MIT licensed. The upstream skill remains the methodological reference.