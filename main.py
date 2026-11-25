"""Exactly one word: the word grandma would text about AI.

Writes the word to /output/entry.txt for make.fun's
"One Word From Grandma" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = "Witchcraft"


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 30 characters, not only white space — and the brief asks
    # for exactly one word, nothing else.
    text = LINE.strip()
    assert 1 <= len(text) <= 30, "word must be 1-30 characters"
    assert len(text.split()) == 1, "entry must be exactly one word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
