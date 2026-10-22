#!/usr/bin/env node

import { chromium } from '@playwright/test';
import { spawn } from 'node:child_process';
import { mkdir, rm, writeFile } from 'node:fs/promises';
import path from 'node:path';

const BRAND_ROUTES = [
  '/marques/',
  '/marques/bosch/',
  '/marques/karcher/',
  '/marques/makita/',
  '/marques/festool/',
  '/marques/dewalt/',
  '/marques/parkside/',
  '/marques/nilfisk/',
  '/marques/mirka/'
];

const COMPARISON_ROUTES = [
  '/comparatifs/',
  '/comparatifs/meilleur-aspirateur-de-chantier/',
  '/comparatifs/aspirateur-eau-poussiere/',
  '/comparatifs/aspirateur-chantier-sans-fil/',
  '/comparatifs/aspirateur-chantier-sans-sac/',
  '/comparatifs/aspirateur-chantier-puissant/',
  '/comparatifs/aspirateur-professionnel/',
  '/comparatifs/aspirateur-industriel/',
  '/comparatifs/aspirateur-classe-m/',
  '/comparatifs/petit-aspirateur-de-chantier/'
];

const SCOPES = { brands: BRAND_ROUTES, comparisons: COMPARISON_ROUTES };
const VIEWPORTS = [
  { name: 'desktop', width: 1440, height: 1000 },
  { name: 'mobile', width: 390, height: 844 }
];

function parseArgs(argv) {
  const options = { baseUrl: '', output: '.artifacts/design-review', port: 4173, routes: [], scope: '' };
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
  if (options.scope && !SCOPES[options.scope]) throw new Error(`Scope inconnu : ${options.scope}. Scopes disponibles : ${Object.keys(SCOPES).join(', ')}`);
  if (!options.routes.length && options.scope) options.routes = SCOPES[options.scope];
  if (!options.routes.length) options.routes = BRAND_ROUTES;
  return options;
}

function slug(route) {
  return route.replace(/^\/+|\/+$/g, '').replaceAll('/', '--') || 'home';
}

