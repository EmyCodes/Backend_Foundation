for x in range(10):
    print(x)
print("Loop is done!")
print("\n")
for x in range(1, 15, 3):
    print(x)
print("Loop is done!")
print("\n")
for x in "Emmanuel":
    print(f"{x}")
print("\n")
name = ["Emmanuel", "Olamide", "Ogundare"]
for x in name:
    print(x)
print("Loop is done!")
print("\n")
scores = ["A", "C", "", "D"]
# Using Break keyword
for score in scores:
    if score == "":
        print("Incomplete")
        break
    else:
        print(score)
print("Loop is done!")
print("\n")
# Using Continue Keyword
scores = ["A", "C", "", "D"]
for score in scores:
    if score == "":
        print("Incomplete")
    else:
        print(score)
print("Loop is done!")
