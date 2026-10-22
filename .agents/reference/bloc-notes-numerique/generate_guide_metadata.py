#!/usr/bin/env python3
"""Generate evidence-based QA reports for /guides/.

This script deliberately does not infer qualitative PASS results from heading counts.
The structural gate is provided by validate_guide_quality.py; this report exposes the
evidence used by that gate so an editor can review every page. Existing briefs are
preserved and are not overwritten here.
"""
from pathlib import Path
import html as html_lib
import re

from validate_guide_quality import inspect, article_html, sections, words, P_RE, TABLE_RE, LINK_RE, SOURCE_LINK_RE

ROOT = Path(__file__).resolve().parent
TODAY = "2026-09-08"
PRICE_SLUG = "prix-bloc-notes-numerique"


def clean(raw: str) -> str:
    raw = re.sub(r"<[^>]+>", " ", raw, flags=re.S)
    raw = html_lib.unescape(raw)
    return re.sub(r"\s+", " ", raw).strip()


def metrics(slug: str):
    page = ROOT / "guides" / slug / "index.html"
    html = page.read_text(encoding="utf-8")
    article = article_html(html)
    main_without_sources = re.split(r'<h2\b[^>]*id="sources"', article, maxsplit=1, flags=re.I)[0]
    sec = []
    for sid, title, body in sections(article):
        if sid == "sources":
            continue
        table_count = len(TABLE_RE.findall(body))
        sec.append({
            "id": sid,
            "title": title,
            "words": words(body),
            "paragraphs": len(P_RE.findall(body)),
            "tables": table_count,
            "lists": len(re.findall(r'<(?:ul|ol)\b', body, re.I)),
        })
    internal = [u for u in LINK_RE.findall(article) if not u.startswith('/transparence-affiliation/')]
    source_count = len(SOURCE_LINK_RE.findall(article))
    return {
        "page": page,
        "words": words(main_without_sources),
        "sections": sec,
        "internal": internal,
        "unique_internal": sorted(set(internal)),
        "sources": source_count,
        "tables": len(TABLE_RE.findall(main_without_sources)),
        "noindex": 'name="robots" content="noindex,follow"' in html,
        "issues": inspect(page),
    }


def render(slug: str, m: dict) -> str:
    verdict = "PASS" if not m["issues"] else "FAIL"
    status = "DRAFT_READY" if verdict == "PASS" else "REVISION_REQUIRED"
    standard = "reference" if slug == PRICE_SLUG else "must meet price-guide quality floor"
    sec_lines = "\n".join(
        f"- `{s['title']}` — {s['words']} mots ; {s['paragraphs']} paragraphe(s) ; {s['tables']} tableau(x) ; {s['lists']} liste(s)."
        for s in m["sections"]
    )
    link_lines = "\n".join(f"- `{u}`" for u in m["unique_internal"]) or "- Aucun lien interne contextuel."
    issue_lines = "\n".join(f"- {x}" for x in m["issues"]) if m["issues"] else "- Aucun blocker du quality gate."
    return f"""# Rapport de contrôle — standard guide Prix

```yaml
url: /guides/{slug}/
reviewed_at: {TODAY}
structural_quality_gate: {verdict}
content_status: {status}
indexing_status: {'noindex' if m['noindex'] else 'CHECK_REQUIRED'}
quality_reference: /guides/prix-bloc-notes-numerique/
page_role_in_standard: {standard}
```

## 1. Profondeur sémantique mesurable

- Contenu utile hors navigation et hors section Sources : **{m['words']} mots**.
- H2 substantiels : **{len(m['sections'])}**.
- Tableaux : **{m['tables']}**.
- Les sections trop courtes, mono-paragraphe non développé ou tableaux sans contexte sont bloquants dans `validate_guide_quality.py`.

### Détail par section

{sec_lines}

## 2. Maillage interne

- Liens internes contextuels : **{len(m['internal'])}**.
- Cibles uniques : **{len(m['unique_internal'])}**.

{link_lines}

Le gate exige au minimum 4 liens contextuels et 3 cibles distinctes, sauf modification explicite du standard.

## 3. Sources et factualité

- Sources externes officielles identifiables : **{m['sources']}**.
- Les fonctions variables sont rédigées avec leurs marques, générations ou conditions lorsque celles-ci sont nécessaires à la précision.
- Aucune expérience directe, mesure propriétaire ou résultat de test n'est déduit automatiquement par ce script.
- Le fact-check éditorial reste une passe distincte : la présence d'une source n'est pas, à elle seule, une preuve que toute affirmation est correcte.

## 4. Content refresh / conservation

- Pour les anciens guides, les angles utiles ont été conservés lorsque cohérents avec le nouveau standard ; l'enrichissement porte sur contexte, exemples, limites, entités et prochaine étape.
- Pour les pages initialement vides, le contenu est construit depuis le brief et non depuis un simple gabarit H2.
- La page Prix reste la référence de densité et de valeur décisionnelle, sans imposer une longueur artificiellement identique à chaque tutoriel.

## 5. Natural writing / Humanizer / General writing

Ces passes ont été appliquées pendant la réécriture éditoriale mais **ne sont pas déclarées PASS par déduction automatique**. Le script contrôle uniquement des signaux structurels observables. La validation humaine finale doit encore vérifier le rythme, les répétitions, les transitions et le ton dans le rendu.

## 6. Anti-AI-slop

Le gate structurel bloque le principal défaut du précédent lot : H2 très courts, tableaux sans explication et maillage quasi absent. Il ne prétend pas détecter l'origine d'un texte. Toute formulation générique ou mécanique relevée lors de la lecture finale doit être corrigée avant publication.

## 7. SEO / GEO

- Une réponse initiale autonome est exigée par le quality gate.
- Les H2 doivent couvrir des sous-questions distinctes et suffisamment développées.
- Les tableaux doivent être introduits et interprétés.
- Les entités et sources sont explicites dans le corps lorsqu'elles soutiennent une décision ou un mécanisme.
- Le maillage dirige vers des guides, usages, comparatifs ou pages marques selon l'étape suivante du lecteur.

## 8. Technique

- `noindex,follow` : **{'PASS' if m['noindex'] else 'FAIL'}**.
- HTML généré depuis `_generate.py` et les modules de contenu, pas modifié uniquement à la main dans les pages générées.
- Les liens internes sont validés séparément dans le workflow CI.

## 9. Blockers observés

{issue_lines}

## Verdict

**{verdict} structurel — {status}.** Ce verdict signifie que la page atteint le plancher de profondeur défini à partir du guide Prix. Il ne remplace pas la validation humaine finale et n'autorise ni retrait du `noindex`, ni publication, ni déploiement.
"""


def main():
    review_dir = ROOT / ".content" / "reviews"
    review_dir.mkdir(parents=True, exist_ok=True)
    failures = []
    pages = sorted((ROOT / "guides").glob("*/index.html"))
    for page in pages:
        slug = page.parent.name
        m = metrics(slug)
        (review_dir / f"{slug}.md").write_text(render(slug, m), encoding="utf-8")
        if m["issues"]:
            failures.append((slug, m["issues"]))
    if failures:
        for slug, issues in failures:
            print(f"FAIL {slug}: {'; '.join(issues)}")
        raise SystemExit(1)
    print(f"PASS: {len(pages)} evidence-based guide reviews generated")


if __name__ == "__main__":
    main()
