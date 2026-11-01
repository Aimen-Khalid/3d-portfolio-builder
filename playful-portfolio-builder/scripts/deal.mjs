#!/usr/bin/env node
/* Deals composition hands for a playful portfolio world.

   Asked to invent a world, a model reaches for the same few layouts every time (a round island town
   seen from above, an isometric room, a desk). This script takes that choice away: it deals hands of
   five axes (camera, ground, movement, time, look) at random, every hand different on every axis,
   and the model picks the hand that the person's own story fits best.

   Usage:
     node scripts/deal.mjs                 deal 3 hands
     node scripts/deal.mjs --count 4       deal 4 hands
     node scripts/deal.mjs --seed 81723    repeat an earlier deal
     node scripts/deal.mjs --redraw look   print 3 alternatives for one axis
     node scripts/deal.mjs --list          print every option on every axis
   No dependencies; Node 16+. */

const AXES = {
  camera: [
    { id: "overhead", name: "Straight down", how: "the camera looks straight down at a surface, like a flat-lay or a map on a table" },
    { id: "high-orbit", name: "High three-quarter, orbiting", how: "looking down at an angle at something you can turn around", common: true },
    { id: "eye-level", name: "Eye level, inside it", how: "standing in the world at a person's height, looking across it" },
    { id: "cross-section", name: "Side cross-section", how: "the world cut open and seen from the side, like a dollhouse, an ant farm or a ship's hull" },
    { id: "first-person", name: "First person, moving", how: "you are the camera: walking, riding or flying through it" },
    { id: "macro", name: "Very close", how: "the camera is tiny next to big objects; things fill the frame and it slides from one to the next" },
    { id: "through", name: "Through a frame", how: "seen through something: a window, a viewfinder, a peephole, a telescope, a phone screen" },
  ],
  ground: [
    { id: "disc", name: "A disc or floating island", how: "a round patch of land with things placed around it", common: true },
    { id: "line", name: "A single line", how: "one road, river, rail line, corridor or timeline; the story is laid out along it" },
    { id: "grid", name: "A grid or board", how: "squares, tiles or a game board; each square holds something" },
    { id: "sphere", name: "A sphere", how: "a globe, planet, ball or bubble you turn" },
    { id: "container", name: "A container", how: "a box, jar, drawer, suitcase, locker, bag or snow globe; things are inside it" },
    { id: "sheet", name: "A sheet that unfolds", how: "a map, page, cloth, scroll or poster that opens out" },
    { id: "stack", name: "A vertical stack", how: "a tower, shelf, stairwell, layers of earth or the floors of a building" },
    { id: "surface", name: "A working surface", how: "a desk, counter, workbench, floor or table", common: true },
  ],
  movement: [
    { id: "orbit-fly", name: "Orbit and fly to things", how: "drag to turn the view; clicking something flies the camera to it", common: true },
    { id: "path", name: "Travel a path", how: "scrolling moves you along a route, stop by stop" },
    { id: "vehicle", name: "Drive or ride", how: "steer something (a bike, rickshaw, boat, train, paper plane) to the places" },
    { id: "steps", name: "Step by step", how: "move square by square or stop by stop, like a board game or a stepping-stone path" },
    { id: "open", name: "Open things up", how: "unfold, unpack, open lids and doors; the content is inside" },
    { id: "zoom", name: "Zoom into layers", how: "each click goes one level deeper into nested worlds, from far to very close" },
    { id: "handle", name: "Handle the whole world", how: "pick up, tilt, spin, shake or rotate the world itself" },
  ],
  time: [
    { id: "day", name: "A day passes", how: "light moves from morning to night; the visitor can change the hour", common: true },
    { id: "seasons", name: "Seasons", how: "the same world in spring, summer, autumn and winter" },
    { id: "years", name: "Years of their life", how: "a scrubber or dial moves through years and the world grows or changes with them" },
    { id: "weather", name: "Weather", how: "rain, sun, fog, wind or snow, each changing how things look and sound" },
    { id: "frozen", name: "One frozen moment", how: "everything is caught mid-motion and the visitor can release it" },
    { id: "lamps", name: "Lights you switch", how: "the visitor turns lamps, screens or signs on and off, one by one" },
  ],
  look: [
    { id: "toy", name: "Low-poly toy", how: "chunky, smooth, rounded, like a toy model", common: true },
    { id: "paper", name: "Paper and card", how: "cut paper, folded card, layered cardboard with visible edges" },
    { id: "clay", name: "Clay and plasticine", how: "soft, hand-pressed, slightly lumpy, with fingerprints" },
    { id: "photoreal", name: "Real materials, real light", how: "wood, metal, fabric and glass under one strong light" },
    { id: "ink", name: "Ink and watercolour", how: "hand-drawn lines and washes, like a sketchbook come alive" },
    { id: "glass", name: "Glass and light", how: "translucent, glowing, refracting, set in the dark" },
    { id: "textile", name: "Textile", how: "felt, embroidery, knit or quilting, stitched together" },
  ],
};

