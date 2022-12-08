people = {
	"Emy":"Emmanauel Ogundare",
	"Inno":"Okoye Innocent",
	"Zip":"Olamide Olugbenga",
	"Timnasco":"Timothy Ogundare",
	"Gina":"Anerouye Regina",
	"Sarstevex":"Olorunsola Stephen"
	}
"""
print(people)
print(len(people))
user1 = people["Zip"]
print(people["Emy"])
print(user1)
"""
people["Emy"] = "Olamide Ogundare Emmanuel"
# To check
check = input("Who're you looking for? ")
check = check.capitalize()
if check in people:
	print("Woohh!!!!  {} is in there already!".format(check))
	print("The user full name is {}.".format(people[check]))
	print("{}={}".format(check, people[check]))
else:
	print("User {} NOT FOUND!".format(check))
print()
for person in people.keys():
	print("{}={}".format(person, people[person]))
print()
for value in people.values():
	print(value)
#	Looping through Dictionary
print()
for person in people:	# To show the keys
	print(person)
print()
for value in people:
	print(people[value])

