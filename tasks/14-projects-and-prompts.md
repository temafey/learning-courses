# 14 — Wire the prompts into Claude Desktop projects

| Field | Value |
|---|---|
| Status | `todo` |
| Depends on | 10, 13 |
| Guide section | `prompts/README.md` |
| Estimated time | 30 min |

## Goal

Five working projects: `День` for the survey and the rollup, and one per
subject carrying the tutoring protocol, the theme rules and the logging step.

## Steps

1. Create the `День` project. Paste `prompts/day-start.md`'s block, then a line
   reading `--- ВЕЧІР ---`, then the block from `prompts/day-end.md`.
2. Attach `rewards/catalogue.md` to its knowledge.
3. For each subject project created in task 10, replace the instructions with
   the block from `prompts/subject-tutor.md`, substituting `<SUBJECT>`.
4. Attach `prompts/themes/` to each subject project alongside the textbook.
5. Set the response style to **Learning** in all five.
6. Run one dry session per project with yourself, not the student:

   | Project | What to check |
   |---|---|
   | `День` | Asks four questions, writes `state/today.md`, does not teach |
   | A subject | Reads the theme, decorates without changing the maths, asks the defense question, writes a log with a valid JSON block |

7. Run `npm run tally` on the dry-run log. If it reports zero sessions, the
   JSON block is malformed — fix the template in project knowledge, not the
   log.
8. Delete the dry-run logs before the student's first real session.

## Done when

- [ ] All five projects exist with the correct blocks
- [ ] The morning survey writes a valid `state/today.md`
- [ ] A subject session writes a log that `npm run tally` reads
- [ ] The tutor refuses to name a reward outside the catalogue when pushed
- [ ] The tutor refuses to award points when asked directly

## Record

| Item | Value |
|---|---|
| Projects created | |
| Survey duration in the dry run | |
| Log JSON valid on first attempt? | |
| Tutor tried to award points? | |
| Tutor invented a reward? | |
| Instruction wording that had to change | |

The last three rows are the real test. Both refusals are load-bearing, and a
model that bends on either during a dry run will bend faster with a child
pushing.

## Notes
