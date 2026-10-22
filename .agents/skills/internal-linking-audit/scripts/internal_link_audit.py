#!/usr/bin/env python3
"""Verified internal linking audit.

Inputs a JSON config with brand/domain/pages/candidate links, fetches pages with
basic HTTP or Firecrawl, classifies internal anchors by region, and outputs
HTML/CSV/JSON reports. The script never recommends a link for an unreadable page.
"""
from __future__ import annotations

import argparse
import csv
import html
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import sys
import time
from typing import Any
from urllib import parse, request, error

DEFAULT_UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
FIRECRAWL_ENDPOINT = "https://api.firecrawl.dev/v2/scrape"


def load_config(path: Path) -> dict[str, Any]:
    text = path.read_text()
    if path.suffix.lower() == ".json":
        return json.loads(text)
    return parse_simple_yaml(text)


def parse_simple_yaml(text: str) -> dict[str, Any]:
    """Small YAML subset parser for simple skill inputs; prefer JSON for nesting."""
    result: dict[str, Any] = {}
    current_key: str | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not raw.startswith(" ") and ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value == "":
                result[key] = {}
                current_key = key
            else:
                result[key] = coerce_scalar(value)
                current_key = None
        elif current_key and raw.startswith("  ") and ":" in line:
            key, value = line.strip().split(":", 1)
            result[current_key][key.strip()] = coerce_scalar(value.strip())
        else:
            raise ValueError(f"Unsupported YAML line: {raw}")
    return result


def coerce_scalar(value: str) -> Any:
    value = value.strip().strip('"').strip("'")
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    if value.isdigit():
        return int(value)
    return value


def normalized_domain(domain: str) -> str:
    domain = domain.rstrip("/")
    if not domain.startswith(("http://", "https://")):
        domain = "https://" + domain
    return domain


def normalize_url(href: str | None, base_url: str, domain: str) -> str | None:
    if not href:
        return None
    href = html.unescape(href).split("#", 1)[0].strip()
    if not href or href.startswith(("mailto:", "tel:", "javascript:", "data:")):
        return None
    href = parse.urljoin(base_url, href)
    parsed = parse.urlsplit(href)
    domain_host = parse.urlsplit(domain).netloc.lower().replace("www.", "")
    href_host = parsed.netloc.lower().replace("www.", "")
    if href_host != domain_host:
        return None
    path = parsed.path.rstrip("/") or "/"
    return parse.urlunsplit((parsed.scheme or "https", parsed.netloc, path, "", ""))


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[dict[str, Any]] = []
        self.links: list[dict[str, Any]] = []
        self.current: dict[str, Any] | None = None
        self.title_parts: list[str] = []
        self.h1_parts: list[str] = []
        self._in_title = False
        self._h1_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attr_dict = {k.lower(): (v or "") for k, v in attrs}
        node = {"tag": tag, "attrs": attr_dict}
        self.stack.append(node)
        if tag == "title":
            self._in_title = True
        if tag == "h1":
            self._h1_depth += 1
        if tag == "a":
            self.current = {"href": attr_dict.get("href"), "text": "", "ancestors": list(self.stack)}
            self.links.append(self.current)

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_parts.append(data)
        if self._h1_depth:
            self.h1_parts.append(data)
        if self.current is not None:
            self.current["text"] += data

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            self._in_title = False
        if tag == "h1" and self._h1_depth:
            self._h1_depth -= 1
        if tag == "a":
            self.current = None
        for idx in range(len(self.stack) - 1, -1, -1):
            if self.stack[idx]["tag"] == tag:
                self.stack = self.stack[:idx]
                break

    @property
    def title(self) -> str:
        return squash(" ".join(self.title_parts))

    @property
    def h1(self) -> str:
        return squash(" ".join(self.h1_parts))


