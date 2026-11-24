# Plan — 2026-11-24-word-count-cli

Add `wordcount/__main__.py` so `python -m wordcount <path>` prints `count_words(path)` (S1, `wordcount/__init__.py:4`)
and owns only argument parsing, output and exit codes (unit D3).

## Files

- `wordcount/__main__.py` — new: a `main()` returning the exit code, and `sys.exit(main())` under `if __name__ == '__main__':`.
- `tests/test_cli.py` — new; one test per AC plus the unit's fit criterion, each running
  `[sys.executable, '-m', 'wordcount', ...]` with `cwd` = the repo root (`tests/..`), `capture_output=True`,
  `text=True`, fixtures in a `tempfile.TemporaryDirectory`.

## Tasks (ordered by reversibility)

1. **AC1 test, then the entry.** Red: write `b'one two three\n'`, run the module, assert stdout `'3\n'`, stderr `''`,
   return code 0; it fails while `__main__.py` is absent (`No module named wordcount.__main__`, exit 1). Green:
   `argparse.ArgumentParser(prog='wordcount')` with one positional `path`; `print(count_words(args.path))`;
   return 0.
2. **AC2 test.** Run with no argument; assert return code 2, stdout `''`, and stderr starts with `usage: wordcount`.
   Expected green on first run (argparse's own behaviour); prove it real by temporarily giving `path` `nargs='?'`
   and watching it go red, then revert.
3. **AC3 test.** Path in the temp dir with no file; assert stderr `'wordcount: no such file: <path>\n'` (the path as
   given), stdout `''`, return code 1. Red: a traceback and exit 1 with the wrong stderr. Green: catch
   `FileNotFoundError`, write the line to `sys.stderr`, return 1.
4. **AC4 tests (two).** (a) the temp directory itself as the path; (b) a file holding `b'\xff\xfe\xfa'`. Assert one
   stderr line starting `wordcount: cannot read: <path>`, no `Traceback` in stderr, stdout `''`, return code 1.
   Red: tracebacks. Green: after the `FileNotFoundError` clause, catch `(OSError, UnicodeDecodeError)` and print
   `wordcount: cannot read: <path>: <str(exc)>` on one line.
5. **Unit fit test.** A multi-line UTF-8 file with a non-ASCII word and a leading BOM; assert stdout equals
   `f'{wordcount.count_words(path)}\n'`. Expected green; prove it real by temporarily printing `count + 1`, then
   revert.

## Verification

`python -m unittest discover -s tests -v` (AGENTS.md): the five new CLI tests plus every existing test pass, on this
Windows machine and on CI's ubuntu runner (`.github/workflows/test.yml`).

## Decisions

- **`argparse` with `prog='wordcount'`.** Rejected: reading `sys.argv` by hand. Why: argparse already prints a usage
  line to stderr and exits 2 on a missing argument (AC2) and on extra arguments, with no code of ours; `prog` keeps
  the usage line from naming `__main__.py`.
- **`main()` returns the exit code; `sys.exit(main())` runs under a `__name__` guard.** Rejected: logic at module level,
  and an `argv` parameter (dropped at simplify: every test runs the module as a subprocess, so nothing passed it).
- **Catch `FileNotFoundError` first, then `OSError` and `UnicodeDecodeError`.** Rejected: one `except Exception`.
  Why: AC3 and AC4 need different messages, and `FileNotFoundError` is an `OSError`; a directory raises
  `IsADirectoryError` on Linux but `PermissionError` on Windows, both `OSError`; bad bytes raise
  `UnicodeDecodeError`. A bug elsewhere still shows its traceback.
- **AC4 message carries the reason after the path.** Why: the spec fixes only the line's start; the reason tells a
  user whether it was a directory or an encoding. Tests assert the prefix only.
- **Tests read stdout with `text=True`.** Rejected: asserting raw bytes. Why: Python's text stdout writes `\r\n` on
  Windows; universal-newline decoding makes `'3\n'` hold on both this machine and CI, and the spec's `\n` means "one
  line", not a byte on Windows.
- **Error lines go through `print(..., file=sys.stderr)`.** One line each; nothing goes to stdout on failure because
  the count is printed only after `count_words` returns.

## Assumptions

- S1's `count_words` raises `FileNotFoundError` for a missing file (tested in `tests/test_count_words.py`) and lets
  `OSError` / `UnicodeDecodeError` propagate.
- Tests run from any cwd; `cwd` is set explicitly so `-m wordcount` resolves the package.
- No packaging or console-script entry point (unit D1).

## In-flight overlap

- worktree `.claude/worktrees/2026-11-23-word-count`, branch `feat/2026-11-23-word-count` (the unit branch this
  child bases on): `tests/test_count_words.py`, `wordcount/__init__.py` — read only here, S1 already merged there.
