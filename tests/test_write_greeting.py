import os
import tempfile
import unittest

import greeting


class WriteGreeting(unittest.TestCase):
	def setUp(self):
		tmp = tempfile.TemporaryDirectory()
		self.addCleanup(tmp.cleanup)
		self.path = os.path.join(tmp.name, 'greeting.txt')

	def written_bytes(self):
		with open(self.path, 'rb') as f:
			return f.read()

	def test_writes_exactly_the_greeting(self):
		greeting.write_greeting(self.path, 'Ada')
		self.assertEqual(self.written_bytes(), b'Hello, Ada!\n')

	def test_replaces_existing_content(self):
		with open(self.path, 'wb') as f:
			f.write(b'An older and much longer greeting\nspread over\nthree lines\n')
		greeting.write_greeting(self.path, 'Ada')
		self.assertEqual(self.written_bytes(), b'Hello, Ada!\n')

	def test_encodes_the_name_as_utf8(self):
		greeting.write_greeting(self.path, 'Åsa')
		self.assertEqual(self.written_bytes(), b'Hello, \xc3\x85sa!\n')


if __name__ == '__main__':
	unittest.main()
