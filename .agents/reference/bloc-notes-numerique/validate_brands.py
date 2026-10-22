#!/usr/bin/env python3
from pathlib import Path
import re
from html import unescape

from brand_pages import PAGES
from brand_publication import INDEXATION_SCOPE, PUBLICATION_STATUS, ROBOTS_DIRECTIVE

ROOT = Path(__file__).resolve().parent
TAG_RE = re.compile(r'<[^>]+>', re.S)
H1_RE = re.compile(r'<h1\b[^>]*>(.*?)</h1>', re.S | re.I)
HEADING_RE = re.compile(r'<h([1-6])\b[^>]*>(.*?)</h\1>', re.S | re.I)
LINK_RE = re.compile(r'<a\b[^>]*href="([^"]+)"', re.I)
SOURCE_RE = re.compile(r'<a\b[^>]*href="https?://', re.I)
CANONICAL_RE = re.compile(r'<link\b[^>]*rel="canonical"[^>]*href="([^"]+)"', re.I)
TITLE_RE = re.compile(r'<title>(.*?)</title>', re.S | re.I)
META_DESC_RE = re.compile(r'<meta\b[^>]*name="description"[^>]*content="([^"]*)"', re.I)
ROBOTS_RE = re.compile(r'<meta\b[^>]*name="robots"[^>]*content="([^"]*)"', re.I)

# These patterns are machine-detectable publication blockers, not a style score.
EDITOR_FACING_PATTERNS = {
    'editor-facing page strategy': [
        r'\bune page marque\b',
        r'\b(?:la|cette) page\b.{0,80}\b(?:doit|sert|permet)\b',
        r'\bce contenu\b.{0,80}\b(?:doit|sert|permet)\b',
        r'\bservir de hub\b',
        r'\bpage (?:hub|pilier)\b',
        r'\bmaillage interne\b',
        r'\bintention de recherche\b',
        r'\boptimis(?:er|é|ée|ation) (?:pour )?(?:le )?seo\b',
        r'\boptimis(?:er|é|ée|ation) (?:pour )?(?:le )?geo\b',
    ],
    'template/meta commentary': [
        r'\bdans cet article,? nous allons\b',
        r'\bcette section (?:présente|explique|permet|sert)\b',
        r'\bvoici ce que (?:la page|cette page)\b',
    ],
}

FAKE_HANDS_ON_PATTERNS = [
    r'\bnous avons testé\b',
    r'\blors de notre test\b',
    r'\bpendant notre test\b',
    r'\baprès (?:plusieurs|quelques) semaines? d[’\']utilisation\b',
    r'\bnous avons mesuré\b',
    r'\bnous avons constaté\b',
]

HIGH_SLOP_PATTERNS = {
    'generic filler': [
        r'\bdans un monde où\b',
        r'\bil est important de (?:noter|souligner|comprendre|savoir)\b',
        r'\bil convient de (?:noter|souligner|rappeler)\b',
        r'\bque vous soyez\b',
        r'\ben conclusion\b',
    ],
    'unsupported promotional wording': [
        r'\bsolution idéale\b',
        r'\bchoix parfait\b',
        r'\bexpérience exceptionnelle\b',
        r'\bproduit incontournable\b',
    ],
}

PAGE_TYPE_CONCEPTS = {
    'DIRECTORY': [
        ('brand differentiation', ['différence', 'marque', 'écosystème']),
    ],
    'BRAND_HUB': [
        ('current range/context', ['gamme', 'modèle', 'génération']),
        ('ecosystem', ['écosystème', 'logiciel', 'cloud', 'intégration']),
        ('limitations', ['limite', 'éviter', 'moins adapté', 'inconvénient']),
    ],
    'PRODUCT': [
        ('decision criteria', ['pour qui', 'choisir', 'usage', 'convient']),
        ('limitations', ['limite', 'éviter', 'moins adapté', 'inconvénient']),
        ('compatibility or workflow', ['compatib', 'export', 'cloud', 'format', 'stylet']),
    ],
    'REVIEW': [
        ('editorial judgment', ['verdict', 'avis', 'analyse', 'évaluation']),
        ('limitations', ['limite', 'éviter', 'moins adapté', 'inconvénient']),
        ('evidence level', ['analyse documentaire', 'sources', 'documentation', 'test']),
    ],
    'SERVICE': [
        ('included or dependency', ['inclus', 'fonction', 'abonnement', 'sans', 'service']),
        ('limitations or cost', ['limite', 'coût', 'prix', 'éviter', 'dépend']),
    ],
    'ACCESSORY_HUB': [
        ('compatibility', ['compatib', 'génération', 'modèle']),
        ('necessity or optionality', ['nécessaire', 'optionnel', 'utile', 'indispensable']),
    ],
    'ALTERNATIVES': [
        ('reason to switch', ['alternative', 'quitter', 'limite', 'remplacer']),
        ('comparison rationale', ['critère', 'si vous', 'selon', 'usage', 'besoin']),
    ],
}


def clean(raw):
    return re.sub(r'\s+', ' ', unescape(TAG_RE.sub(' ', raw))).strip()


def normalized_text(raw):
    return clean(raw).lower().replace('’', "'")


