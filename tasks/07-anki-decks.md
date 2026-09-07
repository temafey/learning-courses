# 07 — Create the subject deck hierarchy

| Field | Value |
|---|---|
| Status | `todo` |
| Depends on | 06 |
| Guide section | `docs/learning-stack-windows11-install.md` §5 |
| Estimated time | 5 min |

## Goal

The four subject decks exist before any tutoring session runs. The project
instructions in §5 tell Claude to write cards into `School::<Subject>`; if the
deck is missing the end-of-session step fails.

## Steps

1. In Anki, create the parent deck `School`, then the four subject decks:

   | Deck |
   |---|
   | `School::Algebra` |
   | `School::Physics` |
   | `School::Chemistry` |
   | `School::English` |

2. The guide states that deck nesting is limited to `Parent::Child`, two
   levels. Try creating `School::Algebra::Fractions` once and record whether
   Anki accepts it — this claim is not in the guide's fact table and is worth
   settling while the collection is empty.
3. Confirm the decks over the API, which also re-proves the AnkiConnect path:

   ```powershell
   Invoke-RestMethod -Uri http://127.0.0.1:8765 -Method Post `
     -ContentType 'application/json' `
     -Body '{"action":"deckNames","version":6}'
   ```

## Done when

- [ ] All four subject decks exist in the Anki UI
- [ ] `deckNames` returns them
- [ ] The nesting-depth question in **Record** is answered

## Record

| Item | Value |
|---|---|
| Decks created | |
| `deckNames` output | |
| Deeper nesting than `Parent::Child` accepted? | |
| FSRS applied to the new decks? | |

## Notes
