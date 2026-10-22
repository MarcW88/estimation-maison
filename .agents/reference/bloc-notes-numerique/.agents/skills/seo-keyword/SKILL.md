---
name: seo-keyword
description: "Run keyword research, classify by search intent, cluster into topical groups, and prioritize for content production. Use this skill whenever the user asks to do keyword research, find target keywords, identify ranking opportunities, classify search intent, build a topical map, or plan a content strategy around what people search for. Triggers on keyword research, keyword strategy, search intent, keyword clustering, topic clusters, keyword difficulty, search volume, ranking opportunity, content gap, what should I write about, target keyword, primary keyword, secondary keyword, long-tail. Also triggers when planning a content calendar or new site without keywords yet defined."
category: seo-foundation
catalog_summary: "Discovery, intent classification, clustering, prioritization"
display_order: 3
metadata:
  upstream: https://github.com/rampstackco/claude-skills/tree/main/skills/seo-keyword
  vendored_for: bloc-notes-numeriques.fr
---

# Keyword Research

Find the queries worth ranking for, classify them by intent, cluster them into topics, and prioritize what to produce. Stack-agnostic. Tool-agnostic (works with any keyword tool).

## When to use

- Starting a new site or content section
- Planning a content calendar
- Looking for ranking opportunities on an existing site
- Understanding search intent before writing
- Building topic clusters for internal linking
- Identifying content gaps vs competitors

## When NOT to use

- Optimizing a single page where the target query is already known (use `seo-onpage`)
- Comparing your site to a competitor across many dimensions (use `seo-competitor`)
- Auditing existing content for performance (use `seo-content-audit`)

## Required inputs

- The site or topic area
- The target audience and what they need
- A keyword tool OR access to search console for an existing site
- Optional: known competitors to seed the research

If no tool is available, the skill still works using SERP inspection and search console data alone, but volume estimates will be rough.

## The framework: 4 stages

### Stage 1: Discover

Cast a wide net from seed terms, competitor keywords, search console queries, related searches, customer language and forum/community language.

### Stage 2: Classify by intent

Map each keyword to informational, navigational, commercial or transactional intent. The SERP is the source of truth. Hybrid intents are allowed; note the dominant intent and modifier.

### Stage 3: Cluster

Group keywords that should target the same page using SERP overlap and topical relevance. Avoid one-keyword-per-page thinking and flag potential cannibalization.

### Stage 4: Prioritize

Assess opportunity, difficulty and strategic fit. Use the data actually available and state gaps rather than inventing precision.

## Workflow

1. Define scope and audience.
2. Discover candidate queries.
3. Deduplicate and clean.
4. Classify intent.
5. Cluster related queries.
6. Assess opportunity/difficulty/strategic fit when data exists.
7. Prioritize.
8. Output the target cluster and the SERP-derived page intent.

## Failure patterns

- Chasing volume without intent.
- Ignoring search console on an existing site.
- One-keyword-per-page clustering.
- Ignoring SERP features and accepted page formats.
- Treating keyword research as static.

## If required data is unavailable

State the gap, what was actually verified, and which conclusions are affected. Never fabricate or interpolate missing numbers.

## Attribution

Vendored and lightly adapted from `rampstackco/claude-skills`, MIT licensed. The upstream skill remains the methodological reference.