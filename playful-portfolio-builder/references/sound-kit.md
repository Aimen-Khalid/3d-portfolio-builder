# Sound kit (procedural Web Audio, no files)

Read this when adding sound. Every action gets a sound that matches what physically happened; everything is synthesised, nothing is loaded.

## Rules

- Oscillators plus shaped, filtered noise for physical sounds. Short envelopes, no constant hiss, everything through a compressor.
- Musical tones for UI and discoveries (chimes, a small fanfare for rewards). A pentatonic theme (kalimba, marimba, music box) turns repeated interactions into a melody.
- Schedule slightly ahead (~10-30 ms). Throttle rapid sounds (typing scratch: one per 40 ms).
- Start the AudioContext on the first gesture. A visible toggle, remembered per visitor in localStorage (try/catch).
- Animal sounds must be believable: a short pitch-bent meow beats a fake purr.

## Engine

```js
const SND = (() => { let ctx=null, out=null, noise=null, on=true;
  try{ if(localStorage.getItem('site-sound')==='off') on=false; }catch(e){}
  function init(){ if(ctx){ if(ctx.state==='suspended') ctx.resume(); return ctx; }
    const C = window.AudioContext||window.webkitAudioContext; if(!C) return null;
    try{ ctx = new C({latencyHint:'interactive'}); }catch(e){ ctx = new C(); }
    const comp = ctx.createDynamicsCompressor(); comp.threshold.value=-16; comp.ratio.value=3.5;
    out = ctx.createGain(); out.connect(comp); comp.connect(ctx.destination);
    // slightly brown noise: softer and more papery than white
    const len = ctx.sampleRate*2, b = ctx.createBuffer(1,len,ctx.sampleRate), d = b.getChannelData(0); let last=0;
    for(let i=0;i<len;i++){ last = last*.6 + (Math.random()*2-1)*.4; d[i] = last*1.6; } noise = b; return ctx; }
  function nz(t0,dur,type,f0,f1,q,g,att){ const s=ctx.createBufferSource(); s.buffer=noise; s.loop=true;
    const f=ctx.createBiquadFilter(); f.type=type; f.Q.value=q||1; f.frequency.setValueAtTime(f0,t0); if(f1) f.frequency.exponentialRampToValueAtTime(f1,t0+dur);
    const gn=ctx.createGain(); gn.gain.setValueAtTime(.0001,t0); gn.gain.exponentialRampToValueAtTime(g,t0+Math.max(.003,att||dur*.3)); gn.gain.exponentialRampToValueAtTime(.0001,t0+dur);
    s.connect(f); f.connect(gn); gn.connect(out); s.start(t0, Math.random()*1.5); s.stop(t0+dur+.05); }
  function tone(t0,dur,f0,f1,g,type){ const o=ctx.createOscillator(); o.type=type||'sine'; o.frequency.setValueAtTime(f0,t0); if(f1) o.frequency.exponentialRampToValueAtTime(f1,t0+dur);
    const gn=ctx.createGain(); gn.gain.setValueAtTime(.0001,t0); gn.gain.exponentialRampToValueAtTime(g,t0+.008); gn.gain.exponentialRampToValueAtTime(.0001,t0+dur);
    o.connect(gn); gn.connect(out); o.start(t0); o.stop(t0+dur+.05); }
  const play = fn => { if(!on || !init()) return; try{ fn(ctx.currentTime+.01); }catch(e){} };
  let lastScratch = 0;
  return { init(){ on && init(); }, isOn(){ return on; },
    toggle(v){ on=v; try{ localStorage.setItem('site-sound', v?'on':'off'); }catch(e){} if(v){ init(); this.tap(); } },
    ...RECIPES(play, nz, tone, () => { const n=performance.now(); if(n-lastScratch<40) return false; lastScratch=n; return true; }) }; })();
addEventListener('pointerdown', () => SND.init(), {once:true, capture:true});
addEventListener('keydown', () => SND.init(), {once:true, capture:true});
```

## Recipes (tuned on a reference build; reuse, retune, add your own)

