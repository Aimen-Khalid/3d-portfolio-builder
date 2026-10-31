# HTML-in-Canvas: live HTML drawn into the scene

Read this when content should **live on an object** (pages, letters, cards, tickets, screens, forms) and be lit, shadowed and distorted like that object, while staying real DOM for text selection, typing, links and screen readers.

## The three parts

1. **Native path** (when the browser supports it): a `<canvas layoutsubtree>` holds the element; in its `paint` event call `ctx.drawElementImage(el, …)`, upload the canvas as a texture, and call `requestPaint()` when content changes. Feature-detect `'drawElementImage' in CanvasRenderingContext2D.prototype`. It may need an origin-trial token, so never rely on it alone.
2. **SVG `<foreignObject>` fallback** (what most visitors see): clone the element, serialise it into an SVG with embedded fonts (base64 `@font-face`, since the SVG cannot load external fonts) and `*{box-sizing:border-box}`, draw it to an offscreen canvas, upload. Re-snapshot on input and changes. Swap form controls in the clone for styled divs showing their values plus a fake blinking caret.
3. **DOM proxy**: the real element sits in an invisible layer (`opacity:.001`), transformed every frame to lie exactly over the object on screen, so clicks, focus and typing hit real elements. Make it interactive (`pointer-events:auto`) only while that object is focused.

## Code

```js
const proto = window.CanvasRenderingContext2D && CanvasRenderingContext2D.prototype;
const NATIVE = !!(proto && 'drawElementImage' in proto);
// obj.art.ink = {x,y,w,h (uv rect on the object), pw,ph (CSS px size of the content)}
function surface(obj, html, onBind){
  const {pw, ph} = obj.art.ink; let el, wrap, cv = null;
  const off = Object.assign(document.createElement('canvas'), {width:pw*2, height:ph*2}), oc = off.getContext('2d');
  obj.inkTex = tex();
  if(NATIVE){ cv = Object.assign(document.createElement('canvas'), {width:pw*2, height:ph*2});
    cv.style.width = pw+'px'; cv.style.height = ph+'px'; cv.setAttribute('layoutsubtree',''); cv.className='proxy'; wrap = cv; }
  else { wrap = document.createElement('div'); wrap.className = 'proxy ghost'; wrap.style.width = pw+'px'; wrap.style.height = ph+'px'; }
  proxies.appendChild(wrap);
  const api = { wrap, obj, focusEl:null, caret:true, src: NATIVE ? cv : off,
    render(){ // keep focus across re-renders
      const foc = wrap.contains(document.activeElement) ? document.activeElement.id : null;
      wrap.innerHTML = html(); el = wrap.firstElementChild; if(NATIVE) el.setAttribute('drawable','');
      onBind(el, api); api.paint();
      if(foc){ const f = wrap.querySelector('#'+foc); f && f.focus({preventScroll:true}); } },
    paint(){ NATIVE ? cv.requestPaint?.() : snap(); } };
  if(NATIVE){ const cx = cv.getContext('2d');
    cv.addEventListener('paint', () => { try{ cx.reset(); cx.drawElementImage(el,0,0,pw*2,ph*2); upload(obj.inkTex,cv,true); }catch(e){ console.warn(e); } }); }
  let busy = false, again = false;
  function snap(){ if(busy){ again = true; return; } busy = true;
    const cl = el.cloneNode(true), src = el.querySelectorAll('input,textarea'), dst = cl.querySelectorAll('input,textarea');
    src.forEach((f,i) => { const d = document.createElement('div'), empty = !f.value;
      d.className = 'fld' + (empty ? ' ph' : ''); d.textContent = empty ? f.placeholder : f.value;
      if(api.focusEl === f && api.caret){ const c = document.createElement('span');
        c.setAttribute('style','display:inline-block;width:2px;height:.9em;vertical-align:-.1em;background:currentColor;margin-left:1px');
        if(empty){ d.textContent=''; d.append(c, f.placeholder); } else d.append(c); }
      dst[i].replaceWith(d); });
    cl.querySelectorAll('button').forEach(b => { const d = document.createElement('div'); d.className = b.className; d.innerHTML = b.innerHTML;
      ['aria-pressed','aria-selected'].forEach(a => b.hasAttribute(a) && d.setAttribute(a, b.getAttribute(a))); b.replaceWith(d); });
    const xml = new XMLSerializer().serializeToString(cl);
    const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${pw*2}" height="${ph*2}" viewBox="0 0 ${pw} ${ph}"><style>${FONTS_CSS}*{box-sizing:border-box}${PAGE_CSS}${CLONE_CSS}</style><foreignObject width="${pw}" height="${ph}">${xml}</foreignObject></svg>`;
    const img = new Image();
    img.onload = () => { oc.clearRect(0,0,off.width,off.height); oc.drawImage(img,0,0,off.width,off.height); upload(obj.inkTex,off,true); busy=false; if(again){ again=false; snap(); } };
    img.onerror = () => { busy = false; };
    img.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg); }
  if(!NATIVE) setInterval(() => { if(api.focusEl){ api.caret = !api.caret; snap(); } }, 530);
  api.render(); return api; }

function bindFields(el, api){ el.querySelectorAll('input,textarea').forEach(f => {
  f.addEventListener('input', () => { api.paint(); SND.scratch(); });   // pencil scratch while typing
  f.addEventListener('focus', () => { api.focusEl = f; api.caret = true; api.paint(); });
  f.addEventListener('blur',  () => { if(api.focusEl === f) api.focusEl = null; api.paint(); }); }); }

// every frame: keep the real DOM exactly over the object
function placeProxy(api){ const o = api.obj, k = o.art.ink, W = o.art.w, H = o.art.hh, z = worldToPx;
  const p = toScreen(o.x, o.y), pv = o.piv || [W/2, H/2];
  api.wrap.style.transform = `translate(${p[0]}px,${p[1]}px) rotate(${o.rot}rad) scale(${o.s*o.sx*z},${o.s*o.sy*z}) translate(${k.x*W-pv[0]}px,${k.y*H-pv[1]}px)`; }
```

In the object shader, composite the content over the surface inside the ink rect (see `engine-lighting.md`). Sample it at `uv + off` so material effects bend the live text along with the surface.

## Gotchas (each one cost a round of feedback)

- `CLONE_CSS` must style the divs that replace buttons and fields exactly like the originals, or the texture and the live DOM disagree.
- Embed every font you use as base64 `@font-face` in `FONTS_CSS`; also register them with `FontFace` and wait for `document.fonts` before the first snapshot, or the first texture renders in a fallback font.
- Snapshots are async. Queue one re-snapshot while busy (`again`) instead of firing many.
- Draw content at 2x the CSS size so small type stays crisp when the object is held close.
- For a page turn, copy the current content canvas to a "previous" texture before re-rendering, so the turning sheet can show the old page on its front (see `page-curl.md`).

## Go beyond static text

Ask what this surface really is and make the content behave like it: ink that bleeds while you type on paper, a form on a visitor badge that fills in your own name, a phone screen that plays, a stamp that presses into a card, frosted glass that clears where you hover. Material rules are in `material-effects.md`.
