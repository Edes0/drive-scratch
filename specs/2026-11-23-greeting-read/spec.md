---
id: 2026-11-23-greeting-read
title: Read a greeting back from a file
short: greeting read
unit: 2026-11-23-greeting-unit
status: verified
domain_gate: done
plan_reviewed:
  sha256: 365d3b08d5beeda1e77d89244f4c042d8f792b6eba7a3704f753e5d2e6ef4763
  status: clean
  rounds: 1
  at: 2026-11-23T18:25:11Z
hardened:
  at: 2026-11-23T18:36:26Z
  by: implement-9.7
  status: clean
  depth: core
  base_sha: a8cb0861a34432f20dddc7421fdc9005d1ca09b5
  diff_sha256: 30f938c8156ba70a99979370bb4f478e3217b2c5a7b6db7b87708d114d0b74ff
  files: 2
  lines: 37
created: 2026-11-23
worktreePath: C:/Projects/Private/drive-scratch/.claude/worktrees/2026-11-23-greeting-read
branch: feat/2026-11-23-greeting-read
branchCreated: true
---

`greeting.read_greeting(path)` returns the greeting in the file at `path` without its trailing newline, and `None`
when the file does not exist.

## Out of scope

- Writing the file (S1).

## Success criteria

- **AC1** — Given a file holding `Hello, Ada!\n`, When `read_greeting(path)` runs, Then it returns `Hello, Ada!`.
- **AC2** — Given a path with no file, When `read_greeting(path)` runs, Then it returns `None`.
