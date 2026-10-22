#!/usr/bin/env python3
"""Remove unsupported Tier 1 / Tier 2 terminology from brand surfaces.

Default mode applies the migration to the navigation source and every committed
HTML page. Use --check in CI to fail if the old tier concept is reintroduced.
"""
from pathlib import Path
import argparse
import re

BASE = Path(__file__).resolve().parent
SOURCE = BASE / "_generate.py"
FORBIDDEN = ("Tier 1", "Tier 2")
OLD_HUB_INTRO = (
    "Tier 1 : Kärcher, Bosch, Makita, Festool — fabricants avec gammes complètes "
    "et SAV établi. Tier 2 : DeWalt, Parkside, Nilfisk, Mirka."
)
NEW_HUB_INTRO = (
    "Kärcher, Bosch, Makita, Festool, DeWalt, Parkside, Nilfisk et Mirka : "
    "huit univers de gamme à comparer selon l’usage, les classes, les outils "
    "et l’écosystème."
)


def targets():
    yield SOURCE
    for path in BASE.rglob("*.html"):
        if ".git" not in path.parts:
            yield path


def migrate(text: str) -> str:
    # Navigation labels. Different generators produced slightly different
    # indentation, so the migration is intentionally whitespace-agnostic.
    text = re.sub(
        r'[ \t]*<span class="dd-label">Tier 1</span>[ \t]*(?:\r?\n)?',
        '',
        text,
    )
    text = re.sub(
        r'[ \t]*<div class="dd-sep"></div>[ \t]*(?:\r?\n)?[ \t]*'
        r'<span class="dd-label">Tier 2</span>[ \t]*(?:\r?\n)?',
        '',
        text,
    )
    text = re.sub(
        r'[ \t]*<span class="dd-label">Tier 2</span>[ \t]*(?:\r?\n)?',
        '',
        text,
    )

    # Homepage brand cards: keep the useful family information, remove the
    # unsupported hierarchy.
    text = text.replace("Tier 1 · ", "")
    text = text.replace("Tier 2 · ", "")

    # Legacy /marques/ generator copy: replace the ranking language with the
    # audited role of the hub.
    text = text.replace(OLD_HUB_INTRO, NEW_HUB_INTRO)

    return text


def violations():
    bad = []
    for path in targets():
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        hits = [term for term in FORBIDDEN if term in text]
        if hits:
            bad.append((path.relative_to(BASE), hits))
    return bad


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    if not args.check:
        changed = 0
        for path in targets():
            if not path.exists():
                continue
            before = path.read_text(encoding="utf-8")
            after = migrate(before)
            if after != before:
                path.write_text(after, encoding="utf-8")
                changed += 1
        print(f"Updated {changed} files")

    bad = violations()
    if bad:
        print("BRAND_TIER_GUARD: FAIL")
        for path, hits in bad:
            print(f" - {path}: {', '.join(hits)}")
        raise SystemExit(1)

    print("BRAND_TIER_GUARD: PASS — no Tier 1 / Tier 2 terminology remains")


if __name__ == "__main__":
    main()
