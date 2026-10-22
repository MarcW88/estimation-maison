---
name: seo-best-practices
description: Practical on-page and implementation SEO conventions, applied only when relevant to the detected project stack.
license: MIT
metadata:
  source_repo: MarcW88/bloc-notes-numerique
  source_sha: 19f1fa2da56ec71ecf1b2df9854397ac50ccbc24
  adaptation: stack-neutralized
---

# SEO Best Practices

Use as a practical implementation checklist after detecting the project type.

## Check when applicable
- unique and intent-aligned title and meta description;
- correct canonical and robots directives;
- one clear H1 and useful semantic heading hierarchy;
- descriptive internal anchors;
- semantic HTML and accessible image alt text;
- honest BreadcrumbList / Article / Product or other structured data only when supported by visible content;
- mobile viewport and content parity;
- appropriate image dimensions/lazy loading and major performance hygiene;
- sitemap and robots consistency for indexable pages.

Do not impose character counts, heading counts, keyword density or framework-specific rules as universal quality gates. React/Laravel/SPA checks are N/A on static HTML unless the stack actually uses them.

Output PASS / FAIL / N/A with concrete evidence and prioritize only issues that can affect crawlability, understanding, trust or search presentation.
