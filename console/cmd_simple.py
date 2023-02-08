#!/usr/bin/python3

import cmd

class HelloWorld(cmd.Cmd):
	"""Simple command processor example."""

	def do_greet(self, person):
		print("Hi", person)

	def do_EOF(self, line):
		return True

if __name__ == "__main__":
	HelloWorld().cmdloop()
