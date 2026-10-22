#!/usr/bin/env python3
"""Canonical brand-content generation entry point.

The generic generator may build the shell/seed only. Every brand must then receive a
bespoke editorial override. Publication readiness is never granted by generation:
`enforce_brand_review_state.py` downgrades pages without a valid v2 shared-skill run.
Validation is intentionally performed by separate CI steps for observability.
"""
from pathlib import Path
import subprocess
import sys

BASE = Path(__file__).resolve().parent


def run(script, *args):
    print(f'→ {script}', flush=True)
    subprocess.run([sys.executable, str(BASE / script), *args], cwd=BASE, check=True)


def main():
    run('validate_brand_skill_stack.py')
    run('_generate_brands.py')                 # shell + seed only
    run('_generate_bosch.py')                  # Bosch bespoke body
    run('_generate_brand_overrides.py')        # legacy bespoke bodies before evidence-led replacements
    run('_generate_karcher.py')                # evidence-led Kärcher body + ledger v2
    run('_generate_makita.py')                 # evidence-led Makita body + ledger v2
    run('_generate_parkside.py')               # evidence-led Parkside body + ledger v2
    run('_generate_nilfisk.py')                # evidence-led Nilfisk body + ledger v2
    run('_brand_rollout_polish.py')

    cluster_metadata = BASE / '_apply_cluster_audit_metadata.py'
    if cluster_metadata.exists():
        run(cluster_metadata.name)

    run('_apply_brand_design_fixes.py')
    run('enforce_brand_review_state.py')
    print('✓ canonical brand generation complete; run machine/run-evidence validators separately')


if __name__ == '__main__':
    main()
