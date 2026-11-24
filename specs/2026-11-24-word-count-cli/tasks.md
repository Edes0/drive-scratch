# Tasks — 2026-11-24-word-count-cli

1. **Implement plan.md**
   - **Scope:** `wordcount/__main__.py` and its subprocess tests, in the plan's order (AC1 red → green, AC2 proved
     by a temporary `nargs='?'`, AC3 red → green, AC4 red → green), then the unit fit test proved red by a
     temporary `count + 1`.
   - **Files:** `wordcount/__main__.py`, `tests/test_cli.py`
   - **Demo:** `python -m unittest tests.test_cli -v` shows all CLI tests passing; `python -m wordcount README.md`
     prints a number.

## AC map

| AC | Planned test | Actual test |
|---|---|---|
| AC1 | tests/test_cli.py::test_prints_the_count_and_exits_0 | tests/test_cli.py::test_prints_the_count_and_exits_0 |
| AC2 | tests/test_cli.py::test_no_path_prints_usage_and_exits_2 | tests/test_cli.py::test_no_path_prints_usage_and_exits_2 |
| AC3 | tests/test_cli.py::test_missing_file_names_the_path_and_exits_1 | tests/test_cli.py::test_missing_file_names_the_path_and_exits_1 |
| AC4 | tests/test_cli.py::test_directory_cannot_be_read; tests/test_cli.py::test_non_utf8_file_cannot_be_read | tests/test_cli.py::test_directory_cannot_be_read; tests/test_cli.py::test_non_utf8_file_cannot_be_read |
