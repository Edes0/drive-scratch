---
id: 2026-11-23-greeting-read
title: Read a greeting back from a file
short: greeting read
unit: 2026-11-23-greeting-unit
status: grilled
domain_gate: done
created: 2026-11-23
---

`greeting.read_greeting(path)` returns the greeting in the file at `path` without its trailing newline, and `None`
when the file does not exist.

## Out of scope

- Writing the file (S1).

## Success criteria

- **AC1** — Given a file holding `Hello, Ada!\n`, When `read_greeting(path)` runs, Then it returns `Hello, Ada!`.
- **AC2** — Given a path with no file, When `read_greeting(path)` runs, Then it returns `None`.
