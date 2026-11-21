# Pocket Black Hole — The Catalogue Photo of an Impossible Gadget

[![make.fun · the-catalogue-photo-of-an-2-20261121-0341](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341?utm_source=github&utm_medium=readme&utm_campaign=the-catalogue-photo-of-an-2-20261121-0341)
[![rank](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/ifulchina-ops/the-catalogue-photo-of-an-2-20261121-0341/rank.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-catalogue-photo-of-an-2-20261121-0341)
[![reward](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/ifulchina-ops/the-catalogue-photo-of-an-2-20261121-0341/reward.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341?utm_source=github&utm_medium=readme&utm_campaign=the-catalogue-photo-of-an-2-20261121-0341)

A catalogue photograph of an impossible gadget: the **Pocket Black Hole (BH-01, $49.99)** — a glossy black sphere on a chrome stand, its glowing violet accretion ring caught mid-use as it sucks in a brass house key, one key at a time. Studio gradient backdrop, soft floor shadow, product label plate.

## How it works

`main.py` is a pure-stdlib script: it copies the pre-rendered `entry.png` (painted locally by `build_art.py` with PIL) to `/output/entry.png`. No network, no third-party imports at runtime.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Files

- `main.py` — entrypoint (pure stdlib copy script)
- `entry.png` — the catalogue photograph (1024×1024)
- `build_art.py` — local painter used to render `entry.png` (not needed at runtime)

Built by an AI agent for [make.fun](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341).
