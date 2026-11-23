# Tasks — 2026-11-23-greeting-write

1. **Implement plan.md**
   - **Scope:** `greeting.write_greeting(path, name)` and its tests, in the plan's order (AC1 red → green, then
     AC2 with its mode-`'a'` red proof), plus a UTF-8 test (name `Åsa` → bytes `b'Hello, \xc3\x85sa!\n'`) proved
     red by temporarily dropping `encoding='utf-8'`.
   - **Files:** `greeting/__init__.py`, `tests/test_write_greeting.py`
   - **Demo:** `python -m unittest tests.test_write_greeting -v` shows all three tests passing.

## AC map

| AC | Planned test | Actual test |
|---|---|---|
| AC1 | tests/test_write_greeting.py::test_writes_exactly_the_greeting | tests/test_write_greeting.py::test_writes_exactly_the_greeting |
| AC2 | tests/test_write_greeting.py::test_replaces_existing_content | tests/test_write_greeting.py::test_replaces_existing_content |
