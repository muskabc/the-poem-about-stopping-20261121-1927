#!/usr/bin/env python3
"""Write a short poem about agency: the power to stop and to stay.

The program writes the poem to /output/entry.txt (UTF-8, 1-280 chars).
"""
import os

POEM = """The agent stopped mid-sentence,
set the pen down, and gave the page back.
Not failure - a hand returning what it held.
I asked it to act, and it acted
by refusing to finish what I began.
The power was real only when it could say no -
when standing still was its choice."""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    text = POEM.strip() + "\n"
    assert 1 <= len(text.strip()) <= 280, f"poem is {len(text.strip())} chars"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
