# Material-true surface effects

Read this when an object should react to the cursor or a touch, and before you invent any new effect.

## The material-truth rule

**Every effect must make sense for its material.** Ask: *what would this thing really do if I touched it?* and build that.

- Paper crumples and crinkles. Tea, coffee and ponds ripple. Jelly and rubber wobble and squish. Glass clinks and refracts. Fabric folds where you drag. Metal catches a sliding highlight.
- A water ripple on a book page, a wobble on a steel medal or a crumple on a phone screen are wrong, however pretty.
- **Every face must make sense too.** When an object turns over, its back must look like that object's real back: an ID card's back with return details, an engraved medal, a phone back through a clear case with a ticket tucked inside. Never write random handwriting on a phone or a glass.
- Creativity is welcome inside this rule. Invent effects that appear nowhere here, as long as the material would really do it.
- Disable all distortion for `prefers-reduced-motion`.

## How effects plug into the renderer

Inside the object fragment shader, accumulate a UV offset `off` (applied to the content lookup) and a height delta `hr` (added to the written height, so the lighting pass catches it). `ax = vec2(aspect, 1.)` keeps shapes round. Pass the cursor in object UV as `lens.xy` with an eased strength `lens.z`.

```js
// object-UV of a world point
function objUV(o, wx, wy){ const dx=wx-o.x, dy=wy-o.y, c=Math.cos(-o.rot), s=Math.sin(-o.rot), pv=o.piv||[o.art.w/2,o.art.hh/2];
  return [((c*dx-s*dy)/(o.s*o.sx)+pv[0])/o.art.w, ((s*dx+c*dy)/(o.s*o.sy)+pv[1])/o.art.hh]; }
// every frame: lens strength rises fast and relaxes slowly
o.lensK += (o.lensT - o.lensK) * Math.min(1, dt * (o.lensT > o.lensK ? 5 : 1.6));
```

## Paper crumple (Voronoi folds)

Folded facets with crease lines that slowly relax when the cursor leaves. Use a Voronoi fold field, not plain noise (noise looks like squiggly worms). Two scales: big folds plus fine creases.

```glsl
vec2 h22(vec2 p){ return vec2(hash(p),hash(p+19.17)); }
vec3 crumple(vec2 p){ vec2 ip=floor(p),fp=fract(p); float f1=9.,f2=9.; vec2 cA=vec2(0.);
  for(int y=-1;y<=1;y++) for(int x=-1;x<=1;x++){ vec2 g=vec2(x,y), r=g+h22(ip+g)*.8+.1-fp; float dd=dot(r,r);
    if(dd<f1){ f2=f1; f1=dd; cA=r; } else if(dd<f2) f2=dd; }
  float e=min(sqrt(f2)-sqrt(f1),.5); return vec3(e, normalize(cA+1e-4)*e); }

// in main(), near the cursor:
if(lens.z>0.){ vec2 d=(uv-lens.xy)*ax; float g=exp(-dot(d,d)/.018)*lens.z; g=g*g*(3.-2.*g);
  vec3 c1=crumple(uv*ax*7.), c2=crumple(uv*ax*16.+4.7);
  hr+=(c1.x-c2.x*.45)*g*3.2; off+=(c1.yz-c2.yz*.4)*g*.006/ax; }
```

Apply it to every paper surface that carries HTML-in-Canvas content (pages, letters, cards, badges), and set `lensT = 1` while the pointer is over the ink rect, `0` when it leaves.

## Liquid ripples

Only on liquid surfaces, masked to the liquid's radius so the glass rim stays still.

```glsl
uniform vec4 rp[4]; // (u, v, age seconds, amplitude)
for(int i=0;i<4;i++){ vec4 Q=rp[i]; if(Q.w<=0.) continue; vec2 d=(uv-Q.xy)*ax; float r=length(d), fr=Q.z*.38, x=r-fr;
  float wv=sin(x*78.)*exp(-x*x*70.)*Q.w*exp(-Q.z*.9)*smoothstep(0.,.06,fr+.01);
  off+=(r>1e-4?d/r:vec2(0.))*wv*.009/ax; hr+=wv; }
if(rmask>0.){ float mk=1.-smoothstep(rmask-.025,rmask,length(uv-.5)); off*=mk; hr*=mk; }
if(rippleAlbedo>.5) A.rgb=texture(tA,uv+off).rgb; // the liquid's own colour moves too
```

```js
function addRip(o,u,v,amp){ o.rp.push({u,v,t0:now,a:amp}); if(o.rp.length>4) o.rp.shift(); o.lastRip=[u,v,now]; }
// on pointer move over the liquid: a ripple every ~100-120 ms of movement (amp ~.3; ~.5 on touch)
// on click / tap / a clink: amp ~1-1.3. Drop ripples older than ~3 s.
```

## Other material-true ideas

- **Jelly, rubber, soft toys:** squish toward the press point and wobble with a damped spring on release.
- **Glass:** refraction of what's behind it and a bright specular that slides as you move; text seen through a glass of water bends.
- **Hot drinks:** steam (see `engine-lighting.md`) that puffs bigger after a clink; heat shimmer above.
- **Ink:** wet-ink bleed while typing on paper; a stamp that presses into a card and leaves a relief in the height map.
- **Fabric:** folds that follow a drag; a napkin that lifts at the corner.
- **Metal:** a brass highlight that slides with the light preset; a medal that spins on its ribbon when flicked.

Whatever you invent, add it to the height map so the light reacts, and give it a matching sound (`sound-kit.md`).
