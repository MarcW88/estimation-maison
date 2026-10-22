#!/usr/bin/env python3
"""Canonical materialization pipeline for the comparison cluster.

Important: this Python pipeline is NOT the editorial workflow. It may materialize the
current noindex draft, apply components/design and validate integrity, but it cannot
claim that shared editorial skills ran and cannot grant READY_FOR_HUMAN_VALIDATION.
That state is derived only from persisted v2 run evidence.
"""
from pathlib import Path
import subprocess
import sys

BASE = Path(__file__).resolve().parent


def run(script, *args):
    print(f"→ {script} {' '.join(args)}".rstrip())
    subprocess.run([sys.executable, str(BASE / script), *args], cwd=BASE, check=True)


def main():
    run("validate_comparison_skill_stack.py")

    # Legacy renderers still build the shared shell and existing draft state. They are
    # not proof that research / brief / writing / humanizer / QA actually ran.
    run("_generate_professional_comparison_override.py")
    run("_generate_comparison_overrides.py")
    run("_polish_comparison_rollout.py")
    run("_normalize_comparatifs.py")
    run("_apply_comparison_design.py")

    # Final editorial bodies are authored and persisted outside Python under
    # .content/comparisons/v2/. This step only materializes those artifacts.
    run("_materialize_comparison_v2.py")

    # READY status is evidence-gated after materialization.
    run("enforce_comparison_review_state.py")

    run("_validate_comparatifs.py")
    run("_validate_comparison_rollout.py")
    run("validate_comparison_run_evidence.py")
    print("✓ canonical comparison materialization complete (publish state remains evidence-gated)")


if __name__ == "__main__":
    main()
