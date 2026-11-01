# Daniyal Ahmed portfolio: build notes

**Unattended run.** Choices made without the user (full message log in `questions.md`):
- Portfolio is for Daniyal himself; visitors are hiring managers with ~30 seconds.
- No résumé, links, photo, quotes or insight answers beyond the message, so the site uses only the stated facts and invents none. No contact links or résumé PDF are shown.
- World picked: **The Week Board** (Scrolling page with objects), my recommendation of the three.
- Sound on by default with a toggle; light presets = the three shifts of a restaurant day; delivered as a single `index.html`.

## Dealt hand + seed

`node scripts/deal.mjs` → **seed 2722144452**

- Hand A: through a frame / sphere / open things up / one frozen moment / real materials
- **Hand B (chosen): overhead / grid / zoom into layers / weather / ink and watercolour**
- Hand C: eye level / container / drive or ride / years of their life / glass and light

**Redraw (one axis):** Hand B's *time* axis redrawn from **weather** to **years of their life** (`node scripts/deal.mjs --redraw time --seed 2722144452` offered lamps / years / weather). Reason: weather means nothing in Daniyal's story and cannot hold content, while his whole story is a growth over years (2019 Shiftly → 2022 Carely at 40k → now 310k). Light still changes through separate presets (the three shifts of a restaurant day).

## Inventory (things that belong to Daniyal and no one else)

1. The week: both his products are measured weekly (restaurant shift rotas at Shiftly; *weekly* active users at Carely).
2. The shift rota grid: a week of shifts, Mon to Sun, the core object of the scheduling product he built.
3. 1,200 restaurants using his shift scheduling.
4. Churn cut by 18% at Shiftly.
5. 40k → 310k weekly active users on Carely's teleconsult product.
6. The teleconsult call itself: the product he launched is a phone/video consult.
7. Restaurant kitchen tickets on a rail: the world his first product's customers lived in.
8. Restaurant shift times (opening, lunch rush, close): his Shiftly customers' day.
9. The CSPO certificate (Certified Scrum Product Owner).
10. The years 2019, 2022, now: his two roles' dates.
11. "30 seconds": the time he says hiring managers give him.

(Thin inventory by necessity: the user gave no personal life details, so the world is built from his work, as the skill directs.)

## Idea sentences (Step 2)

- **Hand B (chosen):** For Daniyal, **the week (the unit both his products live in: shift rotas for 1,200 restaurants, then *weekly* active users)** becomes **a rota grid seen from above where every square zooms into the next layer of his story, and a year dial restaffs the board from 2019 to now**.
  Name-swap test: put another PM in the sentence and it breaks; the rota grid only means something because he built shift scheduling, and the weekly tiles only because his headline metric is weekly active users. Passes.
- Hand A: For Daniyal, **the teleconsult screen he launched** becomes **the frame you see the world through: a globe of patients caught mid-call that you release**. Passes (teleconsult is his), proposed second.
- Hand C: For Daniyal, **his six years** become **a glass locker you ride through as the years fill it**. Weak name-swap (anyone has years); proposed third with that caveat.

**Chosen idea sentence:** For Daniyal, the week (shift rotas for 1,200 restaurants, then weekly active users) becomes a rota grid seen from above where every square zooms into the next layer of his story, and a year dial restaffs it from 2019 to now.

## Concept sheet

**World:** The Week Board. **Category:** 8, Scrolling page with objects (accent: Paper and print for the tear-off sheet and tickets). **Pitch:** a readable one-page portfolio whose hero is a lit, ink-and-watercolour rota board of week tiles; every section below carries its own object from his working world.

**Dealt hand:** seed 2722144452, Hand B, time axis redrawn weather → years (reason above).

**What the visitor sees first:** name, role and the three headline numbers as real HTML on the left (desktop) / top (mobile); on the right, the Week Board seen from above under shift light, full of 31 teal week tiles, a live counter "310,000 weekly active users", a year dial and a "Grow 40k → 310k" button.

