---
name: content-brief-authoring
description: "Build a per-piece editorial brief that guides a writer without bloating the process: target cluster, intent, reader/JTBD, decision, evidence, entities, internal links, anti-patterns and success criteria. Adapted from Rampstack."
category: content
metadata:
  upstream: https://github.com/rampstackco/claude-skills/tree/main/skills/content-brief-authoring
  source_repo: MarcW88/bloc-notes-numerique
  source_sha: 861de637874253aa2302d1ad43fb20b9b01572cf
  vendored_for: aspirateurs-chantier.fr
---

# Content Brief Authoring

A brief exists to reduce drift before writing. It should contain only information that changes the resulting piece.

## Required fields for comparison pages

1. target query + supporting cluster;
2. dominant SERP/search intent and accepted page format;
3. reader and decision to make;
4. JTBD when context-led;
5. scope: what is compared and deliberately out of scope;
6. decision criteria derived from query and evidence;
7. required facts, entities and citations;
8. important trade-offs and contraindications;
9. internal-link destinations for logical next questions;
10. anti-patterns specific to this piece;
11. success criteria;
12. editorial angle / thesis.

## Comparison discipline

For `X vs Y`, make clear where X wins, where Y wins and what variable changes the recommendation. A universal winner is optional.

For `best X` or a use-case selection, state the selection logic before drafting recommendations. An exhaustive market census or numeric score is not required unless it genuinely improves the decision.

## Outline rule

The outline is derived from the brief. Do not force `verdict → criteria → table → product 1 → product 2 → FAQ → conclusion`. H2s should correspond to reader questions, decision points or meaningful comparison dimensions.

A shared UI component is fine; shared editorial architecture is not automatically fine.

## Anti-patterns

- word-count quotas detached from intent;
- keyword-density targets;
- mandatory FAQ;
- heading symmetry for its own sake;
- telling the writer who wins before selection logic is established;
- treating an editorial score as a fact.

## Output

Produce a concise brief plus a proposed outline with a one-line purpose for each section. Mark evidence gaps instead of guessing.

## Attribution

Vendored and adapted from `rampstackco/claude-skills/skills/content-brief-authoring`, MIT licensed.