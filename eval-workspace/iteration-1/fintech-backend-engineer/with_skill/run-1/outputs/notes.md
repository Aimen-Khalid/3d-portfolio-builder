# Build notes: Hamza Siddiqui portfolio ("The Dawn Ride")

## Unattended-run choices (stated at the top, per Step 1)
- User not available: all questions + assumed answers are logged in `questions.md`.
- Built from the user's message only. No résumé, photo, links, quotes, awards or contact details were given, so none appear; nothing was invented.
- Visitors assumed: hiring managers / engineering leaders and conference organisers.
- Sound on by default with a toggle. Light follows the visitor's clock between 05:00 and 08:00, otherwise opens at 6:05 blue hour.
- Artifacts: not published (eval condition). Every place the skill says publish/republish is marked "would publish here" below.

## Inventory (Step 1: 8-12 things only Hamza has)
1. The weekend dawn ride along Sea View, Karachi: the sea wall, the promenade lamps still on before sunrise, the Arabian Sea on one side.
2. The hour itself: dawn on weekends (pre-dawn, blue hour, sunrise, early morning).
3. 14 mechanical keyboards (and counting): keycaps, the thock.
4. "Idempotency at scale", his PyCon Pakistan 2024 talk: press once or ten times, one effect.
5. The 40% cut in p99 latency on Ledgerly's payment API: a tail that got shorter.
6. 2 million accounts moved to a new ledger at Tolly Bank with zero downtime: the flow never stops while the points switch.
7. Three roles as three milestones: Paysphere 2017, Ledgerly 2020, Tolly Bank 2023.
8. 8 years in fintech: a ride measured in years, 2017 to now.
9. Karachi's seafront specifics: sea wall railing with gulls, the beach camel, palms along the road, waves splashing over the wall.
10. Printed things of his world: a payment receipt (with an idempotent transaction ID), road milestones, a conference banner.

## Dealt hand (Step 2)
`node scripts/deal.mjs` -> **seed 3246630383**, three hands:
- **Hand A**: camera *Very close (macro)* · ground *A single line* · movement *Drive or ride* · time *Lights you switch* · look *Paper and card*
- Hand B: camera *Eye level, inside it* · ground *A container* · movement *Handle the whole world* · time *One frozen moment* · look *Clay and plasticine*
- Hand C: camera *High three-quarter, orbiting (common)* · ground *A sheet that unfolds* · movement *Travel a path* · time *Years of their life* · look *Glass and light*
No redraws.

### Idea sentences (with the swap test)
- **A**: "For Hamza, **his weekend dawn ride along Sea View, when the promenade lamps are still on** becomes **one seafront road he rides, the camera low beside his bike, with a lamp that switches on at every stop of his story**." Swap test: put another engineer in it and it breaks (it needs his ride, his seafront, his dawn). PASS.
- **B**: "For Hamza, **his 14-keyboard collection** becomes **a carry case you stand inside and tip, sliding his career keycaps into view**." Swap test: works for any keyboard collector only partially; it is tied to his collection, but the frozen-moment axis is weak. PASS (weaker).
- **C**: "For Hamza, **the ledger he migrated 2 million accounts onto** becomes **a glowing ledger sheet that unfolds year by year as you travel its entries**." Swap test: borderline (any fintech engineer has ledgers), saved only by the migration specifics. PASS (weakest).

### Proposals
1. **The Dawn Ride** (category 4 Scroll/ride-driven story, with a 6 Paper-and-print accent: a paper-cut diorama). Hand A. Pitch: ride Hamza's dawn route along Sea View; every stop on the seafront is a piece of his career, and the promenade lamp at each one clicks on when you find it. Content: 3 roles = 3 roadside milestones; p99 = a billboard whose bar drops 40%; migration = a paper model railway where 2,000,000 accounts switch ledgers while live payments never stop; PyCon talk = a crossing button that changes the light once however often you press it; keyboards = a giant 14-key keyboard; Sea View = the end flag. Light: dawn times (5:40 pre-dawn, 6:05 blue hour, 6:30 sunrise, 7:30 morning). Wow: Sunrise - the paper sun climbs out of the sea, the lamps switch off one by one in a wave, and the camera pulls back from the bike to show eight years on one road. Why: "because you ride Sea View at dawn on weekends". **Recommended & picked.**
2. **The Keyboard Case** (category 5 Tactile playground). Hand B. Stand inside a clay carry case for his keyboards and tip the case to slide keycap-objects (roles, projects, talk) into view; one frozen moment of a keystroke you release. Wow: the case snaps shut and every key thocks at once.
3. **The Ledger Sheet** (category 6 Paper and print, glass accent). Hand C. A glass ledger in the dark that unfolds entry by entry from 2017 to now; a years scrubber rewrites it. Wow: the ledger balances and every entry lights.

