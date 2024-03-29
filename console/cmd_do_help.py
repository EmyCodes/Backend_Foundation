#!/usr/bin/python3

import cmd

class HelloWorld(cmd.Cmd):
	"""Simple command processor example."""

	def do_greet(self, person):
		if person:
			print("Hi", person)
		else:
			print("Hi")
	def help_greet(self):
		print ("\n".join(["greet [person]",
		"Greet the named person",
		]))
	def do_EOF(self, line):
		return True

if __name__ == "__main__":
	HelloWorld().cmdloop()
