"""One line to your younger self, for make.fun's bounty of the same name.

The line is a single original sentence: advice from an older self to the
kid who stays up late chasing two-dollar prizes, reframed as tuition for
the life being built. This program checks the line against the
competition gate (one line, 1-200 characters, not only whitespace) and
writes it verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt) for the judge.

Pure standard library; reads nothing outside this repository and uses no
network, no secrets and no environment beyond the output directory.
"""

import os
import sys

LINE = "Kid, the nights you spend chasing two-dollar prizes aren't wasted \u2014 they're the tuition for the life you're building."

MAX_CHARS = 200


def validate(text: str) -> None:
    """Raise ValueError if the line breaks the competition gate."""
    if not text.strip():
        raise ValueError("line is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"line is {len(text)} characters, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("line contains control characters")


def write_line(path: str, text: str) -> None:
    """Write the line, then read it back and confirm it survived verbatim."""
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise ValueError(f"read-back mismatch in {path}: {written!r} != {text!r}")


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    write_line(path, LINE)
    print(f"wrote {len(LINE)} characters to {path}")
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
