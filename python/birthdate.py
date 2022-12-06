import datetime as dt
year, month, day = input("Enter your Birthdate in this form (yyyy mm dd): ").split()
year =int(year)
month = int(month)
day = int(day)
today = dt.date.today()
actual_date = dt.date(year, month, day)
day_diff = today - actual_date
days = day_diff.days
year_old = days//365
cal_month = (days%365)//30
# print(month)
print(f"You are {year_old}years and {cal_month}months old today")
print("You are born in {}".format(year))
