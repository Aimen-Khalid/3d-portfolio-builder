You are executing one run of a skill evaluation. Do the task exactly as a real assistant using the skill would.

- Skill path: /mnt/skills/plugins/playful-portfolio-builder — read its SKILL.md first and follow it end to end, including its reference files and scripts (deal.mjs etc.) at the steps where it says to read them.
- Task (the user's message):
"""
{PROMPT}
"""
- Input files: none
- Save outputs to: {OUT}

Eval conditions (these override the skill only where they conflict):
1. The user is not available to answer. Follow the skill's unattended path. Every time the skill tells you to ask or tell the user something, append the exact message you would have sent to outputs/questions.md, followed by "ASSUMED ANSWER:" and the answer you assumed, then carry on. Never invent personal facts as assumed answers — if the user would have supplied content, assume they had nothing more to give. Where a choice is offered (e.g. which world), pick the one you'd recommend and say so.
2. Do NOT publish artifacts, deploy, use any connector, send messages or notifications, or touch memory. Where the skill says publish/republish an artifact, skip it and note "would publish here" in notes.md.
3. The machine is shared with other eval runs and has only 2 CPUs and 7 GB RAM. Run at most ONE headless browser at a time and close it promptly.
4. Tooling that works: Python Playwright with Chromium; for WebGL launch with args ["--use-gl=swiftshader","--enable-webgl","--ignore-gpu-blocklist"]. CDNs (cdnjs, jsdelivr, unpkg) and npm/pip are reachable. Do scratch work in outputs/work/.
5. LIGHTER VERIFICATION (time budget for this eval — software rendering is slow here). Keep every verification step the skill requires, but lighter:
   - Use reduced render quality (e.g. a debug URL param that sets pixel ratio 0.5 and disables antialiasing) for the walkthrough and intermediate screenshots; use full quality only for final hero screenshots and the flicker audit.
   - Flicker audit: the default view in each light preset plus one close-up/held view.
   - Real-visitor walkthrough: hover, click, flip and close (button, Escape, outside click) every object; play the game to the end with real input; trigger every Easter egg once; run the wow moment and Put it back. Mobile 390x844 touch pass: one object of each kind, the controls, one secret and the wow moment. If time forces a cut, keep the above core and note exactly what was cut.
   - Wow review: at most 2 rounds in total (the first review plus one round aimed at the signature moment).
6. Required outputs in outputs/: index.html (the final self-contained site); screens/ with at least screens/hero-desktop.png (1440x900 default view) and screens/hero-mobile.png (390x844), plus the verification screenshots; notes.md containing: the dealt hand + seed, the inventory, the idea sentence, the concept sheet, a "Composition fingerprint" section with exactly five lines (Camera:, Ground:, Movement:, Time:, Look:), the real-visitor walkthrough log (pass/fail per step, and anything cut), flicker-audit results per view (% flagged), wow-review scores per item and total for each round, and the self-check; final_message.md with what you would say to the user at handover.
7. When finished, reply with a short summary: world name, category, the five fingerprint lines, final wow score, worst flicker %, and anything that failed, was cut or skipped.
