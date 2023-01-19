import datetime as dt

class Member:
	""" Creating a Member class"""

	expiry_date = 365	#Setting Expiry date to Default

	def __init__(self, firstname, lastname):
		"""Initializing the class"""
		self.firstname = firstname
		self.lastname = lastname
		self.expiry_date = dt.date.today() + dt.timedelta(days=self.expiry_date)
		self.secret_code = "" # Default value for Secret Code
	
	def showExpiry(self):
		"""Function that shows Expiry Date"""
		return "Hi {} {}! Your Subscription expires on {}".format(self.firstname, self.lastname, self.expiry_date)

"""
Joe = Member("Joe", "Anybody")
print(Joe.firstname)
print(Joe.lastname)
print(Joe.expiry_date)
"""
# Creating a Child class or Sub Class
class Admin(Member):
	expiry_date = 365.2422 * 100 # Changing the default value as opposed in the Base class

	def __init__(self, firstname, lastname, secret_code):
		"""Inheriting Parent Class Properties"""
		super().__init__(firstname, lastname)
		self.secret_code = secret_code
	def get_status(self):
		"""Function that shows whelther the Member is a regular user or aAdmin """
		return "{} is an Admin".format(self.firstname)

class User(Member):
	"""Creating a Sub class of Member"""
	def get_status(self):
		"""TO check the status of the Member"""
		return "{} is a regular User".format(self.firstname)

admin1 = Admin("Olamide", "Ogundare", "Olam")
user1 = User("Innocent", "Okoye")


print("{} {} {} {}".format(admin1.lastname, admin1.firstname, admin1.secret_code, admin1.expiry_date))
print("{} {} {} {}".format(user1.lastname, user1.firstname, user1.secret_code, user1.expiry_date))

print(admin1.showExpiry())
print(user1.showExpiry())
print(admin1.get_status())
print(user1.get_status())


