import unittest
import math

class MathTest(unittest.TestCase):
	"""class that test the built-in math methods"""
	def test_sqrt(self):
		self.assertEqual(5, math.sqrt(25))
		self.assertEqual(0, math.sqrt(0))

	
	def test_pow(self):
		#TODO Write some tests of math.pow(x, n)
		self.assertEqual(36, math.pow(6, 2))
		self.assertEqual(8, math.pow(2, 3))

if __name__ == "__main__":
	unittest.main()

