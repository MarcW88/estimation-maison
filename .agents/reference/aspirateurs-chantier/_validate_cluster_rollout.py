#!/usr/bin/env python3
from pathlib import Path
import json
import re

BASE = Path(__file__).resolve().parent

MODELS = [
 'karcher-wd2','karcher-wd5','karcher-wd6','karcher-nt-30-1-tact',
 'bosch-advancedvac-20','bosch-gas-12-25-pl','bosch-gas-18v-10-l','bosch-gas-35-l-afc','bosch-gas-35-m-afc',
 'makita-vc2512l','makita-vc4210mx','festool-ctl-midi','nilfisk-multi-ii-30-t'
]
USAGES = [
 'aspirateur-platre','aspirateur-ponceuse','aspirateur-atelier','aspirateur-bois-sciure-copeaux',
 'aspirateur-gravats','aspirateur-scie','aspirateur-bricolage-renovation'
]

errors = []

def check(cond, msg):
    if not cond:
        errors.append(msg)

for slug in MODELS:
    p = BASE / 'modeles' / slug / 'index.html'
    check(p.exists(), f'missing model page {slug}')
    if not p.exists():
        continue
    h = p.read_text(encoding='utf-8')
    check('MM/AAAA' not in h, f'{slug}: stale verification placeholder')
    check('Contenu test à rédiger' not in h, f'{slug}: test-content placeholder')
    check('<!-- Contenu à rédiger -->' not in h, f'{slug}: content placeholder')
    check('<meta name="robots" content="index, follow">' in h, f'{slug}: robots changed')
    has_source_section = (
        '<h2 id="source">Source fabricant</h2>' in h
        or '<h2 id="sources">Sources et méthode</h2>' in h
    )
    check(has_source_section, f'{slug}: source section missing')

critical = {
 'festool-ctl-midi': ['badge badge-l', 'Classe L', 'AUTOCLEAN', 'Non sur la référence CTL MIDI I standard'],
 'makita-vc4210mx': ['badge badge-m', 'InfiniClean automatique', '42 L brut / 34 L poussière / 30 L liquide'],
 'bosch-gas-35-m-afc': ['74 L/s', '254 mbar', 'Classe M'],
 'bosch-gas-18v-10-l': ['34 L/s', '115 mbar', 'Pas de prise secteur'],
 'karcher-nt-30-1-tact': ['Tact automatique commandé par capteur', 'ACD', '74 L/s'],
}
for slug, needles in critical.items():
    h = (BASE / 'modeles' / slug / 'index.html').read_text(encoding='utf-8')
    for n in needles:
        check(n in h, f'{slug}: missing critical evidence {n!r}')

for slug in ['karcher-wd2','karcher-wd5','karcher-wd6','bosch-advancedvac-20','nilfisk-multi-ii-30-t']:
    h = (BASE / 'modeles' / slug / 'index.html').read_text(encoding='utf-8')
    check('Pas de classe L/M/H documentée' in h, f'{slug}: consumer vacuum incorrectly classed')

for slug in USAGES:
    p = BASE / 'usages' / slug / 'index.html'
    check(p.exists(), f'missing usage page {slug}')
    if not p.exists():
        continue
    h = p.read_text(encoding='utf-8')
    check('<!-- Contenu à rédiger -->' not in h, f'{slug}: placeholder remains')
    check('MM/AAAA' not in h, f'{slug}: stale date placeholder')
    check(len(re.findall(r'<h2\b', h)) >= 5, f'{slug}: insufficient intent depth')
    check('<h2 id="sources">Sources et méthode</h2>' in h, f'{slug}: sources missing')
    check('<meta name="robots" content="index, follow">' in h, f'{slug}: robots changed')

# Professional comparison: validate the current v2 semantic contract rather than
# freezing legacy H2 IDs or exact scenario labels. The comparison workflow forbids
# sibling pages from being forced into a fixed heading template.
professional_path = BASE / 'comparatifs' / 'aspirateur-professionnel' / 'index.html'
check(professional_path.exists(), 'professional comparison: page missing')
professional = professional_path.read_text(encoding='utf-8') if professional_path.exists() else ''
professional_text = re.sub(r'<[^>]+>', ' ', professional)
professional_text = re.sub(r'\s+', ' ', professional_text).lower()

check(
    ('professionnel' in professional_text and 'classe m' in professional_text and
     ('ne sont pas synonymes' in professional_text or 'ne veut pas dire automatiquement' in professional_text)),
    'professional comparison: professional-vs-class-M distinction missing'
)
check('/comparatifs/aspirateur-classe-m/' in professional,
      'professional comparison: class-M handoff missing')
check('<meta name="robots" content="index, follow">' in professional,
      'professional comparison: robots changed')

