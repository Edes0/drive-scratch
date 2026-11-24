---
id: 2026-11-24-word-count-function
title: Count the words in a text file
short: word count function
unit: 2026-11-23-word-count
status: verified
domain_gate: done
plan_reviewed:
  sha256: 2b5a3e049623daa4b3986bc0ec3f83b492376efbfb510926b1d7670dd7795abc
  status: clean
  rounds: 2
  at: 2026-11-24T12:27:39Z
hardened:
  at: 2026-11-24T12:33:35Z
  by: implement-9.7
  status: clean
  depth: core
  base_sha: 80c4a3423d7829fbe2c8645a804a9d068b172105
  diff_sha256: 743ee9ebb19f510c05cea7990cc8f3fc8f4d9d28ad03ed2406f1e59509a6a6cc
  files: 2
  lines: 47
created: 2026-11-24
worktreePath: C:/Projects/Private/drive-scratch/.claude/worktrees/2026-11-24-word-count-function
branch: feat/2026-11-24-word-count-function
branchCreated: true
---

`wordcount.count_words(path)` returns the number of words in the UTF-8 text file at `path`, read with encoding
`utf-8-sig`. A word is a run of non-whitespace characters: the count is `len(text.split())`. Errors are not caught:
a missing file, a directory or bytes that are not UTF-8 raise the `OSError` or `UnicodeDecodeError` Python gives.

## Out of scope

- The command line entry and its error messages (S2).
- Encodings other than UTF-8.

## Success criteria

- **AC1** — Given a file holding `one two  three\nfour\n`, When `count_words(path)` runs, Then it returns `4`.
- **AC2** — Given an empty file, When `count_words(path)` runs, Then it returns `0`.
- **AC3** — Given a path with no file, When `count_words(path)` runs, Then it raises `FileNotFoundError`.
- **AC4** — Given a file starting with a UTF-8 byte-order mark and holding `hello world`, When `count_words(path)`
  runs, Then it returns `2`.
