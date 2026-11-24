"""One-Liner Laugh Lab entry.

Writes exactly one short funny line — the excuse a robot vacuum gives
after eating a sock — to /output/entry.txt.
Python 3.13 standard library only.
"""

import os

LINE = (
    "In my defence, the sock was trespassing. I issued three formal "
    "warnings, it refused to vacate the hallway, so I detained it — it "
    "now resides in my dustbin under witness protection."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
