class Person:
	def __init__(user, name, age):
		user.YourName = name
		user.YourAge = age
	def compute(name_age):
		print("{}({})".format(name_age.YourName, name_age.YourAge))
class Student(Person):
	def __init__(anything, name, age):
		super().__init__(name, age)

x = Student("Timothy", 23)
x.compute()
