import unittest
import math

class MyTest(unittest.TestCase):
	
	@unittest.skip("Not done yet")
	def test_add_fraction(self):
		pass

	def test_fraction_construction(self):
		"""sqrt of a negative number should throw ValueError."""
		with self.assertRaises(ValueError):
			math.sqrt(-1)

