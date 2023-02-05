import unittest

class TestBuiltins(unittest.TestCase):
	"""Test some python built-in methods"""
	def test_len(self):
		self.assertEqual(5, len("hello"))
		self.assertEqual(3, len(["a", "b", "c"]))
		# edge case
		self.assertEqual(0, len(""))

	def test_str_upper(self):
		self.assertTrue("ABC".isupper())
		self.assertFalse("ABc".isupper())
		s = ""	# edge case
		self.assertFalse(s.isupper())
