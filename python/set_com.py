# Set Comprehension
x = {num for num in range(10)}
y = {alpha.strip() for alpha in "Hello World"}
z = {num**2 for num in x}
zz = {num**2 for num in x if num%2 != 0}	# This expression print odd numbers
print(x)
print(y)
print(z)
print(zz)
