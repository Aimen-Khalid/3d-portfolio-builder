---
name: "playful-portfolio-builder"
description: "Build an interactive, physical-feeling portfolio website that people play with instead of just read: a full-screen world (a lit desk, a walk-in space, a miniature world, a book...) or a scrolling page where the hero and every section carry their own real 3D object. Use when someone wants a playful, explorable, wow-factor portfolio rather than a flat, templated site."
---

# Playful Portfolio Builder

Build a portfolio that people *play with* instead of read: a physical-feeling world, either one full-screen scene or a scrolling page of lit 3D objects, where every object holds a piece of the person's story, with real light, sound, a game to complete, hidden secrets and a big payoff moment. Anyone can use this skill: the person gives their own story and content, and you design and build a world that could only be theirs.

The goal: every visitor goes "wow" in the first five seconds and keeps exploring for five minutes.

## The philosophy: raise the bar, never restrict

This skill exists to raise the quality of the sites it generates, never to restrict you. Everything in it (examples, screenshots, code, rules) is a **floor, not a ceiling**.

- **Stay free to invent** worlds, mechanics, effects and payoffs that appear nowhere in this skill. If you can see a better idea for this person, do it.
- **Borrow techniques, never identities.** Never copy a reference build's world, objects, palette, layout or payoff for someone else.
- **If a rule blocks a clearly better idea,** keep the rule's intent (quality, sense, delight, accessibility) and go with the better idea.
- **Defaults vs. the bar.** Specific mechanics, numbers, UI placements and libraries in this file are proven defaults that save time, not requirements. What is never optional is the bar: real light and depth, the person's story easy to find, play worth exploring, effects that make sense, and a site that works for a real visitor.
- **A portfolio first.** The play exists to reveal the person. Every key part of their story (each role, major project, award, talk, degree) gets its own object, place or chapter, and every main interaction leads to something about them. Delight that buries the content has failed.
- **Material truth.** Every effect must make sense for its material (paper crumples, tea ripples, jelly wobbles, glass clinks), and every object's back must look like that object's real back.
- **Every site needs:** everything interactive; depth when you open something; a reason to keep exploring, with a reward; one big reversible wow moment; at least 3 Easter eggs that also work on touch; light or mood that changes; sound; a plain-page fallback; and **zero flicker** (no z-fighting, no popping transparency, no shimmering surfaces), proven by the flicker audit in Step 5.
- **It must work for a real visitor.** Before handover, walk through the whole site the way a visitor would, with real mouse, keyboard and touch input (Step 5). A site that only works through debug shortcuts is broken.
- **The wow review is required:** after building, screenshot the site, score it on the 9-item rubric, iterate until it passes, then do at least one extra round on the signature moment.

## References (read the right file at the right time)

Long code and examples live in reference files so this file stays lean. Read only what the current step needs.

| File | Read it when |
|---|---|
| `references/versions.md` | After the person picks a world (Step 3), or when stuck on making something feel physical. **Never in Step 2** while proposing worlds. |
| `references/engine-lighting.md` | Building a lit scene from a fixed camera (flat-lay, wall, shelf, board): albedo + height maps, G-buffer, lighting pass, light presets. Also for light-preset ideas in any world. |
| `references/html-in-canvas.md` | Any content that lives on an object (pages, letters, cards, screens, forms): native `drawElementImage`, SVG `foreignObject` fallback, DOM proxy. |
| `references/material-effects.md` | Before adding any hover/touch effect: the material-truth rule, paper crumple (Voronoi folds), liquid ripples, other material ideas. |
| `references/page-curl.md` | Anything with pages. |
| `references/lift-and-flip.md` | Building depth on click: rise to the centre, turn over, open containers (2D and 3D). |
| `references/sound-kit.md` | Adding sound: Web Audio engine and tuned recipes. |
| `references/game-tracker.md` | The tracker, checklist, secrets, reward and the reversible wow moment. |
| `assets/quality-bar/*.png` | **Only during the wow review** (see below). |