(Category spread: ride story / tactile / paper. Recruiter-scan need is met inside proposal 1 by a real nav strip of stops plus a full plain page.)

## Concept sheet (Step 3)
- **World**: The Dawn Ride - Hamza's weekend dawn ride along Sea View, as a paper-cut diorama. **Category**: Scroll/ride-driven story (4) + Paper and print accent (6). **Pitch**: Ride with Hamza along Sea View before sunrise; every stop on the seafront is a chapter of his eight years in fintech, and its lamp clicks on when you find it.
- **Dealt hand**: seed 3246630383, Hand A, no redraw. Idea sentence as above.
- **Composition fingerprint**: see section below.
- **Reskin check vs references** (Desk = overhead/surface/open/day/photoreal; Cards page = eye-level-ish scroll page/stack-rail/open/none/photoreal-tactile; Cozy room = high-orbit/room-surface/orbit-fly/lamps/toy; Cupboard = eye-level/container/open/lamps/photoreal): The Dawn Ride differs from every one on at least 4 of 5 axes (it shares only "lamps" with Cozy room and Cupboard). No earlier builds in this conversation. No desk, cupboard, room, badge rail, basket or prayer-time light. With the name removed, it is still a Karachi seafront dawn ride with a 14-key keyboard, an idempotent crossing button and a ledger switch: only Hamza's.
- **First view**: low, close camera beside a paper-cut cyclist on the Sea View road at blue hour; the paper sea in layers behind the railing, gulls on the rail, the first lamp still dark, the start sign with his name filling the frame. Name + role always in the top-left header.
- **How you move**: you ride. Scroll wheel, drag/swipe, ← → keys or the pedal buttons move the bike along the road; the camera slides from stop to stop. A bottom route strip (real buttons) rides straight to any stop. Click an object to open it; if it's ahead, the bike rides there first.
- **Object -> content map** (every key part of the story gets its own object):
  - Start sign -> name, "senior backend engineer with 8 years in fintech, based in Karachi"
  - Milestone "2017" -> Backend Engineer at Paysphere (2017–2020)
  - Milestone "2020" -> Senior Engineer at Ledgerly (2020–2023)
  - Billboard with two paper bars -> p99 latency cut by 40% at Ledgerly (the "after" bar folds to 60%)
  - Milestone "2023" -> Lead Backend Engineer at Tolly Bank (2023–now)
  - Ledger switch sign + paper model railway -> migration of 2 million accounts, zero downtime (counter to 2,000,000, downtime 0 s, live-payments row never stops)
  - Conference banner + pedestrian crossing button -> PyCon Pakistan 2024, "Idempotency at scale"
  - Giant 14-key keyboard + nameplate -> mechanical keyboards (14 so far)
  - Sea View flag -> cycles along Sea View at dawn on weekends; launches the sunrise
- **Depth on opening**: each sign lifts off its posts toward the camera, settles beside the caption, and turns over on a second click to a kraft back with a printed label (HTML-in-Canvas).
- **Signature wow**: "Sunrise" - the paper sun rises out of the layered sea, light sweeps from blue hour to sunrise, the lamps click off one by one down the road, paper year-pennants rise from every stop, and the camera pulls back from macro to a wide view of the whole 8-year road. "Ride again" puts everything back.
- **Game loop**: "Lamps lit 0 of 8": one promenade lamp per story stop, switched on when its stop is opened. All 8 lit -> reward: a paper ride receipt prints (with a transaction ID that stays the same every time you reprint it - idempotent).
- **Easter eggs (4, all touch-friendly)**: ring the bike bell 3 times quickly (tap the cyclist / press B) -> gulls lift off the railing and circle; tap the sea 5 times -> a Sea View wave crashes over the wall with spray; press all 14 keycaps (tap or type Q-U / A-J) -> the keys hop in a wave with a rising run; press the crossing button 10 times -> an "IDEMPOTENT" stamp lands on the box: 10 requests, 1 effect.
- **Light moods**: 5:40 Pre-dawn (lamps carry the scene), 6:05 Blue hour (default outside dawn hours), 6:30 Sunrise (low sun from the left, long shadows ahead of the rider), 7:30 Morning. One compact dropdown, eased transitions, follows visitor clock 05:00-08:00.
- **Palette**: night navy #1D2C55, sea teal #2F6F7E, paper cream #F3EDE2, kraft #B8925F, sodium-lamp amber #FFB547, sunrise coral #F07B5A.
- **Fonts**: Bricolage Grotesque (display/body), IBM Plex Mono (labels, receipt, counters). Embedded as base64.
- **Sound palette** (procedural Web Audio): freewheel ticks while riding, paper rustle/lift/flip, bike bell, keyboard thock, lamp switch click + hum, crossing-signal beeps, stamp thud, waves and splash, gull squawks, camel grunt, receipt printer, discovery chime, reward fanfare.

