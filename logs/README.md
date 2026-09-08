# Session logs

One file per session, appended by the tutor at step 9 of the protocol. The
prose is for the parent; the JSON block is what `scripts/tally.mjs` reads.

| File | Written by | Contains |
|---|---|---|
| `<YYYY-MM-DD>-<subject>.md` | Subject project | One lesson |
| `<YYYY-MM-DD>-day.md` | `День` project, evening | The day's claim decision |
| `weekly/<YYYY>-W<NN>.md` | Parent, from the weekly report | Rollup and decisions |

Logs are append-only. Nothing edits a past log — a correction is a new line in
the current one, so `git diff` stays meaningful.

## Session log format

````markdown
# 2026-09-08 — Алгебра

Тема: розкладання многочленів на множники.

Що трималося: винесення спільного множника.
Що переробити: формула різниці квадратів — плутає знак.

```json
{
  "date": "2026-09-08",
  "type": "session",
  "subject": "algebra",
  "topic": "Розкладання на множники",
  "theme": "star-wars",
  "tone": "по-пацанськи",
  "weather": "sunny",
  "difficulty": "9 з 10",
  "multiplier": 1.3,
  "completed": true,
  "anki_morning_done": true,
  "disengaged": false,
  "tasks": [
    { "n": 1, "attempted": true, "solved": true,
      "hints": 0, "defended": true, "stalled": false },
    { "n": 2, "attempted": true, "solved": true,
      "hints": 1, "defended": true, "stalled": false },
    { "n": 3, "attempted": true, "solved": false,
      "hints": 2, "defended": false, "stalled": true }
  ],
  "boss": { "attempted": true, "solved": false },
  "cards_written": 5,
  "deck": "School::Algebra",
  "gaps_closed": ["Спільний множник"],
  "why_asked": ["Розкладання на множники"],
  "feedback": { "clear": "yes", "interesting": "so-so", "tone": "ok" }
}
```
````

## Field reference

| Field | Values | Used by the tally |
|---|---|---|
| `type` | `session` or `day` | Yes — selects the branch |
| `multiplier` | `1.0` or `1.3` | Yes — applied to the session total |
| `completed` | boolean | Yes — 10 points |
| `anki_morning_done` | boolean | Yes — 5 points |
| `tasks[].attempted` | boolean | Yes — 3 points for a genuine attempt |
| `tasks[].solved` | boolean | Yes — 5 points, hints or not |
| `tasks[].defended` | boolean | Yes — 2 points |
| `tasks[].hints` | integer | No — report only |
| `tasks[].stalled` | boolean | No — report only |
| `boss` | object or `null` | Yes — 5 attempted, 5 more solved |
| `gaps_closed` | array of strings | Yes — 10 each |
| `feedback` | three answers | Yes — 2 points when all three are given |
| `why_asked` | array of topics | No — report only |
| `disengaged` | boolean | No — report only |
| `theme`, `tone`, `weather` | strings | No — report only |

`hints` and `stalled` deliberately earn nothing. They exist so the weekly
report can point at where he got stuck, not to price it.

`why_asked` earns nothing either, and must never be discouraged. A topic he
asks «навіщо» about twice is a motivation problem in that topic; a subject he
asks about every week is a motivation problem in that subject, and no amount of
points fixes it — see `curriculum/why/README.md`.

## The two signals that replace a stopwatch

There is no reliable way to measure how long he sat on a question — see
`docs/engagement-system.md` §8. Two behavioural flags stand in for it:

| Flag | Set when |
|---|---|
| `stalled` | Four or more turns on one problem with no progress |
| `disengaged` | Answers collapse to one word or «не знаю» across the session |

## Day log format

````markdown
# Day — 2026-09-08

Алгебра і фізика. Добре пішло розкладання, повернутися до різниці квадратів.

```json
{
  "date": "2026-09-08",
  "type": "day",
  "claim": "banked",
  "item": null,
  "streak_freeze_used": false
}
```
````

`claim` is `banked` or `requested`. A banked day earns +10% when the week
closes. A requested item is not granted — the parent grants it and records it
in `rewards/history.md`.
