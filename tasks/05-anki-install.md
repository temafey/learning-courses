# 05 — Install Anki and enable FSRS

| Field | Value |
|---|---|
| Status | `todo` |
| Depends on | 01 |
| Guide section | `docs/learning-stack-windows11-install.md` §3.1 |
| Estimated time | 20 min |

## Goal

Anki installed with a local profile and the FSRS scheduler switched on. This
chain is independent of Kolibri — it can be done before or after tasks 02–04.

## Steps

1. Download Anki for Windows from `apps.ankiweb.net` and install with the
   defaults.
2. Create a local profile. AnkiWeb sync is optional and nothing in this setup
   depends on it.
3. Enable FSRS: open any deck's options and switch it on in the **FSRS**
   section at the bottom of that page. The setting is shared across presets,
   so enabling it once covers every deck.
4. Record the exact UI path where the toggle was found. An earlier revision of
   the guide placed it under `Tools → Preferences → Review`, which was wrong
   and had to be corrected — the wording moves between Anki versions, so this
   is worth capturing every time.
5. Restart Anki and confirm FSRS is still enabled.

## Done when

- [ ] Anki opens with a local profile
- [ ] The installed version is 23.10 or newer, which FSRS requires
- [ ] FSRS is enabled and survives a restart

## Record

| Item | Value |
|---|---|
| Anki version installed | |
| Profile name | |
| Collection path | |
| FSRS toggle — UI path as actually seen | |
| Deck options preset the toggle applied to | |
| AnkiWeb sync configured? | |

The collection normally lives at
`%APPDATA%\Anki2\<profile>\collection.anki2` — record the real path, since
task 12 and any backup runbook will reference it.

## Notes
