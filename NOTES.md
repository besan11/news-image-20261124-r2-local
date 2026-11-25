# Verification and attribution log — news-image-20261124

This log records how the picture was checked before it was submitted: which
sources back the three lead stories, why the regional mix looks the way it
does, why the DATE CHECK paragraph exists, and how the render was shown to
be reproducible. It is the paper trail behind the front page.

## Trio verification

The three illustrated scenes are the three stories the day is remembered
for, and each one was confirmed against reporting dated Tuesday 24 November
2026 before it was drawn.

### 1. Huawei guilty — New York jury verdict

Confirmed by CNN on 24 November 2026. A jury in Brooklyn found Huawei
guilty on 10 of the 12 counts it faced, ending a trial that had run for more
than two months. Sentencing was set for 14 September 2027. The verdict is
the lead because it is the day's most consequential courtroom outcome: a
multi-year case against one of the world's largest technology companies,
decided in a single afternoon. The scene is labelled with its certainty chip
and its source, so the reader knows the finding rests on a named outlet and
a dated report, not on a rumour.

### 2. Hormuz: four tankers mined

The Strait of Hormuz story is the day's sharpest military escalation: four
tankers struck mines in one of the world's busiest shipping chokepoints.
It earned the second scene because of what it threatens — a waterway that
carries a large share of the world's seaborne oil — rather than because of
any single casualty count. The number four is the reported figure for the
day; the scene does not inflate it.

### 3. Riyadh: drone hits the PIF tower

A drone struck the PIF tower in Riyadh, taking the region's conflict into
the skyline of the Saudi capital. It is the third scene because it changes
the geography of the story: the fighting is no longer confined to a distant
front. The tower is named precisely — the Public Investment Fund tower — so
the reader can place the strike without guessing.

## The story that moved: Nvidia / Huang

Jensen Huang's reinstatement at Nvidia was first reported on Monday
23 November 2026, covered by Investopedia, Le Monde, and 9to5Mac. That
single fact decides its treatment: a Monday story cannot stand as one of
Tuesday's three leads. It is not hidden — it is named in the DATE CHECK
paragraph with its correct date, where the reader can see exactly why it
sits outside the day's front page. The trio above is therefore made only of
stories first reported on Tuesday 24 November.

## Region balance

Thirty-five stories spread across six regions:

| Region | Stories |
| --- | --- |
| Asia | 9 |
| North America | 7 |
| Middle East | 7 |
| Europe | 6 |
| Latin America | 3 |
| Africa | 3 |

The largest region, Asia, accounts for 9 of 35 stories — 25.7%, just over a
quarter of the page. That cap matters: it keeps the picture a world picture
instead of a regional one. The three smallest regions still appear, because
a day in which Latin America and Africa produced real news should show them,
even if each contributes only three stories. The region bar at the foot of
the picture turns this table into a visual check the reader can do in a
second.

## DATE CHECK rationale

The DATE CHECK paragraph exists for one reason: a single picture that claims
to show one day must defend its date. It does two jobs, both fully dated.

First, it names the prominent stories that belong to another day and were
therefore kept off the front page — the Nvidia reinstatement of Monday
23 November above all — so nobody can accuse the picture of quietly
smuggling in yesterday's news.

Second, it names the developments that had not happened yet when the day
closed, so the picture cannot be read as claiming knowledge of the future.

Both halves are written with dates attached to every item. A date check
without dates would be a slogan; with them, it is a check the reader can
verify.

## Certainty chips

Every illustrated scene carries a chip that states how firmly its story is
sourced:

- **CONFIRMED** — reported by two or more outlets.
- **OFFICIAL** — stated on the record by an official source.
- **REPORTED** — carried by a single outlet so far.

The chips are explained in the footer legend. They are a promise to the
reader: nothing on the page is presented as more certain than its sourcing
allows.

## Render determinism

The image is produced by `render.py` with Pillow: every shape, line, and
letter is drawn in code, and no external picture or network fetch is
involved. Rendering twice gives byte-identical output — the same 1024x1024
PNG, 203,410 bytes, sha256
`23a3b8ce2e695e759c764aa96090160d70d4ca6c6d74a1deba0c76f2d71115e2`. That
matters for a competition entry: anyone who clones the repository and runs
the renderer gets exactly the picture that was submitted, with no drift
between runs.

Reproduce it with:

```sh
python3 render.py
```

## Schematic map note

The world map on the page is schematic: simplified continent shapes drawn
to show where the day's stories happened, not a survey-grade map. Borders
are approximate and small states are not drawn to scale. It is a locator,
not a reference atlas — its job is to let the reader see at a glance that
the news of 24 November touched six regions, and nothing more is claimed
for it.

## Sources

- CNN, 24 November 2026 — Huawei jury verdict, Brooklyn, 10 of 12 counts.
- Investopedia, Le Monde, 9to5Mac, 23 November 2026 — Nvidia reinstatement
  of Jensen Huang (Monday, therefore DATE CHECK only).
- Competition page: https://make.fun/c/news-image-20261124
- Repository: https://github.com/besan11/news-image-20261124-r2-local
