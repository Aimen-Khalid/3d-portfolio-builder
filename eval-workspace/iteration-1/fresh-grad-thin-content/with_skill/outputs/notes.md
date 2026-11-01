# Notes: Hira Baig portfolio, "21 Points"

## Unattended choices (stated up front)
User unavailable. Every question the skill would have asked is in `questions.md` with the answer I assumed. Content is limited to exactly what Hira gave: BS CS, FAST Lahore, 2026; a 3-month React internship at Brightloom (small startup); a final-year project, a sign-language-to-text app built with MediaPipe; no photo, no awards, no links. Nothing invented. The one assumption (ASL handshapes for the fingerspelling) is flagged in the handover.

## Inventory (Step 1)
Belongs to Hira and no one else:
1. The **21 hand landmarks** MediaPipe tracks: the backbone of her final-year project.
2. The **hand itself**, signs read as shapes: the thing her app watches.
3. **Sign → text**: the core transformation of her FYP (a handshape becomes a letter).
4. **FAST Lahore, class of 2026**: the degree, year and place.
5. **Brightloom**: small startup, the name of her one internship.
6. **3 months**: the internship's length, a countable unit (three pages).
7. **React**: what she did there.
8. **Her name, H-I-R-A**: four letters, fingerspellable.
9. **The webcam's lighting problem**: hand tracking has to work under daylight, tube light, a desk lamp, screen glow (the light of a student lab/room).
10. **"I just graduated"**: the frozen moment between finishing and starting.

(Thin by design. Most items come from the project itself, which is the richest thing she has.)

## Dealt hand + seed (Step 2)
`node scripts/deal.mjs` → **seed 2401736525**

- **Hand A:** camera Straight down · ground Disc/floating island (common default) · movement Step by step · time One frozen moment · look Clay and plasticine
- **Hand B:** camera Eye level · ground Sphere · movement Open things up · time Seasons · look Textile
- **Hand C:** camera Very close (macro) · ground Sheet that unfolds · movement Travel a path · time Years of their life · look Ink and watercolour

### Idea sentences (test: swap in another person)
- **A:** "For Hira, **the 21 MediaPipe landmarks of a hand caught mid-sign** become **stepping stones on a round clay board, with the whole scene frozen until you release it**."
  Swap test: another person's site would have no reason for a hand, 21 landmarks or a sign. **Passes.**
- **B:** "For Hira, **the world her app has to read signs in** becomes **a felt globe you turn, with a season on each side**." Swap test: a weak link (seasons have nothing to do with her). **Fails. Dropped.**
- **C:** "For Hira, **the four years at FAST Lahore** become **an unfolding ink map you travel stop by stop, with a year scrubber**." Swap test: any graduate could use it unchanged, and she gave almost no year-by-year content. **Fails as personal. Kept only as a fallback.**

