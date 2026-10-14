const { chromium } = require('playwright');
const path = require('path');
const HEADER = process.env.REPORT_HEADER || '亞洲室內裝修設計市場研究報告 V1 ｜ 璞石集團 ｜ 2026-10-09';
const CHROME = process.env.CHROME_PATH || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';
(async () => {
  const browser = await chromium.launch({ executablePath: CHROME });
  const page = await browser.newPage();
  page.setDefaultTimeout(600000);
  await page.goto('file://' + path.resolve('report2.html'), { waitUntil: 'load', timeout: 600000 });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({
    path: 'report.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true,
    margin: { top: '16mm', bottom: '16mm', left: '15mm', right: '15mm' },
    displayHeaderFooter: true,
    headerTemplate: '<div style="font-size:7pt;width:100%;text-align:center;color:#888;font-family:sans-serif;">' + HEADER + '</div>',
    footerTemplate: '<div style="font-size:7pt;width:100%;text-align:center;color:#888;font-family:sans-serif;"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
    outline: true, timeout: 600000,
  });
  await browser.close();
  console.log('pdf done');
})().catch(e => { console.error('ERR', e.message); process.exit(1); });
