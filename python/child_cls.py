class Person:
	def __init__(user, name, age):
		user.name = name
		user.age = age
	def compute(name_age):
		print("{}({})".format(name_age.name, name_age.age))
class Student(Person):
	pass
x = Student("Innocent", 27)
x.compute()
