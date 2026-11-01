# Hamza Siddiqui portfolio: notes

## What I built
A single self-contained `index.html` (no build step; Google Fonts are the only external request) in which the portfolio is a **mechanical keyboard on a desk, in front of a window looking out over Sea View, Karachi**.

- **Keyboard as navigation.** The board is a full 60%-style board drawn in CSS 3D (tilted with perspective). Eight keys glow: **A**bout, **W**ork, **L**atency, **M**igrate, **T**alk, **K**eebs, **R**ide, **C**ontact. Click them or type the letter on a real keyboard. Every keypress plays a short synthesized click (WebAudio, no audio files), and the non-hot keys depress and click too, so it's satisfying to just type on.
- **Content prints as receipts.** A thermal printer sits on the desk; each section feeds out as a receipt with a timestamp and a fixed "idempotency key" per section. The fintech theme runs all the way through.
- **Idempotency as a running joke that's also a demo.** Pressing the same key again does *not* reprint: a toast says the key was replayed, and the "duplicates prevented" counter goes up. The Talk receipt ("Idempotency at scale", PyCon Pakistan 2024) has a `POST /charge Rs 450` button. The first press creates a charge, retries return `200 replayed` with the same charge id, and the Charges count stays at 1.
- **Project receipts animate their numbers:** a before/after bar for the 40% p99 cut at Ledgerly, and a counter to 2,000,000 accounts with a ZERO DOWNTIME stamp for the Tolly Bank ledger migration.
- **Keebs:** 14 keycap tiles pop in. **Work:** three line items totalling "8 YRS FINTECH".
- **The window runs on real Karachi time (PKT, UTC+5).** The sky, sun position and sea colour follow the actual hour. On weekend mornings around dawn a cyclist rides along the promenade and the clock says Hamza is out riding. The Ride receipt has a "Fast-forward to Saturday dawn" button so every visitor can see it.
- **Progress:** a tally (receipts printed / duplicates prevented / keys found x/8), and found keys get a check mark.
- **Mobile (<900px):** the full board collapses to a 4x2 macro pad of the eight hot keys. The receipt prints above the pad, and the name hides while a receipt is open.
- Accessibility: hot keys are real focusable buttons with aria-labels, Esc closes, the receipt region is `aria-live`, and `prefers-reduced-motion` turns off the animation.
- Only facts Hamza supplied are used. Contact links are placeholders (see questions.md).

## How I checked it
- Python Playwright + Chromium, one browser at a time (`work/shot.py`). Desktop at 1440x900 and mobile at 390x844 (touch, isMobile). It opens every section in turn (keyboard on desktop, taps on mobile), clicks the charge button 3 times, and asserts the log shows 1 create + 2 replays. It also checks `scrollWidth` equals the viewport width (no horizontal scroll) and collects console/page errors (none).
- Screenshots of every receipt in both viewports are in `work/` and I reviewed them by eye.
- Bugs found and fixed along the way: (1) on mobile the receipt covered the pad, so I moved it to print above the pad with a capped height. (2) The macro-pad row leaked onto the desktop board, so it's now hidden on desktop. (3) The name and receipt were offset by the window height twice. (4) Clicks on hot keys sometimes landed on the row behind them, because the pressed-key translate moved the button out from under the pointer under perspective. Keys now fire on `pointerdown`, with `click` kept for keyboard activation.
- Hero screenshots use `?hour=6.4&dow=6` (Saturday dawn) so the cyclist shows. Without the parameter the page uses live Karachi time.

## Composition fingerprint
Camera: Fixed, front-on view from slightly above, looking down at a perspective-tilted keyboard on a desk, with a window strip across the top.
Ground: Wood-grain desk with a dark desk mat and a CSS-3D 60% keyboard in the centre, a thermal printer at the right, and a window onto Sea View filling the top ~38%.
Movement: The visitor doesn't travel. They press glowing keys (click, tap or type letters), and each section prints as a receipt from the printer. Mobile uses a 4x2 macro pad.
Time: The sky, sun and sea follow live Karachi time, and a cyclist rides the promenade only on weekend dawns (with a fast-forward button). Receipts carry live timestamps.
Look: Warm cream and gray keycaps with amber and teal accents, flat CSS gradients with chunky drop-shadow key depth, thermal-paper receipts in monospace, and a dusk-gradient sea window.
