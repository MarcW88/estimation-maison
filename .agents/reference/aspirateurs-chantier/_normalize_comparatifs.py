#!/usr/bin/env python3
"""Keep comparison source verdicts consistent with scoring and normalize generated HTML."""
from pathlib import Path

BASE = Path(__file__).resolve().parent
GENERATOR = BASE / "_generate_comparatifs.py"

OLD_PRO_VERDICT = '"answer": "Pour un usage professionnel polyvalent, le <strong>Kärcher NT 30/1 Tact Te M ACD</strong> prend la première place. Le <strong>Bosch GAS 35 M AFC</strong> reste un excellent généraliste. Le <strong>Festool CTM MIDI I AC</strong> est le meilleur choix compact pour les utilisateurs qui privilégient l\'intégration Festool.",'
NEW_PRO_VERDICT = '"answer": "Pour un usage professionnel polyvalent, le <strong>Festool CTM MIDI I AC</strong> arrive en tête de notre scoring grâce à son format compact, sa classe M, son AUTOCLEAN et son intégration aux outils. Le <strong>Kärcher NT 30/1 Tact Te M ACD</strong> est plus pertinent lorsque capacité et gros volumes de poussières priment. Le <strong>Bosch GAS 35 M AFC</strong> reste un excellent généraliste.",'

source = GENERATOR.read_text(encoding="utf-8")
if OLD_PRO_VERDICT in source:
    source = source.replace(OLD_PRO_VERDICT, NEW_PRO_VERDICT, 1)
    GENERATOR.write_text(source, encoding="utf-8")
    print("✓ professional verdict aligned with calculated ranking")
elif NEW_PRO_VERDICT not in source:
    raise SystemExit("FAIL: professional verdict pattern not found")
else:
    print("✓ professional verdict already aligned")

for page in sorted((BASE / "comparatifs").glob("*/index.html")):
    text = page.read_text(encoding="utf-8")
    normalized = "\n".join(line.rstrip() for line in text.splitlines()) + "\n"
    if normalized != text:
        page.write_text(normalized, encoding="utf-8")
        print(f"✓ whitespace normalized: {page.relative_to(BASE)}")
