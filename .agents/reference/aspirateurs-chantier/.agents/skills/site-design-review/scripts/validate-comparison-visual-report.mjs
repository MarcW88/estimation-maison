#!/usr/bin/env node

import { readFile } from 'node:fs/promises';

const reportPath = process.argv[2] || '.artifacts/design-review/comparisons/report.json';
const report = JSON.parse(await readFile(reportPath, 'utf8'));
const failures = [];
const ARTICLE_ROUTES = report.routes.filter(route => route !== '/comparatifs/');

for (const page of report.pages) {
  const label = `${page.viewport} ${page.route}`;
  if (page.httpStatus !== 200) failures.push(`${label}: HTTP ${page.httpStatus}`);
  if (page.horizontalOverflow) failures.push(`${label}: page-level horizontal overflow`);
  if (page.brokenTocTargets?.length) failures.push(`${label}: broken TOC targets ${page.brokenTocTargets.join(', ')}`);
  if (page.consoleErrors?.length) failures.push(`${label}: console errors`);
  if (page.pageErrors?.length) failures.push(`${label}: page errors`);
  if (page.tables?.some(table => !table.hasExpectedWrapper)) failures.push(`${label}: table without responsive wrapper`);

  // Comparison workflow v2 makes the intent-specific decision module optional.
  // Zero or one module is valid; duplicated modules remain a visual regression.
  if (ARTICLE_ROUTES.includes(page.route) && page.decisionModuleCount > 1) failures.push(`${label}: duplicate intent-specific decision modules`);

  const outlinePx = Number.parseFloat(page.focus?.outlineWidth || '0');
  if (page.focus && (!Number.isFinite(outlinePx) || outlinePx < 2)) failures.push(`${label}: focus outline is not visibly reinforced`);

  if (page.viewport === 'mobile' && ARTICLE_ROUTES.includes(page.route)) {
    if (page.tocBeforeArticle !== true) failures.push(`${label}: TOC is not before article on mobile`);
    if (page.mobileHandoffCount !== 1) failures.push(`${label}: expected one mobile handoff before long-form content`);
  }
}

const mobileHub = report.pages.find(page => page.viewport === 'mobile' && page.route === '/comparatifs/');
if (!mobileHub) {
  failures.push('mobile /comparatifs/: missing from report');
} else {
  if (mobileHub.interaction?.burgerAriaExpanded !== 'true') failures.push('mobile /comparatifs/: burger aria-expanded is not true after click');
  if (mobileHub.interaction?.mobileMenuVisibleAfterClick !== true) failures.push('mobile /comparatifs/: menu not visible after burger click');
}

const desktopHub = report.pages.find(page => page.viewport === 'desktop' && page.route === '/comparatifs/');
if (!desktopHub?.interaction?.desktopSectionMenuVisible) failures.push('desktop /comparatifs/: Comparatifs dropdown not visible on hover');

if (failures.length) {
  console.error('Comparison visual regression gate failed:');
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log(`Comparison visual regression gate passed for ${report.pages.length} page/viewports.`);
