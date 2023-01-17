class Person:
	def __init__(user, name, age):
		user.name = name
		user.age = age
	def compute(name_age):
		print("{}({})".format(name_age.name, name_age.age))
class Student(Person):
	def __init__(user, name, age):
		Person.__init__(user, name, age)
x = Student("Zipporah", 21)
x.compute()
