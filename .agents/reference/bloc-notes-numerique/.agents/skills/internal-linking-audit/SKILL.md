---
name: internal-linking-audit
description: Audit website internal links and produce verified SEO action plans. Use when users ask for internal linking strategy, topic-cluster links, orphan/link gap checks, existing internal link detection, anchor/placement recommendations, Firecrawl-backed crawling, or an exportable internal linking report for a brand site.
---

# Internal Linking Audit

## Core Rule

Never invent link gaps. If a page cannot be read, mark it blocked and do not recommend edits for that page. If a target URL already appears in body/contextual links, mark it `no_action_needed`. If it appears only in navigation/menu/footer/CTA, recommend a contextual body link only when the source section and target topic are semantically aligned.

## Workflow

1. Collect minimal input:
   - `brand.name`
   - `brand.domain`
   - `brand.sitemap` if available
   - `brand.locale`
   - `priority_pages` or user-selected categories
   - `candidate_links` with `source`, `target`, `anchor`, `placement`, `reason`
2. Run lightweight inventory first. Use sitemap/URL patterns/titles to group categories before deep crawling.
3. Ask the user to confirm categories or focus clusters before full audit when the site is large.
4. Crawl only confirmed pages.
5. Extract internal anchors and classify by region: `navigation`, `menu`, `footer`, `cta`, `body`.
6. Evaluate every candidate target URL:
   - `target in body` -> no action needed
   - `target in nav/menu/footer/cta only` -> optional contextual body link
   - `target missing from HTML` -> add internal link
   - unreadable source page -> blocked, no recommendation
7. Export `index.html`, `action-plan.csv`, and `audit.json`.

## Run The Script

Use the bundled script:

```bash
python scripts/internal_link_audit.py \
  --config path/to/config.json \
  --output path/to/report \
  --mode basic
```

For Firecrawl:

```bash
FIRECRAWL_API_KEY=fc-... python scripts/internal_link_audit.py \
  --config path/to/config.json \
  --output path/to/report \
  --mode firecrawl
```

For CMS/exported HTML:

```bash
python scripts/internal_link_audit.py \
  --config path/to/config.json \
  --output path/to/report \
  --mode import \
  --import-dir path/to/html-export
```

## Config Shape

Prefer JSON for nested candidate links:

```json
{
  "brand": {
    "name": "Example",
    "domain": "https://example.com",
    "sitemap": "https://example.com/sitemap.xml",
    "locale": "en-US"
  },
  "crawl_mode": "basic",
  "priority_pages": ["/academy/example-guide"],
  "candidate_links": [
    {
      "source": "/academy/example-guide",
      "target": "/platform/example-product",
      "priority": "P1",
      "anchor": "example product workflow",
      "placement": "section about solving the example problem",
      "reason": "The source section and target page share the same topic cluster."
    }
  ]
}
```

## Firecrawl And MCP

Read `references/firecrawl.md` when the user asks for Firecrawl mode, provides a Firecrawl API key, or mentions Firecrawl MCP. If a Firecrawl MCP tool is available in the active environment, prefer it for scraping/rendering; otherwise use the script's REST API path with `FIRECRAWL_API_KEY`.

## Output Standards

The report must show:

- Pages checked and blocked pages.
- Pages with verified gaps.
- Items that need action and items requiring no action.
- Region distribution per page: navigation, menu, footer, CTA, body.
- For each action item: source page, target page, anchor, placement, and concise optimization analysis.

Do not show process chatter such as “guided discovery probe,” “demo,” or internal reasoning. Keep user-facing text direct and operational.
