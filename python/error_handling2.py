try:
	thefile = open('people.txt')
except FileNotFoundError:
	print("Sorry, I don't see a file named people.txt")
except Exception as err:
	print(err)
else:
	print("\n")
	for one_line in thefile:
		print(one_line)
	thefile.close()
	print("Success!")
finally:
	print("Terminating...")
print("Successfully Shutdown!")

