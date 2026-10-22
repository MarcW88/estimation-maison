#!/usr/bin/env python3
"""Validate per-page proof that the shared comparison workflow actually ran.

The validator does not execute prompt skills. It verifies the persisted handoff from a
real editorial run. A comparison can remain a noindex draft without run evidence, but
it cannot claim READY_FOR_HUMAN_VALIDATION without a valid v2 run file.
"""
from pathlib import Path
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parent
SLUGS = [
    'meilleur-aspirateur-de-chantier',
    'aspirateur-professionnel',
    'aspirateur-classe-m',
    'aspirateur-chantier-puissant',
    'aspirateur-eau-poussiere',
    'aspirateur-chantier-sans-fil',
    'aspirateur-chantier-sans-sac',
    'petit-aspirateur-de-chantier',
    'aspirateur-industriel',
]
READY = 'READY_FOR_HUMAN_VALIDATION'
ALLOWED_STEP_STATUS = {'PASS', 'N/A'}

REQUIRED_SHARED_STEPS = {
    'seo-keyword',
    'jobs-to-be-done',
    'seo-content-audit',
    'evidence-based-reviews',
    'fact-check-pre',
    'affiliate-value',
    'content-brief-authoring',
    'content-and-copy',
    'fact-check-post',
    'humanizer',
    'general-writing',
    'anti-ai-slop',
    'seo-onpage',
    'seo-technical',
    'internal-linking-audit',
    'editorial-qa',
}
REQUIRED_CUSTOM_STEPS = {
    'vacuum-comparison-decision-review',
    'comparison-analysis-publish-review',
}


def load_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def validate_slug(slug, require_run=False):
    errors = []
    ledger_path = ROOT / '.content' / 'comparisons' / f'{slug}.json'
    if not ledger_path.exists():
        return [f'{slug}: missing comparison ledger']
    ledger = load_json(ledger_path)
    publish_status = ledger.get('editorial', {}).get('publish_review')
    run_path = ROOT / '.content' / 'comparisons' / 'runs' / f'{slug}.json'

    if not run_path.exists():
        if require_run or publish_status == READY:
            errors.append(f'{slug}: publish status is {publish_status!r} but run evidence is missing')
        return errors

    run = load_json(run_path)
    if run.get('contract_version') != 2:
        errors.append(f'{slug}: run evidence contract_version must be 2')
    if run.get('slug') != slug:
        errors.append(f'{slug}: run evidence slug mismatch')
    if run.get('status') != 'PASS':
        errors.append(f'{slug}: run evidence status must be PASS')

    shared = run.get('shared_steps', {})
    custom = run.get('custom_steps', {})
    missing_shared = sorted(REQUIRED_SHARED_STEPS - set(shared))
    missing_custom = sorted(REQUIRED_CUSTOM_STEPS - set(custom))
    if missing_shared:
        errors.append(f'{slug}: missing shared execution steps: {", ".join(missing_shared)}')
    if missing_custom:
        errors.append(f'{slug}: missing custom execution steps: {", ".join(missing_custom)}')

    for group_name, group in [('shared', shared), ('custom', custom)]:
        for step, detail in group.items():
            if not isinstance(detail, dict):
                errors.append(f'{slug}: {group_name} step {step} must be an object')
                continue
            status = detail.get('status')
            if status not in ALLOWED_STEP_STATUS:
                errors.append(f'{slug}: {group_name} step {step} has invalid status {status!r}')
            if status == 'N/A' and not str(detail.get('reason', '')).strip():
                errors.append(f'{slug}: {group_name} step {step} is N/A without a reason')
            if status == 'PASS' and not str(detail.get('output', '')).strip():
                errors.append(f'{slug}: {group_name} step {step} PASS has no persisted output summary')

    total = len(REQUIRED_SHARED_STEPS) + len(REQUIRED_CUSTOM_STEPS)
    shared_ratio = len(REQUIRED_SHARED_STEPS) / total
    if shared_ratio < 0.80:
        errors.append(f'{slug}: execution contract shared ratio below 80% ({shared_ratio:.1%})')

    for field in ['reader_decision', 'value_without_affiliate_links', 'comparison_scope']:
        if not str(run.get(field, '')).strip():
            errors.append(f'{slug}: {field} missing')

    candidate_scope = run.get('candidate_scope', {})
    if not isinstance(candidate_scope, dict) or not candidate_scope.get('considered'):
        errors.append(f'{slug}: candidate_scope.considered missing')
    if not isinstance(candidate_scope, dict) or 'major_exclusions' not in candidate_scope:
        errors.append(f'{slug}: candidate_scope.major_exclusions missing')

    outline = run.get('outline', [])
    if not isinstance(outline, list) or not outline:
        errors.append(f'{slug}: evidence-derived outline missing')
    else:
        for i, section in enumerate(outline, start=1):
            if not isinstance(section, dict):
                errors.append(f'{slug}: outline item {i} must be an object')
                continue
            if not str(section.get('question', '')).strip():
                errors.append(f'{slug}: outline item {i} has no reader question')
            if not section.get('evidence_refs'):
                errors.append(f'{slug}: outline item {i} has no evidence_refs')
            if not str(section.get('decision_value', '')).strip():
                errors.append(f'{slug}: outline item {i} has no decision_value')

    if publish_status == READY and run.get('publish_review') != 'PASS — READY_FOR_HUMAN_VALIDATION':
        errors.append(f'{slug}: ledger says READY but run evidence lacks final publish PASS')

    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--slug', choices=SLUGS)
    parser.add_argument('--require-run', action='store_true')
    args = parser.parse_args()
    slugs = [args.slug] if args.slug else SLUGS
    errors = []
    for slug in slugs:
        errors.extend(validate_slug(slug, require_run=args.require_run))
    if errors:
        for error in errors:
            print('FAIL', error)
        return 1
    print(f'PASS: comparison run-evidence contract valid for {len(slugs)} checked comparison(s).')
    return 0


if __name__ == '__main__':
    sys.exit(main())
