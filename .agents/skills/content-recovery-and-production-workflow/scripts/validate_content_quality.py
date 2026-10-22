#!/usr/bin/env python3
from pathlib import Path
import re
import html as html_lib
import argparse

TAG_RE = re.compile(r"<[^>]+>", re.S)
H2_RE = re.compile(r'<h2\b[^>]*>(.*?)</h2>', re.S | re.I)
P_RE = re.compile(r"<p\b[^>]*>(.*?)</p>", re.S | re.I)
TABLE_RE = re.compile(r"<table\b.*?</table>", re.S | re.I)
LINK_RE = re.compile(r'<a\b[^>]*href="(/[^\"]+)"', re.I)
SOURCE_LINK_RE = re.compile(r'<a\b[^>]*href="https?://', re.I)

def clean_text(raw):
    raw = TAG_RE.sub(" ", raw)
    raw = html_lib.unescape(raw)
    return re.sub(r"\s+", " ", raw).strip()

def word_count(raw):
    return len(re.findall(r"\b[\wÀ-ÿ'-]+\b", clean_text(raw)))

def article_html(page_html):
    m = re.search(
        r'<article\b[^>]*class="[^"]*content-main[^"]*"[^>]*>(.*?)</article>',
        page_html, re.S | re.I
    )
    return m.group(1) if m else ""

def split_sections(article):
    matches = list(H2_RE.finditer(article))
    result = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i+1].start() if i+1 < len(matches) else len(article)
        result.append((clean_text(m.group(1)), article[start:end]))
    return result

def inspect_page(page, args):
    html = page.read_text(encoding="utf-8")
    article = article_html(html)
    issues = []

    if not article:
        return ["article.content-main absent"]

    if "<!-- Contenu à rédiger -->" in article:
        issues.append("placeholder présent")

    if args.require_noindex and 'name="robots" content="noindex,follow"' not in html:
        issues.append("noindex,follow absent")

    if 'class="article-answer"' not in article:
        issues.append("réponse initiale absente")

    wc = word_count(article)
    if wc < args.min_words:
        issues.append(f"contenu trop court: {wc} < {args.min_words}")

    sections = [(t,b) for t,b in split_sections(article) if "source" not in t.lower()]
    if len(sections) < args.min_h2:
        issues.append(f"H2 substantiels: {len(sections)} < {args.min_h2}")

    for title, body in sections:
        sw = word_count(body)
        pcount = len(P_RE.findall(body))
        has_table = bool(TABLE_RE.search(body))
        has_list = bool(re.search(r"<(?:ul|ol)\b", body, re.I))

        if sw < args.min_section_words:
            issues.append(f"section trop légère: {title} ({sw} mots)")

        if has_table:
            prose = TABLE_RE.sub(" ", body)
            prose_words = sum(word_count(p) for p in P_RE.findall(prose))
            if prose_words < args.min_table_prose:
                issues.append(f"tableau peu contextualisé: {title}")

            first = TABLE_RE.search(body)
            if first:
                if not P_RE.search(body[:first.start()]):
                    issues.append(f"tableau sans contexte avant: {title}")
                if not P_RE.search(body[first.end():]):
                    issues.append(f"tableau sans interprétation après: {title}")

        if pcount == 1 and not has_table and not has_list and sw < args.single_p_min_words:
            issues.append(f"section mono-paragraphe faible: {title} ({sw} mots)")

    internal = LINK_RE.findall(article)
    if len(internal) < args.min_internal_links:
        issues.append(f"maillage interne: {len(internal)} < {args.min_internal_links}")

    unique = len(set(internal))
    if unique < args.min_unique_targets:
        issues.append(f"cibles internes uniques: {unique} < {args.min_unique_targets}")

    sources = len(SOURCE_LINK_RE.findall(article))
    if sources < args.min_sources:
        issues.append(f"sources: {sources} < {args.min_sources}")

    return issues

def main():
    p = argparse.ArgumentParser()
    p.add_argument("content_dir")
    p.add_argument("--min-words", type=int, default=900)
    p.add_argument("--min-h2", type=int, default=5)
    p.add_argument("--min-section-words", type=int, default=70)
    p.add_argument("--min-table-prose", type=int, default=50)
    p.add_argument("--min-internal-links", type=int, default=4)
    p.add_argument("--min-unique-targets", type=int, default=3)
    p.add_argument("--min-sources", type=int, default=3)
    p.add_argument("--single-p-min-words", type=int, default=130)
    p.add_argument("--require-noindex", action="store_true")
    args = p.parse_args()

    failures = {}
    for page in sorted(Path(args.content_dir).glob("*/index.html")):
        issues = inspect_page(page, args)
        if issues:
            failures[page.parent.name] = issues

    if failures:
        for slug, issues in failures.items():
            print(f"FAIL {slug}")
            for issue in issues:
                print(f"  - {issue}")
        raise SystemExit(1)

    print("PASS: structural quality floor met")

if __name__ == "__main__":
    main()
