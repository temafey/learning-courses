# 01 — Prerequisites

| Field | Value |
|---|---|
| Status | `doing` |
| Depends on | — |
| Guide section | `docs/learning-stack-windows11-install.md` §1 |
| Estimated time | 10 min |

## Goal

Confirm the machine can host all three components before anything is
installed. Node.js and Claude Desktop were audited on 2026-09-07 and already
satisfy the guide; what remains is disk space and installer elevation.

## Steps

1. Check free space on the drive Kolibri will use. Channels are the bulk of
   the footprint — Khan Academy alone is large.

   ```powershell
   Get-PSDrive C | Select-Object Used, Free
   ```

2. Confirm the Windows account can elevate. The Kolibri and Anki installers
   both need administrator rights.
3. Re-confirm the toolchain. Node.js must be `22.12.0` or newer; Node 20 went
   end-of-life on 2026-04-30 and Node 24 is the current Active LTS.

   ```powershell
   node --version
   npm --version
   ```

4. Open Claude Desktop and confirm it is signed in.
5. Do **not** install Python. The Kolibri Windows installer bundles its own
   Python 3, and a separate install only creates ambiguity later.

## Done when

- [ ] At least 15 GB free on the target drive
- [ ] An installer can be run with administrator elevation
- [ ] `node --version` prints `v22.12.0` or newer
- [ ] Claude Desktop opens and is signed in

## Record

| Item | Value |
|---|---|
| Free disk on `C:` | |
| `node --version` | `v24.20.0` — checked 2026-09-07 |
| `npm --version` | `11.4.2` — checked 2026-09-07 |
| Claude Desktop version | `1.46388.4` — checked 2026-09-07 |
| Claude Desktop install path | `%LOCALAPPDATA%\AnthropicClaude` |
| Administrator elevation available | |

## Notes

Machine audit, 2026-09-07: Node.js `24.20.0` and Claude Desktop `1.46388.4`
were already present. Anki and Kolibri were not installed, and nothing was
listening on `127.0.0.1:8080` or `127.0.0.1:8765` — so every port check in
tasks 02 and 06 starts from a clean state.
