def username(fname="Olamide", surname="Ogundare", midname=""):		#Practice function
	"""Docstring here"""
	fname = fname.capitalize()
	surname = surname.capitalize()
	midname = midname.capitalize()
	if len(midname) > 0:
		print("Hey {} {} {}!".format(fname, surname, midname))
	else:
		print("Hey {} {}!".format(fname, surname))

username("Olamide", "OluGBenga", "zipporH")
username()
