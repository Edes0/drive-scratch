import os
import subprocess
import sys
import tempfile
import unittest

import wordcount

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class WordCountCli(unittest.TestCase):
	def setUp(self):
		tmp = tempfile.TemporaryDirectory()
		self.addCleanup(tmp.cleanup)
		self.dir = tmp.name
		self.path = os.path.join(tmp.name, 'words.txt')

	def write(self, data):
		with open(self.path, 'wb') as f:
			f.write(data)

	def run_cli(self, *args):
		return subprocess.run(
			[sys.executable, '-m', 'wordcount', *args],
			cwd=REPO_ROOT, capture_output=True, text=True)

	def test_prints_the_count_and_exits_0(self):
		self.write(b'one two three\n')
		result = self.run_cli(self.path)
		self.assertEqual((result.stdout, result.stderr, result.returncode), ('3\n', '', 0))

	def test_no_path_prints_usage_and_exits_2(self):
		result = self.run_cli()
		self.assertEqual((result.stdout, result.returncode), ('', 2))
		self.assertTrue(result.stderr.startswith('usage: wordcount'), result.stderr)

	def test_missing_file_names_the_path_and_exits_1(self):
		result = self.run_cli(self.path)
		self.assertEqual(
			(result.stdout, result.stderr, result.returncode),
			('', f'wordcount: no such file: {self.path}\n', 1))

	def assert_cannot_read(self, path):
		result = self.run_cli(path)
		self.assertEqual((result.stdout, result.returncode), ('', 1))
		self.assertTrue(result.stderr.startswith(f'wordcount: cannot read: {path}'), result.stderr)
		self.assertNotIn('Traceback', result.stderr)
		self.assertEqual(result.stderr.count('\n'), 1, result.stderr)

	def test_directory_cannot_be_read(self):
		self.assert_cannot_read(self.dir)

	def test_non_utf8_file_cannot_be_read(self):
		self.write(b'\xff\xfe\xfa')
		self.assert_cannot_read(self.path)

	def test_prints_what_count_words_returns_for_a_multi_line_file(self):
		self.write('\ufeffhéllo wörld\nsecond  line\there\n'.encode('utf-8'))
		result = self.run_cli(self.path)
		self.assertEqual(result.stdout, f'{wordcount.count_words(self.path)}\n')
		self.assertEqual(result.stdout, '5\n')


if __name__ == '__main__':
	unittest.main()
