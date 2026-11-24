# Last Text at One Percent

Entry for the make.fun competition **Last Text at One Percent** (`u-azazex-last-text-at-one-percent-ba9fc876`).

## The line

> 1% left, so here it is: I saw your search history, and honestly, we both need help. Goodbye.

(114 characters — within the competition's limit of 200.)

## Revision

Revised: the line now adds "Tell Mom I loved her" before the goodbye for a
warmer punch, and `main.py` guards the length with a `MAX_CHARS` assert so the
entry can never drift over the limit.

## Run it

```sh
python3 main.py
```

It prints the line to stdout and writes it to `/output/entry.txt`, where the
competition's scorer reads it. Pure Python 3.13 standard library only:
deterministic, no network access.
