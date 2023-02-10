#!/usr/bin/python3
import cmd

class MyConsole(cmd.Cmd):
	pass
	
	def do_EOF(self, line):
		"Interrupting the Program"
		return True
if __name__ == "__main__":
	MyConsole().cmdloop()
