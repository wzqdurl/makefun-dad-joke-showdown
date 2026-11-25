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

# The bounty gate: UTF-8 text of 1 to 200 characters, not only whitespace.
# Fail loudly instead of shipping an entry the gate would refuse.
assert JOKE and not JOKE.isspace() and len(JOKE) <= 200, (
    f"joke violates the 1-200 character gate: {len(JOKE)} characters"
)
assert "\n" not in JOKE, "joke must be a single line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
