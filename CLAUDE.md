# CLAUDE.md

<!-- markdownlint-disable-next-line MD013 -->
This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A content repository for a home learning setup: setup runbooks, curriculum
notes, study material and progress logs for a 7th-grade student on the
Ukrainian curriculum. It is not a software project — there is no build, no
test suite and no package manager. Occasional scripts may be added under
`scripts/`.

## Layout

| Path | Contents |
|---|---|
| `docs/` | Setup runbooks and technical guides (English) |
| `tasks/` | Ordered installation/setup work items with status (English) |
| `prompts/` | Claude Desktop project instructions, ready to paste (English wrapper, Ukrainian output) |
| `state/` | What the system remembers between chats: the day, the profile, points, aspirations |
| `logs/` | Session and day logs, append-only, each with a JSON block |
| `rewards/` | Catalogue, proposals and grant history |
| `curriculum/` | Subject plans, the «навіщо» tables, directions and the emphasis plan (Ukrainian) |
| `decks/` | Anki deck sources, card drafts and per-subject styling (Ukrainian) |
| `scripts/` | Automation — currently `tally.mjs`, which computes points from the logs |

`curriculum/`, `decks/` and anything else the student reads is Ukrainian; the
rest is English. Do not scatter content at the repository root.

`state/`, `logs/`, `rewards/`, `prompts/` and `curriculum/` are the five
folders exposed to Claude Desktop through the filesystem MCP server. Anything
written there is writable from a tutoring session; `docs/`, `tasks/` and
`.claude/` deliberately are not. Adding a sixth content folder means updating
`tasks/13-filesystem-mcp.md` and the server's argument list, so prefer a
subfolder of an existing one.

Two rules the design depends on: **only `scripts/tally.mjs` writes
`state/points.md`**, and **logs are append-only** — a correction is a new line,
never an edit to a past log.

`tasks/` is the execution side of `docs/`. Each task file carries a status, a
**Done when** checklist and a **Record** table of what the machine actually
did; `tasks/12-doc-feedback.md` is how those observations get folded back into
the guides, including the claims still marked unverified. Start at
`tasks/README.md`.

The two anchor documents are `docs/learning-stack-windows11-install.md` (the
stack) and `docs/engagement-system.md` (how a lesson is themed, scored,
rewarded and justified to the student). Change either only through a task, so
the change carries evidence.

## Language policy

- Technical docs, runbooks, comments and commit messages: **English**.
- Anything the student reads — cards, exercises, curricula, explanations:
  **Ukrainian**.

## Document conventions

These are required for every new document under `docs/`, not stylistic
preferences. `docs/learning-stack-windows11-install.md` is the reference
implementation — match it.

- Hard-wrap prose at **80 columns**. Do not let paragraphs run long.
- Numbered `##` sections starting at `## 0`, separated by `---` on its own
  line. Sub-steps as `### N.M`.
- Tables for anything enumerable: component lists, troubleshooting
  (Symptom / Cause / Fix), status. Prefer a table over a bullet list.
- Backtick all paths, ports, commands, add-on codes and config keys.
- Architecture diagrams as PlantUML C4 in a ```plantuml fenced block, using
  `!include <C4/C4_Container>`. The source block is the deliverable; there is
  no rendering step.
- Every technical document ends with a **verification status table** — one row
  per factual claim, marked `Verified — <source>` or `**Unverified**` with the
  reason. Date the section. Never present an unverified claim as settled, and
  never mark a claim verified without having actually checked the source.

Use `/new-doc` to scaffold a document with this structure already in place.

## Stack reference

The environment the docs describe, so it does not have to be re-derived:

- **Kolibri** — content library, `127.0.0.1:8080`, Windows `.exe` bundles its
  own Python 3.
- **Anki + AnkiConnect** — add-on code `2055492159`, local HTTP API on
  `127.0.0.1:8765`, binds loopback only by default.
- **`@ankimcp/anki-mcp-server`** — bridges Claude Desktop to AnkiConnect over
  STDIO. Requires Node.js ≥ 22.12.0. Currently 0.22.0 and self-described as
  beta; breaking changes are permitted under 0.x, so pin the version when
  recommending it.
- Claude Desktop config: `%APPDATA%\Claude\claude_desktop_config.json`.

Everything runs on localhost. When a doc suggests exposing a service beyond
loopback, call out the firewall and binding implications explicitly.

## Repository

Git repo, remote `git@github.com:temafey/learning-courses.git`, default branch
`main`. Working files live under OneDrive, so a file may already have been
changed on disk by sync — check `git status` before assuming the tree is clean.

Run `npm run lint` before committing docs. `markdownlint-cli2` enforces the
80-column rule (tables, code blocks and headings exempt) plus heading and
fenced-block hygiene. A `PostToolUse` hook reports over-length lines during
editing; `<!-- markdownlint-disable-next-line MD013 -->` suppresses both for a
single line.
