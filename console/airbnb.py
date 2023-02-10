#!/usr/bin/python3
import cmd

class MyConsole(cmd.Cmd):

	prompt = ">>>> "
	pass
	
	def do_author(self, line):
		"Set yourself as an author"
		print("Hi, {}!\nYou are an Author now".format(line))

	def do_create(self, line):
		"Create a book"
		print("I have created a ", line)

	def precmd(self, line):
		if "." in line:
			line = line.replace(".", " ").replace("(", "").replace(")", "")
		print(line)
		return cmd.Cmd.precmd(self, line)

	def do_EOF(self, line):
		"Interrupting the Program"
		return True
if __name__ == "__main__":
	MyConsole().cmdloop()
