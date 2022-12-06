import math as mt
title = "Quadratic Equation"
print(title.upper())
print("ax2+bx+c")
a = int(input("Enter the coef. of x2: "))
b = int(input("Enter the coef of x: "))
c = int(input("Enter the value of c: "))
D = b - 4*a*c
numerator_1 = -b + float(mt.sqrt(D))
numerator_2 = -b - float(mt.sqrt(D))
denominator = 2*a
formula_1 = numerator_1/denominator
formula_2 = numerator_2/denominator
print(f"x={formula_1} or {formula_2}")
