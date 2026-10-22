---
name: humanizer
description: Remove generic AI-writing patterns while preserving facts, meaning, technical distinctions and the author's real voice.
license: MIT
metadata:
  source_repo: MarcW88/bloc-notes-numerique
  source_sha: accad07f498f5f57e0b6460e74591d057bd96b2b
  source_version: 2.15.0
  adaptation: compact-shared-edition
---

# Humanizer

Use as a broad editing pass after the factual draft is stable.

## Rules
1. Preserve information, evidence boundaries and technical distinctions; structure may change.
2. Never add a fact, number, date, source, test result or experience absent from the draft/evidence.
3. Match the intended voice and any supplied writing sample.
4. Write for the actual reader and decision, not for an abstract “audience”.
5. Remove inflated significance, promotional language, vague attribution, superficial -ing analysis, canned contrasts, rule-of-three patterns, mechanical symmetry, list sprawl, throat clearing and summary-only conclusions.
6. Vary rhythm because meaning requires it, not by alternating sentence lengths mechanically.
7. Keep precise terminology when it carries a real distinction.

For a full pass, use the sibling skills `better-usage`, `writing-cadence`, `non-autoregressive-writing-pass` and, only when the genre calls for it, `academic-voice`. Do not let any stylistic pass change facts or epistemic force.

## Output boundary
When embedded in another workflow, return only the revised prose/findings requested by the caller. Do not expose process notes in final page copy.
