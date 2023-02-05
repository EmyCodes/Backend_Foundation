import unittest

from listutil import average
class TestAverage(unittest.TestCase):
	def test_average_singleton_list(self):
		self.assertEqual(5, average([5]))


	def test_list_with_many_value(self):
		self.assertEqual(list(1, 2, 3, 5), list(2, 1, 5, 3))
	
if __name__ == "__main__":
	unittest.main()

