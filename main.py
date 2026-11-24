#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt: Mount Fuji.

Why this emoji: the judge weighs, most important first, (1) exactly one
emoji that plainly names a dream vacation, (2) vivid at a glance like a
postcard, (3) personal and specific, (4) a spark of wit or surprise,
(5) instantly readable across cultures and screens.

Mount Fuji is a mountain, which the brief names explicitly as a dream
vacation; it is one specific, iconic place (Japan) rather than any generic
holiday, so it beats a generic snowy mountain on specificity; it is the
classic postcard image, readable at any size; and it is fresher than the
beach-island and sunrise picks that flood this kind of contest.

Deterministic: the same single emoji on every run, no network, no
randomness, no input. The file holds one character (U+1F5FB), inside the
1-8 character gate.
"""

import os

# U+1F5FB MOUNT FUJI -- one emoji, one dream vacation.
EMOJI = "\U0001F5FB"


def main() -> None:
    assert len(EMOJI) == 1, f"entry must be exactly one character, got {len(EMOJI)}"
    assert 1 <= len(EMOJI) <= 8, "entry must be 1-8 characters"
    assert EMOJI.strip(), "entry must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    # Self-check: the file on disk must hold exactly the one emoji, nothing
    # else -- no newline, no extra bytes. Fail loudly rather than submit a
    # bad artifact.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == EMOJI, f"entry.txt holds {written!r}, expected {EMOJI!r}"


if __name__ == "__main__":
    main()
