# 04 — Verify Kolibri progress tracking

| Field | Value |
|---|---|
| Status | `todo` |
| Depends on | 03 |
| Guide section | `docs/learning-stack-windows11-install.md` §2.4 |
| Estimated time | 10 min |

## Goal

Prove the loop that makes Kolibri worth running: a learner attempt reaches the
coach dashboard. Content that merely displays is not enough.

## Steps

1. Sign in as the learner at `http://127.0.0.1:8080` and open the Learn page.
2. Open one exercise and answer it — deliberately get one wrong as well, so
   the report has something to show.
3. Sign out, sign in as `parent`, and open `Coach → Reports`.
4. Confirm the attempt is listed against the learner.
5. If nothing appears, the content was opened as a guest or as the admin
   account. Check which user was signed in and repeat.

## Done when

- [ ] The Learn page renders imported content
- [ ] A learner attempt appears in `Coach → Reports`
- [ ] Both a correct and an incorrect answer are visible in the report

## Record

| Item | Value |
|---|---|
| Exercise used for the test | |
| Attempt visible in Coach → Reports | |
| Delay before the attempt appeared | |
| Guest-vs-learner confusion hit? | |

## Notes