**Page order (one object and one mechanic per section):**
1. Hero: **the Week Board** (zoom: click a tile and the camera dives into it; the tile lifts and turns over to show what it stands for; year dial restaffs the board for Shiftly 2019–22 / Carely start / Carely now).
2. Carely, Senior PM 2022–now: **a ringing phone with an incoming teleconsult** (answer it: it lifts to you, the screen connects to the role and result; turn it over for its back).
3. Shiftly, PM 2019–2022: **a ticket rail with three kitchen tickets** (role / 1,200 restaurants / churn −18%): slide them along the rail, pull one out, turn it over; a service bell on the pass.
4. Certification: **a CSPO certificate card and a rubber stamp** (press the stamp: it inks on the pad and stamps the card, leaving relief).
5. 30-second summary: **a tear-off pad** whose top sheet holds the whole story (tear it off, take it, copy it).

**Object → content map:**
| Story piece | Object |
|---|---|
| Carely role + teleconsult launch | Phone (section 2) + Week Board tiles (hero) |
| 40k → 310k WAU | Week Board tiles + tower wow moment |
| Shiftly role | Ticket 1 |
| 1,200 restaurants | Ticket 2 + Week Board "2019–22" mode (12 tiles × 100) |
| Churn −18% | Ticket 3 |
| CSPO | Certificate card + stamp |
| Whole career | Tear-off summary sheet |

**Signature wow moment:** "Grow 40k → 310k": the camera swings from overhead to a low three-quarter view; four pale tiles drop into a short "40k start" stack, then all 31 week tiles lift off the rota one by one and clack onto a second stack that rises toward you, a counter ticking 10,000 per tile, until the 310k tower stands nearly eight times taller than the 40k one; the board jolts and a watercolour bloom spreads across the paper. **Put it back** flies every tile home to its square and the camera returns overhead.

**Game loop:** tracker pill "✦ n of 8 found" (fixed in the header): zoom into a week tile; watch 40k grow to 310k; answer the Carely call; pull each of the 3 Shiftly tickets; stamp the CSPO card; tear off the summary. Reward: the middle row of the Week Board turns over to spell T-H-A-N-K-S-! and a rota slip slides in ("Week complete").

**Easter eggs (all work on touch):**
1. Knock five times on the empty board → time-lapse through the three shifts.
2. Ring the service bell three times quickly → "Order up!": every ticket flutters on the rail.
3. Type "ship" (desktop) or press all four brass pins on the board (any device) → every tile hops in a wave across the week.

**Lighting moods:** 07:00 Open (cool, low, from the left), 12:30 Lunch rush (high warm white), 23:00 Close (dark page, moonlit key and a warm pendant lamp over each object). Opens on the visitor's clock. One compact dropdown.

**Palette:** ink #1f2a33, paper #fbf7ee, Carely teal #2f7f7b, Shiftly ochre #d39a3c, stamp vermilion #c8462b, page #f4efe4 (night #1b1e25).
**Fonts:** Fraunces (headings), Inter (body), Caveat (ink handwriting on the board). **Sound palette:** wooden tile clacks, paper slides and tears, a phone buzz, a service bell, a rubber-stamp thud, chimes for finds, all procedural Web Audio.

## Composition fingerprint

Camera: overhead (straight down onto the board, with the wow moment swinging to a low three-quarter view)
Ground: grid (a 7 × 5 weekly rota board; each square holds a week tile)
Movement: zoom (click a square and the camera dives into it, the tile lifts and turns over to reveal the next layer)
Time: years (a year dial restaffs the board: 2019–22 Shiftly, 2022 Carely start, Carely now)
Look: ink and watercolour (watercolour washes and ink outlines on paper under real light)

