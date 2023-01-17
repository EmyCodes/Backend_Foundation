import datetime as dt

class Member:
	"""Create New member"""
	def __init__(self, username, fullname):
		self.username = username
		self.fullname = fullname

		# Default date_joined to today's date
		self.date_joined = dt.datetime.today()
		# Set is_active to True initially
		self.is_active = True

	def show_username_date_joined(self):
		return f"\n{self.fullname} joined Emzip Technologies on {self.date_joined:%m/%d/%y}"

	def activate(self, yesno):
		self.is_active = yesno


new_guy = Member("EmyCodes", "Ogundare Olamide Emmanuel")

"""new_guy_2 = Member("NoccyCodes", "Okoye Innocent")
print(new_guy.show_username_date_joined())
print(new_guy_2.show_username_date_joined()"""

print(new_guy.is_active)

new_guy.activate(False)

print(new_guy.is_active)
