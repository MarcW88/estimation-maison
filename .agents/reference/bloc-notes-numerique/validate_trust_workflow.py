#!/usr/bin/env python3
"""Validate trust-page records and guard against unsupported institutional claims."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TRUST = ROOT / ".content" / "trust"

EXPECTED = {
    "methode-de-test": ("METHODOLOGY", ROOT / "methode-de-test" / "index.html"),
    "comment-nous-comparons": ("COMPARISON_POLICY", ROOT / "comment-nous-comparons" / "index.html"),
    "a-propos": ("ABOUT", ROOT / "a-propos" / "index.html"),
    "contact": ("CONTACT", ROOT / "contact" / "index.html"),
    "transparence-affiliation": ("AFFILIATE_DISCLOSURE", ROOT / "transparence-affiliation" / "index.html"),
    "mentions-legales": ("LEGAL_PENDING", ROOT / "mentions-legales" / "index.html"),
}

EVIDENCE_LEVELS = {
    "DIRECT_OBSERVATION",
    "REPO_EVIDENCE",
    "OFFICIAL_SOURCE",
    "OWNER_CONFIRMED",
    "EDITORIAL_INFERENCE",
    "UNKNOWN",
}

STATUSES = {
    "READY_FOR_DRAFT",
    "NEEDS_OWNER_INPUT",
    "DRAFT_READY",
    "HUMAN_APPROVED",
    "LEGAL_PENDING",
}

STRICT_STATUSES = {"DRAFT_READY", "HUMAN_APPROVED"}

SENSITIVE_PATTERNS = {
    "physical_test": [
        r"\bnous avons test[ée]",
        r"\blors de nos tests\b",
        r"\bapr[eè]s plusieurs semaines d['’]utilisation\b",
    ],
    "team": [
        r"\bnotre [ée]quipe\b",
        r"\bnos experts\b",
        r"\bnotre r[ée]daction\b",
        r"\bnotre laboratoire\b",
    ],
    "absolute_independence": [
        r"\b100\s*%\s*ind[ée]pendant",
        r"\btotalement ind[ée]pendant",
    ],
    "affiliate_absolutes": [
        r"\bcela ne vous co[uû]te rien\b",
        r"\bm[eê]me prix garanti\b",
    ],
}

PLACEHOLDERS = (
    "Contenu en préparation",
    "<!-- Contenu à rédiger -->",
)


def load_record(slug: str) -> dict | None:
    path = TRUST / f"{slug}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def has_support(record: dict, category: str) -> bool:
    claims = record.get("claims", [])
    if category == "physical_test":
        return any(c.get("evidence_level") == "DIRECT_OBSERVATION" for c in claims)
    if category == "team":
        return any(
            c.get("evidence_level") == "OWNER_CONFIRMED"
            and any(word in (c.get("claim") or "").lower() for word in ("équipe", "team", "rédaction", "expert"))
            for c in claims
        )
    if category == "absolute_independence":
        return bool(record.get("editorial_rules", {}).get("allow_independence_claims"))
    if category == "affiliate_absolutes":
        return False
    return False


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not TRUST.exists():
        errors.append("missing .content/trust directory")

    for slug, (expected_type, html_path) in EXPECTED.items():
        record = load_record(slug)
        if record is None:
            errors.append(f"{slug}: missing trust record")
            continue

        if record.get("page_type") != expected_type:
            errors.append(f"{slug}: expected page_type {expected_type}, got {record.get('page_type')}")

        status = record.get("status")
        if status not in STATUSES:
            errors.append(f"{slug}: invalid status {status}")

        if slug == "mentions-legales" and status != "LEGAL_PENDING":
            warnings.append("mentions-legales: legal status changed; verify all legal data is owner-confirmed before drafting")

        claims = record.get("claims")
        if not isinstance(claims, list):
            errors.append(f"{slug}: claims must be a list")
            claims = []

        for idx, claim in enumerate(claims):
            level = claim.get("evidence_level")
            if level not in EVIDENCE_LEVELS:
                errors.append(f"{slug}: claim #{idx + 1} has invalid evidence level {level}")
            if level == "UNKNOWN" and claim.get("allowed_wording") and not record.get("unknowns"):
                warnings.append(f"{slug}: UNKNOWN claim has wording but no explicit unknowns list")

        if not isinstance(record.get("unknowns"), list):
            errors.append(f"{slug}: unknowns must be a list")

        rules = record.get("editorial_rules", {})
        preserve_noindex = rules.get("preserve_noindex")
        if not isinstance(preserve_noindex, bool):
            errors.append(f"{slug}: preserve_noindex must be a boolean")
            preserve_noindex = True

        if not html_path.exists():
            errors.append(f"{slug}: missing HTML page {html_path.relative_to(ROOT)}")
            continue

        html = html_path.read_text(encoding="utf-8")
        expected_robots = 'name="robots" content="noindex,follow"' if preserve_noindex else 'name="robots" content="index,follow"'
        if expected_robots not in html:
            state = "noindex,follow" if preserve_noindex else "index,follow"
            errors.append(f"{slug}: expected robots state {state} is missing")

        strict = status in STRICT_STATUSES
        for category, patterns in SENSITIVE_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, html, flags=re.IGNORECASE):
                    message = f"{slug}: sensitive {category} claim found: {pattern}"
                    if strict and not has_support(record, category):
                        errors.append(message)
                    else:
                        warnings.append(message)

        if strict:
            for placeholder in PLACEHOLDERS:
                if placeholder in html:
                    errors.append(f"{slug}: placeholder remains in {status} page")

        qa = record.get("qa", {})
        if status == "HUMAN_APPROVED" and qa.get("final_verdict") != "PASS":
            errors.append(f"{slug}: HUMAN_APPROVED requires qa.final_verdict=PASS")

    for warning in warnings:
        print("WARNING:", warning)

    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1

    print(f"PASS: validated {len(EXPECTED)} trust records; unresolved facts remain explicitly non-publishable.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
