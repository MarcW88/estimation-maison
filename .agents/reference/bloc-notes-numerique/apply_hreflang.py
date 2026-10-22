#!/usr/bin/env python3
"""Ensure a self-referencing fr-FR hreflang on every rendered site page."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
LINK_TAG_RE = re.compile(r"<link\b[^>]*>", re.I)
ATTR_RE = re.compile(r"([:\w-]+)\s*=\s*([\"'])(.*?)\2", re.S)


def attrs(tag: str) -> dict[str, str]:
    return {name.lower(): value for name, _, value in ATTR_RE.findall(tag)}


def is_rel(tag: str, rel_name: str) -> bool:
    values = attrs(tag).get("rel", "").lower().split()
    return rel_name in values


def page_files():
    for path in sorted(ROOT.rglob("index.html")):
        if any(part.startswith(".") for part in path.relative_to(ROOT).parts[:-1]):
            continue
        if "node_modules" in path.parts:
            continue
        yield path


def ensure_page(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    link_tags = LINK_TAG_RE.findall(html)
    canonicals = [tag for tag in link_tags if is_rel(tag, "canonical")]
    if len(canonicals) != 1:
        raise RuntimeError(f"{path.relative_to(ROOT)}: expected exactly one canonical, found {len(canonicals)}")

    canonical_tag = canonicals[0]
    canonical_url = attrs(canonical_tag).get("href")
    if not canonical_url:
        raise RuntimeError(f"{path.relative_to(ROOT)}: canonical href missing")

    alternates = [
        tag for tag in link_tags
        if is_rel(tag, "alternate") and attrs(tag).get("hreflang", "").lower() == "fr-fr"
    ]
    desired = f'<link rel="alternate" hreflang="fr-FR" href="{canonical_url}">'

    if len(alternates) == 1 and attrs(alternates[0]).get("href") == canonical_url:
        return False

    if len(alternates) == 1:
        html = html.replace(alternates[0], desired, 1)
    else:
        for alternate in alternates:
            html = html.replace(alternate, "", 1)
        canonical_pos = html.find(canonical_tag)
        if canonical_pos < 0:
            raise RuntimeError(f"{path.relative_to(ROOT)}: canonical tag changed unexpectedly")
        line_start = html.rfind("\n", 0, canonical_pos) + 1
        indent = html[line_start:canonical_pos]
        html = html.replace(canonical_tag, f"{canonical_tag}\n{indent}{desired}", 1)

    path.write_text(html, encoding="utf-8")
    return True


def ensure_generator_template() -> bool:
    path = ROOT / "_generate.py"
    text = path.read_text(encoding="utf-8")
    hreflang_line = '  <link rel="alternate" hreflang="fr-FR" href="https://bloc-notes-numeriques.fr{canonical}">'
    if hreflang_line in text:
        return False

    canonical_line = '  <link rel="canonical" href="https://bloc-notes-numeriques.fr{canonical}">'
    count = text.count(canonical_line)
    if count != 1:
        raise RuntimeError(f"_generate.py: expected one global canonical template line, found {count}")

    text = text.replace(canonical_line, canonical_line + "\n" + hreflang_line, 1)
    path.write_text(text, encoding="utf-8")
    return True


def main():
    changed = []
    for path in page_files():
        if ensure_page(path):
            changed.append(str(path.relative_to(ROOT)))

    generator_changed = ensure_generator_template()
    print(f"hreflang fr-FR ensured on {sum(1 for _ in page_files())} pages")
    print(f"updated rendered pages: {len(changed)}")
    print(f"updated _generate.py template: {'yes' if generator_changed else 'no'}")


if __name__ == "__main__":
    main()
