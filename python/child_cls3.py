class Person:
	def __init__(user, name, age):
		user.name = name
		user.age = age
	def compute(name_age):
		print("{}({})".format(name_age.name, name_age.age))
class Student(Person):
	def __init__(anything, name, age):
		super().__init__(name, age)

x = Student("Timothy", 23)
x.compute()
