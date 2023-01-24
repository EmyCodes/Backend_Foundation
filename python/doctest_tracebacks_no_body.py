# doctest_tracebacks_no_body.py

def this_raise():
	"""This function always raises an exception.

	>>> this_raise()
	Traceback (most recent call last):
	RuntimeError: here is the error

	>>> this_raise()
	Traceback (innermost last):
	RuntimeError: here is the error
	"""
	raise RuntimeError('here is the error')

