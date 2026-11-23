"""Greetings written to and read from a file; the unit's child specs fill this in."""


def write_greeting(path, name):
	"""Replace the file at `path` with `Hello, <name>!` and a newline, UTF-8."""
	with open(path, 'w', encoding='utf-8', newline='\n') as f:
		f.write(f'Hello, {name}!\n')
