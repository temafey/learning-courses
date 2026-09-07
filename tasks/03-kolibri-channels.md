# 03 — Import Kolibri content channels

| Field | Value |
|---|---|
| Status | `todo` |
| Depends on | 02 |
| Guide section | `docs/learning-stack-windows11-install.md` §2.3 |
| Estimated time | 20 min of clicking, plus download time |

## Goal

Subject content available offline, imported as topic-level subtrees rather
than whole channels. This task also settles whether these channels carry any
Ukrainian or Russian material — the one thing the guide could not establish
from upstream sources.

## Steps

1. Sign in as `parent` and go to
   `Device → Channels → Import → Kolibri Studio (online)`.
2. Before importing anything, walk the catalogue with the language filter set
   to Ukrainian, then Russian, and record what each candidate channel offers.
   The public catalogue API ignored the `languages` filter when the guide was
   written, so the Kolibri UI is the authority here, not the API.
3. Import **selectively**. Full channels run to tens of gigabytes; select the
   topic subtrees that match the current school term.
4. Candidate channels from the guide:

   | Channel | Use |
   |---|---|
   | Khan Academy | Math, physics, chemistry |
   | Open Stax | Openly licensed textbooks — two words in the catalogue |
   | CK-12 | STEM exercises |
   | Blockly Games | Programming introduction |
   | EngageNY | Math curriculum sequences |

5. After the import finishes, check the disk cost against what task 01
   recorded as free.

## Done when

- [ ] At least one channel is imported and its content appears on the Learn
      page
- [ ] Every channel row in **Record** has its Ukrainian/Russian finding filled
      in, including the negative ones
- [ ] Free disk space is still comfortable for the remaining terms

## Record

| Item | Value |
|---|---|
| Channels and subtrees imported | |
| Khan Academy — uk/ru content | |
| Open Stax — uk/ru content | |
| CK-12 — uk/ru content | |
| Blockly Games — uk/ru content | |
| EngageNY — uk/ru content | |
| Other channels found with uk/ru content | |
| Disk consumed by the import | |

Closes the guide's §8 entry *Ukrainian / Russian localized channel coverage*,
currently `**Unverified**`.

## Notes
