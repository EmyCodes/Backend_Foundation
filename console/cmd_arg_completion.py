#!/usr/bin/python3

import cmd

class HelloWorld(cmd.Cmd):
	"""Simple command processor example."""
	
	FRIENDS = ["Alice", "Adam", "Barbara", "Bob"]

	def do_greet(self, person):
		"Greet the Person"
		if person and person in FRIENDS:
			greeting = f"Hi, {person}"
		elif person:
			greeting = f"Hello, {person}"
		else:
			greeting = "Hello"
		print(greeting)

	def complete_greeting(self, text,line, begidx, endidx):
		if not text:
			completions = self.FRIENDS[:]
		else:
			completions = [ f
			for f in self.FRIENDS
			if f.startawith(text)
			]
		return completions
	

	def do_EOF(self, line):
		return True

if __name__ == "__main__":
	HelloWorld().cmdloop()
