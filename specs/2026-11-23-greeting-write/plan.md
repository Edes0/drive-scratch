# Plan — 2026-11-23-greeting-write

Add `greeting.write_greeting(path, name)`: write `Hello, <name>!\n` to `path`, UTF-8, replacing any content.

## Files

- `greeting/__init__.py:1` — add `write_greeting` below the module docstring.
- `tests/test_write_greeting.py` — new; one test per AC, in a `tempfile.TemporaryDirectory`.

## Tasks (ordered by reversibility)

1. **AC1 test, then the function.** Red: call `write_greeting(path, "Ada")` and assert the file's **bytes** equal
   `b'Hello, Ada!\n'`, so a platform newline translation (`\r\n` on Windows) fails the test. Green: open with
   `encoding='utf-8', newline='\n'` and mode `'w'`.
2. **AC2 test.** Pre-fill the file with longer text (several lines), call `write_greeting`, assert the bytes are only
   the new greeting. Mode `'w'` truncates, so this is expected green on first run; prove it is a real test by
   temporarily switching to mode `'a'` and watching it go red, then revert.

## Verification

`python -m unittest discover -s tests -v` (AGENTS.md); both new tests and the existing import test pass.

## Decisions

- **Place `write_greeting` in `greeting/__init__.py`.** Rejected: a `greeting/write.py` submodule re-exported from
  `__init__`. Why: the spec names the public path `greeting.write_greeting`, the package is one function wide, and
  S2's `read_greeting` can sit beside it; a submodule adds a file and a re-export for nothing.
- **Write with `newline='\n'`.** Rejected: the default text mode (translates `\n` to `os.linesep`, so `\r\n` on this
  Windows machine) and binary mode with a manual `.encode('utf-8')`. Why: AC1 demands exactly `Hello, Ada!\n`;
  `newline='\n'` keeps the text-mode API and fixes the newline on every platform.
- **Assert on bytes, not text.** Rejected: `read_text()`, which un-translates `\r\n` on read and would hide the bug
  the previous decision prevents.
- **No validation of `name`** (empty, contains a newline). Rejected: raising on such names. Why: the spec states no
  rule for them; inventing one would widen the contract S2 reads against.

## Assumptions

- `path` is a `str` or `os.PathLike`; `open` accepts both.
- The parent directory exists; a missing one raises `FileNotFoundError`, unhandled (not in the spec).
- Return value is `None`.
- Tabs indent Python, as in `tests/test_package.py`.

## In-flight overlap

none
