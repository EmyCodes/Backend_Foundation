counter = 97
# using while loop
print("While loop for ASCII")
while counter < 123:
    print("{}={}".format(str(counter), chr(counter)))
    counter += 1
# Using for loop
print("For loop for ASCII")
for x in range(97, 123):
    print("{}={}".format(str(x), chr(x)))