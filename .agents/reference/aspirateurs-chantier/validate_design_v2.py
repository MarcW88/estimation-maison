#!/usr/bin/env python3
"""Validate that public pages use the Editorial V2 shell and one CSS entry point."""
from pathlib import Path
from _apply_design_v2 import LEGACY_STYLESHEETS, ROOT, SINGLE_STYLESHEET, public_pages, page_classes

CORE_SCRIPT = "/design-v2.js"


def main() -> None:
    errors: list[str] = []
    pages = public_pages()
    for path in pages:
        rel = path.relative_to(ROOT).as_posix()
        if not path.exists():
            errors.append(f"{rel}: missing page")
            continue
        html = path.read_text(encoding="utf-8")
        body_open = html.split("<body", 1)[1].split(">", 1)[0] if "<body" in html else ""
        for cls in page_classes(rel):
            if cls not in body_open.split('class="', 1)[-1]:
                errors.append(f"{rel}: missing body class {cls}")

        if html.count(SINGLE_STYLESHEET) != 1:
            errors.append(f"{rel}: expected exactly one {SINGLE_STYLESHEET}")
        if html.count(CORE_SCRIPT) != 1:
            errors.append(f"{rel}: expected exactly one {CORE_SCRIPT}")
        for asset in LEGACY_STYLESHEETS:
            if asset in html:
                errors.append(f"{rel}: extra stylesheet link remains: {asset}")

    if errors:
        print("EDITORIAL_V2: FAIL")
        for error in errors:
            print(f" - {error}")
        raise SystemExit(1)

    print(f"EDITORIAL_V2: PASS — {len(pages)} public pages use one CSS entry point")


if __name__ == "__main__":
    main()
