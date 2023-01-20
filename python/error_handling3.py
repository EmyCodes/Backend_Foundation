class Error(Exception):
	pass
class EmptyFileError(Error):
	pass

try:
	# my_file = str(input("Enter file name: "))
	thefile = open('enumerate.py')
	line_count = len(thefile.readlines())
	if line_count < 2:
		raise EmptyFileError
except FileNotFoundError:
	print("\n\nThere is no such file here")
except EmptyFileError:
	print("File doesn't have enough stuff")
except Exception as e:
	print("\n\nFailed: The error was {}".format(str(e)))
	thefile.close()
else:
	print()
	for one_line in thefile:
		print(one_line)
		thefile.close()
		print("Success!")
"""
finally:
	print("Terminating...")
	print("Shutdown!!!")
"""
