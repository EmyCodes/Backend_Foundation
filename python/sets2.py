a = {x for x in "abracadabra" if x not in "abc"}
print(a)

for x in "abracadabra":
	if x not in "abc":
		a = set(x)
		print(a)
