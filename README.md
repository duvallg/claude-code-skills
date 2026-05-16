# claude-code-skills

Two Claude Code skills — **doctator** (documentation generator) and **phalanx** (adversarial multi-perspective code review) — packaged together because they exist in productive tension about how much documentation is enough.

See [`docs/PHILOSOPHY.md`](docs/PHILOSOPHY.md) for the argument. See [`examples/`](examples/) for a concrete illustration.

---

## Installation

```bash
# Claude Code CLI
claude plugin install https://github.com/duvallg/claude-code-skills
```

Or clone and install locally:

```bash
git clone https://github.com/duvallg/claude-code-skills
claude plugin install ./claude-code-skills
```

---

## Skills

### doctator

Invoke when you need documentation written or updated.

**Trigger:** `/doctator` or ask Claude to "document this", "update the README", "write the CHANGELOG"

**What it covers:** README, CHANGELOG, ARCHITECTURE, USAGE, INSTALLATION, FAQ, freeform docs. Knows when docs-only changes don't warrant a semver bump. Writes a per-project `.claude/rules/doctator.md` to keep collaborators consistent.

### phalanx

Invoke for a deep adversarial review before shipping.

**Trigger:** `/phalanx` or ask for a "thorough review", "multi-perspective review", "have the staff engineers look at this"

**What it covers:** Seven independent perspectives (Operational, Code Quality, UI/Frontend, UX, Architect, Technical Writer, InfoSec) review in parallel, challenge each other, and reach logged consensus. The Technical Writer archetype will tell you when a comment is compensating for a bad name.

---

## The tension

Doctator makes sure you have documentation. Phalanx makes sure documentation is the right answer. See [`docs/PHILOSOPHY.md`](docs/PHILOSOPHY.md).

---

## Contributing

See [`CLAUDE.md`](CLAUDE.md).
