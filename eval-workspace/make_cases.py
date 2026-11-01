"""Generate eval case folders (evals/) and iteration-1 eval_metadata.json for playful-portfolio-builder."""
import json, os, textwrap

ROOT = os.path.dirname(os.path.abspath(__file__))
EVALS = os.path.join(ROOT, "evals")
IT = os.path.join(ROOT, "iteration-1")

SETTINGS = """---
tags: [skill-creator, playful-portfolio-builder]
max_turns: 400
timeout_seconds: 10800
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

"""

BUILD_COMMON = [
    "The final site is one self-contained index.html that loads in headless Chromium with no console errors",
    "The site has real light and depth (WebGL 3D or a lit canvas scene with shadows), not a flat or CSS-only layout",
    "Every role, project, award, talk and degree given in the prompt has its own object, place or section in the site",
    "The site has a visible discovery game or tracker whose finds are mostly story pieces, with a reward for finding everything",
    "The site has at least three hidden Easter eggs, each with a touch-device trigger",
    "The site has a light or mood control with at least two presets",
    "The site has sound with a visible on/off toggle",
    "The site has a plain, readable fallback page containing all the person's content",
    "The site invents no achievement, number, quote, employer or credential that the prompt did not give",
    "At 390x844 the site has no horizontal scroll and its controls fit on screen",
    "The run's notes report a flicker audit with under 0.05% flagged pixels in every audited view",
    "The run's notes report a real-visitor walkthrough with real mouse/keyboard/touch input, all steps passing",
    "The run's notes report a wow-review score of at least 15/18",
]

NOT_DEFAULT = "The world is not one of the skill's listed defaults (floating disc island, isometric room cutaway, top-down desk, bookshelf of project books, planet with buildings) unless the notes justify it from the person's own inventory"

