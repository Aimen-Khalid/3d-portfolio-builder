# Lit-scene renderer (albedo + height maps, G-buffer, lighting pass)

Read this when the world is a **lit scene seen from a fixed camera** (top-down flat-lay, a wall, a shelf, a tabletop, a board) and you are about to write the renderer. For orbitable 3D worlds use Three.js instead (see SKILL.md, "It must feel physical"), but the light-preset section below still applies.

This is a proven starting point, not a style. Change the camera, objects, palette, light, gobo and atmosphere freely; swap parts out; invent better ones.

## How it works

1. Every object is drawn **in code** onto two canvases at 2x: **albedo** (colour + alpha) and **height** (R = height / hMax, G = roughness, B = metalness).
2. **G-buffer pass.** The background and every object quad are drawn into a framebuffer with two colour attachments: RGBA8 albedo and RGBA16F height/rough/metal/coverage (needs `EXT_color_buffer_float`; fall back to RGBA8). Premultiplied blending: `gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA)`.
3. **Lighting pass.** One full-screen pass derives normals from the height field, raymarches soft shadows toward the sun, adds AO, specular, a light patch with a gobo, steam and dust motes, then tone-maps.

Because the light is real, a code-drawn flat-lay counts as physical. Hover lift, held objects and flips all just change the height written into the G-buffer, so shadows lengthen automatically.

## Drawing objects

```js
const SC = 2; // draw at 2x
function mk(w, h, hMax){
  const A = document.createElement('canvas'), H = document.createElement('canvas');
  A.width = H.width = Math.ceil(w*SC); A.height = H.height = Math.ceil(h*SC);
  const a = A.getContext('2d'), hc = H.getContext('2d'); a.scale(SC,SC); hc.scale(SC,SC);
  return {A, H, a, h:hc, w, hh:h, hMax};
}
// colour to paint into the height canvas: height in world units, roughness 0-1, metal 0-1
function hv(o, v, r=.6, m=0){
  const c = x => Math.round(Math.min(1, Math.max(0, x))*255);
  return `rgb(${c(v/o.hMax)},${c(r)},${c(m)})`;
}
// handy texture helpers
function seeded(s){ return () => (s = (s*16807) % 2147483647, (s-1)/2147483646); }
function speckle(c,x,y,w,h,n,col,rmax,seed){ const R=seeded(seed||3); for(let i=0;i<n;i++){ c.fillStyle=col(R); c.beginPath(); c.arc(x+R()*w,y+R()*h,R()*rmax+.2,0,6.283); c.fill(); } }
function fibers(c,x,y,w,h,n,alpha,seed){ const R=seeded(seed||5); c.save(); c.lineWidth=.5; for(let i=0;i<n;i++){ const px=x+R()*w,py=y+R()*h,a=R()*6.283,l=2+R()*6; c.strokeStyle=`rgba(80,60,40,${alpha*R()})`; c.beginPath(); c.moveTo(px,py); c.lineTo(px+Math.cos(a)*l,py+Math.sin(a)*l); c.stroke(); } c.restore(); }
```

Rules of thumb for height maps:
- Paint height with gradients, not flat fills: a glass has a rim, a liquid surface and a base; a notebook has a spine dip and page stacks; a medal has a raised relief.
- Roughness sells materials: paper ~0.85-0.95, wax ~0.35, glass and liquid ~0.08, brass ~0.3 with metal 1.
- Keep `hMax` honest per object (a sheet of paper ~6, a book ~30, a glass ~120). Shadow length comes from it.
- Redraw art after fonts load; measure text and shrink or wrap so nothing overflows an object's edge.

## Shaders

Shared noise:

```glsl
float hash(vec2 p){vec3 p3=fract(vec3(p.xyx)*.1031);p3+=dot(p3,p3.yzx+33.33);return fract((p3.x+p3.y)*p3.z);}
float noise(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(hash(i),hash(i+vec2(1,0)),f.x),mix(hash(i+vec2(0,1)),hash(i+vec2(1,1)),f.x),f.y);}
float fbm(vec2 p){float s=0.,a=.5;for(int i=0;i<5;i++){s+=a*noise(p);p=mat2(1.6,1.2,-1.2,1.6)*p+7.3;a*=.5;}return s;}
```

