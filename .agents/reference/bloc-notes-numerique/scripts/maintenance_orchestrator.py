"""Prepare existing editorial workflows for execution in chat. No model/API calls."""
import argparse
import hashlib
import json
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECISIONS = {'KEEP', 'LIGHT_UPDATE', 'DEEP_REWRITE', 'MERGE', 'NOINDEX'}


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def inventory(root, config):
    pages = []
    for cluster, route in config['routes'].items():
        for page in sorted((root / cluster).rglob('index.html')):
            url = '/' + page.parent.relative_to(root).as_posix() + '/'
            settings = dict(route, **config.get('overrides', {}).get(url, {}))
            if settings.get('enabled', True) is False:
                continue
            for mode in ('analysis', 'content'):
                skill = f".agents/skills/{settings['workflow']}-{mode}-workflow/SKILL.md"
                if not (root / skill).is_file():
                    raise ValueError(f'Missing workflow: {skill}')
                settings[mode + '_workflow'] = skill
            pages.append(dict(settings, url=url, file=page.relative_to(root).as_posix(),
                              fingerprint=hashlib.sha256(page.read_bytes()).hexdigest()))
    return pages


def prepare(root, today, limit, urls=None):
    config = read(root / 'maintenance.config.json')
    state = read(root / '.content/maintenance/index.json')['pages']
    pages = inventory(root, config)
    requested = set(urls or [])
    if requested - {p['url'] for p in pages}:
        raise ValueError('Unknown or unsupported URLs: ' + ', '.join(sorted(requested - {p['url'] for p in pages})))
    candidates = []
    for page in pages:
        previous = state.get(page['url'])
        due = date.fromisoformat(previous['next_review']) if previous else date.min
        changed = bool(previous and previous['fingerprint'] != page['fingerprint'])
        if requested and page['url'] not in requested:
            continue
        if requested or due <= today or changed:
            page.update(next_review=due.isoformat(), reason='explicit_request' if requested else
                        'changed_since_audit' if changed else 'never_reviewed' if not previous else 'cadence_due')
            candidates.append(page)
    # Oldest reviews first; round-robin across clusters avoids starving guides/usages.
    candidates.sort(key=lambda p: (p['next_review'], p['url']))
    queues = {}
    for page in candidates:
        queues.setdefault(page['workflow'], []).append(page)
    selected = []
    while any(queues.values()) and len(selected) < limit:
        for queue in queues.values():
            if queue and len(selected) < limit:
                selected.append(queue.pop(0))
    return dict(schema_version=1, date=today.isoformat(), status='AWAITING_CHAT_AUDIT',
                inventory_count=len(pages), eligible_count=len(candidates), pages=selected)


def record(root, plan, results):
    selected = {p['url']: p for p in plan['pages']}
    state_path = root / '.content/maintenance/index.json'
    state = read(state_path)
    seen = set()
    for result in results['pages']:
        url = result['url']
        if url not in selected or url in seen or result['decision'] not in DECISIONS:
            raise ValueError('Invalid or duplicate audit result: ' + url)
        seen.add(url)
        page = selected[url]
        # Reject stale plans so a changed page cannot be marked freshly audited.
        current = hashlib.sha256((root / page['file']).read_bytes()).hexdigest()
        if current != page['fingerprint']:
            raise ValueError('Page changed since plan; prepare a new audit: ' + url)
        report = (root / result['audit_report']).resolve()
        if not report.is_relative_to((root / '.content/reviews').resolve()) or not report.is_file():
            raise ValueError('A real audit report under .content/reviews is required')
        reviewed = date.fromisoformat(result['reviewed_at'])
        if reviewed < date.fromisoformat(plan['date']) or reviewed > date.today():
            raise ValueError('Invalid review date')
        decision = result['decision']
        state['pages'][url] = dict(last_reviewed=reviewed.isoformat(),
            next_review=(reviewed + timedelta(days=page['cadence_days'])).isoformat(),
            fingerprint=current, decision=decision, audit_report=result['audit_report'],
            next_action='NONE' if decision == 'KEEP' else 'CONTENT_WORKFLOW' if decision in
            {'LIGHT_UPDATE', 'DEEP_REWRITE'} else 'HUMAN_DECISION',
            content_workflow=page['content_workflow'])
    # Validate all results before writing; preparing a queue never advances review dates.
    write(state_path, state)
    digest = hashlib.sha256(json.dumps(results, sort_keys=True).encode()).hexdigest()[:12]
    write(root / f".content/maintenance/history/{plan['date']}-{digest}.json", results)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('prepare')
    p.add_argument('--date', default=date.today().isoformat())
    p.add_argument('--max-pages', type=int, default=None)
    p.add_argument('--urls', default='', help='Comma-separated canonical paths')
    p.add_argument('--output', default='.artifacts/maintenance')
    r = sub.add_parser('record')
    r.add_argument('--plan', required=True)
    r.add_argument('--results', required=True)
    args = parser.parse_args()
    if args.command == 'record':
        record(ROOT, read(Path(args.plan)), read(Path(args.results)))
        return
    limit = args.max_pages if args.max_pages is not None else read(ROOT / 'maintenance.config.json')['max_pages']
    if not 1 <= limit <= 100:
        parser.error('--max-pages must be between 1 and 100')
    plan = prepare(ROOT, date.fromisoformat(args.date), limit,
                   [u.strip() for u in args.urls.split(',') if u.strip()])
    out = Path(args.output)
    write(out / 'plan.json', plan)
    lines = ['# Maintenance éditoriale — ' + plan['date'], '',
             'Statut : AWAITING_CHAT_AUDIT. Aucun audit IA effectué par GitHub Actions.', '',
             'Lire AGENTS.md et docs/content-maintenance.md, puis exécuter les skills indiqués.', '',
             f"Inventaire : {plan['inventory_count']} ; éligibles : {plan['eligible_count']} ; sélection : {len(plan['pages'])}.", '']
    for page in plan['pages']:
        lines += [f"## {page['url']}", f"- Fichier : `{page['file']}`",
                  f"- Motif : {page['reason']}", f"- AUDIT : `{page['analysis_workflow']}`",
                  f"- Si LIGHT_UPDATE/DEEP_REWRITE : `{page['content_workflow']}`",
                  f"- Validation machine : `python {page['validator']}`",
                  '- Après correction : même workflow analyse, mode PUBLISH_REVIEW.', '']
    out.mkdir(parents=True, exist_ok=True)
    summary = '\n'.join(lines) + '\n'
    (out / 'handoff.md').write_text(summary, encoding='utf-8')
    print(summary)


if __name__ == '__main__':
    main()
