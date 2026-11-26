#!/usr/bin/env python3
"""One-Line Laugh-Off entry: writes exactly one joke line to /output/entry.txt.

Gate: the line is 112 characters / 112 bytes, one line, no trailing newline.
"""
import os

LINE = "I asked my GPS for the fastest route home, and it sighed, recalculated, and suggested I just move closer to work."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
