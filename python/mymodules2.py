from datetime import *
today = datetime.now()
fname = input("FIrst name: ")
lname = input("Surname: ")
midname = input("Middle name (optional): ")
def username(**user):	# creating function username
	"""DOcstring here"""
	print("\tSuccessful Login: {}".format(today))
	if len(midname) > 0:
		password = fname[0:2:3].lower() + midname[-1].capitalize() + fname[0:2:3].lower() + fname[2].capitalize() + lname[-2].lower() + fname[1].capitalize() + lname[0].lower() + midname[:-3].lower()
		print("\nWelcome, {} {} {}!".format(fname.capitalize(), lname.upper(), midname.capitalize()))
		print("\nYour assigned Password is \"{}\"\n".format(password))
	else:
		password = fname[0:2:3].lower() + fname[2].capitalize() + lname[-2].lower() + fname[1].capitalize() + lname[0].lower() + lname[0:2].capitalize()
		print("\nWelcome, {} {}!".format(fname.capitalize(), lname.upper()))
		print("\nYour assigned Password is \"{}\"\n".format(password))
		
