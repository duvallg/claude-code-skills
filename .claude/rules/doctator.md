# doctator-version: 7
# Documentation standards (enforced by /doctator)
# Full workflow and doc-type rules: invoke /doctator

- Never include API keys, credentials, tokens, secrets, or PII in any documentation
  (PII: names, emails, device IDs, user IDs, analytics data, location, or any identifying information)
- Never include local filesystem paths, internal hostnames, or machine-specific details; use placeholders (`~/project`, `<project-root>`) where a path is unavoidable
- README is a distillation: no schema tables, global state references, or comprehensive API listings; lead with what it does, not how
- Code blocks in documentation never include line numbers
- CHANGELOG follows Keep a Changelog semver — docs-only commits (.md, media) do not bump the version
- Every FAQ entry must cite an observable code path, error condition, or config source
- Architecture diagrams use mermaid; no two diagrams express the same relationships
- Documentation is factual: describe what the system does, not how good it is at doing it; no evaluative language
- No feature-list openings: describe behavior in prose; don't lead with an enumerated capability list and inline annotations for each item
- Markdown filenames use UPPERCASE with a lowercase `.md` extension (e.g., `README.md`, `PHILOSOPHY.md`, `CHANGELOG.md`); not `readme.md`, `philosophy.md`, `changelog.md`
- Frame by what something does, not what it prevents — "disagreements are preserved" not "consensus is never manufactured"
- Use disciplinary verbs for systematic processes (challenges, requires, must), not adversarial ones (attacks, exploits, licensed to)
- Earn unusual phrasing or cut it — clever brevity must also be specifically true; glib compression delivers nothing
- No ironic distance: avoid words that create detachment from the subject (reflex, licensed, never X)
- When documenting tools with invocation menus, enumerate the menus and their options explicitly — don't describe them abstractly or omit them
- Never describe a persona or archetype's experience as a year count; describe it through industry, company type and scale, and demonstrable personal impact
