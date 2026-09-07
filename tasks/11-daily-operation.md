# 11 — Put daily operation in place

| Field | Value |
|---|---|
| Status | `todo` |
| Depends on | 10 |
| Guide section | `docs/learning-stack-windows11-install.md` §6 |
| Estimated time | 15 min, then one week of running it |

## Goal

The stack survives a reboot without help, and one full cycle of the daily
routine has actually been run rather than merely described.

## Steps

1. Add Anki to Startup Apps, so the API is up before anyone needs it. Either
   `Settings → Apps → Startup`, or a shortcut in the folder that
   `shell:startup` opens.
2. Decide whether Kolibri should auto-start too, and record the decision. It
   installs as a background service on some setups and as a tray app on
   others — record which one this machine got.
3. Reboot and confirm both are reachable without a manual launch.
4. Run one full cycle:

   | When | What |
   |---|---|
   | Morning | Student clears due cards, 10–15 min |
   | Study session | One Claude Desktop project, one topic, ~30 min |
   | End of session | Claude writes the new cards into the subject deck |
   | Weekly | Parent reads the Kolibri coach report and asks for review stats |

5. For the weekly review, ask Claude directly:

   > Show review stats for `School::Algebra` over the last 30 days. Which
   > cards is he failing repeatedly?

   Cards failing repeatedly are not a memory problem. They mark a concept that
   was never understood, and belong in a teaching session rather than in more
   repetition.

## Done when

- [ ] Anki starts automatically after a reboot
- [ ] Kolibri is reachable after a reboot, or its manual start is documented
- [ ] One complete day of the routine has been run end to end
- [ ] The weekly stats query returns real numbers

## Record

| Item | Value |
|---|---|
| Anki startup method used | |
| Kolibri: service, tray app or manual | |
| Both reachable after reboot? | |
| Actual morning card time | |
| First-week retention observations | |
| Cards flagged as repeated failures | |

## Notes
