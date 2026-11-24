---
id: 2026-11-24-word-count-cli
title: Print the word count of a file named on the command line
short: word count cli
unit: 2026-11-23-word-count
status: grilled
domain_gate: done
created: 2026-11-24
---

`python -m wordcount <path>` prints the word count of the file at `path`, as S1's `count_words(path)` returns it,
followed by a newline, and exits 0.

## Out of scope

- Counting itself (S1).
- More than one path, reading standard input, and flags beyond the one path argument.

## Success criteria

- **AC1** — Given a file holding `one two three\n`, When `python -m wordcount <path>` runs, Then it prints `3\n` to
  standard output and exits 0.
- **AC2** — Given no path argument, When `python -m wordcount` runs, Then it prints a usage line to standard error
  and exits 2.
- **AC3** — Given a path with no file, When `python -m wordcount <path>` runs, Then it prints
  `wordcount: no such file: <path>` to standard error, `<path>` exactly as given, prints nothing to standard
  output, and exits 1.
- **AC4** — Given a directory, or a file holding bytes that are not UTF-8, When `python -m wordcount <path>` runs,
  Then it prints one line starting `wordcount: cannot read: <path>` to standard error, no traceback, nothing to
  standard output, and exits 1.

Tests run the module as a subprocess, `[sys.executable, '-m', 'wordcount', ...]`, from the repo root.
