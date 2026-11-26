#!/usr/bin/env python3
"""The Printer Apology — make.fun bounty entry.

Writes one funny one-line apology from an office printer to
/output/entry.txt. Deterministic, stdlib only, no network.
"""

import os

# One line, at most 120 characters: an apology from the printer, with
# the printer's own gripes in it and the punch at the end. Revised:
# "blame me" lands the blame-shift harder than "act shocked".
LINE = (
    "Sorry I jammed mid-report \u2014 you feed me bargain paper and a tight "
    "deadline, then blame me when I choke."
)


def main() -> None:
    # Self-check against the gate: 1-120 characters, not only whitespace.
    if not 1 <= len(LINE) <= 120:
        raise ValueError("entry line must be 1-120 characters, got %d" % len(LINE))
    if not LINE.strip():
        raise ValueError("entry line must not be only whitespace")
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
