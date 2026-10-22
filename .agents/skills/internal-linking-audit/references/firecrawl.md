# Firecrawl Mode

Use Firecrawl when basic HTTP crawling fails, when pages need JavaScript rendering, or when Cloudflare/anti-bot protection blocks normal requests.

## API Key

Accept the key via either:

- environment variable: `FIRECRAWL_API_KEY`
- CLI arg: `--firecrawl-api-key`

Never print the key. Never write it into reports, CSV, JSON, or logs.

## REST API Path

The bundled script uses Firecrawl v2 Scrape:

- endpoint: `POST https://api.firecrawl.dev/v2/scrape`
- auth: `Authorization: Bearer <token>`
- payload essentials:
  - `url`
  - `formats`: `html`, `rawHtml`, `links`, `markdown`
  - `onlyMainContent: false`
  - `blockAds: true`
  - `proxy: auto`

Use the returned `html` or `rawHtml` for link extraction. If only markdown is available, extract markdown links as a fallback but mark the output as lower confidence.

## MCP Path

If Firecrawl MCP tools are available in the session:

1. Use the MCP scrape/render tool for each source URL.
2. Request full HTML/raw HTML, not only markdown, because region classification needs DOM context.
3. Feed the returned HTML into the same link extraction and region classification logic.
4. If MCP returns links but no HTML, use it for target URL existence detection only and do not claim navigation/footer/body classification.

## Failure Rules

- 401/403: ask user to verify the API key or switch to import mode.
- 402/429: stop or reduce scope; do not retry aggressively.
- timeout: retry once with a higher timeout; if still failing, mark blocked.
- no HTML/raw HTML: use markdown links only for existence checks, not for region breakdown.

## User-Facing Copy

Use precise language:

- “Target URL already exists in body links”
- “Target URL exists only in navigation/footer/CTA; contextual body link may still be useful”
- “Page could not be read; no recommendation generated”