**Comparison with earlier builds** (references in `versions.md`; nothing else built in this conversation):
- The Desk (overhead / surface / open-lift / day / photoreal): differs on ground, movement, time, look (4 of 5).
- The cards page (eye level / line rail / handle-physics / none / photoreal): differs on camera, ground, movement, look (4+ of 5).
- Cozy room (high-orbit / room / orbit-fly / ? / toy-ish): differs on all 5.
- Cupboard (eye level / container / open / lamps / photoreal): differs on all 5.
Shares the *category* (scrolling page with objects) with the cards page, which is allowed; no reused objects (no badge rail, no card stack, no case-file drawer, no visitor badge printer, no basket payoff). Name-off test: a rota board of weekly tiles, kitchen tickets and a teleconsult phone only make sense for someone who built shift scheduling and grew a weekly-active teleconsult product.
Default check: "overhead camera" is near the desk default, but the ground is a rota grid, not a desk surface, and his story demands it (he built shift scheduling).

## Build log

Would publish here (first viewable state), and republish after each chunk; skipped per eval condition 2.

- Published nothing (eval condition 2). **Would publish here:** after the first viewable state (board + 4 section objects roughed in), then republish after: lighting presets → content on objects → lift/flip → material effects (paper crumple, ticket sway, stamp relief) → game + secrets → wow → sound → plain page + mobile → each review round.
- Libraries: three.js r160 (module + RoundedBoxGeometry + RoomEnvironment) inlined as text and imported via blob URLs; Fraunces / Inter / Caveat woff2 inlined as base64. Single self-contained `index.html` (948 KB). No network requests at runtime.
- One shared WebGLRenderer on a fixed full-screen canvas, scissored into each section's region; an IntersectionObserver wakes or sleeps each section's scene. The loop idles after about 30 still frames and restarts on input, scroll or animation.
- **HTML-in-Canvas:** the phone screen (ringing → connected) and the summary sheet are real HTML rendered into their textures through SVG `foreignObject` with embedded fonts, the documented fallback path (native `drawElementImage` isn't available in this Chromium). The live DOM copy of the summary text sits beside the pad as real HTML, so it stays selectable and copyable; I did not add a DOM proxy laid over the moving objects. Paper crumple (Voronoi folds) on the summary sheet bends the HTML content with it.
- A performance finding from verification: under SwiftShader at 1440x900 with antialiasing and DPR 1, a moving frame took about 2.4 s; the cost was in rendering (the GPU stall on readback), not CSS. I added a DPR governor: if moving frames average over 45 ms, the pixel ratio steps down to 0.5x. I also added test-only URL parameters (`?aa=0&dpr=0.5&maxdt=0.35`) so the real-input walkthrough could finish in reasonable time on software GL. They change only rendering quality and the per-frame time cap, never the input or game code. Screenshots and the flicker audit used the default full quality.

## Real-visitor walkthrough log

Real `page.mouse` / `page.keyboard` / `page.touchscreen` (and CDP touch swipes) only; `__site` was used only to read object screen positions and state, never to act. Run 1 failures are listed, followed by fixes and re-runs.

| Step | Result |
|---|---|
| 1 Hover week tile → tooltip ("Tile 10 of 31 · 10,000 weekly active users") | PASS |
| 1 Hover brass pin → tooltip | PASS |
| 1 Hover phone / stamp / ticket → tooltip + hover lift | PASS (phone logged; stamp hover screenshot `hover-stamp.png`) |
| 2 Click tile → camera dives in, tile lifts, caption | PASS |
| 2 Click "Turn it over" → tile back (rota-tile stamp) | PASS |
| 2 Close via × / Escape | PASS / PASS |
| 2 Close via click outside | **FAIL in run 1** (only clicks inside the stage closed it) → added a document-level outside-click close for every held object → PASS |
| 4 Year dial → Shiftly (12 ochre tiles = 1,200 restaurants) and back | **FAIL in run 1** (timing only: the restaff animation hadn't finished on slow software GL) → wait on state → PASS |
| 4 Light dropdown: Open / Close / Lunch rush | PASS |
| 4 Sound toggle | PASS |
| 4 Plain page and back | PASS |
| 4/9 Every nav link lands on its section | PASS |
| 7 Wow "Grow 40k → 310k" (real click) → 31 tiles stacked, counter 310k | PASS (run 1 timed out on slow software GL, fixed via the test params above) |
| 7 Put it back → board restored exactly | PASS (max tile offset from home 0) |
| 2 Click phone → answers, lifts; click again → turns over; Escape puts it down | PASS |
| 3 Drag ticket sideways along the rail | PASS (x −1.55 → −2.08) |
| 2/5 Pull tickets 1, 2, 3 by click; clip back by clicking outside | PASS ×3 |
| 6 Secret: ring service bell 3x → "Order up!" | PASS |
| 5 Click stamp → inks, stamps the CSPO card | PASS |
| 2 Click card right after stamping → pick up | **FAIL in run 2** (click swallowed while the stamp animated) → click is now queued and runs when the stamp finishes → PASS |
| 2 Card turn over + put down via button | PASS |
| 5 Click pad → sheet tears off, held | PASS |
| 4 Copy summary | PASS (clipboard contains the summary) |
| Hover paper crumple on held sheet | PASS (`hover-paper-crumple.png`) |
| 5 Game to the end with real clicks → "All 8 found" + THANKS! reward | PASS (`reward.png`) |
| 4 Tracker menu opens / closes on Escape | PASS / PASS |
| 6 Secret: knock 5x on the board → service-day time-lapse | **FAIL in run 2** (my click landed on a tile, not empty board) → re-run with clicks on an empty rota cell → PASS (`egg-knock.png`) |
| 6 Secret: type "ship" → tiles wave across the week | PASS (`egg-ship-wave.png`) |
| 9 Mouse-wheel scroll top to bottom: live scenes and contexts | **Logged as FAIL** by my strict check (≤2 live scenes) at one point: 3 scenes (shiftly, cspo, summary) at scrollY 2250, all in or near the viewport with the 120 px margin; WebGL contexts = 1 throughout; render loop only draws visible regions. Acceptable by the skill's rule (never all scenes; one context); left as is. |
| 10 Console clean (desktop) | PASS (no errors) |
| 8 Touch 390x844: tap tile → zoom + bottom-sheet caption | PASS |
| 8 Touch secret: tap all four brass pins → wave | PASS |
| 8 Touch: wow + Put it back | PASS |
| 8 Touch: tracker + light dropdown | PASS |
| 9 Touch swipe over a 3D object scrolls the page (not trapped) | PASS (scrollY 0 → 285) |
| 8 Touch: tap phone → answered | PASS |
| 8 Touch: tap ticket → pulled | PASS |
| 10 Console clean (mobile) | PASS |
| Re-run after wow-review change (cap tile, lighting) | Wow + Put it back PASS, knock PASS, no errors |

All steps pass after the fixes.

## Flicker audit (per view, % of pixels flagged; pass < 0.05%)

Run inside the page with the loop paused: 14 renders with sub-mm camera nudges into an offscreen target, counting pixel reversals and raycasting culprits. The nudge was scaled ×0.5 for close-up and held views. Heatmaps: `screens/flicker-*.png`.

| View | % flagged | Culprit meshes |
|---|---|---|
| hero overview, Lunch rush | 0.0006 | none |
| hero overview, Close (night) | 0.0006 | none |
| Carely phone, day / night | 0 / 0 | none |
| Shiftly rail, day / night | 0.0012 / 0.0012 | none |
| CSPO, day / night | 0 / 0 | none |
| Summary pad, day / night | 0 / 0 | none |
| hero tile zoom (close-up) | 0.0013 | none |
| hero tile flipped | 0.0002 | none |
| hero wow tower | 0.0004 | none |
| phone held | 0 | none |
| ticket held | 0.0021 | none |
| CSPO card held | 0 | none |
| summary sheet held | 0 | none |

**Worst: 0.0021% (held ticket); all views pass, no clusters.** Measures that prevented flicker: every tile, pin, sheet and stamp sits 4–6 mm above its surface; the shadow-catcher plane has its own height and renderOrder −1; the phone's camera module and lenses are offset from the back; the summary sheet floats 5 mm over the pad; near/far = 1/80 (ratio 80); shadow bias and normalBias are set.

## Wow review

Compared screenshots against the quality-bar crops for craft only (I took no objects, layout or palette from them). No subagent was available, so I did the review myself.

**Round 1** (after the first full build):
| Item | Score | Note |
|---|---|---|
| First five seconds | 2 | Name + three numbers + a lit watercolour board, readable at once |
| Signature moment | 1 | Tiles flew into one tower, but the 40k start had no visual partner, so "40k → 310k" didn't read as growth |
| Light and depth | 1 | Shadows too faint and soft next to the crops' soft-shadow crop; Open preset barely differed from Lunch |
| Material truth | 1 | Tile and card backs rendered upside down when turned (box bottom-face UVs) |
| Play | 2 | 8 finds, reward, 3 secrets, all objects interactive |
| Personal | 2 | Rota grid + weekly tiles + kitchen tickets only fit him |
| Story (recruiter test) | 2 | Roles, dates and both results visible without clicking |
| Polish | 1 | Board header text overlapped the title; "one tile =" label clipped; the 3D legend pill overlapped the board |
| Originality | 2 | Fingerprint differs from every reference on ≥4 of 5 axes |
| **Total** | **14 / 18** | under 15 → iterate |

Weakest two and fixes: (a) signature moment: added a separate "40k · 2022, the start" stack of four pale tiles that pops up first, so the 310k tower rises beside it at nearly 8x the height, with a counter and a watercolour bloom; (b) polish + material: fitted the header text, moved the legend into the HTML under the board, fixed the label clip, rotated back textures 180° so backs read upright, replaced glyph icons with SVG icons.

**Round 2:**
| Item | Score |
|---|---|
| First five seconds | 2 |
| Signature moment | 2 (two stacks side by side tell 40k → 310k at a glance; screen-recordable) |
| Light and depth | 1 (better, still lighter shadows than the crops) |
| Material truth | 2 |
| Play | 2 |
| Personal | 2 |
| Story | 2 |
| Polish | 2 (flicker audit pass, no overlaps at 1440 / 390) |
| Originality | 2 |
| **Total** | **17 / 18** |

**Round 3 (required extra round on the signature moment + light):** the top tile of the finished tower now turns to a "310k · now" cap tile; shadows strengthened (opacity .24 → .36, PCF radius); Open became a low warm side light and Lunch a higher, harder one, so the presets read differently; on mobile, toasts moved to the bottom so they never cover the counter. Re-ran wow + Put it back, the knock secret and the full flicker audit after these changes: all pass.
| Item | Score |
|---|---|
| First five seconds | 2 |
| Signature moment | 2 |
| Light and depth | 1 (real light, shadows and presets now change mood clearly, but it's still not at the crops' level of raymarched softness, dust and steam) |
| Material truth | 2 |
| Play | 2 |
| Personal | 2 |
| Story | 2 |
| Polish | 2 |
| Originality | 2 |
| **Total** | **17 / 18** |

Stopped after three rounds. Still worth improving: richer light (a patch of window light across the board at Open, a warm lamp pool at Close), and the board would gain from slight paper curl at its corners.

## Self-check against the skill

**Every site needs**
- Everything interactive: board tiles, pins, empty board (knock), phone, tickets (pull + drag), bell, card, stamp, ink pad, pad/sheet. Confirmed: walkthrough steps 1–3.
- Depth when opening: camera dives into a tile and it lifts and turns; the phone, ticket and card rise to the centre and turn over; the sheet peels and tears. Confirmed: `hero-tile-zoom/flipped`, `carely-back`, `shiftly-ticket2-back`, `cspo-card-back`, `summary-torn`.
- A reason to explore + reward: tracker pill "n of 8 found" with checklist; THANKS! reward. Confirmed: walkthrough step 5, `reward.png`, `tracker-menu.png`.
- One big reversible wow: Grow 40k → 310k / Put it back, restored exactly (offset 0). Confirmed: step 7.
- At least 3 Easter eggs working on touch: knock 5x (works on touch by tapping), bell 3x (tap), "ship" / four brass pins (pins on touch). Confirmed: steps 6 and 8.
- Light that changes and means something: three restaurant shifts, starting from the visitor's clock. Confirmed: `light-*.png`.
- Sound: procedural Web Audio with a toggle, remembered per visitor. Confirmed: step 4 (toggle). Audio output itself can't be heard headless.
- Plain-page fallback + WebGL-failure fallback: confirmed `plain-page.png`. The no-WebGL branch hides the stages and shows a note; it is coded but I didn't force-test it.
- Zero flicker: audit worst 0.0021%.

**Story spread:** Carely role and its result → phone + board; Shiftly role → ticket 1; 1,200 restaurants → ticket 2 + year dial; churn −18% → ticket 3; CSPO → certificate + stamp; whole career → tear-off sheet. Headlines are also real HTML in the first screen. Confirmed: `hero-desktop.png`, `fullpage-desktop.png`.

**Scrolling page with objects:** the hero is the signature object; each section has its own object and mechanic (dive/zoom, answer a call, pull/slide tickets, stamp, tear); text is real HTML; one palette, type system and light across sections; one renderer, scenes paused off-screen; vertical swipes scroll (touch-action pan-y; drags are horizontal only); the tracker stays fixed in the header; the nav is real. Confirmed: step 9, `fullpage-desktop.png`.

**Build rules:** single self-contained file ✓ (948 KB, no external requests). Name and role always visible (fixed header) ✓. Captions close with ×, Escape or outside click ✓. Object backs are real (tile back = rota-tile ink stamp; phone back = aluminium + camera module; ticket back = blank thermal paper; card back = embossed CSPO; sheet back = plain paper) ✓. Texture text fitted (fitText/wrap) ✓; textures redrawn after fonts load (await `document.fonts.load` before painting) ✓. No overlaps at 1440 and 390 ✓ (screens). Springs and easing, no linear motion ✓. prefers-reduced-motion: short or instant moves, no crumple or shake ✓ (coded; not screenshot-tested). DPR capped at 2, loop pauses when hidden or idle ✓.

**Voice and accuracy:** only the user's facts. Role lines use his exact phrasing ("launched our teleconsult product and grew weekly active users from 40k to 310k"; "built shift scheduling used by 1,200 restaurants and cut churn by 18%"). The tile split (four "start" tiles = 40k, one tile = 10,000; 12 tiles × 100 restaurants) is a visual scale for his own numbers, labelled on the board, not a new fact. No invented quotes, links, employers or dates.

**Accessibility:** each stage is focusable with an aria-label and its own keys (arrows/Enter/Esc on the board; Enter/B/1-3/S keys on the sections); captions use role=dialog and move focus to their button; visible focus ring; the tracker menu has aria-expanded; the light menu is a keyboard-navigable listbox. Confirmed by code review; keyboard Enter/Escape exercised in the walkthrough.

**Mobile:** portrait layout (stats in a 3-up row, board below, bottom-sheet captions, compact icon controls). Confirmed: `hero-mobile.png`, `*-mobile.png`, step 8.

**Reskin check / fingerprint:** differs from every reference on ≥4 of 5 axes; no reused objects or payoff. Confirmed: fingerprint section above.

**Not done / honest gaps:**
- Résumé PDF: none supplied; I would offer to generate one (not done, unattended).
- Contact links: none supplied, so the page has no contact call-to-action. This is the biggest gap for a recruiter site.
- No companion: none fits his story, and he gave no pets.
- Audio was not listened to (headless).
- The reduced-motion and no-WebGL fallbacks are coded but weren't screenshot-verified.
