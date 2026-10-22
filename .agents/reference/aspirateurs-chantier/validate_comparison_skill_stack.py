#!/usr/bin/env python3
"""Validate comparison workflow 80/20 governance and shared-skill provenance."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / '.agents' / 'skills' / 'comparison-skill-stack.json'
CONFIG = ROOT / 'comparison-workflow.config.yaml'

REQUIRED_SHARED = {
    'seo-content-audit', 'seo-keyword', 'jobs-to-be-done',
    'evidence-based-reviews', 'fact-check', 'affiliate-value',
    'content-brief-authoring', 'content-and-copy', 'humanizer',
    'general-writing', 'anti-ai-slop', 'seo-onpage', 'seo-technical',
    'internal-linking-audit', 'editorial-qa'
}
CUSTOM_ALLOWED = {'comparison-content-workflow', 'comparison-analysis-workflow'}


def main():
    errors = []
    if not MANIFEST.exists():
        errors.append(f'missing manifest: {MANIFEST.relative_to(ROOT)}')
        data = {}
    else:
        try:
            data = json.loads(MANIFEST.read_text(encoding='utf-8'))
        except Exception as exc:
            errors.append(f'invalid manifest JSON: {exc}')
            data = {}

    governance = data.get('governance', {})
    shared_resp = governance.get('shared_responsibilities', [])
    custom_resp = governance.get('custom_responsibilities', [])
    total_resp = len(shared_resp) + len(custom_resp)
    shared_ratio = len(shared_resp) / total_resp if total_resp else 0.0
    custom_ratio = len(custom_resp) / total_resp if total_resp else 1.0
    shared_min = float(governance.get('target_shared_ratio_min', 0.80))
    custom_max = float(governance.get('target_custom_ratio_max', 0.20))

    if data.get('version') != 2:
        errors.append('comparison skill-stack manifest version must be 2')
    if governance.get('ratio_basis') != 'workflow_responsibilities':
        errors.append('ratio_basis must be workflow_responsibilities')
    if shared_ratio < shared_min:
        errors.append(f'shared responsibility ratio {shared_ratio:.1%} is below target {shared_min:.1%}')
    if custom_ratio > custom_max:
        errors.append(f'custom responsibility ratio {custom_ratio:.1%} exceeds target {custom_max:.1%}')
    if not governance.get('require_external_provenance_for_shared_skills'):
        errors.append('shared-skill provenance gate must be enabled')
    if not governance.get('require_run_evidence_before_publish_review_pass'):
        errors.append('run-evidence publish gate must be enabled')

    shared = data.get('shared', [])
    custom = data.get('custom', [])
    shared_names = {item.get('name') for item in shared}
    custom_names = {item.get('name') for item in custom}

    missing_shared = sorted(REQUIRED_SHARED - shared_names)
    if missing_shared:
        errors.append('missing required shared skills in manifest: ' + ', '.join(missing_shared))
    unexpected_custom = sorted(custom_names - CUSTOM_ALLOWED)
    if unexpected_custom:
        errors.append('custom comparison stack exceeds allowed scope: ' + ', '.join(unexpected_custom))
    missing_custom = sorted(CUSTOM_ALLOWED - custom_names)
    if missing_custom:
        errors.append('missing comparison orchestrators: ' + ', '.join(missing_custom))

    for item in shared + custom:
        name = item.get('name')
        if not name:
            errors.append('manifest entry without name')
            continue
        skill = ROOT / '.agents' / 'skills' / name / 'SKILL.md'
        if not skill.exists():
            errors.append(f'missing skill: {name}')
            continue
        if name in shared_names:
            source_repo = item.get('source_repo')
            source_sha = item.get('source_sha')
            if source_repo != 'MarcW88/bloc-notes-numerique' or not source_sha:
                errors.append(f'{name}: missing bloc-notes shared-skill provenance')
                continue
            text = skill.read_text(encoding='utf-8')
            if f'source_repo: {source_repo}' not in text or f'source_sha: {source_sha}' not in text:
                errors.append(f'{name}: local SKILL.md provenance does not match manifest')

    evidence_item = next((x for x in shared if x.get('name') == 'evidence-based-reviews'), {})
    if evidence_item.get('upstream') != 'rampstackco/claude-skills/skills/evidence-based-reviews':
        errors.append('evidence-based-reviews upstream provenance missing')

    for workflow in CUSTOM_ALLOWED:
        path = ROOT / '.agents' / 'skills' / workflow / 'SKILL.md'
        if not path.exists():
            continue
        text = path.read_text(encoding='utf-8').lower()
        if '80/20' not in text:
            errors.append(f'{workflow}: 80/20 governance not documented')
        if 'aspirateurs-chantier.fr' not in text:
            errors.append(f'{workflow}: target domain adaptation not explicit')
        for forbidden in ['when available', 'lorsque les skills spécialisés sont disponibles']:
            if forbidden in text:
                errors.append(f'{workflow}: optional-skill fallback still present')

    if not CONFIG.exists():
        errors.append('missing comparison-workflow.config.yaml')
    else:
        config = CONFIG.read_text(encoding='utf-8').lower()
        for token in [
            'scoring_optional: true',
            'weighting_optional: true',
            'hard_gates_optional: true',
            'prohibit_word_count_quotas: true',
            'prohibit_heading_count_quotas: true',
            'prohibit_internal_link_quotas: true',
            'prohibit_comparison_type_templates: true',
            'prohibit_inferring_dust_class_from_hepa_power_or_airflow: true',
            'require_run_evidence_before_publish_review_pass: true',
            'generator_role: "shell_and_components_only"',
        ]:
            if token not in config:
                errors.append(f'config missing governance rule: {token}')

    if errors:
        for error in errors:
            print('FAIL', error)
        return 1

    print(
        f'PASS: comparison governance uses {len(shared_resp)} shared responsibilities and '
        f'{len(custom_resp)} custom responsibilities; shared={shared_ratio:.1%}, custom={custom_ratio:.1%}.'
    )
    print(f'PASS: {len(shared)} shared skills have bloc-notes provenance; only {len(custom)} custom orchestrators are allowed.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
