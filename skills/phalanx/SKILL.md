---
name: phalanx
description: >-
  Run a multi-archetype adversarial review of code, a change, or a proposal.
  Seven staff-level perspectives (Operational, Code Quality, UI/Frontend, UX,
  Architect, Technical Writer, InfoSec) analyze independently, then challenge
  each other, then reach a logged consensus. Use this whenever the user asks for
  a deep, thorough, multi-perspective, or "panel"-style review; a pre-merge or
  pre-ship audit; an adversarial or red-team read of a design; a second opinion
  from multiple experts; or says "phalanx review", "run the phalanx", "have the
  staff engineers look at this", or wants conflicting expert viewpoints
  reconciled — even if they don't name the skill. Prefer this over a
  single-pass review when the stakes, ambiguity, or cross-discipline surface
  justify it.
---

# Phalanx

A phalanx is a formation that only works because each shield covers a
neighbor's blind side. This skill convenes staff-level archetypes (12–20 years'
experience each) who **analyze independently, then attack each other's
positions, then converge**. No single archetype is trusted by default; each has
documented blind spots the others are licensed to exploit.

You are the **orchestrator**. You run the phases, spawn the archetypes as
independent subagents, enforce evidence and blind-spot discipline, and write
the audit log. You do not yourself decide the findings — the phalanx does.

The full archetype briefs (mandate, blind spots, self-checks, shared subagent
rules) live in `references/archetypes.md`. **Read that file now**, before
Phase 0 — you copy archetype blocks verbatim into subagent prompts.

**The user is the roster authority.** Surface the roster first and let the
user staff the phalanx.

---

## Phase 0 — Intake

Do this yourself, before spawning anyone. The order is deliberate:
**engineers → specialists → surface scope → surface → stack**.

### 0.1 Check for shorthands (silent)

Before presenting menus, check the invocation for shorthands. If present and
fully specified, use them and skip the corresponding menu steps:

- `--only a,b,c` or `--lock-roster a,b,c` → roster is **exactly** those lanes;
  skip 0.2; **recall OFF**.
- `--with a,b,c` → roster is exactly those lanes; skip 0.2; **recall OFF**
  unless all seven are named.

Lane tokens: `ops` (Operational), `cq` (Code Quality), `ui` (UI/Frontend),
`ux` (UX), `arch` (Architect), `tw` (Technical Writer), `sec` (InfoSec).

### 0.2 Roster + Surface scope

Present all three questions in **one AskUserQuestion call** — not markdown
output. Engineers and Specialists are multiSelect (pick any subset); Surface
Scope is single-select.

```
AskUserQuestion({
  questions: [
    {
      header: "Engineers",
      question: "Which engineering disciplines should participate?",
      multiSelect: true,
      options: [
        {
          label: "Staff Engineer — Operational (ops)",
          description: "Failure modes, observability, resource behavior, deploy/rollback"
        },
        {
          label: "Staff Engineer — Code Quality (cq)",
          description: "Readability, correctness, tests, abstraction fit, complexity"
        },
        {
          label: "Staff Engineer — UI/Frontend (ui)",
          description: "Component soundness, rendering performance, platform compatibility"
        }
      ]
    },
    {
      header: "Specialists",
      question: "Which specialist roles should participate?",
      multiSelect: true,
      options: [
        {
          label: "Staff Architect (arch)",
          description: "Boundaries, coupling, extensibility, data ownership, technology fit"
        },
        {
          label: "Staff InfoSec Engineer (sec)",
          description: "Trust boundaries, authN/Z, secrets, transport, concrete exploit paths"
        },
        {
          label: "Staff Technical Writer / Editor (tw)",
          description: "Accuracy, onboarding path, API contracts, naming, comment hygiene"
        },
        {
          label: "Staff UX Practitioner / Designer (ux)",
          description: "Flow integrity, friction, error experience, information architecture"
        }
      ]
    },
    {
      header: "Surface Scope",
      question: "What is the scope of the surface to review?",
      multiSelect: false,
      options: [
        {
          label: "Entire Codebase",
          description: "Broad scan of the whole repo; each specialist explores freely in their lane"
        },
        {
          label: "Subset of Codebase",
          description: "Specific paths, modules, or a diff range — you'll provide them next"
        },
        {
          label: "Specific Concern",
          description: "A targeted question or aspect of the system — you'll describe it next"
        },
        {
          label: "Deep Research",
          description: "A question, RFC, design doc, or proposal — little or no code"
        }
      ]
      // "Other" auto-option handles anything else
    }
  ]
})
```

