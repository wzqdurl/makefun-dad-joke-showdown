#!/usr/bin/env python3
"""Dad Joke Showdown — make.fun bounty entry.

Writes one original dad joke (at most 200 characters) to /output/entry.txt
and prints it to stdout. Deterministic: the same joke on every run.

The joke was written for this entry in this session. It is a single
self-contained program: no network, no input, no dependencies beyond the
Python 3 standard library.
"""

import os

JOKE = (
    "I told my son the moon throws shade at the sun every few years. "
    "He said, 'Dad, that's an eclipse.' "
    "I said, 'No, son, that's just the moon being shady.'"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
