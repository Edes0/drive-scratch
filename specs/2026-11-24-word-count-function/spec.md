---
id: 2026-11-24-word-count-function
title: Count the words in a text file
short: word count function
unit: 2026-11-23-word-count
status: draft
created: 2026-11-24
---

`wordcount.count_words(path)` returns the number of words in the UTF-8 text file at `path`. A word is a run of
non-whitespace characters: the count is `len(text.split())`.

## Out of scope

- The command line entry (S2).
- Encodings other than UTF-8, and directories as `path`.

## Success criteria

- **AC1** — Given a file holding `one two  three\nfour\n`, When `count_words(path)` runs, Then it returns `4`.
- **AC2** — Given an empty file, When `count_words(path)` runs, Then it returns `0`.
- **AC3** — Given a path with no file, When `count_words(path)` runs, Then it raises `FileNotFoundError`.
