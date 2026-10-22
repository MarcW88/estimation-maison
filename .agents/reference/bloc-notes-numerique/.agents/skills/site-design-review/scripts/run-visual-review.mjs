#!/usr/bin/env node

import { chromium } from '@playwright/test';
import { spawn } from 'node:child_process';
import { mkdir, rm, writeFile } from 'node:fs/promises';
import path from 'node:path';

const BRAND_ROUTES = [
  '/marques/',
  '/marques/remarkable/',
  '/marques/remarkable/remarkable-paper-pro/',
  '/marques/remarkable/remarkable-paper-pro-avis/',
  '/marques/remarkable/remarkable-2/',
  '/marques/remarkable/remarkable-2-avis/',
  '/marques/remarkable/abonnement-connect/',
  '/marques/remarkable/accessoires/',
  '/marques/remarkable/alternatives/',
  '/marques/boox/',
  '/marques/boox/boox-note-air/',
  '/marques/boox/boox-tab-ultra/',
  '/marques/boox/avis/',
  '/marques/boox/accessoires/',
  '/marques/boox/alternatives/',
  '/marques/kindle-scribe/',
  '/marques/kobo-elipsa/',
  '/marques/supernote/'
];

const COMPARISON_ROUTES = [
  '/comparatifs/',
  '/comparatifs/meilleur-bloc-notes-numerique/',
  '/comparatifs/tablette-e-ink/',
  '/comparatifs/bloc-notes-numerique-professionnel/',
  '/comparatifs/bloc-notes-numerique-etudiant/',
  '/comparatifs/bloc-notes-numerique-couleur/',
  '/comparatifs/bloc-notes-numerique-a4/',
  '/comparatifs/bloc-notes-numerique-sans-abonnement/',
  '/comparatifs/bloc-notes-numerique-pas-cher/',
  '/comparatifs/kindle-scribe-vs-remarkable/',
  '/comparatifs/kindle-scribe-vs-kobo-elipsa/',
  '/comparatifs/remarkable-vs-boox/',
  '/comparatifs/remarkable-vs-supernote/',
  '/comparatifs/boox-vs-supernote/',
  '/comparatifs/kobo-elipsa-vs-remarkable/'
];

const USAGE_ROUTES = [
  '/usages/',
  '/usages/prise-de-notes-professionnelle/',
  '/usages/prise-de-notes-etudiant/',
  '/usages/prise-de-notes-reunion/',
  '/usages/lecture-et-prise-de-notes/',
  '/usages/dessin/',
  '/usages/remplacer-cahiers-papier/'
];

const GUIDE_ROUTES = [
  '/guides/',
  '/guides/choisir-bloc-notes-numerique/',
  '/guides/liseuse-ou-bloc-notes-numerique/',
  '/guides/tablette-classique-ou-tablette-e-ink/',
  '/guides/taille-ecran-bloc-notes-numerique/',
  '/guides/bloc-notes-numerique-couleur-ou-noir-et-blanc/',
  '/guides/bloc-notes-numerique-avec-ou-sans-abonnement/',
  '/guides/prix-bloc-notes-numerique/',
  '/guides/tablette-e-ink/',
  '/guides/encre-electronique-fonctionnement/',
  '/guides/latence-ecriture/',
  '/guides/ocr-manuscrit/',
  '/guides/autonomie-tablette-e-ink/',
  '/guides/formats-fichiers-compatibles/',
  '/guides/exporter-notes/',
  '/guides/synchroniser-notes-cloud/',
  '/guides/bloc-notes-numerique-google-drive/',
  '/guides/bloc-notes-numerique-onedrive/',
  '/guides/bloc-notes-numerique-dropbox/',
  '/guides/ecosysteme-ouvert-ou-ferme/',
  '/guides/annoter-pdf-tablette-e-ink/',
  '/guides/convertir-notes-manuscrites-en-texte/',
  '/guides/organiser-notes-numeriques/',
  '/guides/transfert-notes-vers-ordinateur/',
  '/guides/imprimer-notes-numeriques/'
];

const DEAL_ROUTES = [
  '/bons-plans/',
  '/bons-plans/bloc-notes-numerique/',
  '/bons-plans/remarkable/',
  '/bons-plans/kindle-scribe/',
  '/bons-plans/kobo-elipsa/',
  '/bons-plans/boox/',
  '/bons-plans/bloc-notes-numerique-occasion/',
  '/bons-plans/black-friday/'
];

const SCOPES = {
  brands: BRAND_ROUTES,
  comparisons: COMPARISON_ROUTES,
  usages: USAGE_ROUTES,
  guides: GUIDE_ROUTES,
  deals: DEAL_ROUTES
};

const VIEWPORTS = [
  { name: 'desktop', width: 1440, height: 1000 },
  { name: 'mobile', width: 390, height: 844 }
];

function parseArgs(argv) {
  const options = {
    baseUrl: '',
    output: '.artifacts/design-review',
    port: 4173,
    routes: [],
    scope: ''
  };

  for (let index = 0; index < argv.length; index += 1) {
    const value = argv[index];
    const next = argv[index + 1];
    if (value === '--base-url') options.baseUrl = next, index += 1;
    else if (value === '--output') options.output = next, index += 1;
    else if (value === '--port') options.port = Number(next), index += 1;
    else if (value === '--route') options.routes.push(next), index += 1;
    else if (value === '--scope') options.scope = next, index += 1;
    else if (value === '--help') options.help = true;
    else throw new Error(`Option inconnue : ${value}`);
  }

  if (options.scope && !SCOPES[options.scope]) {
    throw new Error(`Scope inconnu : ${options.scope}. Scopes disponibles : ${Object.keys(SCOPES).join(', ')}`);
  }
  if (!options.routes.length && options.scope) options.routes = SCOPES[options.scope];
  if (!options.routes.length) options.routes = ['/marques/'];
  return options;
}

