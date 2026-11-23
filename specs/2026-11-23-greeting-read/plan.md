# Plan — 2026-11-23-greeting-read

Add `greeting.read_greeting(path)`: return the file's text without its one trailing newline, UTF-8, or `None` when no
file exists at `path`.

## Files

- `greeting/__init__.py:4` — add `read_greeting` below `write_greeting`.
- `tests/test_read_greeting.py` — new; one test per AC plus a round trip with `write_greeting`, each in a
  `tempfile.TemporaryDirectory`.

## Tasks (ordered by reversibility)

1. **AC1 test, then the function.** Red: write the raw bytes `b'Hello, Ada!\n'` to the file (not through
   `write_greeting`, so the test does not depend on S1) and assert `read_greeting(path) == 'Hello, Ada!'`; it fails
   with `AttributeError` while the function is absent. Green: open with `encoding='utf-8'`, read, and drop one
   trailing `'\n'` with `str.removesuffix`.
2. **AC2 test.** Red: assert `read_greeting(<path in the temp dir with no file>) is None`; it fails with
   `FileNotFoundError` after task 1. Green: catch `FileNotFoundError` and return `None`.
3. **Round-trip test (the unit's fit criterion, seen from this side).** `write_greeting(path, 'Åsa')`, then assert
   `read_greeting(path) == 'Hello, Åsa!'`. Expected green on first run; prove it is a real test by temporarily
   dropping `encoding='utf-8'` from `read_greeting` (the locale here is cp1252, so `Å` decodes as `Ã…`) and watching
   it go red, then revert.

## Verification

`python -m unittest discover -s tests -v` (AGENTS.md): the three new tests, S1's three and the import test pass, on
this Windows machine and on CI's ubuntu runner (`.github/workflows/test.yml`).

## Decisions

- **Place `read_greeting` in `greeting/__init__.py`, beside `write_greeting`.** Rejected: a `greeting/read.py`
  submodule re-exported from `__init__`. Why: the spec names the public path `greeting.read_greeting`, and S1's plan
  already chose one module for the package's two functions.
- **Strip exactly one trailing `'\n'` (`removesuffix('\n')`).** Rejected: `rstrip()` / `rstrip('\n')`, and
  `splitlines()[0]`. Why: the spec says "without its trailing newline", singular; `rstrip` would also eat trailing
  spaces or blank lines that are part of the content, and `splitlines()[0]` would drop everything after a first line.
- **Read in text mode with the default `newline=None` (universal newlines).** Rejected: `newline=''` and binary mode.
  Why: S1 writes `\n`, which reads back unchanged; a file someone saved with `\r\n` still reads as one greeting
  without a stray `\r`, at no cost.
- **Return `None` by catching `FileNotFoundError`.** Rejected: an `os.path.exists` check first (a race between the
  check and the open), and catching `OSError` (it would hide a permission error or a directory at `path`, which the
  spec does not make `None`). Why: the spec's `None` case is "the file does not exist", and that is exactly
  `FileNotFoundError`, which a missing parent directory also raises.
- **Assert on text in the read tests, but write the AC1 fixture as bytes.** Why: the fixture pins the exact file
  content the spec names; the result under test is a `str`.
- **Add a round-trip test with a non-ASCII name** beyond AC1/AC2. Why: the unit's fit criterion is that S2 reads what
  S1 writes; without it, a reader decoding with the locale default would pass both ACs (ASCII only) and break the
  unit on Windows.

## Assumptions

- `path` is a `str` or `os.PathLike`; `open` accepts both.
- The file, when present, is UTF-8; invalid UTF-8 raises `UnicodeDecodeError`, unhandled (not in the spec).
- An empty file returns `''`, a file with no trailing newline returns its content unchanged; neither is in the
  spec, both follow from `removesuffix`.
- Tabs indent Python, as in the existing tests.
- S1's `write_greeting` stays unchanged (unit spec AC1: "with no change to either").

## In-flight overlap

- worktree `.claude/worktrees/2026-11-23-greeting-unit`, branch `feat/2026-11-23-greeting-unit`, shares
  `greeting/__init__.py` — the unit branch this child branches from and merges into; expected.
