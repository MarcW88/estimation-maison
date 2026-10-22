#!/usr/bin/env node

import { readFile } from 'node:fs/promises';

const reportPath = process.argv[2] || '.artifacts/design-review/brands/report.json';
const report = JSON.parse(await readFile(reportPath, 'utf8'));
const failures = [];

for (const page of report.pages) {
  const label = `${page.viewport} ${page.route}`;
  if (page.httpStatus !== 200) failures.push(`${label}: HTTP ${page.httpStatus}`);
  if (page.horizontalOverflow) failures.push(`${label}: page-level horizontal overflow`);
  if (page.brokenTocTargets?.length) failures.push(`${label}: broken TOC targets ${page.brokenTocTargets.join(', ')}`);
  if (page.consoleErrors?.length) failures.push(`${label}: console errors`);
  if (page.pageErrors?.length) failures.push(`${label}: page errors`);
  if (page.tables?.some(table => !table.hasExpectedWrapper)) failures.push(`${label}: table without responsive wrapper`);
}

const mobileHub = report.pages.find(page => page.viewport === 'mobile' && page.route === '/marques/');
if (!mobileHub) {
  failures.push('mobile /marques/: missing from report');
} else {
  if (mobileHub.interaction?.burgerAriaExpanded !== 'true') failures.push('mobile /marques/: burger aria-expanded is not true after click');
  if (mobileHub.interaction?.mobileMenuVisibleAfterClick !== true) failures.push('mobile /marques/: menu not visible after burger click');
}

const desktopHub = report.pages.find(page => page.viewport === 'desktop' && page.route === '/marques/');
if (!desktopHub?.interaction?.desktopBrandMenuVisible) failures.push('desktop /marques/: Marques dropdown not visible on hover');

if (failures.length) {
  console.error('Brand visual regression gate failed:');
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log(`Brand visual regression gate passed for ${report.pages.length} page/viewports.`);
