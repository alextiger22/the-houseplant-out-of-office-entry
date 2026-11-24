"""Out-of-office reply written by a houseplant.

The program holds a single line — a houseplant's out-of-office message —
and writes it to the output file exactly as given.
"""

import os
import sys

ENTRY = "Out of office: I am a houseplant. I have no hands, no inbox, and no intention of replying. Please water me."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    # Validate the output: one UTF-8 line, 1-120 characters, exact match.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    lines = written.split("\n")
    if len(lines) != 1:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(written) <= 120:
        print(
            f"error: entry is {len(written)} characters, expected 1-120",
            file=sys.stderr,
        )
        return 1
    if written != ENTRY:
        print("error: entry does not match the expected line", file=sys.stderr)
        return 1
    print(f"Wrote out-of-office reply ({len(ENTRY)} characters) to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
