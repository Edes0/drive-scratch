# Notes — 2026-11-23-greeting-read

Added `greeting.read_greeting(path)` beside `write_greeting` in `greeting/__init__.py`: it reads the file as UTF-8
(universal newlines), drops exactly one trailing `'\n'`, and returns `None` only on `FileNotFoundError`. Three tests
in `tests/test_read_greeting.py`: AC1 (raw-bytes fixture), AC2 (missing file), and a round trip with
`write_greeting(path, 'Åsa')`, proved red on this cp1252 machine by temporarily dropping `encoding='utf-8'`. Plan
review clean (1 round, plan unchanged), goal met (1 evaluation), code review clean (core, 1 round), all 7 tests and
the check floor pass.

## Decided in an autonomous run

- The SessionStart prompt to register the repo's branch prefix and environment was not asked (autonomous runs never
  ask); the branch prefix stays `feat/` (`ask:enter-worktree-branch-prefix`) and the repo stays unregistered.
- Research lane 2 suggested `newline=''` for the read; the plan's decision (default universal newlines) was kept.

## Hand checks

- none
