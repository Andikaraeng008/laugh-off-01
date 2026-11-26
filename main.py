#!/usr/bin/env python3
"""One-Line Laugh-Off entry: writes exactly one joke line to /output/entry.txt.

Gate: the line is 112 characters / 112 bytes, one line, no trailing newline.
"""
import os

LINE = "I asked the self-checkout for help; it printed a receipt longer than my arm and wished me luck finding the exit."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
