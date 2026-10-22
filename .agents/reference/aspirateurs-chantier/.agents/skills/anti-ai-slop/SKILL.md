---
name: anti-ai-slop
description: Detect template-like, generic, over-smoothed output patterns without making authorship claims.
metadata:
  source_repo: MarcW88/bloc-notes-numerique
  source_sha: a0ae97dc8814bf450847eb2b7653ab64fbdf0ee0
  adaptation: writing-focused-shared-edition
---

# Anti-AI Slop

This is not an AI detector. Review whether an artifact looks purpose-built for the actual job rather than like the average shape of a polished answer.

## Review questions
1. Purpose: what decision, understanding or action must the artifact support?
2. Specificity: which details make it unmistakably fit this subject and context?
3. Structure: does the form follow the material, or a reusable template?

## Writing signals
Flag generic transitions, interchangeable headings, repeated section roles, symmetry for its own sake, rule-of-three filler, vague authority, promotional smoothing, list sprawl, boilerplate disclaimers repeated unnecessarily, conclusions that only summarize, and paragraphs that could be moved to another entity with name substitution.

Every finding must point to visible evidence and include a concrete fix. Preserve useful tables, bullets and repeated technical terms when they serve the task.

Severity: LOW, MEDIUM or HIGH. HIGH means the generic pattern materially damages specificity, credibility or decision value.