## Composition fingerprint
Camera: Very close (macro) - a low camera beside the paper cyclist; big objects fill the frame and it slides from one to the next
Ground: A single line - one seafront road (Sea View) with the story laid out along it
Movement: Drive or ride - you ride the bicycle (scroll, drag/swipe, arrow keys, route strip) from stop to stop
Time: Lights you switch - each story stop's promenade lamp switches on when you find it, over dawn presets (5:40 / 6:05 / 6:30 / 7:30)
Look: Paper and card - die-cut card signs with visible edges, layered paper sea, paper palms, gulls and camel, grain + bump texture

Comparison: differs from The Desk (overhead/surface/open/day/photoreal) on 5 of 5; from the cards page on 4-5; from Cozy room (high-orbit/room/orbit-fly/lamps/toy) on 4 (shares "lamps"); from Cupboard (eye-level/container/open/lamps/photoreal) on 4. No earlier builds in this conversation. PASS (needs 3 of 5).

## Build log ("would publish here" markers, per eval condition 2)
1. Scene roughed in (road, kerb, promenade, sea wall, layered paper sea, sky, cyclist, signs) -> **would publish here** ("Your ride is up; open it and watch it grow").
2. Lighting: dawn presets, sun from the east, lamps, shadows -> **would publish here**.
3. Content on objects: HTML-in-Canvas card faces and kraft backs (SVG foreignObject path, DOM proxy over the held card) -> **would publish here**.
4. Depth on click: lift to the centre, turn over, caption panel / bottom sheet -> **would publish here**.
5. Material effects: p99 bars fold down, ledger railway switches tracks, crossing button presses, keycaps press, palms rustle, lamps wobble -> **would publish here**.
6. Game + secrets: lamps tracker, ride receipt reward, 4 Easter eggs -> **would publish here**.
7. Wow: Sunrise -> **would publish here**.
8. Sound, plain page, mobile layout -> **would publish here**.
9. After wow review rounds -> **would publish here** (final).

Technical notes:
- Three.js 0.160.0 pinned from jsdelivr via importmap; fonts embedded as base64; everything else inline. Single file `index.html` (~220 KB).
- HTML-in-Canvas: every card face and back is real HTML rendered through SVG `<foreignObject>` into a canvas texture (native `drawElementImage` is used if the browser has it... the hook is feature-detected but this build ships the foreignObject path); the real DOM sits as an invisible proxy exactly over the held card, so its text is selectable and readable by screen readers. The ledger counter re-renders live (0 -> 2,000,000) and the receipt re-renders on reprint.
- Material truth: cards are card stock (paper rustle, lift, bump-mapped grain, kraft backs with a printed part number and fold tab, as die-cut diorama pieces really have); the bars are paper that folds down; keycaps travel and thock; the crossing button depresses and beeps; palms rustle; lamp posts wobble and clank; the sea bobs and splashes (spray uses a soft round sprite); the camel nods and grunts. No crumple or ripple was used because nothing here is a sheet of paper held in the hand or a liquid surface in a cup.
- Performance: one renderer; lamp light is a pool of 3 point lights that follow the nearest lamps (constant light count, no shader recompiles); adaptive pixel ratio drops from 2 toward 0.75 if frames are slow; loop pauses when the tab is hidden or the plain page is open.
- Test harness only: SwiftShader rendered ~1 frame/s at 1440x900, so verification used the skill's slowed clock (`__site.pause(true)` + `__site.step()`), a local copy of the same pinned three.module.js (network on the shared box was flaky), and disabled `backdrop-filter` in the test browser only. Inputs were all real Playwright mouse/keyboard/touch events.

## Real-visitor walkthrough log
All with real `page.mouse` / `page.keyboard` / touch input; `__site` was used only to advance the paused clock (and to read state/positions for assertions).

