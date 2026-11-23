import os
import tempfile
import unittest

import greeting


class ReadGreeting(unittest.TestCase):
	def setUp(self):
		tmp = tempfile.TemporaryDirectory()
		self.addCleanup(tmp.cleanup)
		self.path = os.path.join(tmp.name, 'greeting.txt')

	def test_returns_the_greeting_without_its_newline(self):
		with open(self.path, 'wb') as f:
			f.write(b'Hello, Ada!\n')
		self.assertEqual(greeting.read_greeting(self.path), 'Hello, Ada!')

	def test_returns_none_when_no_file(self):
		self.assertIsNone(greeting.read_greeting(self.path))

	def test_reads_back_what_write_greeting_wrote(self):
		greeting.write_greeting(self.path, 'Åsa')
		self.assertEqual(greeting.read_greeting(self.path), 'Hello, Åsa!')


if __name__ == '__main__':
	unittest.main()
