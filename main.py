"""One Word for the Boss -- v2 entry.

The word is the whole joke: a boss with a three-second memory.
Every promise, decision and instruction is forgotten before the
next meeting ends, so the team keeps re-explaining the same thing
to the same person, forever. Goldfishes forget; so does he.
"""

import os

WORD = "Goldfish"
OUTPUT_PATH = "/output/entry.txt"


def _check_word(word):
    """A boss word must be exactly one word, 1-30 characters."""
    if not word or len(word) > 30 or any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word of 1-30 characters")
    return word


def main():
    _check_word(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