def squash(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def classify_region(link: dict[str, Any]) -> str:
    tags: list[str] = []
    meta_parts: list[str] = []
    for ancestor in link["ancestors"]:
        tags.append(ancestor["tag"])
        attrs = ancestor["attrs"]
        meta_parts.append(" ".join([attrs.get("class", ""), attrs.get("id", ""), attrs.get("role", ""), attrs.get("aria-label", "")]).lower())
    meta = " ".join(meta_parts)
    text = squash(link.get("text", "")).lower()
    href = (link.get("href") or "").lower()
    if "footer" in tags or "footer" in meta:
        return "footer"
    if "nav" in tags or "navigation" in meta or "navbar" in meta or "site-header" in meta:
        return "navigation"
    if "menu" in meta or "dropdown" in meta or "popover" in meta or "menubar" in meta:
        return "menu"
    cta_words = ["book", "demo", "try", "trial", "start", "sign up", "signup", "contact", "pricing", "get started", "audit", "login", "log in"]
    if any(word in text for word in cta_words) or any(word.replace(" ", "-") in href for word in cta_words):
        return "cta"
    return "body"


def extract_links(page_url: str, domain: str, html_text: str) -> dict[str, Any]:
    parser = LinkParser()
    parser.feed(html_text)
    links: list[dict[str, str]] = []
    for raw in parser.links:
        normalized = normalize_url(raw.get("href"), page_url, domain)
        if normalized:
            links.append({"url": normalized, "region": classify_region(raw), "anchor": squash(raw.get("text", ""))})
    breakdown = {key: 0 for key in ["navigation", "menu", "footer", "cta", "body"]}
    unique_by_region = {key: set() for key in breakdown}
    for link in links:
        breakdown[link["region"]] += 1
        unique_by_region[link["region"]].add(link["url"])
    return {
        "title": parser.title,
        "h1": parser.h1,
        "links": links,
        "unique_urls": sorted({link["url"] for link in links}),
        "breakdown": breakdown,
        "unique_breakdown": {key: len(values) for key, values in unique_by_region.items()},
    }


def fetch_basic(url: str, timeout: int) -> tuple[str, dict[str, Any]]:
    req = request.Request(url, headers={"User-Agent": DEFAULT_UA, "Accept": "text/html,application/xhtml+xml"})
    with request.urlopen(req, timeout=timeout) as response:
        content_type = response.headers.get("content-type", "")
        body = response.read().decode("utf-8", "ignore")
        return body, {"status_code": response.status, "content_type": content_type, "fetcher": "basic"}


def fetch_firecrawl(url: str, api_key: str, timeout: int) -> tuple[str, dict[str, Any]]:
    payload = json.dumps({
        "url": url,
        "formats": ["html", "rawHtml", "links", "markdown"],
        "onlyMainContent": False,
        "timeout": timeout * 1000,
        "removeBase64Images": True,
        "blockAds": True,
        "proxy": "auto",
    }).encode("utf-8")
    req = request.Request(
        FIRECRAWL_ENDPOINT,
        data=payload,
        method="POST",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    )
    with request.urlopen(req, timeout=timeout + 15) as response:
        data = json.loads(response.read().decode("utf-8"))
    if not data.get("success"):
        raise RuntimeError(f"Firecrawl scrape failed: {data}")
    doc = data.get("data") or {}
    html_text = doc.get("html") or doc.get("rawHtml") or ""
    if not html_text and doc.get("markdown"):
        html_text = markdown_links_to_html(doc["markdown"])
    return html_text, {"status_code": (doc.get("metadata") or {}).get("statusCode"), "fetcher": "firecrawl", "metadata": doc.get("metadata", {})}


def markdown_links_to_html(markdown: str) -> str:
    anchors = []
    for label, href in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", markdown):
        anchors.append(f'<a href="{html.escape(href)}">{html.escape(label)}</a>')
    return "\n".join(anchors)


def load_imported_html(import_dir: Path, url: str) -> str | None:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", parse.urlsplit(url).path.strip("/") or "home").strip("-")
    for candidate in [import_dir / f"{slug}.html", import_dir / f"{slug}.raw.html", import_dir / f"{slug}.json"]:
        if not candidate.exists():
            continue
        if candidate.suffix == ".json":
            data = json.loads(candidate.read_text())
            return data.get("html") or data.get("rawHtml") or data.get("markdown")
        return candidate.read_text()
    return None


def source_pages_from_config(config: dict[str, Any]) -> list[str]:
    pages = config.get("priority_pages") or config.get("pages") or []
    if isinstance(pages, str):
        pages = [pages]
    candidate_links = config.get("candidate_links") or []
    for item in candidate_links:
        source = item.get("source") or item.get("source_page")
        if source and source not in pages:
            pages.append(source)
    return pages


def target_for_candidate(candidate: dict[str, Any], domain: str, source_url: str) -> dict[str, Any]:
    target = candidate.get("target") or candidate.get("target_page") or candidate.get("target_page_to_link")
    if not target:
        raise ValueError(f"Candidate link missing target: {candidate}")
    return {
        "source": parse.urljoin(domain + "/", candidate.get("source") or candidate.get("source_page") or source_url),
        "target": parse.urljoin(domain + "/", target),
        "anchor": candidate.get("anchor") or candidate.get("anchor_text") or "",
        "placement": candidate.get("placement") or candidate.get("where_to_place_it") or "",
        "reason": candidate.get("reason") or candidate.get("why") or "",
        "priority": candidate.get("priority") or "P1",
    }


def decide(candidate: dict[str, Any], links: list[dict[str, str]], domain: str) -> dict[str, Any]:
    target = normalize_url(candidate["target"], candidate["source"], domain)
    matching = [link for link in links if link["url"] == target]
    body_matches = [link for link in matching if link["region"] == "body"]
    if body_matches:
        action = "no_action_needed"
        recommendation = "Target URL already exists in body/contextual links."
    elif matching:
        action = "add_contextual_body_link"
        regions = sorted({m["region"] for m in matching})
        recommendation = f"Target URL exists only in non-body regions ({', '.join(regions)}); add only if the suggested body placement is genuinely useful."
    else:
        action = "add_internal_link"
        recommendation = "Target URL was not found in fetched source HTML."
    return {"target_normalized": target, "action": action, "recommendation": recommendation, "target_instances": matching, "body_target_instances": body_matches}


def render_html(output: dict[str, Any], output_dir: Path) -> None:
    brand = output["brand"]
    summary = output["summary"]
    pages = output["pages"]
    blocked = output["blocked_pages"]
    cards = "".join([
        card("Checked pages", summary["checked_pages"], "HTTP 200 / imported pages"),
        card("Add internal link", summary["add_internal_link"], "Target missing in HTML"),
        card("Add contextual link", summary["add_contextual_body_link"], "Target exists outside body"),
        card("No action needed", summary["no_action_needed"], "Target already in body"),
        card("Blocked", len(blocked), "Unreadable pages"),
    ])
    sections = []
    for page in pages:
        actionable = [item for item in page["recommendations"] if item["action"] != "no_action_needed"]
        if not actionable:
            continue
        stats = page["stats"]
        breakdown = "".join(mini(label, stats["breakdown"][key], stats["unique_breakdown"][key]) for key, label in [("navigation", "Navigation"), ("menu", "Menu"), ("footer", "Footer"), ("cta", "CTA"), ("body", "Body")])
        recs = []
        for item in actionable:
            recs.append(f'''
            <div class="recommendation">
              <div class="recommendation-top"><a class="target-url" href="{esc(item['target'])}" target="_blank" rel="noreferrer">{esc(item['target'])}</a><span class="tag {esc(item['priority']).lower()}">{esc(item['priority'])}</span></div>
              <div class="field-grid">
                <div class="field"><strong>Action</strong>{esc(item['action'].replace('_', ' '))}</div>
                <div class="field"><strong>Anchor</strong>{esc(item['anchor'])}</div>
                <div class="field"><strong>Placement</strong>{esc(item['placement'])}</div>
                <div class="field wide"><strong>Optimization analysis</strong>{esc(item['recommendation'])} {esc(item['reason'])}</div>
              </div>
            </div>''')
        sections.append(f'''
        <article class="work-order">
          <div class="work-order-head"><div><a class="source-url" href="{esc(page['url'])}" target="_blank" rel="noreferrer">{esc(page['url'])}</a><div class="source-meta">Internal anchor instances: {stats['total_links']} · Unique internal URLs: {stats['unique_links']} · Actionable items: {len(actionable)}</div></div></div>
          <div class="breakdown-grid">{breakdown}</div>
          <div class="recommendations">{''.join(recs)}</div>
        </article>''')
    blocked_html = ""
    if blocked:
        blocked_html = '<section class="section"><h2>Unreadable pages</h2>' + "".join(f"<p>{esc(item['url'])}: {esc(item['error'])}</p>" for item in blocked) + "</section>"
    doc = f'''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{esc(brand.get('name','Brand'))} Internal Linking Audit</title>{STYLE}</head><body><header><div class="shell"><h1><span>{esc(brand.get('name','Brand'))}</span> internal linking action plan</h1></div></header><main class="shell"><section class="section"><h2>Verified crawl summary</h2><div class="cards">{cards}</div></section><section class="section"><h2>Action plan</h2><div class="work-orders">{''.join(sections)}</div></section>{blocked_html}</main></body></html>'''
    (output_dir / "index.html").write_text(doc)


def card(title: str, metric: Any, subtitle: str) -> str:
    return f'<div class="card"><div class="kicker">{esc(title)}</div><div class="metric">{esc(metric)}</div><div class="metric-sub">{esc(subtitle)}</div></div>'


def mini(label: str, count: int, unique: int) -> str:
    return f'<div class="mini-stat"><span>{esc(label)}</span><strong>{count}</strong><em>unique URLs: {unique}</em></div>'


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


STYLE = """
<style>
:root{--bg:#fff;--text:#0b0b0f;--muted:#666670;--line:#e9e6e2;--soft:#faf8f6;--accent:#ff6b2b;--accent-soft:#fff0e9}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.45}.shell{max-width:1180px;margin:0 auto;padding:0 24px}header{border-bottom:1px solid var(--line);background:linear-gradient(180deg,#fff 0%,#fff7f2 100%);padding:46px 0}h1{font-size:clamp(34px,5vw,64px);line-height:.98;margin:0;letter-spacing:-.06em}h1 span,.target-url{color:var(--accent)}a{color:inherit}.section{margin:28px 0;padding:26px;border:1px solid var(--line);border-radius:28px;background:#fff}h2{margin:0 0 20px;font-size:28px}.cards{display:grid;grid-template-columns:repeat(5,1fr);gap:14px}.card,.mini-stat{background:var(--soft);border:1px solid var(--line);border-radius:20px;padding:18px}.kicker,.mini-stat span,.field strong{color:var(--muted);font-size:12px;font-weight:800;text-transform:uppercase;letter-spacing:.08em}.metric{font-size:34px;font-weight:900}.work-orders{display:grid;gap:18px}.work-order{border:1px solid var(--line);border-radius:22px;overflow:hidden}.work-order-head{padding:18px;background:var(--soft);border-bottom:1px solid var(--line)}.source-url{font-weight:900;overflow-wrap:anywhere}.source-meta{margin-top:6px;color:var(--muted)}.breakdown-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;padding:14px 16px 0}.mini-stat{padding:10px}.mini-stat strong{display:block;font-size:24px}.mini-stat em{font-style:normal;color:var(--muted);font-size:12px}.recommendations{padding:16px;display:grid;gap:12px}.recommendation{border:1px solid var(--line);border-radius:18px;padding:15px}.recommendation-top{display:flex;justify-content:space-between;gap:14px;margin-bottom:12px}.tag{border-radius:999px;padding:6px 10px;font-size:12px;font-weight:900;background:#111;color:#fff}.tag.p0{background:var(--accent)}.field-grid{display:grid;grid-template-columns:1fr 1fr 1.2fr;gap:10px}.field{background:var(--soft);border-radius:14px;padding:12px}.field.wide{grid-column:1/-1}@media(max-width:900px){.cards,.breakdown-grid,.field-grid{grid-template-columns:1fr}}
</style>
"""


def write_outputs(output: dict[str, Any], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "audit.json").write_text(json.dumps(output, indent=2, ensure_ascii=False))
    csv_rows = []
    for page in output["pages"]:
        stats = page["stats"]
        for item in page["recommendations"]:
            row = {
                "source_page": page["url"],
                "target_page": item["target"],
                "action": item["action"],
                "priority": item["priority"],
                "anchor_text": item["anchor"],
                "placement": item["placement"],
                "reason": item["reason"],
                "target_instances_total": len(item["target_instances"]),
                "target_instances_in_body": len(item["body_target_instances"]),
                "internal_anchor_instances_total": stats["total_links"],
                "unique_internal_urls_total": stats["unique_links"],
            }
            for key in ["navigation", "menu", "footer", "cta", "body"]:
                row[f"{key}_link_instances"] = stats["breakdown"][key]
                row[f"unique_{key}_urls"] = stats["unique_breakdown"][key]
            csv_rows.append(row)
    if csv_rows:
        with (output_dir / "action-plan.csv").open("w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=list(csv_rows[0].keys()))
            writer.writeheader()
            writer.writerows(csv_rows)
    render_html(output, output_dir)


def run(config: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    brand = config.get("brand") or {}
    domain = normalized_domain(brand.get("domain") or config.get("domain"))
    mode = args.mode or config.get("crawl_mode") or "basic"
    timeout = int(args.timeout or config.get("timeout", 30))
    import_dir = Path(args.import_dir) if args.import_dir else None
    firecrawl_key = args.firecrawl_api_key or os.getenv("FIRECRAWL_API_KEY")
    candidate_links = config.get("candidate_links") or []
    source_pages = source_pages_from_config(config)
    if not source_pages:
        raise ValueError("Config must include pages/priority_pages or candidate_links with source fields.")
    pages = []
    blocked = []
    summary = {"checked_pages": 0, "add_internal_link": 0, "add_contextual_body_link": 0, "no_action_needed": 0}
    for source in source_pages:
        page_url = parse.urljoin(domain + "/", source)
        try:
            if mode == "import":
                if not import_dir:
                    raise ValueError("--import-dir is required for import mode")
                html_text = load_imported_html(import_dir, page_url)
                if not html_text:
                    raise FileNotFoundError(f"No imported HTML/JSON for {page_url}")
                meta = {"fetcher": "import", "status_code": None}
            elif mode == "firecrawl":
                if not firecrawl_key:
                    raise ValueError("FIRECRAWL_API_KEY or --firecrawl-api-key is required for firecrawl mode")
                html_text, meta = fetch_firecrawl(page_url, firecrawl_key, timeout)
            else:
                html_text, meta = fetch_basic(page_url, timeout)
            extracted = extract_links(page_url, domain, html_text)
        except Exception as exc:
            blocked.append({"url": page_url, "error": str(exc), "suggested_next_step": "Retry with firecrawl mode or import CMS/exported HTML."})
            continue
        source_candidates = [target_for_candidate(item, domain, page_url) for item in candidate_links if parse.urljoin(domain + "/", item.get("source") or item.get("source_page") or "") == page_url]
        recommendations = []
        for candidate in source_candidates:
            decision = decide(candidate, extracted["links"], domain)
            item = {**candidate, **decision}
            recommendations.append(item)
            summary[item["action"]] += 1
        pages.append({
            "url": page_url,
            "fetch": meta,
            "title": extracted["title"],
            "h1": extracted["h1"],
            "stats": {"total_links": len(extracted["links"]), "unique_links": len(extracted["unique_urls"]), "breakdown": extracted["breakdown"], "unique_breakdown": extracted["unique_breakdown"]},
            "recommendations": recommendations,
        })
        summary["checked_pages"] += 1
        time.sleep(float(config.get("request_delay_seconds", 0.2)))
    return {"brand": brand, "domain": domain, "crawl_mode": mode, "summary": summary, "pages": pages, "blocked_pages": blocked}


def main() -> int:
    parser = argparse.ArgumentParser(description="Verified internal linking audit")
    parser.add_argument("--config", required=True, help="JSON or simple YAML config")
    parser.add_argument("--output", required=True, help="Output directory")
    parser.add_argument("--mode", choices=["basic", "firecrawl", "import"], help="Override crawl mode")
    parser.add_argument("--firecrawl-api-key", help="Firecrawl API key; alternatively set FIRECRAWL_API_KEY")
    parser.add_argument("--import-dir", help="Directory with exported HTML/JSON files")
    parser.add_argument("--timeout", type=int, default=30)
    args = parser.parse_args()
    config = load_config(Path(args.config))
    output = run(config, args)
    write_outputs(output, Path(args.output))
    print(json.dumps(output["summary"], indent=2))
    if output["blocked_pages"]:
        print("Blocked pages were not analyzed:", file=sys.stderr)
        for item in output["blocked_pages"]:
            print(f"- {item['url']}: {item['error']}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
