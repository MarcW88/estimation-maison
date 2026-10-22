---
name: internal-linking-audit
description: Audit contextual internal links and recommend only verified, useful next-step links.
metadata:
  source_repo: MarcW88/bloc-notes-numerique
  source_sha: 98d75a089bb2d0c143ca5f824533abbdda333b8e
  adaptation: repository-local
---

# Internal Linking Audit

## Core rule
Never invent link gaps. Verify source and target pages before recommending changes.

Classify existing links by region where possible: navigation, menu, footer, CTA, or body. If the target already appears contextually in the body, return `no_action_needed`. A navigation-only link does not automatically justify a contextual body link.

## Workflow
1. Inventory the relevant cluster and candidate target pages.
2. Read the source page and verify existing body links.
3. Confirm that the target page exists and serves the promised next question.
4. Recommend a contextual link only when source section, anchor and target intent align.
5. Flag orphan or weakly connected pages only from verified evidence.
6. Do not use link quotas as a quality target.

## Output
For each recommendation provide source, target, anchor, placement, reason, and status (`ADD`, `OPTIONAL`, `NO_ACTION`, `BLOCKED`).

Unreadable pages are BLOCKED, not guessed.