**Background** (writes straight into the G-buffer; procedural surface, e.g. wood planks, stone, cloth). Map the fragment to world space with `vec2 w = cam + vec2(p.x-res.x*.5, res.y*.5-p.y)/S;`, compute colour `c`, height `h` and roughness, then:

```glsl
o0 = vec4(pow(c, vec3(1./2.2)), 1.);  o1 = vec4(h, rough, 0., 1.);
```

**Object quad** vertex shader (position, size, pivot, scale, rotation in world units):

```glsl
#version 300 es
in vec2 a; uniform vec2 pos,size,scl,piv,cam,res; uniform float rot,S; out vec2 uv;
void main(){ vec2 l=(a*size-piv)*scl; float c=cos(rot),s=sin(rot);
  vec2 w=pos+vec2(c*l.x-s*l.y,s*l.x+c*l.y); vec2 d=(w-cam)*S+res*.5; uv=a;
  gl_Position=vec4(d.x/res.x*2.-1.,1.-d.y/res.y*2.,0.,1.); }
```

**Object fragment** core (`base` lifts the object off the surface, `lift` is hover lift; `off` and `hr` come from material effects, see `material-effects.md`; the ink rect comes from `html-in-canvas.md`):

```glsl
#version 300 es
precision highp float; in vec2 uv;
layout(location=0) out vec4 o0; layout(location=1) out vec4 o1;
uniform sampler2D tA,tH,tI; uniform vec4 inkR; uniform float hasInk,hMax,base,lift,alpha;
void main(){ vec4 A=texture(tA,uv); if(A.a<.003) discard;
  vec2 off=vec2(0.); float hr=0.;
  /* material effects add to off / hr here */
  if(hasInk>.5){ vec2 iu=(uv+off-inkR.xy)/inkR.zw;
    if(iu.x>0.&&iu.y>0.&&iu.x<1.&&iu.y<1.){ vec4 k=texture(tI,iu); A.rgb=k.rgb*A.a+A.rgb*(1.-k.a); } }
  vec4 H=texture(tH,uv); float cov=A.a*alpha; float hh=base+lift+H.r*hMax+hr*9.;
  o0=vec4(A.rgb*alpha,cov); o1=vec4(hh*cov,H.g*cov,H.b*cov,cov); }
```

**Lighting pass** (`L` = unit sun direction, `S` = world-to-pixel scale, `sunPatch` = centre + half-size of the light patch, `steam` = screen position + radius of a hot drink):