async function waitForServer(url) {
  for (let attempt = 0; attempt < 60; attempt += 1) {
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
  console.log('Usage: run-visual-review.mjs [--scope brands|comparisons] [--route /chemin/] [--base-url URL] [--output dossier] [--port 4173]');
  process.exit(0);
}

const outputRoot = path.resolve(options.output);
await rm(outputRoot, { recursive: true, force: true });
await mkdir(outputRoot, { recursive: true });

let server;
let baseUrl = options.baseUrl.replace(/\/$/, '');
if (!baseUrl) {
  baseUrl = `http://127.0.0.1:${options.port}`;
  server = spawn('python3', ['-m', 'http.server', String(options.port), '--bind', '127.0.0.1', '--directory', '.'], { stdio: ['ignore', 'pipe', 'pipe'] });
  await waitForServer(`${baseUrl}/`);
}

const report = {
  generatedAt: new Date().toISOString(),
  baseUrl,
  scope: options.scope || 'brands',
  routes: options.routes,
  viewports: VIEWPORTS,
  pages: []
};

let browser;
try {
  browser = await chromium.launch({ headless: true });
  for (const viewport of VIEWPORTS) {
    const context = await browser.newContext({ viewport: { width: viewport.width, height: viewport.height }, reducedMotion: 'reduce' });
    for (const route of options.routes) {
      const page = await context.newPage();
      const consoleErrors = [];
      const pageErrors = [];
      page.on('console', message => { if (message.type() === 'error') consoleErrors.push(message.text()); });
      page.on('pageerror', error => pageErrors.push(error.message));

      const response = await page.goto(`${baseUrl}${route}`, { waitUntil: 'networkidle' });
      await page.evaluate(() => document.fonts?.ready);

      const measurements = await page.evaluate(() => {
        const sidebar = document.querySelector('.content-sidebar');
        const main = document.querySelector('.content-main');
        const tocBox = document.querySelector('.mobile-toc-box') || sidebar?.querySelector('.sidebar-box:first-child');
        const headings = [...document.querySelectorAll('.content-main h2, .content-main h3')];
        const tocLinks = [...document.querySelectorAll('.toc-list a')];
        const fixedHeader = document.querySelector('.site-header');
        const tables = [...document.querySelectorAll('.content-main table')];
        const answerBox = document.querySelector('.answer-box');
        const burger = document.querySelector('.burger');
        const siteNav = document.querySelector('.site-nav');
        const images = [...document.querySelectorAll('img')];
        const contentLinks = [...document.querySelectorAll('.content-main a')];
        const primaryActions = [...document.querySelectorAll('.content-main .btn-primary, .content-main .btn-accent')];
        const decisionModules = [...document.querySelectorAll('.comparison-decision-module')];
        const mobileHandoffs = [...document.querySelectorAll('.comparison-mobile-handoff')];
        const brokenTocTargets = tocLinks.map(link => link.getAttribute('href')).filter(href => href?.startsWith('#') && !document.getElementById(href.slice(1)));
        const tocBeforeArticle = tocBox && main ? Boolean(tocBox.compareDocumentPosition(main) & Node.DOCUMENT_POSITION_FOLLOWING) : null;

        return {
          title: document.title,
          statusReady: document.readyState,
          horizontalOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
          scrollWidth: document.documentElement.scrollWidth,
          clientWidth: document.documentElement.clientWidth,
          h1Count: document.querySelectorAll('h1').length,
          headingCount: headings.length,
          tocLinkCount: tocLinks.length,
          tocBeforeArticle,
          tocTop: tocBox ? Math.round(tocBox.getBoundingClientRect().top + window.scrollY) : null,
          missingHeadingIds: headings.filter(heading => !heading.id).map(heading => heading.textContent.trim()),
          brokenTocTargets,
          tableCount: tables.length,
          tables: tables.map((table, index) => {
            const wrapper = table.closest('.table-wrap, .data-table-wrap');
            const rect = table.getBoundingClientRect();
            const parent = table.parentElement;
            return {
              index,
              hasExpectedWrapper: Boolean(wrapper),
              width: Math.round(rect.width),
              parentWidth: parent ? Math.round(parent.getBoundingClientRect().width) : null,
              exceedsParent: parent ? table.scrollWidth > parent.clientWidth : false,
              exceedsViewport: rect.right > document.documentElement.clientWidth || rect.left < 0
            };
          }),
          answerBox: answerBox ? {
            height: Math.round(answerBox.getBoundingClientRect().height),
            background: getComputedStyle(answerBox).backgroundColor,
            borderLeftWidth: getComputedStyle(answerBox).borderLeftWidth
          } : null,
          sidebar: sidebar ? {
            width: Math.round(sidebar.getBoundingClientRect().width),
            height: Math.round(sidebar.getBoundingClientRect().height),
            top: Math.round(sidebar.getBoundingClientRect().top + window.scrollY),
            position: getComputedStyle(sidebar).position
          } : null,
          mainWidth: main ? Math.round(main.getBoundingClientRect().width) : null,
          headerHeight: fixedHeader ? Math.round(fixedHeader.getBoundingClientRect().height) : 0,
          affiliateDisclosureCount: document.querySelectorAll('.affil-note').length,
          contentLinkCount: contentLinks.length,
          primaryActionCount: primaryActions.length,
          decisionModuleCount: decisionModules.length,
          mobileHandoffCount: mobileHandoffs.length,
          imageCount: images.length,
          imagesMissingAlt: images.filter(image => !image.hasAttribute('alt')).length,
          burgerVisible: burger ? getComputedStyle(burger).display !== 'none' : false,
          navDisplay: siteNav ? getComputedStyle(siteNav).display : null,
          navVisibility: siteNav ? getComputedStyle(siteNav).visibility : null
        };
      });

      const viewportFolder = path.join(outputRoot, viewport.name);
      await mkdir(viewportFolder, { recursive: true });
      const screenshot = path.join(viewportFolder, `${slug(route)}.png`);
      await page.screenshot({ path: screenshot, fullPage: true, animations: 'disabled' });

      let interaction = {};
      if (route === options.routes[0] && viewport.name === 'desktop') {
        const navLabel = options.scope === 'comparisons' ? 'Comparatifs' : 'Marques';
        const navItem = page.locator('.nav-item').filter({ has: page.locator('a.nav-link', { hasText: navLabel }) }).first();
        if (await navItem.count()) {
          await navItem.hover();
          await page.screenshot({ path: path.join(viewportFolder, `${slug(route)}--nav-menu-open.png`), fullPage: false, animations: 'disabled' });
          interaction.desktopSectionMenuVisible = await navItem.locator('.dropdown').evaluate(element => {
            const style = getComputedStyle(element);
            const rect = element.getBoundingClientRect();
            return style.visibility !== 'hidden' && style.opacity !== '0' && rect.width > 0 && rect.height > 0;
          });
          if (options.scope === 'brands') interaction.desktopBrandMenuVisible = interaction.desktopSectionMenuVisible;
        }
      }

      if (route === options.routes[0] && viewport.name === 'mobile') {
        const burger = page.locator('.burger');
        if (await burger.count()) {
          await burger.click();
          await page.waitForTimeout(150);
          interaction.burgerAriaExpanded = await burger.getAttribute('aria-expanded');
          interaction.mobileMenuVisibleAfterClick = await page.locator('.site-nav').evaluate(element => {
            const style = getComputedStyle(element);
            const rect = element.getBoundingClientRect();
            return style.display !== 'none' && style.visibility !== 'hidden' && rect.width > 0 && rect.height > 0;
          });
          await page.screenshot({ path: path.join(viewportFolder, `${slug(route)}--burger-clicked.png`), fullPage: false, animations: 'disabled' });
        }
      }

      const focus = await page.evaluate(() => {
        const target = document.querySelector('a[href], button:not([disabled])');
        if (!target) return null;
        target.focus();
        const style = getComputedStyle(target);
        return { tag: target.tagName, outlineStyle: style.outlineStyle, outlineWidth: style.outlineWidth, boxShadow: style.boxShadow };
      });

      report.pages.push({ route, viewport: viewport.name, httpStatus: response?.status() ?? null, screenshot: path.relative(process.cwd(), screenshot), consoleErrors, pageErrors, focus, interaction, ...measurements });
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
