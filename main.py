#!/usr/bin/env python3
"""One-Line Laugh-Off entry: writes exactly one joke line to /output/entry.txt.

Gate: the line is 102 characters / 102 bytes, one line, no trailing newline.
"""
import os

LINE = "I told my GPS I was lost, and it sighed, recalculated, and filed for custody of my sense of direction."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
