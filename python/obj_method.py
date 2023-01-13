class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def myfunc(self):
		print("{}({})".format(self.name, self.age))
p1 = Person("Israel", 17)
p1.myfunc()
