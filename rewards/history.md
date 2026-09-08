# Reward history

What was actually granted, and what it cost in points. Parent-owned — a
requested item in a day log is a request, not a grant.

`scripts/tally.mjs` reads the JSON block below to compute the spendable
balance. Points are subtracted only for rows with status `granted`.

Guaranteed monthly and quarterly rewards are recorded here too, with
`"points": 0` — they are keyed to points *earned* in the period, not bought
from the balance, so they never reduce what he can spend.

```json
{
  "claims": []
}
```

## Row shape

```json
{
  "date": "2026-10-04",
  "period": "week",
  "item": "Гра в Steam до 300 грн",
  "points": 250,
  "status": "granted"
}
```

| Field | Values |
|---|---|
| `period` | `day`, `week`, `month`, `quarter` |
| `item` | Exact name from `rewards/catalogue.md` |
| `points` | Points deducted. `0` for guaranteed month/quarter rewards |
| `status` | `granted` or `declined`. Only `granted` affects the balance |

## Keep this honest

A reward promised and not delivered costs more than never offering one. If a
grant has to be delayed, write the row with `status: declined` and a note
rather than leaving it ambiguous — the student can read this file, and a
pending row that never resolves is what teaches him the system is theatre.
