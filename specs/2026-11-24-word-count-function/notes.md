# Notes — 2026-11-24-word-count-function

Added `wordcount.count_words(path)` in a new `wordcount/` package: it reads the file with `utf-8-sig` and returns
`len(text.split())`, letting `OSError` / `UnicodeDecodeError` propagate. Five tests cover AC1–AC4 plus a BOM-only
guard (D2): AC4 alone passes under plain `utf-8` too (U+FEFF is not whitespace), which the TDD run confirmed — only
the guard went red against a plain `utf-8` read. Plan review clean (2 rounds), code review clean (core, 1 round),
suite and check floor pass.