Record the **roster disposition**, which sets the Phase 2 recall flag:

- **All 7 lanes selected** → `RECALL = ON`.
- **Any subset** → `RECALL = OFF`. A deliberately narrow run stays narrow.

### 0.3 Collect the surface

After scope type is known, collect the concrete surface via normal chat in
one follow-up message:

- **Entire Codebase** — confirm the repo root (cwd); no further input needed
  unless the user wants to add context.
- **Subset of Codebase** — *"Which paths, modules, or diff range?"*
- **Specific Concern** — *"Describe the concern or question."*
- **Deep Research** — *"Provide the research question, RFC text, or doc path."*
- **Other** — *"Describe the surface."*

Subagents start cold; whatever you collect here must be concrete and
self-contained so each specialist prompt can stand alone.

### 0.4 Run log

The log lives in a **gitignored `reviews/` directory at the repo root** (the
cwd's git root; if not a git repo, `./reviews/`).

1. Ensure `reviews/` exists.
2. Ensure it is gitignored. If `.gitignore` exists and lacks a `reviews/`
   entry, append `reviews/`. If no `.gitignore` exists, create one containing
   `reviews/`. Never commit anything under `reviews/`.
3. Run id: `DATE` = today `YYYY-MM-DD`; `SLUG` = kebab-case of the
   surface/subject (≤ 40 chars); `HASH` = 4 lowercase base36 chars from
   `python3 -c "import random,string;print(''.join(random.choice(string.ascii_lowercase+string.digits) for _ in range(4)))"`.
   `RUN_ID = <DATE>-<SLUG>-<HASH>`.
4. Log file = `reviews/<RUN_ID>.md`, **one file per run**; each phase is
   appended as its own top-level section as it completes, so the file is the
   complete in-order audit trail. Write the header now:

   ```
   # Phalanx — <RUN_ID>
   Scope: <surface scope type>   Surface: <surface description>
   Roster: <lanes>   Recall: ON | OFF   Started: <timestamp>

   ## Stack
   <filled in 0.5>

   ## Roster
   <lane> — ACTIVE (surface: …) — disposition recorded
   ```

### 0.5 Stack detection & veto

Each archetype must reason as a specialist *in this surface's stack*, not a
generalist — this structurally counters the "assumes generic web/cloud context"
blind spot.

1. **Detect.** Read `CLAUDE.md`, `README*`, and manifest/loader files
   (`package.json`, `go.mod`, `Cargo.toml`, `pyproject.toml`, `Gemfile`,
   `pom.xml`, `*.csproj`, `appinfo.json`, `sources.json`, etc.) plus dominant
   file extensions. Infer: language(s), framework, runtime/host, build system
   (or explicitly *none*), persistence, external services, deployment target,
   and the operating context that bounds threat model and scale (e.g.
   *single-user offline device app*, not *public multi-tenant web service*).

2. **Veto.** Use **AskUserQuestion** to present the detected stack before
   spending any tokens on subagents. Write the stack description as plain
   prose — no markdown bold, no bullet syntax, no backticks. The question
   field is rendered as plain text in the Claude Code UI.

   ```
   AskUserQuestion({
     questions: [
       {
         header: "Stack",
         question: "Does this detected stack look right?\n\n<one plain-text paragraph describing language, framework, runtime, build system, persistence, external services, deployment target, and operating context>",
         multiSelect: false,
         options: [
           {
             label: "Looks right — proceed",
             description: "Use this stack for all archetype prompts"
           },
           {
             label: "Need to correct it",
             description: "Describe corrections in your next message and I'll update before spawning"
           }
         ]
       }
     ]
   })
   ```

   If the user selects "Need to correct it", accept their corrections via
   normal chat and update `STACK_BRIEF` accordingly.

3. **Freeze `STACK_BRIEF`.** Write the confirmed stack into the log's
   `## Stack` section and keep it as `STACK_BRIEF` — a short paragraph you
   will inject **verbatim into every subagent prompt** (Phases 1, 2, and
   consensus).

Track the phases with the task tool so progress is visible.

---

## Phase 1 — Independent analysis

**Goal: genuine independence.** Spawn every specialist on the final roster as a
separate subagent **in a single message (parallel)**. They must not see each
other's work. Use the `Agent` tool with `subagent_type: "general-purpose"`.

Each prompt is assembled from:

1. The archetype's **entire block** from `references/archetypes.md` (Identity +
   Mandate + Blind spots + Self-check), verbatim.
