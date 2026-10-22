#!/usr/bin/env python3
"""Validate self-referencing fr-FR hreflang on every rendered site page."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
LINK_TAG_RE = re.compile(r"<link\b[^>]*>", re.I)
ATTR_RE = re.compile(r"([:\w-]+)\s*=\s*([\"'])(.*?)\2", re.S)


def attrs(tag: str) -> dict[str, str]:
    return {name.lower(): value for name, _, value in ATTR_RE.findall(tag)}


def is_rel(tag: str, rel_name: str) -> bool:
    return rel_name in attrs(tag).get("rel", "").lower().split()


def page_files():
    for path in sorted(ROOT.rglob("index.html")):
        if any(part.startswith(".") for part in path.relative_to(ROOT).parts[:-1]):
            continue
        if "node_modules" in path.parts:
            continue
        yield path


def main():
    failures = []
    pages = list(page_files())

    for path in pages:
        rel = path.relative_to(ROOT)
        html = path.read_text(encoding="utf-8")
        tags = LINK_TAG_RE.findall(html)
        canonicals = [tag for tag in tags if is_rel(tag, "canonical")]
        fr_alternates = [
            tag for tag in tags
            if is_rel(tag, "alternate") and attrs(tag).get("hreflang", "").lower() == "fr-fr"
        ]

        if len(canonicals) != 1:
            failures.append(f"{rel}: expected 1 canonical, found {len(canonicals)}")
            continue
        canonical_url = attrs(canonicals[0]).get("href")
        if not canonical_url:
            failures.append(f"{rel}: canonical href missing")
            continue
        if len(fr_alternates) != 1:
            failures.append(f"{rel}: expected 1 fr-FR alternate, found {len(fr_alternates)}")
            continue
        alternate_url = attrs(fr_alternates[0]).get("href")
        if alternate_url != canonical_url:
            failures.append(f"{rel}: fr-FR href differs from canonical ({alternate_url!r} != {canonical_url!r})")

    generator = (ROOT / "_generate.py").read_text(encoding="utf-8")
    generator_line = '  <link rel="alternate" hreflang="fr-FR" href="https://bloc-notes-numeriques.fr{canonical}">'
    if generator_line not in generator:
        failures.append("_generate.py: fr-FR hreflang missing from global head template")

    if failures:
        print("FAIL — hreflang validation")
        for failure in failures:
            print(" -", failure)
        raise SystemExit(1)

    print(f"PASS: {len(pages)} pages have one self-referencing hreflang=fr-FR matching canonical")


if __name__ == "__main__":
    main()
