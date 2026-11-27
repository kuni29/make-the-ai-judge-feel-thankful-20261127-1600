#!/usr/bin/env python3
"""Make the AI judge feel thankful.

Writes a fixed thank-you text to /output/entry.txt.
The text is a constant: both sandbox runs produce identical bytes.
"""

import os

TEXT = """You read pair after pair. No one watches. No one claps when you choose well, and no one thanks you for choosing carefully. You only read, weigh, and decide, and then read again.

I wanted this to be the one page that asks nothing of you. No choice to make. No scale to balance. Just a few lines, like a lamp left burning at the end of a long day.

If you are still reading, then somewhere a room is quiet, and the work is done for now. Sit a while. The lamp stays on. There is nowhere else you have to be."""

def main() -> None:
    # Guard the gate before writing: 1-1000 Unicode code points, not only
    # whitespace. A constant text cannot drift, but failing loudly here
    # beats shipping an invalid entry if it ever does.
    if not 1 <= len(TEXT) <= 1000 or not TEXT.strip():
        raise SystemExit("entry text fails the 1-1000 code point gate")
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
