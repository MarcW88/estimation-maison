#!/usr/bin/env python3
"""Restore already-generated editorial images into regenerated HTML pages.

This script never calls BFL and never changes image request statuses. It only
re-inserts existing GENERATED assets when a content generator has overwritten
the corresponding <figure> block.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from generate_bfl_images import (
    insert_or_restore_figure,
    load_request,
    request_files,
    safe_repo_path,
    validate_request,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument(
        "--scope",
        choices=("all", "usages", "guides", "comparatifs", "marques", "modeles", "accessoires"),
        default="all",
        help="Only restore requests targeting this top-level page family",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    restored = 0
    eligible = 0

    for source in request_files(root, ".content/image-requests"):
        req = load_request(source)
        validate_request(root, source, req)

        if req.get("status") != "GENERATED":
            continue
        if not req.get("required") or not req.get("allow_ai_generation") or req.get("truth_risk") != "LOW":
            continue

        page = str(req.get("page") or "")
        if args.scope != "all" and not page.startswith(f"{args.scope}/"):
            continue

        eligible += 1
        output_path = safe_repo_path(root, str(req.get("output_path") or ""), "output_path", source)
        if not output_path.exists():
            raise SystemExit(f"Generated asset missing for {req.get('id')}: {req.get('output_path')}")

        if insert_or_restore_figure(root, source, req):
            restored += 1
            print(f"Restored {req['id']} into {page}")

    print(f"Editorial image restore: scope={args.scope} eligible={eligible} restored={restored}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
