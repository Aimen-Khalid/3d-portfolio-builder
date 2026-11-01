# Notes: Daniyal Ahmed portfolio (baseline, no skill)

## What I built
A single-file, one-page résumé site (`index.html`, only external dependency is Google Fonts) designed around a 30-second skim:

- **Hero (first screen):** name, role badge, a big serif headline, a one-sentence summary with the two headline numbers in bold, and chips for "6 yrs", industry, and the CSPO certification. On the right, a "metric card" styled like a product dashboard: Carely teleconsult WAU counts up from 40k to 310k while an orange growth line draws itself (7.75x badge). That chart is the "special" moment: a PM's résumé shown as the kind of chart PMs live in. The curve is labelled as illustrative because only the endpoints are real.
- **Scan strip:** four numbers in a row (40k→310k, 1,200, −18%, 6 yrs) with a short label each.
- **Experience:** one card per role: dates/company/title | bullets taken from his message | a highlighted "win" number.
- **What I bring:** Launch / Scale / Retain, each tied to one fact he gave.
- **Contact block** with placeholder Email / LinkedIn / Résumé buttons.
- **"30s skim" ring** in the top bar: a small progress ring that counts down "30s left" to "skim done" as you scroll. A nod to his "30 seconds" brief.
- Light and dark themes (prefers-color-scheme), scroll-reveal, honours prefers-reduced-motion (chart shows its final state immediately), responsive down to 390px.

Only facts from his message are used; no invented employers, numbers or contact details (see questions.md).

## How I checked it
- Python Playwright + Chromium: screenshots at 1440x900 and 390x844 (`screens/`), full-page shots and a dark-mode shot in `work/`.
- Confirmed no console/page errors, no horizontal scroll (scrollWidth equals viewport width at both sizes), the WAU counter ends at 310 and the skim ring reaches "skim done" at the bottom.
- Looked at every screenshot: caught and fixed a broken chart caption from a bad sed substitution; checked the sticky bar and section layout in the full-page shot.

## Composition fingerprint
Camera: none; a flat, straight-on 2D web page with no 3D view.
Ground: warm off-white paper background with a centered 1160px column; two-column hero (text left, dashboard-style chart card right), then stacked rounded cards.
Movement: ordinary vertical scrolling with a sticky top bar and anchor links; no free exploration.
Time: on load the WAU line draws and the counter climbs 40k→310k once; sections fade up on scroll; the skim ring fills as you scroll. Nothing changes otherwise.
Look: clean editorial/dashboard look: Fraunces serif headlines, Inter body, mono labels, cream paper cards with thin borders and soft shadows, orange accent and green "growth" highlights.
