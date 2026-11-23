# Tasks — 2026-11-23-greeting-read

1. **Implement plan.md**
   - **Scope:** `greeting.read_greeting(path)` and its tests, in the plan's order (AC1 red → green, AC2 red → green),
     then the round-trip test with `write_greeting(path, 'Åsa')`, proved red by temporarily dropping
     `encoding='utf-8'` from `read_greeting` (red on this cp1252 machine only; CI's UTF-8 locale would stay green).
   - **Files:** `greeting/__init__.py`, `tests/test_read_greeting.py`
   - **Demo:** `python -m unittest tests.test_read_greeting -v` shows all three tests passing.

## AC map

| AC | Planned test | Actual test |
|---|---|---|
| AC1 | tests/test_read_greeting.py::test_returns_the_greeting_without_its_newline | |
| AC2 | tests/test_read_greeting.py::test_returns_none_when_no_file | |
