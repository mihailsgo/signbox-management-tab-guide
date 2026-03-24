import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const USER = process.env.SIGNBOX_USER;
const PASS = process.env.SIGNBOX_PASS;

if (!USER || !PASS) {
  console.error('Missing SIGNBOX_USER or SIGNBOX_PASS environment variables.');
  process.exit(1);
}

const outDir = path.resolve('docs/images/management/raw');
fs.mkdirSync(outDir, { recursive: true });

const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));

const clickByText = async (page, textCandidates) => {
  for (const text of textCandidates) {
    const el = page.getByRole('link', { name: text }).first();
    if ((await el.count()) > 0) {
      await el.click({ timeout: 7000 });
      return true;
    }
  }
  return false;
};

const shot = async (page, name) => {
  await page.screenshot({
    path: path.join(outDir, name),
    fullPage: true,
  });
};

const main = async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1720, height: 980 },
  });
  const page = await context.newPage();

  try {
    await page.goto('https://signbox.trustlynx.com/', {
      waitUntil: 'domcontentloaded',
      timeout: 120000,
    });
    await sleep(2000);
    await shot(page, '01-login-page.png');

    await page.locator('input[type="text"], input[name="username"], input[type="email"]').first().fill(USER);
    await page.locator('input[type="password"], input[name="password"]').first().fill(PASS);
    await page.locator('button[type="submit"], input[type="submit"]').first().click();

    await page.waitForLoadState('networkidle', { timeout: 120000 });
    await sleep(2500);
    await shot(page, '02-post-login-home.png');

    const openedManagement = await clickByText(page, ['Management', 'management']);
    if (!openedManagement) {
      await page.getByText('Management').first().click();
    }

    await page.waitForLoadState('networkidle', { timeout: 120000 });
    await sleep(1800);
    await shot(page, '03-management-overview.png');
    await shot(page, '04-document-profiles-list.png');

    const firstProfile = page.locator('table tbody tr td a, tbody tr td:first-child, .text-primary.font-semibold').first();
    await firstProfile.click({ timeout: 10000 });
    await page.waitForLoadState('networkidle', { timeout: 120000 });
    await sleep(1600);
    await shot(page, '05-document-profiles-detail.png');
    await shot(page, '06-document-profiles-edit.png');

    await page.goto('https://signbox.trustlynx.com/management/doc-profiles', {
      waitUntil: 'networkidle',
      timeout: 120000,
    });
    await sleep(1300);
    await page.getByText('Create new profile').first().click({ timeout: 15000 });
    await page.waitForLoadState('networkidle', { timeout: 120000 });
    await sleep(1500);
    await shot(page, '07-document-profiles-create-form.png');

    await page.getByRole('link', { name: 'Document attributes' }).first().click();
    await page.waitForLoadState('networkidle', { timeout: 120000 });
    await sleep(1500);
    await shot(page, '08-document-attributes-list.png');

    await page.getByText('Create new attribute').first().click({ timeout: 15000 });
    await sleep(1200);
    await shot(page, '09-document-attributes-create-form.png');

    console.log('Management raw screenshots captured successfully.');
  } finally {
    await browser.close();
  }
};

main().catch(error => {
  console.error(error);
  process.exit(1);
});
