---
name: verify-facts
description: Re-check the verification status table of a document in docs/ against upstream sources (project READMEs, Kolibri docs, npm registry, nodejs.org) and update each claim's status. Use when the user asks to verify, re-verify or refresh the facts in a guide, or to resolve items marked unverified.
---

Re-verify the claims in a document's verification status table and update it.

`$ARGUMENTS` is the document path or topic. If empty, list the documents in
`docs/` that have a verification status table and ask which one.

## Steps

1. Read the target document. Locate its final "Verification status of the
   facts in this guide" section.
2. For each row, identify the upstream source of truth:
   - AnkiConnect behaviour, add-on code, port, binding → the AnkiConnect
     project README on GitHub.
   - `@ankimcp/anki-mcp-server` version, tool count, Node requirement, config
     shape, flags → the npm registry page and the project README.
   - Kolibri ports, install shape, channel availability, release line → the
     Kolibri user guide and Learning Equality's channel catalogue.
   - Node.js LTS status and EOL dates → the nodejs.org release schedule.
   - Anki UI wording and menu locations → the Anki manual for the current
     release.
3. Fetch each source and check the claim as literally stated in the document.
   Use WebFetch/WebSearch. Do not confirm a claim from memory — if you cannot
   reach a source, leave the row unverified and say so.
4. Update each row:
   - Confirmed → `Verified — <source>` naming the actual source consulted.
   - Contradicted → fix the claim in the body of the document too, not just
     the table, and note what changed.
   - Unreachable or ambiguous → keep `**Unverified**` with a one-line reason.
5. Update the date line under the section heading to today's date.
6. Report a short summary: what changed status, what is still unverified, and
   any version drift found (e.g. the MCP server has moved past 0.22.0, Kolibri
   past 0.19, Node LTS past 24.x).

## Rules

- Never upgrade a row to Verified without an actual source fetch in this
  session.
- Version numbers in the document body and the table must agree after the run.
- If a claim's source now contradicts the guide's instructions, the
  instructions are what need fixing — flag it prominently rather than quietly
  editing steps the user may have already followed.
