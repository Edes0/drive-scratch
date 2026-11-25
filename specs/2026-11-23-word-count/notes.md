# 2026-11-23-word-count — fit check notes

Unit fit check, 2026-11-25. Both children (S1 #5, S2 #6) were merged into the unit branch; the catch-up with
`main` found nothing new. AC1: on a 4-line UTF-8 file with a BOM and non-ASCII text, `python -m wordcount <path>`
printed `9` and `count_words(path)` returned `9`; neither child's code changed (only the two child merges touch
`wordcount/` and its tests). The fit review (one critic, the fit lens, depth full: 398 lines / 12 files) was clean
in one round. Suite: compile, 18 tests and the check floor passed. No code edits were made on the unit branch.
