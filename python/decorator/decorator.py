def my_decorator(func):
	def wrap_func():
		print("*********")
		func()
		print("*********")
	return wrap_func

@my_decorator
def hello():
	print("Helllllooooo")


@my_decorator
def alias():
	print("Emy")

hello()
alias()
