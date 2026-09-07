# 08 — Install the Anki MCP server

| Field | Value |
|---|---|
| Status | `todo` |
| Depends on | 06 (01 for Node.js) |
| Guide section | `docs/learning-stack-windows11-install.md` §4, §4.1 |
| Estimated time | 20 min |

## Goal

Claude Desktop can reach AnkiConnect through `@ankimcp/anki-mcp-server`,
installed read-only for now. Start with the bundle path; fall back to `npx`
only if it fails.

## Steps — Path A, MCPB bundle (preferred)

1. Download the latest `.mcpb` bundle from the GitHub Releases page of
   `ankimcp/anki-mcp-server`.
2. In Claude Desktop: `Settings → Extensions`, then drag and drop the file.
   The alternative route is
   `Settings → Developer → Extensions → Install Extension`.
3. Confirm the AnkiConnect URL. The default `http://localhost:8765` is correct
   for this setup.
4. Restart Claude Desktop.

The bundle ships its own dependencies, so this path does not depend on the
system Node.js install at all.

## Steps — Path B, npx via config file (fallback)

Edit `%APPDATA%\Claude\claude_desktop_config.json`, reachable from
`Settings → Developer → Edit Config`:

```json
{
  "mcpServers": {
    "anki-mcp": {
      "command": "npx",
      "args": ["-y", "@ankimcp/anki-mcp-server", "--stdio", "--read-only"],
      "env": {
        "ANKI_CONNECT_URL": "http://localhost:8765"
      }
    }
  }
}
```

If the server does not appear after a restart, `npx` did not resolve from
inside Electron — a common Windows failure. Install globally instead and point
the config at the binary:

```powershell
npm install -g @ankimcp/anki-mcp-server
```

```json
"command": "ankimcp",
"args": ["--stdio", "--read-only"]
```

## Read-only first

`--read-only` allows reads and review operations — sync, answering cards,
suspend and unsuspend — while blocking `addNote`, `deleteNotes`, `createDeck`
and `updateNoteFields`. Keep it on while evaluating the setup. Task 10 needs
it removed before Claude can write cards, so note here when it comes off.

## Version

The npm `latest` tag was **0.25.0** on 2026-09-07, while the project README
still said 0.22.0 and described itself as beta. Breaking changes are permitted
under `0.x`, so pin the version if this setup needs to hold for months.

## Done when

- [ ] The server is listed in Claude Desktop without an error badge
- [ ] Claude Desktop was restarted after the install
- [ ] The version installed is written down, not assumed

## Record

| Item | Value |
|---|---|
| Path used (A bundle / B npx / B global) | |
| Server version installed | |
| npm `latest` at install time | |
| Version pinned? | |
| `--read-only` active? | |
| Config file path used | |
| Node.js actually invoked (Path B only) | |

## Notes
