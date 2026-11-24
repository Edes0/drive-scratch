---
id: 2026-11-23-word-count
title: Count the words in a text file
short: word count
kind: unit
status: grilled
domain_gate: done
created: 2026-11-23
---

The fresh fixture for the Drive hand check (claude-home spec `2026-11-22-card-orchestrator`, AC9): one Drive press
takes this card from Draft to `landed`. The greeting unit cannot count: its two children were built and merged
outside Drive.

Idea, meant to grill into a unit of two small children:

- a function that counts the words in a text file;
- a command line entry that prints that count for a path given as an argument.

## Specs

- S1 — 2026-11-24-word-count-function — Count the words in a text file
- S2 — 2026-11-24-word-count-cli — Print the word count of a file named on the command line

## Decisions

- **D1.** A new package `wordcount/` beside `greeting/`, standard library only (`AGENTS.md`): S1 is
  `wordcount/__init__.py`, S2 is `wordcount/__main__.py`, run as `python -m wordcount`. No console-script entry
  point: the repo has no packaging.
- **D2.** A word is a run of non-whitespace characters, `str.split()` with no argument; the file is read with
  encoding `utf-8-sig`, so a leading byte-order mark is not part of the first word.
- **D3.** S2 builds on S1: it calls `count_words` and owns only argument parsing, output and exit codes.

## Success criteria

- **AC1** — Given a multi-line UTF-8 file, `python -m wordcount <path>` (S2) prints the number
  `count_words(path)` (S1) returns for that file, with no change to either spec's code.
