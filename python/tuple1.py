prices = (12, 34, 78, 93, 32)
search = "12"
if search in prices:
	position = prices.index(search)
else:
	position = "Not Found"
print(position)

