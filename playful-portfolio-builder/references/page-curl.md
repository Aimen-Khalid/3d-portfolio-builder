# Page curl: a bending, shaded sheet

Read this when the world has anything with pages (books, notebooks, scrapbooks, passports, zines, comics, menus, calendars). A flat card flip is never acceptable for a page.

## Idea

The turning page is a grid mesh rebuilt on the CPU every frame of the turn. In a lit scene it is drawn **into the same G-buffer** as everything else, so the scene's light catches it, a gobo pattern slides over it and it casts a real shadow. In Three.js, use the same vertex math on a `BufferGeometry` with a double-sided material and shadows on. Any approach is fine as long as the page really bends and is lit. The front face shows the old page, the back face the new one. While the curl runs, the flat book keeps showing the old page on the turning side.

## Mesh

An (N+1) x (M+1) grid, N = 44 along the page, M = 16 down it. For turn progress `k` (0 to 1, ease-in-out over ~1.05 s), each row integrates the bend angle along the page so the free edge lags and the top and bottom curl differently:

```js
const CN = 44, CM = 16, curlData = new Float32Array((CN+1)*(CM+1)*6); // xyz + (uFront, v, uBack)
function curlBuild(book, W, H, spineX, topY, k, dir){ // dir: +1 turning forward, -1 back
  const e = k<.5 ? 2*k*k : 1-Math.pow(-2*k+2,2)/2, th = Math.PI*e, sn = Math.sin(th);
  const c = Math.cos(book.rot), s = Math.sin(book.rot), sc = book.s, ds = W/CN; let ptr = 0;
  for(let j=0;j<=CM;j++){ const yn = j/CM, y = yn*H; let X = 0, Z = 0;
    for(let i=0;i<=CN;i++){
      if(i>0){ const m = (i-.5)/CN;
        const ph = Math.min(Math.PI, Math.max(0, th + sn*(-1.05*Math.pow(m,1.5) + 1.1*m*m*(yn-.32))));
        X += Math.cos(ph)*ds; Z += Math.sin(ph)*ds; }
      const si = i/CN*W, ax = spineX + dir*X, ay = topY + y;
      const h0 = 7 + 15*(1-Math.exp(-Math.abs(X)/52));   // pages rise off the stack near the spine
      const lx = (ax-book.cx)*sc, ly = (ay-book.cy)*sc;   // book-local → world
      curlData[ptr++] = book.x + c*lx - s*ly; curlData[ptr++] = book.y + s*lx + c*ly; curlData[ptr++] = (Z+h0+1.2)*sc;
      curlData[ptr++] = (spineX + dir*si)/book.artW; curlData[ptr++] = ay/book.artH; curlData[ptr++] = (spineX - dir*si)/book.artW; } } }
// indices once: for each cell q=j*(CN+1)+i → q,q+1,q+CN+1, q+1,q+CN+2,q+CN+1
```

## Shaders

```glsl
// vertex
#version 300 es
layout(location=0) in vec3 p; layout(location=1) in vec3 u; uniform vec2 cam,res; uniform float S;
out vec3 vu; out float vh;
void main(){ vec2 d=(p.xy-cam)*S+res*.5; vu=u; vh=p.z; gl_Position=vec4(d.x/res.x*2.-1.,1.-d.y/res.y*2.,0.,1.); }

// fragment: writes albedo + height like any object, so it is lit and casts shadows
#version 300 es
precision highp float; in vec3 vu; in float vh;
layout(location=0) out vec4 o0; layout(location=1) out vec4 o1;
uniform sampler2D tA,tPrev,tNext; uniform float ffFront; uniform vec4 inkR;
void main(){ bool front=(ffFront>.5)==gl_FrontFacing; float au=front?vu.x:vu.z; vec2 a=vec2(au,vu.y);
  vec4 A=texture(tA,a); vec2 iu=(a-inkR.xy)/inkR.zw;
  vec4 k=front?texture(tPrev,iu):texture(tNext,iu); A.rgb=k.rgb+A.rgb*(1.-k.a);
  o0=vec4(A.rgb,1.); o1=vec4(vh,.9,0.,1.); }
```

Set `ffFront` from the turn direction so the right face shows the right page whichever way you turn.

## Turning

```js
function turnTo(n){
  if(turn.active || n===spread) return; SND.flip(); found('book');
  if(reduceMotion || !curlProgram){ spread = n; pageApi.render(); return; }   // reduced motion: instant swap
  copyCanvas(pageApi.src, prevCanvas); upload(prevTex, prevCanvas, true);    // freeze the old page
  turn.dir = n > spread ? 1 : -1; spread = n; pageApi.render(); turn.k = 0; turn.active = true; }
// frame: turn.k = min(1, turn.k + dt/1.05); draw the book (old page on the turning side), then the curl
```

Pair it with a page-flip sound (`sound-kit.md`), drive spreads with explicit index state and buttons/keys (never scroll-position math), and give the visitor visible Left page / Right page controls while the book is open.
