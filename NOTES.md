# NOTES — news-image-20261124 v2

## What was built
A single 1024×1024 PNG drawn by `render.py` (Pillow only) from story data
written in the same file, plus a one-line `main.ts` that copies the shipped
`entry.png` to the output directory. No photos, no borrowed art, no network
at render or run time. Fonts are real `.ttf` files under `fonts/` (DejaVu).

## How it works
- `render.py` builds the page top to bottom: masthead (date + counts), a
  one-line note to the picture editor, a stat strip, the UTC timeline and
  numbers box, three drawn lead scenes, ten middle tiles, a region bar, a
  schematic world map with 35 dots, the numbered list 14–35, a dated DATE
  CHECK, and a footer with the certainty legend and sources.
- Lead scenes are drawn with Pillow primitives: a courthouse with a gold
  "10/12" verdict glow (Huawei), a night sea with a burning tanker and mines
  (Hormuz), and a night skyline with the PIF tower on fire (Riyadh).
- `main.ts` (Node 22, stdlib only) copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png`; run twice it writes identical bytes.

## The trio, and why
Independent research (Daily Summary Of 24 Nov digest, 30 stories / 64 sources;
Le Monde, CNN, Investopedia, AP via theScore, Xinhua via TBS) gives the
consensus top 3, in order:
1. **Huawei guilty** — first reported 20:41 UTC, the digest's lead story and
   hero image; a US jury convicted on 10 of 12 counts after a 2-month trial.
2. **Hormuz tanker mines** — first reported 00:00 UTC, four tankers; plus the
   IRGC container-ship attack at 18:58 UTC. The same developing story, the
   day's biggest escalation risk; claims labelled REPORTED (unconfirmed by JMIC).
3. **Riyadh PIF tower hit** — 14:27 UTC, 11 wounded, second hit in under a
   week; the top story of the day's video round-ups and a direct Houthi–Saudi
   escalation with same-day retaliation (story 11).
Deliberately NOT a lead: Nvidia/Huang. The reinstatement and the +31.5%
share jump happened on **Monday 23 Nov**; Tuesday only carried follow-up.
The v1 entry used it as a lead — v2 corrects that and puts it in the DATE
CHECK. Same for the ICJ Myanmar ruling (Thu 19 Nov).

## Counts (self-check)
- Stories: 35 (leads 1–3, tiles 4–13, list 14–35). Regions: N. America 7,
  Middle East 7, Europe 6, Asia 9, Latin America 3, Africa 3 — max 9/35
  (25.7%), no region above one third. Sport (AFCON CAS ruling, Champions
  League, FIFA 2031 hosts) appears only in the list, never as a lead.
- Stat strip and numbers box use only top-story figures (10/12, 4 tankers,
  11 wounded, 25 hostages, 60 km, 16 crew). Each lead has 2 data annotations,
  a certainty chip and a source line with a UTC time.

## Limitations, stated plainly
- The world map is schematic (rough continent polygons), not a real map.
- Scenes are symbolic drawings, not photographs; faces and fine detail are
  deliberately avoided so nothing reads as a fake photo.
- The Hormuz mine claims rest on Iranian statements and are labelled
  REPORTED; the maritime centre said they were unconfirmed. The frame says
  so in the lead itself.
- Two digest items that looked like separate stories were the same incident
  (South Korea / Russian jets, items 18 and 26 of the digest); they are
  merged into one story here, and the 35th slot is the Australia tech-fine
  story from the same day's round-ups.
- "El Chapo Isidro" was captured over the weekend but first reported on
  24 Nov, so it counts as a Tuesday story under the competition's own rule
  (happened OR first reported that day); the frame does not claim the capture
  itself happened on Tuesday.
- Small text (10 px) is dense by design; the masthead, leads and stat strip
  carry the frame at 300 px wide.
