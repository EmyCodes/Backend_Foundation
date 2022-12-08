combs = []
for x in [1, 2, 3]:
	for y in [3, 1, 4]:
	#	combs.append((x, y))
	#	print(combs)
		if x is not y:
			combs.append((x, y))
print(combs)
