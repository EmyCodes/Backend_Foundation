import unittest

def add(x, y):
	return x+y

class TestAdd(unittest.TestCase):
	def test_add_1(self):
		self.assertEqual(9, add(5, 4))
		#OR
		self.assertEqual(add(4, 5), 9)


if __name__ == "__main__":
	unittest.main()
