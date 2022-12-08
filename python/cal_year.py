from datetime import *
grad_date = date(2024, 9, 20)
year, month, day = input("Today's date (yyyy mm dd): ").split()
year = int(year)
month = int(month)
day = int(day)
current_date = date(year, month, day)
diff_in_date = grad_date - current_date
diff_days = diff_in_date.days
print(diff_days)
no_of_year = diff_days//365
days_left = (diff_days%365)//30
print("You graduate in {}years and {}months time".format(no_of_year, days_left))

