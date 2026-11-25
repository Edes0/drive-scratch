"""Count the words in a text file."""


def count_words(path):
	"""Return the number of whitespace-separated words in the file at `path`, UTF-8 with an optional BOM."""
	with open(path, encoding='utf-8-sig') as f:
		return len(f.read().split())
