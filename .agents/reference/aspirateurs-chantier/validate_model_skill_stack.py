#!/usr/bin/env python3
"""Validate the shared/custom model skill stack and its 80/20 governance target."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / ".agents" / "skills" / "model-skill-stack.json"
CONFIG = ROOT / "model-workflow.config.yaml"

REQUIRED_DIRECT = {
    "search-intent",
    "content-audit",
    "content-refresh",
    "affiliate-value",
    "fact-check",
    "evidence-based-reviews",
    "content-brief-authoring",
    "content-and-copy",
    "internal-linking-audit",
    "humanizer",
    "general-writing",
    "anti-ai-slop",
    "seo-technical",
    "seo-best-practices",
    "editorial-qa",
}
CUSTOM_ALLOWED = {"model-content-workflow", "model-analysis-workflow"}


def main():
    errors = []

    if not MANIFEST.exists():
        errors.append(f"missing manifest: {MANIFEST.relative_to(ROOT)}")
        data = {}
    else:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))

    governance = data.get("governance", {})
    shared_resp = governance.get("shared_responsibilities", [])
    custom_resp = governance.get("custom_responsibilities", [])
    total = len(shared_resp) + len(custom_resp)
    shared_ratio = len(shared_resp) / total if total else 0.0
    custom_ratio = len(custom_resp) / total if total else 1.0
    shared_min = float(governance.get("target_shared_ratio_min", 0.80))
    custom_max = float(governance.get("target_custom_ratio_max", 0.20))

    if governance.get("ratio_basis") != "workflow_responsibilities":
        errors.append("ratio_basis must be workflow_responsibilities")
    if shared_ratio < shared_min:
        errors.append(
            f"shared responsibility ratio {shared_ratio:.1%} is below target {shared_min:.1%}"
        )
    if custom_ratio > custom_max:
        errors.append(
            f"custom responsibility ratio {custom_ratio:.1%} exceeds target {custom_max:.1%}"
        )
    if not governance.get("require_external_provenance_for_shared_skills"):
        errors.append("shared-skill provenance gate must be enabled")
    if not governance.get("require_run_evidence_before_publish_review_pass"):
        errors.append("run-evidence publish gate must be enabled")

    shared = data.get("shared", [])
    custom = data.get("custom", [])
    shared_names = {item.get("name") for item in shared}
    custom_names = {item.get("name") for item in custom}

    missing = sorted(REQUIRED_DIRECT - shared_names)
    if missing:
        errors.append("missing required shared skills in manifest: " + ", ".join(missing))

    unexpected_custom = sorted(custom_names - CUSTOM_ALLOWED)
    if unexpected_custom:
        errors.append(
            "custom stack exceeds allowed orchestration scope: "
            + ", ".join(unexpected_custom)
        )
    missing_custom = sorted(CUSTOM_ALLOWED - custom_names)
    if missing_custom:
        errors.append("missing custom model orchestrators: " + ", ".join(missing_custom))

    for item in shared + custom:
        name = item.get("name")
        if not name:
            errors.append("manifest entry without name")
            continue

        skill = ROOT / ".agents" / "skills" / name / "SKILL.md"
        if not skill.exists():
            errors.append(f"missing skill: {name}")
            continue

        if name in shared_names and name != "content-recovery-and-production-workflow":
            source_repo = item.get("source_repo")
            source_sha = item.get("source_sha")
            if source_repo != "MarcW88/bloc-notes-numerique" or not source_sha:
                errors.append(f"{name}: missing bloc-notes shared-skill provenance")

            text = skill.read_text(encoding="utf-8")
            if (
                f"source_repo: {source_repo}" not in text
                or f"source_sha: {source_sha}" not in text
            ):
                errors.append(
                    f"{name}: local SKILL.md provenance does not match manifest"
                )

    evidence_item = next(
        (x for x in shared if x.get("name") == "evidence-based-reviews"), {}
    )
    if (
        evidence_item.get("upstream")
        != "rampstackco/claude-skills/skills/evidence-based-reviews"
    ):
        errors.append("evidence-based-reviews upstream provenance missing")

    for workflow in CUSTOM_ALLOWED:
        path = ROOT / ".agents" / "skills" / workflow / "SKILL.md"
        if path.exists():
            text = path.read_text(encoding="utf-8").lower()
            if "80" not in text or "shared" not in text or "custom" not in text:
                errors.append(
                    f"{workflow}: 80/20 shared/custom governance not explicit"
                )
            if "/modeles/" not in text:
                errors.append(f"{workflow}: /modeles/ scope not explicit")

    if not CONFIG.exists():
        errors.append("missing model-workflow.config.yaml")
    else:
        config_text = CONFIG.read_text(encoding="utf-8")
        required_config_markers = [
            'name: "phase_1_governance_only"',
            "modify_existing_model_content: false",
            "migrate_renderer_now: false",
            "legacy_renderer_may_grant_editorial_pass: false",
            "target_shared_ratio_min: 0.80",
            "target_custom_ratio_max: 0.20",
            "prohibit_page_type_templates: true",
            "require_cluster_structure_review: true",
            'derive_valid_slugs_from: ".content/models/model-evidence.json"',
        ]
        for marker in required_config_markers:
            if marker not in config_text:
                errors.append(f"config missing governance marker: {marker}")

    if errors:
        for error in errors:
            print("FAIL", error)
        return 1

    print(
        "PASS: model workflow governance uses "
        f"{len(shared_resp)} shared responsibilities and "
        f"{len(custom_resp)} custom responsibilities; "
        f"shared={shared_ratio:.1%}, custom={custom_ratio:.1%}."
    )
    print(
        f"PASS: {len(shared)} shared skills/components have provenance; "
        f"only {len(custom)} custom model orchestrators are allowed."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
