# 02 — Install Kolibri and set up the facility

| Field | Value |
|---|---|
| Status | `todo` |
| Depends on | 01 |
| Guide section | `docs/learning-stack-windows11-install.md` §2.1–2.2 |
| Estimated time | 30 min, most of it the first start |

## Goal

Kolibri installed, serving on `127.0.0.1:8080`, with a self-managed facility
and two accounts: a parent admin/coach and the learner. Installation and the
setup wizard are one task because the installer runs straight into the wizard.

## Steps

1. Download the Windows installer from `learningequality.org`. The guide was
   written against release **0.19.5** (published 2026-07-14) — record the
   version actually offered, it may have moved.
2. Run the `.exe` with administrator rights and select the installation
   language.
3. Accept the bundled Python 3 install/upgrade prompt when it appears.
4. Answer the Windows Firewall prompt for the Python process. **Allow access**
   is only needed to reach Kolibri from another device on the LAN; loopback
   works either way. Record which network profiles were allowed.
5. Wait out the first start — it runs database migrations and is slow. Do not
   kill the process. Kolibri opens the default browser at
   `http://127.0.0.1:8080`.
6. In the setup wizard, choose a **self-managed / personal** facility, not a
   school-managed one. It keeps the account model simple.
7. Create the two accounts:

   | Account | Role | Purpose |
   |---|---|---|
   | `parent` | Admin / Coach | Assigns lessons, reads the progress dashboard |
   | `<child>` | Learner | Daily use |

8. Confirm the listener is bound as expected:

   ```powershell
   Get-NetTCPConnection -LocalPort 8080 -State Listen |
     Select-Object LocalAddress, LocalPort, OwningProcess
   ```

## Done when

- [ ] `http://127.0.0.1:8080` loads the Kolibri UI
- [ ] Something is listening on port `8080`
- [ ] Both accounts can sign in
- [ ] The `parent` account sees the **Coach** section

## Record

| Item | Value |
|---|---|
| Kolibri version installed | |
| Guide says `0.19.5` — matched? | |
| Install path | |
| Data directory (`KOLIBRI_HOME`) | |
| Firewall: network profiles allowed | |
| Listener address on `8080` | |
| First-start duration | |
| Facility name and type | |
| Learner username | |

## Notes
