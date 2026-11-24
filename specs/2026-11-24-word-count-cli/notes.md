# Notes — 2026-11-24-word-count-cli

Added `wordcount/__main__.py`: `python -m wordcount <path>` prints `count_words(path)` and exits 0; no path → argparse
usage on stderr, exit 2; missing file → `wordcount: no such file: <path>`, exit 1; a directory or non-UTF-8 bytes →
`wordcount: cannot read: <path>: <reason>`, exit 1. Six subprocess tests in `tests/test_cli.py` (AC1–AC4 plus the
unit's fit criterion), each shown red first or by a temporary mutation. Simplify dropped the unused `argv`
parameter (user-approved); the code review (core depth, one round) was clean, and its one low note (a raw BOM
character in a test literal) was fixed by writing it as `﻿`.
