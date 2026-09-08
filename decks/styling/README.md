# Card styling

The one place in this stack where "background" is literal. Anki accepts
arbitrary CSS in the **Styling** section of the Cards screen, so each subject
can carry its own look.

## The constraint that decides the layout

Styling is shared **per note type**, not per deck. Four subject decks under one
note type all render identically, whatever their deck names.

So: **one note type per subject.**

| Note type | Deck | Stylesheet |
|---|---|---|
| `School-Algebra` | `School::Algebra` | `space.css` or your own |
| `School-Physics` | `School::Physics` | |
| `School-Chemistry` | `School::Chemistry` | |
| `School-English` | `School::English` | |

Create each by cloning `Basic` in `Tools → Manage Note Types → Add → Clone:
Basic`, then paste the stylesheet into `Cards... → Styling`.

There is a second route — a `Theme` field substituted into a `class` attribute
in the template, which would let one note type carry many looks. It is untested
here, and the note-type route is the one to use until someone checks it.

## Available hooks

| Selector | Applies to |
|---|---|
| `.card` | Every card of the note type |
| `.card1`, `.card2` | A specific card template |
| `.nightMode` | Dark mode |
| `.win`, `.mac`, `.android`, `.iphone`, `.mobile` | Platform |

Background images work. Keep them dark, low-contrast and quiet — a card is read
for four seconds under time pressure, and anything that competes with the text
costs recall.

## Rules for a stylesheet here

| Rule | Why |
|---|---|
| Body text at least 20px | Cards are reviewed on a phone too |
| Contrast ratio 4.5:1 or better, in both modes | Every card gets read in night mode eventually |
| Never colour-code meaning | Colour alone stops working the moment it is printed or dimmed |
| No web fonts | Anki renders offline; a missing font falls back mid-review |
