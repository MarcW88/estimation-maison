#!/usr/bin/env python3
"""Apply verified trust copy to the existing static page shells only.

This intentionally does not run _generate.py: other page families have their own
rendering workflows and must not be regenerated as a side effect.
"""

from __future__ import annotations

import re
from pathlib import Path

from trust_content import TRUST_CONTENT, TRUST_PAGE_META

ROOT = Path(__file__).resolve().parent


def replace_once(text: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.DOTALL)
    if count != 1:
        raise RuntimeError(f"Could not replace {label}: expected 1 match, got {count}")
    return updated


def patch_page(path: str) -> None:
    page = ROOT / path.strip("/") / "index.html"
    text = page.read_text(encoding="utf-8")
    meta = TRUST_PAGE_META[path]
    body = TRUST_CONTENT[path].strip()

    text = replace_once(text, r"<title>.*?</title>", f"<title>{meta['title']} — bloc-notes numériques.fr</title>", f"title {path}")
    text = replace_once(
        text,
        r'<meta name="description" content=".*?">',
        f'<meta name="description" content="{meta["description"]}">',
        f"description {path}",
    )
    text = replace_once(text, r"<h1>.*?</h1>", f"<h1>{meta['title']}</h1>", f"h1 {path}")
    text = replace_once(text, r'<p class="lead">.*?</p>', f'<p class="lead">{meta["description"]}</p>', f"lead {path}")
    text = replace_once(
        text,
        r'<span class="page-meta-item">.*?</span>',
        f'<span class="page-meta-item">{meta["status_label"]}</span>',
        f"status {path}",
    )
    text = replace_once(
        text,
        r'(<article class="content-main">).*?(</article>)',
        rf'\1\n      {body}\n    \2',
        f"article {path}",
    )
    text = replace_once(
        text,
        r'<p class="affiliation-note">.*?</p>',
        '<p class="affiliation-note">Certains liens sont affiliés. Les commissions n\'entrent pas dans nos scores ni classements. <a href="/transparence-affiliation/">En savoir plus.</a></p>',
        f"affiliate note {path}",
    )
    text = text.replace(">Méthode de test</a>", ">Méthode d’évaluation</a>")

    page.write_text(text, encoding="utf-8")
    print(f"✓ {path}")


def patch_pending_about() -> None:
    """Remove unsupported team/test language while keeping the page explicitly pending."""
    page = ROOT / "a-propos" / "index.html"
    text = page.read_text(encoding="utf-8")
    text = replace_once(
        text,
        r'<meta name="description" content=".*?">',
        '<meta name="description" content="Présentation de l’éditeur et des choix éditoriaux du site — informations en cours de confirmation.">',
        "pending about description",
    )
    text = replace_once(
        text,
        r'<p class="lead">.*?</p>',
        '<p class="lead">Cette page présentera l’éditeur du site, son parcours et ses règles éditoriales une fois ces informations confirmées.</p>',
        "pending about lead",
    )
    text = replace_once(
        text,
        r'<p class="affiliation-note">.*?</p>',
        '<p class="affiliation-note">Ce site contient des liens affiliés. Leur rôle dans le financement et les classements est détaillé dans notre <a href="/transparence-affiliation/">politique de transparence</a>.</p>',
        "pending about affiliate note",
    )
    text = text.replace(">Méthode de test</a>", ">Méthode d’évaluation</a>")
    page.write_text(text, encoding="utf-8")
    print("✓ /a-propos/ (placeholder neutralized; content still pending)")


def main() -> int:
    for path in TRUST_CONTENT:
        patch_page(path)
    patch_pending_about()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
