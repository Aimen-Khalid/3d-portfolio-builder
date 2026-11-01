# Evals for playful-portfolio-builder

Each folder is one test case in the layout `claude plugin eval` reads (`prompt.md`, `case.yaml`, one statement per file in `graders/`).

| Case | What it checks |
|---|---|
| `scroll-page-for-recruiters` | A recruiter-facing brief lands on a scrolling page with a 3D object per section, with real HTML text. |
| `second-site-not-a-copy` | After the user describes an earlier island-town site, the next person's world takes its shape from their own life and its composition differs from the earlier one. |

## The variety check (run it after any change to Step 2 or `scripts/deal.mjs`)

One site can pass and the skill can still collapse to one layout across people. So:

1. Run the skill, unattended, for five or six different people with sparse prompts (a student, a nurse, a chef, a game designer, a retired teacher, a company).
2. From each run's notes, copy the composition fingerprint: camera, ground, movement, time, look.
3. Put them in one table. **No two runs should share three or more of the five**, and no more than one should be one of the defaults listed in Step 2 of `SKILL.md`.
4. If runs cluster, look at which axis repeats and why (an axis option that wins every time, an idea sentence that keeps picking the same inventory item), and fix the skill, not the run.
