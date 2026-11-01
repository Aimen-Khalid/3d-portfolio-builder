---
type: llm
focus: trace
weight: 1
---

Section scenes are created or rendered only when near the viewport (shared renderer, IntersectionObserver or equivalent), so not every scene's render loop runs at once.
