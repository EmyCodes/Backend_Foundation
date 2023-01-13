class Person:
	def __init__(mySillyObject, name, age):
		mySillyObject.name = name
		mySillyObject.age = age
	def myfunc(abc):
		print("{}({})".format(abc.name, abc.age))
p1 = Person("EmyCodes", 25)
p1.myfunc()
p1.name = "Timnasco"
p1.age = 23
p1.myfunc()
