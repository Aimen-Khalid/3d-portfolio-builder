// Flicker audit for playful-portfolio-builder sites.
// Usage: node flicker-audit.js path/to/index.html '[{"name":"overview","cam":[30,20,30],"light":"day"},{"name":"walk-1","walk":[x,z,heading]}]'
// Needs playwright (Chromium) and a local three.js in ./node_modules/three if the page loads three from jsDelivr.
// The page must expose window.__site with pause(bool), step(dt,n), light(key), walk(bool) and _three() -> { renderer, scene, camera, THREE, player, walk }.
// It freezes time, nudges the camera by sub-millimetre steps over 14 renders, and flags pixels that flip back and forth (z-fighting / sort popping).
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
const NM = path.join(process.cwd(), 'node_modules/three');
(async () => {
  const [W, H] = [960, 600];
  const browser = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  const page = await browser.newPage({ viewport: { width: W, height: H } });
  if (fs.existsSync(NM)) await page.route(/cdn\.jsdelivr\.net\/npm\/three@[^/]+\//, r => r.fulfill({ path: path.join(NM, r.request().url().replace(/^.*three@[^/]+\//, '')), contentType: 'application/javascript' }));
  await page.goto('file://' + path.resolve(process.argv[2] || 'index.html'));
  await page.waitForFunction(() => window.__site && document.body.classList.contains('ready'), null, { timeout: 60000 });
  await page.evaluate(() => { __site.pause(true); __site.step(1 / 30, 30); });
  const views = JSON.parse(process.argv[3] || '[]');
  const report = [];
  for (const v of views) {
    const res = await page.evaluate(async v => {
      const { renderer, scene, camera, THREE } = __site._three();
      if (v.light) __site.light(v.light);
      if (v.walk) { __site.walk(true); __site.step(1 / 30, 50); const { player, walk } = __site._three(); player.position.set(v.walk[0], 0, v.walk[1]); walk.h = v.walk[2]; walk.camK = 1; __site.step(1 / 30, 2); }
      else if (v.cam) { __site.walk(false); camera.position.set(...v.cam); camera.lookAt(0, .5, 0); }
      const gl = renderer.getContext(), w = gl.drawingBufferWidth, h = gl.drawingBufferHeight;
      const N = 14, frames = [], base = camera.position.clone(), q = camera.quaternion.clone();
      for (let i = 0; i < N; i++) {
        camera.position.copy(base).add(new THREE.Vector3(i * .0007, i * .0004, -i * .0005)); camera.quaternion.copy(q); camera.updateMatrixWorld();
        renderer.render(scene, camera);
        const px = new Uint8Array(w * h * 4); gl.readPixels(0, 0, w, h, gl.RGBA, gl.UNSIGNED_BYTE, px);
        const L = new Uint8Array(w * h); for (let p = 0; p < w * h; p++) L[p] = (px[p * 4] * 3 + px[p * 4 + 1] * 6 + px[p * 4 + 2]) / 10; frames.push(L);
      }
      const flag = new Uint8Array(w * h); let count = 0;
      for (let p = 0; p < w * h; p++) {
        let rev = 0, last = 0;
        for (let i = 1; i < N; i++) { const d = frames[i][p] - frames[i - 1][p]; if (Math.abs(d) < 30) continue; const sgn = Math.sign(d); if (last && sgn !== last) rev++; last = sgn; }
        if (rev >= 3) { flag[p] = 1; count++; }
      }
      // name the objects under flagged pixels
      const ray = new THREE.Raycaster(), hits = {};
      for (let p = 0, k = 0; p < w * h && k < 400; p += 37) if (flag[p]) {
        k++; const x = p % w, y = (p / w) | 0; ray.setFromCamera(new THREE.Vector2(x / w * 2 - 1, y / h * 2 - 1), camera);
        const hit = ray.intersectObjects(scene.children, true).find(o => o.object.visible && o.object.isMesh);
        if (hit) { const o = hit.object; const key = (o.userData.lm || '?') + ':' + o.geometry.type + ':' + (o.material.name || o.material.type) + '@' + o.position.toArray().map(n => n.toFixed(2)).join(','); hits[key] = (hits[key] || 0) + 1; }
      }
      // heatmap
      const c = document.createElement('canvas'); c.width = w; c.height = h; const x = c.getContext('2d'); const id = x.createImageData(w, h);
      for (let p = 0; p < w * h; p++) { const yy = h - 1 - ((p / w) | 0), xx = p % w, o = (yy * w + xx) * 4, l = frames[0][p]; id.data[o] = flag[p] ? 255 : l * .5; id.data[o + 1] = flag[p] ? 0 : l * .5; id.data[o + 2] = flag[p] ? 0 : l * .5; id.data[o + 3] = 255; }
      x.putImageData(id, 0, 0);
      return { count, pct: +(count / (w * h) * 100).toFixed(3), hits: Object.entries(hits).sort((a, b) => b[1] - a[1]).slice(0, 12), png: c.toDataURL() };
    }, v);
    fs.mkdirSync('audit', { recursive: true }); fs.writeFileSync(`audit/${v.name}.png`, Buffer.from(res.png.split(',')[1], 'base64'));
    report.push({ view: v.name, flickerPixels: res.count, pct: res.pct, culprits: res.hits });
  }
  console.log(JSON.stringify(report, null, 1));
  await browser.close();
})();
