import datetime as dt
auto_today = dt.datetime.today()
man_today = dt.date(2022, 12, 4)
print("Today's date is {} at your location on the map".format(auto_today))
print("Today's date is {} on your computer".format(man_today))
if auto_today == man_today:
	print("Woo! Your timing is Perfect")
else:
	print("Your time is inaccurate. Check your setting and adjust your date. Ok?")
