# claude-code-skills

Two complementary Claude Code skills: **doctator** for documentation and **phalanx** for adversarial code review. They're packaged together because they answer the same question from different directions — see [`docs/PHILOSOPHY.md`](docs/PHILOSOPHY.md).

---

## Installation

```bash
claude plugin install https://github.com/duvallg/claude-code-skills
```

Or clone and install locally:

```bash
git clone https://github.com/duvallg/claude-code-skills
claude plugin install ./claude-code-skills
```

---

## doctator

Doctator is a 7–10 year technical writer persona with an outside-in perspective and economy-of-words discipline. It reads your system as a new reader would — not as the implementer — and writes only what earns its place. It knows the rules for each doc type: README is a distillation, CHANGELOG follows Keep a Changelog, FAQ entries require a code-path source. It detects when existing docs contradict current code and surfaces the conflict before overwriting anything.

On first invocation in any project, it writes a `.claude/rules/doctator.md` and commits it to the repo — so every session and every collaborator works to the same documentation standard without having to invoke the skill again.

Each invocation opens two menus before any writing happens:

**Scope** — what to document this run:
- All doc types (full audit: README, CHANGELOG, ARCHITECTURE, USAGE, INSTALLATION, FAQ)
- Specific doc types (you choose which)
- Only what you asked for (strictly the doc type in your request)

**Delivery** — how to receive changes:
- Propose each diff with rationale before applying
- Apply all diffs directly

Both can be persisted in config so the menus stop appearing on future invocations.

**Trigger:** `/doctator` or say "document this", "update the README", "write the CHANGELOG"

**Doc types:** README · CHANGELOG · ARCHITECTURE · USAGE · INSTALLATION · FAQ

**Source:** [`skills/doctator/SKILL.md`](skills/doctator/SKILL.md) · [`skills/doctator/config.json`](skills/doctator/config.json)

---

## phalanx

Phalanx reviews code and designs through three phases. In Phase 1, seven staff-level archetypes (12–20 years' experience each) analyze your surface independently and in parallel — they never see each other's work. In Phase 2, each archetype sees the others' findings and challenges what it believes is wrong, overstated, or driven by a documented bias in that lane. Findings that don't survive are withdrawn; those that do carry more weight for it. In Phase 3, a consensus agent synthesizes the full record — disagreements that neither side conceded are preserved, not papered over.

Each archetype brief includes documented blind spots, and the other archetypes are explicitly asked to test against them. The Technical Writer flags documentation that compensates for a bad name rather than fixing it. The InfoSec reviewer must name a plausible attacker before any security finding stands. The Architect must state a migration cost before proposing a structural change.

Each invocation opens three menus before any analysis begins:

**Engineers** (multiselect) — pick any combination:
- Staff Engineer — Operational (`ops`)
- Staff Engineer — Code Quality (`cq`)
- Staff Engineer — UI/Frontend (`ui`)

**Specialists** (multiselect) — pick any combination:
- Staff Architect (`arch`)
- Staff InfoSec Engineer (`sec`)
- Staff Technical Writer (`tw`)
- Staff UX Practitioner (`ux`)

**Surface scope** (single select):
- Entire codebase
- Subset of codebase (paths or diff range — you provide them next)
- Specific concern (a question or aspect — you describe it next)
- Deep research (an RFC, design doc, or proposal)

After roster and scope, phalanx detects the stack (language, framework, runtime, deployment target) and presents it for confirmation before spawning any subagents. You can correct it if it's wrong.

The shorthands `--only ops,sec` and `--with cq,arch` skip the roster menus entirely for repeat invocations.

Every run produces a permanent audit log in `reviews/` (gitignored) with each phase appended in order as it completes.

**Trigger:** `/phalanx` or say "thorough review", "multi-perspective review", "have the staff engineers look at this"

**Archetypes:** Operational (`ops`) · Code Quality (`cq`) · UI/Frontend (`ui`) · UX (`ux`) · Architect (`arch`) · Technical Writer (`tw`) · InfoSec (`sec`)

**Verdict:** ship / proceed-with-conditions / do-not-proceed, with findings ranked by severity × confidence and surviving dissent recorded.

**Source:** [`skills/phalanx/SKILL.md`](skills/phalanx/SKILL.md) · [`skills/phalanx/references/archetypes.md`](skills/phalanx/references/archetypes.md)

---

## The tension

Doctator makes sure you have documentation. Phalanx makes sure documentation is the right answer. See [`docs/PHILOSOPHY.md`](docs/PHILOSOPHY.md) and [`examples/`](examples/).

---

## Contributing

See [`CLAUDE.md`](CLAUDE.md).
