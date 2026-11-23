---
id: 2026-11-23-greeting-write
title: Write a greeting to a file
short: greeting write
unit: 2026-11-23-greeting-unit
status: verified
domain_gate: done
plan_reviewed:
  sha256: 4cebad54be52883a5afc430e062b57a3afcbc0e2e18c1914185e409622579c90
  status: clean
  rounds: 1
  at: 2026-11-23T17:38:44Z
hardened:
  at: 2026-11-23T17:52:53Z
  by: implement-9.7
  status: clean
  depth: standard
  base_sha: 37aaafce0db8c87f778d9748b5d23e94b2692c2b
  diff_sha256: 68bcfbdacf08064836ae7d99654c04a799ef92b82142376e0575288af782d705
  files: 4
  lines: 83
created: 2026-11-23
worktreePath: C:/Projects/Private/drive-scratch/.claude/worktrees/2026-11-23-greeting-write
branch: feat/2026-11-23-greeting-write
branchCreated: true
---

`greeting.write_greeting(path, name)` writes one line, `Hello, <name>!`, to the file at `path`, replacing what was
there, UTF-8, ending in a newline.

## Out of scope

- Reading the file back (S2).

## Success criteria

- **AC1** — Given a temp path, When `write_greeting(path, "Ada")` runs, Then the file holds exactly `Hello, Ada!\n`.
- **AC2** — Given a file that already holds text, When `write_greeting` writes to it, Then only the new greeting is
  left.
