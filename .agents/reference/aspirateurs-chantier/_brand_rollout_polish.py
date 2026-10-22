#!/usr/bin/env python3
"""Small editorial polish pass for bespoke brand renders."""
from pathlib import Path

BASE = Path(__file__).resolve().parent

REPLACEMENTS = {
    "dewalt": {
        "Cette distinction est précisément le type de raccourci que notre méthodologie interdit.":
        "Un filtre HEPA et une classe de poussière répondent à deux classifications différentes : il faut donc vérifier les deux séparément.",
    },
}


def main():
    for slug, replacements in REPLACEMENTS.items():
        path = BASE / "marques" / slug / "index.html"
        html = path.read_text(encoding="utf-8")
        for old, new in replacements.items():
            if old not in html:
                raise RuntimeError(f"{slug}: expected polish text not found: {old}")
            html = html.replace(old, new, 1)
        path.write_text(html, encoding="utf-8")
        print(f"✓ editorial polish: {slug}")


if __name__ == "__main__":
    main()
