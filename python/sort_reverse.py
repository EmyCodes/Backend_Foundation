import datetime as dt
datelist = []
datelist.append(dt.date(2020, 1, 12))
datelist.append(dt.date(2019, 1, 12))
datelist.append(dt.date(2018, 1, 12))
print(F"{datelist}")
datelist.sort()		# sort() is used to Alphabetize from A-Z and 0-9 in a chronological order
for date in datelist:
	print("{:%m/%d/%Y}\t".format(date))
print("Reverse the order")
datelist.sort(reverse=True)	# To reverse the order from Z-A and 9-0
for date in datelist:
        print("{:%m/%d/%Y}\t".format(date))
print(f"{datelist}")

datelist.reverse()	# reverse() is used to change the order of arrangement in a list and not alphabetizing in chronological order
for date in datelist:
	print("{:%m/%d/%Y}".format(date))

