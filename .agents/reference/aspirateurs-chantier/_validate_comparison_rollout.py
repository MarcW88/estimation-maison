#!/usr/bin/env python3
"""Semantic gate for the evidence-led comparison v2 rollout.

This validator checks page roles, safety boundaries and anti-template signals. It does
not impose fixed H2 labels, word counts, scoring systems or a universal page template.
"""
from pathlib import Path
import json
import re

BASE = Path(__file__).resolve().parent
V2 = [
    "meilleur-aspirateur-de-chantier",
    "aspirateur-professionnel",
    "aspirateur-classe-m",
    "aspirateur-chantier-puissant",
    "aspirateur-industriel",
    "aspirateur-chantier-sans-fil",
    "aspirateur-eau-poussiere",
    "petit-aspirateur-de-chantier",
]
BAGLESS = "aspirateur-chantier-sans-sac"
ALL = V2 + [BAGLESS]
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def html(slug):
    return (BASE / "comparatifs" / slug / "index.html").read_text(encoding="utf-8")


def data(slug):
    return json.loads((BASE / ".content" / "comparisons" / f"{slug}.json").read_text(encoding="utf-8"))


def text(slug):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html(slug))).lower()


for slug in ALL:
    h = html(slug)
    d = data(slug)
    check('<meta name="robots" content="index, follow">' in h, f"{slug}: noindex/follow changed")
    check(d.get("notes", {}).get("affiliate_commission_used_in_ranking") is False, f"{slug}: affiliate independence missing")
    check("notre classement 2026" not in h.lower() and "score ajusté" not in h.lower(), f"{slug}: legacy ranking language remains")

for slug in V2:
    d = data(slug)
    source = BASE / ".content" / "comparisons" / "v2" / f"{slug}.html"
    check(source.exists(), f"{slug}: authored v2 fragment missing")
    check(d.get("status") == "V2_EDITORIAL_REWRITE", f"{slug}: v2 materialization status missing")
    check(d.get("notes", {}).get("v2_editorial_source") == f".content/comparisons/v2/{slug}.html", f"{slug}: v2 source provenance missing")
    check(d.get("notes", {}).get("generator_authored_content") is False, f"{slug}: generator must not claim editorial authorship")

bag = data(BAGLESS)
check(bag.get("editorial", {}).get("publish_review") != "READY_FOR_HUMAN_VALIDATION", "bagless: merge candidate must not become READY automatically")

class_m = text("aspirateur-classe-m")
for needle in ["surveillance", "décolmatage", "collecte", "antistatique", "inrs", "filtre se charge"]:
    check(needle in class_m, f"class M: missing decision layer {needle}")
check("hepa" in class_m and "ne transforment" in class_m, "class M: HEPA/class distinction missing")

industrial = text("aspirateur-industriel")
for needle in ["process", "triphasé", "fonctionnement continu", "vho200", "huile", "copeaux", "atex", "acd"]:
    check(needle in industrial, f"industrial: missing process marker {needle}")
check("hors zone atex" in industrial, "industrial: ACD/ATEX boundary missing")

powerful = text("aspirateur-chantier-puissant")
for needle in ["à la turbine", "colmatage", "débit", "dépression", "flexible", "pas un classement"]:
    check(needle in powerful, f"powerful: missing comparability marker {needle}")
check("inrs" in powerful, "powerful: independent filter-loading evidence missing")

best = html("meilleur-aspirateur-de-chantier")
for path in [
    "/comparatifs/aspirateur-classe-m/",
    "/comparatifs/aspirateur-chantier-sans-fil/",
    "/comparatifs/aspirateur-eau-poussiere/",
    "/comparatifs/aspirateur-chantier-puissant/",
    "/comparatifs/aspirateur-industriel/",
    "/comparatifs/petit-aspirateur-de-chantier/",
]:
    check(path in best, f"general: missing specialist handoff {path}")
check("score global" in best.lower(), "general: no-universal-score rationale missing")

cordless = text("aspirateur-chantier-sans-fil")
for needle in ["parc batteries", "autonomie", "coût", "poids", "déclenchement", "vendu sans batterie"]:
    check(needle in cordless, f"cordless: missing system-cost/workflow marker {needle}")
check("score commun" in cordless, "cordless: runtime non-equivalence caveat missing")

wetdry = text("aspirateur-eau-poussiere")
for needle in ["sec au liquide", "vidange", "sac", "filtre", "wet/dry ne dit rien"]:
    check(needle in wetdry, f"wet/dry: missing transition or safety marker {needle}")

compact = text("petit-aspirateur-de-chantier")
for needle in ["poids prêt à travailler", "dimensions d’emballage", "escaliers", "véhicule", "classe"]:
    check(needle in compact, f"compact: missing mobility marker {needle}")
# The page may mention the old threshold only to reject it. What is forbidden is
# reintroducing it as a positive definition or selection rule.
for forbidden in ["compact = moins de 15 litres", "compact : moins de 15 litres", "définition : moins de 15 litres", "< 15 l = compact"]:
    check(forbidden not in compact, f"compact: arbitrary litre threshold reintroduced: {forbidden}")

professional = text("aspirateur-professionnel")
for needle in ["professionnel", "classe l", "classe m", "workflow", "consommables", "inrs"]:
    check(needle in professional, f"professional: missing v2 decision layer {needle}")

signatures = {}
for slug in V2:
    headings = tuple(
        re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", x)).strip().lower()
        for x in re.findall(r"<h2\b[^>]*>(.*?)</h2>", html(slug), flags=re.S | re.I)
    )
    check(len(headings) >= 5, f"{slug}: insufficient decision sections after v2 rewrite")
    signatures.setdefault(headings, []).append(slug)
for sig, slugs in signatures.items():
    check(len(slugs) == 1, "cluster: identical H2 architecture remains: " + ", ".join(slugs))

paragraph_owners = {}
for slug in V2:
    for p in re.findall(r"<p[^>]*>(.*?)</p>", html(slug), flags=re.S | re.I):
        clean = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", p)).strip().lower()
        if len(clean) >= 220:
            paragraph_owners.setdefault(clean, []).append(slug)
for paragraph, owners in paragraph_owners.items():
    if len(set(owners)) > 1:
        check(False, "cluster: long paragraph reused across pages: " + ", ".join(sorted(set(owners))))

if errors:
    print("COMPARISON_ROLLOUT_V2: FAIL")
    for error in errors:
        print(" -", error)
    raise SystemExit(1)

print("COMPARISON_ROLLOUT_V2: PASS")
print(" - 8 retained comparisons materialize authored evidence-led v2 fragments")
print(" - bagless remains a human-gated merge candidate")
print(" - page roles are distinct and exact structural cloning is blocked")
print(" - all 9 comparison URLs remain index, follow")
