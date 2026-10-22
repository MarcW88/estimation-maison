#!/usr/bin/env python3
"""Validate /usages/ workflow governance and structural safety.

This is deliberately a machine floor, not an editorial/JTBD reviewer. It checks the
80/20 skill contract, provenance, authored-source/record presence, publish-review
contract shape, known usage routes and draft robots state. Substantive decisions remain
in usage-analysis-workflow and the shared skills.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
STACK = ROOT / ".agents" / "skills" / "usage-skill-stack.json"
CONFIG = ROOT / "usage-workflow.config.yaml"
ANALYSIS = ROOT / ".agents" / "skills" / "usage-analysis-workflow" / "SKILL.md"
CONTENT = ROOT / ".agents" / "skills" / "usage-content-workflow" / "SKILL.md"
V2 = ROOT / ".content" / "usages" / "v2"
RENDER_MAP = V2 / "render-map.json"

USAGE_SLUGS = [
    "aspirateur-atelier",
    "aspirateur-bois-sciure-copeaux",
    "aspirateur-bricolage-renovation",
    "aspirateur-gravats",
    "aspirateur-platre",
    "aspirateur-ponceuse",
    "aspirateur-scie",
]

EXPECTED_CUSTOM_EXECUTION = {"usage-analysis-workflow", "usage-content-workflow"}
REQUIRED_SHARED_EXECUTION = {
    "content-audit",
    "search-intent",
    "jobs-to-be-done",
    "content-refresh",
    "fact-check",
    "evidence-based-reviews",
    "affiliate-value",
    "content-brief-authoring",
    "content-and-copy",
    "humanizer",
    "general-writing",
    "anti-ai-slop",
    "internal-linking-audit",
    "seo-onpage",
    "seo-technical",
    "seo-best-practices",
    "editorial-qa",
}

errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


check(STACK.exists(), "missing usage-skill-stack.json")
check(CONFIG.exists(), "missing usage-workflow.config.yaml")
check(ANALYSIS.exists(), "missing usage-analysis-workflow/SKILL.md")
check(CONTENT.exists(), "missing usage-content-workflow/SKILL.md")
check(RENDER_MAP.exists(), "missing .content/usages/v2/render-map.json")

stack = {}
shared_resp = []
custom_resp = []
total = 0
shared_ratio = 0
custom_ratio = 1
if STACK.exists():
    stack = json.loads(STACK.read_text(encoding="utf-8"))
    gov = stack.get("governance", {})
    shared_resp = gov.get("shared_responsibilities", [])
    custom_resp = gov.get("custom_responsibilities", [])
    total = len(shared_resp) + len(custom_resp)
    shared_ratio = len(shared_resp) / total if total else 0
    custom_ratio = len(custom_resp) / total if total else 1
    check(shared_ratio >= float(gov.get("target_shared_ratio_min", 0.8)), f"shared responsibility ratio too low: {shared_ratio:.1%}")
    check(custom_ratio <= float(gov.get("target_custom_ratio_max", 0.2)), f"custom responsibility ratio too high: {custom_ratio:.1%}")

    shared = stack.get("shared", [])
    custom = stack.get("custom", [])
    check(len(custom) == 2, f"expected exactly 2 custom usage orchestrators, got {len(custom)}")
    check({x.get("name") for x in custom} == EXPECTED_CUSTOM_EXECUTION, "custom usage skills must be exactly the two workflow orchestrators")

    for item in shared:
        name = item.get("name")
        check(bool(name), "shared skill without name")
        check(item.get("source_repo") == "MarcW88/bloc-notes-numerique", f"{name}: shared provenance must pass through MarcW88/bloc-notes-numerique")
        check(bool(item.get("source_sha")), f"{name}: missing source_sha provenance")
        skill_file = ROOT / ".agents" / "skills" / str(name) / "SKILL.md"
        check(skill_file.exists(), f"{name}: shared skill missing locally")

for path in [ANALYSIS, CONTENT]:
    if path.exists():
        text = path.read_text(encoding="utf-8")
        check("source_repo: MarcW88/bloc-notes-numerique" in text, f"{path}: source workflow provenance missing")
        check('orchestration_target: ">=80% existing skills"' in text, f"{path}: 80/20 orchestration target missing")

if RENDER_MAP.exists():
    render_map = json.loads(RENDER_MAP.read_text(encoding="utf-8"))
    check(set(render_map) == set(USAGE_SLUGS), "usage v2 render-map must contain exactly the 7 audited usage slugs")

for slug in USAGE_SLUGS:
    page = ROOT / "usages" / slug / "index.html"
    fragment = V2 / f"{slug}.html"
    record_path = ROOT / ".content" / "usages" / f"{slug}.json"

    check(page.exists(), f"{slug}: usage page missing")
    check(fragment.exists(), f"{slug}: authored v2 fragment missing")
    check(record_path.exists(), f"{slug}: workflow record missing")

    if page.exists():
        html = page.read_text(encoding="utf-8")
        check('<meta name="robots" content="index, follow">' in html, f"{slug}: draft noindex/follow missing")
        h1_count = len(re.findall(r"<h1\b", html, flags=re.I))
        check(h1_count == 1, f"{slug}: expected exactly one H1, got {h1_count}")

    if fragment.exists():
        body = fragment.read_text(encoding="utf-8")
        check("<h1" not in body.lower(), f"{slug}: authored fragment must not contain its own H1")
        check(len(re.findall(r"<h2\b", body, flags=re.I)) >= 4, f"{slug}: authored fragment unexpectedly shallow")

    if record_path.exists():
        try:
            record = json.loads(record_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{slug}: invalid JSON workflow record: {exc}")
            continue
        check(record.get("slug") == slug, f"{slug}: record slug mismatch")
        check(bool(record.get("intent", {}).get("user_job")), f"{slug}: user_job missing")
        check(bool(record.get("jtbd", {}).get("circumstances")), f"{slug}: JTBD circumstances missing")
        check(bool(record.get("criteria")), f"{slug}: criteria missing")
        check(bool(record.get("evidence")), f"{slug}: evidence ledger missing")
        check(bool(record.get("outline")), f"{slug}: evidence-led outline missing")

        execution = record.get("workflow_execution", {})
        shared_steps = execution.get("shared", [])
        custom_steps = execution.get("custom", [])
        shared_names = {step.get("skill") for step in shared_steps}
        custom_names = {step.get("skill") for step in custom_steps}
        check(REQUIRED_SHARED_EXECUTION <= shared_names, f"{slug}: missing required shared-skill execution evidence")
        check(custom_names == EXPECTED_CUSTOM_EXECUTION, f"{slug}: custom execution must be exactly the 2 usage orchestrators")
        for step in shared_steps + custom_steps:
            status = step.get("status")
            check(status in {"PASS", "N/A"}, f"{slug}: invalid workflow step status for {step.get('skill')}")
            if status == "PASS":
                check(bool(step.get("output")), f"{slug}: PASS step {step.get('skill')} missing output")
            if status == "N/A":
                check(bool(step.get("reason")), f"{slug}: N/A step {step.get('skill')} missing reason")

        editorial = record.get("editorial", {})
        check(editorial.get("publish_review") == "PASS — READY_FOR_HUMAN_VALIDATION", f"{slug}: publish review is not PASS")
        check(editorial.get("human_validation") is False, f"{slug}: workflow must not fabricate human validation")
        check(editorial.get("robots") == "index, follow", f"{slug}: record must preserve index, follow")

if errors:
    print("USAGE_WORKFLOW: FAIL")
    for error in errors:
        print(" -", error)
    raise SystemExit(1)

print("USAGE_WORKFLOW: PASS")
print(f" - shared responsibilities: {len(shared_resp)}/{total} ({shared_ratio:.1%})")
print(f" - custom responsibilities: {len(custom_resp)}/{total} ({custom_ratio:.1%})")
print(f" - shared skills with bloc-notes provenance: {len(stack.get('shared', []))}")
print(" - custom skills restricted to usage-analysis-workflow and usage-content-workflow")
print(f" - {len(USAGE_SLUGS)} authored v2 fragments + workflow records present")
print(f" - {len(USAGE_SLUGS)} usage drafts exist and remain index, follow")
print("NOTE: machine PASS validates the contract shape; editorial decisions remain the responsibility of shared skills + usage-analysis-workflow.")
