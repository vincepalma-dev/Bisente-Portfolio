// Captures the landing page of each live project for the homepage showcase.
// Landing pages only: no logging in, no internal screens.
// Run: node scripts/capture-shots.mjs
import { mkdir } from 'node:fs/promises';
import { chromium } from 'playwright';

// `dismiss` lists buttons to click (cookie banners: always the essential-only choice),
// `escape` closes a promo modal.
const SITES = {
  'bizmaker-erp': { url: 'https://bizmaker-payroll.vercel.app/', dismiss: ['Reject Non-Essential'] },
  'omma-platform': { url: 'https://omma-art.vercel.app/', dismiss: ['Essential only'] },
  tlcph: { url: 'https://tlcph.online/', escape: true },
};

const outDir = 'public/images/projects/shots';
await mkdir(outDir, { recursive: true });

const browser = await chromium.launch();
let failed = 0;
try {
  for (const [id, site] of Object.entries(SITES)) {
    let page;
    try {
      page = await browser.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
      await page.goto(site.url, { waitUntil: 'networkidle', timeout: 60_000 });
      await page.waitForTimeout(4000); // let entrance animations, toasts and popups appear
      for (const name of site.dismiss ?? []) {
        await page.getByRole('button', { name }).first().click({ timeout: 5000 }).catch(() => console.warn(`${id}: no "${name}" button`));
      }
      if (site.escape) await page.keyboard.press('Escape');
      await page.waitForTimeout(6000); // let toasts and close animations finish
      await page.screenshot({ path: `${outDir}/${id}.jpg`, type: 'jpeg', quality: 80 });
      console.log(`${id}: ${site.url} -> ${outDir}/${id}.jpg`);
    } catch (err) {
      failed++;
      console.error(`${id}: failed (${site.url}): ${err.message}`); // keep the old screenshot, move on
    } finally {
      await page?.close();
    }
  }
} finally {
  await browser.close();
}
if (failed) process.exitCode = 1;
