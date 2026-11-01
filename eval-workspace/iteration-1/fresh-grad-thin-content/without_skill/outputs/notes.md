# Notes: Hira Baig portfolio (baseline, no skill)

## What I built
A single self-contained `index.html` (only Google Fonts are external; no JS libraries).

- **Hero:** her name sits beside a live, rotatable 3D hand skeleton drawn in 2D canvas: the 21 MediaPipe hand landmarks, depth-sorted bones, fingertip highlights and a corner-bracket detection box labelled `hand · X`. The hand **fingerspells H-I-R-A B-A-I-G**, morphing between poses. An "OUT>" console types each letter as it is "recognised" and shows three confidence bars that imitate a classifier (desktop only). Visitors can tap letter keys (H I R A B G) to show a pose and drag to spin the hand (inertia, plus a gentle idle sway). There is also a small HUD (landmarks / fps / pose).
- The point: she has thin content, so the hero *is* her final year project. The site acts out what her app does, in reverse.
- **01 Final year project:** a plain-language description and a 4-step pipeline (Camera → MediaPipe → Recognise → Text) with small SVG diagrams. Step 2 reuses the same landmark model.
- **02 Experience & education:** Brightloom card (3 months, React) and BS CS card (FAST-NUCES Lahore, 2026).
- **03 Contact:** "Looking for my first full-time role" with Email / GitHub / LinkedIn buttons. These are **placeholders** marked with a TODO.
- No photo, awards or invented facts. The footer says the hand poses are hand-drawn approximations of ASL fingerspelling.
- Responsive: on screens under 820px the text stacks above the hand, and the HUD and confidence bars are hidden. Honours prefers-reduced-motion (no sway, no fade-ins).

## How I checked it
- Python Playwright + Chromium at 1440x900 and 390x844 (mobile with touch emulation). No console or page errors, and `scrollWidth` equals the viewport width (no horizontal scroll).
- Clicked each letter key and checked every pose in screenshots (B, A, I, R, G; H shares G's sideways orientation).
- Scrolled the full page so the fade-in sections trigger, then checked full-page shots at both sizes.
- Fixes made after checking: on mobile the tall poses collided with the intro text (moved the hand lower and made it smaller). Tapped keys kept a sticky hover highlight on touch devices (hover is now limited to `(hover:hover)`). Brightloom copy claimed more than the user said (trimmed to the facts).
- Known limit: the poses are believable approximations, not exact sign-language references. A signer should check them, especially R and the thumb in G.

## Composition fingerprint
Camera: Fixed front-on view of a 3D hand skeleton, drawn in perspective, with small idle sway; the visitor can drag to orbit it, and it eases back.
Ground: Dark dot-grid "camera feed" field with a soft radial glow and a floor shadow ellipse; normal vertically scrolling page with sections below the full-screen hero.
Movement: Ordinary page scroll; in the hero, drag to rotate the hand and tap letter keys to make it sign that letter.
Time: The hand loops through fingerspelling H-I-R-A B-A-I-G while the console types the letters and confidence bars update; sections fade in on scroll.
Look: Flat vector debug overlay: cyan glowing bones, white and coral landmark dots, lime detection brackets, monospace HUD text on near-black navy.