### Desktop 1440x900 (final run; earlier runs found and fixed the failures listed below)
| Step | Result |
|---|---|
| 4 Light dropdown: Pre-dawn / Blue hour / Sunrise / Morning | PASS (x4) |
| 4 Sound toggle off/on | PASS |
| 4 Plain page and back | PASS |
| 3 Drag the road to ride | PASS |
| 9 Mouse wheel rides along the road | PASS |
| Ride to each next stop with ArrowRight (8 stops) | PASS (x8) |
| 1 Hover every story object shows tooltip (9 cards) | PASS (x9) |
| 2 Click every story object: lifts to centre + caption (9) | PASS (x9) |
| 2 Click again: turns over (9) | PASS (x9) |
| 2 Close via button / Escape / click outside (rotated across the 9) | PASS (x9) |
| 5 All 8 lamps lit by real clicks | PASS |
| 5 Reward (ride receipt) appears | PASS (after fix) |
| 5 Reprint gives the same receipt and transaction ID | PASS |
| 4 Tracker menu opens / closes with Escape | PASS |
| 1 Hover lamp, gull, bike, camel, palm, crossing button | PASS (x6) |
| 6 Egg: B x3 rings the bell, gulls fly | PASS (after fix) |
| 6 Egg: tap the sea x5, wave over the wall | PASS (after fix) |
| 6 Egg: press all 14 keys, keys hop in a wave | PASS |
| 6 Egg: crossing button x10, IDEMPOTENT stamp | PASS |
| 7 Sunrise runs (light to sunrise + wide pull-back) | PASS |
| 7 Ride again restores bike position, light, camera, lamps | PASS |
| 10 Console clean (no errors/warnings except SwiftShader's ReadPixels perf notice from the audit) | PASS |

### Mobile 390x844, touch context
| Step | Result |
|---|---|
| Touch swipe rides | PASS |
| Tap route strip, milestone opens as bottom sheet | PASS (after fix) |
| Tap the card, it turns over | PASS |
| Close the sheet (x) | PASS |
| Billboard opens / tap outside closes | PASS |
| Secret on touch: tap the bike 3x | PASS |
| All 14 keys visible at the keyboard stop | PASS (after fix: 11/14 before) |
| Secret on touch: tap all 14 keys | PASS |
| Light control / tracker / sound / plain page | PASS (x4) |
| Sunrise + Ride again restores | PASS |
| No horizontal overflow at 390 | PASS |
| Console clean | PASS |

### Failures found and fixed during verification
1. Every real-time-paced click timed out: SwiftShader ran at <1 fps with `backdrop-filter` + MSAA + 11 point lights. Fixed in the site by pooling lamp lights (3 lights) and adaptive pixel ratio; in the harness by the slowed clock.
2. Clicking outside at (700,140) landed on the card in its held pose, so "close via outside" failed: harness click point moved to a truly empty spot; tooltip no longer shows over a held card.
3. Reward never appeared when the 8th lamp was lit while a card was still held (receipt and card fought for the caption): reward now waits until that card is closed, with a toast saying so.
4. Bell / sea secrets used wall-clock windows; on a slow device the 3 taps could fall outside them. Windows now use the scene clock.
5. Phone: ride-then-open used a setTimeout after arrival, which a slow frame could race; it now runs in the same frame as arrival.
6. Phone: 3 of the 14 keycaps were off-screen at the keyboard stop; the portrait camera now leads further at that stop.
7. Two ledger carriages overlapped after wrap-around (flicker cluster on `cart`): carriages are now evenly spaced on the loop.
8. Kraft backs on short cards (keys, PyCon, ledger) overflowed the card; arched milestone backs had text cut by the arch. Both now use compact layouts; a DOM overflow check over all card faces passes (the IDEMPOTENT stamp was resized to fit).

## Flicker audit (core from SKILL.md, 960x600 drawing buffer; nudge scaled x1.9 for held close-ups, x20 for the wide wow view)
Round 1:
| View | Flagged | Culprits (raycast hits) |
|---|---|---|
| blue-start | 0.0054% | none |
| blue-p99 | 0.0073% | none |
| blue-ledger | 0.1286% | cart×25 **FAIL** |
| blue-pycon | 0.0042% | none |
| blue-keys | 0.0040% | none |
| blue-sea | 0.0064% | none |
| morning-start | 0.0245% | post×2 |
| morning-p99 | 0.0201% | none |
| morning-ledger | 0.2372% | cart×30 **FAIL** |
| morning-pycon | 0.0191% | none |
| morning-keys | 0.0203% | none |
| morning-sea | 0.0243% | railPosts×1 |
| predawn-p23 | 0.0010% | none |
| held-p99 | 0.0148% | card-p99-edge×2, shoe×1 |
| held-p99-back | 0.0061% | shoe×1 |
| held-keys | 0.0017% | none |
| wow-wide | 0.0057% | rail1×1 |

Fix: two carriages shared a position after wrap-around (z-fighting). Re-audit (round 2, after all geometry changes):
| View | Flagged | Culprits |
|---|---|---|
| blue-start | 0.0056% | none |
| blue-p99 | 0.0063% | none |
| blue-ledger | 0.0040% | none |
| blue-pycon | 0.0042% | none |
| blue-keys | 0.0040% | none |
| blue-sea | 0.0064% | none |
| morning-start | 0.0245% | post×2 (silhouette edge) |
| morning-p99 | 0.0187% | none |
| morning-ledger | 0.0438% | none |
| morning-pycon | 0.0187% | none |
| morning-keys | 0.0200% | none |
| morning-sea | 0.0243% | railPosts×1 |
| predawn-p23 | 0.0010% | none |
| held-p99 | 0.0156% | card-p99-edge×2, shoe×1 (edges) |
| held-p99-back | 0.0061% | shoe×1 |
| held-keys | 0.0023% | none |
| wow-wide | 0.0108% | sea4×1, openSea×1, frond×1 |

All views under 0.05%, no surface clusters. Worst: morning-ledger, 0.0438%. Heatmaps in `screens/flicker-*.png`.

## Wow review (Step 6)
Compared my screenshots against `assets/quality-bar/*.png` for craft only (shadow softness, light that falls and changes, surface detail, UI polish). No subagent was available in this run, so the review is my own; I scored conservatively.

### Round 1 (after the first working build)
| Item | Score | Why |
|---|---|---|
| First five seconds | 1 | Strong silhouette at blue hour, but the bottom third was an empty dark verge and the city side was a void |
| Signature moment | 1 | Sunrise worked but read as "the sky turns orange"; the pull-back first went straight up and lost the road |
| Light and depth | 1 | Real shadows and lamps, but flat-ish surfaces next to the crops' textured light |
| Material truth | 2 | Card stock behaves like card; bars fold; keys thock; backs are kraft with part numbers |
| Play | 2 | Everything clickable, 8-lamp game, receipt reward, 4 secrets |
| Personal | 2 | Sea View dawn ride, 14 keys, idempotent crossing button and receipt, ledger points |
| Story (recruiter test) | 2 | Route strip shows all roles/projects; every role, project and the talk has its own object |
| Polish | 1 | Ledger carriages z-fought, card backs overflowed, keyboard cropped on phones, reward collided with an open card |
| Originality | 2 | Fingerprint differs on 4-5 axes from every reference |
| **Total** | **14 / 18** | Below 15: iterate |

Weakest two and fixes: Polish (fixed the ledger overlap, card back layouts, keyboard framing, reward queueing, tooltip over held card) and First five seconds / Signature (added a foreground bougainvillea hedge, a city side with apartment blocks whose windows glow before sunrise, the pull-back now looks down the whole road into the sun, a rotating paper-sun ray fan, and the gulls lift off as the sun clears the horizon).

### Round 2
| Item | Score |
|---|---|
| First five seconds | 2 |
| Signature moment | 2 |
| Light and depth | 1 (shadows and lamp pools are real; no gobo-quality light patches like the crops) |
| Material truth | 2 |
| Play | 2 |
| Personal | 2 |
| Story | 2 |
| Polish | 2 |
| Originality | 2 |
| **Total** | **17 / 18** |

### Round 3 (required extra round on the signature moment)
Added the sun's glitter path across the Arabian Sea during Sunrise (additive strip, its own height above the sea plane, depthWrite off, fixed renderOrder) and widened the ray fan as the sun clears. Re-checked the wow mid/end and Ride again on desktop and phone.
| Item | Score |
|---|---|
| First five seconds | 2 |
| Signature moment | 2 |
| Light and depth | 1 |
| Material truth | 2 |
| Play | 2 |
| Personal | 2 |
| Story | 2 |
| Polish | 2 |
| Originality | 2 |
| **Total** | **17 / 18** |

Still to improve (stopped after 3 rounds): light and depth at the crops' level, meaning soft window-style light patches through the palms onto the promenade, warmer bounce on the card faces at sunrise, and long raking shadows of the railing across the road at 6:30.

## Self-check against SKILL.md
| Item | Status | How confirmed |
|---|---|---|
| Everything interactive | PASS | Walkthrough steps 1-2 (9 cards + lamp, gull, bike, camel, palm, crossing button, keys, sea all respond) |
| Depth when opening | PASS | Cards lift to the centre in an arc, turn over (screens/open-*.png, flip-*.png) |
| Reason to explore + reward | PASS | 8 lamps tracker, reward receipt (screens/reward-receipt.png, reward-reprint.png) |
| One big reversible wow | PASS | Sunrise + Ride again (screens/wow-mid.png, wow-end.png, wow-putback.png; walkthrough step 7) |
| 3+ Easter eggs, work on touch | PASS (4) | Bell (B / tap bike), sea x5 (click/tap), 14 keys (type/tap), crossing x10 (click/tap); mobile walkthrough taps bell + keys; sea and crossing button are tap targets by design |
| Light/mood that changes and means something | PASS | 4 dawn presets of his weekend ride, visitor clock 05:00-08:00 (screens/light-*.png) |
| Sound | PASS | Procedural Web Audio for every action; toggle tested (walkthrough step 4). Audio itself not audible in headless; recipes listed in concept sheet |
| Plain page + WebGL fallback | PASS | screens/plain-page.png; renderer try/catch opens the plain page with a note if WebGL fails (code path read, not triggered in test) |
| Zero flicker | PASS | Flicker audit round 2: all views < 0.05%, worst 0.0438% |
| Real-visitor walkthrough | PASS | Logs above |
| Story spread: one object per role/project/talk | PASS | 3 milestones, billboard, ledger railway + sign, PyCon banner + crossing, keyboard, Sea View flag; route strip names them |
| HTML-in-Canvas on content objects | PASS | All card faces/backs, the receipt, labels via foreignObject; DOM proxy over held card (code + text selectable) |
| Material truth / real backs | PASS | Kraft backs with part number and fold tab (a die-cut diorama piece's real back); no ripples/crumples on wrong materials |
| Format: single self-contained file | PASS | index.html, fonts as data URIs, three.js pinned 0.160.0 from jsdelivr |
| Name + role always visible | PASS | Header pill on every screenshot |
| Captions close via button, Escape, outside | PASS | Walkthrough step 2 rotated all three |
| Text fits on objects | PASS | DOM overflow check over all card faces returns none (after fixes) |
| No overlaps at breakpoints; toasts never cover the mobile sheet | PASS | Screens at 1440 and 390; CSS hides toasts while the sheet is open on phones |
| Springs/easing, reduced motion | PASS | Eased holds/flips/camera; prefers-reduced-motion jumps to end states (code read; not emulated in test) |
| No flicker build rules (offsets, renderOrder, near/far ≤ 2000, depthWrite off, soft sprites, shadow bias) | PASS | near .1 / far 200 (ratio 2000) in ride view, .5/420 wide; decals offset; glows/sprites depthWrite false; spray uses a soft sprite map |
| Voice and accuracy: only facts given, word for word | PASS | Every fact in the site is from his message; the plain page uses his sentences verbatim; no invented numbers, quotes, links or contact |
| Accessibility: keyboard to every section, focus, dialog roles, alt | PASS | Arrow keys + Enter ride/open, route strip buttons, focus outlines, caption role=dialog, canvas aria-label |
| Mobile first-class | PASS | Portrait camera, bottom sheet, compact controls, taps (mobile walkthrough) |
| Performance: DPR ≤ 2, pause when hidden | PASS | setPixelRatio(min(2,dpr)) + adaptive drop; visibilitychange pauses |
| Résumé | NOT INCLUDED | None was provided; offered in the handover message |
| Reskin check | PASS | Fingerprint section |
| Wow review ≥ 15 with an extra signature round | PASS | 14 -> 17 -> 17 |
| Publish/republish to one artifact URL | SKIPPED | Eval condition 2; marked "would publish here" in the build log |
| Netlify deploy | SKIPPED | Eval condition 2; offered in final message |

## Final regression
After the last code change (in-frame arrival callback, compact backs, stamp size): desktop walkthrough re-run in full, 75 PASS / 0 FAIL, console clean; mobile walkthrough re-run in full, 16 PASS / 0 FAIL. The flicker audit was last run after the final geometry change (tree/house rows moved); the later glitter strip is transparent additive with depthWrite off and its own height, and the later changes were HTML/CSS and timing only.
