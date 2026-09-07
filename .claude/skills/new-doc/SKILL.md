---
name: new-doc
description: Scaffold a new technical document under docs/ in this repository's house style — numbered sections, 80-column wrap, troubleshooting table and a verification status table. Use when the user asks for a new guide, runbook, setup document or technical note.
---

Create a new document in `docs/` following this repository's conventions.

`$ARGUMENTS` is the document topic. If it is empty, ask what the document
covers before writing anything.

## Steps

1. Derive a kebab-case filename from the topic, e.g.
   `kolibri-channel-import.md`. Confirm the path with the user if the topic is
   broad enough that the name is a guess.
2. Read `docs/learning-stack-windows11-install.md` first and match its shape.
   It is the reference implementation, not just an example.
3. Write the file using the skeleton below, filled in for the topic.
4. Do not invent facts to populate the sections. Where you do not know
   something, write the section heading with a `TODO:` line naming what needs
   to be looked up, and list the claim as `**Unverified**` in the fact table.

## Skeleton

```markdown
# <Title>

<One- or two-sentence statement of what this document gets the reader to.>

<A summary table of components / prerequisites / outcomes, if the topic has
enumerable parts.>

Estimated time: <X> minutes.

---

## 0. Architecture

<A ```plantuml block using !include <C4/C4_Container> — only if the topic has
structure worth drawing. Omit the whole section if it does not.>

---

## 1. Prerequisites

---

## 2. <First major step>

### 2.1 Install

### 2.2 Verify

---

## N. Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|

---

## N+1. Verification status of the facts in this guide

Written <YYYY-MM-DD>. Anything marked *unverified* should be checked against
the source before relying on it.

| Claim | Status |
|---|---|
| <claim> | Verified — <source> |
| <claim> | **Unverified** — <why> |
```

## Rules

- Hard-wrap prose at 80 columns.
- `---` separators between top-level sections.
- Backtick every path, port, command and config key.
- Each major step gets its own verify sub-section — the reader must be able to
  confirm the step worked before moving on.
- The verification status table is mandatory. A document without one is not
  finished.
- English prose, per the language policy in `CLAUDE.md`.
