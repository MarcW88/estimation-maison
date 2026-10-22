#!/usr/bin/env python3
"""Canonical Guide generation for the evidence-led v2 workflow.

The order is intentional:
1. validate 80/20 governance and draft safety;
2. regenerate the legacy Guide shell/content baseline;
3. normalize answer-first blocks;
4. retain the audited L/M/H pilot;
5. materialize authored v2 fragments for worked Guides;
6. validate workflow records and machine-detectable blockers.

No renderer grants editorial approval or indexation.
"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


def run(script):
    print(f"→ {script}")
    subprocess.run([sys.executable, str(ROOT / script)], cwd=ROOT, check=True)


def main():
    run("validate_guide_workflow.py")
    run("_generate_guides.py")
    run("_normalize_guide_answers.py")
    run("_guide_classes_lmh_pilot.py")
    run("_materialize_guides_v2.py")
    run("validate_guide_workflow.py")
    run("validate_guide_quality.py")
    print("✓ canonical Guide v2 generation complete; publish/index state remains workflow-gated")


if __name__ == "__main__":
    main()