**The quality-bar crops** in `assets/quality-bar/` are close-up details from the main reference build: soft shadows under objects, a sunlight patch through a lattice, steam over a hot drink, paper crumpling under the cursor, a page mid-curl, an object held at the centre and mid-turn, liquid rippling, the tracker dropdown, sunset light on a detail. Load them **only during the wow review**, to compare the quality of your light, detail and polish against them. **Never look at them while choosing the concept or designing the world**: they are deliberately crops, not full pages, so they set a bar for craft without suggesting a layout, palette or set of objects.

## Step 1 - Get to know the person

This is a conversation, not a form.

- **Ask the who-they-are and content questions ONE per message.** Never batch them, and never send an AskUserQuestion call with more than one question. Wait, react briefly, then ask the next question, shaped by the answer.
- **The insight questions are the exception:** they go out together as one optional list (see below), because most people only have good answers to a few of them.
- Use AskUserQuestion (single question) only for clear choices; ask open questions in plain text.
- **Do NOT ask what metaphor, concept, theme or category they want.** That is your job, and comes in Step 2.
- If they attach a résumé or paste LinkedIn early, read it first and skip questions it answers.

Work through these roughly in order, skipping anything known and following interesting threads:

**Who they are**
1. Who is this portfolio for - you, or someone else?
2. What do you do, and where are you in your career?
3. Who should visit this site, and what should they do after?

**Their content** - collect everything the site will show:
4. Your résumé / CV or LinkedIn (attach or paste).
5. Your journey: the moments that changed things for you.
6. Projects you're proudest of and what came out of them (push gently for numbers).
7. Awards, recognition, things people have said about you (exact name, role, company for every quote; can real names be shown?).
8. A photo or portrait? Links?

**Content check (do this once the content is in).** Look at what they gave you and tell them briefly, in one short message:
- what you have and how you'll use it;
- what else would make the site richer, each as an optional "if you have X, send it and I'll do Y" (e.g. "if you have a photo, it can go on your ID badge"; "if you have quotes from colleagues, they become a card of kind words"; "numbers for that project would make its case file land harder");
- and that **it's completely fine if they don't**: you'll build a great site from whatever they've provided.
Never block on missing content. Design around what exists, and leave out (rather than invent) anything they didn't give.

**Insight questions (one optional list)** - what makes the world personal. Send them together in a single message, as a list the person picks from, introduced with something like: "Answer any that apply and skip the rest, or just tell me anything about yourself you'd like the site to feel like."
- What do you do when you're not working? Hobbies, collections, rituals?
- Objects you keep or collect?
- Three words friends or teammates would use for you?
- A story behind your career people always ask about?
- Pets, characters, companions?
- A time of day, season or kind of light that feels like you?
- A place where you feel most like yourself?

Every one is optional, including the place. Never come back to a question they skipped, and never push for a place or setting. If they answer none, build the world from their content and work instead.

Then ask, as its own question: **Is there anything that must NOT appear on the site?**

Summarise what you learned in a few lines before moving on.

If the user is unattended, make sensible choices, state them at the top, and proceed.

## Step 2 - Suggest tailored worlds, each in a category

Only now propose concepts. Do not read `references/versions.md` or the quality-bar crops yet.

