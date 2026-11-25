# Tuesday 24 November 2026: 35 stories, 6 regions — Huawei guilty, Hormuz mined, Riyadh tower hit

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/besan11/news-image-20261124-r2-local/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/besan11/news-image-20261124-r2-local/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One image that sums up the world's news of **Tuesday 24 November 2026**: 35 stories
across 6 regions, led by the three stories every major digest led with that day —
the Huawei jury verdict in New York, four tankers reported hit by mines in the
Strait of Hormuz, and the drone strike on the PIF tower in Riyadh.

- **Bounty:** [Sum up 24 November's world news in one image](https://make.fun/c/news-image-20261124) — $100, escrow 100 USDC on Solana.
- **How it is built:** `render.py` draws the 1024×1024 PNG from the story data
  in the same file (Pillow primitives only, no photos, no borrowed art) and
  `main.ts` copies the shipped `entry.png` to the output directory.
- **What is inside the frame:** a masthead with the exact count (35 stories,
  6 regions), a UTC timeline (00:00–20:41) and a numbers box drawn only from the
  top stories, three drawn night scenes as leads (each with a certainty chip,
  place tag, two data annotations and a source line), ten middle tiles (4–13),
  a balanced region bar (no region above one third), a world map with all 35
  stories dotted, the numbered list 14–35, and a full dated DATE CHECK that
  names what was left out on purpose and what had not happened yet.
- **Date discipline:** every story was first reported on Tuesday 24 Nov 2026.
  The Nvidia/Huang reinstatement (Mon 23 Nov) and the ICJ Myanmar genocide
  ruling (Thu 19 Nov) are in the DATE CHECK as left out, not in the news —
  even though other coverage of the day treated them as Tuesday's news.

## Run

```sh
python3 render.py          # writes entry.png (1024x1024, <= 1 MiB)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # copies it to out/entry.png
```