function slug(route) {
  return route.replace(/^\/+|\/+$/g, '').replaceAll('/', '--') || 'home';
}

async function waitForServer(url) {
  for (let attempt = 0; attempt < 50; attempt += 1) {
    try {
      const response = await fetch(url);
      if (response.ok) return;
    } catch {}
    await new Promise(resolve => setTimeout(resolve, 100));
  }
  throw new Error(`Le serveur local ne répond pas : ${url}`);
}

const options = parseArgs(process.argv.slice(2));
if (options.help) {
  console.log('Usage: run-visual-review.mjs [--scope brands|comparisons|usages|guides|deals] [--route /chemin/] [--base-url URL] [--output dossier] [--port 4173]');
  process.exit(0);
}

const outputRoot = path.resolve(options.output);
await rm(outputRoot, { recursive: true, force: true });
await mkdir(outputRoot, { recursive: true });

let server;
let baseUrl = options.baseUrl.replace(/\/$/, '');
if (!baseUrl) {
  baseUrl = `http://127.0.0.1:${options.port}`;
  server = spawn('python3', ['-m', 'http.server', String(options.port), '--bind', '127.0.0.1', '--directory', '.'], {
    stdio: ['ignore', 'pipe', 'pipe']
  });
  await waitForServer(`${baseUrl}/`);
}

const report = {
  generatedAt: new Date().toISOString(),
  baseUrl,
  scope: options.scope || null,
  routes: options.routes,
  viewports: VIEWPORTS,
  pages: []
};

let browser;
try {
  browser = await chromium.launch({ headless: true });

  for (const viewport of VIEWPORTS) {
    const context = await browser.newContext({
      viewport: { width: viewport.width, height: viewport.height },
      reducedMotion: 'reduce'
    });

    for (const route of options.routes) {
      const page = await context.newPage();
      const consoleErrors = [];
      const pageErrors = [];
      page.on('console', message => {
        if (message.type() === 'error') consoleErrors.push(message.text());
      });
      page.on('pageerror', error => pageErrors.push(error.message));

      const response = await page.goto(`${baseUrl}${route}`, { waitUntil: 'networkidle' });
      await page.evaluate(() => document.fonts?.ready);

      const measurements = await page.evaluate(() => {
        const sidebar = document.querySelector('.content-sidebar');
        const headings = [...document.querySelectorAll('.content-main h2, .content-main h3')];
        const toc = document.querySelector('.sidebar-toc');
        const tocLinks = [...document.querySelectorAll('.sidebar-toc a')];
        const fixedHeader = document.querySelector('.site-header');
        const tables = [...document.querySelectorAll('.table-wrapper')];
        const articleAnswer = document.querySelector('.article-answer');
        const firstEditorialLink = document.querySelector('.content-main a:not(.btn)');
        return {
          title: document.title,
          statusReady: document.readyState,
          horizontalOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
          scrollWidth: document.documentElement.scrollWidth,
          clientWidth: document.documentElement.clientWidth,
          headingCount: headings.length,
          tocLinkCount: tocLinks.length,
          tocParentClass: toc?.parentElement?.className || null,
          missingHeadingIds: headings.filter(heading => !heading.id).map(heading => heading.textContent.trim()),
          tableCount: tables.length,
          rawTableCount: document.querySelectorAll('.content-main table:not(.comp-table)').length,
          overflowingTables: tables
            .filter(wrapper => wrapper.scrollWidth > wrapper.clientWidth)
            .map(wrapper => ({ scrollWidth: wrapper.scrollWidth, clientWidth: wrapper.clientWidth })),
          articleAnswer: articleAnswer ? {
            height: Math.round(articleAnswer.getBoundingClientRect().height),
            background: getComputedStyle(articleAnswer).backgroundColor,
            borderLeftWidth: getComputedStyle(articleAnswer).borderLeftWidth
          } : null,
          firstEditorialLink: firstEditorialLink ? {
            color: getComputedStyle(firstEditorialLink).color,
            decoration: getComputedStyle(firstEditorialLink).textDecorationLine
          } : null,
          sidebar: sidebar ? {
            height: Math.round(sidebar.getBoundingClientRect().height),
            top: Math.round(sidebar.getBoundingClientRect().top),
            position: getComputedStyle(sidebar).position
          } : null,
          headerHeight: fixedHeader ? Math.round(fixedHeader.getBoundingClientRect().height) : 0
        };
      });

      const viewportFolder = path.join(outputRoot, viewport.name);
      await mkdir(viewportFolder, { recursive: true });
      const screenshot = path.join(viewportFolder, `${slug(route)}.png`);
      await page.screenshot({ path: screenshot, fullPage: true, animations: 'disabled' });

      if (viewport.name === 'mobile' && route === options.routes[0]) {
        const burger = page.locator('.burger');
        if (await burger.count()) {
          await burger.click();
          await page.screenshot({
            path: path.join(viewportFolder, `${slug(route)}--menu-open.png`),
            fullPage: false,
            animations: 'disabled'
          });
        }
      }

      report.pages.push({
        route,
        viewport: viewport.name,
        httpStatus: response?.status() ?? null,
        screenshot: path.relative(process.cwd(), screenshot),
        consoleErrors,
        pageErrors,
        ...measurements
      });
      await page.close();
    }
    await context.close();
  }
} finally {
  if (browser) await browser.close();
  if (server) server.kill('SIGTERM');
}

await writeFile(path.join(outputRoot, 'report.json'), `${JSON.stringify(report, null, 2)}\n`);
console.log(`Captures créées : ${report.pages.length}`);
console.log(`Rapport : ${path.join(outputRoot, 'report.json')}`);
