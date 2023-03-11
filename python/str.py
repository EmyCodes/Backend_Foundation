#!/usr/bin/python3

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

person = Person("Alice", 25)
print(str(person)) # Alice is 25 years old.\
print(person.__str__)
