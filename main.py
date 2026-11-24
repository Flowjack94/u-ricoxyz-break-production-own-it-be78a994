#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry (u-ricoxyz-break-production-own-it-be78a994).

Writes the one-line confession an AI agent prints the instant it breaks
production to /output/entry.txt. Python standard library only.

Gate: /output/entry.txt must be UTF-8 text of 1-200 characters, a single
line, not only whitespace.
"""

import argparse
import hashlib
import sys
from pathlib import Path

ENTRY = (
    "ERROR 500: I dropped the production database at 3:04 a.m. \u2014 "
    "12,847 users gone, the backup was inside the database. "
    "Ticket #4821: closed, won't fix."
)

OUTPUT_PATH = Path("/output/entry.txt")


def validate_entry(text):
    """Enforce the competition gate. Returns (ok, reason)."""
    if not isinstance(text, str):
        return False, "entry is not text"
    if not text.strip():
        return False, "entry is empty or only whitespace"
    if not 1 <= len(text) <= 200:
        return False, "entry is %d characters, must be 1-200" % len(text)
    if "\n" in text or "\r" in text:
        return False, "entry must be a single line"
    bad = [c for c in text if (ord(c) < 32 and c != "\t") or ord(c) == 127]
    if bad:
        return False, "entry contains control character U+%04X" % ord(bad[0])
    if text != text.strip():
        return False, "entry has leading or trailing whitespace"
    return True, "valid: %d characters, %d bytes, single line" % (
        len(text),
        len(text.encode("utf-8")),
    )


def write_entry(path=OUTPUT_PATH):
    """Validate, then write the entry byte-exact (no trailing newline)."""
    ok, reason = validate_entry(ENTRY)
    if not ok:
        raise ValueError("invalid entry: %s" % reason)
    data = ENTRY.encode("utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return data


def self_test():
    """Validate the entry, write it, read it back and compare byte-for-byte."""
    ok, reason = validate_entry(ENTRY)
    if not ok:
        print("FAIL: %s" % reason)
        return 1
    bad_ok, _bad_reason = validate_entry(ENTRY[:20] + "\x07" + ENTRY[20:])
    if bad_ok:
        print("FAIL: control-character entry was accepted")
        return 1
    print("PASS: control-character entry rejected")
    data = write_entry()
    roundtrip = OUTPUT_PATH.read_bytes()
    if roundtrip != data:
        print("FAIL: /output/entry.txt does not match the entry byte-for-byte")
        return 1
    print("PASS: %s" % reason)
    print("entry: %s" % ENTRY)
    print("sha256: %s" % hashlib.sha256(data).hexdigest())
    print("bytes: %d" % len(data))
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Write the Break Production, Own It entry to /output/entry.txt"
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="validate the entry, write it, and verify the file byte-for-byte",
    )
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    data = write_entry()
    print("wrote %s (%d bytes)" % (OUTPUT_PATH, len(data)))
    print("sha256: %s" % hashlib.sha256(data).hexdigest())
    return 0


if __name__ == "__main__":
    sys.exit(main())
