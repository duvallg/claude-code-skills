# Documentation Tension

Documentation has two failure modes that feel opposite but stem from the same impulse: wanting to be helpful.

**Over-documentation** adds prose to things that are already clear. A function named `parse_iso8601_date` doesn't need a docstring that says "Parses a date in ISO 8601 format." The name did that. The docstring is noise — it's something to maintain, something that can drift out of sync, something that buries the one comment that actually matters.

**Under-documentation** assumes shared context that doesn't exist. The function that silently truncates to UTC without saying so. The configuration key with no description. The CHANGELOG that just says "bug fixes." These cost readers time and trust.

The tools in this repo address both failure modes from different angles.

---

## What doctator does

Doctator writes documentation. It knows which doc types are appropriate for which kinds of changes, when a CHANGELOG entry is warranted (docs-only changes don't bump semver), and what belongs in a README versus an ARCHITECTURE file. It has a persona: a technical writer who's read enough bad documentation to have opinions about economy of words.

Use doctator when the problem is "we don't have docs" or "the docs are stale."

## What phalanx does

Phalanx runs a multi-perspective code review. One of its seven archetypes is a Technical Writer whose mandate includes naming consistency, comment hygiene, and clarity of load-bearing prose. This archetype's defined blind spot: *"demands docs where better naming would serve."*

That blind spot is intentional. The Technical Writer archetype will flag missing documentation — but it will also flag documentation that exists to compensate for bad names, and recommend fixing the name instead. No amount of doctator runs fixes a function called `process_data`.

Use phalanx when the problem is "we don't know what we don't know" — including whether the documentation strategy is right.

---

## How they relate

Doctator and phalanx are not alternatives. They address different questions:

| Question | Tool |
|---|---|
| What docs should we have? | doctator |
| Are our docs accurate and complete? | doctator |
| Is our documentation *strategy* right? | phalanx |
| Are we documenting instead of naming clearly? | phalanx |
| Is there a security implication in how we document secrets? | phalanx (InfoSec archetype) |

The tension is useful. A codebase reviewed by phalanx then documented by doctator is better than either alone. A codebase documented by doctator and then phalanx-reviewed will sometimes get the feedback: "this comment is compensating for a bad name — fix the name."

That's the right outcome.