def find_matches(text, patterns):
    return [pattern for pattern in patterns if re.search(pattern, text, re.I)]


def heading_levels(fragment):
    return [int(level) for level, _ in HEADING_RE.findall(fragment)]


def has_heading_jump(levels):
    if not levels:
        return False
    previous = levels[0]
    for level in levels[1:]:
        if level > previous + 1:
            return True
        previous = level
    return False


def page_type_concept_failures(page_type, text):
    failures = []
    for label, terms in PAGE_TYPE_CONCEPTS.get(page_type, []):
        if not any(term in text for term in terms):
            failures.append(f'page-type concept missing: {label}')
    return failures


failures = {}
warnings = {}

for url, spec in PAGES.items():
    issues = []
    notes = []

    if not url.startswith(INDEXATION_SCOPE):
        failures[url] = ['brand page outside approved indexation scope']
        continue

    page = ROOT / url.strip('/') / 'index.html'
    if not page.exists():
        failures[url] = ['page missing']
        continue

    html = page.read_text(encoding='utf-8')
    raw_html_lower = html.lower()

    article_match = re.search(r'<article class="content-main">(.*?)</article>', html, re.S | re.I)
    if not article_match:
        failures[url] = ['article.content-main missing']
        continue

    body = article_match.group(1)
    body_text = normalized_text(body)

    # Publication safety and basic SEO integrity.
    if '<!-- contenu à rédiger -->' in raw_html_lower or 'contenu en préparation' in raw_html_lower:
        issues.append('placeholder/preparation marker remains')

    robots = ROBOTS_RE.search(html)
    if not robots:
        issues.append('robots meta missing')
    elif robots.group(1).strip().lower() != ROBOTS_DIRECTIVE.lower():
        issues.append(f'robots directive must be {ROBOTS_DIRECTIVE} for approved brand publication')

    titles = TITLE_RE.findall(html)
    if len(titles) != 1 or not clean(titles[0]):
        issues.append('missing or invalid title')

    descriptions = META_DESC_RE.findall(html)
    if len(descriptions) != 1 or not clean(descriptions[0]):
        issues.append('missing or invalid meta description')

    canonicals = CANONICAL_RE.findall(html)
    if len(canonicals) != 1:
        issues.append('missing or duplicate canonical')

    h1s = [clean(x) for x in H1_RE.findall(html)]
    if len(h1s) != 1:
        issues.append(f'expected exactly one H1, found {len(h1s)}')

    # Check the document's editorial heading flow only: one page H1 followed by article headings.
    editorial_levels = ([1] if len(h1s) == 1 else []) + heading_levels(body)
    if has_heading_jump(editorial_levels):
        issues.append('article heading hierarchy skips a level')

    # Editorial blockers visible in user-facing prose.
    for label, patterns in EDITOR_FACING_PATTERNS.items():
        if find_matches(body_text, patterns):
            issues.append(f'{label} detected')

    for label, patterns in HIGH_SLOP_PATTERNS.items():
        if find_matches(body_text, patterns):
            issues.append(f'high-risk generic writing pattern: {label}')

    if find_matches(body_text, FAKE_HANDS_ON_PATTERNS):
        issues.append('unsupported first-hand test language detected')

    # Reviews need explicit evidence framing when no test data is stored in this repo.
    if spec['page_type'] == 'REVIEW':
        evidence_terms = ['analyse documentaire', 'analyse éditoriale', 'sources officielles', 'documentation']
        if not any(term in body_text for term in evidence_terms):
            issues.append('review does not clearly disclose documentary/editorial evidence level')

    # Semantic floor by page type. No H2/word/link quotas.
    issues.extend(page_type_concept_failures(spec['page_type'], body_text))

    # Sources are required for factual commercial pages, but we do not impose an arbitrary count.
    if len(SOURCE_RE.findall(body)) == 0:
        issues.append('no external source found in article')

    # Internal linking is judged contextually by the analysis workflow; machine validator only flags total absence.
    internal_links = [href for href in LINK_RE.findall(body) if href.startswith('/')]
    if not internal_links:
        notes.append('no internal link found; verify next-step navigation manually')

    # Absolute best-language needs a manual criteria check rather than an automatic failure.
    if re.search(r'\bmeilleur\b', body_text) and not any(term in body_text for term in ['critère', 'selon', 'pour ', 'notre sélection']):
        notes.append('absolute best-language may need explicit criteria')

    if issues:
        failures[url] = issues
    if notes:
        warnings[url] = notes

if warnings:
    print('WARNINGS — manual brand-analysis review notes')
    for url, notes in warnings.items():
        print('WARN', url)
        for note in notes:
            print('  -', note)
    print()

if failures:
    print('FAIL — machine-detectable editorial/publication blockers found')
    for url, issues in failures.items():
        print('FAIL', url)
        for issue in issues:
            print('  -', issue)
    raise SystemExit(1)

print(f'PASS: {len(PAGES)} brand pages have no machine-detectable publication blockers')
print(f'PUBLICATION: {PUBLICATION_STATUS} — robots={ROBOTS_DIRECTIVE} — scope={INDEXATION_SCOPE}')