const args = process.argv.slice(2);
const flag = (k) => { const i = args.indexOf("--" + k); return i < 0 ? null : (args[i + 1] && !args[i + 1].startsWith("--") ? args[i + 1] : true); };

if (flag("list")) {
  for (const [axis, opts] of Object.entries(AXES)) {
    console.log(`\n${axis.toUpperCase()}`);
    for (const o of opts) console.log(`  ${o.id.padEnd(14)} ${o.name}: ${o.how}${o.common ? "  (a common default; only if the person's story calls for it)" : ""}`);
  }
  process.exit(0);
}

const seedArg = flag("seed");
const seed = seedArg && seedArg !== true ? Number(seedArg) >>> 0 : (Date.now() ^ Math.floor(Math.random() * 2 ** 31)) >>> 0;
let s = seed || 1;
const rnd = () => { s = (s * 1664525 + 1013904223) >>> 0; return s / 2 ** 32; };
// common defaults are dealt a third as often, so they turn up only now and then
const weight = (o) => (o.common ? 1 : 3);
function draw(pool, taken) {
  const left = pool.filter((o) => !taken.has(o.id));
  const total = left.reduce((t, o) => t + weight(o), 0);
  let r = rnd() * total;
  for (const o of left) { r -= weight(o); if (r <= 0) return o; }
  return left[left.length - 1];
}

const redraw = flag("redraw");
if (redraw && redraw !== true) {
  const pool = AXES[redraw];
  if (!pool) { console.error(`No axis "${redraw}". Axes: ${Object.keys(AXES).join(", ")}`); process.exit(1); }
  const taken = new Set();
  console.log(`Alternatives for ${redraw} (seed ${seed}):`);
  for (let i = 0; i < 3; i++) { const o = draw(pool, taken); taken.add(o.id); console.log(`  - ${o.name}: ${o.how}${o.common ? " (common default)" : ""}`); }
  process.exit(0);
}

const count = Math.max(1, Math.min(6, Number(flag("count")) || 3));
const used = Object.fromEntries(Object.keys(AXES).map((k) => [k, new Set()]));
console.log(`Composition deal · seed ${seed} · ${count} hands. Every hand differs from the others on every axis.\n`);
for (let h = 0; h < count; h++) {
  console.log(`HAND ${String.fromCharCode(65 + h)}`);
  for (const [axis, pool] of Object.entries(AXES)) {
    const o = draw(pool, used[axis]); used[axis].add(o.id);
    console.log(`  ${axis.padEnd(9)} ${o.name}: ${o.how}${o.common ? "  (common default)" : ""}`);
  }
  console.log("");
}
console.log("Pick the hand the person's own story fits best, and fill it with something only they have.");
console.log("You may redraw one axis for a reason you can state (it fights the story, or it cannot hold the content). Record the seed and any redraw in your notes.");
