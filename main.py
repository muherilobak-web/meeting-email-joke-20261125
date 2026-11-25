#!/usr/bin/env python3
"""One-line joke entry for the make.fun bounty
"The Meeting That Should Have Been an Email".

Concept: a single participant ends the whole meeting with one
ordinary sentence at the close, revealing by a trivial fact that
the meeting never needed to happen at all.

Validation matters here because the bounty scores exactly one line
of text: any stray newline, trailing space, or control character
would make the entry read as a formatting slip instead of a joke,
so the writer guards the single line before it is ever written out.
"""

import os
import sys

ENTRY = "The meeting ended when Dave said, 'The client approved this last Tuesday,' and nine laptops closed at once."

MAX_LEN = 200


def validate(text):
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if not (1 <= len(text) <= MAX_LEN):
        raise ValueError("entry must be 1-200 characters")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must not contain control characters")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    return text


def main():
    text = validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != text:
        print("error: round-trip mismatch", file=sys.stderr)
        sys.exit(1)
    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
