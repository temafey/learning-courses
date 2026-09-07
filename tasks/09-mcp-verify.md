# 09 — Verify the MCP bridge

| Field | Value |
|---|---|
| Status | `todo` |
| Depends on | 07, 08 |
| Guide section | `docs/learning-stack-windows11-install.md` §4.2, §7 |
| Estimated time | 10 min |

## Goal

Prove the full chain — Claude Desktop → MCP server → AnkiConnect → collection
— and find where Claude Desktop actually writes MCP logs on Windows, which the
guide could only infer from the macOS path.

## Steps

1. Make sure Anki is running. Every tool call fails without it.
2. In Claude Desktop, ask:

   > List my Anki decks.

   A correct response returns the real deck list: `Default` plus the four
   `School::` decks from task 07.
3. Record how many tools the server exposes. The guide claims **50** — 39
   essential plus 11 GUI.
4. Find the log directory:

   ```powershell
   Get-ChildItem "$env:APPDATA\Claude\logs" -ErrorAction SilentlyContinue |
     Select-Object Name, Length, LastWriteTime
   ```

   Record whether the directory exists, and the exact file names — an
   `mcp.log` plus a per-server log is what the macOS layout produces. If it is
   not there, search for it rather than guessing:

   ```powershell
   Get-ChildItem "$env:APPDATA\Claude", "$env:LOCALAPPDATA\AnthropicClaude" `
     -Recurse -Filter "*mcp*.log" -ErrorAction SilentlyContinue |
     Select-Object FullName
   ```

5. On failure, work the §7 troubleshooting table. The common ones:
   `ERR_REQUIRE_ESM` means Node older than 22.12.0; a missing server means
   `npx` did not resolve from Electron; all tools failing means Anki is
   closed.

## Done when

- [ ] Claude Desktop returns the real deck list, not an error
- [ ] The tool count is recorded
- [ ] The Windows log path is recorded as found — or recorded as absent

## Record

| Item | Value |
|---|---|
| Deck list returned | |
| Tool count exposed | |
| Guide says 50 — matched? | |
| Log directory found at | |
| Log file names | |
| Errors hit and their fixes | |

Closes the guide's §8 entry *Windows log path `%APPDATA%\Claude\logs\`*,
currently `**Unverified**`.

## Notes
