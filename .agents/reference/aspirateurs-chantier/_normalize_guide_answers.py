#!/usr/bin/env python3
"""Normalize each guide to exactly one answer-first block.

This makes repeated guide generation idempotent even when a previously generated
HTML page already contains the validator-facing nested answer markup.
"""
from pathlib import Path
import re

BASE = Path(__file__).resolve().parent
ARTICLE_RE = re.compile(r'(<article class="content-main">)(.*?)(</article>)', re.S)
RAW_RE = re.compile(r'<div class="article-answer answer-box"><p>(.*?)</p></div>', re.S)
NESTED_RE = re.compile(r'<div class="answer-box"><div class="article-answer"><p>(.*?)</p></div></div>', re.S)


def normalize_page(path: Path) -> None:
    html = path.read_text(encoding="utf-8")
    match = ARTICLE_RE.search(html)
    if not match:
        raise RuntimeError(f"article.content-main missing: {path}")

    body = match.group(2)
    candidates = []
    for pattern in (RAW_RE, NESTED_RE):
        for answer in pattern.finditer(body):
            candidates.append((answer.start(), answer.group(1)))
    if not candidates:
        raise RuntimeError(f"answer-first block missing: {path}")

    candidates.sort(key=lambda item: item[0])
    answer_text = candidates[0][1]
    cleaned = RAW_RE.sub("", body)
    cleaned = NESTED_RE.sub("", cleaned).lstrip()
    normalized = (
        f'\n      <div class="answer-box"><div class="article-answer"><p>{answer_text}</p></div></div>\n'
        + cleaned
    )
    replacement = match.group(1) + normalized + match.group(3)
    html = html[:match.start()] + replacement + html[match.end():]

    if html.count('class="article-answer"') != 1:
        raise RuntimeError(f"expected exactly one article-answer: {path}")

    path.write_text(html, encoding="utf-8")
    print(f"✓ normalized answer: {path.parent.name}")


def main() -> None:
    pages = sorted((BASE / "guides").glob("*/index.html"))
    for page in pages:
        normalize_page(page)
    print(f"\n{len(pages)} guide answer blocks normalized.")


if __name__ == "__main__":
    main()