```js
const RECIPES = (play, nz, tone, scratchOk) => ({
  flip:   () => play(t => { nz(t,.62,'bandpass',600,2400,.6,.30,.22); for(let i=0;i<6;i++) nz(t+.06+Math.random()*.42,.03,'highpass',3200+Math.random()*1500,null,.8,.09,.003); nz(t+.8,.13,'lowpass',520,180,.8,.24,.006); tone(t+.8,.1,150,70,.10); }), // page turn + settle
  card:   () => play(t => { nz(t,.18,'bandpass',1700,3300,1,.22,.03); nz(t+.14,.05,'highpass',2600,null,.7,.13,.004); }),          // card turned over
  paper:  () => play(t => { nz(t,.55,'bandpass',450,1300,.8,.22,.2); for(let i=0;i<3;i++) nz(t+.1+Math.random()*.35,.035,'highpass',3000,null,.8,.07,.004); }),
  seal:   () => play(t => { for(let i=0;i<7;i++) nz(t+i*.021+Math.random()*.012,.028,'highpass',1700+Math.random()*1800,null,1,.30,.002); tone(t,.16,130,52,.22); nz(t+.02,.18,'lowpass',400,120,.7,.2,.01); }), // wax cracking
  lift:   () => play(t => { nz(t,.5,'bandpass',300,1100,.9,.12,.25); tone(t,.45,220,330,.025,'triangle'); }),
  settle: () => play(t => { nz(t,.35,'bandpass',900,300,.9,.10,.1); nz(t+.3,.09,'lowpass',500,160,.8,.18,.005); tone(t+.3,.09,120,65,.09); }),
  pick:   () => play(t => { nz(t,.08,'bandpass',1200,800,1,.12,.01); tone(t,.07,260,330,.035); }),
  drop:   () => play(t => { nz(t,.12,'lowpass',700,200,.8,.25,.006); tone(t,.12,110,60,.15); }),
  tap:    () => play(t => { nz(t,.06,'bandpass',1500,null,1.2,.1,.005); tone(t,.07,520,420,.03,'triangle'); }),
  scratch:() => scratchOk() && play(t => nz(t,.05,'bandpass',3000+Math.random()*1000,null,3,.06,.006)), // pencil while typing
  swell:  () => play(t => { nz(t,1.5,'lowpass',260,1100,.6,.16,.75); tone(t,1.7,196,null,.028); tone(t+.06,1.7,294,null,.02); tone(t+.12,1.7,392,null,.012); }), // light change
  rumble: d  => play(t => { nz(t,d||.8,'lowpass',150,80,1,.55,.06); nz(t,d||.8,'bandpass',900,500,2,.06,.05); }),           // earthquake
  whoosh: () => play(t => nz(t,.5,'bandpass',350+Math.random()*200,1700,1.1,.13,.28)),
  thud:   () => play(t => { nz(t,.1,'lowpass',650,170,.8,.2,.004); tone(t,.1,90+Math.random()*40,58,.11); nz(t+.01,.06,'bandpass',2200,null,3,.05,.004); }),
  creak:  () => play(t => { for(let i=0;i<9;i++) nz(t+i*.055,.065,'bandpass',800+Math.random()*900,null,5,.17,.008); }),    // wicker / wood
  plip:   () => play(t => { tone(t,.16,1100,320,.05); tone(t+.05,.2,700,260,.025); nz(t,.08,'bandpass',1800,600,2,.03,.01); }), // drop into liquid
  clink:  n  => play(t => { const f=2350+(n||0)*180; tone(t,1.1,f,null,.05); tone(t,.8,f*1.51,null,.022); tone(t,.5,f*2.76,null,.012); nz(t,.02,'highpass',5000,null,1,.06,.002); }), // glass; n raises pitch
  knock:  () => play(t => { nz(t,.09,'lowpass',420,140,1,.32,.003); tone(t,.08,150,90,.14); }),                               // knuckle on wood
  chime:  () => play(t => { tone(t,.9,784,null,.045); tone(t+.09,1.1,1175,null,.035); tone(t+.18,1.3,1568,null,.02); }),        // discovery
  fanfare:() => play(t => { [523,659,784,1047,1319].forEach((f,i)=>{ tone(t+i*.11,1.4,f,null,.04); tone(t+i*.11,1,f*2,null,.01); }); nz(t+.5,1.2,'highpass',5000,9000,.5,.03,.6); }), // reward
  pop:    () => play(t => { tone(t,.2,330,780,.08,'triangle'); tone(t+.05,.25,660,990,.03); nz(t+.02,.45,'bandpass',700,2100,.8,.17,.12); }), // something rises out
});
```

Match recipes to the real material: a wooden drawer slides (lowpassed noise sweep + soft thud), a ceramic cup clinks lower than glass, a balloon squeaks (pitch-bent triangle), a jelly plops (low sine with fast downward bend).