```glsl
#version 300 es
precision highp float; out vec4 o;
uniform sampler2D tA,tM; uniform vec2 res,cam; uniform float S,t,motes;
uniform vec3 L,sunC,ambC; uniform vec4 sunPatch; uniform float patchRot,gobScale; uniform vec3 steam; uniform vec2 drift;
/* hash/noise/fbm */
float hh(vec2 p){ return texture(tM,p/res).r; }
float gobo(vec2 q,float w){ // swap for any pattern: window panes, leaves, blinds, a lattice screen
  vec2 f=fract(q)-.5; float a=max(abs(f.x),abs(f.y)); vec2 r=mat2(.7071,-.7071,.7071,.7071)*f;
  float s=min(a,max(abs(r.x),abs(r.y))*1.1); float star=1.-smoothstep(.235-w,.235+w,s);
  float corner=1.-smoothstep(.06-w,.06+w,length(fract(q+.5)-.5)); return max(star,corner); }
vec3 aces(vec3 x){ return clamp((x*(2.51*x+.03))/(x*(2.43*x+.59)+.14),0.,1.); }
void main(){ vec2 p=gl_FragCoord.xy, uv=p/res; vec4 A=texture(tA,uv), M=texture(tM,uv);
  vec3 alb=pow(A.rgb,vec3(2.2)); float h=M.r, rough=M.g, metal=M.b;
  float hx=(hh(p+vec2(1,0))-hh(p-vec2(1,0)))*.5*S, hy=(hh(p+vec2(0,1))-hh(p-vec2(0,1)))*.5*S;
  vec3 n=normalize(vec3(-hx,-hy,1.));
  vec2 w=cam+vec2(p.x-res.x*.5,res.y*.5-p.y)/S;
  // soft shadows: march toward the sun through the height field
  vec2 d2=normalize(L.xy); float slope=L.z/length(L.xy), hd=h*S, maxD=min(150.*S/slope,420.), st=maxD/34., sh=1.;
  for(int i=1;i<=34;i++){ float dist=float(i)*st, pen=.6+dist*.07; sh=min(sh,smoothstep(-pen,pen,hd+dist*slope-hh(p+d2*dist)*S)); }
  // light patch through a gobo; taller things catch it offset along the light
  vec2 wp=w+vec2(L.x,-L.y)/L.z*h, q=wp-sunPatch.xy; float cs=cos(patchRot),sn=sin(patchRot);
  vec2 pq=vec2(cs*q.x+sn*q.y,-sn*q.x+cs*q.y), pr=abs(pq)/sunPatch.zw;
  float soft=.06+.05*clamp(1.-h/80.,0.,1.);
  float pm=(1.-smoothstep(1.-soft,1.+soft,pr.x))*(1.-smoothstep(1.-soft*1.4,1.+soft*1.4,pr.y));
  float jw=.07+.04*noise(w*.004)+.05*(1.-clamp(h/90.,0.,1.)); // blurrier gobo edges on taller objects
  float gob=mix(.26,1.,gobo(pq*gobScale+drift,jw))*pm;
  float dif=max(dot(n,L),0.), direct=sh*gob;
  // ambient occlusion: 8 taps
  float ao=0.; for(int k=0;k<8;k++){ float an=float(k)*.785+.3; ao+=clamp((hh(p+vec2(cos(an),sin(an))*14.*S)-h)/14.,0.,1.); } ao=1.-ao/8.*.75;
  vec3 Hv=normalize(L+vec3(0,0,1)); float spw=mix(420.,10.,rough);
  float spec=pow(max(dot(n,Hv),0.),spw)*mix(1.,.05,rough)*(spw+8.)/40.; vec3 F0=mix(vec3(.04),alb,metal);
  vec3 bounce=ambC*(.7+.3*n.z);
  vec3 col=alb*(1.-metal)*(bounce*ao+sunC*dif*direct)+F0*spec*sunC*direct+alb*metal*bounce*ao*.9+F0*metal*ambC*.25;
  // steam over a hot drink: two fbm layers swirling upward, brighter inside the light
  float sd=length(p-steam.xy)/steam.z;
  if(sd<2.6){ float an=atan(p.y-steam.y,p.x-steam.x); vec2 sw=vec2(an*1.6+t*.25,sd*2.4-t*.55);
    float f=fbm(sw)*fbm(sw*1.9+3.1); float m=smoothstep(2.6,.6,sd)*smoothstep(.15,.7,sd);
    col+=vec3(1.,.97,.92)*m*smoothstep(.22,.55,f)*.16*(.4+.6*pm); }
  // dust motes, only inside the light
  if(motes>0.){ vec2 cell=floor(p/56.), rnd=vec2(hash(cell),hash(cell+7.1));
    vec2 mp=(cell+.5+.4*vec2(sin(t*.3+rnd.x*30.),cos(t*.23+rnd.y*30.)))*56.;
    col+=vec3(1.,.9,.7)*(1.-smoothstep(.6,2.2,length(p-mp)))*step(.62,rnd.x)*gob*.8*motes; }
  col=aces(col*1.1); col=mix(vec3(dot(col,vec3(.299,.587,.114))),col,1.08);
  vec2 vv=uv-.5; col*=1.-dot(vv,vv)*.55; col=pow(col,vec3(1./2.2));
  col+=(hash(p+fract(t))-.5)*.018; // film grain
  o=vec4(col,1.); }
```

## WebGL plumbing

