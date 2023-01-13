class Person:
	def __init__(sillyObject, fname, lname):
		sillyObject.fname = fname
		sillyObject.lname = lname
	def myfunc(together):
		print("Hello {} {}".format(together.lname, together.fname))

p1 = Person("Israel", "Ogundare")
p1.myfunc()
