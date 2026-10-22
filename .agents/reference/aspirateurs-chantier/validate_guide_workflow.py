#!/usr/bin/env python3
"""Validate /guides/ workflow governance and draft safety.

Machine floor only: this script validates the 80/20 contract, provenance, workflow
files, configured routes, draft robots/canonical state and the shape of any persisted
Guide run evidence. It does not award editorial PASS or human approval.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
STACK = ROOT / ".agents" / "skills" / "guide-skill-stack.json"
CONFIG = ROOT / "guide-workflow.config.yaml"
ANALYSIS = ROOT / ".agents" / "skills" / "guide-analysis-workflow" / "SKILL.md"
CONTENT = ROOT / ".agents" / "skills" / "guide-content-workflow" / "SKILL.md"
RECORDS = ROOT / ".content" / "guides"
SITE_ORIGIN = "https://aspirateurs-chantier.fr"

GUIDE_SLUGS = [
    "capacite-cuve",
    "classes-l-m-h",
    "comment-choisir-aspirateur-de-chantier",
    "debit-air-aspirateur",
    "decolmatage-automatique",
    "depression-kpa-mbar-air-watt",
    "entretien-aspirateur-chantier",
    "filtre-hepa-aspirateur",
    "prise-asservie",
    "puissance-aspiration",
    "sac-ou-sans-sac",
]

EXPECTED_CUSTOM = {"guide-analysis-workflow", "guide-content-workflow"}
REQUIRED_SHARED_EXECUTION = {
    "seo-content-audit",
    "seo-keyword",
    "search-intent",
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
    "seo-drift",
    "editorial-qa",
}
ALLOWED_DECISIONS = {"KEEP", "LIGHT_UPDATE", "DEEP_REWRITE", "MERGE", "NOINDEX"}
ALLOWED_TYPES = {"CHOICE", "EXPLAINER", "HOW_TO", "HYBRID"}
ALLOWED_PUBLISH = {"PASS — READY_FOR_HUMAN_VALIDATION", "FAIL — KEEP_NOINDEX"}

ROBOTS_RE = re.compile(r'<meta\b[^>]*name="robots"[^>]*content="([^"]+)"[^>]*>', re.I)
CANONICAL_RE = re.compile(r'<link\b[^>]*rel="canonical"[^>]*href="([^"]+)"[^>]*>', re.I)
H1_RE = re.compile(r"<h1\b", re.I)

errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def normalized_robots(value):
    return ",".join(part.strip().lower() for part in value.split(","))


for path, label in [
    (STACK, "guide-skill-stack.json"),
    (CONFIG, "guide-workflow.config.yaml"),
    (ANALYSIS, "guide-analysis-workflow/SKILL.md"),
    (CONTENT, "guide-content-workflow/SKILL.md"),
]:
    check(path.exists(), f"missing {label}")

stack = {}
shared_resp = []
custom_resp = []
total = 0
shared_ratio = 0.0
custom_ratio = 1.0
if STACK.exists():
    try:
        stack = json.loads(STACK.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"invalid guide-skill-stack.json: {exc}")
    else:
        gov = stack.get("governance", {})
        shared_resp = gov.get("shared_responsibilities", [])
        custom_resp = gov.get("custom_responsibilities", [])
        total = len(shared_resp) + len(custom_resp)
        shared_ratio = len(shared_resp) / total if total else 0.0
        custom_ratio = len(custom_resp) / total if total else 1.0
        check(shared_ratio >= float(gov.get("target_shared_ratio_min", 0.8)), f"shared responsibility ratio too low: {shared_ratio:.1%}")
        check(custom_ratio <= float(gov.get("target_custom_ratio_max", 0.2)), f"custom responsibility ratio too high: {custom_ratio:.1%}")

        custom = stack.get("custom", [])
        check(len(custom) == 2, f"expected exactly 2 custom Guide orchestrators, got {len(custom)}")
        check({item.get("name") for item in custom} == EXPECTED_CUSTOM, "custom Guide skills must be exactly the two workflow orchestrators")

        for item in stack.get("shared", []):
            name = item.get("name")
            check(bool(name), "shared skill without name")
            check(item.get("source_repo") == "MarcW88/bloc-notes-numerique", f"{name}: shared provenance must pass through MarcW88/bloc-notes-numerique")
            check(bool(item.get("source_sha")), f"{name}: missing source_sha provenance")
            skill_file = ROOT / ".agents" / "skills" / str(name) / "SKILL.md"
            check(skill_file.exists(), f"{name}: shared skill missing locally")

for path in (ANALYSIS, CONTENT):
    if path.exists():
        text = path.read_text(encoding="utf-8")
        check("source_repo: MarcW88/bloc-notes-numerique" in text, f"{path}: source workflow provenance missing")
        check('orchestration_target: ">=80% existing skills"' in text, f"{path}: 80/20 orchestration target missing")

if CONFIG.exists():
    config_text = CONFIG.read_text(encoding="utf-8")
    for slug in GUIDE_SLUGS:
        check(f'/guides/{slug}/' in config_text, f"{slug}: route missing from guide-workflow.config.yaml")
    check('draft_robots: "index, follow"' in config_text, "config must preserve draft index, follow")
    check('require_human_validation_before_indexation: true' in config_text, "config must require human validation before indexation")
    check('allow_automatic_indexation: false' in config_text, "config must prohibit automatic indexation")

# The current Guide source of truth already exists and must be preserved.
check((ROOT / "_generate_guides.py").exists(), "missing current Guide editorial source _generate_guides.py")

# Draft route safety: the workflow installation itself must not change publication state.
for slug in GUIDE_SLUGS:
    page = ROOT / "guides" / slug / "index.html"
    check(page.exists(), f"{slug}: guide page missing")
    if not page.exists():
        continue
    html = page.read_text(encoding="utf-8")
    robots = [normalized_robots(v) for v in ROBOTS_RE.findall(html)]
    check("index,follow" in robots, f"{slug}: draft index, follow missing")
    canonicals = CANONICAL_RE.findall(html)
    expected = f"{SITE_ORIGIN}/guides/{slug}/"
    check(canonicals == [expected], f"{slug}: canonical mismatch ({canonicals!r})")
    check(len(H1_RE.findall(html)) == 1, f"{slug}: expected exactly one H1")

hub = ROOT / "guides" / "index.html"
check(hub.exists(), "Guide hub missing")
if hub.exists():
    html = hub.read_text(encoding="utf-8")
    robots = [normalized_robots(v) for v in ROBOTS_RE.findall(html)]
    check("index,follow" in robots, "Guide hub must remain index, follow during recovery")
    check(CANONICAL_RE.findall(html) == [f"{SITE_ORIGIN}/guides/"], "Guide hub canonical mismatch")

# Run evidence is optional until a Guide actually enters the workflow. If a record
# exists, however, its execution and publication claims must be internally coherent.
if RECORDS.exists():
    for record_path in sorted(RECORDS.glob("*.json")):
        try:
            record = json.loads(record_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{record_path.name}: invalid JSON: {exc}")
            continue
        slug = record.get("slug")
        check(slug in GUIDE_SLUGS, f"{record_path.name}: unknown Guide slug {slug!r}")
        if not slug:
            continue
        check(record.get("guide_type") in ALLOWED_TYPES, f"{slug}: invalid or missing guide_type")
        check(record.get("audit_decision") in ALLOWED_DECISIONS, f"{slug}: invalid or missing audit_decision")
        intent = record.get("intent", {})
        check(bool(intent.get("reader_task") or record.get("reader_task")), f"{slug}: reader task missing")
        check(bool(record.get("evidence")), f"{slug}: evidence ledger missing")
        check(bool(record.get("outline")), f"{slug}: evidence-led outline missing")

        execution = record.get("workflow_execution", {})
        shared_steps = execution.get("shared", [])
        custom_steps = execution.get("custom", [])
        shared_names = {step.get("skill") for step in shared_steps}
        custom_names = {step.get("skill") for step in custom_steps}
        check(REQUIRED_SHARED_EXECUTION <= shared_names, f"{slug}: missing required shared-skill execution evidence")
        check(custom_names == EXPECTED_CUSTOM, f"{slug}: custom execution must be exactly the 2 Guide orchestrators")
        for step in shared_steps + custom_steps:
            status = step.get("status")
            check(status in {"PASS", "N/A"}, f"{slug}: invalid workflow status for {step.get('skill')}")
            if status == "PASS":
                check(bool(step.get("output")), f"{slug}: PASS step {step.get('skill')} missing output")
            if status == "N/A":
                check(bool(step.get("reason")), f"{slug}: N/A step {step.get('skill')} missing reason")

        editorial = record.get("editorial", {})
        check(editorial.get("publish_review") in ALLOWED_PUBLISH, f"{slug}: invalid publish_review")
        check(editorial.get("human_validation") is False, f"{slug}: workflow must not fabricate human validation")
        check(editorial.get("robots") == "index, follow", f"{slug}: record must preserve index, follow")

if errors:
    print("GUIDE_WORKFLOW: FAIL")
    for error in errors:
        print(" -", error)
    raise SystemExit(1)

print("GUIDE_WORKFLOW: PASS")
print(f" - shared responsibilities: {len(shared_resp)}/{total} ({shared_ratio:.1%})")
print(f" - custom responsibilities: {len(custom_resp)}/{total} ({custom_ratio:.1%})")
print(f" - shared skills with bloc-notes provenance: {len(stack.get('shared', []))}")
print(" - custom skills restricted to guide-analysis-workflow and guide-content-workflow")
print(f" - {len(GUIDE_SLUGS)} Guide drafts + hub remain index, follow")
print("NOTE: run-evidence is required only once a Guide is worked; machine PASS never awards editorial approval.")
