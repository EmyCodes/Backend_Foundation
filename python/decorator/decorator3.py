from time import time

def performance(fn):
	def wrapper(*args, **kwargs):
		t1 = time()
		result = fn(*args, **kwargs)
		t2 = time()
		print(f"Took {t2 - t1}ms")
		return result
	return wrapper

@performance
def long_time():
	for i in range(1000):
		i

long_time()
