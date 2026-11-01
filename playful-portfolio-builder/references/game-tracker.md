# Game tracker, secrets and reward

Read this when building the reason to keep exploring: a way to track progress, the Easter eggs and the reward.

This is a proven default, not the only shape. Any mechanic that suits the world works (stamps filling a passport, stars lighting up in a sky, pages filling a scrapbook, buildings lighting up in a town), as long as progress is visible, the things to find are mostly the person's story, and finishing pays off.

## The default shape

- A glass pill (top-left works well): `✦ 3 of 10 found` (compact `3/10` on phones), with `· 1 secret` once any secret is found.
- Clicking it opens a dropdown with two lists: **Things to find** and **Secrets** (cryptic hints shown as `?` until found, then replaced by what was found).
- **Things to find are mostly the story pieces** (each role, project, award, talk, degree), written as what the visitor did: "Read about the onboarding redesign", "Turned the ID badge over". Finishing the list should mean the visitor has seen the whole career. Pure-fun finds belong in Secrets.
- Each discovery: a chime, the star bumps, and a toast `✦ Found <what> · n of N`.
- Finding every main item plays the **reward** once (a polaroid that drops onto the scene with a thank-you, an unlocked light mode, a hidden room, a song). Choose a reward that is personal to the site's owner.
- Progress is remembered per visitor in localStorage, inside try/catch.
- Hook `found()` into the **real actions** (page turned, object flipped, seal broken, payoff finished), never into hovers.

## Code

```js
const QUEST = {
  main:   [['book','Turned a page of the notebook'], ['badge','Turned the ID badge over'] /* …one per object */],
  secret: [['name','Say my name. Just type it.','Typed my name'] /* [key, hint, label once found] */],
  got:{}, rewarded:false };
const TOUCH = matchMedia('(hover:none)').matches;
if(TOUCH) QUEST.secret[0] = ['name','Tap every flower in the garland.','Woke up the flowers']; // keyboard secret → tap secret
try{ Object.assign(QUEST.got, JSON.parse(localStorage.getItem('site-found-v1')||'{}')); }catch(e){}
QUEST.rewarded = QUEST.main.every(m => QUEST.got[m[0]]);

const mainCount = () => QUEST.main.filter(m => QUEST.got[m[0]]).length;
function found(k){ if(QUEST.got[k]) return; QUEST.got[k] = 1;
  try{ localStorage.setItem('site-found-v1', JSON.stringify(QUEST.got)); }catch(e){}
  renderQuest(); bumpStar();
  const m = QUEST.main.find(x => x[0]===k), s = QUEST.secret.find(x => x[0]===k);
  if(m){ SND.chime(); toast(`<b>✦ Found</b> ${m[1]} · ${mainCount()} of ${QUEST.main.length}`);
    if(mainCount()===QUEST.main.length && !QUEST.rewarded){ QUEST.rewarded = true; setTimeout(startReward, 1600); } }
  if(s) toast(`<b>✦ Secret</b> ${s[2]}`, 3200); }
function renderQuest(){ const n = mainCount(), N = QUEST.main.length;
  questLabel.textContent = n===N ? `All ${N} found` : `${n} of ${N} found`;
  questList.innerHTML = QUEST.main.map(m => `<li class="${QUEST.got[m[0]]?'done':''}"><i>${QUEST.got[m[0]]?'✦':'○'}</i>${m[1]}</li>`).join('');
  secretList.innerHTML = QUEST.secret.map(m => `<li class="${QUEST.got[m[0]]?'done':''}"><i>${QUEST.got[m[0]]?'✦':'?'}</i>${QUEST.got[m[0]]?m[2]:m[1]}</li>`).join(''); }
```

Make the dropdown a proper menu: `aria-expanded` on the button, closes on outside click and Escape, scrolls if tall (`max-height:70vh`).

## Secret patterns that work (adapt, don't copy)

- **Type a word** (the owner's name, a nickname) with a rolling buffer of the last N keys; ignore keys typed into inputs. On touch, swap for a tap secret.
- **Knock N times** on the empty surface within a time window → a time-lapse through every light preset, then back.
- **Clink / tap an object N times** quickly → a burst (bigger steam, a splash, a song).
- **Tap every one of a set** (flowers, keys, stars) → they all hop in a wave with a fanfare.
- **Leave it alone** for a while → the companion falls asleep, the light dims, a small thing happens.

At least three, personal, hidden, every one reachable on touch, each with its own sound and toast.

## Reward and wow moment

The reward (for finding everything) and the big wow moment (the signature payoff) are different. The wow moment should be reachable any time, be tied to the person, and **always be reversible** ("Put it back"). During any sequence, make sure no other per-frame code (a hold pose, a hover lift) fights the animation: gate them on the sequence state.
