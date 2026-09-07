# 12 — Fold findings back into the guide

| Field | Value |
|---|---|
| Status | `todo` |
| Depends on | 01–11 |
| Guide section | all of `docs/learning-stack-windows11-install.md` |
| Estimated time | 30 min |

## Goal

Make the guide describe the machine that exists. Until this task runs, the
install is documented from upstream sources and the observations sit unused in
twelve **Record** tables.

## Steps

1. Read the **Record** and **Notes** sections of tasks 01–11 end to end.
2. Update §8, the verification status table:

   | Claim | Settled by |
   |---|---|
   | Ukrainian / Russian localized channel coverage | Task 03 |
   | Windows log path `%APPDATA%\Claude\logs\` | Task 09 |

   Move each to `Verified — observed on this machine, <date>` with what was
   actually seen, or leave it unverified with a better-stated reason. Re-date
   the section header.
3. Correct any step whose UI path, version number or behaviour diverged from
   what the guide says. Follow the existing correction style — the FSRS
   blockquote in §3.1 is the model: state what the old text said, why it was
   wrong, and what to do instead.
4. Add a troubleshooting row to §7 for every real problem hit, with the fix
   that actually worked.
5. Update the version numbers the guide quotes: Kolibri release, Anki version,
   MCP server version, tool count.
6. If upstream has moved since 2026-09-07, run `/verify-facts` on the document
   rather than re-checking by hand.
7. `npm run lint`, then commit the guide and the closed-out task files
   together.

## Done when

- [ ] No claim in §8 rests on evidence that was never gathered
- [ ] Every task's **Notes** has been folded in or explicitly dismissed
- [ ] Every problem actually hit has a §7 row
- [ ] `npm run lint` passes
- [ ] All twelve tasks in `README.md` read `done`

## Record

| Item | Value |
|---|---|
| Guide revision date | |
| Claims moved Unverified → Verified | |
| Claims still unverified, and why | |
| Corrections made to steps | |
| New troubleshooting rows | |

## Notes
