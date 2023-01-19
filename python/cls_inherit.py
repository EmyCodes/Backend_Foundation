import datetime as dt

class Member:
	expiry_date = 365

	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
		self.expiry_date = dt.date.today() + dt.timedelta(days=self.expiry_date)
		self.secret_code = ""
	
	def showExpiry(self):
		return "Hi {} {}! Your Subscription expires on {}".format(self.firstname, self.lastname, self.expiry_date)
"""
Joe = Member("Joe", "Anybody")
print(Joe.firstname)
print(Joe.lastname)
print(Joe.expiry_date)
"""

class Admin(Member):
	expiry_date = 365.2422 * 100

	def __init__(self, firstname, lastname, secret_code):
		super().__init__(firstname, lastname)
		self.secret_code = secret_code

class User(Member):
	pass

admin1 = Admin("Olamide", "Ogundare", "Olam")
user1 = User("Innocent", "Okoye")


print("{} {} {} {}".format(admin1.lastname, admin1.firstname, admin1.secret_code, admin1.expiry_date))
print("{} {} {} {}".format(user1.lastname, user1.firstname, user1.secret_code, user1.expiry_date))

print(admin1.showExpiry())
print(user1.showExpiry())
