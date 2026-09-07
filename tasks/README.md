# Installation tasks

Ordered work breakdown for building the learning stack described in
`docs/learning-stack-windows11-install.md`. One file per task; the number is
the task ID and the sort order is the execution order.

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
| 12 | [Fold findings back into the guide](12-doc-feedback.md) | 01–11 | `todo` |

Kolibri (02–04) and Anki (05–09) are independent chains. Either can be done
first, and a failure in one does not block the other.

## Status values

| Value | Meaning |
|---|---|
| `todo` | Not started |
| `doing` | In progress |
| `done` | Every box under **Done when** is checked |
| `blocked` | Cannot proceed; the reason is written in that task's **Notes** |

## Why every task has a Record table

The guide was written from upstream sources, not from a working machine. Two
of its claims are still marked `**Unverified**` in §8 because only a live
install can settle them. The **Record** tables collect what the machine
actually does — versions, paths, UI wording, firewall answers — and task 12
folds that back into `docs/`, so the guide ends up describing the system that
exists rather than the one that was documented.

Fill a Record row even when it matches the guide. "Matched" is evidence too.
