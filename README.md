[![make.fun](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![Rank](https://make.fun/badge/news-image-20261126/Darkarmy921/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126)
[![Reward](https://make.fun/badge/news-image-20261126/Darkarmy921/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126)

# THE WORLD TODAY — 26 November 2026

A program that writes one image summing up the world's news of
Thursday 26 November 2026: a 1024×1024 newspaper front page —
40 verified stories from 7 regions, led by the US plan for new
tariffs on 14 economies.

Built for the make.fun bounty
[news-image-20261126](https://make.fun/bounty/news-image-20261126).
Referral code: `ppee1fs7`.

## Run

```sh
python3 main.py
```

Writes `/output/entry.png` (1024×1024 PNG, under 1 MiB).
Deterministic: `main.py` copies the baked image with the standard
library only, so every run writes the same bytes. To rebuild the image
from the data, run `python3 render.py` (needs Pillow, local build only)
with `OUTPUT_PATH` set — that is how `entry.png` was made in this
session; the grader never runs it.

## How it works

- `stories.json` — the 40 verified stories (lead + 39), each with a
  headline, one-line summary, region and category.
- `render.py` — the in-session builder: draws the front page with
  Python PIL (local build only, not run by the grader) from
  `stories.json` into `entry.png`.
- `entry.png` — the finished front page, drawn in this session.
- `main.py` — entrypoint (standard library only): copies `entry.png`
  to `/output/entry.png`.
- `NOTES.md` — the source for every story, with publication dates.

## License

MIT — see `LICENSE`.
