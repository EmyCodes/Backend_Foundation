list1 = [12, 13, 15, 16]
list2 = [17, 18, 19, 20]
# list1.extend(list2)
# list2[2] = 30
list1.insert(2, 1000)
letters = ["A", "B", "C", "D", "D", "D"]
# for letter in letters:
#     if letter is "D":
#         letter.remove
#         print(letter)
# letters.remove("D")
for letter in letters:
    letter.remove("D")
    print(letter)
print(letters)
# print(list1)
