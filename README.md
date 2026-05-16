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

Each invocation begins with a scope question: full audit of all doc types, a specific subset you choose, or strictly what you asked for. Diff mode is also configurable — propose each change with rationale before applying, or apply directly. Both preferences can be persisted in config so the questions stop appearing.

**Trigger:** `/doctator` or say "document this", "update the README", "write the CHANGELOG"

**Doc types:** README · CHANGELOG · ARCHITECTURE · USAGE · INSTALLATION · FAQ

**Source:** [`skills/doctator/SKILL.md`](skills/doctator/SKILL.md) · [`skills/doctator/config.json`](skills/doctator/config.json)

---

## phalanx

Phalanx reviews code and designs through three phases. In Phase 1, seven staff-level archetypes (12–20 years' experience each) analyze your surface independently and in parallel — they never see each other's work. In Phase 2, each archetype sees the others' findings and challenges what it believes is wrong, overstated, or driven by a documented bias in that lane. Findings that don't survive are withdrawn; those that do carry more weight for it. In Phase 3, a consensus agent synthesizes the full record — disagreements that neither side conceded are preserved, not papered over.

Each archetype brief includes documented blind spots, and the other archetypes are explicitly asked to test against them. The Technical Writer flags documentation that compensates for a bad name rather than fixing it. The InfoSec reviewer must name a plausible attacker before any security finding stands. The Architect must state a migration cost before proposing a structural change.

You staff the roster. Phalanx presents the seven archetypes and lets you pick which participate — run all seven for a pre-ship audit, or narrow to just InfoSec and Code Quality for a targeted pass. A narrowed roster stays narrow: archetypes that stood down aren't recalled mid-run. The shorthands `--only ops,sec` and `--with cq,arch` skip the roster menu entirely. The surface is also up to you: the full codebase, a specific path or diff, a targeted concern, or a design document with no code at all.

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
