#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
GEN = ROOT / "_generate.py"
AGENTS = ROOT / "AGENTS.md"


def patch_generator():
    text = GEN.read_text(encoding="utf-8")

    if "from deal_content import DEAL_CONTENT, DEAL_STATUS_LABEL" not in text:
        text = text.replace(
            "from usage_content import USAGE_CONTENT\n",
            "from usage_content import USAGE_CONTENT\nfrom deal_content import DEAL_CONTENT, DEAL_STATUS_LABEL\n",
            1,
        )

    text = text.replace(
        'def content_page(title, desc, canonical, crumbs, page_type="", body_html=""):',
        'def content_page(title, desc, canonical, crumbs, page_type="", body_html="", status_label=None):',
        1,
    )
    text = text.replace(
        'content_status = "Vérifié le 8 septembre 2026" if body_html else "Contenu en préparation"',
        'content_status = status_label or ("Vérifié le 8 septembre 2026" if body_html else "Contenu en préparation")',
        1,
    )

    text = text.replace(
        '"Bons plans — Bloc-notes numériques en promotion",\n    "Les meilleures offres et promotions sur les tablettes E Ink et bloc-notes numériques.",',
        '"Bons plans — Offres et prix des bloc-notes numériques",\n    "Promotions, baisses de prix et repères d’achat vérifiés sur les tablettes E Ink et bloc-notes numériques.",',
        1,
    )
    text = text.replace(
        '"Les meilleures offres du moment sur les bloc-notes numériques, vérifiées régulièrement.",',
        '"Des offres vérifiées, des prix de référence datés et les promotions expirées clairement séparées des bons plans encore achetables.",',
        1,
    )

    start = text.index("BONS_PLANS = [")
    end = text.index("# ── ACCESSOIRES", start)
    replacement = '''BONS_PLANS = [
    ("/bons-plans/bloc-notes-numerique/", "Bons plans bloc-notes numériques — Offres et prix vérifiés", "Promotions réellement vérifiées, prix à surveiller et offres expirées sur les tablettes E Ink."),
    ("/bons-plans/remarkable/", "Bons plans reMarkable — Offres et prix à surveiller", "Bundles, reconditionné et baisses de prix reMarkable vérifiés avec leur prix de référence."),
    ("/bons-plans/kindle-scribe/", "Bons plans Kindle Scribe — Offres et baisses de prix", "Promotions Kindle Scribe actives, prix à surveiller et historiques de baisse clairement séparés."),
    ("/bons-plans/kobo-elipsa/", "Bons plans Kobo Elipsa — Offres et prix", "Prix de référence et promotions vérifiées sur la Kobo Elipsa 2E."),
    ("/bons-plans/boox/", "Bons plans BOOX — Promotions et disponibilité", "Promotions BOOX vérifiées avec contrôle du stock, du bundle et du coût final."),
    ("/bons-plans/bloc-notes-numerique-occasion/", "Bloc-notes numérique d'occasion — Guide d'achat", "Acheter un bloc-notes numérique d'occasion ou reconditionné : prix, état, garantie et contrôles utiles."),
    ("/bons-plans/black-friday/", "Black Friday 2026 — Bloc-notes numériques", "Date, prix de référence et watchlist pour les offres Black Friday 2026 sur les tablettes E Ink."),
]

for path, title, desc in BONS_PLANS:
    crumbs = breadcrumb(("Bons plans", "/bons-plans/"), title.split("—")[0].strip())
    write(path + "index.html", content_page(title, desc, path, crumbs, "Offres", DEAL_CONTENT.get(path, ""), DEAL_STATUS_LABEL.get(path)))

'''
    text = text[:start] + replacement + text[end:]
    GEN.write_text(text, encoding="utf-8")


def patch_agents():
    text = AGENTS.read_text(encoding="utf-8")
    marker = "## Production éditoriale — Bons plans"
    if marker in text:
        return
    addition = '''

## Production éditoriale — Bons plans

Pour toute création, réécriture ou actualisation sous `/bons-plans/` :

1. Utiliser `.agents/skills/deal-content-workflow/SKILL.md`.
2. Créer ou mettre à jour `.content/deals/<slug>.json` avant de modifier le texte : prix, disponibilité, statut et date de contrôle doivent être documentés.
3. Distinguer strictement `ACTIVE_VERIFIED`, `ACTIVE_STOCK_SENSITIVE`, `PRICE_WATCH`, `EXPIRED`, `SOLD_OUT`, `UNVERIFIED` et `NOT_STARTED`.
4. Un prix barré marchand ne suffit jamais à prouver une remise. Documenter le prix de référence et sa base avant d'afficher une économie ou un pourcentage.
5. Une offre qui dépasse son TTL ne peut plus être présentée comme active sans nouvelle vérification.
6. Les pages de bons plans n'effectuent pas de ranking produit selon la commission. Le choix produit reste dans `/comparatifs/` ; la page deal juge l'offre, pas la valeur absolue du produit.
7. Les liens affiliés doivent rester transparents et utiliser `rel="sponsored"` lorsque nécessaire.
8. Utiliser `content-refresh`, `fact-check`, `affiliate-value`, `internal-linking-audit`, `natural-writing`, `humanizer`, `anti-ai-slop` et `editorial-qa` conformément au workflow.
9. Conserver `noindex,follow` jusqu'à validation humaine explicite.
'''
    AGENTS.write_text(text.rstrip() + addition + "\n", encoding="utf-8")


def main():
    patch_generator()
    patch_agents()
    subprocess.run([sys.executable, str(GEN)], cwd=ROOT, check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
