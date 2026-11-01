# Lift to the centre and turn over

Read this when building **depth when you open something**. The proven default: an object rises toward the visitor, settles at the centre of the screen, and turns over (or opens) on a second click. Every site needs depth on opening, in whatever form fits its world: the camera flying in, an object unfolding, a container unpacking, or this lift-and-turn.

## Holding (2D lit scenes)

Each object stores `home = [x, y, rot, base]` and `homeS`. A held group (one object, or a few that come up together, like a fan of sticky notes) has a target: the screen centre minus the caption panel, scaled to fit the free space.

```js
function holdTargets(group){
  const cap = captionSize(group);                          // desktop: panel on the right; portrait: bottom sheet
  const sx = (VW - cap.w)/2, sy = (VH - cap.h)/2;          // centre of the free area
  const wx = WORLD_W/2 + (sx - VW/2)/S0, wy = WORLD_H/2 + (sy - VH/2)/S0;
  const freeH = VH - cap.h - 130, freeW = VW - cap.w - 60, d = DIM[group];
  const s = Math.min(freeH/(d.h*S0), freeW/(d.w*S0)) * .94; // fit, then cap so small things don't go huge
  return {[group]: {x:wx, y:wy - d.oy*s, rot:-.015, s:Math.min(s, 2.8), base:120}}; }

function holdStep(dt){ for(const g in HOLD){
  const tk = holdT[g]||0, ck = holdK[g]||0; if(tk===ck && ck===0) continue;
  const nk = reduceMotion ? tk : ck + clamp(tk-ck, -dt/.85, dt/.85); holdK[g] = nk;   // ~0.85 s
  const T = holdTargets(g), e = ease(nk), arc = Math.sin(nk*Math.PI);
  for(const id of HOLD[g]){ const o = byId[id], h = o.home, t = T[id]; o.held = nk > .001;
    o.x = lerp(h[0], t.x, e); o.y = lerp(h[1], t.y, e); o.rot = lerp(h[2], t.rot, e); o.s = lerp(o.homeS, t.s, e);
    o.base = lerp(h[3], t.base, e) + arc*70;               // arcs up toward the viewer on the way
    if(nk===0){ Object.assign(o, {x:h[0], y:h[1], rot:h[2], s:o.homeS, base:h[3], held:false, flipT:0}); } } } }
```

Because `base` is height in the G-buffer, the shadow grows and softens as the object rises. Draw held and dragged objects last.

## Turning over

```js
function flipStep(dt){ for(const o of objs){ const t = o.flipT||0; let k = o.flipK||0; if(t===k) continue;
  k = reduceMotion ? t : k + clamp(t-k, -dt/.6, dt/.6); o.flipK = k; } }               // ~0.6 s
// when drawing: x-scale by max(.03, |cos(flipK*PI)|), use the back textures once flipK > .5,
// and add sin(flipK*PI)*60 to the height so it lifts while it turns
```

Every object that turns needs a **back drawn for real** (`material-effects.md`, material-truth rule): return details on an ID card, engraving on a medal, a phone case with a ticket tucked inside, a postcard's stamp and address lines.

## Opening (containers)

Envelopes, boxes, drawers, books, jars: give them a staged pose `pose(k)` driven by one eased value, e.g. an envelope comes forward, the seal cracks (sound + seal pieces), the flap rotates open past 90° (draw order swaps behind the body), the letter slides out and then rises above. Reverse it on close.

## Real 3D version

In Three.js: on click, tween the object (or the camera) so the object sits at the centre in front of the camera, with damped springs and a slight overshoot; a second click rotates it 180° around its long axis, or opens its lid/door with a hinge rotation. Raise shadow camera bounds so the lifted object still casts. Return with the same curve reversed.

## Captions and controls

- Details live **on the object** first; a caption can add context. A layout that works well: a glass panel on the right on desktop, a bottom sheet on phones, with the held object fitted to the space left over. Design what suits the world.
- Close with a button, Escape or a click outside. A visible "← Back" pill while something is held.
- `prefers-reduced-motion`: jump to the end state with a short fade.
