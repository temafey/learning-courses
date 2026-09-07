# 10 — Set up Claude Desktop projects

| Field | Value |
|---|---|
| Status | `todo` |
| Depends on | 09 |
| Guide section | `docs/learning-stack-windows11-install.md` §5 |
| Estimated time | 30 min |

## Goal

One Claude Desktop Project per subject, each carrying the textbook and the
tutoring protocol, and each able to write its own cards into Anki at the end
of a session.

## Steps

1. Create one Project per subject: Algebra, Physics, Chemistry, English.
2. Attach the subject textbook PDF to the project knowledge. The protocol
   requires facts and formulas to come from the textbook rather than from
   model memory, so this is not optional.
3. Set the response style to **Learning**.
4. Paste the project instructions from §5 of the guide, substituting the
   subject name in the deck path `School::<Subject>`.
5. Remove `--read-only` from the MCP server configuration (task 08). With it
   on, step 5 of the tutoring protocol — writing cards — fails silently as a
   blocked operation.
6. Run one short test session in a single subject and confirm the cards land
   in the right deck.

## Done when

- [ ] Each subject has a Project with its textbook attached
- [ ] The instruction block is in place with the correct deck path
- [ ] A test session writes at least one card into `School::<Subject>`
- [ ] The card is visible in Anki's Browser

## Record

| Item | Value |
|---|---|
| Projects created | |
| Textbook sources used | |
| `--read-only` removed on | |
| Test session subject and topic | |
| Cards written, and to which deck | |
| Protocol steps the model skipped | |

The last row matters: if the model drifts from the protocol — hands out
answers, skips the diagnostic question, forgets the progress block — that is
an instruction problem to fix in the project, and worth carrying into task 12.

## Notes
