# Prompts

Project instructions for Claude Desktop. Each file holds a paste-ready block
plus the reasoning behind it; the reasoning stays here, only the block goes
into the project.

| File | Claude Desktop project | Runs |
|---|---|---|
| `day-start.md` | `День` | Each morning, before the first lesson |
| `day-end.md` | `День`, below the morning block | Each evening, plus the weekly report |
| `subject-tutor.md` | One per subject | Each study session |
| `themes/` | Attached to every subject project | Read during a lesson |

## Project setup

| Project | Knowledge to attach | MCP servers needed |
|---|---|---|
| `День` | `rewards/catalogue.md` | filesystem |
| Алгебра | Textbook PDF, `prompts/themes/` | filesystem, anki-mcp |
| Фізика | Textbook PDF, `prompts/themes/` | filesystem, anki-mcp |
| Хімія | Textbook PDF, `prompts/themes/` | filesystem, anki-mcp |
| Англійська | Textbook PDF, `prompts/themes/` | filesystem, anki-mcp |

Response style: **Learning**, in every project.

## Language

The instruction blocks are English because the model reads them. Everything the
student reads is Ukrainian, and the blocks say so in their first two lines.
Ukrainian text appears inside the blocks only where the exact wording matters —
the four survey questions, the three closing questions, the tone samples.

## When you edit a block

Two rules that are load-bearing, and both look like boilerplate that could be
trimmed:

- **The tutor never awards points.** Softening this once produces a session
  where points are negotiated, and after that they are negotiated every time.
- **The tutor never names a reward outside the catalogue.** Without it the
  model will eventually invent something generous that the parent has to
  refuse.

Both are in `subject-tutor.md` under POINTS AND REWARDS. Keep the wording
absolute; a hedged version does not survive a persistent 12-year-old.
