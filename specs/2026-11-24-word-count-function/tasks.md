# Tasks — 2026-11-24-word-count-function

## T1 — Implement plan.md

- Scope: `wordcount.count_words(path)` and its tests, test-first.
- Files: `wordcount/__init__.py`, `tests/test_count_words.py`
- Demo: `python -m unittest tests.test_count_words -v` — five tests pass.

## AC map

| AC | Planned test | Actual test |
|---|---|---|
| AC1 | tests/test_count_words.py::test_counts_words_across_lines_and_runs_of_spaces | tests/test_count_words.py::test_counts_words_across_lines_and_runs_of_spaces |
| AC2 | tests/test_count_words.py::test_empty_file_has_no_words | tests/test_count_words.py::test_empty_file_has_no_words |
| AC3 | tests/test_count_words.py::test_missing_file_raises | tests/test_count_words.py::test_missing_file_raises |
| AC4 | tests/test_count_words.py::test_byte_order_mark_is_not_a_word | tests/test_count_words.py::test_byte_order_mark_is_not_a_word |
