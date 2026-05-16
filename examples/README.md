# Examples: The Documentation Tension in Practice

The same function, documented three ways. The function is real — it parses ISO 8601 dates but silently truncates to UTC and raises `ValueError` on anything ambiguous.

Read the three examples in order. Then read `docs/philosophy.md`.

| Example | Problem | Which tool catches it |
|---|---|---|
| `over-documented/` | Noise that hides the actual gotcha | phalanx (Technical Writer: "this comment is compensating for a bad name") |
| `under-documented/` | Missing the silent UTC truncation | doctator ("ARCHITECTURE or inline comment warranted for non-obvious behavior") |
| `calibrated/` | Right amount | — |
