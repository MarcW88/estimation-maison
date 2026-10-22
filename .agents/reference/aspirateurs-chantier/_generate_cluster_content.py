#!/usr/bin/env python3
"""Canonical generation for the audited content cluster.

The order is intentional and enforced:
1. shared/custom skill governance for Brands, Comparisons, Usages and Guides;
2. canonical Guide generation from baseline + authored v2 fragments;
3. model evidence/pages;
4. non-brand usage shell + authored v2 materialization;
5. comparison cluster with audited bespoke overrides;
6. brand hubs;
7. restore cross-cutting rendered layers (design, products, affiliate CTAs, images);
8. cluster metadata/index;
9. validation.

Cross-cutting layers are part of the committed public artifact. Regenerating the
editorial body must therefore not make canonical validation falsely report
Amazon modules, verified model CTAs or already-generated editorial images as
uncommitted drift.
"""
from pathlib import Path
import subprocess
import sys

BASE = Path(__file__).resolve().parent


def run(script, *args):
    print('→ ' + ' '.join((script, *args)))
    subprocess.run([sys.executable, str(BASE / script), *args], cwd=BASE, check=True)


def main():
    run('validate_brand_skill_stack.py')
    run('validate_comparison_skill_stack.py')
    run('validate_usage_workflow.py')
    run('validate_guide_workflow.py')
    run('_generate_guide_content.py')
    run('_generate_model_overrides.py')
    run('_generate_usage_overrides.py')
    run('_materialize_usage_v2.py')
    run('validate_usage_workflow.py')
    run('_generate_comparison_content.py')
    run('_generate_brand_content.py')
    run('_generate_brand_hub_index.py')

    # Shared visual shell is canonical across generated page families.
    run('_apply_design_v2.py')

    # Commerce is a guarded post-render layer: restore only approved placements
    # and exact-model links already present in the product registry.
    placements = BASE / '.content/products/placements.json'
    if placements.exists():
        run('apply_product_cards.py', 'comparisons')
        run('apply_product_cards.py', 'usages')
        run('apply_product_cards.py', 'guides')
        run('validate_product_cards.py', 'comparisons')
        run('validate_product_cards.py', 'usages')
        run('validate_product_cards.py', 'guides')
        run('apply_inline_affiliate_links.py')
        run('validate_inline_affiliate_links.py')

    # Editorial images are restored from existing GENERATED assets only. This
    # helper never calls BFL, so canonical regeneration has no generation cost.
    run('scripts/restore_editorial_images.py', '--scope', 'usages')
    run('scripts/restore_editorial_images.py', '--scope', 'guides')

    run('_apply_cluster_audit_metadata.py')
    run('_validate_comparatifs.py')
    run('_validate_comparison_rollout.py')
    run('_validate_brands.py')
    run('_validate_cluster_rollout.py')
    print('✓ ordered cluster generation complete')


if __name__ == '__main__':
    main()
