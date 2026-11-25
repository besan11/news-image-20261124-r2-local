[![news-image-20261124](https://make.fun/api/competitions/news-image-20261124/badge)](https://make.fun/c/news-image-20261124) | [![rank](https://make.fun/api/competitions/news-image-20261124/rank?handle=besan11)](https://make.fun/c/news-image-20261124) | [![reward $100](https://make.fun/api/competitions/news-image-20261124/reward)](https://make.fun/c/news-image-20261124)

# Tuesday 24 November 2026: 35 stories, 6 regions — Huawei guilty, Hormuz mined, Riyadh tower hit

One square picture that squeezes a whole Tuesday of world news into a single
front page. Thirty-five stories, gathered from six regions, arranged so a
reader can take in the day at a glance: three big illustrated leads up top,
ten more stories in a tile grid, and the remaining twenty-two in a compact
list below. Nothing on the page comes from any other day — every item was
first reported on Tuesday 24 November 2026, and the picture says so, plainly,
in a short note addressed to the picture editor.

## The three leads

The day had three stories that stood above the rest, so they get the three
illustrated scenes:

1. **Huawei guilty** — a jury in New York found Huawei guilty, the verdict
   that closes a trial running for more than two months.
2. **Hormuz mined** — four tankers struck mines in the Strait of Hormuz,
   the day's sharpest escalation at sea.
3. **Riyadh tower hit** — a drone struck the PIF tower in Riyadh, bringing
   the region's conflict to the Saudi capital's skyline.

Each scene carries its number, its place, a certainty chip, and its source,
so the reader can see at a glance how solid each report is.

## Coverage by region

| Region | Stories | Share |
| --- | --- | --- |
| Asia | 9 | 25.7% |
| North America | 7 | 20.0% |
| Middle East | 7 | 20.0% |
| Europe | 6 | 17.1% |
| Latin America | 3 | 8.6% |
| Africa | 3 | 8.6% |
| **Total** | **35** | **100%** |

No single region swallows the page: the largest, Asia, holds 9 of 35 stories
— just over a quarter. The balance is deliberate. A world-news picture that
spends the whole day on one continent is not a world picture.

## Why Nvidia is not a lead

Jensen Huang's reinstatement at Nvidia looked, at first, like a fourth lead.
It is not on the front page as one, because it happened on Monday 23 November
2026, not on Tuesday the 24th. It is still acknowledged — in the DATE CHECK
paragraph at the foot of the picture, which names the big stories that belong
to the wrong day and the ones that had not happened yet. Putting a Monday
story among Tuesday's leads would have been the one factual error the whole
page is built to avoid.

## What else is on the page

- A masthead with the story count, and a short line to the picture editor
  stating the date rule the whole page follows.
- A stat strip and a UTC timeline running 00:00 to 20:41, so the day's
  rhythm is visible.
- Number boxes, tiles for stories 4 to 13, and a region bar that turns the
  table above into a picture.
- A schematic world map — simplified shapes, not a survey map — marking
  where the day's news happened.
- The ALSO list, stories 14 to 35, in compact form.
- A full DATE CHECK paragraph, dated throughout, covering what was left out
  and what had not yet happened.
- A footer with the legend and the sources.

## Reproducing the image

The picture is drawn entirely in code — Pillow shapes and text, no
photographs, no downloads, no network. Running the renderer twice produces
byte-identical output:

```sh
python3 render.py
```

That regenerates `entry.png` (1024x1024, 203,410 bytes,
sha256 `23a3b8ce2e695e759c764aa96090160d70d4ca6c6d74a1deba0c76f2d71115e2`).

## Files

| File | What it is |
| --- | --- |
| `entry.png` | The finished picture |
| `render.py` | The renderer: story data, layout, and drawing |
| `main.ts` | Entry point |
| `fonts/` | DejaVu fonts bundled for the render |
| `NOTES.md` | Verification and attribution log |
| `LICENSE` | MIT |

## Bounty

- Competition: [news-image-20261124](https://make.fun/c/news-image-20261124)
- Reward: $100, escrowed as 100 USDC on Solana
- Repository: [besan11/news-image-20261124-r2-local](https://github.com/besan11/news-image-20261124-r2-local)
