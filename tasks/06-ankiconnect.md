# 06 — Install and verify AnkiConnect

| Field | Value |
|---|---|
| Status | `todo` |
| Depends on | 05 |
| Guide section | `docs/learning-stack-windows11-install.md` §3.2–3.4 |
| Estimated time | 10 min |

## Goal

AnkiConnect installed and answering on `127.0.0.1:8765`, still bound to
loopback. This API has no authentication — the binding is the only thing
keeping the collection private.

## Steps

1. `Tools → Add-ons → Get Add-ons...`
2. Enter the add-on code **`2055492159`**, click OK, restart Anki when
   prompted.
3. If Windows Firewall prompts for Anki, note the answer. AnkiConnect only
   needs loopback, so blocking the LAN is fine and is the safer answer.
4. Open `http://localhost:8765` in a browser — the add-on replies with
   `Anki-Connect`.
5. Probe the API directly:

   ```powershell
   Invoke-RestMethod -Uri http://127.0.0.1:8765 -Method Post `
     -ContentType 'application/json' `
     -Body '{"action":"version","version":6}'
   ```

6. Open `Tools → Add-ons → AnkiConnect → Config` and confirm
   `webBindAddress` is `127.0.0.1`. **Leave it alone.** Exposing this API to
   the LAN gives anyone on the network full write access to the collection.
7. Confirm the binding from outside the app:

   ```powershell
   Get-NetTCPConnection -LocalPort 8765 -State Listen |
     Select-Object LocalAddress, LocalPort, OwningProcess
   ```

## Done when

- [ ] `http://localhost:8765` shows `Anki-Connect`
- [ ] The `version` probe returns a result
- [ ] The listener is on `127.0.0.1`, not `0.0.0.0`
- [ ] `webBindAddress` is unchanged from the default

## Record

| Item | Value |
|---|---|
| AnkiConnect version / release date | |
| `version` action result | |
| `webBindAddress` value | |
| `webCorsOriginList` value | |
| Listener address on `8765` | |
| Firewall answer for Anki | |

## Notes

Anki must stay running for anything downstream to work — every MCP tool call
fails with a connection error when it is closed. Task 11 puts it in Startup
Apps.
