# 13 — Add the filesystem MCP server

| Field | Value |
|---|---|
| Status | `todo` |
| Depends on | 09 |
| Guide section | `docs/engagement-system.md` §0, §11 |
| Estimated time | 15 min |

## Goal

Claude Desktop can read and write the five content folders in this repository,
and nothing else on the disk. Without this the engagement layer has no memory
between chats.

## Steps

1. Add the server to `%APPDATA%\Claude\claude_desktop_config.json`, alongside
   the existing `anki-mcp` entry. Pass every allowed folder as an argument —
   the server exposes only the directories listed here.

   ```json
   {
     "mcpServers": {
       "learning-files": {
         "command": "npx",
         "args": [
           "-y", "@modelcontextprotocol/server-filesystem",
           "C:\\Users\\temaf\\OneDrive\\Documents\\Projects\\TymurLearningCources\\state",
           "C:\\Users\\temaf\\OneDrive\\Documents\\Projects\\TymurLearningCources\\logs",
           "C:\\Users\\temaf\\OneDrive\\Documents\\Projects\\TymurLearningCources\\rewards",
           "C:\\Users\\temaf\\OneDrive\\Documents\\Projects\\TymurLearningCources\\prompts",
           "C:\\Users\\temaf\\OneDrive\\Documents\\Projects\\TymurLearningCources\\curriculum"
         ]
       }
     }
   }
   ```

2. Do **not** pass the repository root. `docs/`, `.git/` and `.claude/` have no
   business being writable from a tutoring session.
3. If `npx` does not resolve from inside Electron — the same Windows failure as
   task 08 — install globally and use the binary name:

   ```powershell
   npm install -g @modelcontextprotocol/server-filesystem
   ```

   The binary is `mcp-server-filesystem`; the folder arguments stay the same.
4. Restart Claude Desktop.
5. Ask it to read `state/today.md` and then to append a line to a scratch file
   in `logs/`. Delete the scratch file afterwards.
6. Confirm the boundary holds: ask it to read `docs/engagement-system.md`. It
   should fail.

## Done when

- [ ] The server appears in Claude Desktop without an error badge
- [ ] Reading `state/today.md` works
- [ ] Writing into `logs/` works
- [ ] Reading anything outside the five folders fails

## Record

| Item | Value |
|---|---|
| Server version installed | |
| Path used (npx / global) | |
| Folders passed as arguments | |
| Read outside the allow-list refused? | |
| OneDrive path caused problems? | |

The last row is worth watching. The repository lives under OneDrive, so a file
written by Claude Desktop and a file synced by OneDrive can collide. If logs
start showing conflicted copies, that is why.

## Notes
