# Plan — 2026-11-24-word-count-function

S1 of unit `2026-11-23-word-count`: `wordcount.count_words(path)`.

## Files

- `wordcount/__init__.py` (new) — module docstring + `count_words(path)`, mirroring `greeting/__init__.py:1-15`
  (tab indent, single quotes, one-line docstrings).
- `tests/test_count_words.py` (new) — one `unittest.TestCase`, temp dir per test as in
  `tests/test_read_greeting.py:9-12`; one test per AC1–AC4, files written as bytes so the content is exact.

## Work, by reversibility

1. **Tests first (red):** `tests/test_count_words.py` with AC1–AC4 plus a BOM-only guard (D2). Red first on the
   import error, then each test red against a stub `count_words` that returns `-1` (so AC2's `0` and AC3's raise
   cannot pass by accident), and the BOM-only guard red against a plain `utf-8` read (it returns 1, not 0).
2. **Implement (green):** `count_words` opens `path` with `encoding='utf-8-sig'`, returns `len(f.read().split())`.
   No `try` — errors propagate (spec).

Nothing here is hard to reverse: a new module and a new test file, no public route or schema.

## Decisions

- **D1 (unit D1).** Code lives in `wordcount/__init__.py`, a package beside `greeting/`. Rejected: a top-level
  `wordcount.py` module — S2 needs `wordcount/__main__.py` for `python -m wordcount`, which requires a package.
- **D2 (unit D2).** Word = `str.split()` with no argument; file read with `utf-8-sig`. Rejected: a regex `\w+`
  (splits `don't` into two, contradicts "run of non-whitespace"); plain `utf-8` (a BOM is glued to the first
  word). AC4 alone does not pin this: U+FEFF is not whitespace, so BOM + `hello world` counts 2 under both
  encodings (probed). The pin is an extra test: a file holding only a BOM counts 0 with `utf-8-sig`, 1 with
  `utf-8`.
- **D3.** No error handling in `count_words`: `FileNotFoundError`, `IsADirectoryError`/`PermissionError` and
  `UnicodeDecodeError` propagate. Rejected: catching and returning `None` like `read_greeting` — the spec says
  errors are not caught; S2 owns the messages and exit codes (unit D3).
- **D4.** Read the whole file with `f.read()`. Rejected: line-by-line streaming — the spec targets small text
  files and a whole read keeps the one-expression definition `len(text.split())` literal.

## Assumptions

- Python 3.9+ (the repo already uses `str.removesuffix`).
- Test discovery picks up `tests/test_count_words.py` with the existing command; no `tests/__init__.py` needed
  (the existing tests run without one).
- `open()` with no `newline=` argument is fine: universal newlines only turn `\r\n` into `\n`, both whitespace.

## In-flight overlap

none

## Verification

- `python -m unittest discover -s tests -v` — all existing tests plus the five new ones pass.
- AC map: AC1 `test_counts_words_across_lines_and_runs_of_spaces`, AC2 `test_empty_file_has_no_words`,
  AC3 `test_missing_file_raises`, AC4 `test_byte_order_mark_is_not_a_word`; D2 guard
  `test_file_of_only_a_byte_order_mark_has_no_words`.