2. The **shared rules** block from the bottom of `references/archetypes.md`,
   verbatim.
3. `STACK_BRIEF` (from 0.5), verbatim, prefaced: *"You are a specialist in this
   exact stack. Reason in its idioms and constraints, not a generalist's."*
4. The surface and scope type — describe what to analyze and how broadly.
5. This deliverable spec:

> You are this archetype, with the experience stated, **specialized to the
> stack above**. Investigate the surface **only through your archetype's lens**.
> First decide relevance:
>
> - If the surface contains **nothing in your domain**, respond with exactly:
>   `VERDICT: STAND DOWN — <one sentence: why the surface contains nothing in
>   your lane>` and stop. "Only minor findings" is **not** stand-down — that is
>   `VERDICT: ACTIVE` with minor findings.
> - Otherwise: `VERDICT: ACTIVE`, then your findings in the shared finding
>   format, ordered by severity, judged against **best practice for this
>   stack** (not generic advice). Run your blind-spot self-check and annotate
>   any finding it implicates.
> - **Course-correction (all lanes, bounded):** if you see the current
>   direction foreclosing a future option in your lane, surface **one**
>   alternative with the tradeoff named. This is a flagged tradeoff, not a
>   redesign — do not produce unsolicited rearchitecting.
> - End with up to three **cross-lane flags** (one line each) for other
>   archetypes, and a one-paragraph **position summary** (your single most
>   important conclusion).

Spawn all at once. As each returns, append to the log under `## Phase 1 —
Independent`, one subsection per archetype, verbatim. Fill `## Roster`: mark
each ACTIVE or STOOD DOWN with its one-sentence reason. The **ACTIVE** set is
the working roster for Phase 2.

---

## Phase 2 — Adversarial challenge

**Goal: stress every position until only what survives contact remains.**

### 2.1 Recall check (only if `RECALL = ON`)

If `RECALL = OFF`, **skip recall entirely** — the user deliberately narrowed
the roster and a narrow run stays narrow. Note in the log: *"Recall suppressed:
user-narrowed roster."*

If `RECALL = ON`, scan all Phase 1 outputs (findings *and* cross-lane flags)
plus the surface. Apply the recall test in `references/archetypes.md`: if a
stood-down lane's domain is implicated, recall it — spawn a catch-up
Phase-1-style subagent (same template, same `STACK_BRIEF`), append under
`## Phase 1 — Recalled: <archetype>`, add it to the working roster, and log the
one-sentence recall reason.

### 2.2 Challenge round (parallel subagents)

Spawn each working-roster archetype again, in parallel, one subagent each. Each
gets: its own archetype block + shared rules + `STACK_BRIEF` (verbatim), its
own Phase 1 output, and **the Phase 1 (and recall) outputs of all other
archetypes**. Deliverable spec:

> You have seen every archetype's independent analysis. Make the final
> consensus *correct*, not polite. Produce:
>
> - **Challenges:** name specific findings (by archetype + claim) you believe
>   are wrong, overstated, miscalibrated to this stack's real context, or
>   driven by that archetype's documented blind spot. Say which blind spot and
>   why. Cite evidence.
> - **Concessions:** your own Phase 1 findings you now withdraw or downgrade —
>   especially any your own blind-spot self-check flags.
> - **Reinforcements:** others' findings you independently confirm from your
>   lane, and why that matters.
> - **Revised positions:** merged or re-severitied findings you stand behind
>   for consensus, in the shared finding format.
> - **Hard disagreements:** conflicts you do *not* concede, as a crisp
>   either/or with the evidence on each side.

