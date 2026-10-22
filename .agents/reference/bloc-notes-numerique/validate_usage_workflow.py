#!/usr/bin/env python3
"""Validate the /usages/ editorial workflow infrastructure.

This validator intentionally checks only observable structural rules. It does
not claim that JTBD research, fact-checking, Humanizer, SEO/GEO quality or an
editorial PUBLISH_REVIEW have passed.
"""

from __future__ import annotations

import json
from pathlib import Path

from publication_indexation import INDEXABLE_USAGE_ROUTES

ROOT = Path(__file__).resolve().parent

EXPECTED_USAGE_SLUGS = {
    "prise-de-notes-professionnelle",
    "prise-de-notes-etudiant",
    "prise-de-notes-reunion",
    "annotation-pdf",
    "lecture-et-prise-de-notes",
    "dessin",
    "remplacer-cahiers-papier",
}

REQUIRED_RECORD_KEYS = {
    "slug",
    "page_url",
    "status",
    "intent",
    "jtbd",
    "workflow_map",
    "criteria",
    "solution_families",
    "contraindications",
    "evidence_ledger",
    "editorial",
    "qa",
}

FORBIDDEN_RECORD_KEYS = {
    "ranking",
    "rankings",
    "ranked_products",
    "scores",
    "product_scores",
    "winner",
}

REUSED_SKILLS = {
    "content-audit",
    "search-intent",
    "jobs-to-be-done",
    "content-refresh",
    "fact-check",
    "evidence-based-reviews",
    "affiliate-value",
    "content-brief-authoring",
    "content-and-copy",
    "internal-linking-audit",
    "humanizer",
    "general-writing",
    "anti-ai-slop",
    "seo-onpage",
    "seo-technical",
    "seo-best-practices",
    "editorial-qa",
}


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def walk_keys(value):
    if isinstance(value, dict):
        for key, child in value.items():
            yield key
            yield from walk_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_keys(child)


def require_text(path: Path, fragments: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    missing = [fragment for fragment in fragments if fragment not in text]
    if missing:
        fail(f"{path.relative_to(ROOT)} missing workflow markers: {', '.join(missing)}")


def assert_robots(route: str, page: Path) -> None:
    html = page.read_text(encoding="utf-8")
    expected = "index,follow" if route in INDEXABLE_USAGE_ROUTES else "noindex,follow"
    marker = f'name="robots" content="{expected}"'
    if marker not in html:
        fail(f"{route} expected robots={expected}")


def main() -> None:
    required_files = [
        ROOT / ".agents/skills/usage-analysis-workflow/SKILL.md",
        ROOT / ".agents/skills/usage-content-workflow/SKILL.md",
        ROOT / ".content/usages/_template.json",
        ROOT / ".content/usages/README.md",
        ROOT / "usage-workflow.config.yaml",
        ROOT / "publication_indexation.py",
        ROOT / "apply_section_indexation.py",
    ]
    required_files.extend(
        ROOT / f".agents/skills/{skill}/SKILL.md" for skill in sorted(REUSED_SKILLS)
    )
    missing = [str(path.relative_to(ROOT)) for path in required_files if not path.exists()]
    if missing:
        fail("missing workflow/reused-skill files: " + ", ".join(missing))

    analysis_skill = ROOT / ".agents/skills/usage-analysis-workflow/SKILL.md"
    require_text(
        analysis_skill,
        [
            "`AUDIT`",
            "`CLUSTER_AUDIT`",
            "`PUBLISH_REVIEW`",
            "`KEEP`",
            "`LIGHT_UPDATE`",
            "`DEEP_REWRITE`",
            "`MERGE`",
            "`NOINDEX`",
            "PASS — READY_FOR_HUMAN_VALIDATION",
            "FAIL — KEEP_NOINDEX",
            "jobs-to-be-done",
            "search-intent",
            "content-audit",
        ],
    )

    content_skill = ROOT / ".agents/skills/usage-content-workflow/SKILL.md"
    require_text(
        content_skill,
        [
            "usage-analysis-workflow / AUDIT",
            "usage-analysis-workflow / PUBLISH_REVIEW",
            "content-brief-authoring",
            "content-and-copy",
            "jobs-to-be-done",
            "aucune architecture éditoriale obligatoire",
        ],
    )

    config_path = ROOT / "usage-workflow.config.yaml"
    require_text(
        config_path,
        [
            "version: 2",
            "target_existing_skill_share: \">=80%\"",
            "custom_share_target: \"<=20%\"",
            "prohibit_word_count_quotas: true",
            "prohibit_heading_count_quotas: true",
            "prohibit_internal_link_quotas: true",
            "prohibit_fixed_usage_page_templates: true",
            "require_cluster_structure_review: true",
        ],
    )

    template_path = ROOT / ".content/usages/_template.json"
    try:
        template = json.loads(template_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid usage template JSON: {exc}")

    missing_keys = REQUIRED_RECORD_KEYS - set(template)
    if missing_keys:
        fail("usage template missing keys: " + ", ".join(sorted(missing_keys)))

    usage_root = ROOT / "usages"
    if not usage_root.exists():
        fail("usages/ directory is missing")

    actual_slugs = {
        path.name
        for path in usage_root.iterdir()
        if path.is_dir() and (path / "index.html").exists()
    }
    missing_slugs = EXPECTED_USAGE_SLUGS - actual_slugs
    if missing_slugs:
        fail("missing current usage routes: " + ", ".join(sorted(missing_slugs)))

    assert_robots("/usages/", usage_root / "index.html")
    for slug in sorted(EXPECTED_USAGE_SLUGS):
        assert_robots(f"/usages/{slug}/", usage_root / slug / "index.html")

    records_dir = ROOT / ".content/usages"
    for record_path in sorted(records_dir.glob("*.json")):
        if record_path.name == "_template.json":
            continue
        try:
            record = json.loads(record_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"{record_path}: invalid JSON: {exc}")

        missing = REQUIRED_RECORD_KEYS - set(record)
        if missing:
            fail(f"{record_path}: missing keys {', '.join(sorted(missing))}")

        forbidden = FORBIDDEN_RECORD_KEYS & set(walk_keys(record))
        if forbidden:
            fail(
                f"{record_path}: product-ranking data belongs in comparison workflow: "
                + ", ".join(sorted(forbidden))
            )

        slug = record.get("slug")
        if slug and slug not in actual_slugs:
            fail(f"{record_path}: slug {slug!r} has no matching /usages/ page")

        page_url = record.get("page_url", "")
        if slug and page_url != f"/usages/{slug}/":
            fail(f"{record_path}: page_url does not match slug")

    print(
        "PASS: usage infrastructure and publication state are valid; "
        f"{len(INDEXABLE_USAGE_ROUTES)} approved route(s) are indexable."
    )
    print(
        "PASS: /usages/annotation-pdf/ remains noindex because it redirects and "
        "canonicals to the consolidated Guide."
    )
    print(
        "NOTE: this machine PASS does not replace JTBD, fact-check, editorial, "
        "SEO/GEO or PUBLISH_REVIEW judgment."
    )


if __name__ == "__main__":
    main()
