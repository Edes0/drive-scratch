---
id: 2026-11-24-word-count-function
title: Count the words in a text file
short: word count function
unit: 2026-11-23-word-count
status: grilled
domain_gate: done
created: 2026-11-24
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
