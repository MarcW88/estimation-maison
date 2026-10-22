---
name: seo-keyword
description: "Run keyword research, classify by search intent, cluster into topical groups, and prioritize for content production. Adapted from Rampstack."
category: seo-foundation
metadata:
  upstream: https://github.com/rampstackco/claude-skills/tree/main/skills/seo-keyword
  source_repo: MarcW88/bloc-notes-numerique
  source_sha: 97eb0de9d21b79802957a2e93ed89d9acdd13542
  vendored_for: aspirateurs-chantier.fr
---

# Keyword Research

Find the queries worth ranking for, classify them by intent, cluster them into topics, and prioritize what to produce. The SERP and first-party data are the source of truth.

## When to use

- understanding search intent before writing;
- identifying the target cluster for a comparison;
- separating nearby commercial intents;
- detecting cannibalization risk;
- finding accepted page formats in the SERP.

## Framework

### Discover
Use seed terms, competitor queries, Search Console, related searches, customer language and community language.

### Classify by intent
Map each query to informational, navigational, commercial or transactional intent. Hybrid intents are allowed; note the dominant intent and modifier.

### Cluster
Group keywords that should target the same page using SERP overlap and topical relevance. Avoid one-keyword-per-page thinking.

### Prioritize
Assess opportunity, difficulty and strategic fit using the data actually available. State gaps rather than inventing precision.

## Workflow

1. Define scope and audience.
2. Discover candidate queries.
3. Deduplicate and clean.
4. Classify intent.
5. Cluster related queries.
6. Assess opportunity/difficulty/fit when data exists.
7. Output the target cluster and SERP-derived page role.

## Failure patterns

- chasing volume without intent;
- ignoring Search Console on an existing site;
- one-keyword-per-page clustering;
- ignoring SERP features and accepted page formats;
- treating keyword research as static.

If required data is unavailable, state the gap and which conclusions are affected.

## Attribution

Vendored and lightly adapted from `rampstackco/claude-skills`, MIT licensed.