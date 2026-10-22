#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import urlparse
import json
import re
from brand_pages import PAGES
from brand_data import VERIFIED_AT, BRANDS
from brand_publication import PUBLICATION_STATUS, ROBOTS_DIRECTIVE
from brand_bespoke_output import bespoke_entity_summary
from brand_hub_bespoke_output import hub_entity_summary

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '.content' / 'brands'
REVIEWS = ROOT / '.content' / 'reviews'
OUT.mkdir(parents=True, exist_ok=True)
REVIEWS.mkdir(parents=True, exist_ok=True)

TITLE_RE = re.compile(r'<title>(.*?)</title>', re.S | re.I)
H2_RE = re.compile(r'<h2\b[^>]*>(.*?)</h2>', re.S | re.I)
LINK_RE = re.compile(r'<a\b[^>]*href="(/[^"]+)"', re.I)
SOURCE_RE = re.compile(r'<a\b[^>]*href="(https?://[^"]+)"', re.I)
TAG_RE = re.compile(r'<[^>]+>', re.S)
VERIFIED_RE = re.compile(r'vérifi(?:é|ée|és|ées)\s+le\s+([0-9]{1,2}\s+[A-Za-zÀ-ÿ]+\s+[0-9]{4})', re.I)

OFFICIAL_DOMAINS = {
    'remarkable': ('remarkable.com',),
    'boox': ('boox.com',),
    'kindle': ('amazon.com',),
    'kobo': ('kobo.com',),
    'supernote': ('supernote.com',),
}


def text(raw):
    return re.sub(r'\s+', ' ', TAG_RE.sub(' ', raw)).strip()


def slug_for(url):
    rel = url.strip('/')
    return rel.replace('/', '--') or 'home'


def official_source(url, brand):
    host = (urlparse(url).hostname or '').lower()
    return any(host == domain or host.endswith('.' + domain) for domain in OFFICIAL_DOMAINS.get(brand, ()))


for url, spec in PAGES.items():
    path = ROOT / url.strip('/') / 'index.html'
    html = path.read_text(encoding='utf-8')
    article = re.search(r'<article class="content-main">(.*?)</article>', html, re.S)
    body = article.group(1) if article else ''
    rendered_titles = TITLE_RE.findall(html)
    rendered_title = text(rendered_titles[0]) if rendered_titles else spec['title']
    body_text = text(body)
    verified_matches = VERIFIED_RE.findall(body_text)
    page_verified_at = verified_matches[-1] if verified_matches else VERIFIED_AT
    source_urls = SOURCE_RE.findall(body)
    official_urls = [u for u in source_urls if official_source(u, spec['brand'])]
    independent_urls = [u for u in source_urls if u not in official_urls]
    robots_match = re.search(r'<meta\b[^>]*name="robots"[^>]*content="([^"]*)"', html, re.I)
    rendered_robots = robots_match.group(1).strip() if robots_match else ''

    record = {
        'url': url,
        'title': rendered_title,
        'page_type': spec['page_type'],
        'brand': spec['brand'],
        'verified_at': page_verified_at,
        'h2': [text(x) for x in H2_RE.findall(body)],
        'internal_links': LINK_RE.findall(body),
        'unique_internal_targets': sorted(set(LINK_RE.findall(body))),
        'source_urls': source_urls,
        'official_sources': official_urls,
        'independent_sources': independent_urls,
        'robots': rendered_robots,
        'indexable': rendered_robots.lower() == ROBOTS_DIRECTIVE.lower(),
        'noindex_follow': rendered_robots.lower() == 'noindex,follow',
        'publication_status': PUBLICATION_STATUS,
        'analysis_documentary': 'analyse documentaire' in body_text.lower(),
    }
    (OUT / f'{slug_for(url)}.json').write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding='utf-8')

    review = f'''# Brand QA — {url}\n\n- Page type: `{spec['page_type']}`\n- Brand: `{spec['brand']}`\n- Sources verified: {page_verified_at}\n- H2 count: {len(record['h2'])}\n- Internal links: {len(record['internal_links'])}\n- Unique targets: {len(record['unique_internal_targets'])}\n- Official sources: {len(record['official_sources'])}\n- Independent sources: {len(record['independent_sources'])}\n- Robots: `{rendered_robots}`\n- Publication: `{PUBLICATION_STATUS}`\n\n## Editorial gates\n\n- Entity / range / ecosystem: represented in source data and rendered according to page intent.\n- Fact-check: source presence does not by itself prove every claim; use the page evidence brief and editorial review.\n- Review integrity: no first-hand test may be inferred unless explicitly documented.\n- Humanizer / general-writing / anti-AI-slop / GEO: covered by the completed editorial workflow and publication review.\n\n## Status\n\n`{PUBLICATION_STATUS}`\n'''
    (REVIEWS / f'{slug_for(url)}-brand.md').write_text(review, encoding='utf-8')

for key, brand in BRANDS.items():
    summary = {
        'brand': key,
        'name': brand['name'],
        'positioning': brand['positioning'],
        'current_range': brand['current_range'],
        'ecosystem': brand['ecosystem'],
        'strengths': brand['strengths'],
        'limits': brand['limits'],
        'choose': brand['choose'],
        'avoid': brand['avoid'],
        'verified_at': VERIFIED_AT,
    }
    summary = bespoke_entity_summary(key, summary)
    summary = hub_entity_summary(key, summary)
    (OUT / f'entity-{key}.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')

print(f'generated metadata for {len(PAGES)} brand pages')
