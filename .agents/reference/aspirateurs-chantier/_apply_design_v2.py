#!/usr/bin/env python3
"""Apply the Editorial V2 shell and normalize CSS assets on all public pages.

Idempotent by design: generators can run first, then this script restores the
shared body classes and ensures every public page points to one CSS entry point:
/style.css. The entry point preserves the existing cascade through the generated
bundle.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
SECTIONS = ("accessoires", "comparatifs", "guides", "marques", "modeles", "usages")
STATIC = (
    "a-propos/index.html",
    "contact/index.html",
    "mentions-legales/index.html",
    "methode-de-test/index.html",
    "transparence-affiliation/index.html",
)

SINGLE_STYLESHEET = "/style.css"
LEGACY_STYLESHEETS = (
    "/comparison-pages.css",
    "/brand-pages.css",
    "/design-v2.css",
    "/design-v2-rollout.css",
    "/assets/product-cards.css",
    "/assets/inline-affiliate.css",
    "/home-model-polish.css",
    "/model-pages-v3.css",
    "/home-hero-refresh.css",
)


def page_classes(rel: str) -> list[str]:
    if rel == "index.html":
        return ["design-v2", "design-home"]

    parts = Path(rel).parts
    section = parts[0]
    is_hub = len(parts) == 2 and parts[1] == "index.html"

    if section == "comparatifs":
        return ["design-v2", "design-hub", "design-comparison-hub"] if is_hub else ["design-v2", "design-comparison"]
    if section == "guides":
        return ["design-v2", "design-hub", "design-guide-hub"] if is_hub else ["design-v2", "design-guide"]
    if section == "modeles":
        return ["design-v2", "design-hub", "design-model-hub"] if is_hub else ["design-v2", "design-model"]
    if section == "marques":
        return ["design-v2", "design-hub", "design-brand-hub"] if is_hub else ["design-v2", "design-brand"]
    if section == "usages":
        return ["design-v2", "design-hub", "design-usage-hub"] if is_hub else ["design-v2", "design-usage"]
    if section == "accessoires":
        return ["design-v2", "design-hub", "design-accessory-hub"] if is_hub else ["design-v2", "design-accessory"]
    return ["design-v2", "design-static"]


def merge_body_classes(html: str, wanted: list[str]) -> str:
    match = re.search(r"<body(?:\s+class=\"([^\"]*)\")?\s*>", html, flags=re.I)
    if not match:
        return html
    existing = (match.group(1) or "").split()
    classes = existing[:]
    for cls in wanted:
        if cls not in classes:
            classes.append(cls)
    replacement = '<body class="' + " ".join(classes) + '">'
    return html[: match.start()] + replacement + html[match.end() :]


def strip_stylesheet(html: str, href: str) -> str:
    pattern = re.compile(
        rf'^[ \t]*<link\b(?=[^>]*\brel=["\']stylesheet["\'])(?=[^>]*\bhref=["\']{re.escape(href)}["\'])[^>]*>\s*$',
        flags=re.I | re.M,
    )
    return pattern.sub("", html)


def normalize_stylesheets(html: str) -> str:
    # Already-normalized pages must be byte-for-byte stable. This guard also
    # prevents whitespace drift when the applicator is run repeatedly in CI.
    if html.count(SINGLE_STYLESHEET) == 1 and not any(href in html for href in LEGACY_STYLESHEETS):
        return html

    # Legacy/generated pages are migrated to one canonical site stylesheet.
    # External preconnect/font links are intentionally left untouched.
    html = strip_stylesheet(html, SINGLE_STYLESHEET)
    for href in LEGACY_STYLESHEETS:
        html = strip_stylesheet(html, href)

    tag = f'  <link rel="stylesheet" href="{SINGLE_STYLESHEET}">'
    if "</head>" not in html:
        return html
    return html.replace("</head>", tag + "\n</head>", 1)


def ensure_assets(html: str) -> str:
    html = normalize_stylesheets(html)
    if '/design-v2.js' not in html:
        html = html.replace('</body>', '  <script src="/design-v2.js" defer></script>\n</body>', 1)
    return html


def public_pages() -> list[Path]:
    pages = [ROOT / "index.html"]
    for section in SECTIONS:
        base = ROOT / section
        if base.exists():
            pages.extend(sorted(base.rglob("index.html")))
    pages.extend(ROOT / rel for rel in STATIC)
    # Deduplicate while preserving deterministic order.
    return list(dict.fromkeys(pages))


def apply_page(path: Path) -> bool:
    if not path.exists():
        return False
    rel = path.relative_to(ROOT).as_posix()
    original = path.read_text(encoding="utf-8")
    html = merge_body_classes(original, page_classes(rel))
    html = ensure_assets(html)
    if html == original:
        return False
    path.write_text(html, encoding="utf-8")
    print(f"✓ {rel}: {' '.join(page_classes(rel))}")
    return True


def main() -> None:
    pages = public_pages()
    changed = sum(apply_page(path) for path in pages)
    print(f"Editorial V2 applied: {changed} page(s) changed; {len(pages)} page(s) checked.")


if __name__ == "__main__":
    main()
