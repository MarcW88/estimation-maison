---
name: content-audit
description: Audit an existing editorial page before rewriting and decide KEEP, UPDATE, MERGE, REDIRECT or REMOVE.
license: MIT
metadata:
  source_repo: MarcW88/bloc-notes-numerique
  source_sha: 1316a54fbd73849d3a68b3ea04f36f1fd48ade6c
  adaptation: domain-neutralized
---

# Content Audit

Audit first; do not rewrite during this pass.

A weak page does not automatically deserve a rewrite. Check whether the URL still has a distinct function, identifiable intent, historical/editorial value, useful links, and recovery potential.

Never fill missing performance or evidence data by assumption. Missing signals remain UNKNOWN.

## Decisions
- `KEEP`: unique, current and useful; only minor corrections needed.
- `UPDATE`: useful role remains but facts, structure, evidence, value or intent need repair.
- `MERGE`: another URL serves essentially the same intent and the distinction is too weak.
- `REDIRECT`: no autonomous role remains but a clear successor exists.
- `REMOVE`: no useful intent, history, links, consolidation value or editorial role remains.

## Risks to flag
Merchant/manufacturer paraphrase, pages where only the entity name changes, cloned structure, generic introductions/conclusions, unsupported recommendations, outdated facts, fake experience, cannibalization, and content that loses most value when affiliate links disappear.

## Output
1. Decision
2. Confidence
3. Evidence used
4. Unknowns
5. Main problem
6. Recovery potential
7. Next skill
