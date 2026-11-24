#!/usr/bin/env python3
"""Writes the robot pickup line entry to entry.txt. Stdlib only."""

import os
import sys

ENTRY = "I scanned a million faces today and my system crashed on only one — yours. Give me one date and I will never need an update again."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(os.path.abspath(__file__))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0

if __name__ == "__main__":
    sys.exit(main())
