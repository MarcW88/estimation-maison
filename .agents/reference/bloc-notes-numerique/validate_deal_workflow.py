#!/usr/bin/env python3
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from publication_indexation import INDEXABLE_DEAL_ROUTES

ROOT = Path(__file__).resolve().parent
DEALS = ROOT / ".content" / "deals"
EXPECTED = {
    "bloc-notes-numerique",
    "remarkable",
    "kindle-scribe",
    "kobo-elipsa",
    "boox",
    "bloc-notes-numerique-occasion",
    "black-friday",
}
ALLOWED_TYPES = {"LIVE_DEALS", "BRAND_DEALS", "EVENT_DEALS", "SECOND_HAND"}
ALLOWED_STATUSES = {
    "ACTIVE_VERIFIED", "ACTIVE_STOCK_SENSITIVE", "PRICE_WATCH", "EXPIRED",
    "SOLD_OUT", "UNVERIFIED", "NOT_STARTED"
}
ACTIVE = {"ACTIVE_VERIFIED", "ACTIVE_STOCK_SENSITIVE"}


def parse_dt(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def fail(errors, message):
    errors.append(message)


def expected_robots(route):
    return "index,follow" if route in INDEXABLE_DEAL_ROUTES else "noindex,follow"


def main():
    errors = []
    warnings = []
    records = {}

    hub = ROOT / "bons-plans" / "index.html"
    if not hub.exists():
        fail(errors, "missing Bons plans hub")
    else:
        marker = f'<meta name="robots" content="{expected_robots("/bons-plans/")}">'
        if marker not in hub.read_text(encoding="utf-8"):
            fail(errors, "Bons plans hub publication state mismatch")

    for slug in EXPECTED:
        path = DEALS / f"{slug}.json"
        if not path.exists():
            fail(errors, f"missing deal record: {path}")
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            fail(errors, f"invalid json {path}: {exc}")
            continue
        records[slug] = data

        if data.get("slug") != slug:
            fail(errors, f"{slug}: slug mismatch")
        if data.get("page_type") not in ALLOWED_TYPES:
            fail(errors, f"{slug}: invalid page_type")
        if not data.get("checked_at"):
            fail(errors, f"{slug}: missing checked_at")
        if data.get("qa", {}).get("final_verdict") != "PASS":
            fail(errors, f"{slug}: qa verdict is not PASS")
        # Historical pre-publication QA: noindex had to remain in place until
        # this explicit human publication approval.
        if not data.get("qa", {}).get("noindex_preserved"):
            fail(errors, f"{slug}: pre-publication noindex preservation not confirmed")

        for offer in data.get("offers", []):
            status = offer.get("status")
            if status not in ALLOWED_STATUSES:
                fail(errors, f"{slug}: invalid offer status {status}")
            if not offer.get("checked_at"):
                fail(errors, f"{slug}: offer missing checked_at")
            if status in ACTIVE:
                for key in ("merchant", "price", "currency", "source"):
                    if offer.get(key) in (None, ""):
                        fail(errors, f"{slug}: active offer missing {key}")
                ttl = data.get("freshness_policy", {}).get("active_offer_ttl_hours")
                if ttl and offer.get("checked_at"):
                    age = datetime.now(timezone.utc) - parse_dt(offer["checked_at"]).astimezone(timezone.utc)
                    if age.total_seconds() > ttl * 3600:
                        warnings.append(f"{slug}: active offer is stale ({age.total_seconds()/3600:.1f}h > {ttl}h)")
            if offer.get("reference_price") is not None and offer.get("reference_price_basis") in (None, ""):
                fail(errors, f"{slug}: reference price has no documented basis")

        route = f"/bons-plans/{slug}/"
        html = ROOT / "bons-plans" / slug / "index.html"
        if not html.exists():
            fail(errors, f"{slug}: missing generated html")
        else:
            text = html.read_text(encoding="utf-8")
            marker = f'<meta name="robots" content="{expected_robots(route)}">'
            if marker not in text:
                fail(errors, f"{slug}: publication robots state mismatch")
            if "Contenu à rédiger" in text or "Contenu en préparation" in text:
                fail(errors, f"{slug}: placeholder content remains")

    unexpected = [p.stem for p in DEALS.glob("*.json") if p.stem != "_template" and p.stem not in EXPECTED]
    if unexpected:
        warnings.append("unexpected deal records: " + ", ".join(sorted(unexpected)))

    if warnings:
        print("WARNINGS")
        for warning in warnings:
            print("-", warning)
    if errors:
        print("FAIL")
        for error in errors:
            print("-", error)
        return 1
    print(
        f"PASS: {len(records)} deal records plus hub validated; "
        f"{len(INDEXABLE_DEAL_ROUTES)} approved routes are indexable"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
