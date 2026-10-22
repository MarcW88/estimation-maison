#!/usr/bin/env python3
"""Small post-render cleanup for audited comparison pages.

Keeps the final copy user-facing, removes stale legacy wording and can add a
small piece of primary evidence when the renderer's local model ledger is less
specific than the current official manufacturer page.
"""
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent


def polish(slug, replacements):
    path = BASE / "comparatifs" / slug / "index.html"
    text = path.read_text(encoding="utf-8")
    for old, new in replacements:
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")


polish("petit-aspirateur-de-chantier", [
    ("Un petit aspirateur de chantier ne se définit pas par “moins de 15 L”.", "Un petit aspirateur de chantier ne se définit pas par un seuil fixe de volume."),
])

polish("aspirateur-industriel", [
    ("<span>Meilleur aspirateur industriel mobile</span>", "<span>Aspirateur industriel</span>"),
    ("Comparaison documentaire de familles et références industrielles actuelles.", "Recherche documentaire sur des familles et références industrielles actuelles."),
])

polish("aspirateur-classe-m", [
    ("Une fois ce gate franchi", "Une fois ce prérequis rempli"),
    ("Le gate M", "Le prérequis M"),
    ("comme podium cross-brand", "comme podium entre marques"),
])

polish("aspirateur-chantier-sans-fil", [
    ("le voltage seul ne suffit pas", "la tension seule ne suffit pas"),
    ("changent davantage le workflow", "changent davantage la façon de travailler"),
    ("le workflow change", "la façon de travailler change"),
    ("Workflow outil", "Travail avec l’outil"),
    ("wet/dry grand public", "eau/poussière grand public"),
])

polish("meilleur-aspirateur-de-chantier", [
    ("La bonne page générale doit donc vous orienter vers un profil, pas imposer un vainqueur unique.", "Il faut donc choisir par profil plutôt que chercher un vainqueur unique."),
    ("Pourquoi nous avons supprimé le score global", "Pourquoi un score global serait trompeur"),
])

polish("aspirateur-chantier-sans-sac", [
    ("Référence retenue historiquement pour son usage sans sac et sa compacité classe L.", "Bosch documente explicitement une conception sans sac, avec technologie cyclonique, dans un format compact de classe L."),
    ("Cuve wet/dry pour déchets grossiers / liquides", "Cuve eau/poussière pour déchets grossiers / liquides"),
    ("Wet/dry 30 L ;", "Eau/poussière 30 L ;"),
    ("Wet/dry 30 L avec entretien manuel", "Eau/poussière 30 L avec entretien manuel"),
    ("pas tous les wet/dry comme “bagless”", "pas tous les aspirateurs eau/poussière comme “sans sac”"),
    ("workflow de sécurité", "sécurité de collecte"),
])

bagless_ledger = BASE / ".content/comparisons/aspirateur-chantier-sans-sac.json"
data = json.loads(bagless_ledger.read_text(encoding="utf-8"))
for rec in data.get("recommendation_logic", []):
    if rec.get("product_id") == "bosch-gas-18v-10-l":
        rec["why"] = "Bosch documente explicitement une conception sans sac avec technologie cyclonique sur ce modèle compact de classe L."
if not any(e.get("product") == "bosch-gas-18v-10-l" and e.get("criterion") == "bagless_design" for e in data.get("evidence", [])):
    data.setdefault("evidence", []).append({
        "product": "bosch-gas-18v-10-l",
        "criterion": "bagless_design",
        "claim": "Bosch décrit le GAS 18V-10 L comme une conception sans sac avec technologie cyclonique pour l’aspiration de matières solides et de liquides.",
        "source": "https://www.bosch-professional.com/fr/fr/products/gas-18v-10-l-06019C6302/",
        "source_date": "2026-09-09",
        "evidence_class": "VERIFIED",
    })
bagless_ledger.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

for page in sorted((BASE / "comparatifs").glob("*/index.html")):
    text = page.read_text(encoding="utf-8")
    text = text.replace("Desk research", "Recherche documentaire")
    text = text.replace('<span class="ctype ctype-comp">Comp</span>', '<span class="ctype ctype-comp">Comparatif</span>')
    page.write_text(text, encoding="utf-8")

print("✓ comparison rollout editorial polish")
