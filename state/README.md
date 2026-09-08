# State

What the system remembers between chats. Claude Desktop projects do not share
conversation history, so these files are the only thing that carries the day
from the morning survey into a lesson and out into the weekly report.

| File | Written by | Lifetime |
|---|---|---|
| `today.md` | `День` project, each morning | Overwritten daily |
| `profile.md` | Parent, weekly | Grows over the term |
| `points.md` | `scripts/tally.mjs` **only** | Regenerated on every tally |

`points.md` is generated. Editing it by hand is always the wrong move — the
next tally overwrites it, and the discrepancy in between is exactly the kind of
thing that turns into an argument about points. Fix the logs instead.

## Why files rather than the model's memory

Three reasons, in order of how much they matter:

1. The parent can read and correct any of it without a chat.
2. Git shows every change, which is the only tamper-evidence this setup needs.
3. The tally is deterministic — the same logs always produce the same number.
