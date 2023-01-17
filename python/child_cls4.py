class Person:
	def __init__(method, fname, lname):
		method.firstName = fname.capitalize()
		method.lastName = lname
	def output(sentence):
		print("Hi {}, child of {}".format(sentence.firstName, sentence.lastName))

class Student(Person):
	def __init__(method2, fname, lname, year):
		super().__init__(fname, lname)
		method2.graduationYear = year

	def welcome(greetings):
		print("Welcome {} {} of Class {}".format(greetings.firstName, greetings.lastName, greetings.graduationYear))

somebody = Student("Olamide", "Ogundare", 2024)
somebody.welcome()
