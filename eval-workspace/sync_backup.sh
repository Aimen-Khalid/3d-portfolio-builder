#!/usr/bin/env bash
# Back up eval progress to the 'evals' branch of Aimen-Khalid/3d-portfolio-builder.
# Commits are authored by Aimen only (no co-author trailers), per her standing preference.
set -euo pipefail
WS=/home/claude/ppb-workspace
REPO=/home/claude/3d-portfolio-builder
cd "$REPO"
git fetch -q origin main
if git show-ref --verify -q refs/remotes/origin/evals; then
  git fetch -q origin evals
  git checkout -q -B evals origin/evals
elif ! git rev-parse -q --verify evals >/dev/null; then
  git checkout -q -b evals origin/main
else
  git checkout -q evals
fi

# Test cases live in the skill folder, where `claude plugin eval` reads them.
mkdir -p playful-portfolio-builder/evals
rm -rf playful-portfolio-builder/evals && cp -R "$WS/evals" playful-portfolio-builder/evals

# Run results + tooling go in eval-workspace/ (work/ scratch dirs skipped; screenshots shrunk to JPEG).
mkdir -p eval-workspace
cp "$WS/make_cases.py" "$WS/checks.py" "$WS/executor_template_light.md" "$WS/cases_index.json" "$WS/sync_backup.sh" eval-workspace/
[ -f "$WS/PROGRESS.md" ] && cp "$WS/PROGRESS.md" eval-workspace/
(cd "$WS" && find iteration-1 -path '*/work' -prune -o -type f ! -name '*.png' -print | while read -r f; do mkdir -p "$REPO/eval-workspace/$(dirname "$f")"; cp "$f" "$REPO/eval-workspace/$f"; done)
python3 - "$WS/iteration-1" "$REPO/eval-workspace/iteration-1" <<'PY'
import os, sys
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
for root, dirs, files in os.walk(src):
    dirs[:] = [d for d in dirs if d != "work"]
    for f in files:
        if not f.endswith(".png"): continue
        s = os.path.join(root, f)
        d = os.path.join(dst, os.path.relpath(s, src))[:-4] + ".jpg"
        if os.path.exists(d) and os.path.getmtime(d) >= os.path.getmtime(s): continue
        os.makedirs(os.path.dirname(d), exist_ok=True)
        im = Image.open(s).convert("RGB")
        if im.width > 1280: im = im.resize((1280, round(im.height * 1280 / im.width)))
        im.save(d, "JPEG", quality=78)
PY

git add -A playful-portfolio-builder/evals eval-workspace
if git diff --cached --quiet; then echo "nothing new"; exit 0; fi
git -c user.name="Aimen-Khalid" -c user.email="aimenkhalid338@gmail.com" \
  commit -q -m "Eval progress: ${1:-update}"
git push -q -u origin evals
git log --oneline -1
du -sh eval-workspace