# The persistent comparison ledger is the source of truth for intent boundaries,
# candidate diversity and scenario logic. This avoids encoding the editorial plan
# a second time in a machine validator.
ledger_path = BASE / '.content' / 'comparisons' / 'aspirateur-professionnel.json'
check(ledger_path.exists(), 'professional comparison: evidence ledger missing')
if ledger_path.exists():
    ledger = json.loads(ledger_path.read_text(encoding='utf-8'))
    intent = ledger.get('intent', {})
    notes = ledger.get('notes', {})
    candidates = ledger.get('product_universe') or ledger.get('scope', {}).get('candidates', [])
    recommendation_logic = ledger.get('recommendation_logic', [])

    boundary = str(intent.get('boundary', '')).lower()
    check('aspirateur-classe-m' in boundary or 'classe m' in boundary,
          'professional comparison: ledger intent boundary with class-M page missing')
    check(len(candidates) >= 4, 'professional comparison: ledger candidate scope too narrow')
    check(len(recommendation_logic) >= 4,
          'professional comparison: insufficient scenario diversity in v2 recommendation logic')

    candidate_ids = {c.get('id') for c in candidates if c.get('id')}
    scenario_products = {r.get('product_id') for r in recommendation_logic if r.get('product_id')}
    check(len(scenario_products & candidate_ids) >= 4,
          'professional comparison: recommendation logic does not cover enough distinct candidates')

    brands = {str(c.get('brand', '')).strip().lower() for c in candidates if c.get('brand')}
    check(len(brands) >= 3, f'professional comparison: insufficient cross-brand diversity ({len(brands)} brands)')

    # Ensure the rendered page still reflects a multi-scenario professional decision,
    # without requiring exact wording for those scenarios.
    rendered_candidate_hits = sum(str(c.get('name', '')).lower() in professional_text for c in candidates if c.get('name'))
    check(rendered_candidate_hits >= 4,
          f'professional comparison: too few v2 candidates represented in rendered page ({rendered_candidate_hits})')

    check(notes.get('affiliate_commission_used_in_ranking') is False,
          'professional comparison: affiliate independence not documented')
    check(not ledger.get('scores'), 'professional comparison: legacy scores unexpectedly restored')
    check(not ledger.get('ranking'), 'professional comparison: legacy ranking unexpectedly restored')

# The cluster audit concerns the /marques/ hub content, not the global navigation
# shell that is still shared site-wide. Validate only the hub's <main> region.
brand_index = (BASE / 'marques' / 'index.html').read_text(encoding='utf-8')
main_match = re.search(r'<main>.*?</main>', brand_index, flags=re.S)
check(main_match is not None, 'brand index: main region missing')
brand_main = main_match.group(0) if main_match else ''
check('Tier 1' not in brand_main and 'Tier 2' not in brand_main, 'brand index: unsupported tiers remain in hub content')
for needle in ['DCV586M','PWD 12 à 30','DEXOS','Buddy / Multi','GAS Professional','AMPShare']:
    check(needle in brand_main, f'brand index: missing current family {needle}')

# Latest brand CLUSTER_AUDIT (2026-09-10) is the source of truth for recovery
# work classification. A per-page v2 PUBLISH_REVIEW may later mark a page READY,
# but it must not rewrite the original recovery verdict.
expected = {
 'karcher':'DEEP_REWRITE',
 'makita':'DEEP_REWRITE',
 'parkside':'DEEP_REWRITE',
 'nilfisk':'DEEP_REWRITE',
 'bosch':'LIGHT_UPDATE',
 'festool':'LIGHT_UPDATE',
 'dewalt':'LIGHT_UPDATE',
 'mirka':'LIGHT_UPDATE',
}
for slug, verdict in expected.items():
    d = json.loads((BASE / '.content' / 'brands' / f'{slug}.yaml').read_text(encoding='utf-8'))
    audit = d.get('cluster_audit', {})
    check(audit.get('verdict') == verdict, f'{slug}: wrong cluster verdict')
    check(d.get('recovery_verdict') == verdict, f'{slug}: recovery verdict not aligned')
    check(audit.get('date') == '2026-09-10', f'{slug}: stale cluster-audit date')
    check(audit.get('audit_artifact') == '.content/brands/cluster-audit-2026-09-10.md',
          f'{slug}: latest cluster-audit artifact not referenced')

check((BASE / '.content/brands/cluster-audit-2026-09-10.md').exists(), 'latest brand cluster audit artifact missing')

if errors:
    print('CLUSTER_ROLLOUT: FAIL')
    for e in errors:
        print(' -', e)
    raise SystemExit(1)

print('CLUSTER_ROLLOUT: PASS')
print(f' - {len(MODELS)} model pages verified')
print(f' - {len(USAGES)} usage pages completed')
print(' - professional comparison v2 intent boundary and scenario diversity verified from persistent evidence')
print(' - brand recovery verdicts aligned with latest 2026-09-10 cluster audit')
print(' - index, follow preserved')
