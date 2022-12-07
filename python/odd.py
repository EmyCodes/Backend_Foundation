print("CALCULATING ODD NUMBERS")
odd = []
initial = int(input("Start counting from: "))
endpoint = int(input("End at: "))
for x in range(initial, endpoint, 2):
	if initial%2 == 1:
		odd.append(x+2)
	else:
		odd.append(x+1)
print(odd)
	
