import unittest

import greeting


class PackageImports(unittest.TestCase):
	def test_the_package_imports(self):
		self.assertIsNotNone(greeting.__doc__)


if __name__ == '__main__':
	unittest.main()