**Separate the world from the category.** The *world* is what the site is (their desk in their city, a darkroom, a grandmother's kitchen). The *category* is the broad mode it's built in. Categories are broad on purpose, with lots of variety inside each; never treat a category as one fixed object.

**Categories**

1. **Lit flat-lay** - any scene seen from above under real, changing light: a desk, a picnic, a kitchen counter, a workbench, a vanity, a travel map table.
2. **Walk-in spaces** - any 3D place you explore: a room, a studio, a café, a library, a greenhouse, a train carriage, a spaceship, a cupboard.
3. **Miniature worlds** - tiny scenes you look down into: an island, a town, a planet, a board game, a snow globe. Each building or landmark is a project.
4. **Scroll-driven stories** - scrolling drives one continuous story: a product being made, a river journey, day turning to night, a rocket launch, a hero object transforming.
5. **Tactile playground** - physics and squish: jelly, balloons, magnets, pinball, things on strings, badges on a rail.
6. **Paper and print** - books in every form plus scrapbooks, zines, passports, comics, letters, postcards. Real page curls are required.
7. **Elemental worlds** - built from a medium rather than objects: underwater, night sky and constellations, clouds, deep space.
8. **Scrolling page with objects** - a readable scrolling site (nav, sections, real HTML text) where the hero holds the signature 3D piece and every section has its own interactive 3D object made for that content: a stack of cards to flip through for kind words, a drawer of files for projects, a shelf of trophies for awards, a printer that makes the visitor a badge for contact. Unlike a scroll-driven story, each section is its own object rather than one story that transforms. It suits people whose visitors (recruiters, clients) want to scan fast, and anyone who says they want something special but still easy to read. Read "Scrolling page with objects" under Step 4.

These are starting points, not a closed list. If a person needs a mode that isn't here, invent it.

How to propose:
- Suggest **2-3 worlds built from what they told you**, each labelled with its category. Give each a short name, a one-line pitch, how their content maps to objects, the lighting idea, the wow moment, and *why it fits them* ("because you said you collect film cameras...").
- Spread the proposals across categories rather than offering three versions of one scene. When the person's visitors need to scan quickly (recruiters, clients) or there is a lot of content, make one of the proposals a scrolling page with objects.
- Then ask, as its own question: **"Would you like a different category, a mix, or something specific of your own?"**
- **Mixing:** usually one main category with one accent works best (e.g. a walk-in space with jelly objects, a flat-lay with a curling book); more tends to muddy the experience, so only go further when the idea clearly holds together.
- Do not default to the reference builds' worlds (a desk, a cupboard, a room, a badge rail) unless they genuinely fit this person, and even then make the world unmistakably theirs.

Once they pick, ask a few follow-ups one at a time: sound feel (on by default with a toggle), the lighting/time-of-day idea, where it will live.

## Step 3 - Concept sheet (confirm before building)

Now read `references/versions.md` to understand the bar (techniques only, never identities).

**Reskin check, before building.** Sharing a category or a technique with a reference build is fine and expected: a lit surface seen from above, window light, objects that lift and turn over, a game tracker. What isn't fine is reusing a reference's identity: its specific objects, its arrangement of items, or its wow moment with new labels on top. The test: take the person's name off the site. Could it still only belong to them? If yes, it passes, however familiar the camera angle is. If it could belong to anyone, or it reads as a reference build with new labels, make it theirs before building.

Then write a short sheet and get a yes:
- World + category (+ accent) + one-line pitch
- What the visitor sees first, and how they move around (for a scrolling page: the hero object, then each section in order with its object)
- Object → content map: one visible object per key part of the story (each role, major project, award, talk, degree). A book, folder or drawer can hold extra detail, but the headlines are easy to see and reach (from the opening view, or early in a scroll story).
- The signature wow moment (the payoff)
- The game loop: the list of things to find (mostly the story pieces themselves) and the reward
- 3+ Easter eggs (each working on touch)
- Lighting moods (e.g. times of day), palette (4-6 colours), fonts, sound palette

## Step 4 - Build

### Build in the open: a live artifact from the start

The person should watch their site come to life, not wait for a finished file.

- **Publish early.** As soon as there is a first viewable state (the scene with its surface, light and objects roughed in, even before interactions work), publish it as an artifact and tell the person in one line that they can open it and watch it grow.
- **Republish after every chunk of work** to the **same artifact URL** (never a new one): e.g. objects drawn → lighting and shadows → content on the objects → depth on click → material effects → game and secrets → wow moment → sound → plain page and mobile. After each republish, send one short line saying what's new ("Lighting is in, try the time-of-day dropdown"). Keep it brief; don't narrate every step.
- Only publish states that load without errors. If a chunk breaks something, fix it before republishing.

### It must feel physical

- **Never flat.** Every site has real light, real shadows, depth, and materials you could touch. No flat illustration, no CSS-transform fake depth, no layered parallax PNGs pretending to be a scene.
- Proven ways to get there (use any, combine them, or find another that reaches the same bar):
  - **Real 3D** with Three.js / WebGL meshes, perspective camera, lights and shadows (walk-in spaces, miniature worlds, elemental worlds).
  - **A lit scene**: objects drawn in code as albedo + height (+ roughness/metal) maps, composited in a G-buffer and lit by a real lighting pass. Read `references/engine-lighting.md`.
  - **Custom shaders**: raymarched or signed-distance scenes, particles, fluid or cloth simulations, when they suit the world better.
- Objects drawn in code (canvas/SVG/procedural) at high resolution. No stock clip-art.
- **Real-3D surfaces need material.** Hero objects and large surfaces get texture and variation (procedural canvas textures for wood grain, fabric, fur, paper, metal; roughness and normal variation), never flat untextured primitives next to each other.
- **Real-3D toolbox (defaults, not limits):** geometry from Three.js primitives (rounded boxes, cylinders, lathe, extrude), custom BufferGeometry or procedural meshes, in whatever style fits the world; soft key light with shadows, hemisphere fill, warm practical lights; tone mapping and sRGB output; OrbitControls-style damped drag with clamped angles; clicking flies the camera to the object and back; raycast hover and click with a tooltip naming each object; text on meshes via canvas textures. Check clipping: notes sit on boards, doors stay visible, hollow furniture is hollow, labels aren't cut off.
- HTML is for overlays (header, small pill controls, captions, the plain page) *and* for HTML-in-Canvas content that lives on objects (`references/html-in-canvas.md`).

### The experience layer (every site, every category)

0. **The story is spread across the world.** Each role, major project, award, talk and degree gets its own object, place or chapter, easy to find and quick to open. Never pack the whole career into one container; a hiring manager should be able to scan the world (or the first scroll) and see the shape of the person's work.
1. **Everything interactive, and everything makes sense.** Nothing is just decoration. Things drag, lift, flip, open and make sound, and every reaction is what that object would really do (`references/material-effects.md`).
2. **Depth when you open something.** Opening an object should feel physical: it lifts toward you and turns over, the camera flies in, it unfolds or unpacks. Envelopes open, boxes unpack, books curl. Lift-to-centre-and-turn-over is a proven default (`references/lift-and-flip.md`, `references/page-curl.md`); use whatever suits the object and the world.
3. **A reason to keep exploring, with a reward.** The proven default is a visible tracker ("✦ 3 of 10 found") with a checklist, a chime and toast per discovery, and a personal reward for finding everything, with progress remembered per visitor (`references/game-tracker.md`). Any mechanic that suits the world works as well (stamps in a passport, stars lit in a sky, pages filled in a scrapbook), as long as progress is visible and finishing it pays off. **The things to find are mostly the story pieces**, so finishing the game means the visitor has seen the whole career. Pure-fun finds belong in the Easter eggs, not the main list.
4. **One big wow moment.** A payoff sequence tied to the person, always reversible ("Put it back").
5. **At least three Easter eggs**, personal and hidden, listed as cryptic hints under "Secrets", each also working on touch devices.
6. **Light or mood that changes, and means something.** Presets that mean something to the person (their prayer times, golden hour in their city, seasons, a studio's lamps, depth underwater), with eased transitions. Defaults that work well: one compact control rather than a row of buttons, and starting from the visitor's own clock when the light is time-based.
7. **Sound.** Procedural Web Audio for every action, a visible toggle, started on first gesture (`references/sound-kit.md`).
8. **Companions (when they fit).** A cat, dog, robot or plant that reacts: pet it, it gets startled during big events, it causes mischief the visitor fixes. Keep it charming (no growing in size, no black speech boxes); it faces the way it moves and passes in front of/behind objects correctly.
9. **A plain page.** An accessible, readable fallback with all the content, plus a WebGL-failure fallback.

### Scrolling page with objects

When the world is a scrolling page (category 8, or any mix that scrolls through sections), everything above still applies, section by section. What changes:

- **The hero is the signature.** The first screen carries the biggest, best-lit, most interactive object, with the person's name and role as real HTML beside it. It must earn the "wow in five seconds" on its own.
- **One object per section, each different.** Every section gets its own 3D object built for its content, with its own interaction (flip through, pull out, spin, stack, print). Neighbouring sections never reuse the same object or mechanic. A plain text block between two objects is fine; a section with no object of its own is not.
- **Text stays real HTML.** Headings, captions and body copy sit beside or over the canvas as DOM, so the page reads and scans without touching anything. The objects hold the depth: open a file to read the full case, flip a card to see who said it.
- **The page has one look.** One palette, one type system, one lighting language across every section's scene, so it reads as one world rather than a set of demos. Light can still change across the page (morning at the top, night at the footer) as long as it moves smoothly with the scroll or the light control.
- **Several scenes, one budget.** Browsers cap live WebGL contexts (often around 8-16) and every scene costs battery. Prefer one shared renderer drawing each section's scene into its own region (scissor/viewport), or one renderer per section that is created when the section nears the viewport and paused when it leaves (IntersectionObserver). Never run every scene's loop at once.
- **Nothing hijacks the scroll.** Dragging an object must not trap the page: use horizontal drags or a clear handle for objects, let vertical swipes scroll on touch, and drive card stacks and carousels with explicit buttons, keys and index state.
- **The game and the wow moment span the page.** The tracker stays visible as the visitor scrolls (a small fixed pill), finds come from every section, and the wow moment can gather objects from the whole page into one place, then Put it back returns each to its own section.
- **Navigation is real.** A plain nav with anchors to each section, so a visitor can jump straight to projects.

### HTML-in-Canvas (make it a signature)

Render real HTML content into the scene so it is lit, shadowed and distorted like a physical surface, while staying real DOM for selection, typing, links and screen readers. Then go beyond static text with effects true to the surface's material. Read `references/html-in-canvas.md` and `references/material-effects.md`.

Use it on at least one object that carries real content (a letter, a page, a card, a screen, a form, a visitor badge) whenever the world has one. Drawing every piece of text as a flat canvas texture is the easy path and misses the signature; if you truly can't use it, say why in your notes.

### Using inspiration the person shares

People will share references (Instagram posts, X posts, sites). **They are inspiration, not templates.**
- **Pick and choose.** Take one or two ideas that fit this person and leave the rest.
- Extract the *technique* or the *feeling*; never reproduce a reference literally.
- Techniques worth knowing: procedural lighting over code-drawn objects (albedo + height maps, one strong sun, soft shadows, warm grain); live DOM drawn into canvas/WebGL and distorted; one signature motion per site that gets most of the effort; soft-body "jelly" objects; 3D books with real page curls; scroll-driven stories where one hero object transforms.
- **The screenshot loop:** build, screenshot, look critically, fix, repeat. Never hand over something you haven't looked at.

### Build rules

**Format**
- A single self-contained HTML file: inline CSS/JS, fonts and images as data URIs, pinned CDN versions if a library is used. Easy to publish as an artifact or drop on any static host.
- The scene is the site: a full-screen canvas (100vw x 100dvh) for a single world, a full-bleed scroll for scroll-driven stories, or a scrolling page of sections each with its own 3D object. Keep the person's name and role always visible (on a scrolling page, in the hero and a small fixed header). A layout that works well: small glass controls top-right (light, sound, plain page, links to other versions) and the tracker top-left; design the UI to suit the world.

**Objects and content**
- Details live on the objects (flip the badge, open the letter, curl the page). Any caption or panel closes with a button, Escape or clicking outside.
- **Every face must make sense.** When an object turns over, its back is what that object's back really looks like, with any extra content in a believable form. Never write random handwriting on a phone or glass.
- Text drawn into textures must fit: measure and shrink or wrap, never overflow an object's edge. Redraw textures after fonts load.
- Check overlaps at every breakpoint: objects must not collide with each other at rest. On mobile, toasts and hints must never cover a caption sheet, and nothing important may be cropped at the bottom edge.

**Motion**
- Springs and easing, never linear. Weight, arcs, settle. Lifted objects cast longer shadows.
- Carousels and rolodexes: drive them with explicit index state and clicks/keys, not scroll-position math.
- During any sequence, make sure no other per-frame code fights the animation.
- `prefers-reduced-motion`: short fades instead of big moves; no distortions.

**No flicker (build it out, then prove it in Step 5)**
Flicker is the fastest way to make a polished world feel broken, and it gets worse up close (first-person or zoomed views). Build so it can't happen:
- **Never put two surfaces in the same place.** Anything laid on a face (signs, decals, windows, doors, posters, labels, rugs, sand in a box, water in a basin, road markings) sits clearly in front of it: offset along the face's normal by at least 1-2% of the object's size (e.g. `mesh.translateZ(.014)` after rotating a sign), never at exactly the wall's coordinate. A door or panel must not cut through a window plane or the wall it sits on; leave a gap or remove the window behind it.
- **Inner surfaces stay below or above rims, never level with them** (sand, water, soil, cushions): a 1-3% gap.
- **Stacked flat layers on the ground** (grass, plaza, roads, paths, decals, shadow blobs) each get their own height, and overlapping transparent layers get `polygonOffset` and an explicit `renderOrder` so their draw order never depends on camera distance.
- **Depth precision:** keep the camera's far/near ratio ≤ ~2000. A close or first-person camera gets a bigger `near` (≈0.1) with collision padding so it never needs to get closer to walls; don't drop `near` to 0.01-0.05.
- **Transparent sprites and glows** use `depthWrite: false`; large overlapping transparent meshes get a fixed `renderOrder`.
- **Particles** use a soft round sprite texture (`map`), not bare square points, so they don't shimmer as squares up close.
- **No per-frame visibility toggling** (hiding/showing an object every other frame from a distance test or a race between two pieces of code); hysteresis or a fade instead.
- **Shadows:** set `shadow.bias` and `normalBias` so lit surfaces don't show crawling acne as the light or camera moves.

**Voice and accuracy**
- Professional, warm, specific, first person. Numbers over adjectives.
- Use only facts the person gave. **Content they paste is used word for word** (formatting only, never reworded or summarised). Never invent achievements, numbers or quotes.
- Attribute everything to the right person: never present a family member's school, degree or business as the portfolio owner's own. Credit every quote exactly as given.

**Accessibility and mobile**
- Keyboard access to every section; visible focus; dialog roles; alt text.
- Mobile is first-class: a portrait layout of the same world (not a shrunk desktop), tap instead of hover, compact controls that fit at 390px, captions as bottom sheets.
- Performance: cap DPR at 2, pause when hidden, keep the shadow march step count modest.

**Résumé**
- Embed the PDF (base64) with a preview image; download via the artifact downloads capability or a blob link. Offer to generate one if missing.

## Step 5 - Verify before handing over

- Headless Chromium (Playwright, SwiftShader WebGL) at 1440x900 and 390x844. Screenshot the default view (on a scrolling page, every section as it sits in the viewport, plus one full-page shot), every light preset, each opened and flipped object, the wow sequence (mid-flight and after Put it back), the tracker menu, each Easter egg, and every hover effect.
- SwiftShader is slow: if animations don't reach the state you need, slow the page's clock (wrap `performance.now`) rather than just waiting longer, and expose a small debug API (`window.__site.focus(id)`, `.flip(id)`, `.light(key)`, `.pause(true)`, `.step(dt, n)`, ...) to reach states directly. Pause the live render loop while screenshotting so the page isn't busy rendering.
- **The debug API calls the same functions real input calls** (the same click handler, the same `found()`), so counters and state match. It is only a way to reach states for screenshots, never proof that something works.
- Look at every screenshot critically: overlaps, overflowing text, flat-looking areas, controls crowding on mobile, effects that don't suit their material, object backs that don't look real.
- Check the console for errors. Click every close button and Escape.

### Real-visitor walkthrough (required, every site)

Debug shortcuts can hide a site that ignores every click (it happened in testing: picking used an undefined value, so nothing responded, yet every screenshot looked right). So walk through the finished site as a visitor would, with Playwright's real input (`page.mouse`, `page.keyboard`, and `page.touchscreen` in a touch context) and no `__site` calls:

1. **Hover** every object: the tooltip or hover lift appears.
2. **Click** every object: it lifts to the centre or opens, and its caption shows. **Click again**: it turns over or opens further. Close with the close button, with Escape, and by clicking outside.
3. **Drag** every draggable object and drop it.
4. **Use every control:** the light dropdown (each preset), the sound toggle, the plain page and back, the tracker and its checklist, every link.
5. **Play the game to the end** with real clicks only: the tracker counts each find, and the reward appears. Screenshot the reward.
6. **Trigger every Easter egg** by its real input (keys on desktop, taps on touch) and screenshot each one.
7. **Run the wow moment** and **Put it back**; the scene is restored exactly.
8. **Repeat on a 390x844 touch context** with taps: at least one object of each kind, the controls, one secret and the wow moment.
9. **On a scrolling page:** scroll from top to bottom with the mouse wheel and with touch swipes. Each section's object wakes up as it arrives and pauses after it leaves (log the number of live render loops and WebGL contexts at each section), dragging an object never traps the page scroll, every nav link lands on its section, and the tracker stays reachable the whole way down.
10. Watch the console the whole time.

Log each step with pass or fail in your notes. Fix every failure and walk through again until all steps pass.

### Self-check against this skill (required)

Finally, go back through this file and check the site against it, item by item: every point under "Every site needs", the story spread (one object per key part of the story), the experience layer, the build rules (format, objects and content, motion, no flicker, voice and accuracy, accessibility and mobile) and the reskin check. Write each item in your notes with how you confirmed it (a walkthrough step, a screenshot, an audit number). Anything unconfirmed is not done: fix it or tell the person plainly what is missing.

### Flicker audit (required, every site)

Screenshots can't show flicker, so audit for it directly with the core below inside `page.evaluate`. It freezes the scene's clock, then renders the same view many times while nudging the camera by sub-millimetre steps. Smooth motion changes a pixel in one direction; **z-fighting and transparent-sort popping make a pixel flip back and forth.** It flags pixels that reverse direction three or more times, names the meshes under them with a raycast, and saves a red heatmap per view. Fix those meshes and re-run until clean.

- Run it on: the default overview in day and night light (on a scrolling page, every section's scene), every close-up or flown-to view, and (if the site has a walk or first-person mode) at least six spots in that mode, including next to every building with signs, doors, windows or inner surfaces.
- For Three.js sites, expose `window.__site` with `pause(bool)`, `step(dt, n)`, `light(key)` and `_three()` returning `{ renderer, scene, camera, THREE }` (plus `walk(bool)` and `player`/`walk` state for walk modes).
- **Scale the nudge with distance.** The nudge in the code suits overview distances. For close-ups and held objects, scale it to about 0.0005 x the camera's distance to the target, or text and edges register as parallax rather than flicker.
- **Pass:** under 0.05% of pixels flagged in every view and no named mesh with a cluster of hits. A few scattered pixels on silhouette edges are anti-aliasing, not flicker. Any cluster on a surface (a sign, a door, a box top, a decal) is a failure: fix it with the No-flicker build rules and re-audit.

```js
// inside page.evaluate, with the site's render loop paused (__site.pause(true))
const { renderer, scene, camera, THREE } = __site._three();
const gl = renderer.getContext(), w = gl.drawingBufferWidth, h = gl.drawingBufferHeight;
const N = 14, frames = [], base = camera.position.clone(), q = camera.quaternion.clone();
for (let i = 0; i < N; i++) {
  camera.position.copy(base).add(new THREE.Vector3(i * .0007, i * .0004, -i * .0005)); camera.quaternion.copy(q); camera.updateMatrixWorld();
  renderer.render(scene, camera);
  const px = new Uint8Array(w * h * 4); gl.readPixels(0, 0, w, h, gl.RGBA, gl.UNSIGNED_BYTE, px);
  const L = new Uint8Array(w * h); for (let p = 0; p < w * h; p++) L[p] = (px[p*4] * 3 + px[p*4+1] * 6 + px[p*4+2]) / 10; frames.push(L);
}
const flag = new Uint8Array(w * h); let count = 0;
for (let p = 0; p < w * h; p++) {
  let rev = 0, last = 0;
  for (let i = 1; i < N; i++) { const d = frames[i][p] - frames[i-1][p]; if (Math.abs(d) < 30) continue; const s = Math.sign(d); if (last && s !== last) rev++; last = s; }
  if (rev >= 3) { flag[p] = 1; count++; }
}
// name the culprits: raycast a sample of flagged pixels (readPixels rows run bottom-up)
const ray = new THREE.Raycaster(), hits = {};
for (let p = 0, k = 0; p < w * h && k < 400; p += 37) if (flag[p]) {
  k++; ray.setFromCamera(new THREE.Vector2((p % w) / w * 2 - 1, ((p / w) | 0) / h * 2 - 1), camera);
  const hit = ray.intersectObjects(scene.children, true).find(o => o.object.visible && o.object.isMesh);
  if (hit) { const key = hit.object.name || (hit.object.geometry.type + '@' + hit.object.position.toArray().map(n => n.toFixed(2))); hits[key] = (hits[key] || 0) + 1; }
}
return { pct: count / (w * h) * 100, culprits: Object.entries(hits).sort((a, b) => b[1] - a[1]) };
```

- For 2D lit-scene sites, run the same reversal test on frames rendered while nudging the light or the scene offset by sub-pixel steps.

## Step 6 - The wow review (required, then iterate)

After the site works, judge it as a first-time visitor would, and improve it before handing over.

1. **Look at it fresh.** Open your screenshots, then open the crops in `assets/quality-bar/` and compare close-ups of your own site against them **for craft only**: softness and direction of shadows, how light falls and changes, surface detail, how effects read, how polished the UI is. Do not take objects, layout or palette from them. If you can spawn a subagent, ask a fresh one to review your screenshots against the crops with only this rubric, not your reasoning.
2. **Score each item 0-2:**
   - **First five seconds:** is the opening view beautiful and intriguing before any click?
   - **Signature moment:** is there one moment people would screen-record and send to a friend?
   - **Light and depth:** does it feel physical, with real light that changes, at the level of the crops?
   - **Material truth:** does every effect and every object back make sense?
   - **Play:** is everything interactive, with a game, a reward and at least three secrets?
   - **Personal:** could this only be this person's site?
   - **Story (the recruiter test):** in 60 seconds, without hunting, could a hiring manager say who this person is, where they've worked and their two biggest results? Does every role, project, award, talk and degree have its own object, place or chapter?
   - **Polish:** no overlaps, overflow, flat spots, jank, flicker (the flicker audit passed) or broken mobile layout.
   - **Originality:** it passes the reskin check: with the name removed, it could still only be this person's site, and it reuses no reference build's specific objects, arrangement or wow moment.
3. **Iterate.** If any item scores 0, or the total is under 15 of 18, write down the weakest two items and a concrete improvement for each, build them, re-screenshot and score again. **Always do at least one more round aimed at the signature moment, even when it passes.** Stop after three rounds and report what you'd still improve.
4. After any change from the review, re-run the real-visitor walkthrough for what you touched.
5. Republish the artifact and tell the person briefly what the review found and what you changed, then go to Step 7.

## Step 7 - Ask for feedback and iterate

Once the wow review is done and the artifact is republished, hand it to the person and ask for their reactions in one short, friendly message:
- What do you love? (so you protect it)
- What don't you like, or what feels off?
- Anything to change: content, wording, objects, light, sounds, the wow moment, secrets?
- Anything missing you'd like added?

Then iterate. Expect many rounds of specific feedback: apply each precisely, re-verify with screenshots, **re-run the real-visitor walkthrough for anything you touched, and the flicker audit after any change to geometry, cameras or transparency**, and republish to the **same artifact URL** after each round with one line on what changed. If there are several versions, keep them in sync. Keep asking after each round until they say it's done.

## Step 8 - Deploy and share

When the person says the site is final, offer to deploy it so they get a public link they can share with anyone.

- **Netlify (recommended).** Check whether a Netlify connector is connected. If it isn't, search the connector registry for Netlify and suggest it, and tell the person in one line: "Add the Netlify connector and I'll deploy your site and give you a link you can share." Once it's connected, deploy the single self-contained `index.html` (plus any other versions in sub-folders, linked from each other) as a new Netlify site, confirm the deploy succeeded, open the live URL to check it loads, and give the person the link. Ask before creating the site, and ask what they'd like the site name to be (it becomes `<name>.netlify.app`).
- **Alternatives** if they prefer: keep the published artifact link, or hand over `index.html` for any static host. For a repo-based deploy: `netlify.toml` with `publish = "site"`, `site/index.html`, other versions at `site/v2/`, `site/v3/`; git commits authored by the person (ask whether they want a Claude co-author line; add none unless they do); ask before pushing.
- For any later change, update the same Netlify site so the shared link stays the same.

## Optional demo video

Offer a 60-90s click-around demo with the site's own sounds, every Easter egg and the wow moment, with a title-card cover so the thumbnail isn't black. Record with deterministic virtual-time frame stepping in Playwright, render the logged sound events offline, and mux with ffmpeg.