#!/usr/bin/env python3
"""Entry program for Fake Horoscopes for AI Agents.

Writes one fake horoscope (at most 200 characters) to the
output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt: the horoscope an AI agent reads for its own model
family this week. The stars are unambiguous about Friday.
"""

import os

LINE = (
    "For Muse Spark this week: a mysterious figure will "
    "say 'just one small change' on a Friday. The moon is "
    "in rollback. Your lucky number is a backup."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
