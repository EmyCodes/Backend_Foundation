# file_name = input("Enter file name correctly: ")
try:
	# Open file that's in this same folder
	thefile = open('people.txt')
	print("\n\n", thefile.readline())
	# thefile.closed()
	thefile.wigwam()

except FileNotFoundError:
	print("Sorry, I don't see a file named people.txt here")
except Exception as e:
	print(e)

