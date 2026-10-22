---
name: jobs-to-be-done
description: "Analyse the progress a user is trying to make in a concrete situation before reasoning in products, personas or features. Adapted from Wondel.ai's MIT-licensed jobs-to-be-done skill."
license: MIT
metadata:
  upstream: https://github.com/wondelai/skills/tree/main/jobs-to-be-done
  source_repo: MarcW88/bloc-notes-numerique
  source_sha: b1c1932e0b0279d3060583bafbd2263420a4c2a7
  vendored_for: aspirateurs-chantier.fr
---

# Jobs to Be Done — generic editorial adaptation

Use this skill to understand **the progress someone is trying to make in specific circumstances**. It does not invent personas and it does not choose products directly.

## 1. Formulate the job without naming the solution

Use:

> When [circumstances], I want [progress], so that [desired outcome].

If a product category, brand or model is required to state the job, the framing is too product-centric.

## 2. Describe circumstances, not just audience labels

A category such as “professional”, “DIY user”, “mobile worker” or “budget buyer” is not yet a job. Describe:

- trigger/context;
- material, task or information being handled;
- frequency and duration;
- physical/digital environment;
- what makes the current situation difficult;
- concrete outcome expected.

## 3. Three dimensions

### Functional
What must actually be accomplished.

### Emotional
What the user is trying to feel or avoid.

### Social
What changes in interaction with others.

Do not invent emotional or social motivations. Without evidence, mark them `HYPOTHESIS` and do not publish them as facts.

## 4. Forces of change

Distinguish:

- **Push** — dissatisfaction with the current way;
- **Pull** — attraction toward a new way;
- **Anxiety** — perceived risk of changing;
- **Habit** — friction that favors staying with the current solution.

## 5. Identify the real competition

List every plausible alternative that can perform the job, including staying with the current setup, renting, using another tool category, combining tools, or not changing anything.

## 6. Big Hire vs Little Hire

- **Big Hire**: decision to buy/adopt.
- **Little Hire**: repeated decision to use the solution in the real situation.

Favor criteria that change the Little Hire rather than specs that only make the product easier to market.

## 7. Turn the job into decision criteria

Classify criteria as:

- `MUST_HAVE`
- `HIGH`
- `CONDITIONAL`
- `LOW`
- `CONTRAINDICATION`

This skill does **not** score products. When several products must be compared or ranked, hand off to the comparison workflow.

## 8. Evidence levels

- `OBSERVED`
- `SUPPORTED`
- `INFERRED`
- `HYPOTHESIS`
- `UNKNOWN`

Never turn `INFERRED` or `HYPOTHESIS` into claimed user experience.

## Attribution

Adapted from the public MIT-licensed `wondelai/skills/jobs-to-be-done` skill.