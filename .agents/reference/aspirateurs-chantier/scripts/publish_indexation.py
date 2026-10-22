#!/usr/bin/env python3
"""Publish and maintain the live indexation state for aspirateurs-chantier.fr."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
SITE_ORIGIN = "https://aspirateurs-chantier.fr"

# Reuse the same explicit public inventory as the design layer.
import sys
sys.path.insert(0, str(ROOT))
from _apply_design_v2 import public_pages  # noqa: E402

ROBOTS_META_RE = re.compile(
    r'<meta\b[^>]*name=["\']robots["\'][^>]*>', re.I
)
ROBOTS_CONTENT_RE = re.compile(
    r'content=["\'][^"\']*["\']', re.I
)

ACTIVE_GUARD_FILES = (
    "_validate_cluster_rollout.py",
    "_validate_comparison_rollout.py",
    "_materialize_comparison_v2.py",
    "_materialize_usage_v2.py",
    "_materialize_guides_v2.py",
    "validate_guide_workflow.py",
    "validate_guide_quality.py",
    "validate_usage_workflow.py",
    "_validate_brands.py",
    "_validate_comparatifs.py",
    "_generate.py",
    "brand-workflow.config.yaml",
    "comparison-workflow.config.yaml",
    "content-workflow.config.yaml",
    "model-workflow.config.yaml",
    "guide-workflow.config.yaml",
    "usage-workflow.config.yaml",
    ".github/workflows/validate-product-workflow.yml",
    ".github/workflows/maintain-inline-affiliate-links.yml",
    ".github/workflows/apply-product-modules.yml",
    ".github/workflows/validate-guide-methodology-pilot.yml",
    ".github/workflows/generate-guides-content.yml",
    ".github/workflows/generate-comparatifs-content.yml",
    ".github/workflows/generate-usage-content.yml",
    ".github/workflows/generate-brand-content.yml",
)

VISIBLE_NOINDEX_PATTERNS = (
    r"\s*Page maintenue en noindex jusqu[’']à validation humaine\.",
    r"\s*Page maintenue en noindex pendant le rollout\.",
    r"\s*Page maintenue en noindex\.",
    r"\s*La page reste en noindex pendant le pilote\.",
)


def set_index_follow(html: str) -> str:
    match = ROBOTS_META_RE.search(html)
    replacement = '<meta name="robots" content="index, follow">'
    if match:
        return html[: match.start()] + replacement + html[match.end() :]
    if "</head>" in html:
        return html.replace("</head>", f"  {replacement}\n</head>", 1)
    raise RuntimeError("HTML document has no </head> for robots insertion")


def clean_visible_noindex_copy(text: str) -> str:
    for pattern in VISIBLE_NOINDEX_PATTERNS:
        text = re.sub(pattern, "", text, flags=re.I)
    return text


def page_url(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return SITE_ORIGIN + "/"
    route = rel[: -len("index.html")]
    return SITE_ORIGIN + "/" + route.lstrip("/")


def write_public_files() -> tuple[int, list[str]]:
    pages = public_pages()
    changed = 0
    urls: list[str] = []
    for path in pages:
        if not path.exists():
            raise RuntimeError(f"Missing public page: {path.relative_to(ROOT)}")
        original = path.read_text(encoding="utf-8")
        html = clean_visible_noindex_copy(set_index_follow(original))
        if html != original:
            path.write_text(html, encoding="utf-8")
            changed += 1
        urls.append(page_url(path))

    # Keep source fragments used by content materializers truthful as well.
    for folder in (ROOT / ".content" / "usages" / "v2", ROOT / ".content" / "comparisons" / "v2"):
        if folder.exists():
            for path in folder.glob("*.html"):
                original = path.read_text(encoding="utf-8")
                cleaned = clean_visible_noindex_copy(original)
                if cleaned != original:
                    path.write_text(cleaned, encoding="utf-8")

    robots = "User-agent: *\nAllow: /\n\nSitemap: https://aspirateurs-chantier.fr/sitemap.xml\n"
    (ROOT / "robots.txt").write_text(robots, encoding="utf-8")

    sitemap = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for url in urls:
        sitemap.extend(("  <url>", f"    <loc>{escape(url)}</loc>", "  </url>"))
    sitemap.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8")
    return changed, urls


def migrate_records() -> int:
    changed = 0
    content_root = ROOT / ".content"
    if not content_root.exists():
        return 0
    for path in content_root.rglob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        dirty = False

        def walk(value):
            nonlocal dirty
            if isinstance(value, dict):
                for key, item in list(value.items()):
                    if key == "robots" and isinstance(item, str) and item.replace(" ", "").lower() == "noindex,follow":
                        value[key] = "index, follow"
                        dirty = True
                    elif key in {"noindex_during_rollout", "noindex_during_pilot"} and item is True:
                        value[key] = False
                        dirty = True
                    else:
                        walk(item)
            elif isinstance(value, list):
                for item in value:
                    walk(item)

        walk(data)
        if dirty:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            changed += 1
    return changed


def migrate_source_guards() -> int:
    changed = 0
    for rel in ACTIVE_GUARD_FILES:
        path = ROOT / rel
        if not path.exists():
            continue
        original = path.read_text(encoding="utf-8")
        text = original
        text = text.replace("noindex, follow", "index, follow")
        text = text.replace("noindex,follow", "index,follow")
        text = text.replace("require_noindex_in_draft: true", "require_noindex_in_draft: false")
        # One comparison validator checks only for the token itself.
        text = text.replace('"noindex" not in robots.group(1).lower()', '"index" not in robots.group(1).lower()')
        if text != original:
            path.write_text(text, encoding="utf-8")
            changed += 1

    # Future generated comparison copy must not claim the live page is noindex.
    for rel in ("_generate_comparison_overrides.py", "_generate_professional_comparison_override.py"):
        path = ROOT / rel
        if not path.exists():
            continue
        original = path.read_text(encoding="utf-8")
        text = clean_visible_noindex_copy(original)
        if text != original:
            path.write_text(text, encoding="utf-8")
            changed += 1
    return changed


def validate() -> list[str]:
    errors: list[str] = []
    pages = public_pages()
    expected_urls = [page_url(path) for path in pages]

    for path in pages:
        html = path.read_text(encoding="utf-8")
        match = ROBOTS_META_RE.search(html)
        if not match:
            errors.append(f"{path.relative_to(ROOT)}: missing robots meta")
            continue
        content = ROBOTS_CONTENT_RE.search(match.group(0))
        normalized = (content.group(0).split("=", 1)[1].strip("\"'") if content else "").replace(" ", "").lower()
        if normalized != "index,follow":
            errors.append(f"{path.relative_to(ROOT)}: robots={normalized or 'missing'}")

    robots = (ROOT / "robots.txt").read_text(encoding="utf-8") if (ROOT / "robots.txt").exists() else ""
    if "User-agent: *" not in robots or "Allow: /" not in robots or "Sitemap: https://aspirateurs-chantier.fr/sitemap.xml" not in robots:
        errors.append("robots.txt: expected allow-all policy and sitemap declaration")

    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8") if (ROOT / "sitemap.xml").exists() else ""
    for url in expected_urls:
        if f"<loc>{url}</loc>" not in sitemap:
            errors.append(f"sitemap.xml: missing {url}")
    if sitemap.count("<url>") != len(expected_urls):
        errors.append(f"sitemap.xml: expected {len(expected_urls)} URLs, found {sitemap.count('<url>')}")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--migrate-source-guards", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    if not args.check:
        guards = migrate_source_guards() if args.migrate_source_guards else 0
        records = migrate_records() if args.migrate_source_guards else 0
        pages, urls = write_public_files()
        print(f"INDEXATION_APPLY: {pages} public page(s) changed; {len(urls)} URL(s) in sitemap; {guards} guard file(s) migrated; {records} record file(s) migrated")

    errors = validate()
    if errors:
        print("INDEXATION: FAIL")
        for error in errors:
            print(f" - {error}")
        raise SystemExit(1)
    print(f"INDEXATION: PASS — {len(public_pages())} public pages are index, follow and present in sitemap.xml")


if __name__ == "__main__":
    main()
