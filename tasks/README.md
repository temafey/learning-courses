# Installation tasks

Ordered work breakdown for building the learning stack. Tasks 01–11 build the
stack described in `docs/learning-stack-windows11-install.md`; tasks 13–18
build the engagement layer described in `docs/engagement-system.md`; task 12
folds everything observed back into both documents and runs last. One file per
task; the number is the task ID and the sort order is the execution order.

Each task file owns its own status. This index mirrors it — if the two
disagree, the task file wins.

| # | Task | Depends on | Status |
|---|---|---|---|
| 01 | [Prerequisites](01-prerequisites.md) | — | `doing` |
| 02 | [Install Kolibri and set up the facility](02-kolibri-install.md) | 01 | `todo` |
| 03 | [Import Kolibri content channels](03-kolibri-channels.md) | 02 | `todo` |
| 04 | [Verify Kolibri progress tracking](04-kolibri-verify.md) | 03 | `todo` |
| 05 | [Install Anki and enable FSRS](05-anki-install.md) | 01 | `todo` |
| 06 | [Install and verify AnkiConnect](06-ankiconnect.md) | 05 | `todo` |
| 07 | [Create the subject deck hierarchy](07-anki-decks.md) | 06 | `todo` |
| 08 | [Install the Anki MCP server](08-mcp-server-install.md) | 06 | `todo` |
| 09 | [Verify the MCP bridge](09-mcp-verify.md) | 07, 08 | `todo` |
| 10 | [Set up Claude Desktop projects](10-claude-projects.md) | 09 | `todo` |
| 11 | [Put daily operation in place](11-daily-operation.md) | 10 | `todo` |
| 13 | [Add the filesystem MCP server](13-filesystem-mcp.md) | 09 | `todo` |
| 14 | [Wire up the projects and prompts](14-projects-and-prompts.md) | 10, 13 | `todo` |
| 15 | [Agree the rewards catalogue](15-rewards-catalogue.md) | — | `todo` |
| 16 | [Run the calibration window](16-calibration-window.md) | 14, 15 | `todo` |
| 17 | [Theme the Anki cards](17-card-theming.md) | 07 | `todo` |
| 18 | [Fill the «навіщо» tables and run the first check-in](18-why-and-direction.md) | 10, 13, 14 | `todo` |
| 12 | [Fold findings back into the guide](12-doc-feedback.md) | 01–11, 13–18 | `todo` |

Three chains run independently. Kolibri is 02–04, Anki is 05–09, and the
engagement layer is 13–18 — which needs the filesystem server from 13 before
any of it can remember anything between chats. A failure in one chain does not
block the others.

Task 12 is numbered before the engagement tasks but runs after all of them: it
is the write-back step, and it has nothing to write until every other Record
table is filled. Tasks 15 and 17 need no install at all and can be done on any
evening while a download runs.

## Status values

| Value | Meaning |
|---|---|
| `todo` | Not started |
| `doing` | In progress |
| `done` | Every box under **Done when** is checked |
| `blocked` | Cannot proceed; the reason is written in that task's **Notes** |

## Why every task has a Record table

Both guides were written from upstream sources and from design reasoning, not
from a working machine. Two claims in the install guide's §8 and several in
`docs/engagement-system.md` §13 are still marked `**Unverified**` because only
a live install — or a month of real sessions — can settle them.

The **Record** tables collect what actually happened — versions, paths, UI
wording, firewall answers, which reward he chose, what he said he wanted to be
— and task 12 folds that back into `docs/`, so both documents end up describing
the system that exists rather than the one that was designed.

Fill a Record row even when it matches the guide. "Matched" is evidence too.
