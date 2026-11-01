# Nadia Rahman: "First Light" portfolio (baseline, no skill)

## What I built
A single self-contained `index.html` (three.js r160 from jsDelivr, Google Fonts, everything else inline and procedurally generated with no image assets). The whole portfolio is one marble kitchen counter under a window at dawn, seen head-on at standing height.

- **The surprise is a time-of-morning dial.** On arrival the clock reads 5:48 with the sky still dark, and a pendant lamp is the only light. Over about 40 seconds the sun rises through the window on its own. The sky goes from indigo to coral to pale blue, a dusty light shaft sweeps across the counter, mullion shadows slide over the crust, flour motes glow in the beam, the lamp switches off, and the wall clock's hands move. The visitor can drag the dial anywhere from 5:30 to 8:15. A handwritten line under her name changes with the light ("There it is. The first twenty minutes are the good ones.").
- **Every object is a section.** Tapping an object glides the camera to it and opens a lined recipe card:
  - the scored boule: Crumb Bakery quote ("makes bread look like a sunrise", which the sunrise itself acts out)
  - the leaning *Flour Moons* cookbook: 2023, 120 recipes, plus the Leila Haddad quote
  - the steaming karak cup: Karak House quote
  - the magazine: Gulf Food "30 to Watch", 2024
  - a ticket rail of kitchen order tickets: the career timeline (Sugar & Salt, Maison Lumière, photography)
  - the camera: the 2021 switch to photography
  - the wall clock: why mornings
  - a spiked "NEW ORDER · book a morning" ticket: contact
- **Shutter button.** It captures the current frame as a polaroid that develops into a tray. Click a polaroid to download it.
- "Show me around" runs a guided tour of all 8 cards. "Read it as a page" opens a plain, fully readable HTML version with every fact and quote, which is also the fallback if WebGL fails. Esc and the arrow keys work, and the hotspot dots are real buttons with labels.
- Responsive: cards become a bottom sheet on phones, and the camera reframes for portrait.
- `?t=6.4` in the URL pins the time (used for screenshots).

## How I checked it
- Rendered with Python Playwright + Chromium (swiftshader WebGL), one browser at a time: hero at 1440x900 and 390x844, plus dawn (5:35), late morning (8:00), an open loaf card, the shutter/polaroid, the mobile bottom-sheet card, and the plain page (in `work/`).
- No page errors or console errors (only swiftshader "GPU stall due to ReadPixels" performance notices from the screenshot readback).
- Mobile `scrollWidth` is 390, so there's no horizontal overflow.
- I iterated on the screenshots. The first pass was murky with the sun patch off the counter and the clock hidden behind the title, so I raised the sun, brightened the ambient light and crust, and moved the clock and lamp. Mobile framing was redone twice to remove an empty band at the bottom.
- Checked the copy against the brief: all dates, names, titles, "120 recipes", "30 to Watch" 2024, and the three quotes verbatim. Nothing invented (no email, city, or clients beyond those named).

## Known limits
- No real photographs. The scene stands in for her portfolio until she supplies images.
- On narrow phones the clock, camera, rail and booking ticket sit off-frame in the hero. They are reached via the tour or the card's next/previous buttons.
- Needs network for three.js and fonts. Without WebGL it falls back to the plain page.

## Composition fingerprint
Camera: Fixed eye-level, slightly elevated head-on view of a kitchen counter against a window wall, gliding in to close-ups of each object when tapped, with subtle mouse parallax.
Ground: A single marble countertop strip with a linen cloth, backed by a plaster-and-tile wall with a mullioned window. Objects (loaf, croissants, camera, cookbook, cup, magazine, ticket spike, wall clock, ticket rail) are arranged along it as hotspots.
Movement: Visitor stays put and taps or clicks objects (or pulsing labelled dots) to fly the camera to them and open recipe-card panels. There's also a next/previous card sequence and an auto tour, but no walking or scrolling.
Time: Sunrise. A time dial from 5:30 to 8:15 AM (auto-advancing on arrival) drives sky colour, sun angle, a moving light shaft and mullion shadows, glowing flour motes, the pendant lamp switching off, wall-clock hands and the caption.
Look: Warm, softly lit, low-poly-realistic 3D with procedural canvas textures (veined marble, plaster, tiles, crusty bread, linen), ACES tone mapping and soft shadows, under a cream paper-and-serif UI with handwritten Caveat notes.