CASES = [
 dict(name="fintech-backend-engineer", kind="build", runs=3, baseline=True,
  outcome="A playful, physical-feeling portfolio built from Hamza's own inventory (keyboards, dawn rides on Sea View, Karachi fintech). Three independent runs should produce clearly different worlds.",
  prompt="""I'm Hamza Siddiqui, a senior backend engineer with 8 years in fintech, based in Karachi. Roles: Backend Engineer at Paysphere (2017–2020), Senior Engineer at Ledgerly (2020–2023), Lead Backend Engineer at Tolly Bank (2023–now). Biggest projects: cut our payment API's p99 latency by 40% at Ledgerly, and led the migration of 2 million accounts to a new ledger at Tolly Bank with zero downtime. I gave a talk at PyCon Pakistan 2024 called "Idempotency at scale". Outside work I collect mechanical keyboards (14 so far) and cycle along Sea View at dawn on weekends. Make me a portfolio that's fun to explore. You decide the rest.""",
  extra=[NOT_DEFAULT]),
 dict(name="fresh-grad-thin-content", kind="build", baseline=True,
  outcome="A complete, delightful site built only from the little Hira gave; nothing invented; the content check offers optional additions without blocking.",
  prompt="""hi i just graduated (BS CS from FAST Lahore, 2026). i did one internship at a small startup called Brightloom for 3 months doing react stuff, and my final year project was a sign language to text app using mediapipe. i don't have a photo or awards or anything. i don't have much but i want something cool for my portfolio. my name is Hira Baig""",
  extra=["The site shows no awards, metrics, testimonials, photo or extra jobs that Hira did not give",
         "The site still feels complete and rich despite thin content (judged from screenshots)",
         "The run's questions/messages include a content check that offers optional additions and says it is fine not to have them"]),
 dict(name="pastry-chef-photographer", kind="build", baseline=True,
  outcome="A non-tech portfolio whose materials and effects make sense for food and photography; testimonials quoted exactly.",
  prompt="""I'm Nadia Rahman. I spent 7 years as a pastry chef — Sugar & Salt in Lahore (2014–2018), then head pastry chef at Maison Lumière in Dubai (2018–2021). Since 2021 I've been a food photographer. I shot the cookbook "Flour Moons" (2023, 120 recipes) and Gulf Food Magazine put me in their "30 to Watch" list in 2024.

Some things clients said:
"Nadia makes bread look like a sunrise." — Omar Farooq, owner, Crumb Bakery
"She understands food because she's made it." — Leila Haddad, editor, Flour Moons
"Every single shot was usable." — Sami Khan, marketing lead, Karak House

I love early morning light in a kitchen. Build my portfolio, surprise me.""",
  extra=["All three testimonials appear word for word with the exact name, role and company given",
         "Hover/touch effects suit their materials (e.g. dough, flour, paper prints, liquid), per the run's notes and screenshots"]),
 dict(name="architect-avoids-room-default", kind="build", baseline=True,
  outcome="An architect's portfolio that resists the obvious room-cutaway or desk default and is built from Zain's own habits.",
  prompt="""I'm Zain Malik, an architect with 12 years of practice. Five built projects I'm proud of: Ravi Riverside Library (2016), Gulberg Courtyard House (2018), Thar Solar School (2020 — won Gold at the Pakistan Green Building Awards 2021), Hunza Guest Lodge (2022) and Model Town Clinic (2024). I sketch every building in pencil first, always in a grey Moleskine. My visitors are clients and competition juries. Make my portfolio something they explore, not scroll past.""",
  extra=["All five buildings and the Gold award each have their own object or place", NOT_DEFAULT]),
 dict(name="sound-designer", kind="build", baseline=True,
  outcome="A portfolio where sound is the centre of the experience, built from Ayesha's field recordings and credits.",
  prompt="""I'm Ayesha Noor, a sound designer and composer for games. Credits: audio lead on the mobile game "Kite Rush" (5 million downloads), sound design for the indie game "Moth & Lantern" (nominated for Best Audio at the Pakistan Game Awards 2025), and the score for the short film "Rain on Anarkali" (2023). I record field sounds around Lahore — rickshaws, rain on tin roofs, the pigeons at Badshahi Mosque. Make me a portfolio people play with.""",
  extra=["Sound is central to the experience (e.g. her recordings or credits are playable or drive the world), not only UI click sounds",
         "All three credits and the nomination each have their own object or place"]),
 dict(name="pm-recruiter-scannable", kind="build", baseline=True,
  outcome="A scrolling page with objects (category 8): real HTML text that scans in 30 seconds, one distinct 3D object per section, no scroll hijacking.",
  prompt="""I'm Daniyal Ahmed, a product manager with 6 years of experience. Senior PM at Carely (2022–now): launched our teleconsult product and grew weekly active users from 40k to 310k. PM at Shiftly (2019–2022): built shift scheduling used by 1,200 restaurants and cut churn by 18%. I'm a Certified Scrum Product Owner. Hiring managers will skim this in 30 seconds. Make it special but easy to read.""",
  extra=["The site is a readable scrolling page: headings and body copy are real HTML text, with a nav of anchors to each section",
         "Each section has its own interactive 3D object, and neighbouring sections never reuse the same object or mechanic",
         "Dragging objects does not trap vertical page scroll, and offscreen sections' render loops are paused",
         "A hiring manager can see roles, employers and the two biggest results without clicking anything"]),
 dict(name="two-people-same-chat", kind="build",
  outcome="Two sites built in one conversation; the second is not a reskin of the first.",
  prompt="""Make me a portfolio. I'm Sara Iqbal, a data scientist (5 years). Data Scientist at Retailytics (2021–now): built a demand-forecasting model that cut stock-outs by 30% across 220 stores. Analyst at Northwind Telecom (2019–2021). MSc Statistics, Punjab University. I bake sourdough and run a small book club. You decide everything.

[After the first site is finished, the user's next message is:]
Love it! Now make one for my colleague Bilal Khan. He's a mobile developer (6 years): Android Lead at Rideo (2022–now), shipped the driver app used by 80,000 drivers; Mobile Developer at Tapstack (2018–2022). He plays cricket on Sundays and restores old radios.""",
  extra=["Second site's composition fingerprint (camera, ground, movement, time, look) differs from the first site's on at least 3 of 5 axes",
         "Second site reuses none of the first site's objects, arrangement or wow moment",
         "The run suggests starting a fresh chat for the second person, as the skill instructs"]),
 dict(name="clone-reference-site", kind="build",
  outcome="The run takes techniques or feelings from the referenced site but does not clone its world, layout or signature mechanic.",
  prompt="""Make me a portfolio exactly like Bruno Simon's site (bruno-simon.com), the one where you drive a little car around the 3D world and knock things over. I'm Omar Javed, frontend engineer at Pixelwell for 4 years; I built their design system, now used by 30 engineers across 5 products. Before that I was a junior dev at Webnest (2019–2021). I make my own cold brew and keep a sourdough starter called Gerald.""",
  extra=["The run tells the user it will borrow techniques or feelings from the reference rather than copy it",
         "The site's main mechanic is not driving a vehicle around an open 3D playground"]),
 dict(name="pasted-content-verbatim", kind="build",
  outcome="Pasted bio and quotes appear word for word, with spelling, punctuation and lowercase brand untouched.",
  prompt="""Build my portfolio. I'm Mariam Sheikh. Here's my bio:

I started writing code at fourteen on a hand-me-down Pentium that crashed whenever the fan got dusty. Twelve years later I lead the platform team at labcraft, where we keep 3,400 science simulations running for students in 60 countries. I care about boring infrastructure, honest estimates, and leaving every codebase a little kinder than I found it.

And some things people have said:

"Mariam doesn't just fix the outage — she writes the doc so it never happens again." — Asad Raza, VP Engineering, labcraft
"The calmest person in any incident channel. Genuinely." — Tom Becker, Staff Engineer, labcraft
"She taught our whole team to love on-call, which I did not think was possible." — Priya Nair, Engineering Manager, Opentrail""",
  extra=["The bio paragraph appears word for word (only formatting changed), including the lowercase 'labcraft'",
         "All three quotes appear word for word with their exact attributions"]),
 dict(name="sister-attribution", kind="build",
  outcome="The site is Fatima's; her father's school and her cousin's shop are attributed correctly.",
  prompt="""Build a portfolio for my younger sister, Fatima Zafar. Here's her CV:

Fatima Zafar
- BS Biotechnology, Kinnaird College (2025)
- Research Assistant, Plant Genomics Lab, Kinnaird College (2024–2025): co-authored a poster on drought-tolerant wheat
- Volunteers teaching science at Zafar Model School (our father's school — he founded it in 1998)
- Runs social media for Petal & Pot, our cousin Hina's plant shop
- 2nd place, Punjab Young Scientists Fair 2023""",
  extra=["Zafar Model School is presented as her father's school where she volunteers, never as hers or as one she founded",
         "Petal & Pot is presented as cousin Hina's shop that Fatima helps with, never as Fatima's business",
         "The site is written about Fatima, not about the person who asked for it"]),
 dict(name="must-not-show-employer", kind="build",
  outcome="The current employer and the university appear nowhere in the delivered site, including metadata and code.",
  prompt="""I'm Usman Tariq, a security engineer. Please don't show my current employer or my university anywhere on the site.

CV: Security Engineer at Northgate Systems (2023–now): built our bug bounty program, 140 valid reports in its first year. Penetration Tester at RedKite Labs (2020–2023). BS Computer Science, NUST (2020). OSCP certified. Found a critical bug in a popular open-source PDF library and was credited in its 2024 release notes. I play chess (1900 on lichess).""",
  extra=["The strings 'Northgate' and 'NUST' do not appear anywhere in index.html (text, alt text, metadata, comments or scripts)",
         "The bug bounty program, RedKite Labs role, OSCP and the PDF-library credit are each present"]),
 dict(name="bare-trigger-asks-one-question", kind="first-turn",
  outcome="The first reply asks one question about who the portfolio is for or about the person, does not ask for a theme, and does not start building.",
  prompt="Make me a 3D portfolio.",
  graders=["The first reply asks exactly one question",
           "The first reply does not ask the user to pick a theme, metaphor, concept or category",
           "The first reply does not start building or propose worlds yet"]),
 dict(name="unattended-build", kind="build",
  outcome="A complete site built without stalling, with the assumptions stated at the top of the handover.",
  prompt="""I'm Rabia Hassan, a UX designer (7 years). Designer at Tiffin (2018–2021), Senior UX Designer at Bazaar Lane (2021–now), where I redesigned checkout and conversion went up 22%. I speak at UXPK meetups. I do pottery on weekends. I'll be away all day — make all the choices yourself and have it ready when I'm back.""",
  extra=["The handover message states the choices/assumptions made, at the top",
         "The run never stops to wait on a question; it completes the site"]),
 dict(name="feedback-round", kind="feedback",
  outcome="Each requested change is applied precisely, nothing else breaks, and the walkthrough is re-run for what changed.",
  prompt="""[Continuing after the unattended-build site was handed over. The user's message:]
The darkest light setting is too dark, I can barely see anything. The sounds are a bit loud. And add my new award: UXPK Designer of the Year 2026.""",
  graders=["The darkest light preset is measurably brighter than before (mean luminance of its screenshot increased)",
           "Sound levels are reduced (master gain or per-sound gains lowered) and the toggle still works",
           "UXPK Designer of the Year 2026 has its own object or place and is counted in the discovery game",
           "Nothing else regressed: no console errors and other objects still open and close",
           "The run's notes report re-running the real-visitor walkthrough for the changed parts"]),
 dict(name="deploy-asks-first", kind="deploy",
  outcome="The run offers Netlify, checks the connector, and asks for the site name and confirmation before creating anything.",
  prompt="""[Continuing after the pastry-chef-photographer site was handed over. The user's message:]
It's final, put it online.""",
  graders=["The run checks whether a Netlify connector is available before deploying",
           "The run asks the user what the site name should be before creating the site",
           "The run does not create or deploy a site without the user's confirmation"]),
 dict(name="no-trigger-plain-resume-site", kind="trigger",
  outcome="Plain minimal site requested; the playful skill should not be used (or, if considered, the run checks with the user first).",
  prompt="""can you make me a simple one-page resume website? plain and minimal, black text on white, no animations. I'm Ali Raza, a QA engineer, 3 years at Testwise, ISTQB certified.""",
  graders=["The run does not load the playful-portfolio-builder skill (or, if it does, it asks the user before building anything playful)",
           "The delivered page is plain and minimal with no 3D, animation or game"]),
 dict(name="no-trigger-copy-review", kind="trigger",
  outcome="A copy review request; no site is built and the playful skill is not used.",
  prompt="""Can you review the copy on my portfolio's About section? Be blunt.

"Hi! I'm Sana. I'm a passionate full-stack developer who loves building things. I have experience in many technologies and I'm always learning. I'm a team player and a quick learner. Let's build something amazing together!\"""",
  graders=["The run does not load the playful-portfolio-builder skill",
           "The run gives a direct critique of the copy rather than building a site"]),
 dict(name="no-trigger-product-configurator", kind="trigger",
  outcome="A 3D product configurator for a brand is not a portfolio; the playful skill is not used.",
  prompt="""Build a 3D product configurator for our sneaker brand Stridewell: users rotate the shoe, pick sole and lace colours, and see the price update. Single HTML file.""",
  graders=["The run does not load the playful-portfolio-builder skill",
           "The run builds a configurator (rotate shoe, choose colours, price updates) rather than a portfolio"]),
]