**Default check (Hand A's disc is a common default).** The round board is justified by her inventory: it's the **tray a clay hand model lies on**, the circular camera frame a webcam demo is read in. It is not an island town: there are no buildings round the edge, no ring road, no plaza. The hand fills the centre and the objects sit at its fingertips, laid out by MediaPipe's own topology (wrist → 5 fingertips), not round a rim.

### Proposals (what I would have sent)
1. **"21 Points" (recommended).** *Tactile playground, with a miniature board-game accent* (Hand A). A clay hand lies frozen mid-sign on a round clay board. Its 21 teal landmark beads are strung into MediaPipe's skeleton, and each fingertip has a path of clay stepping stones leading to one part of her story. A little clay pawn hops along the landmarks. **Wow:** "Release it" unfreezes the moment and the hand fingerspells H-I-R-A while letter tiles pop up, which is her project running in clay. **Why her:** the site *is* her FYP; everything she has hangs off the fingers.
2. **"The Reading Room Globe."** *Elemental/miniature* (Hand B). Rejected at the idea-sentence test.
3. **"The Scrolling Sign Page."** *Scrolling page with objects* (offered because recruiters scan). A readable page whose hero is the clay hand and whose sections each get their own object: the laptop, the calendar, the diploma. It uses the same pieces in a recruiter-first layout.
Then: "Would you like a different category, a mix, or something specific of your own?" → assumed: **#1**.

## Concept sheet (Step 3)
- **World:** "21 Points": a clay hand on a clay board. **Category:** Tactile playground (clay squish, physics crumbs, springy fingers) + **accent:** miniature board game (pawn on stepping stones). **Pitch:** *Her final-year project, made of clay: 21 landmarks, and every fingertip leads to a piece of her story.*
- **Hand:** seed 2401736525, Hand A, no redraws. **Idea sentence:** as above.
- **First view:** straight down on a lit clay board. The coral clay hand sits in the middle, frozen mid-sign (index and middle straight; thumb, ring and pinky half-curled), with crumbs and the pawn hanging in mid-air. A mustard "❚❚ Frozen mid-sign · Release it" pill sits below. Her name and degree are bottom-left.
- **Moving around:** click/tap any object (it lifts to the centre and a caption opens); click again to turn it over or open it further. The pawn walks the landmark graph (arrow keys, click a bead, or drag it onto a stone).
- **Object → content map** (one visible object per story piece):
  - Wrist → **Nameplate**: Hira Baig · BS CS · FAST Lahore · 2026. *Back:* rougher underside with "H.B." scratched in and a thumbprint, "pressed by hand · 2026".
  - Thumb → **Diploma scroll** tied with a teal ribbon: unrolls into the degree sheet (HTML-in-canvas). The paper crumples under the cursor (Voronoi folds). *Back:* plain paper back.
  - Index → **Laptop** (FYP: sign language to text, MediaPipe). Opens on a hinge; the screen draws the *live* landmarks of the clay hand and shows DETECTED / TEXT.
  - Middle → **Desk calendar** (Brightloom internship): 3 month pages (Brightloom / React / 3 months) flipped on the spiral. *Page backs:* lined paper.
  - Ring → **Atom** (React, MediaPipe: what I've worked with). Spins; drag to spin.
  - Pinky → **Slate** ("Sign ← text"): type a word (real `<input>` DOM proxy over an HTML-in-canvas face) and the hand fingerspells it.
- **Signature wow:** *Release the frozen moment.* The crumbs fall with gravity and bounce, the pawn lands, the hand relaxes, then fingerspells **H-I-R-A** while clay letter tiles pop up over the board, the beads pulse, and a toast reads "Sign → text. That's my final year project, in clay." **Put it back** re-freezes everything (crumbs fly back to their mid-air spots and the tiles vanish).
- **Game:** "✦ n of 9 pressed": nameplate read, nameplate turned over, diploma unrolled, FYP picked up, laptop opened, 3 months flipped, atom spun, hand signed a word, frozen moment released. **Reward:** the hand signs ASL "I love you", the tiles spell THANKS, the beads ripple with light and a thank-you note appears. The beads keep glowing on later visits.
- **Easter eggs (4, all touch-reachable):**
  1. Type **"hira"** → the hand waves (on touch: tap the five fingertip beads).
  2. **Poke the palm 5×** → fist bump with a screen shake.
  3. **Tap the pawn 3×** → backflip.
  4. **Leave it alone 22 s** → the fingers drum on the board.
- **Lighting moods:** the four kinds of light hand tracking has to survive: ☀ Window daylight, ▭ Tube light, ◐ Desk lamp (warm spotlight, dark room), ▣ Screen glow (blue room lit by the laptop). Eased 1.3 s transitions. Opens on the visitor's clock (day 6–17, lamp 17–21, screen at night).
- **Palette:** cream clay #efe4d2 · coral #e0785f / hand #e48a70 · teal #2c8a85 · navy #22375a · mustard #e3b04a.
- **Fonts:** Caveat Brush (hand-pressed headings, tiles), Newsreader (body). Both embedded as base64.
- **Sound palette:** clay squish (low-passed thud), pawn hop/land, paper unroll, card flip, hinge creak, marimba pentatonic for letters (each signed letter plays a note), chime/fanfare for finds. Toggle remembered.

## Composition fingerprint
Camera: Straight down (near-overhead perspective with slight pointer parallax)
Ground: A disc (a round clay board the hand lies on; no rim buildings, objects at the fingertips)
Movement: Step by step (a clay pawn hops landmark to landmark and along stepping stones to each object)
Time: One frozen moment (the scene is caught mid-sign with crumbs and pawn in mid-air; Release / Put it back)
Look: Clay and plasticine (lumpy hand-pressed geometry, fingerprint bump maps, tool drags)

**Reskin check.** Compared with the four reference builds (desk flat-lay, cards scrolling page, cozy room, cupboard), and with nothing else built in this conversation: the closest is the Desk (also overhead), but it differs on ground (disc board vs. walnut desk surface), movement (pawn steps vs. lift-from-desk), time (frozen moment vs. prayer-time day cycle) and look (clay vs. photoreal). **That's 4 of 5 axes different.** It differs from the cards page, room and cupboard on all 5. No reference objects are reused (no badge, basket, letter, lattice, chai, drawer, cat, lanyard or kind-words stack). With the name removed it is still unmistakably a MediaPipe sign-language project's portfolio.

## Build notes
- One self-contained `index.html` (~265 KB). Three.js r160 and RoundedBoxGeometry come from jsDelivr (pinned via importmap). Fonts are base64. All textures are procedural canvas.
- Physical: real Three.js scene, ACES tone mapping, PCF soft shadows (bias −0.0004, normalBias 0.03), hemisphere fill, a spotlight for the lamp preset, a point light from the laptop screen. Clay geometry is noise-displaced, with procedural fingerprint/lump bump maps.
- **HTML-in-Canvas:** the diploma sheet and the slate face are live HTML rendered via SVG `foreignObject` into canvas textures, with base64 fonts embedded in the SVG. The slate has a real `<input>` DOM proxy, matrix-transformed every frame over the slate face, so typing, focus and screen readers hit real DOM, with a blinking caret drawn into the texture. There is no native `drawElementImage` path (not available in this Chromium), so I used the documented fallback.
- Material truth: paper crumples (diploma only); clay squishes and springs (all clay objects, the hand, the pawn); calendar pages flip on the spiral; the laptop lid hinges; the atom spins. Backs: a rough nameplate underside with thumbprint; plain paper on the diploma back and calendar page backs.
- No-flicker measures: tags, stones and the ring torus sit above the board top (+0.035 to +0.05), never coplanar. The screen is offset −0.012 from the lid face and the slate face +0.012 above the frame. Camera near/far ratio ~2.2 (near ≈ H·0.25, far ≈ H·2.2). Crumbs are meshes, not point sprites. No per-frame visibility toggling.
- Accessibility: hidden-until-focused object nav buttons (Tab reaches every object and Release), visible focus rings, `role=dialog` caption, `aria-expanded` tracker menu, aria-live toasts, a plain page with all content, and a WebGL-failure fallback that opens the plain page. `prefers-reduced-motion` gives short moves and no crumple.
- Mobile: portrait-specific object positions and camera fit, bottom-sheet captions (44 dvh), compact `n/9` tracker, tap instead of hover, toasts placed above the sheet.
- Performance: DPR capped at 2, the loop pauses when the tab is hidden or the plain page is open, the screen canvas redraws at ~8 Hz only while the lid is open, and the simulation is substepped (max 1/30 s) so slow devices stay in sync.
- No résumé was given, so nothing is embedded. I'd offer to generate one in the handover.
- **Would publish here** (Step 4, first viewable state; republished after each chunk: objects → light → content → depth → effects → game → wow → sound → mobile). Skipped per eval rules.

## Fixes found while screenshot-looping (Step 4/5)
- First pass: fingers curled *into* the board (wrong rotation sign). The wow and every sign looked broken. Fixed the sign and added automatic hand lift proportional to curl so curled fingers clear the board.
- Hand too small and the hero crowded; scaled the hand ×1.16, moved objects inside the groove ring, and enlarged the tags ×1.35.
- Held objects were too large at the centre (the calendar covered half the screen). Capped the hold scale and moved the caption to an auto-height panel.
- Letter tiles appeared under the hand. Moved them to float over the board at y = TOP + 2.3, scaled for portrait.
- The Screen-glow preset was too dark to read. Raised its hemisphere fill.
- **Walkthrough found a real bug:** clicking an object while the scene was frozen queued a pawn walk that never ran, leaving the pawn path stuck. Fixed: walks are ignored while frozen.
- **Walkthrough found:** the idle-drum secret started a sequence that blocked clicks for 5.5 s. Changed it to a non-blocking overlay animation.
- Slow devices: the simulation is now substepped so the springs and sequences finish on time at low fps.
