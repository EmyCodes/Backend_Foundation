import unittest

from primes import is_prime

class TestPrimes(unittest.TestCase):

	def test_is_three_prime(self):
		self.assertEqual(True, is_prime(3))


	def test_is_four_prime(self):
		self.assertEqual(False,is_prime(4))

if __name__ == "__main__":
	unittest.main()

