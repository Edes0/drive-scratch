"""Print the word count of the file named on the command line: `python -m wordcount <path>`."""

import argparse
import sys

from wordcount import count_words


def main():
	parser = argparse.ArgumentParser(prog='wordcount')
	parser.add_argument('path')
	args = parser.parse_args()
	try:
		count = count_words(args.path)
	except FileNotFoundError:
		print(f'wordcount: no such file: {args.path}', file=sys.stderr)
		return 1
	except (OSError, UnicodeDecodeError) as exc:
		print(f'wordcount: cannot read: {args.path}: {exc}', file=sys.stderr)
		return 1
	print(count)
	return 0


if __name__ == '__main__':
	sys.exit(main())
