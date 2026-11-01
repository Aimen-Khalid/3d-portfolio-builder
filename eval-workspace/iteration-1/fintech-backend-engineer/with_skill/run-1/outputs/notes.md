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
