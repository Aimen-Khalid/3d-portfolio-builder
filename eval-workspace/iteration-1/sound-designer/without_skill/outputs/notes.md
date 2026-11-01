# Ayesha Noor — playable soundscape portfolio (baseline, no skill)

## What I built
A single self-contained `index.html` (Google Fonts are the only external request; no libraries). The hero is a full-screen, hand-drawn Canvas 2D Lahore rooftop scene. Every credit is an object you can play with, and each one makes a sound synthesized live with Web Audio:
- **Cloud** (drag it or hold it): rain falls on the corrugated tin roof. Each drop pings at a pitch set by where it lands, and a rain hiss fades in and out. This stands for her "rain on tin roofs" recordings.
- **Rickshaw** (tap it): it drives across the street with a two-stroke putter, a doppler-ish pitch bend, stereo panning, horns and exhaust puffs. One also passes by on its own now and then.
- **Badshahi Mosque pigeons** (tap the mosque): the flock scatters with wing-clap bursts, coos, then flies home.
- **Kite / patang** (drag and fling it): wind and string sounds follow how fast you move it. Labelled "Kite Rush · audio lead".
- **Lantern and moth** (tap it): the lantern glows, the moth flutters faster, and you hear a hum plus a chime. Labelled "Moth & Lantern · Best Audio nominee".
- **Radio** (tap it): a short plucked sketch in a Bhairavi-like scale over a drone and rain. It is clearly labelled as a synth sketch, not the real "Rain on Anarkali" score.
- Tapping anywhere else plays a single drop.
- **Tape-deck bar** along the bottom: a now-playing label, spinning reels, a live oscilloscope fed by the audio analyser, and an 8-step "Make a Lahore loop" sequencer (tin / honk / coo / flap). The sequencer is hidden on mobile.
- **Day cycle:** the sky moves through a 2-minute loop (dusk, night, dawn, day). At night, windows light up, stars come out, the mosque darkens and the rickshaw's headlight turns on.
- **Below the hero:** paper "liner notes" with three tracklist cards for the credits, each with a play button that scrolls up and triggers its object. Then a field-recordings list with play buttons, then contact.
- **Honesty and accessibility:** a sound on/off chip, and audio only starts after the visitor interacts. A note says the sounds are synthesized stand-ins. Each sound has a `src` slot so real clips replace the synth with no other changes. Reduced motion is respected for the reels and scroll.

## How I checked it
- Python Playwright + Chromium (one browser at a time) at 1440x900 and at 390x844 (mobile, touch).
- No console or page errors.
- `scrollWidth` matches the viewport width, so there is no horizontal scroll.
- Hit-testing returns the right object for the lantern, radio, kite and mosque.
- Dragged the cloud to trigger rain, called every sound trigger, and screenshotted the result (pigeons in flight, rickshaw puffs, radio waves, rain splashes all render).
- Looked at the screenshots and fixed what they showed: the chip and hint overlapped on mobile, labels collided, the mosque was cut off on mobile, the city was drawn over the mosque, and the pigeons' initial `rain` state was NaN.
- Not verified: how the sounds actually sound by ear (headless). The synthesis was reasoned about, not listened to.

## Composition fingerprint
Camera: Fixed side-on, eye-level 2D view across a Lahore rooftop toward the street and Badshahi Mosque on the skyline.
Ground: A corrugated tin roof along the bottom edge, a street band above it and a layered city/mosque skyline behind, with a tape-deck control bar docked at the bottom and scrolling paper liner notes below.
Movement: The visitor doesn't travel; they drag the cloud and kite, tap objects to trigger sounds, then scroll down into the liner-notes page.
Time: A 2-minute day cycle loops dusk to night to dawn to day (sky colour, sun/moon, lit windows, stars, headlight).
Look: Flat illustrated vector shapes in warm sandstone, dusk-gradient and paper tones, with mono-type label chips and a dark wooden tape-deck UI.
