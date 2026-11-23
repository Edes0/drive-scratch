# Notes — 2026-11-23-greeting-write

Added `greeting.write_greeting(path, name)` in `greeting/__init__.py`: opens with mode `'w'`, `encoding='utf-8'`,
`newline='\n'` and writes `Hello, <name>!\n`. Three tests in `tests/test_write_greeting.py` assert the file's bytes:
AC1 (exact greeting), AC2 (longer multi-line content replaced) and a UTF-8 test (`Åsa` → `b'Hello, \xc3\x85sa!\n'`)
added at Phase 5 to cover the spec's UTF-8 clause. Each test was proven by mutation on this Windows machine: mode
`'a'` fails AC2, dropping the encoding fails the UTF-8 test (locale cp1252), dropping the newline pin fails all three.
Plan review clean (1 round), goal met (1 evaluation), code review clean (1 round, standard depth), verify-suite pass.
