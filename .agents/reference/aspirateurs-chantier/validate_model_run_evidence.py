#!/usr/bin/env python3
"""Validate per-model evidence that the 80/20 model workflow actually ran.

Valid slugs come from .content/models/model-evidence.json. During phase 1, a model
may exist without a run file. A run becomes mandatory with --require-run, and a
final PASS always requires a complete run-evidence v2.
"""
from pathlib import Path
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parent
MODEL_DATA = ROOT / ".content" / "models" / "model-evidence.json"
RUNS_DIR = ROOT / ".content" / "models" / "runs"
MODELS_DIR = ROOT / "modeles"

READY = "PASS — READY_FOR_HUMAN_VALIDATION"
ALLOWED_RUN_STATUS = {"IN_PROGRESS", "PASS"}
ALLOWED_STEP_STATUS = {"PASS", "N/A"}

REQUIRED_SHARED_STEPS = {
    "search-intent",
    "content-audit",
    "content-refresh",
    "fact-check-pre",
    "evidence-based-reviews",
    "affiliate-value",
    "content-brief-authoring",
    "content-and-copy",
    "fact-check-post",
    "humanizer",
    "general-writing",
    "anti-ai-slop",
    "internal-linking-audit",
    "seo-technical",
    "seo-best-practices",
    "editorial-qa",
}
REQUIRED_CUSTOM_STEPS = {
    "vacuum-model-domain-review",
    "model-analysis-publish-review",
}


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_model_slugs():
    if not MODEL_DATA.exists():
        raise FileNotFoundError(
            f"missing model evidence: {MODEL_DATA.relative_to(ROOT)}"
        )
    data = load_json(MODEL_DATA)
    models = data.get("models")
    if not isinstance(models, dict) or not models:
        raise ValueError("model-evidence.json must contain a non-empty 'models' object")
    return set(models)


def validate_inventory(model_slugs):
    errors = []

    for slug in sorted(model_slugs):
        page = MODELS_DIR / slug / "index.html"
        if not page.exists():
            errors.append(f"{slug}: evidence exists but rendered model page is missing")

    if MODELS_DIR.exists():
        rendered_slugs = {
            path.name
            for path in MODELS_DIR.iterdir()
            if path.is_dir() and (path / "index.html").exists()
        }
        missing_evidence = sorted(rendered_slugs - model_slugs)
        if missing_evidence:
            errors.append(
                "rendered model pages missing from model-evidence.json: "
                + ", ".join(missing_evidence)
            )

    return errors


def validate_slug(slug, model_slugs, require_run=False):
    errors = []

    if slug not in model_slugs:
        return [f"{slug}: unknown model slug (not present in model-evidence.json)"]

    run_path = RUNS_DIR / f"{slug}.json"
    if not run_path.exists():
        if require_run:
            errors.append(f"{slug}: run evidence is required but missing")
        return errors

    run = load_json(run_path)

    if run.get("contract_version") != 2:
        errors.append(f"{slug}: run evidence contract_version must be 2")
    if run.get("slug") != slug:
        errors.append(f"{slug}: run evidence slug mismatch")

    run_status = run.get("status")
    if run_status not in ALLOWED_RUN_STATUS:
        errors.append(f"{slug}: invalid run status {run_status!r}")

    shared = run.get("shared_steps", {})
    custom = run.get("custom_steps", {})
    if not isinstance(shared, dict):
        errors.append(f"{slug}: shared_steps must be an object")
        shared = {}
    if not isinstance(custom, dict):
        errors.append(f"{slug}: custom_steps must be an object")
        custom = {}

    missing_shared = sorted(REQUIRED_SHARED_STEPS - set(shared))
    missing_custom = sorted(REQUIRED_CUSTOM_STEPS - set(custom))
    if missing_shared:
        errors.append(
            f"{slug}: missing shared execution steps: {', '.join(missing_shared)}"
        )
    if missing_custom:
        errors.append(
            f"{slug}: missing custom execution steps: {', '.join(missing_custom)}"
        )

    for group_name, group in [("shared", shared), ("custom", custom)]:
        for step, detail in group.items():
            if not isinstance(detail, dict):
                errors.append(f"{slug}: {group_name} step {step} must be an object")
                continue
            status = detail.get("status")
            if status not in ALLOWED_STEP_STATUS:
                errors.append(
                    f"{slug}: {group_name} step {step} has invalid status {status!r}"
                )
            if status == "N/A" and not str(detail.get("reason", "")).strip():
                errors.append(
                    f"{slug}: {group_name} step {step} is N/A without a reason"
                )
            if status == "PASS" and not str(detail.get("output", "")).strip():
                errors.append(
                    f"{slug}: {group_name} step {step} PASS has no persisted output summary"
                )

    total = len(REQUIRED_SHARED_STEPS) + len(REQUIRED_CUSTOM_STEPS)
    shared_ratio = len(REQUIRED_SHARED_STEPS) / total
    if shared_ratio < 0.80:
        errors.append(
            f"{slug}: execution contract shared ratio below 80% ({shared_ratio:.1%})"
        )

    if not str(run.get("reader_decision", "")).strip():
        errors.append(f"{slug}: reader_decision missing")
    if not str(run.get("value_without_affiliate_links", "")).strip():
        errors.append(f"{slug}: affiliate-independent value statement missing")

    outline = run.get("outline", [])
    if not isinstance(outline, list) or not outline:
        errors.append(f"{slug}: evidence-derived outline missing")
    else:
        for i, section in enumerate(outline, start=1):
            if not isinstance(section, dict):
                errors.append(f"{slug}: outline item {i} must be an object")
                continue
            if not str(section.get("question", "")).strip():
                errors.append(f"{slug}: outline item {i} has no reader question")
            refs = section.get("evidence_refs")
            if not isinstance(refs, list) or not refs:
                errors.append(f"{slug}: outline item {i} has no evidence_refs")
            if not str(section.get("decision_value", "")).strip():
                errors.append(f"{slug}: outline item {i} has no decision_value")

    publish_review = run.get("publish_review")
    if run_status == "PASS" and publish_review != READY:
        errors.append(
            f"{slug}: PASS run status requires publish_review={READY!r}"
        )

    publish_step = custom.get("model-analysis-publish-review", {})
    if publish_review == READY and publish_step.get("status") != "PASS":
        errors.append(
            f"{slug}: final publish PASS requires model-analysis-publish-review PASS"
        )

    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--slug")
    parser.add_argument(
        "--require-run",
        action="store_true",
        help="require a run file even during phase 1",
    )
    args = parser.parse_args()

    try:
        model_slugs = load_model_slugs()
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
        print("FAIL", exc)
        return 1

    errors = validate_inventory(model_slugs)

    slugs = [args.slug] if args.slug else sorted(model_slugs)
    for slug in slugs:
        errors.extend(validate_slug(slug, model_slugs, require_run=args.require_run))

    if errors:
        for error in errors:
            print("FAIL", error)
        return 1

    existing_runs = sum((RUNS_DIR / f"{slug}.json").exists() for slug in slugs)
    print(
        f"PASS: model inventory valid for {len(model_slugs)} model(s); "
        f"run-evidence contract valid for {existing_runs} existing run(s)."
    )
    if existing_runs < len(slugs) and not args.require_run:
        print(
            "INFO: missing run files are allowed in phase 1; "
            "use --require-run before PUBLISH_REVIEW."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
