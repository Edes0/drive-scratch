---
id: 2026-11-23-greeting-read
title: Read a greeting back from a file
short: greeting read
unit: 2026-11-23-greeting-unit
status: planned
domain_gate: done
plan_reviewed:
  sha256: 365d3b08d5beeda1e77d89244f4c042d8f792b6eba7a3704f753e5d2e6ef4763
  status: clean
  rounds: 1
  at: 2026-11-23T18:25:11Z
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
