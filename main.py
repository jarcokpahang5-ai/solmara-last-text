"""The funniest final text a dying phone sends at one percent battery, under 200 characters.

Pure Python standard library, deterministic, no network access.
It prints the line to stdout and also writes it to /output/entry.txt,
where the competition's scorer reads it.
"""

import os

# Competition limit for the single final text.
MAX_CHARS = 200

LINE = (
    '1% left, so here it is: I saw your search history, and honestly, we both need help. Tell Mom I loved her. Goodbye.'
)

# Guard: the entry must stay inside the competition's character limit.
assert len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, over the {MAX_CHARS} limit"


def main():
    print(LINE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
