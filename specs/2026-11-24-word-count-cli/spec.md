---
id: 2026-11-24-word-count-cli
title: Print the word count of a file named on the command line
short: word count cli
unit: 2026-11-23-word-count
status: verified
domain_gate: done
plan_reviewed:
  sha256: 106f626e4b38630ffce552291b359104f81bfff43d8432e9286328d6425b9906
  status: clean
  rounds: 1
  at: 2026-11-24T15:13:28Z
created: 2026-11-24
worktreePath: C:/Projects/Private/drive-scratch/.claude/worktrees/2026-11-24-word-count-cli
branch: feat/2026-11-24-word-count-cli
branchCreated: true
hardened:
  at: 2026-11-24T15:25:00Z
  by: implement-9.7
  status: clean
  depth: core
  base_sha: f037e5d30326396339c095ceaca089d976dac225
  diff_sha256: 176a43438570f972f19c14ce64586aaf4842b53824f9e00a6bb6e1ecf712b5c5
  files: 2
  lines: 92
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
