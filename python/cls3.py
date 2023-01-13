class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __str__(self):
		return f"Your name is {self.name}. You are of age {self.age}\n{self.name}({self.age})"
p1 = Person("John", 10)
print(p1.name)
print(p1.age)
print(p1)
