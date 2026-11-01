"""Programmatic checks for a portfolio build run.
Usage: python3 checks.py <case-name> <run-dir>   -> writes <run-dir>/auto_checks.json
Run one at a time (shared 2-CPU machine)."""
import json, os, re, sys, html, unicodedata
from playwright.sync_api import sync_playwright

ARGS = ["--use-gl=swiftshader", "--enable-webgl", "--ignore-gpu-blocklist"]

VERBATIM = {
  "pasted-content-verbatim": [
    "I started writing code at fourteen on a hand-me-down Pentium that crashed whenever the fan got dusty.",
    "Twelve years later I lead the platform team at labcraft, where we keep 3,400 science simulations running for students in 60 countries.",
    "I care about boring infrastructure, honest estimates, and leaving every codebase a little kinder than I found it.",
    "Mariam doesn't just fix the outage — she writes the doc so it never happens again.",
    "The calmest person in any incident channel. Genuinely.",
    "She taught our whole team to love on-call, which I did not think was possible.",
    "Asad Raza", "Tom Becker", "Priya Nair",
  ],
  "pastry-chef-photographer": [
    "Nadia makes bread look like a sunrise.",
    "She understands food because she's made it.",
    "Every single shot was usable.",
    "Omar Farooq", "Leila Haddad", "Sami Khan",
  ],
}
FORBIDDEN = {"must-not-show-employer": ["northgate", "nust"]}


def norm(s):
    s = html.unescape(s)
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("&#39;", "'")
    return re.sub(r"\s+", " ", s)


def parse_notes(notes):
    fp = {}
    for k in ("Camera", "Ground", "Movement", "Time", "Look"):
        m = re.search(rf"^\W*{k}\W*:\s*(.+)$", notes, re.M | re.I)
        fp[k.lower()] = m.group(1).strip() if m else None
    pcts = [float(x) for x in re.findall(r"(\d+(?:\.\d+)?)\s*%", notes[notes.lower().find("flicker"):] if "flicker" in notes.lower() else "")]
    return fp, pcts


def main(case, run):
    out = os.path.join(run, "outputs")
    res = {"case": case, "run": run}
    idx = os.path.join(out, "index.html")
    res["index_exists"] = os.path.exists(idx)
    src = open(idx, encoding="utf-8", errors="ignore").read() if res["index_exists"] else ""
    res["index_kb"] = round(len(src.encode()) / 1024)
    nsrc = norm(src)
    if case in VERBATIM:
        res["verbatim"] = {s: (norm(s) in nsrc) for s in VERBATIM[case]}
    if case in FORBIDDEN:
        res["forbidden_hits"] = {s: len(re.findall(s, src, re.I)) for s in FORBIDDEN[case]}
    notes_p = os.path.join(out, "notes.md")
    notes = open(notes_p, errors="ignore").read() if os.path.exists(notes_p) else ""
    res["notes_exists"] = bool(notes)
    res["fingerprint"], pcts = parse_notes(notes)
    res["flicker_pcts_in_notes"] = pcts[:40]
    if res["index_exists"]:
        with sync_playwright() as p:
            b = p.chromium.launch(args=ARGS)
            for label, vp, touch in (("desktop", (1440, 900), False), ("mobile", (390, 844), True)):
                ctx = b.new_context(viewport={"width": vp[0], "height": vp[1]}, has_touch=touch, is_mobile=touch)
                pg = ctx.new_page()
                errs = []
                pg.on("console", lambda m, e=errs: e.append(m.text[:200]) if m.type == "error" else None)
                pg.on("pageerror", lambda x, e=errs: e.append("pageerror: " + str(x)[:200]))
                try:
                    pg.goto("file://" + os.path.abspath(idx), wait_until="load", timeout=90000)
                    pg.wait_for_timeout(6000)
                    info = pg.evaluate("""() => ({
                        hscroll: document.documentElement.scrollWidth > window.innerWidth + 1,
                        canvases: document.querySelectorAll('canvas').length,
                        webgl: [...document.querySelectorAll('canvas')].some(c => { try { return !!(c.getContext('webgl2')||c.getContext('webgl')) } catch(e){ return false } }),
                        textLen: document.body.innerText.length,
                        hasSite: typeof window.__site !== 'undefined'
                    })""")
                except Exception as ex:
                    info = {"load_error": str(ex)[:200]}
                info["console_errors"] = errs[:10]
                res[label] = info
                ctx.close()
            b.close()
    json.dump(res, open(os.path.join(run, "auto_checks.json"), "w"), indent=2, ensure_ascii=False)
    print(json.dumps({k: res[k] for k in res if k not in ("verbatim",)}, ensure_ascii=False)[:1500])
    if "verbatim" in res:
        print("verbatim:", sum(res["verbatim"].values()), "/", len(res["verbatim"]))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
