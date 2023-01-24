# doctest_private_tests.py

import doctest_private_tests_external

__test__ = {
	"numbers": """
>>> my_function(2, 3)
6

>>> my_function(2.0, 3)
6.0
""",
	'string': """
>>> my_function('a', 3)
'aaa'
""",
	"external": doctest_private_tests_external,
}

def my_function(a, b):
	"""Returns a * b
	"""
	return a * b