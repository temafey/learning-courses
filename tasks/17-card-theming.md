# 17 — Per-subject note types and card styling

| Field | Value |
|---|---|
| Status | `todo` |
| Depends on | 07 |
| Guide section | `decks/styling/README.md` |
| Estimated time | 20 min |

## Goal

Each subject's cards look like that subject. This is the only place in the
stack where the "background" the student picks can be literal.

Do this **before** the collection fills up. Changing note types later means
migrating existing notes, which is tedious and loses scheduling if done wrong.

## Steps

1. `Tools → Manage Note Types → Add → Clone: Basic`. Create four:
   `School-Algebra`, `School-Physics`, `School-Chemistry`, `School-English`.
2. For each, open `Cards... → Styling` and paste a stylesheet.
   `decks/styling/space.css` is the worked example; copy it and change the two
   gradients per subject.
3. Set each subject project's cards to use the matching note type. The tutor
   creates notes through `anki-mcp`, so the note type name has to be exactly
   what the project instructions say.
4. Review one card of each type in both light and night mode, and once on a
   phone if the collection syncs there.

## Done when

- [ ] Four note types exist
- [ ] Each has its own styling
- [ ] Text is legible in night mode — check, do not assume
- [ ] A card written by the tutor lands on the right note type

## Record

| Item | Value |
|---|---|
| Note types created | |
| Stylesheets used | |
| Night mode legible? | |
| Phone check done? | |
| Note type the MCP server defaults to | |

The last row is the one that bites: if the MCP server writes to `Basic`
regardless, the styling never shows, and the fix is in the project instructions
rather than in Anki.

## Notes
