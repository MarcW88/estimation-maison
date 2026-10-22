#!/usr/bin/env python3
"""
Structural quality gate for brand pages.

Checks observable structure only.
Does not prove fact-check, GEO quality, humanization, or real testing.
"""

from pathlib import Path
import argparse
import re
import html as html_lib

TAG_RE = re.compile(r"<[^>]+>", re.S)
H2_RE = re.compile(r"<h2\b[^>]*>(.*?)</h2>", re.S | re.I)
LINK_RE = re.compile(r'<a\b[^>]*href="(/[^\"]+)"', re.I)
SOURCE_RE = re.compile(r'<a\b[^>]*href="https?://', re.I)

def clean(raw):
    raw = TAG_RE.sub(" ", raw)
    raw = html_lib.unescape(raw)
    return re.sub(r"\s+", " ", raw).strip()

def article(html):
    m = re.search(
        r'<article\b[^>]*class="[^"]*content-main[^"]*"[^>]*>(.*?)</article>',
        html, re.S | re.I
    )
    return m.group(1) if m else ""

def inspect(page, args):
    html = page.read_text(encoding="utf-8")
    body = article(html)
    issues = []

    if not body:
        return ["article.content-main absent"]

    if args.require_noindex and re.search(r'name="robots"\s+content="noindex,\s*follow"', html, re.I) is None:
        issues.append("noindex,follow absent")

    if "<!-- Contenu à rédiger -->" in body:
        issues.append("placeholder présent")

    h2s = [clean(x).lower() for x in H2_RE.findall(body)]

    if len(h2s) < args.min_h2:
        issues.append(f"H2 insuffisants: {len(h2s)} < {args.min_h2}")

    joined = " ".join(h2s)

    if args.require_limits and not any(k in joined for k in ["limite", "à éviter", "éviter", "inconvénient"]):
        issues.append("section de limites absente")

    if args.require_choose_avoid:
        text = clean(body).lower()
        if not any(k in text for k in ["choisissez", "à privilégier", "convient si", "pour qui"]):
            issues.append("bloc 'choose' absent")
        if not any(k in text for k in ["évitez", "à éviter", "convient moins", "moins adapté"]):
            issues.append("bloc 'avoid' absent")

    internal = LINK_RE.findall(body)
    unique = set(internal)

    if len(internal) < args.min_internal_links:
        issues.append(f"maillage interne trop faible: {len(internal)} < {args.min_internal_links}")

    if len(unique) < args.min_unique_targets:
        issues.append(f"cibles uniques insuffisantes: {len(unique)} < {args.min_unique_targets}")

    sources = len(SOURCE_RE.findall(body))
    if sources < args.min_sources:
        issues.append(f"sources insuffisantes: {sources} < {args.min_sources}")

    text = clean(body).lower()

    fake_test_terms = [
        "nous avons testé",
        "lors de notre test",
        "pendant notre test",
        "après plusieurs semaines d'utilisation",
    ]
    if any(term in text for term in fake_test_terms) and "méthodologie de test" not in text:
        issues.append("langage de test détecté sans preuve structurelle de méthodologie")

    return issues

def main():
    p = argparse.ArgumentParser()
    p.add_argument("content_dir")
    p.add_argument("--min-h2", type=int, default=7)
    p.add_argument("--min-internal-links", type=int, default=6)
    p.add_argument("--min-unique-targets", type=int, default=5)
    p.add_argument("--min-sources", type=int, default=3)
    p.add_argument("--require-noindex", action="store_true")
    p.add_argument("--require-limits", action="store_true")
    p.add_argument("--require-choose-avoid", action="store_true")
    args = p.parse_args()

    failures = {}

    for page in sorted(Path(args.content_dir).glob("*/index.html")):
        issues = inspect(page, args)
        if issues:
            failures[page.parent.name] = issues

    if failures:
        for slug, issues in failures.items():
            print(f"FAIL {slug}")
            for issue in issues:
                print("  -", issue)
        raise SystemExit(1)

    print("PASS: brand structural quality floor met")

if __name__ == "__main__":
    main()
