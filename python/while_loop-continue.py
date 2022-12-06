import random
print("Odd Number")
counter = 0
while counter < 10:
    number = random.randint(1, 999)
    if int(number/2) == number/2:
        continue
    else:
        print(number)
        counter += 1
print("All done!")
