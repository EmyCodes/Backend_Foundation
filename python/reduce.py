from functools import reduce
from myAdd import *
numbers = [1, 2, 3, 4, 5]
reduce(my_add, numbers)
reduce(my_add, numbers, 100)
# reduce(my_sum, numbers)
print(reduce(lambda a, b: a+b, numbers))
f = lambda a, b: a*b
print(reduce(f, numbers))
