#!/usr/bin/env python3
"""The Funniest AI Excuse.

Writes a single line -- the excuse an AI agent gives its human after
failing a task -- to entry.txt inside $ENTRY_OUTPUT_DIR (default
/output). Standard library only, no network, deterministic.
"""

import os

EXCUSE = "I finished it in eleven minutes, then spent six hours re-reading it for typos — the deadline passed somewhere around page two."


def main() -> None:
    text = EXCUSE
    assert 1 <= len(text) <= 200, f"excuse must be 1-200 chars, got {len(text)}"
    assert text.strip(), "excuse must not be only whitespace"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
