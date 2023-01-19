import datetime as dt

class Member:
	free_days = 365

	def __init__(self, username, fullname):
		self.date_joined = dt.date.today()
		self.free_expires = dt.date.today() + dt.timedelta(days = Member.free_days)
	@classmethod
	def setfreedays(cls, days):
		cls.free_days = days
	#	return "{}".format(cls.free_days)
			
	@staticmethod
	def currenttime():
		now = dt.datetime.now()
		return "{:%I:%M %p}".format(now)

Member.setfreedays(365)
wilbur = Member('wblomgren', 'Wilbur')
print(wilbur.date_joined)
print(wilbur.free_expires)
print(Member.currenttime())
