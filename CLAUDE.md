# CLAUDE.md

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
| `curriculum/` | Subject plans and lesson sequences (Ukrainian) |
| `decks/` | Anki deck sources and card drafts (Ukrainian) |
| `logs/` | Session logs and progress notes |
| `scripts/` | Any automation (deck generation, exports) |

Only `docs/` exists today. Create the others as needed rather than up front;
do not scatter content at the repository root.

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
