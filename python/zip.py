questions = ["name", "age", "level"]
answers = ["Emmanuel", 30, 500]
# To loop over two or more sequences at the same time, the entries can be paired with the zip() function
for q, a in zip(questions, answers):
	print("What is your {0}? {1}".format(q, a))
