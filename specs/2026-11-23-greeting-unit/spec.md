---
id: 2026-11-23-greeting-unit
title: A greeting saved to a file and read back
short: greeting unit
kind: unit
status: grilled
domain_gate: done
created: 2026-11-23
---

The Drive hand check's fixture (claude-home spec `2026-11-22-card-orchestrator`, AC9): a unit of two small child
specs, one writing a greeting file and one reading it back.

## Specs

- S1 — 2026-11-23-greeting-write — Write a greeting to a file
- S2 — 2026-11-23-greeting-read — Read a greeting back from a file

## Success criteria

- **AC1** — `read_greeting(path)` returns the greeting `write_greeting(path, name)` wrote to that path: S2 reads the
  file S1 writes, with no change to either.