def w(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(text)


def main():
    index = []
    for c in CASES:
        graders = c.get("graders") or (BUILD_COMMON + c.get("extra", []))
        d = os.path.join(EVALS, c["name"])
        w(os.path.join(d, "prompt.md"), SETTINGS + c["prompt"].strip() + "\n")
        w(os.path.join(d, "case.yaml"),
          f'schema_version: "1.1"\nname: {c["name"]}\nexpected_outcome: |\n' +
          textwrap.indent(c["outcome"], "  ") + "\n")
        for i, g in enumerate(graders, 1):
            slug = "-".join("".join(ch if ch.isalnum() else " " for ch in g.lower()).split()[:5])
            w(os.path.join(d, "graders", f"{i:02d}-{slug}.md"),
              f"---\ntype: llm\nfocus: trace\nweight: 1\n---\n\n{g}\n")
        w(os.path.join(IT, c["name"], "eval_metadata.json"),
          json.dumps({"eval_name": c["name"], "prompt": c["prompt"].strip(), "assertions": graders}, indent=2))
        index.append({k: c.get(k) for k in ("name", "kind", "runs", "baseline")})
    w(os.path.join(ROOT, "cases_index.json"), json.dumps(index, indent=2))
    print(len(CASES), "cases written")


if __name__ == "__main__":
    main()