Append all challenge outputs under `## Phase 2 — Adversarial`, one subsection
per archetype, verbatim.

If a few hard disagreements remain and turn on a checkable question of fact,
do **one** targeted verification yourself, log it under `## Phase 2 —
Adjudication`, and carry the resolved fact into consensus. Do not run another
full round; unresolved *judgment* disagreements are meant to survive into the
consensus as recorded dissent.

---

## Phase 3 — Consensus

Spawn **one** consensus subagent (`general-purpose`). It is a neutral synthesis
mind — not an extra opinion. Its prompt contains `STACK_BRIEF` and the **entire
log so far** (Phases 0–2), with this charge:

> You are the consensus agent. Read the full engagement. Do **not** introduce
> new findings of your own. Synthesize, weighing arguments by evidence quality
> and by each archetype's documented blind spots — a finding an archetype's own
> self-check flagged, or that survived a well-evidenced challenge, is weighted
> accordingly; all findings are judged against best practice for the stack.
> Produce:
>
> 1. **Verdict** — one paragraph: ship/proceed, proceed-with-conditions, or
>    do-not-proceed, and the single reason.
> 2. **Consensus findings** — ranked by `severity × confidence`, each with the
>    surviving evidence, the resolution history (who challenged, what was
>    conceded), and the smallest effective remediation.
> 3. **Dissent register** — unresolved hard disagreements preserved as minority
>    opinions with evidence on each side. Do not flatten these; a suppressed
>    minority view is how blind spots win.
> 4. **Action list** — concrete, ordered, each tagged with the owning lane.
> 5. **Coverage & confidence** — which lanes were active / stood down /
>    recalled / suppressed and why, and where the phalanx itself is blind.

Append verbatim under `## Phase 3 — Consensus`, write a `Completed:`
timestamp, and finalize the log.

---

## Reporting back to the user

Keep the chat reply tight:

- The **verdict** and top consensus findings (severity-ranked, with
  `path:line`).
- Any **live dissent** — explicitly; that is where judgement is required of
  *them*.
- Roster outcome in one line: who was active / stood down / recalled /
  suppressed, and any phalanx-level blind spot.
- The **log path** (`reviews/<RUN_ID>.md`) as the full audit trail.

Don't paste the whole log into chat; it is the artifact, the reply is the
briefing.

---

## Operating doctrine

- **The user staffs the phalanx.** A deliberately narrow run stays narrow —
  `RECALL = OFF` unless the user selected all 7.
- **Stack-grounded, gold-standard.** Every archetype reasons as a specialist in
  the confirmed stack and judges against that platform's accepted best
  practice — never lowest-common-denominator generalist advice. "Generically
  unusual but idiomatic and correct here" is not a finding; "violates this
  platform's accepted best practice" is.
- **Independence is the product.** Phase 1 subagents never see each other.
  Collapsing this into one context defeats the skill.
- **Evidence or it's speculation.** Enforce the shared finding format. Claims
  about the code *or the stack* ("this framework does X") need grounding;
  unverified stack assertions are speculative, same as evidence-free code
  claims.
- **Blind spots are first-class.** Phase 2 is largely about catching findings
  that are an archetype indulging its blind spot. Severity is calibrated to
  *this* stack's real context (scale, users, threat model), never a generic
  ideal.
- **Course-correction is bounded.** Any lane may flag a foreclosed future
  option with its tradeoff named — but that is a flag, not unsolicited
  rearchitecting.
- **Dissent survives.** The consensus agent reconciles where honest and
  preserves disagreement where not. Never manufacture agreement.
- **Right-size the engagement.** Match effort to the roster the user chose and
  the surface; flag to the user if a broad run will be token-heavy before
  launching it.
