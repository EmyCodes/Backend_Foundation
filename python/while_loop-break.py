import random
print("Numbers that aren't divisible by 5")
counter = 0
while counter < 10:
    number = random.randint(1, 999)
    if int(number/5) == number/5:
        break
    else:
        print(number)
        counter += 1
print("Loop is done")
