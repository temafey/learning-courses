# 16 — Two-week calibration window

| Field | Value |
|---|---|
| Status | `todo` |
| Depends on | 15 |
| Guide section | `docs/engagement-system.md` §6, §7 |
| Estimated time | Two weeks of running, then 30 min |

## Goal

Replace every guessed number in the system with a measured one. Thresholds set
before anyone knows this student's output are either trivially cheap or
unreachable, and both kill the mechanism inside a week.

## How it runs

For two weeks the system runs **complete except for thresholds**: themes, tone,
lessons, defense questions, logs, and `npm run tally` after each day. Points
accumulate and are visible. Nothing can be claimed yet, and he is told that
plainly — «два тижні рахуємо, потім вирішуємо ціни».

## Steps

1. Run the full daily cycle for ten school days.
2. Run `npm run tally` at the end of each day. Never edit `state/points.md`.
3. After two weeks, read the by-day table and write down:

   | Measure | Value |
   |---|---|
   | Median points on a day he studied | |
   | Best day | |
   | Worst day that still counted | |
   | Days with no session | |
   | Median points in a full week | |

4. Set the tiers from those numbers:

   | Tier | Rule of thumb |
   |---|---|
   | Day threshold | Around the median day — reachable on an ordinary day, not on a bad one |
   | Week bronze | A week of ordinary days |
   | Week silver | An ordinary week with one strong day |
   | Week gold | Genuinely his best week so far |
   | Month I / II / III | Scale the week tiers by the number of school days |

5. Price the catalogue items against those tiers and fill the blanks left in
   task 15.
6. Write the first real `state/profile.md` from the logs: which themes he
   picked, which tone landed, what difficulty he chose when free to, where he
   stalled.

## Done when

- [ ] Ten school days logged
- [ ] The five measures above written down
- [ ] Every tier threshold set from data, not guessed
- [ ] Catalogue prices filled in
- [ ] `state/profile.md` written from logs rather than assumptions

## Record

| Item | Value |
|---|---|
| Days actually logged out of ten | |
| Median day / best day | |
| Sessions abandoned | |
| Themes picked, in order of frequency | |
| Tone changed mid-window? | |
| `кринж` count | |
| Anything he gamed | |

The last row matters more than the rest. If he found a way to farm points
without learning during a window with nothing to win, the formula has a hole
worth fixing before there is something to win.

## Notes
