---
name: content-refresh
description: Decide how an UPDATE page should be repaired while preserving useful existing material.
license: MIT
metadata:
  source_repo: MarcW88/bloc-notes-numerique
  source_sha: 8bad3c8958bdfd452dda9adbd61d2214026c4fc1
  adaptation: domain-neutralized
---

# Content Refresh

Use only after `content-audit` returns UPDATE.

Preserve what already works. Repair the problem instead of automatically replacing the entire page.

## Diagnose
Classify the main cause: Intent drift, Thin value, Merchant duplication, Outdated, Weak structure, Cannibalization, Generic prose, or Trust gap.

## Refresh level
- `LIGHT`: targeted facts/passages/answers; preserve the useful structure.
- `MAJOR`: substantial section rebuilding while retaining strong passages, evidence and links.
- `FULL`: only when the existing text is largely duplicative, generic, obsolete or aimed at the wrong intent.

Do not replace precise information with smoother but vaguer prose. Do not add FAQ sections, headings or keyword variants merely for SEO.

## Output
1. What stays
2. What is removed
3. What is rewritten
4. New information required
5. Claims requiring research
6. Recommended refresh level
