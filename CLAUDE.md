# Contributing to claude-code-skills

## Markdown file naming

All markdown files in this repo use uppercase filenames with a lowercase `.md` extension (e.g., `README.md`, `PHILOSOPHY.md`, `CHANGELOG.md`). If you add a markdown file, follow this convention.

## Skills live in `skills/`

Each skill is `skills/<name>/SKILL.md` plus optional `references/`. Do not add to `~/.claude/skills/` — that's where these are installed, not where they live.

## The documentation tension is intentional

If you edit doctator or phalanx, don't smooth over the productive conflict between them. Doctator's job is more docs; phalanx's Technical Writer archetype's job includes recommending fewer docs and better names. Both should stay true to their mandates.

## Editing skills

- Read from `skills/<name>/SKILL.md` — don't read from `~/.claude/skills/`
- Commit skill changes separately from docs changes

## Adding skills

If you add a skill, it must:
- Live in `skills/<skill-name>/SKILL.md`
- Have `name:` and `description:` frontmatter
- Be documented in `README.md` under the Skills section
