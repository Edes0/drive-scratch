import os
import tempfile
import unittest

import wordcount


class CountWords(unittest.TestCase):
	def setUp(self):
		tmp = tempfile.TemporaryDirectory()
		self.addCleanup(tmp.cleanup)
		self.path = os.path.join(tmp.name, 'words.txt')

	def write(self, data):
		with open(self.path, 'wb') as f:
			f.write(data)

	def test_counts_words_across_lines_and_runs_of_spaces(self):
		self.write(b'one two  three\nfour\n')
		self.assertEqual(wordcount.count_words(self.path), 4)

	def test_empty_file_has_no_words(self):
		self.write(b'')
		self.assertEqual(wordcount.count_words(self.path), 0)

	def test_missing_file_raises(self):
		with self.assertRaises(FileNotFoundError):
			wordcount.count_words(self.path)

	def test_byte_order_mark_is_not_a_word(self):
		self.write(b'\xef\xbb\xbfhello world')
		self.assertEqual(wordcount.count_words(self.path), 2)

	def test_file_of_only_a_byte_order_mark_has_no_words(self):
		self.write(b'\xef\xbb\xbf')
		self.assertEqual(wordcount.count_words(self.path), 0)


if __name__ == '__main__':
	unittest.main()