```js
const gl = canvas.getContext('webgl2', {antialias:false, alpha:false, premultipliedAlpha:false});
if(!gl) showPlainPage();                       // WebGL failure → plain page
const hasF16 = !!gl.getExtension('EXT_color_buffer_float');
function tex(){ const t=gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D,t);
  [gl.TEXTURE_MIN_FILTER,gl.TEXTURE_MAG_FILTER].forEach(k=>gl.texParameteri(gl.TEXTURE_2D,k,gl.LINEAR));
  [gl.TEXTURE_WRAP_S,gl.TEXTURE_WRAP_T].forEach(k=>gl.texParameteri(gl.TEXTURE_2D,k,gl.CLAMP_TO_EDGE)); return t; }
function upload(t,src,premul){ gl.bindTexture(gl.TEXTURE_2D,t); gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL,!!premul);
  gl.texImage2D(gl.TEXTURE_2D,0,gl.RGBA,gl.RGBA,gl.UNSIGNED_BYTE,src); }
// albedo uploads premultiplied (true); height uploads not premultiplied (false)
function allocG(){ gl.bindTexture(gl.TEXTURE_2D,gA); gl.texImage2D(gl.TEXTURE_2D,0,gl.RGBA8,DW,DH,0,gl.RGBA,gl.UNSIGNED_BYTE,null);
  gl.bindTexture(gl.TEXTURE_2D,gM);
  if(hasF16) gl.texImage2D(gl.TEXTURE_2D,0,gl.RGBA16F,DW,DH,0,gl.RGBA,gl.HALF_FLOAT,null);
  else gl.texImage2D(gl.TEXTURE_2D,0,gl.RGBA8,DW,DH,0,gl.RGBA,gl.UNSIGNED_BYTE,null);
  gl.bindFramebuffer(gl.FRAMEBUFFER,fbo);
  gl.framebufferTexture2D(gl.FRAMEBUFFER,gl.COLOR_ATTACHMENT0,gl.TEXTURE_2D,gA,0);
  gl.framebufferTexture2D(gl.FRAMEBUFFER,gl.COLOR_ATTACHMENT1,gl.TEXTURE_2D,gM,0); }
```

Each frame: bind the FBO, `gl.drawBuffers([COLOR_ATTACHMENT0, COLOR_ATTACHMENT1])`, draw the background with blending off, enable premultiplied blending, draw objects in a back-to-front order list (held and dragged objects last), unbind, run the lighting pass to the screen. Wrap shader compilation in try/catch and fall back to the plain page if it fails.

Performance: cap device pixel ratio (1.75-2), pause when `document.hidden`, keep the shadow march at ~34 steps and AO at 8 taps.

## Light presets

One object per mood, eased every frame, chosen from a single dropdown, defaulting to the visitor's clock. Pick presets that **mean something to this person** (prayer times, golden hour in their city, seasons, studio lights on and off, a lighthouse sweep, stage lighting). Example values from a reference build (a warm sun through a screen onto a dark wood surface):

```js
const LIGHTS = {
  dawn:   {name:'Dawn',    dot:'#B9C7E8', L:[.62,.38,.69],  sun:[1.05,.98,1.12], amb:[.13,.14,.19],  shift:[-430,40],  size:[1.1,.9],  rot:-.22, scale:.0118},
  midday: {name:'Midday',  dot:'#FFF3D6', L:[-.16,.22,.96], sun:[2.05,1.95,1.72],amb:[.25,.235,.22], shift:[-120,-30], size:[.82,.9],  rot:.05,  scale:.0145},
  late:   {name:'Late afternoon', dot:'#F2C46B', L:[-.56,.46,.69], sun:[1.75,1.42,1.02], amb:[.21,.18,.17], shift:[0,0], size:[1,1], rot:0, scale:.0125},
  sunset: {name:'Sunset',  dot:'#E8794A', L:[-.84,.26,.36], sun:[2.1,.82,.46],  amb:[.10,.085,.13], shift:[240,70],  size:[1.15,.86],rot:.12,  scale:.0098},
  night:  {name:'Night',   dot:'#8FA6D8', L:[.42,.55,.72],  sun:[.34,.46,.82],  amb:[.04,.045,.08], shift:[-260,-20], size:[.95,.95], rot:-.1,  scale:.0112},
};
// every frame: ease toward the target (k = 1 - exp(-dt*2.2)); reduced motion → k = 1
for(const key of ['L','sun','amb','shift','size']) cur[key] = cur[key].map((v,i)=> v + (T[key][i]-v)*k);
cur.rot += (T.rot-cur.rot)*k; cur.scale += (T.scale-cur.scale)*k;
```

What makes presets feel alive: a **low sun** gives long shadows and saturated colour (sunset), a **high sun** short crisp shadows; move and resize the light patch with the sun; night swaps the sun for cool moonlight with very low ambient. A light-change swell sound and a knock/tap secret that time-lapses through all presets are cheap, lovely touches.
